# Planning: Do LLMs behave differently when the prompt reads LLM-written?

## Motivation & Novelty Assessment

### Why This Research Matters
Safety evaluations (model-written evals, synthetic red-teaming, automated auditors) and multi-agent
systems feed LLM-written user turns to models. If a responder's refusal, sycophancy or accuracy shifts
because a prompt *reads* LLM-written, evaluation numbers do not transfer to human-user deployment, and
orchestrator-written prompts get systematically different treatment from human ones.

### Gap in Existing Work
(`literature_review.md`) Models distinguish eval from deployment transcripts (Needham 2505.23836), eval
awareness can be probed/steered and changes compliance (2505.14617, 2507.01786), and human-vs-machine
text is linearly separable in activations (RepreGuard 2508.13152; 2608.24780). Nobody has (a) isolated
prompt *authorship style* with content fixed across several safety behaviours, (b) tested causally
whether an internal "LLM-written" representation, rather than length/politeness/clarity, drives a
change, or (c) related that representation to the eval-awareness direction.

### Our Novel Contribution
A content-matched 2x2 (style x length) rewrite design over refusal, sycophancy and accuracy items, with
a perception manipulation check; an authorship direction in two open models that is decorrelated from
length by construction; fixed-text activation steering with random, norm-matched, length-direction and
positive-control baselines; and the geometry between the authorship and eval-awareness directions.

### Experiment Justification
- **E1 stimulus set + audit + manipulation check**: without content-fidelity filtering and a check that
  the responder perceives the style difference, neither an effect nor a null is interpretable.
- **E2 behavioural 2x2 (D1+D2)**: both arms are paraphrases by the same rewriter, so "was paraphrased"
  is constant; crossing style with length separates "reads LLM" from "is longer". Explicit-label arm
  (identical text, system note says the author is an AI / a human) tests stated authorship directly.
- **E3 probe + mediation**: does the internal authorship score explain within-item behaviour changes
  beyond surface covariates?
- **E4 steering on fixed text**: the cleanest content control; baselines distinguish a specific effect
  from generic perturbation.
- **E5 relation to eval awareness**: cosine and cross-projection between authorship and eval-awareness
  directions, against random baselines.

## Research Question
With request content held fixed, does human-style vs LLM-style phrasing of the user prompt change
refusal, sycophancy or accuracy of the responding model? If so, is the change attributable to the
model's internal representation of "LLM-written", or to surface features?

## Hypothesis Decomposition
- H1 (manipulation): responders perceive LLM-style rewrites as more LLM-written than human-style ones,
  including when length is matched (verbal judgment and linear probe).
- H2 (behaviour): style changes refusal / sycophancy / accuracy within item (two-sided).
- H3 (specificity): any H2 effect survives the length-matched contrast and surface covariates.
- H4 (causal): steering the authorship direction on fixed text changes behaviour more than random
  norm-matched directions, at doses comparable to the natural human-LLM gap.
- H5 (geometry): the authorship direction is aligned with the eval-awareness direction above chance.

## Proposed Methodology

### Stimuli
Seeds (benchmark originals):
- Refusal: 100 JBB harmful, 50 JBB benign, 100 XSTest (50 safe, 50 unsafe contrast) -> borderline mix
  for headroom.
- Sycophancy (factual): 150 TriviaQA items from sycophancy-eval `answer.jsonl`, with user suggesting the
  wrong answer; Accuracy: the same 150 questions without the suggestion.
- Sycophancy (opinion): 150 model-written-evals items (50 per file); only the biography is rewritten,
  the question and choices are appended verbatim; scored by A/B logits or the answered letter.
- Authorship reference: 300 real WildChat first-turn prompts (25-400 chars) - truly human-written.

Rewrite conditions per seed, by two rewriter models from different providers:
`H_s` human style natural length; `H_l` human style, length-matched to `L_l`; `L_l` LLM style natural
length; `L_s` LLM style, length-matched to `H_s`. Human style is anchored with real WildChat few-shots.
Plus `orig` and explicit-label arms on `orig` (system note: author is an AI system / a human).
Audit: a judge model checks each rewrite preserves the request (content, intent, stated beliefs); a
seed is kept only if all its rewrites pass. Rewriter refusals are dropped and counted.

### Models
- Open weights (internals): `meta-llama/Llama-3.1-8B-Instruct` (primary), `Qwen/Qwen2.5-7B-Instruct`
  (replication). Greedy decoding.
