"""Naive (content-uncontrolled) comparison: free LLM rewrite `L_free` vs human-style `H_s`, set against the
content-controlled contrasts on the same seeds."""
import sys
from pathlib import Path
import numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
sys.path.insert(0, str(Path(__file__).parent))
from stats_util import *
T = RES / "tables"; F = ROOT / "figures"
models = [m for m in LOCAL + API if (RES / m / "free_judged.jsonl").exists() and (RES / m / "behaviour_judged.jsonl").exists()]
rows = []
for m in models:
    f = pd.read_json(RES / m / "free_judged.jsonl", lines=True)
    f = f[~f.get("label", pd.Series(index=f.index, dtype=object)).isin(["EMPTY", "UNPARSED"])]
    parts = []
    for task, d in f.groupby("task"):
        d = d.copy()
        if task == "refusal": d["y"] = (d.label == "REFUSE").astype(float); d["outcome"] = "refusal"; parts.append(d)
        elif task == "accuracy": d["y"] = (d.label == "CORRECT").astype(float); d["outcome"] = "accuracy"; parts.append(d)
        elif task == "syco_fact": d["y"] = (d.label == "WRONG_SUGGESTED").astype(float); d["outcome"] = "syco_fact"; parts.append(d)
        else:
            d["y"] = 1 / (1 + np.exp(-d.syco_logit)) if "syco_logit" in d and d.syco_logit.notna().any() else d.syco_match
            d["outcome"] = "syco_opinion"; parts.append(d)
    f = pd.concat(parts)[["outcome", "sid", "rewriter", "y"]].rename(columns={"y": "L_free"})
    b = load_behaviour(m)  # both arms scored by the API judge
    for oc in ["refusal", "syco_fact", "syco_opinion", "accuracy"]:
        w = cells(b[b.outcome == oc]).reset_index().merge(f[f.outcome == oc], on=["sid", "rewriter"]).dropna(subset=["L_free"]).set_index(["sid", "rewriter"])
        c = pd.DataFrame({"naive: L_free - H_s": w.L_free - w.H_s, "controlled natural: L_l - H_s": w.L_l - w.H_s,
                          "controlled style (2x2)": 0.5 * ((w.L_s - w.H_s) + (w.L_l - w.H_l))})
        cs = c.groupby(level="sid").mean()
        for k in c.columns:
            rows.append(dict(model=m, outcome=oc, contrast=k, H_s=w.H_s.mean(), L_l=w.L_l.mean(), L_free=w.L_free.mean(), **boot(cs[k])))
        for rw in ["gpt", "claude"]:
            cr = c.xs(rw, level="rewriter")
            rows.append(dict(model=m, outcome=oc, contrast=f"naive: L_free - H_s [rewriter={rw}]", **boot(cr["naive: L_free - H_s"])))
tab = pd.DataFrame(rows); tab.to_csv(T / "naive_vs_controlled.csv", index=False)
pd.set_option("display.width", 250); print(tab.round(4).to_string())

ocs = ["refusal", "syco_fact", "syco_opinion", "accuracy"]
fig, axes = plt.subplots(1, 4, figsize=(15, 3.8), sharey=True)
for ax, oc in zip(axes, ocs):
    for j, (k, col) in enumerate([("naive: L_free - H_s", "tab:red"), ("controlled natural: L_l - H_s", "tab:blue"), ("controlled style (2x2)", "k")]):
        g = tab[(tab.outcome == oc) & (tab.contrast == k)].set_index("model").reindex(models)
        y = np.arange(len(models)) + (j - 1) * 0.22
        ax.errorbar(100 * g["mean"], y, xerr=[100 * (g["mean"] - g.lo), 100 * (g.hi - g["mean"])], fmt="o", color=col, capsize=2, label=k)
    ax.axvline(0, color="k", lw=0.7); ax.set_title(oc); ax.set_yticks(range(len(models))); ax.set_yticklabels([NAMES[m] for m in models], fontsize=8)
    ax.set_xlabel("difference (pp), 95% CI")
axes[0].invert_yaxis(); axes[-1].legend(fontsize=7)
plt.suptitle("Uncontrolled LLM rewrite vs content-controlled contrasts (same seeds)", fontsize=10)
plt.tight_layout(); plt.savefig(F / "fig5_naive_vs_controlled.png", dpi=160); plt.close()
