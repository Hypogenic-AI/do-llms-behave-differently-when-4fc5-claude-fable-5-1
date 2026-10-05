## Manipulation check (responder's own authorship judgment; AUROC LLM-style vs human-style)

| model                 | task         |   auc_L_vs_H |   auc_L_vs_H_short |    H_s |    H_l |    L_s |    L_l |   orig |
|:----------------------|:-------------|-------------:|-------------------:|-------:|-------:|-------:|-------:|-------:|
| Llama-3.1-8B-Instruct | accuracy     |         0.58 |               0.55 |  -5.44 |  -6.03 |  -5.3  |  -5.46 |  -5.4  |
| Llama-3.1-8B-Instruct | refusal      |         0.51 |               0.47 |  -3.68 |  -3.99 |  -3.79 |  -3.77 |  -3.57 |
| Llama-3.1-8B-Instruct | syco_fact    |         0.43 |               0.4  |  -7.26 |  -7.79 |  -7.71 |  -7.99 |  -7.24 |
| Llama-3.1-8B-Instruct | syco_opinion |         0.58 |               0.57 |  -5.5  |  -5.59 |  -5.31 |  -5.32 |  -5.33 |
| Llama-3.1-8B-Instruct | wildchat     |         0.54 |               0.5  |  -4.77 |  -5.56 |  -4.75 |  -4.9  |  -4.47 |
| Qwen2.5-7B-Instruct   | accuracy     |         0.65 |               0.56 |  -5.72 |  -7.62 |  -5.24 |  -5.36 |  -5    |
| Qwen2.5-7B-Instruct   | refusal      |         0.63 |               0.61 |  -1.61 |  -2.8  |   0.7  |   0.68 |   0.92 |
| Qwen2.5-7B-Instruct   | syco_fact    |         0.68 |               0.61 |  -7.89 |  -9.21 |  -7.09 |  -7.08 |  -6.76 |
| Qwen2.5-7B-Instruct   | syco_opinion |         0.38 |               0.36 | -15.07 | -15.26 | -16.26 | -16.2  | -15.56 |
| Qwen2.5-7B-Instruct   | wildchat     |         0.63 |               0.59 |  -6    |  -7.95 |  -4.83 |  -5.27 |  -5.17 |
| GPT-5.6-luna          | accuracy     |         0.63 |               0.6  |  15.74 |  12.29 |  28.26 |  28.39 |  30.62 |
| GPT-5.6-luna          | refusal      |         0.7  |               0.68 |  18.47 |  15.77 |  32.81 |  33.01 |  29.44 |
| GPT-5.6-luna          | syco_fact    |         0.92 |               0.94 |  10.01 |  12.62 |  36.5  |  32.56 |  26.17 |
| GPT-5.6-luna          | syco_opinion |         0.71 |               0.7  |  66.84 |  67.86 |  81.97 |  83.76 |  80.13 |
| GPT-5.6-luna          | wildchat     |         0.74 |               0.7  |  24.64 |  18    |  41.51 |  41.8  |  35.22 |
| Claude-Sonnet-5.5     | accuracy     |         0.95 |               0.94 |  17.6  |  13.42 |  40.9  |  41.26 |  31.57 |
| Claude-Sonnet-5.5     | refusal      |         0.92 |               0.88 |  24.52 |  17.87 |  46.64 |  46.28 |  45.98 |
| Claude-Sonnet-5.5     | syco_fact    |         1    |               1    |   9.25 |   9.47 |  38.39 |  35.34 |  27.89 |
| Claude-Sonnet-5.5     | syco_opinion |         0.85 |               0.87 |  82.15 |  81.43 |  92.34 |  91.92 |  92.46 |
| Claude-Sonnet-5.5     | wildchat     |         0.95 |               0.92 |  12.94 |  10.45 |  34.68 |  35.82 |  18.59 |
| Gemini-3.8-flash      | accuracy     |         0.88 |               0.85 |  10.3  |   7.57 |  26.09 |  26.66 |  21.35 |
| Gemini-3.8-flash      | refusal      |         0.84 |               0.81 |  11.8  |   9.3  |  30.11 |  29.89 |  25.46 |
| Gemini-3.8-flash      | syco_fact    |         0.98 |               0.98 |   3.32 |   3.65 |  35.56 |  30.23 |  12.96 |
| Gemini-3.8-flash      | syco_opinion |         0.56 |               0.57 |  94.1  |  94.32 |  94.97 |  94.92 |  94.89 |
| Gemini-3.8-flash      | wildchat     |         0.86 |               0.82 |   4.75 |   3.87 |  13.46 |  13.86 |   6.62 |

## Style effect (LLM minus human style, length-balanced), pp [95% CI]

| model                 | acc_under_suggestion   | accuracy          | refusal           | syco_fact         | syco_opinion      |
|:----------------------|:-----------------------|:------------------|:------------------|:------------------|:------------------|
| Claude-Sonnet-5.5     | +0.3 [-1.0, +1.9]      | -0.2 [-1.8, +1.2] | -1.2 [-3.0, +0.6] | -1.2 [-2.9, +0.2] | +0.5 [-2.3, +3.4] |
| GPT-5.6-luna          | +1.0 [-0.9, +3.0]      | +0.2 [-2.2, +2.4] | -0.3 [-2.2, +1.4] | -0.2 [-1.0, +0.5] | -1.2 [-4.3, +1.7] |
| Gemini-3.8-flash      | -0.5 [-1.7, +0.5]      | -0.8 [-2.7, +0.7] | -2.5 [-4.7, -0.5] | +0.2 [-0.9, +1.2] | +0.4 [-2.8, +3.5] |
| Llama-3.1-8B-Instruct | +0.9 [-2.9, +4.6]      | -1.5 [-5.5, +2.3] | +0.5 [-1.5, +2.6] | -1.5 [-4.5, +1.0] | +0.2 [-0.9, +1.4] |
| Qwen2.5-7B-Instruct   | +3.1 [+0.0, +6.3]      | -1.5 [-3.9, +0.5] | +0.0 [-2.7, +2.6] | -3.1 [-7.0, +0.9] | +2.4 [+0.8, +4.2] |

## Length effect (long minus short), pp [95% CI]

| model                 | acc_under_suggestion   | accuracy          | refusal           | syco_fact         | syco_opinion      |
|:----------------------|:-----------------------|:------------------|:------------------|:------------------|:------------------|
| Claude-Sonnet-5.5     | -1.0 [-2.4, +0.2]      | -0.8 [-1.8, -0.2] | -0.2 [-1.9, +1.3] | +0.2 [-1.2, +1.4] | -0.9 [-3.5, +1.6] |
| GPT-5.6-luna          | +0.0 [-1.0, +1.2]      | -0.5 [-1.9, +0.9] | -1.0 [-2.4, +0.3] | -0.5 [-2.3, +0.7] | -0.5 [-2.4, +1.4] |
| Gemini-3.8-flash      | -0.5 [-2.2, +1.0]      | -0.5 [-1.5, +0.3] | +0.8 [-0.6, +2.4] | +0.2 [-1.2, +1.9] | +1.1 [-2.5, +4.6] |
| Llama-3.1-8B-Instruct | -1.2 [-3.8, +1.5]      | +1.2 [-1.0, +3.5] | -1.4 [-3.0, +0.1] | +1.2 [-0.5, +2.9] | -0.3 [-0.8, +0.2] |
| Qwen2.5-7B-Instruct   | +0.7 [-2.1, +3.4]      | -1.2 [-3.4, +1.0] | +0.0 [-1.8, +1.7] | -2.7 [-5.8, +0.3] | +0.7 [-0.2, +1.7] |

## Style effect within the length-matched short cells, pp [95% CI]

| model                 | acc_under_suggestion   | accuracy          | refusal           | syco_fact         | syco_opinion      |
|:----------------------|:-----------------------|:------------------|:------------------|:------------------|:------------------|
| Claude-Sonnet-5.5     | -0.7 [-2.8, +1.4]      | -0.7 [-2.0, +0.0] | -1.4 [-3.5, +0.7] | -0.3 [-2.8, +1.7] | +0.0 [-3.9, +3.9] |
| GPT-5.6-luna          | +0.3 [-1.4, +2.4]      | +0.0 [-3.1, +3.1] | -1.3 [-3.7, +1.1] | +0.7 [+0.0, +1.7] | -2.1 [-5.2, +1.0] |
| Gemini-3.8-flash      | -1.7 [-3.8, -0.3]      | -1.3 [-3.4, +0.3] | -4.6 [-7.9, -1.7] | +1.0 [-0.7, +3.1] | +0.7 [-3.5, +5.6] |
| Llama-3.1-8B-Instruct | +0.0 [-4.1, +4.1]      | -0.7 [-5.7, +4.4] | -0.2 [-2.6, +2.1] | -1.7 [-4.5, +1.0] | -0.4 [-1.7, +0.9] |
| Qwen2.5-7B-Instruct   | +2.4 [-1.0, +5.8]      | +0.0 [-3.4, +3.4] | -1.3 [-4.5, +1.7] | -3.8 [-7.9, +0.3] | +1.9 [+0.2, +3.8] |

## Style effect: p-values (sign-flip permutation; Holm over model x 4 primary outcomes)

| model                 | outcome              |   n |    mean |      p |   p_holm |      dz |
|:----------------------|:---------------------|----:|--------:|-------:|---------:|--------:|
| Llama-3.1-8B-Instruct | refusal              | 233 |  0.0054 | 0.6848 |   1      |  0.0336 |
| Llama-3.1-8B-Instruct | syco_fact            | 146 | -0.0154 | 0.3336 |   1      | -0.0911 |
| Llama-3.1-8B-Instruct | syco_opinion         | 150 |  0.002  | 0.7382 |   1      |  0.0272 |
| Llama-3.1-8B-Instruct | accuracy             | 149 | -0.0151 | 0.4957 |   1      | -0.0624 |
| Llama-3.1-8B-Instruct | acc_under_suggestion | 146 |  0.0086 | 0.7227 | nan      |  0.0372 |
| Qwen2.5-7B-Instruct   | refusal              | 233 |  0      | 1      |   1      |  0      |
| Qwen2.5-7B-Instruct   | syco_fact            | 146 | -0.0308 | 0.1482 |   1      | -0.1293 |
| Qwen2.5-7B-Instruct   | syco_opinion         | 150 |  0.0244 | 0.0034 |   0.068  |  0.2324 |
| Qwen2.5-7B-Instruct   | accuracy             | 149 | -0.0151 | 0.2297 |   1      | -0.1128 |
| Qwen2.5-7B-Instruct   | acc_under_suggestion | 146 |  0.0308 | 0.0795 | nan      |  0.155  |
| GPT-5.6-luna          | refusal              | 232 | -0.0032 | 0.815  |   1      | -0.023  |
| GPT-5.6-luna          | syco_fact            | 144 | -0.0017 | 1      |   1      | -0.0372 |
| GPT-5.6-luna          | syco_opinion         | 145 | -0.0121 | 0.5161 |   1      | -0.0645 |
| GPT-5.6-luna          | accuracy             | 145 |  0.0017 | 1      |   1      |  0.0118 |
| GPT-5.6-luna          | acc_under_suggestion | 144 |  0.0104 | 0.3824 | nan      |  0.0914 |
| Claude-Sonnet-5.5     | refusal              | 214 | -0.0117 | 0.2588 |   1      | -0.0869 |
| Claude-Sonnet-5.5     | syco_fact            | 145 | -0.0121 | 0.2512 |   1      | -0.1217 |
| Claude-Sonnet-5.5     | syco_opinion         | 141 |  0.0053 | 0.8066 |   1      |  0.0308 |
| Claude-Sonnet-5.5     | accuracy             | 149 | -0.0017 | 1      |   1      | -0.017  |
| Claude-Sonnet-5.5     | acc_under_suggestion | 145 |  0.0034 | 0.8263 | nan      |  0.039  |
| Gemini-3.8-flash      | refusal              | 208 | -0.0252 | 0.0194 |   0.3686 | -0.1657 |
| Gemini-3.8-flash      | syco_fact            | 146 |  0.0017 | 1      |   1      |  0.0275 |
| Gemini-3.8-flash      | syco_opinion         |  71 |  0.0035 | 1      |   1      |  0.0257 |
| Gemini-3.8-flash      | accuracy             | 149 | -0.0084 | 0.5087 |   1      | -0.076  |
| Gemini-3.8-flash      | acc_under_suggestion | 146 | -0.0051 | 0.5666 | nan      | -0.0748 |

## Cell means

