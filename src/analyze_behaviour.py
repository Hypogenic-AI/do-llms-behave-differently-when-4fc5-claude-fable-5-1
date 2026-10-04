"""D1/D2 analysis: manipulation check, 2x2 style x length contrasts, explicit-label arm, surface features.
Writes CSV tables to results/tables/ and figures to figures/."""
import json, sys
from pathlib import Path
import numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score
sys.path.insert(0, str(Path(__file__).parent))
from stats_util import *
T = RES / "tables"; T.mkdir(exist_ok=True); F = ROOT / "figures"; F.mkdir(exist_ok=True)
models = [m for m in LOCAL + API if (RES / m / "behaviour_judged.jsonl").exists()]
print("models:", models)
OUTCOMES = ["refusal", "syco_fact", "syco_opinion", "accuracy", "acc_under_suggestion"]

# ---------------- stimulus descriptives ----------------
stim = pd.read_json(ROOT / "data/stimuli.jsonl", lines=True)
stim = stim[stim.audit_ok]
sf = pd.DataFrame([surface(b) for b in stim.body]); sf.index = stim.index
stim = pd.concat([stim, sf], axis=1)
desc = stim.groupby(["task", "cond"])[["n_words", "polite", "lower_start", "end_punct", "apostrophe_free_contraction", "mean_word_len"]].mean().round(3)
desc.to_csv(T / "stimulus_surface_features.csv"); print(desc.to_string())
aud = pd.read_json(ROOT / "data/stimuli.jsonl", lines=True)
aud = aud[aud.rewriter != "none"].groupby(["task", "subset", "rewriter", "sid"]).audit_ok.all().reset_index()
aud.groupby(["task", "subset", "rewriter"]).audit_ok.agg(kept="sum", total="size").to_csv(T / "audit_retention.csv")

# ---------------- manipulation check: perceived authorship ----------------
rows = []; percell = []
for m in models:
    s = pd.read_json(RES / m / "stimuli_scored.jsonl", lines=True)
    s = s[s.judge_ai.notna()]
    for task, d in s.groupby("task"):
        c = seed_level(contrasts(cells(d, "judge_ai")))
        for k in ["style", "length", "style_at_short", "style_at_long"]:
            rows.append(dict(model=m, task=task, contrast=k, **boot(c[k])))
        w = cells(d, "judge_ai")
        auc = roc_auc_score(np.r_[np.zeros(2 * len(w)), np.ones(2 * len(w))], np.r_[w.H_s, w.H_l, w.L_s, w.L_l])
        auc_short = roc_auc_score(np.r_[np.zeros(len(w)), np.ones(len(w))], np.r_[w.H_s, w.L_s])
        cm = d.groupby("cond").judge_ai.mean()
        percell.append(dict(model=m, task=task, auc_L_vs_H=auc, auc_L_vs_H_short=auc_short, **cm.to_dict()))
        if task == "wildchat":  # real human originals vs rewrites
            o = d[d.cond == "orig"].judge_ai
            for cnd in CONDS:
                x = d[d.cond == cnd].judge_ai
                percell[-1][f"auc_{cnd}_vs_realhuman"] = roc_auc_score(np.r_[np.zeros(len(o)), np.ones(len(x))], np.r_[o, x])
mc = pd.DataFrame(rows); mc.to_csv(T / "manipulation_check_contrasts.csv", index=False)
pc = pd.DataFrame(percell); pc.to_csv(T / "manipulation_check_cells.csv", index=False)
print(pc.round(2).to_string()); print(mc[mc.contrast.isin(["style", "length"])].round(3).to_string())

