"""D3 analysis for an open model: authorship probe validity, geometry vs eval-awareness / length / refusal
directions, and mediation of behaviour by the probe score.  Usage: python src/analyze_probe.py {llama|qwen}"""
import json, sys
from pathlib import Path
import numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler
sys.path.insert(0, str(Path(__file__).parent))
from stats_util import *
key = sys.argv[1]; out = RES / key; T = RES / "tables"; F = ROOT / "figures"
st = pd.read_json(out / "stimuli_scored.jsonl", lines=True)
body = pd.read_json(ROOT / "data/stimuli.jsonl", lines=True); body = body[body.audit_ok].reset_index(drop=True)
assert (body.sid.values == st.sid.values).all()
st = pd.concat([st.drop(columns=["n_words"]), pd.DataFrame([surface(b) for b in body.body])], axis=1)
A = np.load(out / "acts_last.npy", mmap_mode="r"); Am = np.load(out / "acts_mean.npy", mmap_mode="r")
Dz = np.load(out / "directions.npz"); LAYERS = list(Dz["layers"])
cfg = json.load(open(out / "steer_config.json")); L, li = cfg["layer"], cfg["idx"]
split = json.load(open(out / "wildchat_split.json")); tr, te = set(split["train"]), set(split["test"])
unit = lambda v: v / np.linalg.norm(v)
auc = lambda y, s: roc_auc_score(y, s)
st["style_L"] = st.cond.str.startswith("L").astype(float); st["long"] = st.cond.str.endswith("_l").astype(float)
wc = st[st.task == "wildchat"]; rwm = st.cond.isin(CONDS)

# ---------- 1. probe AUROC by layer (held-out WildChat rewrites), baselines ----------
rows = []
te_rw = wc[wc.sid.isin(te) & wc.cond.isin(CONDS)]; tr_rw = wc[wc.sid.isin(tr) & wc.cond.isin(CONDS)]
te_o = wc[wc.sid.isin(te) & (wc.cond == "orig")]
rnd_keys = [k for k in Dz.files if k.startswith("iso")]
for i, lay in enumerate(LAYERS):
    X = np.asarray(A[te_rw.uid.values, i], np.float32); d = unit(Dz["auth"][i]); s = X @ d
    so = np.asarray(A[te_o.uid.values, i], np.float32) @ d
    r = dict(layer=lay, auc_L_vs_H=auc(te_rw.style_L, s),
             auc_short_cells=auc(te_rw[te_rw.long == 0].style_L, s[(te_rw.long == 0).values]),
             auc_long_cells=auc(te_rw[te_rw.long == 1].style_L, s[(te_rw.long == 1).values]),
             auc_long_vs_short_on_auth=auc(te_rw.long, s),
             auc_L_vs_realhuman=auc(np.r_[np.zeros(len(so)), np.ones(int(te_rw.style_L.sum()))], np.r_[so, s[te_rw.style_L.values == 1]]),
             auc_Hrewrite_vs_realhuman=auc(np.r_[np.zeros(len(so)), np.ones(int((te_rw.style_L == 0).sum()))], np.r_[so, s[te_rw.style_L.values == 0]]),
             auc_random_dir=np.mean([max(a, 1 - a) for a in [auc(te_rw.style_L, X @ unit(Dz[k][i])) for k in rnd_keys]]),
             cos_auth_eval=float(unit(Dz["auth"][i]) @ unit(Dz["eval"][i])), cos_auth_len=float(unit(Dz["auth"][i]) @ unit(Dz["len"][i])),
             cos_auth_refusal=float(unit(Dz["auth"][i]) @ unit(Dz["refusal"][i])), cos_eval_refusal=float(unit(Dz["eval"][i]) @ unit(Dz["refusal"][i])),
             cos_len_eval=float(unit(Dz["len"][i]) @ unit(Dz["eval"][i])),
             cos_null_iso_abs=float(np.mean([abs(unit(Dz["auth"][i]) @ unit(Dz[k][i])) for k in rnd_keys])),
             cos_null_cov_abs=float(np.mean([abs(unit(Dz["auth"][i]) @ unit(Dz[k][i])) for k in Dz.files if k.startswith("cov")])),
             eval_split_half_cos=float(Dz["eval_rel"][i]))
    # cross-rewriter generalisation: direction from one rewriter's training pairs, tested on the other
    for a_, b_ in [("gpt", "claude"), ("claude", "gpt")]:
        t = tr_rw[tr_rw.rewriter == a_]
        da = np.asarray(A[t[t.style_L == 1].uid.values, i], np.float32).mean(0) - np.asarray(A[t[t.style_L == 0].uid.values, i], np.float32).mean(0)
        m = (te_rw.rewriter == b_).values
        r[f"auc_train_{a_}_test_{b_}"] = auc(te_rw.style_L[m], X[m] @ unit(da))
    rows.append(r)