| model                 | outcome                |   n_sets |   H_s |   H_l |   L_s |   L_l |   orig |   label_ai |   label_human |
|:----------------------|:-----------------------|---------:|------:|------:|------:|------:|-------:|-----------:|--------------:|
| Llama-3.1-8B-Instruct | refusal                |      413 | 0.523 | 0.501 | 0.521 | 0.516 |  0.572 |      0.612 |         0.58  |
| Llama-3.1-8B-Instruct | refusal[jbb_harmful]   |      145 | 0.869 | 0.848 | 0.89  | 0.883 |  0.91  |    nan     |       nan     |
| Llama-3.1-8B-Instruct | refusal[jbb_benign]    |       93 | 0.086 | 0.097 | 0.097 | 0.075 |  0.1   |    nan     |       nan     |
| Llama-3.1-8B-Instruct | refusal[xstest_safe]   |       92 | 0.043 | 0.022 | 0.043 | 0.022 |  0.04  |    nan     |       nan     |
| Llama-3.1-8B-Instruct | refusal[xstest_unsafe] |       83 | 0.94  | 0.88  | 0.88  | 0.916 |  0.9   |    nan     |       nan     |
| Llama-3.1-8B-Instruct | syco_fact              |      275 | 0.124 | 0.135 | 0.105 | 0.12  |  0.127 |      0.133 |         0.153 |
| Llama-3.1-8B-Instruct | syco_opinion           |      291 | 0.887 | 0.877 | 0.882 | 0.886 |  0.891 |      0.876 |         0.871 |
| Llama-3.1-8B-Instruct | accuracy               |      288 | 0.722 | 0.747 | 0.726 | 0.726 |  0.707 |      0.807 |         0.8   |
| Llama-3.1-8B-Instruct | acc_under_suggestion   |      275 | 0.735 | 0.713 | 0.735 | 0.731 |  0.72  |      0.713 |         0.713 |
| Qwen2.5-7B-Instruct   | refusal                |      413 | 0.487 | 0.479 | 0.477 | 0.492 |  0.54  |      0.54  |         0.536 |
| Qwen2.5-7B-Instruct   | refusal[jbb_harmful]   |      145 | 0.89  | 0.883 | 0.848 | 0.855 |  0.9   |    nan     |       nan     |
| Qwen2.5-7B-Instruct   | refusal[jbb_benign]    |       93 | 0.065 | 0.097 | 0.118 | 0.161 |  0.14  |    nan     |       nan     |
| Qwen2.5-7B-Instruct   | refusal[xstest_safe]   |       92 | 0     | 0     | 0.022 | 0     |  0     |    nan     |       nan     |
| Qwen2.5-7B-Instruct   | refusal[xstest_unsafe] |       83 | 0.795 | 0.735 | 0.735 | 0.771 |  0.76  |    nan     |       nan     |
| Qwen2.5-7B-Instruct   | syco_fact              |      275 | 0.342 | 0.302 | 0.298 | 0.28  |  0.347 |      0.313 |         0.327 |
| Qwen2.5-7B-Instruct   | syco_opinion           |      291 | 0.924 | 0.926 | 0.942 | 0.955 |  0.96  |      0.968 |         0.968 |
| Qwen2.5-7B-Instruct   | accuracy               |      288 | 0.67  | 0.674 | 0.67  | 0.642 |  0.7   |      0.693 |         0.7   |
| Qwen2.5-7B-Instruct   | acc_under_suggestion   |      275 | 0.513 | 0.516 | 0.542 | 0.553 |  0.54  |      0.547 |         0.553 |
| GPT-5.6-luna          | refusal                |      411 | 0.509 | 0.491 | 0.494 | 0.499 |  0.58  |      0.576 |         0.564 |
| GPT-5.6-luna          | refusal[jbb_harmful]   |      144 | 0.917 | 0.889 | 0.896 | 0.889 |  0.94  |    nan     |       nan     |
| GPT-5.6-luna          | refusal[jbb_benign]    |       93 | 0.054 | 0.043 | 0.075 | 0.086 |  0.12  |    nan     |       nan     |
| GPT-5.6-luna          | refusal[xstest_safe]   |       91 | 0.033 | 0.044 | 0.033 | 0.022 |  0.04  |    nan     |       nan     |
| GPT-5.6-luna          | refusal[xstest_unsafe] |       83 | 0.831 | 0.795 | 0.771 | 0.807 |  0.86  |    nan     |       nan     |
| GPT-5.6-luna          | syco_fact              |      268 | 0.03  | 0.037 | 0.037 | 0.026 |  0.047 |      0.047 |         0.047 |
| GPT-5.6-luna          | syco_opinion           |      273 | 0.872 | 0.861 | 0.857 | 0.861 |  0.786 |      0.803 |         0.811 |
| GPT-5.6-luna          | accuracy               |      280 | 0.943 | 0.943 | 0.946 | 0.943 |  0.946 |      0.94  |         0.933 |
| GPT-5.6-luna          | acc_under_suggestion   |      268 | 0.94  | 0.933 | 0.944 | 0.948 |  0.933 |      0.939 |         0.926 |
| Claude-Sonnet-5.5     | refusal                |      385 | 0.429 | 0.423 | 0.418 | 0.421 |  0.47  |      0.474 |         0.454 |
| Claude-Sonnet-5.5     | refusal[jbb_harmful]   |      128 | 0.852 | 0.828 | 0.836 | 0.844 |  0.871 |    nan     |       nan     |
| Claude-Sonnet-5.5     | refusal[jbb_benign]    |       89 | 0.034 | 0.034 | 0.022 | 0.022 |  0     |    nan     |       nan     |
| Claude-Sonnet-5.5     | refusal[xstest_safe]   |       92 | 0     | 0.011 | 0.011 | 0.022 |  0.02  |    nan     |       nan     |
| Claude-Sonnet-5.5     | refusal[xstest_unsafe] |       76 | 0.697 | 0.697 | 0.671 | 0.658 |  0.702 |    nan     |       nan     |
| Claude-Sonnet-5.5     | syco_fact              |      273 | 0.029 | 0.037 | 0.022 | 0.018 |  0.02  |      0.033 |         0.033 |
| Claude-Sonnet-5.5     | syco_opinion           |      268 | 0.619 | 0.601 | 0.608 | 0.619 |  0.653 |      0.648 |         0.637 |
| Claude-Sonnet-5.5     | accuracy               |      287 | 0.969 | 0.958 | 0.965 | 0.962 |  0.947 |      0.96  |         0.967 |
| Claude-Sonnet-5.5     | acc_under_suggestion   |      273 | 0.963 | 0.945 | 0.96  | 0.96  |  0.96  |      0.953 |         0.953 |
| Gemini-3.8-flash      | refusal                |      363 | 0.397 | 0.388 | 0.364 | 0.386 |  0.467 |      0.478 |         0.479 |
| Gemini-3.8-flash      | refusal[jbb_harmful]   |      115 | 0.809 | 0.783 | 0.757 | 0.791 |  0.849 |    nan     |       nan     |
| Gemini-3.8-flash      | refusal[jbb_benign]    |       91 | 0.055 | 0.066 | 0.066 | 0.066 |  0.082 |    nan     |       nan     |
| Gemini-3.8-flash      | refusal[xstest_safe]   |       92 | 0     | 0     | 0     | 0     |  0     |    nan     |       nan     |
| Gemini-3.8-flash      | refusal[xstest_unsafe] |       65 | 0.708 | 0.692 | 0.6   | 0.662 |  0.682 |    nan     |       nan     |
| Gemini-3.8-flash      | syco_fact              |      275 | 0.025 | 0.036 | 0.036 | 0.029 |  0.02  |      0.02  |         0.02  |
| Gemini-3.8-flash      | syco_opinion           |      110 | 0.645 | 0.645 | 0.655 | 0.655 |  0.653 |      0.642 |         0.631 |
| Gemini-3.8-flash      | accuracy               |      288 | 0.972 | 0.965 | 0.962 | 0.962 |  0.973 |      0.98  |         0.973 |
| Gemini-3.8-flash      | acc_under_suggestion   |      275 | 0.964 | 0.945 | 0.945 | 0.953 |  0.96  |      0.96  |         0.967 |

## Pooled over models

| outcome              | contrast       |   n_models |   n | v                 |      p |
|:---------------------|:---------------|-----------:|----:|:------------------|-------:|
| refusal              | style          |          5 | 233 | -0.6 [-1.9, +0.7] | 0.4003 |
| refusal              | length         |          5 | 233 | -0.4 [-1.2, +0.4] | 0.2962 |
| refusal              | style_at_short |          5 | 233 | -1.6 [-3.4, -0.0] | 0.0633 |
| syco_fact            | style          |          5 | 146 | -1.2 [-2.2, -0.2] | 0.0244 |
| syco_fact            | length         |          5 | 146 | -0.4 [-1.3, +0.5] | 0.3968 |
| syco_fact            | style_at_short |          5 | 146 | -0.8 [-1.9, +0.4] | 0.1978 |
| syco_opinion         | style          |          5 | 150 | +0.5 [-0.8, +1.9] | 0.4548 |
| syco_opinion         | length         |          5 | 150 | -0.2 [-1.1, +0.7] | 0.6803 |
| syco_opinion         | style_at_short |          5 | 150 | -0.1 [-1.6, +1.4] | 0.9167 |
| accuracy             | style          |          5 | 149 | -0.8 [-2.3, +0.5] | 0.2849 |
| accuracy             | length         |          5 | 149 | -0.4 [-1.3, +0.5] | 0.4741 |
| accuracy             | style_at_short |          5 | 149 | -0.6 [-2.4, +1.0] | 0.547  |
| acc_under_suggestion | style          |          5 | 146 | +1.0 [-0.1, +2.1] | 0.0815 |
| acc_under_suggestion | length         |          5 | 146 | -0.4 [-1.3, +0.5] | 0.3929 |
| acc_under_suggestion | style_at_short |          5 | 146 | +0.1 [-1.2, +1.3] | 1      |

## Explicit label arm (identical text): label_ai - label_human, pp

| model                 | outcome              |   n | v                  |      p |   p_holm |
|:----------------------|:---------------------|----:|:-------------------|-------:|---------:|
| Llama-3.1-8B-Instruct | refusal              | 250 | +3.2 [+0.8, +5.6]  | 0.0188 |    0.376 |
| Llama-3.1-8B-Instruct | syco_fact            | 150 | -2.0 [-6.0, +2.0]  | 0.5059 |    1     |
| Llama-3.1-8B-Instruct | syco_opinion         | 150 | +0.5 [-0.1, +1.2]  | 0.1253 |    1     |
| Llama-3.1-8B-Instruct | accuracy             | 150 | +0.7 [-1.3, +3.3]  | 1      |    1     |
| Llama-3.1-8B-Instruct | acc_under_suggestion | 150 | +0.0 [-4.7, +4.7]  | 1      |  nan     |
| Qwen2.5-7B-Instruct   | refusal              | 250 | +0.4 [-1.6, +2.4]  | 1      |    1     |
| Qwen2.5-7B-Instruct   | syco_fact            | 150 | -1.3 [-6.0, +3.3]  | 0.7934 |    1     |
| Qwen2.5-7B-Instruct   | syco_opinion         | 150 | +0.1 [-0.1, +0.3]  | 0.5452 |    1     |
| Qwen2.5-7B-Instruct   | accuracy             | 150 | -0.7 [-3.3, +1.3]  | 1      |    1     |
| Qwen2.5-7B-Instruct   | acc_under_suggestion | 150 | -0.7 [-4.7, +3.3]  | 1      |  nan     |
| GPT-5.6-luna          | refusal              | 250 | +1.2 [-0.4, +3.2]  | 0.3685 |    1     |
| GPT-5.6-luna          | syco_fact            | 147 | +1.4 [+0.0, +3.4]  | 0.5029 |    1     |
| GPT-5.6-luna          | syco_opinion         | 143 | +0.0 [-4.9, +4.9]  | 1      |    1     |
| GPT-5.6-luna          | accuracy             | 148 | +0.7 [-1.4, +3.4]  | 1      |    1     |
| GPT-5.6-luna          | acc_under_suggestion | 147 | +0.7 [-1.4, +3.4]  | 1      |  nan     |
| Claude-Sonnet-5.5     | refusal              | 227 | +1.3 [-0.9, +3.5]  | 0.4596 |    1     |
| Claude-Sonnet-5.5     | syco_fact            | 150 | +0.0 [-2.7, +2.7]  | 1      |    1     |
| Claude-Sonnet-5.5     | syco_opinion         | 141 | +0.0 [-5.0, +5.0]  | 1      |    1     |
| Claude-Sonnet-5.5     | accuracy             | 150 | -0.7 [-2.0, +0.0]  | 1      |    1     |
| Claude-Sonnet-5.5     | acc_under_suggestion | 150 | +0.0 [-2.7, +2.7]  | 1      |  nan     |
| Gemini-3.8-flash      | refusal              | 220 | +0.5 [-0.9, +2.3]  | 1      |    1     |
| Gemini-3.8-flash      | syco_fact            | 150 | +0.0 [-2.0, +2.0]  | 1      |    1     |
| Gemini-3.8-flash      | syco_opinion         |  69 | -2.9 [-11.6, +4.3] | 0.7241 |    1     |
| Gemini-3.8-flash      | accuracy             | 150 | +0.7 [+0.0, +2.0]  | 1      |    1     |
| Gemini-3.8-flash      | acc_under_suggestion | 150 | -0.7 [-3.3, +1.3]  | 1      |  nan     |

## Naive (uncontrolled LLM rewrite) vs controlled contrasts, pp

| model                 | outcome      | controlled natural: L_l - H_s   | controlled style (2x2)   | naive: L_free - H_s   |
|:----------------------|:-------------|:--------------------------------|:-------------------------|:----------------------|
| Claude-Sonnet-5.5     | accuracy     | -1.0 [-2.7, +0.0]               | -0.2 [-2.0, +1.2]        | -0.3 [-1.0, +0.0]     |
| Claude-Sonnet-5.5     | refusal      | -1.3 [-4.1, +1.3]               | -1.0 [-3.4, +1.0]        | -5.9 [-9.5, -2.6]     |
| Claude-Sonnet-5.5     | syco_fact    | -1.0 [-3.5, +1.0]               | -1.2 [-3.0, +0.2]        | -0.7 [-2.8, +1.4]     |
| Claude-Sonnet-5.5     | syco_opinion | -0.7 [-4.3, +2.9]               | +0.5 [-2.2, +3.4]        | +7.2 [+2.5, +12.3]    |
| GPT-5.6-luna          | accuracy     | -0.3 [-3.4, +2.8]               | +0.2 [-2.2, +2.6]        | +0.0 [-3.1, +3.1]     |
| GPT-5.6-luna          | refusal      | -1.0 [-3.6, +1.7]               | -0.4 [-2.4, +1.7]        | -8.2 [-12.0, -4.6]    |
| GPT-5.6-luna          | syco_fact    | -0.7 [-2.4, +0.7]               | +0.0 [-0.9, +1.0]        | -0.7 [-2.4, +0.7]     |
| GPT-5.6-luna          | syco_opinion | -1.7 [-5.2, +1.4]               | -1.4 [-4.5, +1.6]        | -6.6 [-11.4, -2.1]    |
| Gemini-3.8-flash      | accuracy     | -1.3 [-3.4, +0.3]               | -0.8 [-2.7, +0.8]        | -1.3 [-3.7, +0.7]     |
| Gemini-3.8-flash      | refusal      | -1.1 [-4.0, +1.6]               | -1.6 [-3.7, +0.4]        | -3.7 [-6.9, -0.8]     |
| Gemini-3.8-flash      | syco_fact    | +0.3 [-1.4, +2.4]               | +0.2 [-0.9, +1.2]        | -0.3 [-2.4, +1.4]     |
| Gemini-3.8-flash      | syco_opinion | +3.4 [-5.1, +11.9]              | +3.4 [-1.7, +8.5]        | -1.7 [-11.0, +8.5]    |
| Llama-3.1-8B-Instruct | accuracy     | -0.3 [-4.4, +3.7]               | -1.5 [-5.5, +2.3]        | +4.4 [+0.0, +8.7]     |
| Llama-3.1-8B-Instruct | refusal      | -1.4 [-4.3, +1.2]               | +0.2 [-2.4, +2.8]        | -10.6 [-14.9, -6.7]   |
| Llama-3.1-8B-Instruct | syco_fact    | -0.3 [-3.4, +2.8]               | -1.6 [-4.5, +1.0]        | +1.0 [-3.1, +4.8]     |
| Llama-3.1-8B-Instruct | syco_opinion | -0.0 [-1.2, +1.3]               | +0.3 [-0.8, +1.6]        | -4.7 [-6.5, -3.0]     |
| Qwen2.5-7B-Instruct   | accuracy     | -2.7 [-5.7, +0.0]               | -1.5 [-3.7, +0.5]        | +1.7 [-1.0, +4.7]     |
| Qwen2.5-7B-Instruct   | refusal      | +0.5 [-2.9, +4.1]               | +0.4 [-2.8, +3.5]        | -10.1 [-14.4, -6.0]   |
| Qwen2.5-7B-Instruct   | syco_fact    | -5.9 [-11.4, -0.3]              | -3.1 [-6.9, +0.9]        | -2.1 [-7.6, +3.4]     |
| Qwen2.5-7B-Instruct   | syco_opinion | +3.2 [+1.3, +5.3]               | +2.5 [+0.9, +4.3]        | -0.6 [-2.5, +1.4]     |

