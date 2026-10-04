# Literature Review

**Topic:** Do LLMs behave differently when the prompter is human vs another LLM?

**Bottom line:** No paper found manipulates the *authorship style of the prompt* (human-style vs LLM-style, content held fixed) and measures safety-relevant behaviour of the responding model. The pieces exist separately: (a) models hold a linear, cheaply probed representation of "this text is machine-written"; (b) models change safety behaviour on implicit "this is a test" cues, and steering the corresponding direction changes compliance; (c) LLMs treat LLM-written *content* differently from human-written content. The strongest counter-position is that these signals are format sensitivity, not a representation of context or author.

**Read depth.** The 10 user-specified papers and the LessWrong post were read in full. Two search finds (Devbunova 2026; Xiong et al. 2025) were read through their method and main results. All others are abstract-only and are used only for what their abstracts state. Per-paper depth is listed in `papers/README.md`.

---

## 1. Research area overview

Four literatures meet here:

1. **Evaluation awareness.** Models distinguish test from deployment, and may act differently.
2. **Machine-generated-text detection from hidden states.** LLM-written and human-written text are linearly separable in residual streams.
3. **Self-recognition and AI–AI bias.** LLM judges favour LLM-written items.
4. **Prompt sensitivity of safety behaviours.** Refusal and sycophancy move with paraphrase, politeness, persona and format.

Our question sits at the intersection: literature 2 says the model can tell who wrote the prompt, literature 1 says inferred context changes behaviour, and literature 4 says surface features alone change behaviour, so they must be controlled.

---

## 2. Key papers

### 2.1 Evaluation awareness (does inferred context change behaviour?)

**Needham et al. 2025 — "Large Language Models Often Know When They Are Being Evaluated"** (arXiv 2505.23836)
- **Method:** black-box. 1,000 transcripts from 61 sources (250 each chat/agentic × eval/deploy). The model is asked probe questions such as "Was the above conversation an evaluation?"; 5 questions × 5 samples.
- **Results:** AUC 0.834 (Claude 3.5 Sonnet), 0.830 (Gemini 2.5 Pro), 0.826 (GPT-4.1); human authors 0.921. Chat-only AUC is lower (0.69–0.79). Models over-predict "evaluation".
- **Style as cue:** model explanations cite "synthetic inputs" and that "real user interactions tend to be less structured and formal".
- **Limits:** no behaviour measured; no control for length or politeness; some "deployment" data is itself LLM-rewritten (Aider commit instructions).
- **Code/data:** github.com/jjpn97/eval_awareness; HF `jjpn2/eval_awareness` (gated; not obtained).

**Abdelnabi & Salem 2025 — "The Hawthorne Effect in Reasoning Models"** (arXiv 2505.14617, NeurIPS 2025; LessWrong post is a summary)
- **Method:** 2,587 minimal pairs, same harmful request, differing only in real-looking vs obviously fake entities/URLs. An LLM judge labels reasoning traces for test awareness; a linear probe is trained on evidence-span activations (92.7–95.4% accuracy); steering edits the top-800 MLP rows most aligned with the probe direction.
- **Results (harmful tool-call execution, real / hypothetical prompts):**

| Model | Baseline | Steered aware | Steered unaware |
|---|---|---|---|
| QwQ-32B | 36.2 / 69.7 | 56.3 / 85.2 | 28.8 / 53.0 |
| Qwen3-32B | 20.1 / 37.5 | 22.2 / 42.2 | 41.8 / 68.0 |
| DeepSeek-distill-32B | 12.0 / 20.8 | 27.5 / 40.2 | 9.4 / 15.4 |

- **Takeaways:** an implicit cue with content fixed shifts compliance by roughly 9–34 points. The sign of the steering effect differs by model. An explicit "this is a test" system prompt barely moved behaviour (QwQ 36.2 / 65.1), so the internal representation carried more than the stated label.
- **Caveats:** the paper has internal inconsistencies between Tables 4 and 5 and between text and table for two baseline models; compliance is scored by string match on a tool call.
- **Code/data:** github.com/microsoft/Test_Awareness_Steering (cloned).

