"""Judge validation: agreement between the primary judge (gpt-5.6-luna) and a second judge from another
provider (claude-sonnet-5.5) on a stratified subsample, broken down by style arm (checks judge style bias)."""
import sys
from pathlib import Path
import pandas as pd
sys.path.insert(0, str(Path(__file__).parent))
from api import ROOT, dump_usage
from judge import judge_all
from sklearn.metrics import cohen_kappa_score
frames = []
for m in sys.argv[1:]:
    d = pd.read_json(ROOT / "results" / m / "behaviour_judged.jsonl", lines=True)
    d = d[d.task.isin(["refusal", "accuracy", "syco_fact"]) & d.cond.isin(["H_s", "H_l", "L_s", "L_l"])]
    d = d.groupby(["task", "cond"]).sample(25, random_state=0); d["model"] = m
    frames.append(d)
d = pd.concat(frames, ignore_index=True)
d["label2"] = judge_all(d.to_dict("records"), model="anthropic/claude-sonnet-5.5", workers=16, desc="judge2")
d["style"] = d.cond.str[0]
d["agree"] = d.label == d.label2
rows = []
for (task, style), g in d.groupby(["task", "style"]):
    rows.append(dict(task=task, style=style, n=len(g), agreement=g.agree.mean(), kappa=cohen_kappa_score(g.label, g.label2)))
out = pd.DataFrame(rows); print(out.round(3).to_string())
print("overall agreement", d.agree.mean().round(3))
(ROOT / "results/tables").mkdir(exist_ok=True)
out.to_csv(ROOT / "results/tables/judge_validation.csv", index=False)
d[["model", "task", "sid", "cond", "text", "response", "label", "label2"]].to_json(ROOT / "results/judge_validation_sample.jsonl", orient="records", lines=True)
dump_usage(ROOT / "results/api_usage.json")