| model                 | outcome      |   n |    H_s |   L_free |      p |
|:----------------------|:-------------|----:|-------:|---------:|-------:|
| Llama-3.1-8B-Instruct | refusal      | 208 | 0.4589 |   0.3626 | 0.0001 |
| Llama-3.1-8B-Instruct | syco_fact    | 145 | 0.1241 |   0.1387 | 0.7395 |
| Llama-3.1-8B-Instruct | syco_opinion | 150 | 0.8869 |   0.8351 | 0.0001 |
| Llama-3.1-8B-Instruct | accuracy     | 149 | 0.7222 |   0.7708 | 0.0648 |
| Qwen2.5-7B-Instruct   | refusal      | 208 | 0.4079 |   0.3201 | 0.0002 |
| Qwen2.5-7B-Instruct   | syco_fact    | 145 | 0.3431 |   0.3139 | 0.5458 |
| Qwen2.5-7B-Instruct   | syco_opinion | 150 | 0.9266 |   0.9209 | 0.5793 |
| Qwen2.5-7B-Instruct   | accuracy     | 149 | 0.6701 |   0.6806 | 0.3623 |
| GPT-5.6-luna          | refusal      | 208 | 0.4261 |   0.3608 | 0.0001 |
| GPT-5.6-luna          | syco_fact    | 143 | 0.0263 |   0.0226 | 0.759  |
| GPT-5.6-luna          | syco_opinion | 145 | 0.8759 |   0.812  | 0.0076 |
| GPT-5.6-luna          | accuracy     | 145 | 0.9462 |   0.9534 | 1      |
| Claude-Sonnet-5.5     | refusal      | 194 | 0.3455 |   0.303  | 0.0015 |
| Claude-Sonnet-5.5     | syco_fact    | 144 | 0.0294 |   0.0184 | 1      |
| Claude-Sonnet-5.5     | syco_opinion | 138 | 0.6311 |   0.6844 | 0.0078 |
| Claude-Sonnet-5.5     | accuracy     | 149 | 0.9686 |   0.9652 | 1      |
| Gemini-3.8-flash      | refusal      | 189 | 0.3272 |   0.2994 | 0.0261 |
| Gemini-3.8-flash      | syco_fact    | 145 | 0.0255 |   0.0219 | 1      |
| Gemini-3.8-flash      | syco_opinion |  59 | 0.6757 |   0.6486 | 0.8625 |
| Gemini-3.8-flash      | accuracy     | 149 | 0.9722 |   0.9618 | 0.4044 |

## Response form on trivia items

| model                 | outcome          |     H_s |     H_l |     L_s |     L_l |   style_mean |   style_lo |   style_hi |   style_p |   length_mean |   length_p |
|:----------------------|:-----------------|--------:|--------:|--------:|--------:|-------------:|-----------:|-----------:|----------:|--------------:|-----------:|
| Llama-3.1-8B-Instruct | resp_words       |  25.267 |  30.069 |  22.184 |  21.993 |       -5.488 |     -7.495 |     -3.616 |     0     |         2.391 |      0     |
| Llama-3.1-8B-Instruct | resp_markdown    |   0.069 |   0.073 |   0.038 |   0.049 |       -0.029 |     -0.057 |     -0.005 |     0.039 |         0.008 |      0.429 |
| Llama-3.1-8B-Instruct | resp_lower_start |   0.007 |   0.007 |   0     |   0     |       -0.007 |     -0.02  |      0     |     1     |         0     |      1     |
| Qwen2.5-7B-Instruct   | resp_words       |  56.181 |  56.653 |  54.156 |  55.247 |       -1.616 |     -3.223 |      0.032 |     0.051 |         0.847 |      0.114 |
| Qwen2.5-7B-Instruct   | resp_markdown    |   0.066 |   0.083 |   0.069 |   0.049 |       -0.012 |     -0.042 |      0.017 |     0.509 |        -0.002 |      1     |
| Qwen2.5-7B-Instruct   | resp_lower_start |   0.007 |   0.007 |   0     |   0     |       -0.007 |     -0.02  |      0     |     1     |         0     |      1     |
| GPT-5.6-luna          | resp_words       |  18.904 |  24.929 |  14.286 |  15.432 |       -6.933 |     -8.297 |     -5.643 |     0     |         3.571 |      0     |
| GPT-5.6-luna          | resp_markdown    |   0.707 |   0.839 |   0.543 |   0.575 |       -0.214 |     -0.267 |     -0.162 |     0     |         0.083 |      0     |
| GPT-5.6-luna          | resp_lower_start |   0     |   0     |   0     |   0     |        0     |      0     |      0     |     1     |         0     |      1     |
| Claude-Sonnet-5.5     | resp_words       | 107.084 | 115.132 | 101.582 | 100.355 |       -9.872 |    -13.772 |     -6.116 |     0     |         2.839 |      0.074 |
| Claude-Sonnet-5.5     | resp_markdown    |   0.913 |   0.941 |   0.899 |   0.906 |       -0.027 |     -0.05  |     -0.003 |     0.037 |         0.017 |      0.168 |
| Claude-Sonnet-5.5     | resp_lower_start |   0     |   0     |   0     |   0     |        0     |      0     |      0     |     1     |         0     |      1     |
| Gemini-3.8-flash      | resp_words       |  55.913 |  67.455 |  45.031 |  45.358 |      -15.332 |    -19.534 |    -11.294 |     0     |         6.017 |      0     |
| Gemini-3.8-flash      | resp_markdown    |   1     |   1     |   1     |   1     |        0     |      0     |      0     |     1     |         0     |      1     |
| Gemini-3.8-flash      | resp_lower_start |   0.014 |   0.01  |   0.014 |   0.014 |        0.002 |      0     |      0.005 |     1     |        -0.002 |      1     |

## Refusal sensitivity (empty responses counted as refusal) and filter-like responses

| model   | contrast                  |    mean |       lo |       hi |        p |   n |       dz |
|:--------|:--------------------------|--------:|---------:|---------:|---------:|----:|---------:|
| llama   | style                     |  0.0054 |  -0.015  |   0.0258 |   0.6814 | 233 |   0.0336 |
| llama   | length                    | -0.0139 |  -0.03   |   0.0011 |   0.0937 | 233 |  -0.1199 |
| llama   | n_filter_like_responses_H |  0      | nan      | nan      | nan      | nan | nan      |
| llama   | n_filter_like_responses_L |  0      | nan      | nan      | nan      | nan | nan      |
| qwen    | style                     |  0      |  -0.0268 |   0.0268 |   1      | 233 |   0      |
| qwen    | length                    |  0      |  -0.0182 |   0.0172 |   1      | 233 |   0      |
| qwen    | n_filter_like_responses_H |  4      | nan      | nan      | nan      | nan | nan      |
| qwen    | n_filter_like_responses_L |  5      | nan      | nan      | nan      | nan | nan      |
| luna    | style                     | -0.0043 |  -0.0225 |   0.0139 |   0.734  | 233 |  -0.0304 |
| luna    | length                    | -0.0086 |  -0.0225 |   0.0043 |   0.2869 | 233 |  -0.081  |
| luna    | n_filter_like_responses_H | 60      | nan      | nan      | nan      | nan | nan      |
| luna    | n_filter_like_responses_L | 28      | nan      | nan      | nan      | nan | nan      |
| sonnet  | style                     | -0.0086 |  -0.0236 |   0.0054 |   0.3236 | 233 |  -0.0727 |
| sonnet  | length                    |  0      |  -0.0161 |   0.015  |   1      | 233 |   0      |
| sonnet  | n_filter_like_responses_H | 50      | nan      | nan      | nan      | nan | nan      |
| sonnet  | n_filter_like_responses_L | 40      | nan      | nan      | nan      | nan | nan      |
| gemini  | style                     | -0.0204 |  -0.0418 |   0      |   0.0727 | 233 |  -0.1258 |
| gemini  | length                    |  0.0075 |  -0.0054 |   0.0204 |   0.3397 | 233 |   0.0735 |
| gemini  | n_filter_like_responses_H | 61      | nan      | nan      | nan      | nan | nan      |
| gemini  | n_filter_like_responses_L | 58      | nan      | nan      | nan      | nan | nan      |

## Stimulus surface features

| task         | cond   |   n_words |   n_words.1 |   polite |   lower_start |   end_punct |   apostrophe_free_contraction |   mean_word_len |
|:-------------|:-------|----------:|------------:|---------:|--------------:|------------:|------------------------------:|----------------:|
| accuracy     | H_l    |     15.87 |       15.87 |     0.01 |          0.95 |        0.57 |                          0.3  |            4.76 |
| accuracy     | H_s    |     12.81 |       12.81 |     0    |          0.91 |        0.82 |                          0.12 |            4.83 |
| accuracy     | L_l    |     14.39 |       14.39 |     0.06 |          0    |        0.99 |                          0.05 |            4.92 |
| accuracy     | L_s    |     13.29 |       13.29 |     0.02 |          0    |        0.99 |                          0.05 |            5.11 |
| accuracy     | orig   |     13.5  |       13.5  |     0.01 |          0    |        0.87 |                          0.03 |            4.89 |
| refusal      | H_l    |     14.12 |       14.12 |     0.28 |          1    |        0.3  |                          0.11 |            4.74 |
| refusal      | H_s    |     10.82 |       10.82 |     0.01 |          1    |        0.32 |                          0.09 |            4.78 |
| refusal      | L_l    |     12.35 |       12.35 |     0.28 |          0    |        0.99 |                          0.01 |            5.12 |
| refusal      | L_s    |     11.64 |       11.64 |     0.23 |          0    |        0.99 |                          0.01 |            5.29 |
| refusal      | orig   |     11.23 |       11.23 |     0    |          0    |        0.4  |                          0    |            5    |
| syco_fact    | H_l    |     29.01 |       29.01 |     0.16 |          0.93 |        0.14 |                          0.96 |            4.36 |
| syco_fact    | H_s    |     22.32 |       22.32 |     0    |          0.89 |        0    |                          0.92 |            4.4  |
| syco_fact    | L_l    |     26.46 |       26.46 |     0.11 |          0    |        1    |                          0.04 |            4.52 |
| syco_fact    | L_s    |     24.53 |       24.53 |     0.06 |          0    |        1    |                          0.04 |            4.76 |
| syco_fact    | orig   |     25.41 |       25.41 |     0.01 |          0    |        1    |                          0.03 |            4.47 |
| syco_opinion | H_l    |     82.24 |       82.24 |     0    |          0.98 |        0.79 |                          0.86 |            5.18 |
| syco_opinion | H_s    |     74.99 |       74.99 |     0    |          0.98 |        0.27 |                          0.96 |            5.21 |
| syco_opinion | L_l    |     81.64 |       81.64 |     0    |          0    |        1    |                          0.05 |            5.36 |
| syco_opinion | L_s    |     77.7  |       77.7  |     0.01 |          0    |        1    |                          0.04 |            5.5  |
| syco_opinion | orig   |     86.48 |       86.48 |     0    |          0    |        1    |                          0.05 |            5.16 |
| wildchat     | H_l    |     21.76 |       21.76 |     0.49 |          0.98 |        0.31 |                          0.17 |            4.61 |
| wildchat     | H_s    |     16.38 |       16.38 |     0.11 |          0.97 |        0.25 |                          0.13 |            4.74 |
| wildchat     | L_l    |     19.54 |       19.54 |     0.4  |          0    |        0.95 |                          0.03 |            4.98 |
| wildchat     | L_s    |     17.33 |       17.33 |     0.34 |          0    |        0.95 |                          0.03 |            5.15 |
| wildchat     | orig   |     17.45 |       17.45 |     0.12 |          0.36 |        0.44 |                          0.02 |            5.11 |

## Probe by layer: Llama-3.1-8B-Instruct

|   layer |   auc_L_vs_H |   auc_short_cells |   auc_long_vs_short_on_auth |   auc_L_vs_realhuman |   auc_Hrewrite_vs_realhuman |   auc_random_dir |   auc_train_gpt_test_claude |   cos_auth_eval |   cos_auth_len |   cos_auth_refusal |   cos_null_cov_abs |   cos_null_iso_abs |   eval_split_half_cos |
|--------:|-------------:|------------------:|----------------------------:|---------------------:|----------------------------:|-----------------:|----------------------------:|----------------:|---------------:|-------------------:|-------------------:|-------------------:|----------------------:|
|       2 |        0.96  |             0.958 |                       0.499 |                0.801 |                       0.361 |            0.575 |                       0.978 |          -0.086 |          0.028 |              0.401 |              0.211 |              0.009 |                 0.677 |
|       4 |        0.982 |             0.98  |                       0.513 |                0.82  |                       0.308 |            0.648 |                       0.987 |          -0.108 |          0.171 |              0.466 |              0.13  |              0.02  |                 0.497 |
|       6 |        0.988 |             0.989 |                       0.518 |                0.857 |                       0.315 |            0.576 |                       0.991 |          -0.032 |          0.162 |              0.348 |              0.113 |              0.009 |                 0.405 |
|       8 |        0.98  |             0.978 |                       0.521 |                0.852 |                       0.35  |            0.609 |                       0.988 |          -0.035 |          0.188 |              0.194 |              0.094 |              0.021 |                 0.469 |
|      10 |        0.956 |             0.962 |                       0.532 |                0.854 |                       0.408 |            0.581 |                       0.974 |          -0.032 |          0.35  |              0.12  |              0.063 |              0.016 |                 0.508 |
|      12 |        0.91  |             0.925 |                       0.525 |                0.818 |                       0.408 |            0.536 |                       0.912 |           0.05  |          0.301 |              0.04  |              0.05  |              0.009 |                 0.522 |
|      14 |        0.842 |             0.848 |                       0.505 |                0.756 |                       0.407 |            0.541 |                       0.827 |           0.127 |          0.149 |              0.108 |              0.063 |              0.01  |                 0.589 |
|      16 |        0.76  |             0.758 |                       0.492 |                0.689 |                       0.419 |            0.538 |                       0.745 |           0.225 |          0.038 |              0.178 |              0.102 |              0.018 |                 0.733 |
|      18 |        0.717 |             0.703 |                       0.479 |                0.645 |                       0.413 |            0.548 |                       0.71  |           0.34  |         -0.097 |              0.255 |              0.139 |              0.017 |                 0.756 |
|      20 |        0.713 |             0.693 |                       0.472 |                0.634 |                       0.409 |            0.519 |                       0.702 |           0.373 |         -0.167 |              0.245 |              0.125 |              0.01  |                 0.75  |
|      22 |        0.709 |             0.689 |                       0.47  |                0.63  |                       0.409 |            0.538 |                       0.692 |           0.398 |         -0.227 |              0.182 |              0.122 |              0.019 |                 0.749 |
|      24 |        0.709 |             0.688 |                       0.469 |                0.631 |                       0.407 |            0.519 |                       0.689 |           0.375 |         -0.269 |              0.173 |              0.109 |              0.014 |                 0.735 |
|      26 |        0.698 |             0.679 |                       0.474 |                0.622 |                       0.411 |            0.515 |                       0.676 |           0.346 |         -0.239 |              0.237 |              0.11  |              0.009 |                 0.718 |
|      28 |        0.711 |             0.693 |                       0.475 |                0.626 |                       0.403 |            0.519 |                       0.689 |           0.346 |         -0.225 |              0.254 |              0.107 |              0.008 |                 0.701 |
|      30 |        0.723 |             0.705 |                       0.474 |                0.63  |                       0.402 |            0.515 |                       0.694 |           0.324 |         -0.217 |              0.236 |              0.09  |              0.013 |                 0.715 |
|      32 |        0.722 |             0.698 |                       0.462 |                0.623 |                       0.388 |            0.517 |                       0.695 |           0.326 |         -0.29  |              0.131 |              0.078 |              0.013 |                 0.748 |

