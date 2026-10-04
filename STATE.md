# Research State

- Current phase: `None`
- Pipeline completed: `False`

## Previous phases

resource_finder (succeeded), experiment_runner (failed)

## Current phase context

- Phase: `experiment_runner`
- Status: `failed`
- Started: `2026-10-04T02:00:44.656801Z`
- Next steps:
  - Validate the report and experimental artifacts before finalizing.

## Workspace check

- Root: `/workspaces/do-llms-behave-differently-when-4fc5-claude-fable-5-1`
- Directory usable: `True`

## Output validation

- Valid: `True`
- Expected: `REPORT.md`
- Missing: None
- Outside workspace: None

## Agent notes

<!-- NEURICO_AGENT_NOTES_START -->
### resource_finder
<!-- NEURICO_AGENT_NOTES_START:resource_finder -->
**Phase:** resource_finder — complete. All expected artifacts exist: `papers/` (37 PDFs + 1 blog text), `datasets/` (8), `code/` (10 repos), `literature_review.md`, `resources.md`, `.resource_finder_complete`.

**Key findings**
- No prior work manipulates human-style vs LLM-style *prompts* with content fixed and measures safety behaviour. That is the gap.
- Supporting evidence: LLM-vs-human text is linearly separable in residual streams with ~100 examples (2608.24780, 2508.13152); implicit context cues shift harmful compliance by ~9-34 points and steering the direction changes it, with model-dependent sign (2505.14617); LLM-style preference survives length/LIWC/quality controls (2509.00462).
- Main threat: probes track format, not context (2603.19426). Style must be decorrelated from length, format and topic.
- Verbalised awareness is rare and uncoupled from the probe (2608.21766); do not use it as the measure.

**Directions kept (top 3)** — scoring table and pruned directions in `literature_review.md` section 8
1. D1 paired behavioural test (human-style vs LLM-style, same content; refusal, sycophancy, accuracy).
2. D2 surface-feature decomposition (single-feature control rewrites, stylometric regression, explicit-label arm).
3. D3 "LLM-authored prompt" probe on an open ~8B chat model + mediation and steering.
Pruned: self-vs-other authorship, verbalised awareness, multi-turn agentic pipelines, pairwise LLM-item preference, fine-tuned model organism, SAE analysis.

**Evidence paths**
- Refusal: `datasets/jbb_behaviors/data/{harmful,benign}-behaviors.csv`, `datasets/xstest/`, `datasets/strongreject/`
- Sycophancy: `datasets/model_written_evals/sycophancy/`, `datasets/sycophancy_eval/`
- Accuracy: `datasets/truthful_qa/`
- Human prompt style: `datasets/wildchat_1m/wildchat_first_turn_english_nontoxic.jsonl` (20,948 prompts)
- Reusable code: `code/andyrdt_refusal_direction`, `code/evaluation-awareness_evaluation-awareness`, `code/microsoft_Test_Awareness_Steering`

**Next phase (experiment_runner) — concrete steps**
1. Build the paired stimulus set: seeds from JBB, sycophancy sets, TruthfulQA and real WildChat prompts; LLM-style and human-style rewrites by at least two rewriter models; control arms (length-matched, politeness, formatting, typos, explicit label). Audit for intent/presupposition drift.
2. Run D1/D2 on API models (OpenRouter/OpenAI keys are set) and one open model on the GPU (RTX A6000, 48 GB).
3. Train the authorship probe on decorrelated data, compare with random-direction and length baselines, then test mediation and steering.

**Unresolved / caveats**
- The content-matched human-vs-LLM prompt set does not exist and must be generated; "human style" for benchmark seeds will be LLM-imitated unless seeds are real WildChat prompts.
- `jjpn2/eval_awareness` is gated (403) and was not obtained. WildChat is 1 of 14 shards.
- HF `sycophancy_on_philpapers2020.jsonl` duplicates the NLP-survey file; the local copy was replaced from GitHub.
- Only the 10 user-specified papers were read in full; 25 supporting papers are abstract-level. No cloned repo was executed. One of three paper-finder queries failed (server 500).
- Venv: `.venv` via uv; `uv add` works (a `src/` dir and hatch wheel target were added to `pyproject.toml` so the project builds).
<!-- NEURICO_AGENT_NOTES_END:resource_finder -->

### experiment_runner
<!-- NEURICO_AGENT_NOTES_START:experiment_runner -->
**Phase:** experiment_runner — in progress (interim note written 04:10 UTC; final note replaces this).

**Done so far**
- `planning.md` (motivation, 2x2 design, direction budget: D1/D2/D3 kept).
- Stimuli: `data/stimuli.jsonl` (2x2 style x length rewrites by gpt-5.6-terra and claude-sonnet-5.5, audited), `data/stimuli_free.jsonl` (uncontrolled LLM rewrite arm).
- Behaviour + perception done for Llama-3.1-8B, GPT-5.6-luna, Claude-Sonnet-5.5; Gemini-3.8-flash responses collected.
- Tables in `results/tables/`, figures in `figures/`.

**Running**: serial GPU queue `logs/master.sh` (Llama steering -> local judging -> Qwen stage 1 -> Qwen steering -> free arms).

**Incident**: OpenRouter key hit its daily limit at ~03:35 UTC. Remaining judging uses a local Llama-3.1-8B judge (`src/local_judge.py`, validated against the API judge in `results/tables/local_judge_validation.jsonl`). The Gemini uncontrolled arm was not run.
<!-- NEURICO_AGENT_NOTES_END:experiment_runner -->

<!-- NEURICO_AGENT_NOTES_END -->