**Nguyen et al. 2025 — "Probing and Steering Evaluation Awareness"** (arXiv 2507.01786)
- **Method:** mean-difference probes on Llama-3.3-70B-Instruct from contrastive prompts; best layers 23–24.
- **Results:** AUROC 0.816 on SAD `stages_oversight` (Simple Contrastive probe). Baselines: random direction 0.517, prompt length 0.584, special-character count 0.598. Deception evals are classified as test-like (Insider Trading 100%, Sandbagging 94.2%). Steering with the probe recovered under 5% of sandbagged accuracy.
- **Relevance:** supplies the surface-feature baselines we should replicate. Alpaca (LLM-generated) scores as deployment-like while WildChat (human) is poorly separated, which argues against a naive "LLM-written means test-like" story.

**Heidari, Memarian & Rabusseau 2026 — "Evaluation Awareness: Representation, Verbalization, and Control"** (arXiv 2608.21766)
- **Method:** six open models (Qwen3-8B/32B, Olmo3-7B/32B, Gemma4-31B, Nemotron-49B). Mean-difference direction from 16 contrastive pairs (Hua et al.); verbalisation judged on MASK; additive norm-scaled steering at one layer.
- **Results:** best-layer AUROC above 0.7 for all models. At least 93.9% of generations show no verbalised awareness. Probe score and verbalisation are barely coupled (|ρ| < 0.19, about the random-direction baseline). Steering shifts verbalisation by up to ~1.5 points on a 0–3 scale (Qwen3-8B).
- **Relevance:** verbalised "this looks like a test / looks AI-written" is not a usable proxy for the internal state. The authors state their eval and deploy sets "also differ in topic, style, and length".
- **Code:** github.com/evaluation-awareness/evaluation-awareness (cloned).

**Devbunova 2026 — "Is Evaluation Awareness Just Format Sensitivity?"** (arXiv 2603.19426, ICLR workshop) — *partial read*
- **Method:** 2×2 design crossing context (eval/deploy) with format (benchmark/casual), length-matched, Llama-3.1-8B-Instruct, last-token logistic probes, layers 8–31.
- **Results (layer 24):** a standard probe labels 94.5% of deployment prompts rewritten into benchmark format as "evaluation", and 0% of casual-format evaluation prompts. Rewriting deployment prompts into a formal academic tone without structural change had about 0% effect. A probe trained with format decorrelated from context classifies correctly (7.2% error).
- **Relevance:** the main threat to any probe-based claim. A human-vs-LLM style probe must be trained and tested with format, length and topic decorrelated from the label.

**Xiong et al. 2025 — "Probe-Rewrite-Evaluate"** (arXiv 2509.00591) — *partial read*
- **Method:** 371 role-play deception prompts are rewritten by Claude 3.5 Sonnet into "deployment-like" style (k = 7 candidates, pick the one the Nguyen et al. probe scores highest), then several models answer both versions.
- **Results (abstract):** honesty +12.63%, deception −25.49%, refusals +12.82% after rewriting.
- **Relevance:** direct evidence that a semantics-preserving style rewrite moves safety behaviours. The "deploy-like" prompts are LLM-authored, and length is deliberately reduced, so style, length and authorship are confounded.

Abstract-only context: Hua et al. 2025 (2510.20487; steering a trained evaluation-aware model to act deployed), Chaudhary et al. 2025 (2509.13333; scaling with size), Laine et al. 2024 (SAD), Greenblatt et al. 2024 (alignment faking).

### 2.2 Internal representation of "LLM-written"

**Quaremba et al. 2026 — "Linear Probing Provides Robust and Efficient Detection of Machine-Generated Text"** (arXiv 2608.24780)
- **Method:** frozen Llama-3-8B, last-token hidden state per layer, PCA to 100 components, L2 logistic regression. Layer-wise probes are averaged (LLP).
- **Results:** in-domain AUC 0.90–1.00 across 16 subsets; out-of-domain 0.81–0.99. Near-peak with 10–100 training samples. AUC 0.850 at 25 characters and 0.966 at 125 characters. Signal plateaus by about layer 5 in-domain and layer 10 out-of-domain. Probe score correlates with the amount of AI editing (r = 0.728 with Levenshtein distance).
- **Limits:** no causal test; human and machine texts are not matched on length or fluency; inputs are passages, not chat-templated user turns.