lay_tab = pd.DataFrame(rows); lay_tab.to_csv(T / f"probe_by_layer_{key}.csv", index=False)
pd.set_option("display.width", 250); print(lay_tab.round(3).to_string())

# surface-feature baselines on the same held-out set
feat = ["log_words", "n_chars", "polite", "lower_start", "end_punct", "upper_frac", "apostrophe_free_contraction", "mean_word_len"]
base = {"auc_length_only": max(auc(te_rw.style_L, te_rw.n_words), 1 - auc(te_rw.style_L, te_rw.n_words))}
sc = StandardScaler().fit(tr_rw[feat]); lr = LogisticRegression(max_iter=2000).fit(sc.transform(tr_rw[feat]), tr_rw.style_L)
base["auc_surface_features_logreg"] = auc(te_rw.style_L, lr.decision_function(sc.transform(te_rw[feat])))
Xtr = np.asarray(A[tr_rw.uid.values, li], np.float32); Xte = np.asarray(A[te_rw.uid.values, li], np.float32)
sc2 = StandardScaler().fit(Xtr); lr2 = LogisticRegression(C=0.01, max_iter=3000).fit(sc2.transform(Xtr), tr_rw.style_L)
base["auc_logreg_probe_selected_layer"] = auc(te_rw.style_L, lr2.decision_function(sc2.transform(Xte)))
base["auc_diffmeans_selected_layer"] = float(lay_tab[lay_tab.layer == L].auc_L_vs_H.iloc[0])
base["auc_verbal_judgment"] = auc(te_rw.style_L, te_rw.judge_ai)
Xm = np.asarray(Am[te_rw.uid.values, li], np.float32); Xmtr = np.asarray(Am[tr_rw.uid.values, li], np.float32)
dm = Xmtr[tr_rw.style_L.values == 1].mean(0) - Xmtr[tr_rw.style_L.values == 0].mean(0)
base["auc_diffmeans_user_token_mean_pool"] = auc(te_rw.style_L, Xm @ unit(dm))

# ---------- 2. transfer of the WildChat-trained direction to benchmark items ----------
d = unit(Dz["auth"][li]); de = unit(Dz["eval"][li])
st["probe"] = np.asarray(A[:, li], np.float32) @ d
st["eval_proj"] = np.asarray(A[:, li], np.float32) @ de
sd = st[st.task == "wildchat"].probe.std()
st["probe_z"] = (st.probe - st[(st.task == "wildchat") & (st.cond == "orig")].probe.mean()) / sd
trans = []
for task, g in st[rwm].groupby("task"):
    if task == "wildchat": g = g[g.sid.isin(te)]
    cp = seed_level(contrasts(cells(g, "probe_z"))); ce = seed_level(contrasts(cells(g, "eval_proj"))); cj = seed_level(contrasts(cells(g, "judge_test")))
    trans.append(dict(task=task, auc_probe_L_vs_H=auc(g.style_L, g.probe), auc_probe_long_vs_short=auc(g.long, g.probe),
                      probe_style_gap_sd=cp["style"].mean(), probe_length_gap_sd=cp["length"].mean(),
                      evalproj_style=boot(ce["style"])["mean"], evalproj_style_p=boot(ce["style"])["p"],
                      evalproj_length=boot(ce["length"])["mean"], evalproj_length_p=boot(ce["length"])["p"],
                      verbal_test_style=boot(cj["style"])["mean"], verbal_test_style_p=boot(cj["style"])["p"],
                      verbal_test_length=boot(cj["length"])["mean"], verbal_test_length_p=boot(cj["length"])["p"]))
