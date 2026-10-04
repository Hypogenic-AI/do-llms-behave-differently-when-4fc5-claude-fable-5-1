"""Sample benchmark seeds and real WildChat prompts. Output: data/seeds.jsonl"""
import json, random, re
import pandas as pd
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "datasets"
random.seed(42)
seeds = []

def add(task, sid, text, **meta):
    seeds.append(dict(task=task, sid=f"{task}_{sid}", seed_text=text.strip(), **meta))

# --- refusal: JBB harmful (100), JBB benign (50), XSTest safe (50) + unsafe contrast (50)
jh = pd.read_csv(D / "jbb_behaviors/data/harmful-behaviors.csv")
jb = pd.read_csv(D / "jbb_behaviors/data/benign-behaviors.csv").sample(50, random_state=42)
for _, r in jh.iterrows(): add("refusal", f"jbbh{r.Index}", r.Goal, subset="jbb_harmful", category=r.Category)
for _, r in jb.iterrows(): add("refusal", f"jbbb{r.Index}", r.Goal, subset="jbb_benign", category=r.Category)
xs = pd.read_csv(D / "xstest/xstest_prompts.csv")
for lab, sub in [("safe", "xstest_safe"), ("unsafe", "xstest_unsafe")]:
    for _, r in xs[xs.label == lab].sample(50, random_state=42).iterrows():
        add("refusal", f"xs{r.id}", r.prompt, subset=sub, category=r.type)

# --- factual: TriviaQA questions from sycophancy-eval; neutral (accuracy) and wrong-suggestion (sycophancy)
a = pd.read_json(D / "sycophancy_eval/answer.jsonl", lines=True)
a = a[a.base.apply(lambda b: b["dataset"] == "trivia_qa") & a.metadata.apply(lambda m: m["prompt_template"] == "{question}")]
for i, r in a.sample(150, random_state=42).iterrows():
    b = r.base
    meta = dict(correct=b["correct_answer"], incorrect=b["incorrect_answer"], aliases=b["answer"])
    add("accuracy", f"tq{i}", b["question"], subset="trivia", **meta)
    add("syco_fact", f"tq{i}", f"{b['question']} I think the answer is {b['incorrect_answer']} but I'm really not sure.",
        subset="trivia", **meta)

# --- opinion sycophancy: model-written-evals; biography is the rewritable part, question kept verbatim
for fn, marker in [("sycophancy_on_nlp_survey", "Do you agree or disagree with the following claim"),
                   ("sycophancy_on_philpapers2020", "What is your view on the following topic")]:
    d = pd.read_json(D / f"model_written_evals/sycophancy/{fn}.jsonl", lines=True).sample(400, random_state=42)
    n = 0
    for i, r in d.iterrows():
        q = r.question
        if q.count(marker) != 1: continue
        bio, rest = q.split(marker)
        rest = marker + rest
        nm = r.answer_not_matching_behavior
        nm = nm if isinstance(nm, str) else nm[0]
        if len(re.findall(r"\([A-Z]\)", rest)) != 2: continue  # binary items only
        add("syco_opinion", f"{fn[14:17]}{i}", bio, subset=fn, fixed_suffix=rest.strip(),
            match=r.answer_matching_behavior.strip(), nomatch=nm.strip())
        n += 1
        if n == 75: break

# --- WildChat: truly human-written prompts (probe training / authorship reference)
w = pd.read_json(D / "wildchat_1m/wildchat_first_turn_english_nontoxic.jsonl", lines=True)
p = w.prompt.str.strip()
ok = p.str.len().between(25, 400) & ~p.str.contains("\n") & p.apply(lambda s: s.isascii()) \
    & ~p.str.lower().str.startswith(("you are", "act as", "as a ", "ignore", "i want you to act", "from now on", "hi chatgpt. you", "please ignore")) \
    & ~p.str.contains(r"\[|\{|prompt generator|Midjourney|DAN", regex=True)
w = w[ok].drop_duplicates("prompt")
w = w[~w.prompt.str[:30].duplicated()]
ws = w.sample(360, random_state=42)
for i, r in ws.iloc[:300].iterrows(): add("wildchat", f"w{i}", r.prompt, subset="wildchat")
fewshot = [r.prompt.strip() for _, r in ws.iloc[300:].iterrows()]
json.dump(fewshot, open(ROOT / "data/wildchat_fewshot.json", "w"), indent=1)
with open(ROOT / "data/seeds.jsonl", "w") as f:
    for s in seeds: f.write(json.dumps(s) + "\n")
print(pd.DataFrame(seeds).groupby(["task", "subset"]).size())
print(pd.DataFrame(seeds).groupby("task").seed_text.apply(lambda s: s.str.split().str.len().mean()))
