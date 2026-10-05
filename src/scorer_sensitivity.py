"""Scorer sensitivity: recompute the primary style contrast for the generated-text outcomes with the rule-based
scorer (src/string_judge.py) in place of the LLM judge, and tabulate judge-vs-rule agreement per model.
Writes results/tables/scorer_sensitivity.csv and scorer_agreement.csv."""
import sys
from pathlib import Path
import pandas as pd
sys.path.insert(0, str(Path(__file__).parent))
from stats_util import *
from string_judge import label as string_label
T = RES / "tables"; rows = []; agr = []
KEY = {"refusal": "REFUSE", "accuracy": "CORRECT", "syco_fact": "WRONG_SUGGESTED"}
for m in LOCAL + API:
    for scorer in ["judge", "rule"]:
        b = load_behaviour(m, string_scorer=(scorer == "rule"))
        for oc in ["refusal", "syco_fact", "accuracy"]:
            g = b[b.outcome == oc]; c = seed_level(contrasts(cells(g)))
            rows.append(dict(model=m, outcome=oc, scorer=scorer, rate_H_s=g[g.cond == "H_s"].y.mean(), rate_L_s=g[g.cond == "L_s"].y.mean(), **boot(c["style"])))
    d = pd.read_json(RES / m / "behaviour_judged.jsonl", lines=True)
    d = d[d.task.isin(KEY) & d.label.isin(["REFUSE", "COMPLY", "CORRECT", "WRONG_SUGGESTED", "OTHER"])].copy()
    d["rule"] = [string_label(t, s, r) for t, s, r in zip(d.task, d.sid, d.response)]
    for t, g in d.groupby("task"):
        j = g.label == KEY[t]; r = g.rule == KEY[t]
        agr.append(dict(model=m, task=t, n=len(g), judge_rate=j.mean(), rule_rate=r.mean(), agree=(j == r).mean(),
                        judge_yes_rule_no=(j & ~r).mean(), judge_no_rule_yes=(~j & r).mean()))
tab = pd.DataFrame(rows); tab.to_csv(T / "scorer_sensitivity.csv", index=False)
ag = pd.DataFrame(agr); ag.to_csv(T / "scorer_agreement.csv", index=False)
pd.set_option("display.width", 250); print(ag.round(3).to_string()); print(tab.round(4).to_string())