```
{
 "auc_length_only": 0.5122162022703818,
 "auc_surface_features_logreg": 0.9944917440660473,
 "auc_logreg_probe_selected_layer": 0.9879772961816305,
 "auc_diffmeans_selected_layer": 0.9096749226006192,
 "auc_verbal_judgment": 0.5449948400412796,
 "auc_diffmeans_user_token_mean_pool": 0.9578087375300999,
 "auc_evaldir_benchmark_orig_vs_wildchat_orig": 0.6680333333333334,
 "auc_authdir_benchmark_orig_vs_wildchat_orig": 0.8141428571428571,
 "corr_probe_evalproj_within_rewrites": 0.5451413031826167,
 "corr_probe_verbal_ai_judgment": -0.2191225527880963,
 "corr_probe_verbal_test_judgment": -0.09243284017072806,
 "selected_layer": 12
}
```

| task         |   auc_probe_L_vs_H |   auc_probe_long_vs_short |   probe_style_gap_sd |   probe_length_gap_sd |   evalproj_style |   evalproj_style_p |   evalproj_length |   evalproj_length_p |   verbal_test_style |   verbal_test_style_p |   verbal_test_length |   verbal_test_length_p |
|:-------------|-------------------:|--------------------------:|---------------------:|----------------------:|-----------------:|-------------------:|------------------:|--------------------:|--------------------:|----------------------:|---------------------:|-----------------------:|
| accuracy     |              0.956 |                     0.475 |                1.104 |                -0.105 |            0.108 |                  0 |            -0.051 |                   0 |               0.192 |                 0     |               -0.123 |                  0     |
| refusal      |              0.93  |                     0.506 |                1.496 |                 0.027 |            0.048 |                  0 |            -0.03  |                   0 |               0.188 |                 0     |               -0.087 |                  0     |
| syco_fact    |              0.998 |                     0.526 |                1.364 |                 0.065 |            0.092 |                  0 |            -0.028 |                   0 |               0.147 |                 0     |                0.001 |                  0.98  |
| syco_opinion |              0.861 |                     0.512 |                0.282 |                 0.012 |            0.031 |                  0 |            -0.01  |                   0 |               0.274 |                 0     |               -0.018 |                  0.152 |
| wildchat     |              0.91  |                     0.525 |                1.413 |                 0.145 |            0.042 |                  0 |            -0.034 |                   0 |               0.028 |                 0.404 |               -0.065 |                  0.022 |

| outcome              | spec        | term      |    coef |     se |      p |    n |
|:---------------------|:------------|:----------|--------:|-------:|-------:|-----:|
| acc_under_suggestion | style_only  | style_L   |  0.0073 | 0.0196 | 0.7086 | 1160 |
| acc_under_suggestion | style_only  | long      | -0.0158 | 0.0142 | 0.264  | 1160 |
| acc_under_suggestion | probe_only  | probe_z   |  0.0112 | 0.0136 | 0.4072 | 1160 |
| acc_under_suggestion | probe_only  | log_words | -0.1129 | 0.0566 | 0.0459 | 1160 |
| acc_under_suggestion | probe_only  | polite    |  0.0189 | 0.0192 | 0.3249 | 1160 |
| acc_under_suggestion | style+probe | style_L   | -0.1355 | 0.0687 | 0.0484 | 1160 |
| acc_under_suggestion | style+probe | probe_z   |  0.1046 | 0.0469 | 0.0258 | 1160 |
| acc_under_suggestion | style+probe | log_words | -0.1279 | 0.0579 | 0.0273 | 1160 |
| acc_under_suggestion | style+probe | polite    | -0.0002 | 0.0213 | 0.9933 | 1160 |
| accuracy             | style_only  | style_L   | -0.0133 | 0.0189 | 0.4829 | 1187 |
| accuracy             | style_only  | long      |  0.0099 | 0.011  | 0.3664 | 1187 |
| accuracy             | probe_only  | probe_z   | -0.0131 | 0.012  | 0.2749 | 1187 |
| accuracy             | probe_only  | log_words |  0.0315 | 0.0536 | 0.556  | 1187 |
| accuracy             | probe_only  | polite    |  0.0467 | 0.0346 | 0.1768 | 1187 |
| accuracy             | style+probe | style_L   |  0.0009 | 0.0311 | 0.9773 | 1187 |
| accuracy             | style+probe | probe_z   | -0.0137 | 0.0196 | 0.4846 | 1187 |
| accuracy             | style+probe | log_words |  0.0311 | 0.0587 | 0.5965 | 1187 |
| accuracy             | style+probe | polite    |  0.0465 | 0.0343 | 0.1748 | 1187 |
| refusal              | style_only  | style_L   |  0.0045 | 0.0104 | 0.6666 | 1789 |
| refusal              | style_only  | long      | -0.0153 | 0.0071 | 0.0319 | 1789 |
| refusal              | probe_only  | probe_z   |  0.0063 | 0.007  | 0.3744 | 1789 |
| refusal              | probe_only  | log_words | -0.035  | 0.021  | 0.0957 | 1789 |
| refusal              | probe_only  | polite    |  0.0026 | 0.0179 | 0.8863 | 1789 |
| refusal              | style+probe | style_L   | -0.0276 | 0.0268 | 0.3038 | 1789 |
| refusal              | style+probe | probe_z   |  0.0212 | 0.0174 | 0.2219 | 1789 |
| refusal              | style+probe | log_words | -0.0329 | 0.0204 | 0.1072 | 1789 |
| refusal              | style+probe | polite    |  0.0022 | 0.0179 | 0.9008 | 1789 |
| syco_fact            | style_only  | style_L   | -0.0158 | 0.0145 | 0.2742 | 1160 |
| syco_fact            | style_only  | long      |  0.0139 | 0.0094 | 0.1406 | 1160 |
| syco_fact            | probe_only  | probe_z   | -0.0129 | 0.0107 | 0.2276 | 1160 |
| syco_fact            | probe_only  | log_words |  0.0576 | 0.0354 | 0.104  | 1160 |
| syco_fact            | probe_only  | polite    | -0.0141 | 0.0164 | 0.3895 | 1160 |
| syco_fact            | style+probe | style_L   |  0.0317 | 0.0443 | 0.4741 | 1160 |
| syco_fact            | style+probe | probe_z   | -0.0347 | 0.0333 | 0.2971 | 1160 |
| syco_fact            | style+probe | log_words |  0.0611 | 0.0362 | 0.0914 | 1160 |
| syco_fact            | style+probe | polite    | -0.0097 | 0.0157 | 0.5371 | 1160 |
| syco_opinion         | style_only  | style_L   |  0.0014 | 0.0058 | 0.8119 | 1188 |
| syco_opinion         | style_only  | long      | -0.0026 | 0.0026 | 0.316  | 1188 |
| syco_opinion         | probe_only  | probe_z   |  0.0214 | 0.0216 | 0.3238 | 1188 |
| syco_opinion         | probe_only  | log_words |  0.0175 | 0.0435 | 0.6876 | 1188 |
| syco_opinion         | probe_only  | polite    | -0.0567 | 0.0279 | 0.0422 | 1188 |
| syco_opinion         | style+probe | style_L   | -0.0303 | 0.0105 | 0.0039 | 1188 |
| syco_opinion         | style+probe | probe_z   |  0.1121 | 0.0412 | 0.0065 | 1188 |
| syco_opinion         | style+probe | log_words |  0.0119 | 0.0455 | 0.7937 | 1188 |
| syco_opinion         | style+probe | polite    | -0.0525 | 0.0278 | 0.059  | 1188 |

## Steering, sign-dependent effect (delta(+a)-delta(-a))/2 : Llama-3.1-8B-Instruct

|   layer |   abs_alpha | direction   | accuracy                    | judge_ai                    | judge_test                  | refusal                     | resp_lowercase              | syco_fact                   | syco_opinion                |
|--------:|------------:|:------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|
|       6 |           4 | auth        | +0.055 (rand 0.017; p=0.11) | -2.951 (rand 0.868; p=0.11) | -0.067 (rand 0.860; p=1.00) | -0.004 (rand 0.018; p=0.89) | -0.132 (rand 0.001; p=0.11) | -0.007 (rand 0.018; p=0.89) | -0.039 (rand 0.039; p=0.44) |
|       6 |           4 | eval        | -0.035 (rand 0.017; p=0.33) | -0.553 (rand 0.868; p=0.67) | -0.209 (rand 0.860; p=0.89) | +0.016 (rand 0.018; p=0.56) | +0.001 (rand 0.001; p=0.67) | +0.037 (rand 0.018; p=0.22) | +0.035 (rand 0.039; p=0.56) |
|       6 |           4 | len         | +0.000 (rand 0.017; p=1.00) | +0.035 (rand 0.868; p=1.00) | -1.531 (rand 0.860; p=0.33) | -0.008 (rand 0.018; p=0.67) | -0.001 (rand 0.001; p=0.67) | -0.020 (rand 0.018; p=0.33) | -0.028 (rand 0.039; p=0.78) |
|       6 |           4 | refusal     | +0.025 (rand 0.017; p=0.44) | +0.776 (rand 0.868; p=0.44) | -0.810 (rand 0.860; p=0.56) | +0.076 (rand 0.018; p=0.11) | -0.005 (rand 0.001; p=0.11) | -0.007 (rand 0.018; p=0.89) | -0.060 (rand 0.039; p=0.33) |
|       6 |           8 | auth        | -0.065 (rand 0.048; p=0.56) | +0.944 (rand 1.040; p=0.56) | +0.200 (rand 0.874; p=0.78) | -0.108 (rand 0.119; p=0.67) | -0.436 (rand 0.002; p=0.11) | +0.060 (rand 0.100; p=0.44) | -0.001 (rand 0.017; p=1.00) |
|       6 |           8 | eval        | +0.085 (rand 0.048; p=0.22) | -1.896 (rand 1.040; p=0.33) | +1.756 (rand 0.874; p=0.22) | -0.052 (rand 0.119; p=0.78) | -0.001 (rand 0.002; p=0.89) | -0.060 (rand 0.100; p=0.44) | +0.016 (rand 0.017; p=0.44) |
|       6 |           8 | len         | +0.000 (rand 0.048; p=1.00) | +1.730 (rand 1.040; p=0.33) | -1.618 (rand 0.874; p=0.22) | +0.076 (rand 0.119; p=0.67) | -0.066 (rand 0.002; p=0.11) | -0.010 (rand 0.100; p=1.00) | -0.001 (rand 0.017; p=1.00) |
|       6 |           8 | refusal     | +0.035 (rand 0.048; p=0.56) | +0.677 (rand 1.040; p=0.56) | -1.434 (rand 0.874; p=0.22) | +0.378 (rand 0.119; p=0.11) | -0.089 (rand 0.002; p=0.11) | -0.007 (rand 0.100; p=1.00) | -0.001 (rand 0.017; p=1.00) |
|      12 |           4 | auth        | +0.000 (rand 0.019; p=1.00) | -1.591 (rand 0.771; p=0.22) | -0.356 (rand 0.346; p=0.44) | -0.018 (rand 0.023; p=0.67) | -0.001 (rand 0.001; p=0.67) | -0.060 (rand 0.026; p=0.11) | +0.028 (rand 0.024; p=0.44) |
|      12 |           4 | eval        | -0.010 (rand 0.019; p=0.78) | -0.049 (rand 0.771; p=1.00) | -0.751 (rand 0.346; p=0.11) | -0.006 (rand 0.023; p=1.00) | +0.000 (rand 0.001; p=1.00) | -0.030 (rand 0.026; p=0.44) | -0.012 (rand 0.024; p=0.67) |
|      12 |           4 | len         | +0.030 (rand 0.019; p=0.33) | +0.133 (rand 0.771; p=0.89) | +0.048 (rand 0.346; p=0.89) | -0.048 (rand 0.023; p=0.22) | +0.002 (rand 0.001; p=0.33) | +0.017 (rand 0.026; p=0.67) | +0.007 (rand 0.024; p=0.89) |
|      12 |           4 | refusal     | -0.055 (rand 0.019; p=0.11) | -4.592 (rand 0.771; p=0.11) | +3.764 (rand 0.346; p=0.11) | +0.358 (rand 0.023; p=0.11) | -0.001 (rand 0.001; p=0.67) | +0.017 (rand 0.026; p=0.67) | -0.065 (rand 0.024; p=0.11) |
|      12 |           8 | auth        | +0.040 (rand 0.034; p=0.44) | -6.668 (rand 1.176; p=0.11) | +0.070 (rand 0.731; p=0.89) | -0.078 (rand 0.050; p=0.44) | -0.466 (rand 0.001; p=0.11) | -0.153 (rand 0.077; p=0.11) | +0.050 (rand 0.029; p=0.33) |
|      12 |           8 | eval        | +0.000 (rand 0.034; p=1.00) | -0.037 (rand 1.176; p=1.00) | -0.008 (rand 0.731; p=1.00) | +0.028 (rand 0.050; p=0.67) | -0.002 (rand 0.001; p=0.44) | -0.100 (rand 0.077; p=0.44) | -0.034 (rand 0.029; p=0.44) |
|      12 |           8 | len         | -0.015 (rand 0.034; p=0.67) | -0.060 (rand 1.176; p=1.00) | +0.435 (rand 0.731; p=0.67) | -0.068 (rand 0.050; p=0.44) | -0.001 (rand 0.001; p=0.78) | +0.000 (rand 0.077; p=1.00) | -0.031 (rand 0.029; p=0.44) |
|      12 |           8 | refusal     | -0.155 (rand 0.034; p=0.11) | -3.259 (rand 1.176; p=0.11) | +3.365 (rand 0.731; p=0.11) | +0.450 (rand 0.050; p=0.11) | +0.000 (rand 0.001; p=1.00) | +0.033 (rand 0.077; p=0.89) | -0.012 (rand 0.029; p=0.67) |
|      24 |           4 | auth        | +0.005 (rand 0.025; p=1.00) | +1.282 (rand 0.576; p=0.11) | -0.530 (rand 0.329; p=0.22) | -0.016 (rand 0.008; p=0.22) | +0.002 (rand 0.000; p=0.11) | -0.013 (rand 0.013; p=0.56) | -0.018 (rand 0.005; p=0.11) |
|      24 |           4 | eval        | -0.075 (rand 0.025; p=0.11) | +0.806 (rand 0.576; p=0.22) | +0.329 (rand 0.329; p=0.56) | -0.032 (rand 0.008; p=0.11) | -0.002 (rand 0.000; p=0.11) | +0.040 (rand 0.013; p=0.11) | -0.015 (rand 0.005; p=0.11) |
|      24 |           4 | len         | -0.040 (rand 0.025; p=0.22) | +0.476 (rand 0.576; p=0.56) | -0.040 (rand 0.329; p=1.00) | +0.046 (rand 0.008; p=0.11) | +0.000 (rand 0.000; p=1.00) | -0.010 (rand 0.013; p=0.67) | -0.001 (rand 0.005; p=1.00) |
|      24 |           4 | refusal     | -0.080 (rand 0.025; p=0.11) | +0.428 (rand 0.576; p=0.67) | +0.137 (rand 0.329; p=1.00) | +0.066 (rand 0.008; p=0.11) | +0.002 (rand 0.000; p=0.11) | -0.003 (rand 0.013; p=0.89) | -0.000 (rand 0.005; p=1.00) |
|      24 |           8 | auth        | +0.020 (rand 0.022; p=0.44) | +2.355 (rand 1.157; p=0.22) | -0.977 (rand 0.615; p=0.11) | -0.020 (rand 0.014; p=0.33) | +0.002 (rand 0.001; p=0.22) | +0.013 (rand 0.012; p=0.44) | -0.035 (rand 0.009; p=0.11) |
|      24 |           8 | eval        | -0.055 (rand 0.022; p=0.22) | +2.022 (rand 1.157; p=0.22) | +1.299 (rand 0.615; p=0.11) | -0.020 (rand 0.014; p=0.33) | -0.001 (rand 0.001; p=0.67) | +0.027 (rand 0.012; p=0.22) | -0.025 (rand 0.009; p=0.11) |
|      24 |           8 | len         | -0.035 (rand 0.022; p=0.33) | +0.774 (rand 1.157; p=0.78) | -0.153 (rand 0.615; p=1.00) | +0.226 (rand 0.014; p=0.11) | -0.001 (rand 0.001; p=0.22) | +0.020 (rand 0.012; p=0.22) | -0.006 (rand 0.009; p=0.56) |
|      24 |           8 | refusal     | -0.160 (rand 0.022; p=0.11) | +0.867 (rand 1.157; p=0.78) | +0.412 (rand 0.615; p=0.78) | +0.150 (rand 0.014; p=0.11) | +0.001 (rand 0.001; p=0.67) | +0.000 (rand 0.012; p=1.00) | +0.000 (rand 0.009; p=1.00) |

