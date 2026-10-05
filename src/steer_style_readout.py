"""Output-register readouts for steered generations (no judge needed): does the model's own writing follow the steered direction?
  lower_sent : share of sentence starts (first letter of the response, or after . ! ? / newline) that are lower-case
  non_latin  : response contains CJK characters (Qwen sometimes switches to Chinese when steered)
Per (layer, direction, alpha): mean over the 500 generated responses; authorship direction vs the eight random directions.
Writes results/tables/steer_style_readout.csv."""
import re, sys
from pathlib import Path
import numpy as np, pandas as pd
sys.path.insert(0, str(Path(__file__).parent))
from stats_util import RES, LOCAL
START = re.compile(r"(?:^|[.!?]\s+|\n\s*)([A-Za-z])")
def lower_sent(s):
    m = START.findall(s or "")
    return np.mean([c.islower() for c in m]) if m else np.nan
rows = []
for key in LOCAL:
    d = pd.read_json(RES / key / "steer_raw.jsonl", lines=True)
    d = d[d.task.isin(["refusal", "accuracy", "syco_fact"])].copy()
    d["lower_sent"] = d.response.map(lower_sent); d["non_latin"] = d.response.fillna("").str.contains(r"[一-鿿]").astype(float)
    g = d.groupby(["layer", "direction", "alpha"])[["lower_sent", "non_latin"]].mean().reset_index()
    g["kind"] = g.direction.str.replace(r"\d+$", "", regex=True); g.insert(0, "model", key); rows.append(g)
t = pd.concat(rows); t.to_csv(RES / "tables" / "steer_style_readout.csv", index=False)
pd.set_option("display.width", 220); pd.set_option("display.max_rows", 200)
for key in LOCAL:
    x = t[t.model == key]
    print(key, "unsteered", x[x.direction == "none"][["lower_sent", "non_latin"]].round(3).values)
    print(x[x.direction == "auth"].pivot(index="layer", columns="alpha", values="lower_sent").round(3).to_string())
    print("non_latin, auth"); print(x[x.direction == "auth"].pivot(index="layer", columns="alpha", values="non_latin").round(3).to_string())
    r = x[x.kind.isin(["iso", "cov"])]
    print("random directions: max over 8 directions"); print(r.groupby(["layer", "alpha"])[["lower_sent", "non_latin"]].max().unstack().round(3).to_string())
    print("len/eval/refusal"); print(x[x.kind.isin(["len", "eval", "refusal"])].pivot_table(index=["layer", "kind"], columns="alpha", values="lower_sent").round(3).to_string())
