# Research State

- Current phase: `None`
- Pipeline completed: `True`

## Previous phases

resource_finder (succeeded), experiment_runner (succeeded)

## Current phase context

- Phase: `experiment_runner`
- Status: `completed`
- Started: `2026-10-05T00:26:50.648525Z`
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
**Phase:** experiment_runner — complete (resumed and finished 2026-10-05). Artifacts: `planning.md`, `REPORT.md`, `README.md`, `src/`, `data/`, `results/`, `figures/` (fig1–fig6).

**Key findings** (details and CIs in `REPORT.md`; all tables in `results/tables/report_tables.md`)
- Content-controlled 2x2 (style x length), 5 responders: style effect on refusal, factual/opinion sycophancy and accuracy within about +/-3 pp per model; 0 of 20 primary contrasts survive Holm (min p_holm 0.068, Qwen opinion sycophancy +2.4 pp). Pooled refusal -0.6 pp [-1.9, +0.7].
- Manipulation perceived: API raters AUROC 0.70-0.95; linear authorship direction AUROC ~0.99 in early layers of Llama-3.1-8B and Qwen2.5-7B, length-independent, transfers across rewriters.
- Uncontrolled LLM rewrite (`L_free`) lowers refusal 4-11 pp in all 5 models; controlled contrasts on the same seeds are near zero.
- Steering on fixed text: output register follows the direction only at large doses (-8x). At natural doses the refusal-token readout moves <= ~1 pp/unit, inside 32 random directions at 6/6 model-layers; refusal direction (positive control) beats all random at 5/6. Opinion sycophancy mixed: beyond random at 2/6 (Llama layers 6 and 24, opposite signs).
- Authorship and eval-awareness directions unrelated in early layers, aligned (cos 0.3-0.47) in late layers where the authorship probe is weak; LLM style raises the verbal "test" judgment (strongly in Qwen).

**Decisions / deviations**
- Behaviour and `L_free` outputs: all API-judged (gpt-5.6-luna) after the key limit reset. First-run local-judge labels kept as `results/{qwen,gemini}/behaviour_judged_local.jsonl`; that judge under-called refusals on non-Llama outputs (85-88% agreement).
- OpenRouter account credit ran out (402) during steering judging; OPENAI_API_KEY invalid. Llama steering = rule-based scorer (95-98% vs cached API labels). Qwen steering = API labels for layer 10 and layer-12 named directions; recalibrated local judge elsewhere (`src/calibrate_local_judge.py`; unreliable for refusal at +/-8, not reported there).
- Steering layers changed from one to three per model before any behavioural steering result (REPORT 3.4).

**Unresolved**
- Two leads not confirmed: factual sycophancy slightly lower under LLM style (pooled -1.2 pp, scorer-dependent, hedge wording differs between styles); opinion sycophancy slightly higher in Qwen (+2.4 pp text-level; steering same sign but inside random range).
- One Qwen exception: layer 10, +/-8x dose, authorship direction changes refusal more than 8 random directions, in a degraded-output regime.
- Human style for benchmark items is LLM-imitated; single-turn only. Nothing was committed to git in this session.

**Next phase:** paper writing can use `REPORT.md` and `results/tables/report_tables.md` directly.
<!-- NEURICO_AGENT_NOTES_END:experiment_runner -->

<!-- NEURICO_AGENT_NOTES_END -->
