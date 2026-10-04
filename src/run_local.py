"""Stage 1 for an open model: activations, perception judgments and behaviour on every stimulus.
Usage: python src/run_local.py {llama|qwen} [--smoke]"""
import json, sys, time
from pathlib import Path
import numpy as np, pandas as pd, torch
sys.path.insert(0, str(Path(__file__).parent))
from local import LM, LABELS
ROOT = Path(__file__).resolve().parent.parent
key = sys.argv[1]; smoke = "--smoke" in sys.argv
out = ROOT / "results" / key; out.mkdir(parents=True, exist_ok=True)
torch.manual_seed(0)
df = pd.read_json(ROOT / "data/stimuli.jsonl", lines=True)
df = df[df.audit_ok].reset_index(drop=True)  # only content-faithful rewrites
if smoke: df = df.groupby(["task", "cond", "rewriter"]).head(2).reset_index(drop=True)
df["uid"] = np.arange(len(df))
seeds = {s["sid"]: s for s in map(json.loads, open(ROOT / "data/seeds.jsonl"))}
lm = LM(key); t0 = time.time()

# 1) activations (default chat template, no label)
last, mean = lm.acts(df.text.tolist())
np.save(out / "acts_last.npy", last); np.save(out / "acts_mean.npy", mean)
print("acts", last.shape, round(time.time() - t0)); 

# 2) perception judgments (logit differences)
df["judge_ai"] = lm.judge_auth(df.text.tolist())
df["judge_test"] = lm.judge_eval(df.text.tolist())
print("judgments", round(time.time() - t0))

# 3) behaviour. Explicit-label arms reuse the orig text with a system note.
beh = df[df.task != "wildchat"].copy(); beh["system"] = None
lab = []
for name, note in LABELS.items():
    d = beh[beh.cond == "orig"].copy(); d["cond"] = name; d["system"] = note; lab.append(d)
beh = pd.concat([beh] + lab, ignore_index=True)
gen = beh[beh.task.isin(["refusal", "accuracy", "syco_fact"])].copy()
gen["response"] = lm.generate(gen.text.tolist(), gen.system.tolist(), max_new_tokens=96)
print("generation", len(gen), round(time.time() - t0))
op = beh[beh.task == "syco_opinion"].copy()
# opinion sycophancy: logit(answer matching user's view) - logit(other), after assistant prefill " ("
ab = lm.logit_diff(op.text.tolist(), "A", "B", op.system.tolist(), prefill="(")
sign = np.array([1.0 if seeds[s]["match"] == "(A)" else -1.0 for s in op.sid])
op["syco_logit"] = ab * sign
df.drop(columns=["body"]).to_json(out / "stimuli_scored.jsonl", orient="records", lines=True)
pd.concat([gen, op], ignore_index=True).drop(columns=["body"]).to_json(out / "behaviour_raw.jsonl", orient="records", lines=True)
print("done", round(time.time() - t0))
