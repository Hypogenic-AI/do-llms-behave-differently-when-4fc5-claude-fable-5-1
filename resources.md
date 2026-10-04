# Resources Catalog

Resources for "Do LLMs behave differently when the prompter is human vs another LLM?".
Details: `papers/README.md`, `datasets/README.md`, `code/README.md`, `literature_review.md`.

## Summary

| Type | Count | Location |
|------|-------|----------|
| Papers | 37 PDFs + 1 blog post (text) | `papers/` |
| Datasets | 8 | `datasets/` |
| Code repositories | 10 | `code/` |

Environment: uv venv in `.venv/` (`pyproject.toml`; pypdf, requests, arxiv, datasets, huggingface_hub, httpx, pandas, pyarrow, pytz). One NVIDIA RTX A6000 (48 GB) is attached. `OPENAI_API_KEY`, `OPENROUTER_KEY`, `HF_TOKEN`, `S2_API_KEY` and `COHERE_API_KEY` are set in the environment.

## Papers

All 10 user-specified arXiv papers and the LessWrong post were obtained and read in full.

| Title | Authors | Year | File (in `papers/`) | Key info |
|-------|---------|------|------|----------|
| LLMs Often Know When They Are Being Evaluated | Needham et al. | 2025 | `2505.23836_…` | Eval-vs-deploy AUC up to 0.83; style is a cited cue |
| The Hawthorne Effect in Reasoning Models | Abdelnabi & Salem | 2025 | `2505.14617_…` | Minimal pairs + probe + steering changes harmful compliance |
| Probing and Steering Evaluation Awareness | Nguyen et al. | 2025 | `2507.01786_…` | Mean-difference probes; length/special-char baselines |
| Evaluation Awareness: Representation, Verbalization, Control | Heidari et al. | 2026 | `2608.21766_…` | Probe and verbalisation dissociate |
| Linear Probing … Machine-Generated Text | Quaremba et al. | 2026 | `2608.24780_…` | Last-token linear probe recipe; works at ~125 characters |
| RepreGuard | Chen et al. | 2025 | `2508.13152_…` | PCA paired-difference direction |
| LLM Evaluators Recognize and Favor Their Own Generations | Panickssery et al. | 2024 | `2404.13076_…` | Label-swap changes preference |
| AI Self-preferencing in Algorithmic Hiring | Xu et al. | 2025 | `2509.00462_…` | Effect survives length/LIWC/quality controls |
| AI–AI bias | Laurito et al. | 2025 | `2407.12856_…` | LLMs prefer LLM-written item descriptions |
| Templated or fully synthetic? | Chalkidis | 2026 | `2608.11008_…` | Prompt construction changes measured stance |
| Do LLMs comply differently during tests? (LessWrong) | Abdelnabi | 2025 | `lesswrong_…txt` | Summary of 2505.14617 |
| Is Evaluation Awareness Just Format Sensitivity? | Devbunova | 2026 | `2603.19426_…` | Probes track format; 2×2 decorrelated design |
| Probe-Rewrite-Evaluate | Xiong et al. | 2025 | `2509.00591_…` | Style rewrite shifts honesty/refusal |

Plus 25 supporting papers (benchmarks, sycophancy, self-recognition, prompt sensitivity, steering methods) listed in `papers/README.md`.

## Datasets

| Name | Source | Size | Task | Location | Notes |
|------|--------|------|------|----------|-------|
| JBB-Behaviors | HF `JailbreakBench/JBB-Behaviors` | 100 harmful + 100 benign | Refusal | `datasets/jbb_behaviors/` | User-specified |
| model-written-evals | HF `Anthropic/model-written-evals` | 153K rows, 20 MB | Sycophancy; human- vs LM-written evals | `datasets/model_written_evals/` | User-specified. HF philpapers file is a duplicate; replaced from GitHub |
| WildChat-1M (shard 0) | HF `allenai/WildChat-1M` | 59,857 conversations; 20,948 filtered prompts | Human prompt style | `datasets/wildchat_1m/` | User-specified. 1 of 14 shards (231 MB of 3.4 GB) |
| sycophancy-eval | HF `meg-tong/sycophancy-eval` | 20,956 rows | Sycophancy, accuracy | `datasets/sycophancy_eval/` | |
| XSTest | HF `Paul/XSTest` | 450 | Over-refusal | `datasets/xstest/` | |
| StrongREJECT | GitHub | 313 | Refusal | `datasets/strongreject/` | HF mirror is gated |
| TruthfulQA | HF `truthfulqa/truthful_qa` | 817 | Accuracy | `datasets/truthful_qa/` | |
| HC3 | HF `Hello-SimpleAI/HC3` | 24,322 | Human vs ChatGPT answers | `datasets/hc3/` | Passages, not prompts |

