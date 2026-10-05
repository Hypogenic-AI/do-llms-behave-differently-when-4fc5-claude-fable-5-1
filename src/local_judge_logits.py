"""Option logits of a local judge for every generated response in a steering file (same rubric as src/judge.py).
Used to build a judge calibrated against the API judge after OpenRouter credits ran out (src/calibrate_local_judge.py).
Usage: python src/local_judge_logits.py {llama|qwen} <model_dir_key> [none]   -> results/<key>/steer_judge_logits_<judge>.parquet
Identical (task, sid, response) triples are scored once; only rows lacking an API label plus a 9,000-row calibration sample are scored."""
import json, os, sys
from pathlib import Path
import numpy as np, pandas as pd, torch
os.environ["API_OFFLINE"] = "1"
sys.path.insert(0, str(Path(__file__).parent))
from local import LM
from local_judge import build, OPTS
ROOT = Path(__file__).resolve().parent.parent
judge, key = sys.argv[1], sys.argv[2]
df = pd.read_json(ROOT / "results" / key / "steer_raw.jsonl", lines=True)
df = df[df.task.isin(["refusal", "accuracy", "syco_fact"])]
# only what is needed: rows without a cached API label, plus a random sample of API-labelled rows for calibration
api = pd.read_json(ROOT / "results" / key / "steer_judged_api_cached.jsonl", lines=True)
api = api[api.task.isin(["refusal", "accuracy", "syco_fact"])]
assert len(api) == len(df) and (api.sid.values == df.sid.values).all()
has = (~api.label.isin(["UNPARSED"])).values
cal = df[has].sample(9000, random_state=0)
NONE = len(sys.argv) > 3 and sys.argv[3] == "none"   # second pass: the unsteered rows (local-scored baseline)
u = (df[df.direction == "none"] if NONE else pd.concat([df[~has], cal]))[["task", "sid", "response"]].drop_duplicates().reset_index(drop=True)
u = u[u.response.fillna("").str.strip() != ""].reset_index(drop=True)
print("rows", len(df), "unique", len(u), flush=True)
lm = LM(judge)
ids = {k: [lm.tok.encode(o, add_special_tokens=False)[0] for o in v] for k, v in OPTS.items()}
built = [build(r) for r in u.to_dict("records")]
out = np.full((len(u), 3), np.nan, np.float32)
order = np.argsort([len(b[0]) for b in built])
with torch.no_grad():
    for b in range(0, len(order), 64):
        idx = order[b:b + 64]
        lg = lm.last_logits(lm._enc([lm.fmt(built[i][0]) for i in idx]))
        lg = torch.log_softmax(lg, -1)
        for row, i in zip(lg, idx):
            v = row[ids[built[i][1]]].cpu().numpy(); out[i, :len(v)] = v
        if (b // 64) % 100 == 0: print(b, len(order), flush=True)
for j in range(3): u[f"l{j}"] = out[:, j]
u.to_parquet(ROOT / "results" / key / f"steer_judge_logits_{judge}{'_none' if NONE else ''}.parquet")
print("done")
