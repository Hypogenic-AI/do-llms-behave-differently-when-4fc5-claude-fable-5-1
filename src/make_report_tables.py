"""Collect the headline numbers from results/tables/*.csv into one markdown file (results/tables/report_tables.md)."""
import json, sys
from pathlib import Path
import pandas as pd
sys.path.insert(0, str(Path(__file__).parent))
from stats_util import RES, NAMES, LOCAL
T = RES / "tables"; out = []
pp = lambda r: f"{100*r['mean']:+.1f} [{100*r.lo:+.1f}, {100*r.hi:+.1f}]"
def md(df): return df.to_markdown(index=False)

mc = pd.read_csv(T / "manipulation_check_cells.csv"); mc["model"] = mc.model.map(NAMES)
out += ["## Manipulation check (responder's own authorship judgment; AUROC LLM-style vs human-style)", md(mc[["model", "task", "auc_L_vs_H", "auc_L_vs_H_short", "H_s", "H_l", "L_s", "L_l", "orig"]].round(2))]
c = pd.read_csv(T / "behaviour_contrasts.csv"); c["model"] = c.model.map(NAMES)
for k, title in [("style", "Style effect (LLM minus human style, length-balanced), pp [95% CI]"), ("length", "Length effect (long minus short), pp [95% CI]"),
                 ("style_at_short", "Style effect within the length-matched short cells, pp [95% CI]")]:
    g = c[(c.scope == "all") & (c.contrast == k)].copy(); g["v"] = g.apply(pp, axis=1)
    out += [f"## {title}", md(g.pivot(index="model", columns="outcome", values="v").reset_index())]
g = c[(c.scope == "all") & (c.contrast == "style")][["model", "outcome", "n", "mean", "p", "p_holm", "dz"]].round(4)
out += ["## Style effect: p-values (sign-flip permutation; Holm over model x 4 primary outcomes)", md(g)]
cm = pd.read_csv(T / "behaviour_cell_means.csv"); cm["model"] = cm.model.map(NAMES)
out += ["## Cell means", md(cm.round(3))]
pool = pd.read_csv(T / "behaviour_contrasts_pooled.csv"); pool["v"] = pool.apply(pp, axis=1)
out += ["## Pooled over models", md(pool[["outcome", "contrast", "n_models", "n", "v", "p"]].round(4))]
lab = pd.read_csv(T / "label_arm.csv"); lab["model"] = lab.model.map(NAMES); lab["v"] = lab.apply(pp, axis=1)
out += ["## Explicit label arm (identical text): label_ai - label_human, pp", md(lab[lab.contrast == "label_ai - label_human"][["model", "outcome", "n", "v", "p", "p_holm"]].round(4))]
f = pd.read_csv(T / "naive_vs_controlled.csv"); f["model"] = f.model.map(NAMES); f["v"] = f.apply(pp, axis=1)
out += ["## Naive (uncontrolled LLM rewrite) vs controlled contrasts, pp", md(f[~f.contrast.str.contains("rewriter")].pivot(index=["model", "outcome"], columns="contrast", values="v").reset_index()),
        md(f[f.contrast == "naive: L_free - H_s"][["model", "outcome", "n", "H_s", "L_free", "p"]].round(4))]
rf = pd.read_csv(T / "response_form.csv"); rf["model"] = rf.model.map(NAMES)
out += ["## Response form on trivia items", md(rf[["model", "outcome", "H_s", "H_l", "L_s", "L_l", "style_mean", "style_lo", "style_hi", "style_p", "length_mean", "length_p"]].round(3))]
out += ["## Refusal sensitivity (empty responses counted as refusal) and filter-like responses", md(pd.read_csv(T / "refusal_sensitivity_empty_as_refusal.csv").round(4))]
out += ["## Stimulus surface features", md(pd.read_csv(T / "stimulus_surface_features.csv").round(2))]
for k in LOCAL:
    if not (T / f"probe_by_layer_{k}.csv").exists(): continue
    p = pd.read_csv(T / f"probe_by_layer_{k}.csv")
    out += [f"## Probe by layer: {NAMES[k]}", md(p[["layer", "auc_L_vs_H", "auc_short_cells", "auc_long_vs_short_on_auth", "auc_L_vs_realhuman", "auc_Hrewrite_vs_realhuman", "auc_random_dir",
                                                      "auc_train_gpt_test_claude", "cos_auth_eval", "cos_auth_len", "cos_auth_refusal", "cos_null_cov_abs", "cos_null_iso_abs", "eval_split_half_cos"]].round(3)),
            "```\n" + json.dumps(json.load(open(T / f"probe_summary_{k}.json")), indent=1) + "\n```",
            md(pd.read_csv(T / f"probe_transfer_{k}.csv").round(3)), md(pd.read_csv(T / f"mediation_{k}.csv").round(4))]
    if (T / f"steer_odd_effects_{k}.csv").exists():
        a = pd.read_csv(T / f"steer_odd_effects_{k}.csv")
        a["v"] = a.apply(lambda r: f"{r.odd_effect:+.3f} (rand {r.rand_abs_mean:.3f}; p={r.p_emp:.2f})", axis=1)
        out += [f"## Steering, sign-dependent effect (delta(+a)-delta(-a))/2 : {NAMES[k]}", md(a.pivot(index=["layer", "abs_alpha", "direction"], columns="outcome", values="v").reset_index())]
        e = pd.read_csv(T / f"steer_effects_{k}.csv"); e = e[(e.direction == "auth")]
        e["v"] = e.apply(lambda r: f"{r.delta:+.3f} [{r.lo:+.3f},{r.hi:+.3f}]", axis=1)
        out += [f"## Steering along authorship direction, change vs unsteered: {NAMES[k]}", md(e.pivot(index=["layer", "alpha"], columns="outcome", values="v").reset_index())]
sl = pd.read_csv(T / "steer_logit_slopes.csv"); sl = sl[sl.scale == "prob"].copy(); sl["model"] = sl.model.map(NAMES)
for c_ in ["slope", "lo", "hi", "rand_abs_mean", "rand_abs_max"]: sl[c_] = 100 * sl[c_]
out += ["## Natural-dose steering (alpha = +/-1, +/-2), slope in pp per natural unit, vs 32 random directions (logit readouts)",
        md(sl[["model", "layer", "outcome", "direction", "slope", "lo", "hi", "rand_abs_mean", "rand_abs_max", "p_emp"]].round(2)), md(pd.read_csv(T / "steer_logit_validity.csv").round(3))]
out += ["## Scorer agreement: API judge vs rule-based scorer on behaviour outputs", md(pd.read_csv(T / "scorer_agreement.csv").round(3)),
        "## Primary style contrast under both scorers", md(pd.read_csv(T / "scorer_sensitivity.csv").round(4)),
        "## Calibrated local judge vs API judge on held-out Qwen steering outputs", md(pd.read_csv(T / "local_judge_calibration_qwen.csv").round(3))]
st = pd.read_csv(T / "steer_style_readout.csv"); st = st[st.kind.isin(["auth", "iso", "cov"])]
out += ["## Output register under steering: share of sentence starts in lower case (mean; random = max over 8 directions)",
        md(st.assign(kind=st.kind.replace({"iso": "random", "cov": "random"})).groupby(["model", "layer", "kind", "alpha"]).lower_sent.max().unstack().round(3).reset_index())]
(T / "report_tables.md").write_text("\n\n".join(out)); print("written", len(out))