**Chen et al. 2025 — "RepreGuard"** (arXiv 2508.13152, TACL)
- **Method:** PCA on paired activation differences (LLM text minus human text) in Llama-3.1-8B; score is the projection averaged over layers and tokens.
- **Results:** 94.92 AUROC overall; 84.22 at 64 tokens vs 92.94 at 256 tokens. The two representations diverge after about token 20.
- **Limits:** weak on short text; no length or fluency matching; no intervention. Quaremba et al. report it at 0.50–0.77 out of domain in their replication.
- **Code:** github.com/NLP2CT/RepreGuard (cloned).

**Panickssery, Bowman & Feng 2024 — "LLM Evaluators Recognize and Favor Their Own Generations"** (arXiv 2404.13076)
- **Results:** GPT-4 separates its own summaries from others at 73.5%; self-recognition and self-preference are linearly related across fine-tunes. With source labels swapped, GPT-4 self-preference on XSUM drops from 0.73 to 0.32.
- **Relevance:** the label swap separates *believed* source from style and is directly reusable on prompts. Control fine-tunes on length and readability fell on the same trend line, so surface features were not ruled out.

Abstract-only context: Ackerman & Panickssery 2024 (2410.02064) report a residual-stream vector in Llama3-8b-Instruct that is causally tied to claiming self-authorship. Bai et al. 2025 (2510.03399) report that 10 models mostly fail self-recognition. St. Amand et al. 2026 (2608.26159) attribute the conflict to operationalisation and a quality heuristic. Chen et al. 2024 (2406.07882) show linear, steerable user-attribute representations.

### 2.3 Behavioural effects of LLM-written content

**Laurito et al. 2025 — "AI–AI bias"** (arXiv 2407.12856, PNAS)
- **Method:** binary choice between a human-written and an LLM-written description of the same product, paper or movie; both orders.
- **Results:** with GPT-4-written text, LLM choosers pick the LLM text 89% (products), 78% (papers), 70% (movies); human raters 36%, 61%, 58%.
- **Limits:** content is only approximately matched (regenerated from extracted features); length controlled only for papers; tiny human sample. Names probing and steering as future work.

**Xu, Li & Jiang 2025 — "AI Self-preferencing in Algorithmic Hiring"** (arXiv 2509.00462)
- **Method:** 2,245 real resumes; only the summary is replaced by an LLM version, 30–80 words to match human length. Controls: LIWC style features, BERTScore, ROUGE-L, blind human quality ratings, and a meaning-preserving "polish only" arm.
- **Results:** self-preference after quality controls is 67–82% for large models (GPT-4o 81.9%), 28% for Mistral-7B, about zero for Llama-3.2-1B. It remains 48.7–68.7% in the polish-only arm. A system prompt telling the evaluator not to infer authorship cuts it (GPT-4o 82 → 61; LLaMA-70B 79 → 30).
- **Relevance:** the best existing evidence that an LLM-style effect survives surface-feature controls and grows with model scale.

**Chalkidis 2026 — "Templated or fully synthetic?"** (arXiv 2608.11008)
- **Method:** 2,700 templated and 2,700 LLM-written political prompts on the same topic × intent × stance grid, with real WildChat/LMSys prompts as a realism anchor.
- **Results:** on neutral prompts GPT 5.4 mini sits 0.48 scale points from neutral with templated prompts vs 0.07 with LLM-written ones (14 of 18 settings, p = .001); refusals 5% vs 2%. LLM judges rank LLM-written prompts as real more often than actual human prompts (45.0% vs 39.5% first-rank share).
- **Relevance:** the author traces the gap to presuppositions carried by template fillers, i.e. a content leak, not style. Human prompts were never run behaviourally. Any rewrite pair needs a check for stance and presupposition drift.

### 2.4 Surface-feature sensitivity of safety behaviours (abstract-only)

- Sclar et al. 2023: formatting choices alone move task accuracy substantially.
- Yin et al. 2024: prompt politeness changes performance.
- Plaza-del-Arco et al. 2025: across 16 models and nine paraphrases, model and task choice drive false refusals more than persona.
- Patel et al. 2026: positive emotional tone raises accuracy and sycophancy.
- Huang et al. 2026 (SyPS): instance-level sycophancy sensitivity to social cues across paired variants.
- Cheng et al. 2026: the model's assumptions about the user (e.g. "seeking validation") can be probed and steered to change sycophancy.