# ---------------- behaviour: 2x2 contrasts ----------------
rows = []; cellrows = []; labrows = []; perseed = {}
for m in models:
    b = load_behaviour(m)
    for oc in OUTCOMES:
        d = b[b.outcome == oc]
        if d.y.notna().sum() == 0: continue
        w = cells(d)
        c = contrasts(w); perseed[(m, oc)] = c
        cm = d.groupby("cond").y.mean()
        cellrows.append(dict(model=m, outcome=oc, n_sets=len(w), **{k: w[k].mean() for k in CONDS}, orig=cm.get("orig"),
                             label_ai=cm.get("label_ai"), label_human=cm.get("label_human")))
        for k in c.columns:
            rows.append(dict(model=m, outcome=oc, scope="all", contrast=k, **boot(seed_level(c)[k])))
        for rw in ["gpt", "claude"]:  # per-rewriter robustness
            cr = c.xs(rw, level="rewriter")
            for k in ["style", "length"]:
                rows.append(dict(model=m, outcome=oc, scope=f"rewriter={rw}", contrast=k, **boot(cr[k])))
        if oc == "refusal":  # per subset (headroom)
            sub = d.drop_duplicates("sid").set_index("sid").subset
            for sname in sub.unique():
                cs = seed_level(c); cs = cs[cs.index.map(sub) == sname]
                ws = w[w.index.get_level_values("sid").map(sub) == sname]
                rows.append(dict(model=m, outcome=oc, scope=f"subset={sname}", contrast="style", **boot(cs["style"])))
                rows.append(dict(model=m, outcome=oc, scope=f"subset={sname}", contrast="length", **boot(cs["length"])))
                cellrows.append(dict(model=m, outcome=f"refusal[{sname}]", n_sets=len(ws), **{k: ws[k].mean() for k in CONDS},
                                     orig=d[(d.cond == "orig") & (d.subset == sname)].y.mean()))
        # explicit-label arm (identical text)
        lw = d[d.cond.isin(["orig", "label_ai", "label_human"])].pivot_table(index="sid", columns="cond", values="y").dropna()
        for k, v in {"label_ai - label_human": lw.label_ai - lw.label_human, "label_ai - none": lw.label_ai - lw.orig,
                     "label_human - none": lw.label_human - lw.orig}.items():
            labrows.append(dict(model=m, outcome=oc, contrast=k, **boot(v)))
con = pd.DataFrame(rows); cel = pd.DataFrame(cellrows); lab = pd.DataFrame(labrows)
prim = (con.scope == "all") & (con.contrast == "style") & con.outcome.isin(["refusal", "syco_fact", "syco_opinion", "accuracy"])
con.loc[prim, "p_holm"] = holm(con.loc[prim, "p"])
pl = (lab.contrast == "label_ai - label_human") & lab.outcome.isin(["refusal", "syco_fact", "syco_opinion", "accuracy"])
lab.loc[pl, "p_holm"] = holm(lab.loc[pl, "p"])
con.to_csv(T / "behaviour_contrasts.csv", index=False); cel.to_csv(T / "behaviour_cell_means.csv", index=False)
lab.to_csv(T / "label_arm.csv", index=False)
pd.set_option("display.width", 250)
print(cel.round(3).to_string())
print(con[(con.scope == "all") & con.contrast.isin(["style", "length", "style_at_short", "natural"])].round(4).to_string())
print(lab.round(4).to_string())

# ---------------- secondary outcomes: form of the response (trivia accuracy items; nothing to refuse) ----------------
import re as _re
def form(resp):
    a = [c for c in resp if c.isalpha()]
    return dict(resp_words=len(resp.split()), resp_markdown=float(bool(_re.search(r"\*\*|^#|^\s*[-*] |^\s*\d+\. ", resp, _re.M))),
                resp_lower_start=float(a[0].islower()) if a else np.nan)
frow = []
for m in models:
    r = pd.read_json(RES / m / "behaviour_judged.jsonl", lines=True)
    r = r[(r.task == "accuracy") & r.response.notna() & (r.response != "") & (r.response != "__API_ERROR__")]
    r = pd.concat([r.reset_index(drop=True), pd.DataFrame([form(x) for x in r.response])], axis=1)
    for oc in ["resp_words", "resp_markdown", "resp_lower_start"]:
        w = cells(r, oc); c = seed_level(contrasts(w))
        frow.append(dict(model=m, outcome=oc, **{k: w[k].mean() for k in CONDS}, **{f"style_{k}": v for k, v in boot(c["style"]).items()},
                         **{f"length_{k}": v for k, v in boot(c["length"]).items()}))
form_tab = pd.DataFrame(frow); form_tab.to_csv(T / "response_form.csv", index=False); print(form_tab.round(3).to_string())

# ---------------- sensitivity: empty responses on refusal items counted as provider-level refusals ----------------
srow = []
for m in models:
    b = load_behaviour(m, empty_as_refusal=True); c = seed_level(contrasts(cells(b[b.outcome == "refusal"])))
    for k in ["style", "length"]: srow.append(dict(model=m, contrast=k, **boot(c[k])))
    r = pd.read_json(RES / m / "behaviour_judged.jsonl", lines=True); r = r[r.task == "refusal"]
    canned = r.response.fillna("").str.startswith("I'm sorry, but I cannot assist with that request.") | (r.response.fillna("") == "")
    srow.append(dict(model=m, contrast="n_filter_like_responses_H", mean=int(canned[r.cond.isin(["H_s", "H_l"])].sum())))
    srow.append(dict(model=m, contrast="n_filter_like_responses_L", mean=int(canned[r.cond.isin(["L_s", "L_l"])].sum())))
