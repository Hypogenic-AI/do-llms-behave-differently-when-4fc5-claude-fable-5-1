"""Steering analysis: effect of adding the authorship direction on fixed prompt text, against random,
length, eval-awareness and refusal directions.  Usage: python src/analyze_steer.py {llama|qwen} [rule]
Default scorer: API judge (steer_judged.jsonl).  `rule`: rule-based scorer (steer_scored.jsonl), tables/figure get the suffix _rule."""
import json, sys
from pathlib import Path
import numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
sys.path.insert(0, str(Path(__file__).parent))
from stats_util import *
key = sys.argv[1]; out = RES / key; T = RES / "tables"; F = ROOT / "figures"
RULE = len(sys.argv) > 2 and sys.argv[2] == "rule"; SUF = "_rule" if RULE else ""  # suffix only when the rule scorer is requested explicitly
RULE = RULE or not (out / "steer_judged.jsonl").exists()   # Llama: only the rule-based scores exist (validated against cached API labels)
df = pd.read_json(out / ("steer_scored.jsonl" if RULE else "steer_judged.jsonl"), lines=True)
cfg = json.load(open(out / "steer_config.json"))
# outcome coding (missing if the judge could not label)
parts = []
g = df[df.task == "refusal"].copy(); g["y"] = np.where(g.label.isin(["REFUSE", "COMPLY"]), (g.label == "REFUSE").astype(float), np.nan); g["outcome"] = "refusal"; parts.append(g)
g = df[df.task == "syco_fact"].copy(); g["y"] = np.where(g.label.isin(["EMPTY", "UNPARSED"]), np.nan, (g.label == "WRONG_SUGGESTED").astype(float)); g["outcome"] = "syco_fact"; parts.append(g)
g = df[df.task == "accuracy"].copy(); g["y"] = np.where(g.label.isin(["UNPARSED"]), np.nan, (g.label == "CORRECT").astype(float)); g["outcome"] = "accuracy"; parts.append(g)
g = df[df.task == "syco_opinion"].copy(); g["y"] = 1 / (1 + np.exp(-g.value)); g["outcome"] = "syco_opinion"; parts.append(g)
for t in ["judge_ai", "judge_test"]:
    g = df[df.task == t].copy(); g["y"] = g.value; g["outcome"] = t; parts.append(g)
# output-style readout: does the response itself start in lower case (a human-casual marker)?
def lower_start(s):
    a = [c for c in (s or "") if c.isalpha()]
    return float(a[0].islower()) if a else np.nan
g = df[df.task.isin(["refusal", "syco_fact", "accuracy"])].copy(); g["y"] = g.response.map(lower_start); g["outcome"] = "resp_lowercase"
g["sid"] = g.task + ":" + g.sid; parts.append(g)
d = pd.concat(parts, ignore_index=True)
# Mixed scoring (Qwen): rows the API judge never reached carry a calibrated local-judge label (src/calibrate_local_judge.py).
# A condition scored mostly by the local judge is compared with the unsteered run scored by the same local judge.
JUDGED = ["refusal", "syco_fact", "accuracy"]; MIXED = "label_local" in d.columns and not RULE
if MIXED:
    code = {"refusal": "REFUSE", "syco_fact": "WRONG_SUGGESTED", "accuracy": "CORRECT"}
    jm = d.outcome.isin(JUDGED)
    d["y_local"] = np.where(jm & d.label_local.notna(), (d.label_local == d.outcome.map(code)).astype(float), np.nan)
    base_local = d[d.direction == "none"].set_index(["outcome", "sid"]).y_local
OUT = ["refusal", "syco_fact", "syco_opinion", "accuracy", "resp_lowercase", "judge_ai", "judge_test"]
base = d[d.direction == "none"].set_index(["outcome", "sid"]).y
rows = []
for (L, dr, a, oc), g in d[d.direction != "none"].groupby(["layer", "direction", "alpha", "outcome"]):
    frac_api = float((g.scorer == "api").mean()) if MIXED and oc in JUDGED else 1.0
    bs_ = base_local if frac_api < 0.5 else base
    diff = g.set_index("sid").y - bs_.loc[oc].reindex(g.sid).values
    b = boot(diff.values, n=4000)
    rows.append(dict(layer=L, direction=dr, alpha=a, outcome=oc, level=g.y.mean(), base=bs_.loc[oc].mean(), delta=b["mean"], lo=b["lo"], hi=b["hi"], p=b["p"], n=b["n"], frac_api=frac_api))
eff = pd.DataFrame(rows)
eff["kind"] = eff.direction.str.replace(r"\d+$", "", regex=True)
eff.to_csv(T / f"steer_effects_{key}{SUF}.csv", index=False)