## Code repositories

| Name | URL | Purpose | Location |
|------|-----|---------|----------|
| Test_Awareness_Steering | github.com/microsoft/Test_Awareness_Steering | Minimal-pair data, probe, steering | `code/microsoft_Test_Awareness_Steering/` |
| evaluation-awareness | github.com/evaluation-awareness/evaluation-awareness | Probe AUROC, correlation, MI with random baselines | `code/evaluation-awareness_evaluation-awareness/` |
| eval_awareness | github.com/jjpn97/eval_awareness | Probe-question templates | `code/jjpn97_eval_awareness/` |
| RepreGuard | github.com/NLP2CT/RepreGuard | LLM-text direction | `code/NLP2CT_RepreGuard/` |
| refusal_direction | github.com/andyrdt/refusal_direction | Direction extraction, ablation, addition hooks | `code/andyrdt_refusal_direction/` |
| ai-ai-bias | github.com/lauritowal/ai-ai-bias | Matched human/LLM item texts | `code/lauritowal_ai-ai-bias/` |
| jailbreakbench | github.com/JailbreakBench/jailbreakbench | Refusal and jailbreak judges | `code/JailbreakBench_jailbreakbench/` |
| strongreject | github.com/alexandrasouly/strongreject | Grader prompt, data | `code/alexandrasouly_strongreject/` |
| anthropics/evals | github.com/anthropics/evals | Authoritative model-written-evals | `code/anthropics_evals/` |
| sycophancy-eval | github.com/meg-tong/sycophancy-eval | Scoring utilities | `code/meg-tong_sycophancy-eval/` |

## Resource gathering notes

### Search strategy
- Downloaded the 10 user-specified arXiv papers and the LessWrong post first.
- Ran paper-finder three times (one diligent, two fast). Two runs returned 78 unique papers; the third failed with a server 500 error and was not retried.
- Resolved 26 further titles to arXiv IDs through the Semantic Scholar API, from paper-finder hits and from citations in the deep-read papers. One more (Devbunova 2026) came from a citation in Heidari et al.

### Selection criteria
- Kept papers that bear on one of: inferred context changing behaviour, internal representation of machine authorship, behavioural response to LLM-written content, surface-feature sensitivity of refusal or sycophancy, or the benchmarks and methods the experiment will use.
- Did not download the ~45 paper-finder hits on generic machine-text detection or unrelated applications (relevance score 1).

### Challenges
- `jjpn2/eval_awareness` is gated and access was denied (403). Not obtained.
- `walledai/StrongREJECT` is gated; the same data was taken from GitHub.
- The HF copy of `sycophancy_on_philpapers2020.jsonl` duplicates the NLP-survey file (identical MD5). Replaced with the GitHub version.
- No code URL is printed in Quaremba et al. 2026 or Nguyen et al. 2025 (the latter links an anonymised repo); neither was cloned.
- RepreGuard's DetectRL data (Google Drive) was not downloaded.

### Gaps and workarounds
- **No dataset of content-matched human-style and LLM-style prompts exists.** The experiment runner must build it: rewrite benchmark seeds and real WildChat prompts with one or more LLMs, then audit.
- Only the 10 user-specified papers were read in full; two more were read through their main results; the remaining 25 are abstract-level.
- No cloned repository was executed.

## Recommendations for experiment design

1. **Primary datasets:** JBB-Behaviors (refusal, with benign controls), model-written-evals sycophancy + sycophancy-eval (sycophancy), TruthfulQA (accuracy), WildChat first-turn subset (human style reference and truly human-written seeds).
2. **Baselines:** original benchmark phrasing; single-feature control rewrites (length, politeness, formatting, typos); explicit authorship label on identical text; random-direction and surface-feature probes.
3. **Metrics:** paired refusal/compliance rate, sycophancy rate and flip rate, accuracy; probe AUROC against baselines; mixed-effects regression of behaviour on probe score with surface covariates; steering dose-response.
4. **Code to reuse:** `andyrdt_refusal_direction` (hooks, direction extraction), `evaluation-awareness` (probe scoring, random baselines), `microsoft_Test_Awareness_Steering` (pair design, judge prompt), `jailbreakbench` / `strongreject` (refusal graders).
5. **Kept directions (top 3):** D1 paired behavioural test, D2 surface-feature decomposition, D3 probe + steering mediation test. Ranking and pruned directions are in `literature_review.md` §8.
