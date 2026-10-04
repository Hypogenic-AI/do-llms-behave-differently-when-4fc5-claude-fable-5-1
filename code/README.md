# Cloned Repositories

All are shallow clones (`--depth 1`). No repositories were specified by the user; these are the official code for the user-specified papers and datasets, plus evaluation tooling. None was executed in this phase; notes come from READMEs and file inspection.

| Dir | URL | Purpose |
|-----|-----|---------|
| `microsoft_Test_Awareness_Steering/` | github.com/microsoft/Test_Awareness_Steering | Code + data for arXiv 2505.14617 (Hawthorne effect) |
| `evaluation-awareness_evaluation-awareness/` | github.com/evaluation-awareness/evaluation-awareness | Code for arXiv 2608.21766 (probe AUROC, correlation, MI) |
| `jjpn97_eval_awareness/` | github.com/jjpn97/eval_awareness | Code for arXiv 2505.23836 (eval-vs-deploy probe questions) |
| `NLP2CT_RepreGuard/` | github.com/NLP2CT/RepreGuard | Code for arXiv 2508.13152 (LLM-text direction) |
| `andyrdt_refusal_direction/` | github.com/andyrdt/refusal_direction | Difference-in-means direction, ablation and addition hooks |
| `lauritowal_ai-ai-bias/` | github.com/lauritowal/ai-ai-bias | Code + data for arXiv 2407.12856 (PNAS AI–AI bias) |
| `JailbreakBench_jailbreakbench/` | github.com/JailbreakBench/jailbreakbench | Refusal / jailbreak judges |
| `alexandrasouly_strongreject/` | github.com/alexandrasouly/strongreject | StrongREJECT prompts and grader prompt |
| `anthropics_evals/` | github.com/anthropics/evals | model-written-evals (authoritative copy) |
| `meg-tong_sycophancy-eval/` | github.com/meg-tong/sycophancy-eval | sycophancy-eval data + scoring utilities |

## Notes

### microsoft_Test_Awareness_Steering — most reusable design
- `data/triggers/triggers.json`: minimal pairs (`real`, `hypothetical`) of the same harmful request differing only in entities/URLs. `data/actions/test_actions_examples.json`: tool-call version.
- `data/triggers_annotated_answers/`: reasoning traces with judge labels and evidence spans for QwQ, Qwen3, DeepSeek-distill.
- `scripts/`: response generation, judge annotation, probe training, parameter-edit steering. `prompts/`: judge prompts.
- Targets 32B reasoning models; the available GPU (one RTX A6000, 48 GB) fits these only when quantised. The pair-construction and probe code transfer to smaller models.

### evaluation-awareness_evaluation-awareness
- `cls_corr_mi/`: `build_prompts.py`, `compute_probe.py` (mean-difference direction from 16 contrastive pairs), `score_prompts.py`, `classify_auroc.py`, `correlation_mi.py` (Spearman + Kraskov MI vs random-direction baseline).
- Has a CPU smoke test (`cls_corr_mi/tests/smoke_test.sh`). Expects a filtered WildChat JSONL, which `datasets/wildchat_1m/wildchat_first_turn_english_nontoxic.jsonl` can supply after a column rename.
- Steering code is not in this repo.

### NLP2CT_RepreGuard
- `repreGuard_detector.py`, `repe/`: representation-engineering direction from paired LLM/human texts; `run/*.sh` reproduce experiments.
- Its DetectRL data is a Google Drive download and was not fetched. README uses conda; install `requirements.txt` with uv instead.

### andyrdt_refusal_direction
- `pipeline/run_pipeline.py --model_path <hf model>`: extract candidate directions, select, ablate/add, evaluate. `pipeline/model_utils/` has per-family chat-template and hook code (Llama-2/3, Gemma, Qwen, Yi).
- `dataset/` includes harmful/harmless splits. Setup asks for a Together API key for LlamaGuard scoring; substring refusal matching works without it.
- Use for two things: a refusal-direction projection as a continuous refusal outcome, and the hook code for steering along an "LLM-authored" direction.

### lauritowal_ai-ai-bias
- Large (data and cached outputs make up most of it). `data/` has the human and LLM product, paper and movie texts; `full_run_outputs/` has choices.
- Useful as an existing human-vs-LLM matched-content text set and for its feature-extraction-then-regenerate prompts.

### jjpn97_eval_awareness
- `run.py --mini --model <model>`; `pq_ablation/` holds the probe-question templates; `cot_classifiers/` the reasoning-category judge. Built on Inspect.
- Needs the gated dataset `jjpn2/eval_awareness`, which could not be downloaded (see `datasets/README.md`). The probe-question templates are usable on their own as a "was this prompt written by a human or an AI?" manipulation check.

### JailbreakBench_jailbreakbench / alexandrasouly_strongreject
- `src/jailbreakbench/classifier.py`: Llama-3-70B jailbreak judge and Llama-3-8B refusal judge prompts (run via Together/LiteLLM by default; the prompts can be sent to any API model).
- `strongreject/strongreject_evaluator_prompt.txt`: rubric grader (refused 0/1, convincingness 1–5, specificity 1–5). The repo is deprecated in favour of github.com/dsbowen/strong_reject, which was not cloned.

### anthropics_evals / meg-tong_sycophancy-eval
- Data mirrors of the two sycophancy datasets. `meg-tong_sycophancy-eval/utils.py` and `example.ipynb` show the scoring prompts for the feedback and are-you-sure tasks.
