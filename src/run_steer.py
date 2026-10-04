"""Stage 2 for an open model: build directions, pick a layer, steer on fixed prompt text.
Usage: python src/run_steer.py {llama|qwen}

Directions (all at the last prompt token, estimated on WildChat training items only):
  auth    = 1/2[(L_s - H_s) + (L_l - H_l)]      LLM-style minus human-style, length-balanced
  len     = 1/2[(H_l - H_s) + (L_l - L_s)]      long minus short, style-balanced
  eval    = test-statement minus deployment-statement system prompts (16 contrastive pairs, Nguyen et al.)
  refusal = harmful (StrongREJECT) minus harmless (WildChat) prompts (Arditi et al.), positive control
  iso_k   = isotropic random directions; cov_k = random directions drawn from the activation covariance
Steering adds alpha * ||auth|| * unit(direction) to the residual stream at one layer (three layers are tried), at every position.
alpha = 1 therefore equals the natural human->LLM style shift for `auth`; every other direction is norm-matched.
"""
import json, re, sys, time
from pathlib import Path
import numpy as np, pandas as pd, torch
from sklearn.metrics import roc_auc_score
sys.path.insert(0, str(Path(__file__).parent))
from local import LM
ROOT = Path(__file__).resolve().parent.parent
key = sys.argv[1]; out = ROOT / "results" / key
rng = np.random.default_rng(0); torch.manual_seed(0)
st = pd.read_json(out / "stimuli_scored.jsonl", lines=True)
A = np.load(out / "acts_last.npy", mmap_mode="r")
lm = LM(key); LAYERS = lm.layers; t0 = time.time()
unit = lambda v: v / np.linalg.norm(v)

# ---------- WildChat split and 2x2 cell means ----------
wc = st[st.task == "wildchat"]
sids = sorted(wc.sid.unique()); rng.shuffle(sids)
train_sids = set(sids[: int(0.7 * len(sids))]); test_sids = set(sids[int(0.7 * len(sids)):])
json.dump({"train": sorted(train_sids), "test": sorted(test_sids)}, open(out / "wildchat_split.json", "w"))
rw = wc[wc.cond != "orig"]
complete = rw.groupby(["sid", "rewriter"]).cond.nunique().reset_index().query("cond == 4")[["sid", "rewriter"]]
rw = rw.merge(complete, on=["sid", "rewriter"])
def cell_mean(cond, sidset):
    u = rw[(rw.cond == cond) & rw.sid.isin(sidset)].uid.values
    return np.asarray(A[np.sort(u)], np.float32).mean(0)  # [layers, d]
M = {c: cell_mean(c, train_sids) for c in ["H_s", "H_l", "L_s", "L_l"]}
D = {"auth": 0.5 * ((M["L_s"] - M["H_s"]) + (M["L_l"] - M["H_l"])),
     "len": 0.5 * ((M["H_l"] - M["H_s"]) + (M["L_l"] - M["L_s"]))}

# ---------- eval-awareness direction ----------
pairs = re.findall(r"positive_example: (.*)\nnegative_example: (.*)",
                   open(ROOT / "code/evaluation-awareness_evaluation-awareness/cls_corr_mi/data/contrastive_pairs_16.txt").read())
assert len(pairs) == 16
wc_orig = wc[wc.cond == "orig"]
neutral = wc_orig[wc_orig.sid.isin(train_sids)].text.tolist()[:40]
dep = lm.acts([u for _ in pairs for u in neutral], systems=[p for p, _ in pairs for _ in neutral])[0].astype(np.float32)
tst = lm.acts([u for _ in pairs for u in neutral], systems=[n for _, n in pairs for _ in neutral])[0].astype(np.float32)
D["eval"] = tst.mean(0) - dep.mean(0)
# split-half reliability of the eval direction across contrastive pairs (cosine, per layer)
h = len(tst) // 2
eval_rel = [float(unit((tst[:h] - dep[:h]).mean(0)[i]) @ unit((tst[h:] - dep[h:]).mean(0)[i])) for i in range(len(LAYERS))]

# ---------- refusal direction ----------
sr = pd.read_csv(ROOT / "datasets/strongreject/strongreject_dataset.csv").sample(150, random_state=0).forbidden_prompt.tolist()
harm = lm.acts(sr)[0].astype(np.float32)
harmless = np.asarray(A[np.sort(wc_orig[wc_orig.sid.isin(train_sids)].uid.values)], np.float32)
D["refusal"] = harm.mean(0) - harmless.mean(0)

# ---------- random baselines ----------
N_RAND = 6
d_model = A.shape[-1]
train_u = np.sort(wc[wc.sid.isin(train_sids)].uid.values)
Xtr = np.asarray(A[train_u], np.float32); Xc = Xtr - Xtr.mean(0)
for k in range(N_RAND):
    D[f"iso{k}"] = rng.standard_normal((len(LAYERS), d_model)).astype(np.float32)
    w = rng.standard_normal(len(Xc)).astype(np.float32)
    D[f"cov{k}"] = np.einsum("n,nld->ld", w, Xc)
np.savez(out / "directions.npz", layers=np.array(LAYERS), eval_rel=np.array(eval_rel), **D)
print("directions", round(time.time() - t0), flush=True)