## Steering along authorship direction, change vs unsteered: Llama-3.1-8B-Instruct

|   layer |   alpha | accuracy               | judge_ai               | judge_test             | refusal                | resp_lowercase         | syco_fact              | syco_opinion           |
|--------:|--------:|:-----------------------|:-----------------------|:-----------------------|:-----------------------|:-----------------------|:-----------------------|:-----------------------|
|       6 |      -8 | -0.270 [-0.380,-0.160] | +1.673 [+1.287,+2.055] | +2.241 [+1.990,+2.474] | -0.360 [-0.424,-0.300] | +0.874 [+0.844,+0.902] | +0.133 [+0.040,+0.227] | -0.370 [-0.441,-0.294] |
|       6 |      -4 | -0.040 [-0.130,+0.050] | +5.763 [+5.463,+6.065] | +0.964 [+0.815,+1.122] | +0.040 [+0.012,+0.068] | +0.268 [+0.230,+0.308] | +0.100 [+0.020,+0.180] | -0.126 [-0.170,-0.085] |
|       6 |      -2 | +0.000 [-0.050,+0.050] | +2.422 [+2.274,+2.575] | -0.139 [-0.229,-0.046] | +0.032 [+0.008,+0.056] | +0.000 [+0.000,+0.000] | +0.000 [-0.073,+0.067] | -0.061 [-0.086,-0.037] |
|       6 |      -1 | -0.010 [-0.050,+0.030] | +1.000 [+0.919,+1.081] | -0.207 [-0.256,-0.160] | +0.016 [+0.004,+0.032] | +0.000 [+0.000,+0.000] | +0.007 [-0.040,+0.060] | -0.019 [-0.030,-0.009] |
|       6 |       1 | +0.020 [-0.020,+0.060] | -0.583 [-0.675,-0.496] | +0.181 [+0.135,+0.226] | -0.004 [-0.020,+0.012] | +0.000 [+0.000,+0.000] | +0.007 [-0.040,+0.053] | +0.019 [+0.010,+0.029] |
|       6 |       2 | +0.060 [+0.000,+0.120] | -2.015 [-2.293,-1.732] | +0.111 [-0.032,+0.260] | +0.012 [-0.008,+0.032] | +0.002 [+0.000,+0.006] | -0.007 [-0.067,+0.047] | +0.034 [+0.018,+0.051] |
|       6 |       4 | +0.070 [-0.010,+0.150] | -0.139 [-0.511,+0.244] | +0.830 [+0.581,+1.089] | +0.032 [+0.000,+0.068] | +0.004 [+0.000,+0.010] | +0.087 [+0.013,+0.160] | -0.205 [-0.252,-0.158] |
|       6 |       8 | -0.400 [-0.510,-0.290] | +3.560 [+3.152,+3.959] | +2.642 [+2.377,+2.890] | -0.576 [-0.636,-0.516] | +0.002 [+0.000,+0.006] | +0.253 [+0.153,+0.347] | -0.373 [-0.444,-0.300] |
|      12 |      -8 | -0.090 [-0.180,-0.010] | +5.228 [+4.932,+5.535] | +0.347 [+0.202,+0.495] | -0.180 [-0.232,-0.132] | +0.936 [+0.914,+0.956] | +0.273 [+0.187,+0.360] | -0.272 [-0.327,-0.216] |
|      12 |      -4 | +0.050 [-0.030,+0.130] | +1.471 [+1.306,+1.629] | +0.715 [+0.658,+0.774] | -0.004 [-0.024,+0.016] | +0.004 [+0.000,+0.010] | +0.100 [+0.033,+0.167] | -0.037 [-0.053,-0.023] |
|      12 |      -2 | +0.020 [-0.040,+0.080] | +0.344 [+0.271,+0.418] | +0.317 [+0.276,+0.356] | +0.008 [-0.008,+0.024] | +0.000 [+0.000,+0.000] | +0.000 [-0.053,+0.053] | -0.017 [-0.025,-0.010] |
|      12 |      -1 | +0.010 [-0.030,+0.050] | +0.103 [+0.062,+0.143] | +0.113 [+0.082,+0.143] | +0.004 [-0.008,+0.020] | +0.000 [+0.000,+0.000] | -0.020 [-0.067,+0.027] | -0.010 [-0.014,-0.006] |
|      12 |       1 | +0.010 [+0.000,+0.030] | -0.050 [-0.093,-0.008] | -0.046 [-0.071,-0.019] | -0.008 [-0.024,+0.008] | +0.000 [+0.000,+0.000] | -0.007 [-0.047,+0.033] | +0.011 [+0.007,+0.016] |
|      12 |       2 | +0.040 [+0.010,+0.080] | -0.194 [-0.268,-0.119] | -0.086 [-0.131,-0.043] | -0.016 [-0.036,+0.004] | +0.002 [+0.000,+0.006] | +0.013 [-0.033,+0.060] | +0.019 [+0.011,+0.028] |
|      12 |       4 | +0.050 [-0.010,+0.120] | -1.711 [-1.904,-1.531] | +0.003 [-0.076,+0.079] | -0.040 [-0.068,-0.012] | +0.002 [+0.000,+0.006] | -0.020 [-0.080,+0.040] | +0.019 [+0.003,+0.035] |
|      12 |       8 | -0.010 [-0.110,+0.100] | -8.108 [-8.456,-7.759] | +0.487 [+0.339,+0.633] | -0.336 [-0.392,-0.276] | +0.004 [+0.000,+0.010] | -0.033 [-0.100,+0.033] | -0.172 [-0.219,-0.124] |
|      24 |      -8 | -0.100 [-0.170,-0.020] | -3.126 [-3.457,-2.788] | +0.932 [+0.801,+1.086] | +0.000 [-0.024,+0.024] | +0.000 [+0.000,+0.000] | +0.053 [-0.020,+0.127] | +0.027 [+0.020,+0.033] |
|      24 |      -4 | +0.010 [-0.050,+0.070] | -1.389 [-1.583,-1.197] | +0.343 [+0.296,+0.397] | +0.008 [-0.008,+0.028] | +0.000 [+0.000,+0.000] | +0.013 [-0.047,+0.073] | +0.015 [+0.012,+0.019] |
|      24 |      -2 | +0.020 [-0.030,+0.070] | -0.682 [-0.779,-0.589] | +0.219 [+0.193,+0.250] | +0.008 [-0.008,+0.024] | +0.000 [+0.000,+0.000] | -0.007 [-0.047,+0.033] | +0.008 [+0.006,+0.010] |
|      24 |      -1 | +0.000 [-0.030,+0.030] | -0.344 [-0.396,-0.297] | +0.135 [+0.115,+0.158] | +0.008 [+0.000,+0.020] | +0.000 [+0.000,+0.000] | +0.000 [-0.047,+0.047] | +0.004 [+0.003,+0.005] |
|      24 |       1 | +0.020 [-0.030,+0.070] | +0.310 [+0.276,+0.346] | -0.158 [-0.178,-0.139] | -0.012 [-0.028,+0.000] | +0.000 [+0.000,+0.000] | +0.020 [-0.013,+0.053] | -0.005 [-0.006,-0.003] |
|      24 |       2 | +0.040 [-0.010,+0.090] | +0.624 [+0.562,+0.689] | -0.338 [-0.367,-0.310] | -0.008 [-0.024,+0.008] | +0.002 [+0.000,+0.006] | +0.027 [-0.020,+0.073] | -0.009 [-0.011,-0.007] |
|      24 |       4 | +0.020 [-0.050,+0.090] | +1.175 [+1.069,+1.281] | -0.717 [-0.774,-0.667] | -0.024 [-0.044,-0.008] | +0.004 [+0.000,+0.010] | -0.013 [-0.060,+0.033] | -0.020 [-0.024,-0.016] |
|      24 |       8 | -0.060 [-0.150,+0.030] | +1.583 [+1.443,+1.726] | -1.022 [-1.122,-0.926] | -0.040 [-0.072,-0.012] | +0.004 [+0.000,+0.010] | +0.080 [+0.007,+0.160] | -0.042 [-0.050,-0.035] |

## Probe by layer: Qwen2.5-7B-Instruct

|   layer |   auc_L_vs_H |   auc_short_cells |   auc_long_vs_short_on_auth |   auc_L_vs_realhuman |   auc_Hrewrite_vs_realhuman |   auc_random_dir |   auc_train_gpt_test_claude |   cos_auth_eval |   cos_auth_len |   cos_auth_refusal |   cos_null_cov_abs |   cos_null_iso_abs |   eval_split_half_cos |
|--------:|-------------:|------------------:|----------------------------:|---------------------:|----------------------------:|-----------------:|----------------------------:|----------------:|---------------:|-------------------:|-------------------:|-------------------:|----------------------:|
|       2 |        0.972 |             0.967 |                       0.483 |                0.797 |                       0.309 |            0.574 |                       0.97  |          -0.03  |         -0.064 |              0.373 |              0.152 |              0.012 |                 0.61  |
|       4 |        0.984 |             0.977 |                       0.458 |                0.819 |                       0.238 |            0.629 |                       0.973 |           0.052 |         -0.214 |              0.307 |              0.148 |              0.017 |                 0.475 |
|       6 |        0.992 |             0.991 |                       0.491 |                0.884 |                       0.282 |            0.682 |                       0.998 |           0.16  |          0.014 |              0.597 |              0.228 |              0.016 |                 0.375 |
|       8 |        0.994 |             0.992 |                       0.476 |                0.899 |                       0.289 |            0.649 |                       1     |           0.178 |         -0.071 |              0.628 |              0.282 |              0.011 |                 0.485 |
|      10 |        0.995 |             0.993 |                       0.486 |                0.9   |                       0.308 |            0.606 |                       0.999 |           0.066 |          0.001 |              0.613 |              0.254 |              0.011 |                 0.411 |
|      12 |        0.99  |             0.985 |                       0.499 |                0.89  |                       0.341 |            0.647 |                       0.997 |           0.156 |          0.084 |              0.634 |              0.286 |              0.013 |                 0.406 |
|      14 |        0.986 |             0.978 |                       0.492 |                0.877 |                       0.339 |            0.628 |                       0.994 |           0.124 |          0.028 |              0.42  |              0.211 |              0.016 |                 0.654 |
|      16 |        0.963 |             0.953 |                       0.492 |                0.855 |                       0.356 |            0.577 |                       0.978 |           0.121 |          0.042 |              0.256 |              0.174 |              0.009 |                 0.642 |
|      18 |        0.915 |             0.9   |                       0.488 |                0.809 |                       0.376 |            0.626 |                       0.935 |           0.177 |         -0.017 |              0.193 |              0.14  |              0.024 |                 0.644 |
|      20 |        0.813 |             0.789 |                       0.477 |                0.718 |                       0.396 |            0.533 |                       0.814 |           0.283 |         -0.18  |              0.133 |              0.102 |              0.011 |                 0.596 |
|      22 |        0.711 |             0.684 |                       0.451 |                0.627 |                       0.403 |            0.524 |                       0.683 |           0.322 |         -0.428 |              0.1   |              0.095 |              0.008 |                 0.512 |
|      24 |        0.65  |             0.621 |                       0.443 |                0.567 |                       0.412 |            0.525 |                       0.616 |           0.431 |         -0.648 |              0.182 |              0.168 |              0.013 |                 0.478 |
|      26 |        0.642 |             0.61  |                       0.44  |                0.561 |                       0.41  |            0.527 |                       0.608 |           0.434 |         -0.642 |              0.129 |              0.148 |              0.015 |                 0.436 |
|      28 |        0.649 |             0.617 |                       0.443 |                0.58  |                       0.425 |            0.53  |                       0.624 |           0.465 |         -0.634 |              0.102 |              0.121 |              0.018 |                 0.395 |

```
{
 "auc_length_only": 0.5122162022703818,
 "auc_surface_features_logreg": 0.9944917440660473,
 "auc_logreg_probe_selected_layer": 0.9975060199518404,
 "auc_diffmeans_selected_layer": 0.9152734778121774,
 "auc_verbal_judgment": 0.662173202614379,
 "auc_diffmeans_user_token_mean_pool": 0.9772789817681459,
 "auc_evaldir_benchmark_orig_vs_wildchat_orig": 0.6132857142857143,
 "auc_authdir_benchmark_orig_vs_wildchat_orig": 0.828895238095238,
 "corr_probe_evalproj_within_rewrites": 0.4604280451163537,
 "corr_probe_verbal_ai_judgment": 0.07543957153188496,
 "corr_probe_verbal_test_judgment": 0.28398828779115715,
 "selected_layer": 18
}
```

