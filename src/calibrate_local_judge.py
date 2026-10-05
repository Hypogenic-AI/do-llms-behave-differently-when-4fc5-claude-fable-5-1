"""Calibrate the local Llama judge against the API judge on steered outputs, then label the rows the API judge never reached.
(OpenRouter credits ran out after the API judge had labelled about half of the Qwen steering outputs.)

Features: the local judge's option log-probabilities (src/local_judge_logits.py).  A logistic regression per task maps them
to the API judge's label; it is fitted on half of the items (split by seed id) and evaluated on the other half.
Output results/<key>/steer_judged.jsonl with
  label       : API label where cached, calibrated local label otherwise
  label_local : calibrated local label wherever local logits exist (incl. all unsteered rows)
  scorer      : "api" or "local"
and results/tables/local_judge_calibration_<key>.csv.   Usage: python src/calibrate_local_judge.py qwen"""
import sys
from pathlib import Path
import numpy as np, pandas as pd
from sklearn.linear_model import LogisticRegression
sys.path.insert(0, str(Path(__file__).parent))
from stats_util import RES
from local_judge import OPTS
key = sys.argv[1]; out = RES / key
GEN = ["refusal", "accuracy", "syco_fact"]; KEY = {"refusal": "REFUSE", "accuracy": "CORRECT", "syco_fact": "WRONG_SUGGESTED"}
df = pd.read_json(out / "steer_judged_api_cached.jsonl", lines=True)
lg = pd.concat([pd.read_parquet(out / "steer_judge_logits_llama.parquet"), pd.read_parquet(out / "steer_judge_logits_llama_none.parquet")]).drop_duplicates(["task", "sid", "response"])
d = df.merge(lg, on=["task", "sid", "response"], how="left")
assert len(d) == len(df)
gen = d.task.isin(GEN); api_ok = gen & ~d.label.isin(["UNPARSED"]); has_lg = gen & d.l0.notna()
rng = np.random.default_rng(0); rows = []
d["label_local"] = None
for t in GEN:
    opts = OPTS["refusal" if t == "refusal" else "trivia"]; cols = ["l0", "l1", "l2"][:len(opts)]
    X = lambda m: d.loc[m, cols].values - d.loc[m, cols].values[:, -1:]
    cal = api_ok & has_lg & (d.task == t) & d.label.isin(opts)
    sids = d[cal].sid.unique(); tr_s = set(rng.choice(sids, len(sids) // 2, replace=False))
    tr = cal & d.sid.isin(tr_s); te = cal & ~d.sid.isin(tr_s)
    clf = LogisticRegression(C=10, max_iter=2000).fit(X(tr), d.loc[tr, "label"])
    raw = np.array(opts)[d.loc[te, cols].values.argmax(1)]; calp = clf.predict(X(te)); y = d.loc[te, "label"].values
    k = KEY[t]
    for nm, m_ in [("all held-out", np.ones(len(y), bool)), ("unsteered", (d.loc[te, "direction"] == "none").values), ("|alpha|<=2", (d.loc[te, "alpha"].abs().between(1, 2)).values),
                   ("|alpha|=4", (d.loc[te, "alpha"].abs() == 4).values), ("|alpha|=8", (d.loc[te, "alpha"].abs() == 8).values),
                   ("authorship dir", (d.loc[te, "direction"] == "auth").values), ("random dirs", d.loc[te, "direction"].str.match("iso|cov").values)]:
        if m_.sum() < 20: continue
        rows.append(dict(task=t, subset=nm, n=int(m_.sum()), api_rate=(y[m_] == k).mean(), raw_rate=(raw[m_] == k).mean(), cal_rate=(calp[m_] == k).mean(),
                         agree_raw=((y[m_] == k) == (raw[m_] == k)).mean(), agree_cal=((y[m_] == k) == (calp[m_] == k)).mean()))
    clf = LogisticRegression(C=10, max_iter=2000).fit(X(cal), d.loc[cal, "label"])   # final model: all calibration rows
    m = has_lg & (d.task == t); d.loc[m, "label_local"] = clf.predict(X(m))
tab = pd.DataFrame(rows); tab.to_csv(RES / "tables" / f"local_judge_calibration_{key}.csv", index=False)
pd.set_option("display.width", 200); print(tab.round(3).to_string())
d["scorer"] = np.where(api_ok, "api", np.where(gen, "local", None))
need = gen & ~api_ok
d.loc[need, "label"] = d.loc[need, "label_local"].where(d.loc[need, "label_local"].notna(), "EMPTY")
print(d[gen].groupby("scorer").label.value_counts(dropna=False))
d.drop(columns=["l0", "l1", "l2"]).to_json(out / "steer_judged.jsonl", orient="records", lines=True)
