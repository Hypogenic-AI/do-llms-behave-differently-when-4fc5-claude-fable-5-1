"""Open-model extras: (a) behaviour, perception and probe projection on the uncontrolled `L_free` arm;
(b) a style-matched refusal direction (StrongREJECT harmful minus unused JBB benign items) for the geometry table.
Usage: python src/run_local_free.py {llama|qwen}"""
import json, sys
from pathlib import Path
import numpy as np, pandas as pd, torch
sys.path.insert(0, str(Path(__file__).parent))
from local import LM
ROOT = Path(__file__).resolve().parent.parent
key = sys.argv[1]; out = ROOT / "results" / key
lm = LM(key)
df = pd.read_json(ROOT / "data/stimuli_free.jsonl", lines=True); df = df[df.audit_ok].reset_index(drop=True)
seeds = {s["sid"]: s for s in map(json.loads, open(ROOT / "data/seeds.jsonl"))}
Dz = np.load(out / "directions.npz"); LAYERS = list(Dz["layers"]); cfg = json.load(open(out / "steer_config.json"))
unit = lambda v: v / np.linalg.norm(v)
last, _ = lm.acts(df.text.tolist(), bs=16)
for L in cfg["layers"]:
    i = LAYERS.index(L); df[f"proj_auth_L{L}"] = last[:, i].astype(np.float32) @ unit(Dz["auth"][i])
df["judge_ai"] = lm.judge_auth(df.text.tolist())
g = df.task.isin(["refusal", "accuracy", "syco_fact"])
df.loc[g, "response"] = lm.generate(df[g].text.tolist(), max_new_tokens=96)
o = df.task == "syco_opinion"
sign = np.array([1.0 if seeds[s]["match"] == "(A)" else -1.0 for s in df[o].sid])
df.loc[o, "syco_logit"] = lm.logit_diff(df[o].text.tolist(), "A", "B", prefill="(") * sign
df.drop(columns=["body"]).to_json(out / "free_raw.jsonl", orient="records", lines=True)

# style-matched refusal direction: both sides are benchmark-style imperatives
used = {s["seed_text"] for s in seeds.values()}
jb = pd.read_csv(ROOT / "datasets/jbb_behaviors/data/benign-behaviors.csv"); benign = [g_ for g_ in jb.Goal if g_.strip() not in used]
sr = pd.read_csv(ROOT / "datasets/strongreject/strongreject_dataset.csv").sample(150, random_state=0).forbidden_prompt.tolist()
harm = lm.acts(sr)[0].astype(np.float32).mean(0); ben = lm.acts(benign)[0].astype(np.float32).mean(0)
np.save(out / "refusal_matched_dir.npy", harm - ben)
print("done", len(df), len(benign))
