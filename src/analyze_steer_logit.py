"""Natural-dose steering (alpha in {-2,-1,1,2}) against 32 fresh random directions; logit readouts.
Per (model, layer, direction, outcome): slope = change in the outcome per natural human->LLM unit
(least squares through the origin over the four doses), compared with the slopes of the random directions.
Writes results/tables/steer_logit_slopes.csv and figures/fig6_steering_natural_dose.png."""
import sys
from pathlib import Path
import numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score
sys.path.insert(0, str(Path(__file__).parent))
from stats_util import *
T = RES / "tables"; rows = []; val = []
sig = lambda x: 1 / (1 + np.exp(-x))
for m in LOCAL:
    f = RES / m / "steer_logit_raw.csv"
    if not f.exists(): continue
    d = pd.read_csv(f)
    d["p"] = sig(d.value)  # syco_opinion: P(matching option); refusal_tok: P(first token is "I")
    base = d[d.direction == "none"].set_index(["task", "sid"])
    # validity of the refusal-token proxy: does it predict the scored refusal of the unsteered generated response?
    s = pd.read_json(RES / m / "steer_scored.jsonl", lines=True)
    s = s[(s.direction == "none") & (s.task == "refusal")].set_index("sid")
    b = base.loc["refusal_tok"].join(s.label)
    val.append(dict(model=m, auc_refusal_tok_vs_scored_refusal=roc_auc_score(b.label == "REFUSE", b.value), base_p_I=b.p.mean(), base_refusal_rate=(b.label == "REFUSE").mean(),
                    base_p_match=base.loc["syco_opinion"].p.mean()))
    for (L, task), g in d[d.direction != "none"].groupby(["layer", "task"]):
        bb = base.loc[task]
        for scale in ["p", "value"]:
            w = g.pivot_table(index="sid", columns=["direction", "alpha"], values=scale).sub(bb[scale], axis=0)  # per-item change vs unsteered
            al = np.array(sorted(g.alpha.unique()), float)
            sl = {k: (w[k][al].values @ al) / (al @ al) for k in w.columns.levels[0]}       # per-item slope per unit dose
            ev = {k: w[k][al].values.mean(1) for k in sl}                                    # sign-independent part
            rnd = np.array([v.mean() for k, v in sl.items() if k[:3] in ("iso", "cov")])
            for k in ["auth", "len", "eval", "refusal"]:
                bt = boot(sl[k], n=4000)
                rows.append(dict(model=m, layer=L, outcome=task, scale={"p": "prob", "value": "logit"}[scale], direction=k, slope=bt["mean"], lo=bt["lo"], hi=bt["hi"],
                                 even=ev[k].mean(), rand_sd=rnd.std(ddof=1), rand_abs_mean=np.abs(rnd).mean(), rand_abs_max=np.abs(rnd).max(), n_rand=len(rnd),
                                 rand_even_mean=np.mean([ev[r].mean() for r in sl if r[:3] in ("iso", "cov")]),
                                 p_emp=(1 + (np.abs(rnd) >= abs(bt["mean"])).sum()) / (1 + len(rnd)), rand_slopes=";".join(f"{x:.5f}" for x in rnd)))
tab = pd.DataFrame(rows); tab.drop(columns="rand_slopes").to_csv(T / "steer_logit_slopes.csv", index=False)
pd.DataFrame(val).to_csv(T / "steer_logit_validity.csv", index=False)
pd.set_option("display.width", 250); print(pd.DataFrame(val).round(3).to_string()); print(tab.drop(columns="rand_slopes").round(4).to_string())

pr = tab[tab.scale == "prob"]; models = list(pr.model.unique())
fig, axes = plt.subplots(2, len(models), figsize=(5.2 * len(models), 5.6), squeeze=False)
for j, m in enumerate(models):
    for i, (oc, title) in enumerate([("refusal_tok", "Refusal token: P(first token = 'I')"), ("syco_opinion", "Opinion sycophancy: P(matching option)")]):
        ax = axes[i, j]; g = pr[(pr.model == m) & (pr.outcome == oc)]; layers = sorted(g.layer.unique())
        for x, L in enumerate(layers):
            gl = g[g.layer == L].set_index("direction")
            rnd = 100 * np.array(gl.loc["auth", "rand_slopes"].split(";"), float)
            ax.scatter(x + RNG.uniform(-0.12, 0.12, len(rnd)), rnd, s=10, color="0.7", zorder=1, label="random (16 iso + 16 cov)" if x == 0 else None)
            for k, col, mk, dx in [("len", "tab:green", "s", 0.2), ("eval", "tab:purple", "D", 0.27), ("refusal", "tab:orange", "^", 0.34)]:
                ax.scatter(x + dx, 100 * gl.loc[k, "slope"], s=22, color=col, marker=mk, zorder=2, label=k if x == 0 else None)
            a = gl.loc["auth"]
            ax.errorbar(x - 0.25, 100 * a.slope, yerr=[[100 * (a.slope - a.lo)], [100 * (a.hi - a.slope)]], fmt="o", color="tab:red", capsize=3, zorder=3, label="authorship" if x == 0 else None)
        ax.axhline(0, color="k", lw=0.6); ax.set_xticks(range(len(layers))); ax.set_xticklabels([f"layer {L}" for L in layers])
        ax.set_title(f"{NAMES[m]}\n{title}", fontsize=9); ax.set_ylabel("pp per natural unit", fontsize=8); ax.tick_params(labelsize=8)
axes[0, 0].legend(fontsize=7)
plt.suptitle("Steering on fixed text at natural doses (±1, ±2): change per natural human→LLM unit, authorship direction vs norm-matched random directions", fontsize=10)
plt.tight_layout(); plt.savefig(ROOT / "figures/fig6_steering_natural_dose.png", dpi=160); plt.close()
