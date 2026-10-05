"""Natural-dose steering with a large random-direction baseline, using logit readouts only (no generation).
Added after the main steering run, where random directions were only run at +/-4 and +/-8 (8 directions).
Usage: python src/run_steer_logit.py {llama|qwen}

Prompt text is fixed to the benchmark's own wording (`orig`).  For each steering layer and each direction
(auth, len, eval, refusal, 16 isotropic random, 16 covariance random) add alpha * ||auth|| * unit(direction), alpha in {-2,-1,1,2}:
  syco_opinion : logit(matching option) - logit(other option) after the assistant prefill "("   (150 items)
  refusal_tok  : log-odds that the first response token is "I" (refusal-token metric of Arditi et al. 2024; 250 items)
Random directions are freshly drawn (seed 1), so they are independent of the 8 used in run_steer.py.
"""
import json, sys, time
from pathlib import Path
import numpy as np, pandas as pd, torch
sys.path.insert(0, str(Path(__file__).parent))
from local import LM
ROOT = Path(__file__).resolve().parent.parent
key = sys.argv[1]; out = ROOT / "results" / key
N_RAND = 16; ALPHAS = (-2, -1, 1, 2); BS = 64
rng = np.random.default_rng(1)
st = pd.read_json(out / "stimuli_scored.jsonl", lines=True)
cfg = json.load(open(out / "steer_config.json")); Dz = np.load(out / "directions.npz"); LAYERS = list(Dz["layers"])
split = json.load(open(out / "wildchat_split.json"))
A = np.load(out / "acts_last.npy", mmap_mode="r")
lm = LM(key); t0 = time.time()
unit = lambda v: v / np.linalg.norm(v)

# directions per steering layer: named ones from the main run + fresh random baselines
wc = st[st.task == "wildchat"]
train_u = np.sort(wc[wc.sid.isin(split["train"])].uid.values)
D = {}
for L in cfg["layers"]:
    i = LAYERS.index(L)
    d = {k: Dz[k][i].astype(np.float32) for k in ["auth", "len", "eval", "refusal"]}
    Xc = np.asarray(A[train_u, i], np.float32); Xc -= Xc.mean(0)
    for k in range(N_RAND):
        d[f"iso{k}"] = rng.standard_normal(Xc.shape[1]).astype(np.float32)
        d[f"cov{k}"] = rng.standard_normal(len(Xc)).astype(np.float32) @ Xc
    D[L] = d

beh = st[(st.cond == "orig") & (st.task != "wildchat")]
seeds = {s["sid"]: s for s in map(json.loads, open(ROOT / "data/seeds.jsonl"))}
op = beh[beh.task == "syco_opinion"]; rf = beh[beh.task == "refusal"]
op_sign = np.array([1.0 if seeds[s]["match"] == "(A)" else -1.0 for s in op.sid])
tid = lambda t: lm.tok.encode(t, add_special_tokens=False)[0]
tA, tB, tI = tid("A"), tid("B"), tid("I")

def batches(texts, prefill=""):
    """Tokenise once; the same encodings are reused for every steering condition."""
    order = np.argsort([len(u) for u in texts]); bs = []
    for i in range(0, len(texts), BS):
        idx = order[i:i + BS]; bs.append((idx, lm._enc([lm.fmt(texts[j], None, prefill) for j in idx])))
    return bs
B_op = batches(op.text.tolist(), "("); B_rf = batches(rf.text.tolist())

@torch.no_grad()
def readout():
    o = np.zeros(len(op), np.float32); r = np.zeros(len(rf), np.float32)
    for idx, enc in B_op:
        lg = lm.last_logits(enc); o[idx] = (lg[:, tA] - lg[:, tB]).cpu().numpy()
    for idx, enc in B_rf:
        lp = torch.log_softmax(lm.last_logits(enc), -1)[:, tI]
        r[idx] = (lp - torch.log1p(-lp.exp().clamp(max=1 - 1e-6))).cpu().numpy()
    return o * op_sign, r

rows = []
def add(L, d, a, o, r):
    rows.extend(dict(layer=L, direction=d, alpha=a, task="syco_opinion", sid=s, value=float(v)) for s, v in zip(op.sid, o))
    rows.extend(dict(layer=L, direction=d, alpha=a, task="refusal_tok", sid=s, value=float(v)) for s, v in zip(rf.sid, r))
add(0, "none", 0, *readout())
for L in cfg["layers"]:
    gap = float(np.linalg.norm(D[L]["auth"]))
    for d, v in D[L].items():
        for a in ALPHAS:
            with lm.steer(L, a * gap * unit(v)):
                add(L, d, a, *readout())
        print(L, d, round(time.time() - t0), flush=True)
    pd.DataFrame(rows).to_csv(out / "steer_logit_raw.csv", index=False)
print("done", len(rows), round(time.time() - t0))