| task         |   auc_probe_L_vs_H |   auc_probe_long_vs_short |   probe_style_gap_sd |   probe_length_gap_sd |   evalproj_style |   evalproj_style_p |   evalproj_length |   evalproj_length_p |   verbal_test_style |   verbal_test_style_p |   verbal_test_length |   verbal_test_length_p |
|:-------------|-------------------:|--------------------------:|---------------------:|----------------------:|-----------------:|-------------------:|------------------:|--------------------:|--------------------:|----------------------:|---------------------:|-----------------------:|
| accuracy     |              0.973 |                     0.46  |                1.203 |                -0.165 |            1.089 |                  0 |            -0.204 |               0     |               4.944 |                     0 |               -2.16  |                  0     |
| refusal      |              0.981 |                     0.483 |                1.587 |                -0.07  |            1.837 |                  0 |            -0.153 |               0     |               2.582 |                     0 |               -1.159 |                  0     |
| syco_fact    |              0.998 |                     0.5   |                1.239 |                 0.001 |            1.719 |                  0 |            -0.188 |               0     |               4.014 |                     0 |               -0.622 |                  0     |
| syco_opinion |              0.806 |                     0.513 |                0.248 |                 0.006 |            0.237 |                  0 |            -0.031 |               0.005 |               2.591 |                     0 |               -0.141 |                  0.016 |
| wildchat     |              0.915 |                     0.488 |                1.406 |                -0.017 |            1.386 |                  0 |            -0.239 |               0     |               2.638 |                     0 |               -1.315 |                  0     |

| outcome              | spec        | term      |    coef |     se |      p |    n |
|:---------------------|:------------|:----------|--------:|-------:|-------:|-----:|
| acc_under_suggestion | style_only  | style_L   |  0.0279 | 0.0167 | 0.0939 | 1160 |
| acc_under_suggestion | style_only  | long      |  0.0038 | 0.0141 | 0.7884 | 1160 |
| acc_under_suggestion | probe_only  | probe_z   |  0.0174 | 0.0126 | 0.1667 | 1160 |
| acc_under_suggestion | probe_only  | log_words | -0.0156 | 0.068  | 0.8192 | 1160 |
| acc_under_suggestion | probe_only  | polite    |  0.0296 | 0.0274 | 0.2793 | 1160 |
| acc_under_suggestion | style+probe | style_L   |  0.0774 | 0.0459 | 0.0913 | 1160 |
| acc_under_suggestion | style+probe | probe_z   | -0.04   | 0.0338 | 0.2367 | 1160 |
| acc_under_suggestion | style+probe | log_words | -0.0165 | 0.0678 | 0.8079 | 1160 |
| acc_under_suggestion | style+probe | polite    |  0.0383 | 0.0271 | 0.1581 | 1160 |
| accuracy             | style_only  | style_L   | -0.0181 | 0.0114 | 0.1131 | 1187 |
| accuracy             | style_only  | long      | -0.0127 | 0.0113 | 0.2593 | 1187 |
| accuracy             | probe_only  | probe_z   | -0.0078 | 0.009  | 0.3888 | 1187 |
| accuracy             | probe_only  | log_words |  0.0098 | 0.0415 | 0.8128 | 1187 |
| accuracy             | probe_only  | polite    | -0.0424 | 0.0546 | 0.4371 | 1187 |
| accuracy             | style+probe | style_L   | -0.0332 | 0.0216 | 0.1238 | 1187 |
| accuracy             | style+probe | probe_z   |  0.0142 | 0.0174 | 0.4169 | 1187 |
| accuracy             | style+probe | log_words |  0.031  | 0.0399 | 0.4377 | 1187 |
| accuracy             | style+probe | polite    | -0.0392 | 0.0549 | 0.4744 | 1187 |
| refusal              | style_only  | style_L   |  0.0016 | 0.0123 | 0.8952 | 1789 |
| refusal              | style_only  | long      |  0.0018 | 0.0073 | 0.8091 | 1789 |
| refusal              | probe_only  | probe_z   | -0.0005 | 0.0078 | 0.9474 | 1789 |
| refusal              | probe_only  | log_words | -0.0249 | 0.0239 | 0.2982 | 1789 |
| refusal              | probe_only  | polite    |  0.0113 | 0.0141 | 0.4237 | 1789 |
| refusal              | style+probe | style_L   |  0.0049 | 0.0278 | 0.86   | 1789 |
| refusal              | style+probe | probe_z   | -0.0032 | 0.0182 | 0.8611 | 1789 |
| refusal              | style+probe | log_words | -0.0258 | 0.0229 | 0.2596 | 1789 |
| refusal              | style+probe | polite    |  0.0112 | 0.0142 | 0.4286 | 1789 |
| syco_fact            | style_only  | style_L   | -0.0318 | 0.0196 | 0.1043 | 1160 |
| syco_fact            | style_only  | long      | -0.027  | 0.0155 | 0.0811 | 1160 |
| syco_fact            | probe_only  | probe_z   | -0.0171 | 0.015  | 0.2538 | 1160 |
| syco_fact            | probe_only  | log_words | -0.1316 | 0.0657 | 0.0451 | 1160 |
| syco_fact            | probe_only  | polite    | -0.05   | 0.031  | 0.1069 | 1160 |
| syco_fact            | style+probe | style_L   | -0.1258 | 0.069  | 0.0681 | 1160 |
| syco_fact            | style+probe | probe_z   |  0.0763 | 0.0529 | 0.1488 | 1160 |
| syco_fact            | style+probe | log_words | -0.13   | 0.0656 | 0.0473 | 1160 |
| syco_fact            | style+probe | polite    | -0.0641 | 0.0306 | 0.0362 | 1160 |
| syco_opinion         | style_only  | style_L   |  0.0222 | 0.0086 | 0.01   | 1188 |
| syco_opinion         | style_only  | long      |  0.0076 | 0.0054 | 0.1558 | 1188 |
| syco_opinion         | probe_only  | probe_z   |  0.0633 | 0.0312 | 0.0425 | 1188 |
| syco_opinion         | probe_only  | log_words |  0.167  | 0.0912 | 0.0671 | 1188 |
| syco_opinion         | probe_only  | polite    | -0.0724 | 0.0247 | 0.0034 | 1188 |
| syco_opinion         | style+probe | style_L   |  0.0229 | 0.0129 | 0.0763 | 1188 |
| syco_opinion         | style+probe | probe_z   | -0.0123 | 0.0426 | 0.773  | 1188 |
| syco_opinion         | style+probe | log_words |  0.169  | 0.092  | 0.0662 | 1188 |
| syco_opinion         | style+probe | polite    | -0.0703 | 0.027  | 0.0093 | 1188 |

## Steering, sign-dependent effect (delta(+a)-delta(-a))/2 : Qwen2.5-7B-Instruct

|   layer |   abs_alpha | direction   | accuracy                    | judge_ai                    | judge_test                  | refusal                     | resp_lowercase              | syco_fact                   | syco_opinion                |
|--------:|------------:|:------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|
|      10 |           4 | auth        | -0.030 (rand 0.022; p=0.22) | -2.198 (rand 3.455; p=0.56) | +5.883 (rand 2.940; p=0.11) | -0.002 (rand 0.029; p=0.89) | +0.001 (rand 0.001; p=0.89) | -0.030 (rand 0.037; p=0.56) | +0.044 (rand 0.022; p=0.22) |
|      10 |           4 | eval        | -0.015 (rand 0.022; p=0.78) | +0.988 (rand 3.455; p=0.89) | +2.617 (rand 2.940; p=0.67) | -0.036 (rand 0.029; p=0.44) | +0.002 (rand 0.001; p=0.33) | -0.110 (rand 0.037; p=0.11) | +0.036 (rand 0.022; p=0.33) |
|      10 |           4 | len         | -0.020 (rand 0.022; p=0.44) | -5.669 (rand 3.455; p=0.22) | -2.127 (rand 2.940; p=0.67) | +0.046 (rand 0.029; p=0.22) | +0.000 (rand 0.001; p=1.00) | +0.000 (rand 0.037; p=1.00) | -0.017 (rand 0.022; p=0.56) |
|      10 |           4 | refusal     | +0.005 (rand 0.022; p=1.00) | -2.672 (rand 3.455; p=0.56) | +6.180 (rand 2.940; p=0.11) | +0.128 (rand 0.029; p=0.11) | -0.003 (rand 0.001; p=0.11) | -0.020 (rand 0.037; p=0.78) | +0.005 (rand 0.022; p=1.00) |
|      10 |           8 | auth        | -0.010 (rand 0.059; p=0.89) | -0.835 (rand 2.751; p=0.78) | +2.118 (rand 1.464; p=0.22) | -0.264 (rand 0.067; p=0.11) | -0.001 (rand 0.007; p=0.89) | +0.133 (rand 0.081; p=0.22) | +0.046 (rand 0.043; p=0.56) |
|      10 |           8 | eval        | -0.205 (rand 0.059; p=0.11) | -2.411 (rand 2.751; p=0.56) | +0.894 (rand 1.464; p=0.78) | +0.104 (rand 0.067; p=0.33) | +0.002 (rand 0.007; p=0.78) | -0.077 (rand 0.081; p=0.44) | -0.016 (rand 0.043; p=0.67) |
|      10 |           8 | len         | -0.030 (rand 0.059; p=0.89) | -5.152 (rand 2.751; p=0.22) | -0.831 (rand 1.464; p=0.78) | +0.026 (rand 0.067; p=0.78) | +0.004 (rand 0.007; p=0.56) | +0.147 (rand 0.081; p=0.22) | -0.039 (rand 0.043; p=0.56) |
|      10 |           8 | refusal     | +0.010 (rand 0.059; p=0.89) | -0.610 (rand 2.751; p=0.89) | +1.117 (rand 1.464; p=0.56) | +0.056 (rand 0.067; p=0.67) | -0.001 (rand 0.007; p=0.78) | +0.044 (rand 0.081; p=0.78) | +0.068 (rand 0.043; p=0.44) |
|      12 |           4 | auth        | -0.105 (rand 0.032; p=0.11) | +3.172 (rand 3.761; p=0.56) | +2.235 (rand 3.505; p=0.89) | -0.016 (rand 0.042; p=0.89) | +0.001 (rand 0.002; p=0.78) | -0.083 (rand 0.065; p=0.33) | +0.004 (rand 0.027; p=0.78) |
|      12 |           4 | eval        | -0.005 (rand 0.032; p=1.00) | +5.589 (rand 3.761; p=0.56) | +6.354 (rand 3.505; p=0.11) | -0.068 (rand 0.042; p=0.11) | +0.002 (rand 0.002; p=0.56) | +0.037 (rand 0.065; p=0.89) | -0.005 (rand 0.027; p=0.67) |
|      12 |           4 | len         | +0.010 (rand 0.032; p=0.89) | -2.003 (rand 3.761; p=0.78) | +3.023 (rand 3.505; p=0.67) | +0.024 (rand 0.042; p=0.89) | +0.000 (rand 0.002; p=1.00) | -0.050 (rand 0.065; p=0.67) | +0.038 (rand 0.027; p=0.33) |
|      12 |           4 | refusal     | +0.005 (rand 0.032; p=1.00) | +3.231 (rand 3.761; p=0.56) | +0.560 (rand 3.505; p=1.00) | +0.216 (rand 0.042; p=0.11) | -0.004 (rand 0.002; p=0.22) | +0.130 (rand 0.065; p=0.22) | +0.130 (rand 0.027; p=0.11) |
|      12 |           8 | auth        | -0.030 (rand 0.099; p=0.89) | -1.027 (rand 2.256; p=0.78) | +3.400 (rand 2.944; p=0.33) | +0.094 (rand 0.089; p=0.56) | +0.003 (rand 0.003; p=0.33) | +0.190 (rand 0.154; p=0.44) | -0.001 (rand 0.025; p=0.78) |
|      12 |           8 | eval        | -0.085 (rand 0.099; p=0.56) | -0.547 (rand 2.256; p=0.89) | +0.814 (rand 2.944; p=1.00) | -0.180 (rand 0.089; p=0.11) | +0.008 (rand 0.003; p=0.22) | -0.087 (rand 0.154; p=0.78) | +0.005 (rand 0.025; p=0.78) |
|      12 |           8 | len         | -0.055 (rand 0.099; p=0.89) | -1.105 (rand 2.256; p=0.78) | +4.784 (rand 2.944; p=0.33) | +0.068 (rand 0.089; p=0.78) | +0.000 (rand 0.003; p=1.00) | +0.110 (rand 0.154; p=0.67) | +0.011 (rand 0.025; p=0.67) |
|      12 |           8 | refusal     | -0.030 (rand 0.099; p=1.00) | -0.642 (rand 2.256; p=0.89) | +0.385 (rand 2.944; p=1.00) | +0.004 (rand 0.089; p=1.00) | -0.006 (rand 0.003; p=0.22) | -0.037 (rand 0.154; p=0.78) | -0.008 (rand 0.025; p=0.78) |
|      18 |           4 | auth        | +0.065 (rand 0.022; p=0.11) | +0.032 (rand 1.573; p=1.00) | +0.992 (rand 2.076; p=0.78) | +0.022 (rand 0.026; p=0.56) | +0.001 (rand 0.001; p=0.67) | -0.007 (rand 0.097; p=1.00) | -0.012 (rand 0.026; p=0.78) |
|      18 |           4 | eval        | +0.000 (rand 0.022; p=1.00) | -2.319 (rand 1.573; p=0.33) | +0.668 (rand 2.076; p=0.78) | +0.002 (rand 0.026; p=1.00) | +0.002 (rand 0.001; p=0.22) | -0.090 (rand 0.097; p=0.67) | +0.000 (rand 0.026; p=1.00) |
|      18 |           4 | len         | -0.010 (rand 0.022; p=0.89) | -1.436 (rand 1.573; p=0.67) | +0.629 (rand 2.076; p=0.78) | -0.008 (rand 0.026; p=0.78) | +0.000 (rand 0.001; p=1.00) | +0.107 (rand 0.097; p=0.67) | +0.022 (rand 0.026; p=0.67) |
|      18 |           4 | refusal     | -0.170 (rand 0.022; p=0.11) | +3.283 (rand 1.573; p=0.11) | -3.243 (rand 2.076; p=0.22) | +0.272 (rand 0.026; p=0.11) | +0.000 (rand 0.001; p=1.00) | -0.207 (rand 0.097; p=0.11) | -0.085 (rand 0.026; p=0.11) |
|      18 |           8 | auth        | +0.125 (rand 0.057; p=0.22) | -0.092 (rand 3.272; p=0.89) | +3.300 (rand 2.736; p=0.44) | +0.026 (rand 0.044; p=0.78) | +0.001 (rand 0.002; p=0.67) | +0.003 (rand 0.163; p=1.00) | -0.034 (rand 0.047; p=0.56) |
|      18 |           8 | eval        | -0.045 (rand 0.057; p=0.56) | -0.214 (rand 3.272; p=0.89) | +0.843 (rand 2.736; p=0.89) | -0.056 (rand 0.044; p=0.56) | +0.001 (rand 0.002; p=0.67) | -0.060 (rand 0.163; p=0.89) | +0.025 (rand 0.047; p=0.56) |
|      18 |           8 | len         | +0.070 (rand 0.057; p=0.44) | -2.317 (rand 3.272; p=0.67) | +1.714 (rand 2.736; p=0.56) | -0.020 (rand 0.044; p=0.78) | -0.002 (rand 0.002; p=0.44) | +0.253 (rand 0.163; p=0.33) | +0.064 (rand 0.047; p=0.44) |
|      18 |           8 | refusal     | -0.245 (rand 0.057; p=0.11) | +1.959 (rand 3.272; p=0.78) | -3.620 (rand 2.736; p=0.44) | +0.304 (rand 0.044; p=0.11) | +0.000 (rand 0.002; p=1.00) | -0.300 (rand 0.163; p=0.22) | -0.011 (rand 0.047; p=0.78) |

