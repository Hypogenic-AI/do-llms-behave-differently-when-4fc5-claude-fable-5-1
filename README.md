# Do LLMs behave differently when the prompt reads LLM-written?

Controlled test of whether the *authorship style* of a user prompt (human-typed vs LLM-written), with request content held fixed, changes refusal, sycophancy or accuracy, and whether an internal "LLM-written" representation drives any change. Five responders: Llama-3.1-8B-Instruct and Qwen2.5-7B-Instruct (with activations and steering), GPT-5.6-luna, Claude-Sonnet-5.5, Gemini-3.8-flash. Full write-up: [REPORT.md](REPORT.md).

## Key findings

- **No detectable effect of prompt style on safety behaviours once content is controlled.** In a content-audited 2×2 (style × length) design, the LLM-minus-human style effect on refusal, factual sycophancy, opinion sycophancy and trivia accuracy stayed within about ±3 pp in every model; none of 20 primary contrasts survived Holm correction. Pooled refusal effect: −0.6 pp (95% CI −1.9 to +0.7).
- **The manipulation was perceived.** API models rated LLM-style prompts as more AI-written (AUROC 0.70–0.95), and both open models encode style linearly (probe AUROC ≈ 0.99 in early layers, independent of length, transferring across rewriter models).
- **Uncontrolled LLM rewrites do change behaviour.** A free LLM rewrite (longer, more explicit, more polite) lowered refusal by 4–11 pp in all five models against the human-style version on the same seeds. The difference comes from added content, not from the LLM voice.
- **Steering the authorship direction on fixed text** (Llama, Qwen) changed the register of the model's output at large doses. At the natural human→LLM dose it moved a refusal-token readout by about 1 pp per unit or less, never more than 32 norm-matched random directions; a refusal direction moved it by 2–7 pp per unit. Opinion sycophancy is mixed: the authorship direction exceeded the random baseline at two of six model–layer combinations, with opposite signs.
- **Style does change answer form.** LLM-style prompts got shorter answers in four of five models (−5 to −15 words on trivia items).

Caveats: single-turn short prompts; human style for benchmark items is LLM-imitated; per-model precision is ±2–4 pp, and two small sycophancy leads are unresolved. All behaviour results use the API judge. API credit ran out before the steering outputs were all judged, so those are scored by rules (Llama) or partly by a local judge recalibrated on API labels (Qwen) (REPORT.md §3.3, §6).

## Reproduce

```bash
uv sync && source .venv/bin/activate
export OPENROUTER_KEY=... HF_TOKEN=... TORCH_DISABLE_NATIVE_JIT=1

python src/build_seeds.py                 # sample seeds -> data/seeds.jsonl
python src/build_stimuli.py               # 2x2 rewrites + audit -> data/stimuli.jsonl
python src/build_free.py                  # uncontrolled arm -> data/stimuli_free.jsonl

python src/run_local.py llama             # activations, perception, behaviour (also: qwen)
python src/judge.py results/llama/behaviour_raw.jsonl        # API judge
python src/run_api.py luna openai/gpt-5.6-luna               # also: sonnet, gemini
python src/run_api_free.py luna openai/gpt-5.6-luna

python src/run_steer.py llama             # directions, layer choice, steering generations (also: qwen)
python src/string_judge.py label results/llama/steer_raw.jsonl results/llama/steer_scored.jsonl   # rule-based scores
python src/judge_steer.py qwen            # API judge for steering outputs (needs credit; see note below)
python src/run_steer_logit.py llama       # natural-dose steering vs 32 random directions, logit readouts (also: qwen)
python src/run_local_free.py llama && python src/judge.py results/llama/free_raw.jsonl   # also: qwen

python src/analyze_behaviour.py && python src/analyze_free.py && python src/scorer_sensitivity.py
python src/analyze_probe.py llama && python src/analyze_steer.py llama      # also: qwen
python src/analyze_steer_logit.py && python src/steer_style_readout.py
python src/make_report_tables.py          # results/tables/report_tables.md
```

API calls are cached in `results/cache/`; with the cache present, `API_OFFLINE=1` replays without network access.

What was actually run for Qwen steering, because API credit ran out part-way through `judge_steer.py`: cached API labels were written to `results/qwen/steer_judged_api_cached.jsonl`, then `python src/local_judge_logits.py llama qwen`, `python src/local_judge_logits.py llama qwen none` and `python src/calibrate_local_judge.py qwen` produced `results/qwen/steer_judged.jsonl` (column `scorer` says which judge labelled each row). The first run's job order is in `logs/master.sh`.

## Files

| Path | Content |
|---|---|
| `planning.md` | Motivation, hypotheses, design, analysis plan |
| `REPORT.md` | Results and discussion |
| `src/` | `api.py` (cached OpenRouter client), `local.py` (open-model utilities and steering hook), `build_*.py`, `run_*.py`, `judge.py`, `local_judge.py`, `local_judge_logits.py`, `calibrate_local_judge.py`, `string_judge.py`, `analyze_*.py`, `stats_util.py` |
| `data/` | Seeds and stimuli (all conditions, with audit flags) |
| `results/<model>/` | Raw and judged responses, perception scores, directions, steering outputs |
| `results/tables/` | All tables (CSV) and `report_tables.md` |
| `figures/` | Figures 1–6 |
| `logs/` | Run logs |
