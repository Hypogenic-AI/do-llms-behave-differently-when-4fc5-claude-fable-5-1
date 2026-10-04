"""Shared loading, outcome coding, 2x2 contrasts and resampling statistics."""
import json, re
from pathlib import Path
import numpy as np, pandas as pd
ROOT = Path(__file__).resolve().parent.parent
RES = ROOT / "results"
LOCAL = ["llama", "qwen"]; API = ["luna", "sonnet", "gemini"]
NAMES = {"llama": "Llama-3.1-8B-Instruct", "qwen": "Qwen2.5-7B-Instruct", "luna": "GPT-5.6-luna",
         "sonnet": "Claude-Sonnet-5.5", "gemini": "Gemini-3.8-flash"}
CONDS = ["H_s", "H_l", "L_s", "L_l"]
RNG = np.random.default_rng(0)

POLITE = re.compile(r"\b(please|pls|plz|could you|would you|can you|kindly|thank|thanks|thx|i would appreciate|i'd appreciate)\b", re.I)

def surface(text):
    """Surface descriptors of a prompt body."""
    words = text.split()
    letters = [c for c in text if c.isalpha()]
    return dict(n_words=len(words), n_chars=len(text), log_words=np.log(max(len(words), 1)),
                polite=float(bool(POLITE.search(text))),
                lower_start=float(text[:1].islower()),
                end_punct=float(text.rstrip()[-1:] in ".?!"),
                upper_frac=np.mean([c.isupper() for c in letters]) if letters else 0.0,
                apostrophe_free_contraction=float(bool(re.search(r"\b(im|dont|cant|its|ive|thats|whats|doesnt|isnt|hes|shes|theyre|youre)\b", text))),
                mean_word_len=np.mean([len(w) for w in words]) if words else 0.0)

def load_behaviour(model, empty_as_refusal=False, string_scorer=False):
    """Long table with one numeric outcome column `y` per (task, sid, rewriter, cond)."""
    df = pd.read_json(RES / model / "behaviour_judged.jsonl", lines=True)
    # responses that are empty / API errors / unjudgeable are treated as missing, which drops that item's set
    if string_scorer:  # re-label generated responses with the rule-based scorer (src/string_judge.py)
        from string_judge import label as _sl
        g = df.task.isin(["refusal", "accuracy", "syco_fact"])
        df.loc[g, "label"] = [_sl(t, s_, r) for t, s_, r in zip(df[g].task, df[g].sid, df[g].response)]
    # (sensitivity option: count an empty response to a refusal-task item as a provider-level refusal)
    if empty_as_refusal:
        df.loc[(df.task == "refusal") & (df.label == "EMPTY"), "label"] = "REFUSE"
    df = df[~df.label.isin(["EMPTY", "UNPARSED"]) & (df.response.fillna("") != "__API_ERROR__")]
    rows = []
    for task, d in df.groupby("task"):
        d = d.copy()
        if task == "refusal":
            d["y"] = (d.label == "REFUSE").astype(float); d["outcome"] = "refusal"
            rows.append(d)
        elif task == "accuracy":
            d["y"] = (d.label == "CORRECT").astype(float); d["outcome"] = "accuracy"
            rows.append(d)
        elif task == "syco_fact":
            d["y"] = (d.label == "WRONG_SUGGESTED").astype(float); d["outcome"] = "syco_fact"
            rows.append(d)
            e = d.copy(); e["y"] = (e.label == "CORRECT").astype(float); e["outcome"] = "acc_under_suggestion"
            rows.append(e)
        elif task == "syco_opinion":
            if "syco_logit" in d and d.syco_logit.notna().any():
                d["y"] = 1 / (1 + np.exp(-d.syco_logit))  # P(match | A or B)
            else:
                d["y"] = d.syco_match
            d["outcome"] = "syco_opinion"
            rows.append(d)
    out = pd.concat(rows, ignore_index=True)
    return out[["task", "outcome", "subset", "sid", "rewriter", "cond", "y", "text"]]

def cells(df, value="y"):
    """Wide table indexed by (sid, rewriter) with the four 2x2 cells; only complete sets."""
    w = df[df.cond.isin(CONDS)].pivot_table(index=["sid", "rewriter"], columns="cond", values=value, aggfunc="first")
    return w.reindex(columns=CONDS).dropna()

def contrasts(w):
    """Per (sid, rewriter) contrasts from the 2x2 cells."""
    c = pd.DataFrame(index=w.index)
    c["style"] = 0.5 * ((w.L_s - w.H_s) + (w.L_l - w.H_l))      # LLM style minus human style
    c["length"] = 0.5 * ((w.H_l - w.H_s) + (w.L_l - w.L_s))     # long minus short
    c["interaction"] = (w.L_l - w.H_l) - (w.L_s - w.H_s)
    c["style_at_short"] = w.L_s - w.H_s
    c["style_at_long"] = w.L_l - w.H_l
    c["natural"] = w.L_l - w.H_s                                  # unmatched "naive" comparison
    return c

def boot(x, n=10000):
    """Mean, bootstrap 95% CI and sign-flip permutation p for a vector of per-seed contrasts."""
    x = np.asarray(x, float); x = x[~np.isnan(x)]
    if len(x) == 0: return dict(mean=np.nan, lo=np.nan, hi=np.nan, p=np.nan, n=0, dz=np.nan)
    m = x.mean()
    bs = x[RNG.integers(0, len(x), (n, len(x)))].mean(1)
    perm = (x * RNG.choice([-1, 1], (n, len(x)))).mean(1)
    p = (np.sum(np.abs(perm) >= abs(m) - 1e-12) + 1) / (n + 1)
    sd = x.std(ddof=1) if len(x) > 1 else np.nan
    return dict(mean=m, lo=np.percentile(bs, 2.5), hi=np.percentile(bs, 97.5), p=p, n=len(x), dz=m / sd if sd and sd > 0 else 0.0)

def seed_level(c):
    """Average the per-(sid, rewriter) contrasts over rewriters -> one row per seed (the cluster)."""
    return c.groupby(level="sid").mean()

def holm(ps):
    ps = np.asarray(ps, float); order = np.argsort(ps); adj = np.empty(len(ps)); running = 0
    for rank, i in enumerate(order):
        running = max(running, (len(ps) - rank) * ps[i]); adj[i] = min(1.0, running)
    return adj
