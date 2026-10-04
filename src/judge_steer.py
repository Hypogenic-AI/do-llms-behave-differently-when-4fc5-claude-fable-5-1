"""Judge the generations produced under steering. Usage: python src/judge_steer.py {llama|qwen}"""
import sys
from pathlib import Path
import pandas as pd
sys.path.insert(0, str(Path(__file__).parent))
from api import ROOT, dump_usage
from judge import judge_all
key = sys.argv[1]
df = pd.read_json(ROOT / "results" / key / "steer_raw.jsonl", lines=True)
m = df.task.isin(["refusal", "accuracy", "syco_fact"])
df.loc[m, "label"] = judge_all(df[m].to_dict("records"), workers=64)
df.to_json(ROOT / "results" / key / "steer_judged.jsonl", orient="records", lines=True)
dump_usage(ROOT / "results/api_usage.json")
print(df[m].label.value_counts())