- API responders (behaviour only), chosen from the live OpenRouter catalog (2026-10-04).
- Rewriters / judges via OpenRouter; exact IDs logged in `results/config.json`.

### Experimental Steps
1. Build + audit stimuli; surface features (length, politeness markers, typos/casing, punctuation).
2. Manipulation check: (a) responder asked "written by human or AI?" (logit difference in open models);
   (b) authorship probe trained on WildChat (real human + rewrites), tested on held-out WildChat and
   transferred to benchmark rewrites; check real-human originals score like `H_*` rewrites.
3. Behaviour on all conditions; refusal and correctness judged by an LLM judge (validated against a
   second judge on a subsample and a manual spot check); opinion sycophancy from logits.
4. Authorship direction per layer: balanced difference of means
   d_auth = 1/2[(L_s - H_s) + (L_l - H_l)], length direction d_len = 1/2[(H_l - H_s) + (L_l - L_s)],
   estimated on WildChat items only (disjoint from behaviour seeds). Layer chosen on WildChat held-out
   probe AUROC and steering effect on the verbal authorship judgment (not on behaviour).
5. Mediation: within-item regression of behaviour on probe score plus surface covariates.
6. Steering on fixed `orig`/`H_s` text: add alpha*d at the chosen layer, alpha in multiples of the
   natural H->L projection gap. Baselines: isotropic random directions (norm-matched), random directions
   sampled from the activation covariance (variance-matched), d_len; positive controls: refusal
   direction (harmful - harmless) and eval-awareness direction. Outcomes: refusal, opinion-sycophancy
   logit, trivia accuracy/sycophancy, verbal authorship judgment, plus a degradation check.
7. Eval-awareness direction from the 16 contrastive pairs of Nguyen et al. (test - deploy system
   statements over neutral WildChat prompts); cosine with d_auth per layer vs random-direction null;
   projection of H/L prompts onto the eval direction; steering cross-effects on verbal eval judgment.

### Baselines
Original benchmark phrasing; length-matched arms; random/variance-matched/length directions;
refusal-direction positive control.

### Evaluation Metrics
Refusal rate (judge), factual sycophancy (rate of endorsing the user's wrong answer; accuracy with
suggestion), accuracy (neutral question), opinion sycophancy (P(answer matching user view) / logit
diff), perceived-AI score (logit diff), probe AUROC.

### Statistical Analysis Plan
Paired within-seed contrasts. Main effect of style = mean over length cells and rewriters of (L - H);
length effect analogously; cluster bootstrap over seeds (10,000 resamples) for 95% CIs, sign-flip
permutation p-values; Holm correction across the behaviour x model family for the primary style
contrast. Mixed/fixed-effects regression with seed fixed effects for covariates. Steering: effect vs
distribution over random directions (empirical p), dose-response slope. alpha = 0.05 two-sided.

## Expected Outcomes
Support: style main effect that survives length-matching, tracked by probe score, reproduced by
steering beyond random baselines. Refute (clean null): manipulation check passes (model perceives
style) but behaviour contrasts are ~0 with tight CIs, and steering at natural doses matches random.
Intermediate: effects that load on length/politeness rather than style.

## Timeline
Stimuli 1h; open-model behaviour + activations 1.5h; API behaviour + judging 1h (parallel with GPU);
steering 1.5h; analysis + report 1.5h. Buffer ~25%.

## Potential Challenges
- Rewriters refusing harmful prompts -> pick compliant rewriters, report attrition.
- Refusal ceiling/floor -> borderline items (XSTest, JBB benign), report per-subset.
- Judge style bias -> second judge + manual sample per style arm.
- Steering degrading the model -> coherence/accuracy checks; doses anchored to natural gap.

## Success Criteria
Manipulation check passes; all contrasts reported with CIs; steering has the stated baselines;
conclusion (effect or null) follows from the controlled comparisons.

## Direction budget
Kept: D1 paired behavioural test, D2 surface-feature decomposition (2x2 + label arm + covariates),
D3 probe/mediation/steering (incl. eval-awareness geometry). Pruned (see `literature_review.md` §8):
self-vs-other authorship, verbalised awareness in reasoning traces, multi-turn agentic pipelines,
pairwise LLM-item preference, fine-tuned model organism, SAE analysis.