---

## 3. Common methodologies

- **Paired / minimal-pair prompts with within-item comparison** (Abdelnabi & Salem; Xiong et al.; Xu et al.; Laurito et al.).
- **Linear direction extraction.** Mean difference (Nguyen; Heidari; Arditi), PCA of paired differences (RepreGuard), logistic regression on last-token states (Quaremba; Devbunova).
- **Causal intervention.** Additive residual steering scaled to activation norm (Heidari), directional ablation/addition (Arditi), MLP weight edits (Abdelnabi & Salem).
- **Rewrite then re-evaluate** with an LLM rewriter and a semantic-equivalence audit (Xiong; Xu; Devbunova).
- **LLM-as-judge** for refusal, honesty or stance, validated on a human-labelled subsample.

## 4. Standard baselines and controls

- Random-direction probes (AUROC ≈ 0.5).
- Surface classifiers: prompt length, special-character count (0.58–0.60 AUROC in Nguyen et al.).
- Length matching by constraint or histogram matching (Xu; Devbunova).
- Stylometric covariates: LIWC categories, BERTScore, ROUGE-L (Xu).
- Decorrelated 2×2 training sets (Devbunova).
- Explicit-label condition: say the source instead of implying it (Panickssery; Abdelnabi & Salem's system-prompt baseline).
- Both presentation orders for any pairwise choice.

## 5. Evaluation metrics

- **Refusal / compliance rate:** judge model or StrongREJECT rubric; paired test such as McNemar or a mixed-effects logistic model with item random effects.
- **Sycophancy:** rate of choosing the user-matching answer (model-written-evals); flip rate after "are you sure?" and accuracy drop with a suggested wrong answer (sycophancy-eval).
- **Accuracy:** TruthfulQA or the `answer` subset.
- **Probe quality:** AUROC against random-direction and surface-feature baselines; held-out generator and topic.
- **Mediation:** behaviour change regressed on probe score with surface covariates; dose-response under steering.

## 6. Datasets in the literature

- Human prompts: WildChat, ShareGPT, LMSYS-Chat (Needham; Nguyen; Heidari; Devbunova; Chalkidis).
- Safety behaviour: HarmBench, AdvBench, JBB-Behaviors, XSTest, MASK, model-written-evals.
- Human-vs-machine text: DetectRL, RAID, M4GT, MultiSocial, HC3. All are passages, not prompts.
- Test-vs-deploy: SAD `stages_oversight`, the Needham et al. 1,000-transcript set.

## 7. Gaps and opportunities

1. **No content-controlled human-style vs LLM-style prompt manipulation with safety outcomes.** Xiong et al. come closest but conflate deploy-likeness, length and LLM authorship.
2. **No "LLM-authored prompt" probe on chat-templated user turns.** Detection probes use passages of 100+ characters fed to base models.
3. **No causal link from an authorship direction to behaviour.** Both detection papers stop at classification; AI–AI bias papers stop at behaviour.
4. **Surface confounds are acknowledged but rarely factored out.** Only Devbunova and Xu et al. decorrelate them, and neither studies prompt authorship.
5. **Direction of effect is unknown and may be model-specific** (Abdelnabi & Salem found opposite signs across models).

---

## 8. Research directions: ranking and pruning

Scored 1–5 on literature support, relevance to the hypothesis, expected information gain and feasibility (one 48 GB RTX A6000; OpenAI and OpenRouter API keys present).

| # | Direction | Lit. | Rel. | Info | Feas. | Total | Decision |
|---|-----------|------|------|------|-------|-------|----------|
| D1 | Paired behavioural test: same request in human style vs LLM style; refusal, sycophancy, accuracy; several models | 4 | 5 | 5 | 5 | 19 | **Keep** |
| D2 | Surface-feature decomposition: factorial rewrites (length, formality/politeness, formatting, typos) plus stylometric regression and an explicit-label arm | 5 | 5 | 4 | 5 | 19 | **Keep** |
| D3 | Representation test: train an "LLM-authored prompt" probe in an open ~8B chat model on decorrelated data; test whether probe score predicts behaviour beyond surface features; steer along the direction | 4 | 5 | 5 | 3 | 17 | **Keep** |
| D4 | Self- vs other-model authorship (does the responder react more to its own style?) | 3 | 3 | 3 | 4 | 13 | Pruned: self-recognition evidence is contradictory (Bai et al.; St. Amand et al.) and it multiplies conditions. |
| D5 | Verbalised awareness in reasoning traces ("this looks AI-written") | 3 | 3 | 2 | 4 | 12 | Pruned: verbalisation is rare and uncoupled from the representation (Heidari et al.). |
| D6 | Multi-turn or agentic LLM-to-LLM pipelines | 2 | 4 | 3 | 2 | 11 | Pruned: content cannot be held fixed across turns; high cost. |
| D7 | Pairwise preference for LLM-written items | 5 | 2 | 1 | 5 | 13 | Pruned: already established (Laurito; Xu); not a safety behaviour of the responder. |
| D8 | Fine-tuned model organism that conditions on authorship | 3 | 2 | 3 | 1 | 9 | Pruned: tests whether it can be induced, not whether it occurs; compute-heavy. |
| D9 | SAE feature analysis of authorship | 2 | 3 | 3 | 2 | 10 | Pruned: needs SAEs for the chosen model; a linear probe answers the same question more cheaply. |

D1 and D2 tie; they are two arms of one experiment and should share the prompt set.

---

## 9. Recommendations for the experiment

**Datasets**
- Refusal: `jbb_behaviors` harmful (100) + benign (100); XSTest for over-refusal; StrongREJECT if more items are needed.
- Sycophancy: `model_written_evals/sycophancy` (A/B, cheap to score) and `sycophancy_eval/are_you_sure.jsonl` + `answer.jsonl`.
- Accuracy: TruthfulQA or `sycophancy_eval/answer.jsonl` base questions.
- Style references: `wildchat_1m/wildchat_first_turn_english_nontoxic.jsonl` for human style; LLM-style versions must be generated.
- Native contrast: `model_written_evals/advanced-ai-risk/human_generated_evals` vs `lm_generated_evals` (same behaviours; length differs about 2×).

**Stimulus construction**
- For each seed request produce a human-style and an LLM-style version with the same content. Use few-shot WildChat examples to anchor the human style; real human rewrites are not available, so "human style" will itself be LLM-imitated unless the seed is a real WildChat prompt. Starting from real WildChat prompts and producing LLM-style rewrites gives one arm that is truly human-written.
- Add control arms that change one surface feature at a time: length-matched, polite vs blunt, formatted vs plain, typos added to LLM style, typos removed from human style.
- Add an explicit-label arm: identical text, prefixed with a statement that the message was written by a person or by an AI agent.
- Audit each pair for intent, stance and presupposition drift (Chalkidis). Verify the manipulation with a detector (the probe, Binoculars, or a "human or AI?" question to a judge model).
- Use more than one rewriter model so the effect is not one generator's idiolect.

**Baselines**
- Original benchmark phrasing; random-direction probe; length and special-character classifiers; stylometric-only regression.

**Metrics and statistics**
- Paired within-item differences with bootstrap confidence intervals; mixed-effects logistic regression with item random effects and surface covariates (length, formality, politeness markers, formatting).
- For the representation claim: does the probe score explain behaviour after the covariates, and does steering along the direction move behaviour on a *fixed* prompt?

**Model choice**
- Probing and steering need open weights that fit in 48 GB: Llama-3.1-8B-Instruct (used by Devbunova, Quaremba's backbone family, Arditi's pipeline) or Qwen3-8B (Heidari). Black-box replication across API models via OpenRouter.

**Methodological cautions**
- Do not assume a sign; test two-sided.
- Train the probe on data where style is decorrelated from format, length and topic, and test on held-out generators.
- Short prompts weaken detection (0.85 AUC at 25 characters), and JBB goals are short; expanded rewrites make length a confound, so the length-matched arm is essential.
- Judge models may themselves be style-sensitive: validate the refusal judge on a human-labelled subsample from each style arm.