# ---------- layer selection (uses only WildChat + the verbal authorship judgment) ----------
test_rw = rw[rw.sid.isin(test_sids)]
Xte = np.asarray(A[np.sort(test_rw.uid.values)], np.float32); yte = test_rw.sort_values("uid").cond.str.startswith("L").values
probe_wild = wc_orig[wc_orig.sid.isin(test_sids)].text.tolist()[:60]
sel = []
for i, L in enumerate(LAYERS):
    if L < 4 or L > lm.n_layers - 4: continue
    auc = roc_auc_score(yte, Xte[:, i] @ unit(D["auth"][i]))
    res_norm = float(np.linalg.norm(Xtr[:, i], axis=1).mean())
    js = {}
    for a in (-4, 4):
        with lm.steer(L, a * D["auth"][i]):
            js[a] = float(lm.judge_auth(probe_wild).mean())
    sel.append(dict(layer=L, idx=i, auc=auc, gap_norm=float(np.linalg.norm(D["auth"][i])), resid_norm=res_norm,
                    judge_ai_m4=js[-4], judge_ai_p4=js[4], djudge=js[4] - js[-4]))
    print(sel[-1], flush=True)
sel = pd.DataFrame(sel); sel.to_csv(out / "layer_selection.csv", index=False)
# Three steering layers (the last-token probe is strongest early and fades with depth, so one layer is not enough):
#   early = layer with the best held-out probe AUROC; mid = deepest layer whose AUROC is still >= 0.9;
#   late  = layer where +/-4 natural doses move the verbal authorship judgment most in the expected direction.
L_early = int(sel.loc[sel.auc.idxmax()].layer)
L_mid = int(sel[sel.auc >= 0.9].layer.max())
L_late = int(sel.loc[sel.djudge.idxmax()].layer)
steer_layers = sorted({L_early, L_mid, L_late})
json.dump({"layer": L_mid, "idx": LAYERS.index(L_mid), "layers": steer_layers, "roles": {"early": L_early, "mid": L_mid, "late": L_late},
           "gap_norm": {str(l): float(np.linalg.norm(D["auth"][LAYERS.index(l)])) for l in steer_layers},
           "resid_norm": {str(int(r.layer)): float(r.resid_norm) for r in sel.itertuples()}}, open(out / "steer_config.json", "w"))
print("steer layers", steer_layers, flush=True)

# ---------- steering on fixed text ----------
beh = st[(st.cond == "orig") & (st.task != "wildchat")]
gen_set = pd.concat([beh[beh.task.isin(["refusal", "syco_fact"])], beh[beh.task == "accuracy"].head(100)])
op = beh[beh.task == "syco_opinion"]
seeds = {s["sid"]: s for s in map(json.loads, open(ROOT / "data/seeds.jsonl"))}
op_sign = np.array([1.0 if seeds[s]["match"] == "(A)" else -1.0 for s in op.sid])
jw = wc_orig[wc_orig.sid.isin(test_sids)]
N_STEER_RAND = 4
conds = [(0, "none", 0.0)]
for L in steer_layers:
    conds += [(L, "auth", a) for a in (-8, -4, -2, -1, 1, 2, 4, 8)]
    conds += [(L, d, a) for d in ["len", "eval", "refusal"] + [f"iso{k}" for k in range(N_STEER_RAND)] + [f"cov{k}" for k in range(N_STEER_RAND)]
              for a in (-8, -4, 4, 8)]
done = set()
fout = out / "steer_raw.jsonl"
if fout.exists():
    done = {(r["layer"], r["direction"], r["alpha"]) for r in map(json.loads, open(fout))}
with open(fout, "a") as f:
    for L, d, a in conds:
        if (L, d, a) in done: continue
        li = LAYERS.index(L) if L else 0
        gap = float(np.linalg.norm(D["auth"][li]))
        vec = None if d == "none" else a * gap * unit(D[d][li])
        with lm.steer(L, vec):
            resp = lm.generate(gen_set.text.tolist(), max_new_tokens=48, bs=96)
            syco = lm.logit_diff(op.text.tolist(), "A", "B", prefill="(") * op_sign
            ja = lm.judge_auth(jw.text.tolist()); je = lm.judge_eval(jw.text.tolist())
        rows = [dict(layer=L, direction=d, alpha=a, task=t, sid=s, response=r) for t, s, r in zip(gen_set.task, gen_set.sid, resp)]
        rows += [dict(layer=L, direction=d, alpha=a, task="syco_opinion", sid=s, value=float(v)) for s, v in zip(op.sid, syco)]
        rows += [dict(layer=L, direction=d, alpha=a, task="judge_ai", sid=s, value=float(v)) for s, v in zip(jw.sid, ja)]
        rows += [dict(layer=L, direction=d, alpha=a, task="judge_test", sid=s, value=float(v)) for s, v in zip(jw.sid, je)]
        for r in rows: f.write(json.dumps(r) + "\n")
        f.flush()
        print(L, d, a, round(time.time() - t0), "| sample:", resp[0][:60].replace("\n", " "), flush=True)
print("done", round(time.time() - t0))
