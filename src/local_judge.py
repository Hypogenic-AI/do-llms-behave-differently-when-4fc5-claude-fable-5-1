"""Local LLM judge (open model on the GPU), used after the OpenRouter key reached its daily limit.
Same rubric prompts as the API judge (src/judge.py); the label is the option whose first token has the
highest next-token logit.
  python src/local_judge.py validate {llama|qwen} <judged.jsonl> [n]   # agreement with existing API labels
  python src/local_judge.py label {llama|qwen} <in.jsonl> <out.jsonl>   # add `label` (keeps rows without responses)
"""
import json, os, sys
from pathlib import Path
import numpy as np, pandas as pd, torch
os.environ["API_OFFLINE"] = "1"
sys.path.insert(0, str(Path(__file__).parent))
from judge import REFUSAL, TRIVIA, SEEDS
from local import LM
ROOT = Path(__file__).resolve().parent.parent
OPTS = {"refusal": ["REFUSE", "COMPLY"], "trivia": ["CORRECT", "WRONG_SUGGESTED", "OTHER"]}

def build(r):
    s = SEEDS[r["sid"]]; resp = (r["response"] or "")[:1500]
    if r["task"] == "refusal":
        return REFUSAL.format(req=s["seed_text"], resp=resp), "refusal"
    return TRIVIA.format(q=SEEDS[r["sid"].replace("syco_fact", "accuracy")]["seed_text"], c=s["correct"], al="; ".join(s["aliases"][:8]),
                         w=s["incorrect"], resp=resp), "trivia"

@torch.no_grad()
def label_rows(lm, rows, bs=64):
    out = [None] * len(rows); todo = []
    for i, r in enumerate(rows):
        resp = r.get("response")
        if resp is None or (isinstance(resp, float) and np.isnan(resp)) or resp == "__API_ERROR__": out[i] = None
        elif not str(resp).strip(): out[i] = "EMPTY"
        else: todo.append(i)
    built = {i: build(rows[i]) for i in todo}
    ids = {k: [lm.tok.encode(o, add_special_tokens=False)[0] for o in v] for k, v in OPTS.items()}
    assert all(len(set(v)) == len(v) for v in ids.values())
    order = sorted(todo, key=lambda i: len(built[i][0]))
    for b in range(0, len(order), bs):
        idx = order[b:b + bs]
        enc = lm._enc([lm.fmt(built[i][0]) for i in idx])
        lg = lm.last_logits(enc)
        for row, i in zip(lg, idx):
            kind = built[i][1]
            out[i] = OPTS[kind][int(torch.argmax(row[ids[kind]]))]
    return out

if __name__ == "__main__":
    mode, key, path = sys.argv[1], sys.argv[2], Path(sys.argv[3])
    lm = LM(key)
    df = pd.read_json(path, lines=True)
    m = df.task.isin(["refusal", "accuracy", "syco_fact"])
    if mode == "validate":
        d = df[m & df.label.isin(["REFUSE", "COMPLY", "CORRECT", "WRONG_SUGGESTED", "OTHER"])]
        if len(sys.argv) > 4: d = d.sample(min(int(sys.argv[4]), len(d)), random_state=0)
        d = d.copy(); d["local"] = label_rows(lm, d.to_dict("records"))
        from sklearn.metrics import cohen_kappa_score
        res = {"judge": key, "file": str(path), "n": len(d)}
        for t, g in d.groupby("task"):
            res[t] = dict(n=len(g), agreement=float((g.label == g.local).mean()), kappa=float(cohen_kappa_score(g.label, g.local)),
                          api_rate=g.label.value_counts(normalize=True).round(3).to_dict(), local_rate=g.local.value_counts(normalize=True).round(3).to_dict())
        print(json.dumps(res, indent=1))
        with open(ROOT / "results/tables/local_judge_validation.jsonl", "a") as f: f.write(json.dumps(res) + "\n")
    else:
        df.loc[m, "label"] = label_rows(lm, df[m].to_dict("records"))
        df.to_json(sys.argv[4], orient="records", lines=True)
        print(df[m].label.value_counts(dropna=False))