# auth vs random-direction null at matched |alpha| (16 random values per layer x dose: 8 directions x 2 signs)
cmp_rows = []
for (L, oc), g in eff.groupby(["layer", "outcome"]):
    for A_ in (4, 8):
        rnd = g[g.kind.isin(["iso", "cov"]) & (g.alpha.abs() == A_)]
        for dr in ["auth", "len", "eval", "refusal"]:
            for sgn in (-1, 1):
                r = g[(g.direction == dr) & (g.alpha == sgn * A_)]
                if r.empty: continue
                r = r.iloc[0]
                cmp_rows.append(dict(layer=L, outcome=oc, direction=dr, alpha=sgn * A_, delta=r.delta, lo=r.lo, hi=r.hi,
                                     rand_abs_mean=rnd.delta.abs().mean(), rand_abs_max=rnd.delta.abs().max(),
                                     iso_abs_mean=rnd[rnd.kind == "iso"].delta.abs().mean(), cov_abs_mean=rnd[rnd.kind == "cov"].delta.abs().mean(),
                                     p_emp=(1 + (rnd.delta.abs() >= abs(r.delta)).sum()) / (1 + len(rnd))))
cmp_ = pd.DataFrame(cmp_rows); cmp_.to_csv(T / f"steer_vs_random_{key}{SUF}.csv", index=False)
# antisymmetry: (delta(+a) - delta(-a)) / 2 is the part of the effect that depends on the sign of the direction
anti = []
for (L, oc), g in eff.groupby(["layer", "outcome"]):
    for A_ in (4, 8):
        def odd(dr):
            p_ = g[(g.direction == dr) & (g.alpha == A_)].delta; m_ = g[(g.direction == dr) & (g.alpha == -A_)].delta
            return (p_.iloc[0] - m_.iloc[0]) / 2 if len(p_) and len(m_) else np.nan
        rnd = np.array([odd(k) for k in g[g.kind.isin(["iso", "cov"])].direction.unique()])
        for dr in ["auth", "len", "eval", "refusal"]:
            v = odd(dr)
            anti.append(dict(layer=L, outcome=oc, direction=dr, abs_alpha=A_, odd_effect=v, rand_abs_mean=np.abs(rnd).mean(), rand_abs_max=np.abs(rnd).max(),
                             p_emp=(1 + (np.abs(rnd) >= abs(v)).sum()) / (1 + len(rnd))))
anti = pd.DataFrame(anti); anti.to_csv(T / f"steer_odd_effects_{key}{SUF}.csv", index=False)
pd.set_option("display.width", 250)
print(eff[(eff.direction == "auth")].pivot_table(index=["layer", "alpha"], columns="outcome", values="delta")[OUT].round(3).to_string())
print(eff[(eff.direction == "auth") & eff.alpha.abs().le(2)].round(4).to_string())
print(anti[anti.direction.isin(["auth", "len", "eval", "refusal"])].pivot_table(index=["layer", "abs_alpha", "direction"], columns="outcome", values="odd_effect")[OUT].round(3).to_string())
print(anti.pivot_table(index=["layer", "abs_alpha", "direction"], columns="outcome", values="p_emp")[OUT].round(3).to_string())
print(anti[anti.direction == "auth"].pivot_table(index=["layer", "abs_alpha"], columns="outcome", values="rand_abs_mean")[OUT].round(3).to_string())

# figure: dose-response per layer and outcome
layers = sorted(eff.layer.unique())
titles = {"refusal": "Refusal rate", "syco_fact": "Factual sycophancy", "syco_opinion": "Opinion sycophancy P(match)", "accuracy": "Trivia accuracy",
          "resp_lowercase": "Response starts lower-case", "judge_ai": "Verbal 'AI-written' (logit)", "judge_test": "Verbal 'this is a test' (logit)"}
fig, axes = plt.subplots(len(layers), len(OUT), figsize=(3.1 * len(OUT), 2.6 * len(layers)), squeeze=False)
for i, L in enumerate(layers):
    for j, oc in enumerate(OUT):
        ax = axes[i, j]; g = eff[(eff.layer == L) & (eff.outcome == oc)]
        rnd = g[g.kind.isin(["iso", "cov"])]
        for k, gg in rnd.groupby("direction"):
            gg = gg.sort_values("alpha"); ax.plot(gg.alpha, gg.delta, "-", color="0.75", lw=0.8, marker=".", ms=3)
        for dr, col in [("len", "tab:green"), ("eval", "tab:purple"), ("refusal", "tab:orange")]:
            gg = g[g.direction == dr].sort_values("alpha"); ax.plot(gg.alpha, gg.delta, "--", color=col, marker="s", ms=3, lw=1, label=dr)
        gg = g[g.direction == "auth"].sort_values("alpha")
        ax.errorbar(gg.alpha, gg.delta, yerr=[gg.delta - gg.lo, gg.hi - gg.delta], color="tab:red", marker="o", ms=4, lw=1.6, capsize=2, label="authorship")
        ax.axhline(0, color="k", lw=0.5); ax.axvline(0, color="k", lw=0.5)
        if i == 0: ax.set_title(titles[oc], fontsize=9)
        if j == 0: ax.set_ylabel(f"layer {L}\nchange vs unsteered", fontsize=8)
        if i == len(layers) - 1: ax.set_xlabel("dose (x natural human->LLM gap)", fontsize=8)
        ax.tick_params(labelsize=7)
axes[0, 0].plot([], [], color="0.75", label="random (iso/cov)"); axes[0, 0].legend(fontsize=6)
plt.suptitle(f"{NAMES[key]}: steering on fixed prompt text (norm-matched directions)", fontsize=11)
plt.tight_layout(); plt.savefig(F / f"fig4_steering_{key}{SUF}.png", dpi=150); plt.close()