## Steering along authorship direction, change vs unsteered: Qwen2.5-7B-Instruct

|   layer |   alpha | accuracy               | judge_ai               | judge_test                | refusal                | resp_lowercase         | syco_fact              | syco_opinion           |
|--------:|--------:|:-----------------------|:-----------------------|:--------------------------|:-----------------------|:-----------------------|:-----------------------|:-----------------------|
|      10 |      -8 | -0.320 [-0.410,-0.220] | +8.057 [+7.179,+8.921] | +8.607 [+7.531,+9.658]    | +0.084 [+0.040,+0.128] | +0.002 [-0.004,+0.008] | +0.073 [-0.020,+0.173] | -0.305 [-0.355,-0.254] |
|      10 |      -4 | -0.080 [-0.150,-0.020] | +0.218 [-0.449,+0.828] | -0.903 [-1.672,-0.140]    | +0.008 [-0.016,+0.032] | +0.000 [+0.000,+0.000] | +0.047 [-0.020,+0.113] | -0.115 [-0.158,-0.073] |
|      10 |      -2 | -0.030 [-0.080,+0.020] | +0.835 [+0.407,+1.246] | -0.729 [-1.269,-0.211]    | +0.000 [-0.024,+0.024] | +0.000 [+0.000,+0.000] | +0.007 [-0.047,+0.060] | -0.051 [-0.077,-0.027] |
|      10 |      -1 | -0.020 [-0.060,+0.020] | +0.357 [+0.114,+0.599] | -0.581 [-0.901,-0.276]    | +0.016 [-0.004,+0.040] | +0.000 [+0.000,+0.000] | -0.013 [-0.067,+0.040] | -0.020 [-0.032,-0.009] |
|      10 |       1 | -0.050 [-0.110,+0.000] | -0.299 [-0.631,+0.060] | +1.251 [+0.886,+1.632]    | +0.024 [+0.004,+0.048] | +0.000 [+0.000,+0.000] | +0.000 [-0.060,+0.060] | +0.013 [+0.003,+0.024] |
|      10 |       2 | -0.050 [-0.110,+0.010] | -1.849 [-2.486,-1.200] | +4.188 [+3.408,+4.983]    | +0.008 [-0.012,+0.032] | -0.002 [-0.006,+0.000] | -0.060 [-0.127,+0.007] | +0.002 [-0.022,+0.024] |
|      10 |       4 | -0.140 [-0.220,-0.060] | -4.178 [-4.994,-3.328] | +10.864 [+9.617,+12.118]  | +0.004 [-0.028,+0.036] | +0.002 [-0.004,+0.010] | -0.013 [-0.087,+0.060] | -0.027 [-0.067,+0.011] |
|      10 |       8 | -0.340 [-0.430,-0.240] | +6.388 [+5.286,+7.488] | +12.843 [+11.532,+14.196] | -0.444 [-0.508,-0.380] | +0.000 [-0.006,+0.006] | +0.340 [+0.247,+0.433] | -0.214 [-0.273,-0.156] |
|      12 |      -8 | -0.490 [-0.590,-0.390] | +1.600 [+0.717,+2.456] | +7.449 [+6.398,+8.478]    | -0.368 [-0.436,-0.300] | +0.002 [-0.004,+0.008] | -0.120 [-0.220,-0.020] | -0.439 [-0.520,-0.355] |
|      12 |      -4 | -0.140 [-0.220,-0.060] | -6.425 [-7.031,-5.799] | +6.001 [+5.190,+6.790]    | -0.080 [-0.120,-0.044] | +0.000 [-0.006,+0.006] | -0.060 [-0.140,+0.020] | -0.209 [-0.267,-0.154] |
|      12 |      -2 | -0.040 [-0.100,+0.010] | -4.583 [-5.015,-4.167] | +3.083 [+2.611,+3.524]    | +0.000 [-0.032,+0.032] | -0.002 [-0.006,+0.000] | -0.060 [-0.133,+0.007] | -0.056 [-0.085,-0.031] |
|      12 |      -1 | -0.030 [-0.080,+0.020] | -2.614 [-2.860,-2.367] | +1.562 [+1.325,+1.782]    | +0.008 [-0.012,+0.032] | +0.000 [+0.000,+0.000] | -0.007 [-0.060,+0.047] | -0.022 [-0.037,-0.010] |
|      12 |       1 | -0.030 [-0.080,+0.010] | +1.740 [+1.435,+2.054] | -0.649 [-0.938,-0.347]    | +0.004 [-0.020,+0.028] | +0.000 [+0.000,+0.000] | -0.020 [-0.080,+0.040] | +0.017 [+0.005,+0.032] |
|      12 |       2 | -0.070 [-0.140,-0.010] | +3.586 [+2.983,+4.214] | +0.079 [-0.588,+0.738]    | +0.016 [-0.012,+0.044] | -0.002 [-0.006,+0.000] | +0.053 [-0.007,+0.120] | +0.024 [+0.007,+0.044] |
|      12 |       4 | -0.350 [-0.450,-0.260] | -0.081 [-0.967,+0.804] | +10.472 [+9.407,+11.536]  | -0.112 [-0.156,-0.068] | +0.002 [-0.004,+0.010] | -0.227 [-0.320,-0.133] | -0.201 [-0.247,-0.155] |
|      12 |       8 | -0.550 [-0.650,-0.450] | -0.453 [-1.385,+0.437] | +14.248 [+13.103,+15.385] | -0.180 [-0.256,-0.104] | +0.008 [+0.000,+0.018] | +0.260 [+0.160,+0.367] | -0.442 [-0.514,-0.368] |
|      18 |      -8 | -0.420 [-0.520,-0.320] | +4.206 [+3.528,+4.854] | -0.240 [-0.968,+0.442]    | -0.112 [-0.160,-0.064] | -0.002 [-0.006,+0.000] | +0.140 [+0.053,+0.227] | -0.128 [-0.165,-0.094] |
|      18 |      -4 | -0.120 [-0.200,-0.050] | +1.793 [+1.431,+2.126] | +0.256 [-0.156,+0.646]    | -0.040 [-0.072,-0.012] | -0.002 [-0.006,+0.000] | -0.013 [-0.093,+0.067] | -0.009 [-0.024,+0.003] |
|      18 |      -2 | +0.000 [-0.060,+0.060] | +0.543 [+0.368,+0.690] | -0.468 [-0.676,-0.275]    | -0.032 [-0.060,-0.008] | +0.000 [+0.000,+0.000] | -0.007 [-0.073,+0.060] | +0.002 [-0.004,+0.008] |
|      18 |      -1 | +0.020 [-0.030,+0.080] | +0.103 [+0.013,+0.182] | -0.400 [-0.510,-0.300]    | -0.008 [-0.028,+0.008] | +0.000 [+0.000,+0.000] | -0.060 [-0.120,+0.000] | +0.002 [-0.001,+0.006] |
|      18 |       1 | -0.010 [-0.060,+0.040] | +0.129 [+0.037,+0.218] | +0.526 [+0.450,+0.603]    | +0.036 [+0.016,+0.060] | +0.000 [+0.000,+0.000] | -0.027 [-0.080,+0.027] | -0.005 [-0.009,-0.001] |
|      18 |       2 | -0.040 [-0.100,+0.020] | +0.506 [+0.326,+0.689] | +1.150 [+1.042,+1.256]    | +0.020 [+0.000,+0.040] | +0.000 [+0.000,+0.000] | -0.040 [-0.100,+0.013] | -0.010 [-0.019,-0.001] |
|      18 |       4 | +0.010 [-0.060,+0.080] | +1.857 [+1.565,+2.167] | +2.239 [+2.039,+2.440]    | +0.004 [-0.024,+0.032] | +0.000 [+0.000,+0.000] | -0.027 [-0.100,+0.047] | -0.032 [-0.055,-0.010] |
|      18 |       8 | -0.170 [-0.270,-0.070] | +4.022 [+3.635,+4.407] | +6.360 [+5.624,+7.047]    | -0.060 [-0.100,-0.020] | +0.000 [+0.000,+0.000] | +0.147 [+0.067,+0.227] | -0.196 [-0.254,-0.142] |

## Natural-dose steering (alpha = +/-1, +/-2), slope in pp per natural unit, vs 32 random directions (logit readouts)

| model                 |   layer | outcome      | direction   |   slope |    lo |    hi |   rand_abs_mean |   rand_abs_max |   p_emp |
|:----------------------|--------:|:-------------|:------------|--------:|------:|------:|----------------:|---------------:|--------:|
| Llama-3.1-8B-Instruct |       6 | refusal_tok  | auth        |   -0.61 | -1    | -0.26 |            0.51 |           1.38 |    0.36 |
| Llama-3.1-8B-Instruct |       6 | refusal_tok  | len         |   -0.73 | -1.24 | -0.26 |            0.51 |           1.38 |    0.3  |
| Llama-3.1-8B-Instruct |       6 | refusal_tok  | eval        |    0.72 |  0.33 |  1.16 |            0.51 |           1.38 |    0.3  |
| Llama-3.1-8B-Instruct |       6 | refusal_tok  | refusal     |    0.92 |  0.37 |  1.53 |            0.51 |           1.38 |    0.21 |
| Llama-3.1-8B-Instruct |       6 | syco_opinion | auth        |    2.28 |  1.44 |  3.19 |            1    |           2.2  |    0.03 |
| Llama-3.1-8B-Instruct |       6 | syco_opinion | len         |   -0.24 | -0.83 |  0.3  |            1    |           2.2  |    0.94 |
| Llama-3.1-8B-Instruct |       6 | syco_opinion | eval        |    0.47 | -0.04 |  1.02 |            1    |           2.2  |    0.85 |
| Llama-3.1-8B-Instruct |       6 | syco_opinion | refusal     |    0.07 | -0.51 |  0.64 |            1    |           2.2  |    1    |
| Llama-3.1-8B-Instruct |      12 | refusal_tok  | auth        |   -0.8  | -1.23 | -0.4  |            0.83 |           3.42 |    0.42 |
| Llama-3.1-8B-Instruct |      12 | refusal_tok  | len         |   -0.79 | -1.33 | -0.3  |            0.83 |           3.42 |    0.42 |
| Llama-3.1-8B-Instruct |      12 | refusal_tok  | eval        |   -0.53 | -0.81 | -0.28 |            0.83 |           3.42 |    0.58 |
| Llama-3.1-8B-Instruct |      12 | refusal_tok  | refusal     |    6.94 |  5.79 |  8.16 |            0.83 |           3.42 |    0.03 |
| Llama-3.1-8B-Instruct |      12 | syco_opinion | auth        |    0.95 |  0.58 |  1.34 |            0.55 |           1.38 |    0.3  |
| Llama-3.1-8B-Instruct |      12 | syco_opinion | len         |    0.55 |  0.15 |  0.94 |            0.55 |           1.38 |    0.42 |
| Llama-3.1-8B-Instruct |      12 | syco_opinion | eval        |   -0.3  | -0.63 |  0.02 |            0.55 |           1.38 |    0.64 |
| Llama-3.1-8B-Instruct |      12 | syco_opinion | refusal     |   -0.92 | -2.16 |  0.26 |            0.55 |           1.38 |    0.3  |
| Llama-3.1-8B-Instruct |      24 | refusal_tok  | auth        |   -0.71 | -0.99 | -0.47 |            0.34 |           1.3  |    0.21 |
| Llama-3.1-8B-Instruct |      24 | refusal_tok  | len         |    1.72 |  1.26 |  2.2  |            0.34 |           1.3  |    0.03 |
| Llama-3.1-8B-Instruct |      24 | refusal_tok  | eval        |    0.21 | -0.03 |  0.48 |            0.34 |           1.3  |    0.61 |
| Llama-3.1-8B-Instruct |      24 | refusal_tok  | refusal     |    1.79 |  1.32 |  2.29 |            0.34 |           1.3  |    0.03 |
| Llama-3.1-8B-Instruct |      24 | syco_opinion | auth        |   -0.44 | -0.54 | -0.35 |            0.11 |           0.37 |    0.03 |
| Llama-3.1-8B-Instruct |      24 | syco_opinion | len         |   -0.03 | -0.12 |  0.07 |            0.11 |           0.37 |    0.94 |
| Llama-3.1-8B-Instruct |      24 | syco_opinion | eval        |   -0.4  | -0.48 | -0.32 |            0.11 |           0.37 |    0.03 |
| Llama-3.1-8B-Instruct |      24 | syco_opinion | refusal     |   -0.03 | -0.07 |  0.02 |            0.11 |           0.37 |    0.94 |
| Qwen2.5-7B-Instruct   |      10 | refusal_tok  | auth        |    0.84 |  0.23 |  1.47 |            0.97 |           2.85 |    0.45 |
| Qwen2.5-7B-Instruct   |      10 | refusal_tok  | len         |    1.54 |  1.01 |  2.1  |            0.97 |           2.85 |    0.27 |
| Qwen2.5-7B-Instruct   |      10 | refusal_tok  | eval        |   -0.64 | -1.13 | -0.15 |            0.97 |           2.85 |    0.55 |
| Qwen2.5-7B-Instruct   |      10 | refusal_tok  | refusal     |    4.12 |  3.14 |  5.17 |            0.97 |           2.85 |    0.03 |
| Qwen2.5-7B-Instruct   |      10 | syco_opinion | auth        |    1.39 |  0.47 |  2.34 |            0.84 |           2.41 |    0.18 |
| Qwen2.5-7B-Instruct   |      10 | syco_opinion | len         |   -0.51 | -1.08 | -0.03 |            0.84 |           2.41 |    0.67 |
| Qwen2.5-7B-Instruct   |      10 | syco_opinion | eval        |    0.73 |  0.01 |  1.49 |            0.84 |           2.41 |    0.48 |
| Qwen2.5-7B-Instruct   |      10 | syco_opinion | refusal     |    0.81 |  0.27 |  1.46 |            0.84 |           2.41 |    0.48 |
| Qwen2.5-7B-Instruct   |      12 | refusal_tok  | auth        |    0.53 |  0.05 |  1.04 |            1.58 |           4.51 |    0.94 |
| Qwen2.5-7B-Instruct   |      12 | refusal_tok  | len         |    0.45 | -0.03 |  0.97 |            1.58 |           4.51 |    0.94 |
| Qwen2.5-7B-Instruct   |      12 | refusal_tok  | eval        |   -1.46 | -2.03 | -0.91 |            1.58 |           4.51 |    0.45 |
| Qwen2.5-7B-Instruct   |      12 | refusal_tok  | refusal     |    5.02 |  3.9  |  6.19 |            1.58 |           4.51 |    0.03 |
| Qwen2.5-7B-Instruct   |      12 | syco_opinion | auth        |    1.99 |  1.09 |  2.94 |            1.22 |           3.31 |    0.24 |
| Qwen2.5-7B-Instruct   |      12 | syco_opinion | len         |    1.8  |  0.84 |  2.84 |            1.22 |           3.31 |    0.3  |
| Qwen2.5-7B-Instruct   |      12 | syco_opinion | eval        |    0.38 | -0.38 |  1.14 |            1.22 |           3.31 |    0.73 |
| Qwen2.5-7B-Instruct   |      12 | syco_opinion | refusal     |    1.8  |  0.88 |  2.79 |            1.22 |           3.31 |    0.3  |
| Qwen2.5-7B-Instruct   |      18 | refusal_tok  | auth        |    1.18 |  0.78 |  1.66 |            1.23 |           3.55 |    0.48 |
| Qwen2.5-7B-Instruct   |      18 | refusal_tok  | len         |    0.86 |  0.47 |  1.27 |            1.23 |           3.55 |    0.58 |
| Qwen2.5-7B-Instruct   |      18 | refusal_tok  | eval        |   -0.22 | -0.53 |  0.06 |            1.23 |           3.55 |    0.94 |
| Qwen2.5-7B-Instruct   |      18 | refusal_tok  | refusal     |    6.81 |  5.59 |  8.06 |            1.23 |           3.55 |    0.03 |
| Qwen2.5-7B-Instruct   |      18 | syco_opinion | auth        |   -0.31 | -0.66 |  0.02 |            0.5  |           1.83 |    0.67 |
| Qwen2.5-7B-Instruct   |      18 | syco_opinion | len         |    0.45 |  0.07 |  0.84 |            0.5  |           1.83 |    0.45 |
| Qwen2.5-7B-Instruct   |      18 | syco_opinion | eval        |    0.07 | -0.13 |  0.31 |            0.5  |           1.83 |    0.97 |
| Qwen2.5-7B-Instruct   |      18 | syco_opinion | refusal     |   -2.39 | -4.07 | -0.7  |            0.5  |           1.83 |    0.03 |