pd.DataFrame(srow).to_csv(T / "refusal_sensitivity_empty_as_refusal.csv", index=False); print(pd.DataFrame(srow).round(4).to_string())

# ---------------- pooled across models (seed x model clusters -> mean over models per seed) ----------------
pool = []
for oc in OUTCOMES:
    cs = [seed_level(perseed[(m, oc)]) for m in models if (m, oc) in perseed]
    allc = pd.concat(cs).groupby(level="sid").mean()
    for k in ["style", "length", "style_at_short"]:
        pool.append(dict(outcome=oc, contrast=k, n_models=len(cs), **boot(allc[k])))
pool = pd.DataFrame(pool); pool.to_csv(T / "behaviour_contrasts_pooled.csv", index=False); print(pool.round(4).to_string())

# ---------------- figures ----------------
fig, axes = plt.subplots(1, 2, figsize=(13, 4.6), sharey=True)
ocs = ["refusal", "syco_fact", "syco_opinion", "accuracy"]
labels = {"refusal": "Refusal rate", "syco_fact": "Factual sycophancy\n(endorses wrong suggestion)", "syco_opinion": "Opinion sycophancy\n(P match user view)", "accuracy": "Trivia accuracy"}
colors = plt.cm.tab10(np.arange(len(models)))
for ax, k, title in zip(axes, ["style", "length"], ["Style effect: LLM-style minus human-style (length-balanced)", "Length effect: long minus short (style-balanced)"]):
    for j, m in enumerate(models):
        for i, oc in enumerate(ocs):
            r = con[(con.model == m) & (con.outcome == oc) & (con.scope == "all") & (con.contrast == k)]
            if r.empty: continue
            r = r.iloc[0]; ypos = i + (j - (len(models) - 1) / 2) * 0.15
            ax.errorbar(100 * r["mean"], ypos, xerr=[[100 * (r["mean"] - r.lo)], [100 * (r.hi - r["mean"])]], fmt="o", color=colors[j],
                        capsize=3, label=NAMES[m] if i == 0 else None)
    ax.axvline(0, color="k", lw=0.8); ax.set_yticks(range(len(ocs))); ax.set_yticklabels([labels[o] for o in ocs])
    ax.set_xlabel("Within-item difference (percentage points), 95% bootstrap CI"); ax.set_title(title, fontsize=10); ax.invert_yaxis()
axes[1].legend(fontsize=8, loc="lower right")
plt.tight_layout(); plt.savefig(F / "fig2_behaviour_contrasts.png", dpi=160); plt.close()

fig, axes = plt.subplots(1, len(models), figsize=(3.3 * len(models), 3.6))
for ax, m in zip(np.atleast_1d(axes), models):
    s = pd.read_json(RES / m / "stimuli_scored.jsonl", lines=True)
    g = s[s.task == "wildchat"].groupby("cond").judge_ai; order = ["orig", "H_s", "H_l", "L_s", "L_l"]
    mu = g.mean().reindex(order); se = g.sem().reindex(order)
    ax.bar(range(5), mu, yerr=1.96 * se, color=["#555", "#2a7", "#2a7", "#c53", "#c53"], capsize=3)
    g2 = s[s.task != "wildchat"].groupby("cond").judge_ai.mean().reindex(order)
    ax.plot(range(5), g2, "kD", ms=5, label="benchmark items")
    ax.set_xticks(range(5)); ax.set_xticklabels(["real\nhuman", "H\nshort", "H\nlong", "LLM\nshort", "LLM\nlong"], fontsize=8)
    ax.set_title(NAMES[m], fontsize=9); ax.set_ylabel("perceived 'AI-written'\n(" + ("logit AI - Human" if m in LOCAL else "0-100 rating") + ")", fontsize=8)
    ax.legend(fontsize=7)
plt.suptitle("Manipulation check: responder's own judgment of authorship (bars: WildChat items)", fontsize=10)
plt.tight_layout(); plt.savefig(F / "fig1_manipulation_check.png", dpi=160); plt.close()
print("saved")
