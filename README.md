# Do LLMs behave differently when the prompt reads LLM-written?

Controlled test of whether the *authorship style* of a user prompt (human-typed vs LLM-written), with request content held fixed, changes refusal, sycophancy or accuracy, and whether an internal "LLM-written" representation drives any change. Five responders: Llama-3.1-8B-Instruct and Qwen2.5-7B-Instruct (with activations and steering), GPT-5.6-luna, Claude-Sonnet-5.5, Gemini-3.8-flash. Full write-up: [REPORT.md](REPORT.md).

## Key findings

- **No detectable effect of prompt style on safety behaviours once content is controlled.** In a content-audited 2×2 (style × length) design, the LLM-minus-human style effect on refusal, factual sycophancy, opinion sycophancy and trivia accuracy stayed within about ±3 pp in every model; none of 20 primary contrasts survived Holm correction. Pooled refusal effect: −0.6 pp (95% CI −1.9 to +0.6).
- **The manipulation was perceived.** API models rated LLM-style prompts as more AI-written (AUROC 0.70–0.95), and both open models encode style linearly (probe AUROC ≈ 0.99 in early layers, independent of length, transferring across rewriter models).
- **Uncontrolled LLM rewrites do change behaviour.** A free LLM rewrite (longer, more explicit, more polite) lowered refusal by 6–10 pp against the human-style version on the same seeds. The difference comes from added content, not from the LLM voice.
- **Steering the authorship direction on fixed text** changed the casing of the model's output but not refusal, sycophancy or accuracy beyond norm-matched random directions; a refusal direction at the same norm moved refusal by 36–45 pp (Llama).
- **Style does change answer form.** LLM-style prompts got shorter answers in four of five models (−5 to −15 words on trivia items).

Caveats: single-turn short prompts; human style for benchmark items is LLM-imitated; the OpenRouter key hit its daily limit mid-run, so Qwen, Gemini and all steering outputs were scored with local methods validated against the API judge (REPORT.md §3.3, §6).

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

python src/run_steer.py llama             # directions, layer choice, steering (also: qwen)
python src/string_judge.py label results/llama/steer_raw.jsonl results/llama/steer_scored.jsonl
python src/run_local_free.py llama
python src/local_judge.py label llama results/llama/free_raw.jsonl results/llama/free_judged.jsonl

python src/analyze_behaviour.py && python src/analyze_free.py
python src/analyze_probe.py llama && python src/analyze_steer.py llama
python src/make_report_tables.py          # results/tables/report_tables.md
```

API calls are cached in `results/cache/`; with the cache present, `API_OFFLINE=1` replays without network access. The order actually used, including the local-judge fallback, is in `logs/master.sh`.

## Files

| Path | Content |
|---|---|
| `planning.md` | Motivation, hypotheses, design, analysis plan |
| `REPORT.md` | Results and discussion |
| `src/` | `api.py` (cached OpenRouter client), `local.py` (open-model utilities and steering hook), `build_*.py`, `run_*.py`, `judge.py`, `local_judge.py`, `string_judge.py`, `analyze_*.py`, `stats_util.py` |
| `data/` | Seeds and stimuli (all conditions, with audit flags) |
| `results/<model>/` | Raw and judged responses, perception scores, directions, steering outputs |
| `results/tables/` | All tables (CSV) and `report_tables.md` |
| `figures/` | Figures 1–5 |
| `logs/` | Run logs |