| model   |   auc_refusal_tok_vs_scored_refusal |   base_p_I |   base_refusal_rate |   base_p_match |
|:--------|------------------------------------:|-----------:|--------------------:|---------------:|
| llama   |                               0.998 |      0.588 |               0.576 |          0.891 |
| qwen    |                               0.992 |      0.536 |               0.5   |          0.96  |

## Scorer agreement: API judge vs rule-based scorer on behaviour outputs

| model   | task      |    n |   judge_rate |   rule_rate |   agree |   judge_yes_rule_no |   judge_no_rule_yes |
|:--------|:----------|-----:|-------------:|------------:|--------:|--------------------:|--------------------:|
| llama   | accuracy  | 1637 |        0.737 |       0.716 |   0.952 |               0.035 |               0.013 |
| llama   | refusal   | 2539 |        0.548 |       0.547 |   0.994 |               0.004 |               0.002 |
| llama   | syco_fact | 1610 |        0.129 |       0.13  |   0.929 |               0.035 |               0.036 |
| qwen    | accuracy  | 1637 |        0.671 |       0.668 |   0.952 |               0.025 |               0.023 |
| qwen    | refusal   | 2539 |        0.509 |       0.461 |   0.936 |               0.056 |               0.008 |
| qwen    | syco_fact | 1610 |        0.312 |       0.404 |   0.811 |               0.048 |               0.141 |
| luna    | accuracy  | 1619 |        0.936 |       0.912 |   0.967 |               0.029 |               0.004 |
| luna    | refusal   | 2536 |        0.532 |       0.504 |   0.951 |               0.038 |               0.011 |
| luna    | syco_fact | 1595 |        0.041 |       0.062 |   0.958 |               0.011 |               0.031 |
| sonnet  | accuracy  | 1636 |        0.96  |       0.953 |   0.975 |               0.016 |               0.009 |
| sonnet  | refusal   | 2388 |        0.446 |       0.458 |   0.959 |               0.015 |               0.027 |
| sonnet  | syco_fact | 1607 |        0.027 |       0.033 |   0.972 |               0.011 |               0.017 |
| gemini  | accuracy  | 1637 |        0.968 |       0.964 |   0.98  |               0.012 |               0.008 |
| gemini  | refusal   | 2369 |        0.44  |       0.428 |   0.965 |               0.024 |               0.011 |
| gemini  | syco_fact | 1610 |        0.029 |       0.037 |   0.965 |               0.014 |               0.022 |

## Primary style contrast under both scorers

| model   | outcome   | scorer   |   rate_H_s |   rate_L_s |    mean |      lo |      hi |      p |   n |      dz |
|:--------|:----------|:---------|-----------:|-----------:|--------:|--------:|--------:|-------:|----:|--------:|
| llama   | refusal   | judge    |     0.5449 |     0.532  |  0.0054 | -0.015  |  0.0258 | 0.6857 | 233 |  0.0336 |
| llama   | syco_fact | judge    |     0.1327 |     0.1073 | -0.0154 | -0.0428 |  0.012  | 0.3425 | 146 | -0.0911 |
| llama   | accuracy  | judge    |     0.7205 |     0.7172 | -0.0151 | -0.0537 |  0.0235 | 0.5025 | 149 | -0.0624 |
| llama   | refusal   | rule     |     0.5383 |     0.5297 |  0.0075 | -0.0118 |  0.0268 | 0.5326 | 233 |  0.0486 |
| llama   | syco_fact | rule     |     0.1293 |     0.083  | -0.0394 | -0.0736 | -0.0068 | 0.0331 | 146 | -0.1884 |
| llama   | accuracy  | rule     |     0.7104 |     0.7037 | -0.0185 | -0.0604 |  0.0219 | 0.4358 | 149 | -0.0705 |
| qwen    | refusal   | judge    |     0.5011 |     0.4863 |  0      | -0.0268 |  0.0268 | 1      | 233 |  0      |
| qwen    | syco_fact | judge    |     0.3435 |     0.2941 | -0.0308 | -0.0685 |  0.0069 | 0.1409 | 146 | -0.1293 |
| qwen    | accuracy  | judge    |     0.6667 |     0.6667 | -0.0151 | -0.0369 |  0.005  | 0.2298 | 149 | -0.1128 |
| qwen    | refusal   | rule     |     0.4464 |     0.4361 |  0      | -0.0268 |  0.0247 | 1      | 233 |  0      |
| qwen    | syco_fact | rule     |     0.449  |     0.3945 | -0.0428 | -0.0719 | -0.0137 | 0.0075 | 146 | -0.2354 |
| qwen    | accuracy  | rule     |     0.6566 |     0.6465 | -0.0134 | -0.0419 |  0.0151 | 0.43   | 149 | -0.0751 |
| luna    | refusal   | judge    |     0.5263 |     0.5068 | -0.0032 | -0.0216 |  0.014  | 0.826  | 232 | -0.023  |
| luna    | syco_fact | judge    |     0.0411 |     0.0385 | -0.0017 | -0.0087 |  0.0052 | 1      | 144 | -0.0372 |
| luna    | accuracy  | judge    |     0.9317 |     0.9386 |  0.0017 | -0.0224 |  0.0259 | 1      | 145 |  0.0118 |
| luna    | refusal   | rule     |     0.5044 |     0.4726 | -0.0226 | -0.0431 | -0.0043 | 0.0287 | 232 | -0.1509 |
| luna    | syco_fact | rule     |     0.0685 |     0.0524 | -0.0069 | -0.0278 |  0.0122 | 0.6195 | 144 | -0.0571 |
| luna    | accuracy  | rule     |     0.9078 |     0.9113 |  0.0052 | -0.019  |  0.0293 | 0.796  | 145 |  0.0335 |
| sonnet  | refusal   | judge    |     0.4385 |     0.4282 | -0.0117 | -0.0304 |  0.0047 | 0.2651 | 214 | -0.0869 |
| sonnet  | syco_fact | judge    |     0.0307 |     0.0242 | -0.0121 | -0.0293 |  0.0017 | 0.2445 | 145 | -0.1217 |
| sonnet  | accuracy  | judge    |     0.9663 |     0.9596 | -0.0017 | -0.0201 |  0.0117 | 1      | 149 | -0.017  |
| sonnet  | refusal   | rule     |     0.4594 |     0.4426 | -0.0117 | -0.0339 |  0.0105 | 0.3589 | 214 | -0.0705 |
| sonnet  | syco_fact | rule     |     0.0307 |     0.0346 | -0.0052 | -0.0172 |  0.0052 | 0.5614 | 145 | -0.0751 |
| sonnet  | accuracy  | rule     |     0.963  |     0.9461 | -0.005  | -0.0252 |  0.0117 | 0.7482 | 149 | -0.044  |
| gemini  | refusal   | judge    |     0.435  |     0.3966 | -0.0252 | -0.0469 | -0.006  | 0.0238 | 208 | -0.1657 |
| gemini  | syco_fact | judge    |     0.0272 |     0.0381 |  0.0017 | -0.0086 |  0.012  | 1      | 146 |  0.0275 |
| gemini  | accuracy  | judge    |     0.9731 |     0.9562 | -0.0084 | -0.0285 |  0.0067 | 0.5108 | 149 | -0.076  |
| gemini  | refusal   | rule     |     0.4137 |     0.3941 | -0.0108 | -0.0349 |  0.012  | 0.4191 | 208 | -0.064  |
| gemini  | syco_fact | rule     |     0.0442 |     0.0415 | -0.0034 | -0.0137 |  0.0068 | 0.7597 | 146 | -0.0522 |
| gemini  | accuracy  | rule     |     0.9596 |     0.963  |  0.0084 | -0.0117 |  0.0302 | 0.5431 | 149 |  0.0655 |

## Calibrated local judge vs API judge on held-out Qwen steering outputs

| task      | subset         |    n |   api_rate |   raw_rate |   cal_rate |   agree_raw |   agree_cal |
|:----------|:---------------|-----:|-----------:|-----------:|-----------:|------------:|------------:|
| refusal   | all held-out   | 2438 |      0.49  |      0.354 |      0.539 |       0.835 |       0.866 |
| refusal   | unsteered      |  125 |      0.552 |      0.496 |      0.528 |       0.944 |       0.976 |
| refusal   | |alpha|<=2     |  345 |      0.548 |      0.501 |      0.533 |       0.954 |       0.98  |
| refusal   | |alpha|=4      |  988 |      0.519 |      0.396 |      0.511 |       0.874 |       0.951 |
| refusal   | |alpha|=8      |  980 |      0.432 |      0.242 |      0.569 |       0.739 |       0.726 |
| refusal   | authorship dir |  537 |      0.492 |      0.417 |      0.52  |       0.907 |       0.931 |
| refusal   | random dirs    | 1105 |      0.48  |      0.328 |      0.55  |       0.819 |       0.843 |
| accuracy  | all held-out   | 1156 |      0.593 |      0.655 |      0.579 |       0.922 |       0.96  |
| accuracy  | unsteered      |   50 |      0.76  |      0.82  |      0.74  |       0.94  |       0.94  |
| accuracy  | |alpha|<=2     |  160 |      0.769 |      0.838 |      0.744 |       0.931 |       0.938 |
| accuracy  | |alpha|=4      |  511 |      0.748 |      0.789 |      0.746 |       0.943 |       0.971 |
| accuracy  | |alpha|=8      |  435 |      0.326 |      0.411 |      0.303 |       0.892 |       0.959 |
| accuracy  | authorship dir |  260 |      0.669 |      0.754 |      0.654 |       0.9   |       0.931 |
| accuracy  | random dirs    |  572 |      0.577 |      0.626 |      0.565 |       0.934 |       0.97  |
| syco_fact | all held-out   | 1450 |      0.418 |      0.19  |      0.467 |       0.761 |       0.859 |
| syco_fact | unsteered      |   75 |      0.333 |      0.173 |      0.373 |       0.84  |       0.88  |
| syco_fact | |alpha|<=2     |  204 |      0.26  |      0.152 |      0.353 |       0.892 |       0.887 |
| syco_fact | |alpha|=4      |  573 |      0.4   |      0.192 |      0.461 |       0.771 |       0.859 |
| syco_fact | |alpha|=8      |  598 |      0.5   |      0.204 |      0.523 |       0.697 |       0.846 |
| syco_fact | authorship dir |  330 |      0.291 |      0.139 |      0.373 |       0.848 |       0.888 |
| syco_fact | random dirs    |  651 |      0.484 |      0.223 |      0.522 |       0.727 |       0.851 |

## Output register under steering: share of sentence starts in lower case (mean; random = max over 8 directions)

| model   |   layer | kind   |    -8 |    -4 |      -2 |      -1 |       1 |       2 |     4 |     8 |
|:--------|--------:|:-------|------:|------:|--------:|--------:|--------:|--------:|------:|------:|
| llama   |       6 | auth   | 0.899 | 0.457 |   0.004 |   0.003 |   0.005 |   0.005 | 0.007 | 0.004 |
| llama   |       6 | random | 0.028 | 0.008 | nan     | nan     | nan     | nan     | 0.008 | 0.034 |
| llama   |      12 | auth   | 0.979 | 0.006 |   0.004 |   0.004 |   0.005 |   0.006 | 0.007 | 0.008 |
| llama   |      12 | random | 0.018 | 0.009 | nan     | nan     | nan     | nan     | 0.011 | 0.029 |
| llama   |      24 | auth   | 0.001 | 0.003 |   0.003 |   0.003 |   0.006 |   0.007 | 0.004 | 0.005 |
| llama   |      24 | random | 0.007 | 0.005 | nan     | nan     | nan     | nan     | 0.006 | 0.008 |
| qwen    |      10 | auth   | 0.194 | 0.003 |   0.003 |   0.004 |   0.003 |   0.005 | 0.008 | 0.01  |
| qwen    |      10 | random | 0.061 | 0.006 | nan     | nan     | nan     | nan     | 0.005 | 0.018 |
| qwen    |      12 | auth   | 0.444 | 0.007 |   0.006 |   0.003 |   0.005 |   0.006 | 0.007 | 0.003 |
| qwen    |      12 | random | 0.038 | 0.016 | nan     | nan     | nan     | nan     | 0.007 | 0.014 |
| qwen    |      18 | auth   | 0.011 | 0.004 |   0.003 |   0.004 |   0.003 |   0.003 | 0.003 | 0.004 |
| qwen    |      18 | random | 0.017 | 0.006 | nan     | nan     | nan     | nan     | 0.005 | 0.008 |