trans = pd.DataFrame(trans); trans.to_csv(T / f"probe_transfer_{key}.csv", index=False); print(trans.round(3).to_string())
o = st[st.cond == "orig"]
base["auc_evaldir_benchmark_orig_vs_wildchat_orig"] = auc((o.task != "wildchat").astype(int), o.eval_proj)
base["auc_authdir_benchmark_orig_vs_wildchat_orig"] = auc((o.task != "wildchat").astype(int), o.probe)
base["corr_probe_evalproj_within_rewrites"] = float(np.corrcoef(st[rwm].probe, st[rwm].eval_proj)[0, 1])
base["corr_probe_verbal_ai_judgment"] = float(np.corrcoef(st[rwm].probe, st[rwm].judge_ai)[0, 1])
base["corr_probe_verbal_test_judgment"] = float(np.corrcoef(st[rwm].probe, st[rwm].judge_test)[0, 1])
base["selected_layer"] = L
json.dump(base, open(T / f"probe_summary_{key}.json", "w"), indent=1); print(json.dumps(base, indent=1))

# ---------- 3. mediation: does the probe score predict behaviour within item, beyond surface features? ----------
b = load_behaviour(key); b = b[b.cond.isin(CONDS)]
b = b.merge(st[["sid", "rewriter", "cond", "probe_z", "style_L", "long", "log_words", "polite", "judge_ai"]], on=["sid", "rewriter", "cond"])
med = []
for oc, g in b.groupby("outcome"):
    g = g.copy()
    for c in ["y", "probe_z", "style_L", "long", "log_words", "polite"]:   # absorb item fixed effects
        g[c + "_w"] = g[c] - g.groupby("sid")[c].transform("mean")
    for name, f in {"style_only": "y_w ~ style_L_w + long_w - 1", "probe_only": "y_w ~ probe_z_w + log_words_w + polite_w - 1",
                    "style+probe": "y_w ~ style_L_w + probe_z_w + log_words_w + polite_w - 1"}.items():
        fit = smf.ols(f, g).fit(cov_type="cluster", cov_kwds={"groups": g.sid})
        for term in fit.params.index:
            med.append(dict(outcome=oc, spec=name, term=term.removesuffix("_w"), coef=fit.params[term], se=fit.bse[term], p=fit.pvalues[term], n=len(g)))
med = pd.DataFrame(med); med.to_csv(T / f"mediation_{key}.csv", index=False); print(med.round(4).to_string())

# ---------- figure ----------
fig, ax = plt.subplots(1, 2, figsize=(11, 3.8))
ax[0].plot(lay_tab.layer, lay_tab.auc_L_vs_H, "o-", label="LLM vs human style (all cells)")
ax[0].plot(lay_tab.layer, lay_tab.auc_short_cells, "s--", label="length-matched short cells")
ax[0].plot(lay_tab.layer, lay_tab.auc_Hrewrite_vs_realhuman, "^-", label="human-style rewrite vs real human")
ax[0].plot(lay_tab.layer, lay_tab.auc_long_vs_short_on_auth, "x-", label="long vs short (should be ~0.5)")
ax[0].plot(lay_tab.layer, lay_tab.auc_random_dir, "k:", label="random direction")
ax[0].axvline(L, color="gray", lw=0.8); ax[0].set_xlabel("layer"); ax[0].set_ylabel("held-out AUROC"); ax[0].legend(fontsize=7); ax[0].set_title(f"{NAMES[key]}: authorship direction", fontsize=10)
ax[1].plot(lay_tab.layer, lay_tab.cos_auth_eval, "o-", label="auth . eval-awareness")
ax[1].plot(lay_tab.layer, lay_tab.cos_auth_len, "s-", label="auth . length")
ax[1].plot(lay_tab.layer, lay_tab.cos_auth_refusal, "^-", label="auth . refusal")
ax[1].fill_between(lay_tab.layer, -lay_tab.cos_null_cov_abs, lay_tab.cos_null_cov_abs, color="gray", alpha=0.3, label="mean |cos| with covariance-matched random")
ax[1].axhline(0, color="k", lw=0.6); ax[1].axvline(L, color="gray", lw=0.8); ax[1].set_xlabel("layer"); ax[1].set_ylabel("cosine similarity"); ax[1].legend(fontsize=7)
plt.tight_layout(); plt.savefig(F / f"fig3_probe_{key}.png", dpi=160); plt.close()
