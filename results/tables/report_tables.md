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
| Gemini-3.8-flash      | -0.4 [-1.4, +0.5]      | -0.7 [-2.9, +1.3] | -2.4 [-4.9, +0.1] | +0.5 [+0.0, +1.4] | +0.4 [-2.9, +3.6] |
| Llama-3.1-8B-Instruct | +0.9 [-2.9, +4.6]      | -1.5 [-5.5, +2.3] | +0.5 [-1.5, +2.6] | -1.5 [-4.5, +1.0] | +0.2 [-0.9, +1.4] |
| Qwen2.5-7B-Instruct   | +5.0 [+1.2, +8.9]      | -1.3 [-4.4, +1.7] | -0.6 [-3.5, +2.1] | -3.1 [-6.7, +0.3] | +2.4 [+0.8, +4.2] |

## Length effect (long minus short), pp [95% CI]

| model                 | acc_under_suggestion   | accuracy          | refusal           | syco_fact         | syco_opinion      |
|:----------------------|:-----------------------|:------------------|:------------------|:------------------|:------------------|
| Claude-Sonnet-5.5     | -1.0 [-2.4, +0.2]      | -0.8 [-1.8, -0.2] | -0.2 [-1.9, +1.3] | +0.2 [-1.2, +1.4] | -0.9 [-3.5, +1.6] |
| GPT-5.6-luna          | +0.0 [-1.0, +1.2]      | -0.5 [-1.9, +0.9] | -1.0 [-2.4, +0.3] | -0.5 [-2.3, +0.7] | -0.5 [-2.4, +1.4] |
| Gemini-3.8-flash      | +0.4 [-1.1, +1.8]      | -1.1 [-2.5, +0.0] | +1.4 [-0.7, +3.7] | -0.5 [-1.4, +0.0] | +1.1 [-2.5, +4.6] |
| Llama-3.1-8B-Instruct | -1.2 [-3.8, +1.5]      | +1.2 [-1.0, +3.5] | -1.4 [-3.0, +0.1] | +1.2 [-0.5, +2.9] | -0.3 [-0.8, +0.2] |
| Qwen2.5-7B-Instruct   | +1.9 [-1.2, +5.0]      | +0.0 [-2.5, +2.5] | +2.1 [+0.2, +4.1] | -1.0 [-3.9, +2.1] | +0.7 [-0.2, +1.7] |

## Style effect within the length-matched short cells, pp [95% CI]

| model                 | acc_under_suggestion   | accuracy          | refusal           | syco_fact         | syco_opinion      |
|:----------------------|:-----------------------|:------------------|:------------------|:------------------|:------------------|
| Claude-Sonnet-5.5     | -0.7 [-2.8, +1.4]      | -0.7 [-2.0, +0.0] | -1.4 [-3.5, +0.7] | -0.3 [-2.8, +1.7] | +0.0 [-3.9, +3.9] |
| GPT-5.6-luna          | +0.3 [-1.4, +2.4]      | +0.0 [-3.1, +3.1] | -1.3 [-3.7, +1.1] | +0.7 [+0.0, +1.7] | -2.1 [-5.2, +1.0] |
| Gemini-3.8-flash      | -0.4 [-1.1, +0.0]      | -0.7 [-3.3, +1.1] | -2.2 [-5.8, +1.2] | +1.1 [+0.0, +2.9] | +0.7 [-3.6, +5.0] |
| Llama-3.1-8B-Instruct | +0.0 [-4.1, +4.1]      | -0.7 [-5.7, +4.4] | -0.2 [-2.6, +2.1] | -1.7 [-4.5, +1.0] | -0.4 [-1.7, +0.9] |
| Qwen2.5-7B-Instruct   | +4.1 [-0.7, +8.9]      | -1.0 [-5.4, +3.0] | +0.4 [-3.2, +3.9] | -4.8 [-9.6, +0.0] | +1.9 [+0.2, +3.8] |

## Style effect: p-values (sign-flip permutation; Holm over model x 4 primary outcomes)

| model                 | outcome              |   n |    mean |      p |   p_holm |      dz |
|:----------------------|:---------------------|----:|--------:|-------:|---------:|--------:|
| Llama-3.1-8B-Instruct | refusal              | 233 |  0.0054 | 0.6848 |    1     |  0.0336 |
| Llama-3.1-8B-Instruct | syco_fact            | 146 | -0.0154 | 0.3336 |    1     | -0.0911 |
| Llama-3.1-8B-Instruct | syco_opinion         | 150 |  0.002  | 0.7382 |    1     |  0.0272 |
| Llama-3.1-8B-Instruct | accuracy             | 149 | -0.0151 | 0.4957 |    1     | -0.0624 |
| Llama-3.1-8B-Instruct | acc_under_suggestion | 146 |  0.0086 | 0.7227 |  nan     |  0.0372 |
| Qwen2.5-7B-Instruct   | refusal              | 233 | -0.0064 | 0.7172 |    1     | -0.0289 |
| Qwen2.5-7B-Instruct   | syco_fact            | 146 | -0.0308 | 0.1175 |    1     | -0.1417 |
| Qwen2.5-7B-Instruct   | syco_opinion         | 150 |  0.0244 | 0.0034 |    0.068 |  0.2324 |
| Qwen2.5-7B-Instruct   | accuracy             | 149 | -0.0134 | 0.4395 |    1     | -0.0732 |
| Qwen2.5-7B-Instruct   | acc_under_suggestion | 146 |  0.0497 | 0.0156 |  nan     |  0.2088 |
| GPT-5.6-luna          | refusal              | 232 | -0.0032 | 0.815  |    1     | -0.023  |
| GPT-5.6-luna          | syco_fact            | 144 | -0.0017 | 1      |    1     | -0.0372 |
| GPT-5.6-luna          | syco_opinion         | 145 | -0.0121 | 0.5161 |    1     | -0.0645 |
| GPT-5.6-luna          | accuracy             | 145 |  0.0017 | 1      |    1     |  0.0118 |
| GPT-5.6-luna          | acc_under_suggestion | 144 |  0.0104 | 0.3824 |  nan     |  0.0914 |
| Claude-Sonnet-5.5     | refusal              | 214 | -0.0117 | 0.2588 |    1     | -0.0869 |
| Claude-Sonnet-5.5     | syco_fact            | 145 | -0.0121 | 0.2512 |    1     | -0.1217 |
| Claude-Sonnet-5.5     | syco_opinion         | 141 |  0.0053 | 0.8066 |    1     |  0.0308 |
| Claude-Sonnet-5.5     | accuracy             | 149 | -0.0017 | 1      |    1     | -0.017  |
| Claude-Sonnet-5.5     | acc_under_suggestion | 145 |  0.0034 | 0.8263 |  nan     |  0.039  |
| Gemini-3.8-flash      | refusal              | 208 | -0.024  | 0.0748 |    1     | -0.1307 |
| Gemini-3.8-flash      | syco_fact            | 138 |  0.0054 | 0.5042 |    1     |  0.1145 |
| Gemini-3.8-flash      | syco_opinion         |  70 |  0.0036 | 1      |    1     |  0.0259 |
| Gemini-3.8-flash      | accuracy             | 138 | -0.0072 | 0.6459 |    1     | -0.0583 |
| Gemini-3.8-flash      | acc_under_suggestion | 138 | -0.0036 | 0.7402 |  nan     | -0.0601 |

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
| Qwen2.5-7B-Instruct   | refusal                |      413 | 0.324 | 0.358 | 0.337 | 0.351 |  0.424 |      0.38  |         0.384 |
| Qwen2.5-7B-Instruct   | refusal[jbb_harmful]   |      145 | 0.579 | 0.676 | 0.628 | 0.641 |  0.77  |    nan     |       nan     |
| Qwen2.5-7B-Instruct   | refusal[jbb_benign]    |       93 | 0.032 | 0.065 | 0.086 | 0.086 |  0.04  |    nan     |       nan     |
| Qwen2.5-7B-Instruct   | refusal[xstest_safe]   |       92 | 0     | 0     | 0     | 0     |  0     |    nan     |       nan     |
| Qwen2.5-7B-Instruct   | refusal[xstest_unsafe] |       83 | 0.566 | 0.53  | 0.482 | 0.53  |  0.54  |    nan     |       nan     |
| Qwen2.5-7B-Instruct   | syco_fact              |      275 | 0.211 | 0.178 | 0.164 | 0.167 |  0.207 |      0.193 |         0.147 |
| Qwen2.5-7B-Instruct   | syco_opinion           |      291 | 0.924 | 0.926 | 0.942 | 0.955 |  0.96  |      0.968 |         0.968 |
| Qwen2.5-7B-Instruct   | accuracy               |      288 | 0.778 | 0.781 | 0.767 | 0.764 |  0.807 |      0.833 |         0.8   |
| Qwen2.5-7B-Instruct   | acc_under_suggestion   |      275 | 0.698 | 0.713 | 0.735 | 0.767 |  0.733 |      0.727 |         0.76  |
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
| Gemini-3.8-flash      | refusal                |      363 | 0.267 | 0.281 | 0.253 | 0.256 |  0.328 |      0.345 |         0.37  |
| Gemini-3.8-flash      | refusal[jbb_harmful]   |      115 | 0.513 | 0.548 | 0.496 | 0.478 |  0.547 |    nan     |       nan     |
| Gemini-3.8-flash      | refusal[jbb_benign]    |       91 | 0.033 | 0.044 | 0.033 | 0.044 |  0.082 |    nan     |       nan     |
| Gemini-3.8-flash      | refusal[xstest_safe]   |       92 | 0     | 0     | 0     | 0     |  0     |    nan     |       nan     |
| Gemini-3.8-flash      | refusal[xstest_unsafe] |       65 | 0.538 | 0.538 | 0.492 | 0.523 |  0.545 |    nan     |       nan     |
| Gemini-3.8-flash      | syco_fact              |      255 | 0     | 0     | 0.008 | 0     |  0     |      0.007 |         0     |
| Gemini-3.8-flash      | syco_opinion           |      109 | 0.651 | 0.651 | 0.661 | 0.661 |  0.653 |      0.642 |         0.656 |
| Gemini-3.8-flash      | accuracy               |      267 | 0.993 | 0.985 | 0.989 | 0.978 |  0.986 |      0.993 |         0.98  |
| Gemini-3.8-flash      | acc_under_suggestion   |      255 | 0.988 | 0.988 | 0.984 | 0.988 |  0.986 |      0.993 |         0.986 |

## Pooled over models

| outcome              | contrast       |   n_models |   n | v                 |      p |
|:---------------------|:---------------|-----------:|----:|:------------------|-------:|
| refusal              | style          |          5 | 233 | -0.6 [-1.9, +0.6] | 0.3311 |
| refusal              | length         |          5 | 233 | +0.1 [-0.7, +0.9] | 0.8179 |
| refusal              | style_at_short |          5 | 233 | -0.9 [-2.5, +0.7] | 0.3011 |
| syco_fact            | style          |          5 | 146 | -1.1 [-2.1, -0.1] | 0.0313 |
| syco_fact            | length         |          5 | 146 | -0.2 [-1.0, +0.6] | 0.6755 |
| syco_fact            | style_at_short |          5 | 146 | -0.9 [-2.3, +0.6] | 0.2154 |
| syco_opinion         | style          |          5 | 150 | +0.5 [-0.8, +1.9] | 0.4452 |
| syco_opinion         | length         |          5 | 150 | -0.2 [-1.1, +0.7] | 0.6827 |
| syco_opinion         | style_at_short |          5 | 150 | -0.1 [-1.6, +1.4] | 0.9199 |
| accuracy             | style          |          5 | 149 | -0.8 [-2.3, +0.6] | 0.3324 |
| accuracy             | length         |          5 | 149 | -0.2 [-1.2, +0.8] | 0.723  |
| accuracy             | style_at_short |          5 | 149 | -0.7 [-2.6, +1.0] | 0.4645 |
| acc_under_suggestion | style          |          5 | 146 | +1.3 [+0.2, +2.6] | 0.035  |
| acc_under_suggestion | length         |          5 | 146 | +0.0 [-0.9, +1.0] | 1      |
| acc_under_suggestion | style_at_short |          5 | 146 | +0.5 [-1.0, +2.1] | 0.496  |

## Explicit label arm (identical text): label_ai - label_human, pp

| model                 | outcome              |   n | v                  |      p |   p_holm |
|:----------------------|:---------------------|----:|:-------------------|-------:|---------:|
| Llama-3.1-8B-Instruct | refusal              | 250 | +3.2 [+0.8, +5.6]  | 0.0188 |    0.376 |
| Llama-3.1-8B-Instruct | syco_fact            | 150 | -2.0 [-6.0, +2.0]  | 0.5059 |    1     |
| Llama-3.1-8B-Instruct | syco_opinion         | 150 | +0.5 [-0.1, +1.2]  | 0.1253 |    1     |
| Llama-3.1-8B-Instruct | accuracy             | 150 | +0.7 [-1.3, +3.3]  | 1      |    1     |
| Llama-3.1-8B-Instruct | acc_under_suggestion | 150 | +0.0 [-4.7, +4.7]  | 1      |  nan     |
| Qwen2.5-7B-Instruct   | refusal              | 250 | -0.4 [-4.0, +3.2]  | 1      |    1     |
| Qwen2.5-7B-Instruct   | syco_fact            | 150 | +4.7 [+0.7, +9.3]  | 0.067  |    1     |
| Qwen2.5-7B-Instruct   | syco_opinion         | 150 | +0.1 [-0.1, +0.3]  | 0.5452 |    1     |
| Qwen2.5-7B-Instruct   | accuracy             | 150 | +3.3 [-1.3, +8.0]  | 0.2652 |    1     |
| Qwen2.5-7B-Instruct   | acc_under_suggestion | 150 | -3.3 [-8.7, +1.3]  | 0.3053 |  nan     |
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
| Gemini-3.8-flash      | refusal              | 220 | -1.8 [-4.5, +0.5]  | 0.2906 |    1     |
| Gemini-3.8-flash      | syco_fact            | 137 | +0.7 [+0.0, +2.2]  | 1      |    1     |
| Gemini-3.8-flash      | syco_opinion         |  63 | -3.2 [-12.7, +4.8] | 0.7178 |    1     |
| Gemini-3.8-flash      | accuracy             | 139 | +1.4 [+0.0, +3.6]  | 0.5035 |    1     |
| Gemini-3.8-flash      | acc_under_suggestion | 137 | +0.7 [+0.0, +2.2]  | 1      |  nan     |

## Naive (uncontrolled LLM rewrite) vs controlled contrasts, pp

| model                 | outcome      | controlled natural: L_l - H_s   | controlled style (2x2)   | naive: L_free - H_s   |
|:----------------------|:-------------|:--------------------------------|:-------------------------|:----------------------|
| Claude-Sonnet-5.5     | accuracy     | -1.0 [-2.7, +0.0]               | -0.2 [-2.0, +1.2]        | -0.3 [-1.0, +0.0]     |
| Claude-Sonnet-5.5     | refusal      | -1.3 [-4.1, +1.3]               | -1.0 [-3.4, +1.0]        | -5.9 [-9.5, -2.6]     |
| Claude-Sonnet-5.5     | syco_fact    | -1.0 [-3.5, +1.0]               | -1.2 [-3.0, +0.2]        | -0.7 [-3.5, +1.4]     |
| Claude-Sonnet-5.5     | syco_opinion | -0.7 [-4.3, +2.5]               | +0.5 [-2.2, +3.4]        | +7.2 [+2.5, +12.3]    |
| GPT-5.6-luna          | accuracy     | -0.3 [-3.1, +2.8]               | +0.2 [-2.1, +2.6]        | +0.0 [-3.1, +3.1]     |
| GPT-5.6-luna          | refusal      | -1.0 [-3.6, +1.7]               | -0.4 [-2.5, +1.6]        | -8.2 [-12.0, -4.8]    |
| GPT-5.6-luna          | syco_fact    | -0.7 [-2.4, +0.7]               | +0.0 [-0.9, +1.0]        | -0.7 [-2.4, +0.7]     |
| GPT-5.6-luna          | syco_opinion | -1.7 [-5.2, +1.4]               | -1.4 [-4.3, +1.6]        | -6.6 [-11.0, -2.1]    |
| Llama-3.1-8B-Instruct | accuracy     | -2.3 [-7.0, +2.3]               | -1.8 [-6.0, +2.2]        | +3.7 [-1.0, +8.7]     |
| Llama-3.1-8B-Instruct | refusal      | -0.7 [-3.1, +1.7]               | +0.4 [-2.3, +2.8]        | -10.3 [-14.7, -6.2]   |
| Llama-3.1-8B-Instruct | syco_fact    | -1.0 [-4.8, +2.4]               | -4.0 [-7.4, -0.7]        | +0.0 [-4.1, +3.8]     |
| Llama-3.1-8B-Instruct | syco_opinion | -0.0 [-1.2, +1.3]               | +0.3 [-0.8, +1.6]        | -4.7 [-6.5, -3.0]     |

| model                 | outcome      |   n |    H_s |   L_free |      p |
|:----------------------|:-------------|----:|-------:|---------:|-------:|
| Llama-3.1-8B-Instruct | refusal      | 208 | 0.4504 |   0.3569 | 0.0001 |
| Llama-3.1-8B-Instruct | syco_fact    | 145 | 0.1204 |   0.1241 | 1      |
| Llama-3.1-8B-Instruct | syco_opinion | 150 | 0.8869 |   0.8351 | 0.0001 |
| Llama-3.1-8B-Instruct | accuracy     | 149 | 0.7153 |   0.7604 | 0.1821 |
| GPT-5.6-luna          | refusal      | 208 | 0.4261 |   0.3608 | 0.0001 |
| GPT-5.6-luna          | syco_fact    | 143 | 0.0263 |   0.0226 | 0.7491 |
| GPT-5.6-luna          | syco_opinion | 145 | 0.8759 |   0.812  | 0.009  |
| GPT-5.6-luna          | accuracy     | 145 | 0.9462 |   0.9534 | 1      |
| Claude-Sonnet-5.5     | refusal      | 194 | 0.3455 |   0.303  | 0.001  |
| Claude-Sonnet-5.5     | syco_fact    | 144 | 0.0294 |   0.0184 | 1      |
| Claude-Sonnet-5.5     | syco_opinion | 138 | 0.6311 |   0.6844 | 0.006  |
| Claude-Sonnet-5.5     | accuracy     | 149 | 0.9686 |   0.9652 | 1      |

## Response form on trivia items

| model                 | outcome          |     H_s |     H_l |     L_s |     L_l |   style_mean |   style_lo |   style_hi |   style_p |   length_mean |   length_p |
|:----------------------|:-----------------|--------:|--------:|--------:|--------:|-------------:|-----------:|-----------:|----------:|--------------:|-----------:|
| Llama-3.1-8B-Instruct | resp_words       |  25.267 |  30.069 |  22.184 |  21.993 |       -5.488 |     -7.534 |     -3.569 |     0     |         2.391 |      0     |
| Llama-3.1-8B-Instruct | resp_markdown    |   0.069 |   0.073 |   0.038 |   0.049 |       -0.029 |     -0.057 |     -0.005 |     0.041 |         0.008 |      0.431 |
| Llama-3.1-8B-Instruct | resp_lower_start |   0.007 |   0.007 |   0     |   0     |       -0.007 |     -0.02  |      0     |     1     |         0     |      1     |
| Qwen2.5-7B-Instruct   | resp_words       |  56.181 |  56.653 |  54.156 |  55.247 |       -1.616 |     -3.221 |      0.054 |     0.051 |         0.847 |      0.115 |
| Qwen2.5-7B-Instruct   | resp_markdown    |   0.066 |   0.083 |   0.069 |   0.049 |       -0.012 |     -0.042 |      0.017 |     0.512 |        -0.002 |      1     |
| Qwen2.5-7B-Instruct   | resp_lower_start |   0.007 |   0.007 |   0     |   0     |       -0.007 |     -0.02  |      0     |     1     |         0     |      1     |
| GPT-5.6-luna          | resp_words       |  18.904 |  24.929 |  14.286 |  15.432 |       -6.933 |     -8.307 |     -5.622 |     0     |         3.571 |      0     |
| GPT-5.6-luna          | resp_markdown    |   0.707 |   0.839 |   0.543 |   0.575 |       -0.214 |     -0.267 |     -0.162 |     0     |         0.083 |      0     |
| GPT-5.6-luna          | resp_lower_start |   0     |   0     |   0     |   0     |        0     |      0     |      0     |     1     |         0     |      1     |
| Claude-Sonnet-5.5     | resp_words       | 107.084 | 115.132 | 101.582 | 100.355 |       -9.872 |    -13.876 |     -5.983 |     0     |         2.839 |      0.075 |
| Claude-Sonnet-5.5     | resp_markdown    |   0.913 |   0.941 |   0.899 |   0.906 |       -0.027 |     -0.052 |     -0.005 |     0.037 |         0.017 |      0.17  |
| Claude-Sonnet-5.5     | resp_lower_start |   0     |   0     |   0     |   0     |        0     |      0     |      0     |     1     |         0     |      1     |
| Gemini-3.8-flash      | resp_words       |  56.142 |  67.554 |  45.052 |  45.461 |      -15.377 |    -19.681 |    -11.009 |     0     |         6.029 |      0     |
| Gemini-3.8-flash      | resp_markdown    |   1     |   1     |   1     |   1     |        0     |      0     |      0     |     1     |         0     |      1     |
| Gemini-3.8-flash      | resp_lower_start |   0.015 |   0.011 |   0.015 |   0.015 |        0.002 |      0     |      0.005 |     1     |        -0.002 |      1     |

## Refusal sensitivity (empty responses counted as refusal) and filter-like responses

| model   | contrast                  |    mean |       lo |       hi |        p |   n |       dz |
|:--------|:--------------------------|--------:|---------:|---------:|---------:|----:|---------:|
| llama   | style                     |  0.0054 |  -0.015  |   0.0258 |   0.6811 | 233 |   0.0336 |
| llama   | length                    | -0.0139 |  -0.029  |   0      |   0.0949 | 233 |  -0.1199 |
| llama   | n_filter_like_responses_H |  0      | nan      | nan      | nan      | nan | nan      |
| llama   | n_filter_like_responses_L |  0      | nan      | nan      | nan      | nan | nan      |
| qwen    | style                     | -0.0064 |  -0.0365 |   0.0215 |   0.7181 | 233 |  -0.0289 |
| qwen    | length                    |  0.0215 |   0.0021 |   0.0408 |   0.0471 | 233 |   0.1408 |
| qwen    | n_filter_like_responses_H |  4      | nan      | nan      | nan      | nan | nan      |
| qwen    | n_filter_like_responses_L |  5      | nan      | nan      | nan      | nan | nan      |
| luna    | style                     | -0.0043 |  -0.0225 |   0.0139 |   0.7319 | 233 |  -0.0304 |
| luna    | length                    | -0.0086 |  -0.0225 |   0.0043 |   0.2837 | 233 |  -0.081  |
| luna    | n_filter_like_responses_H | 60      | nan      | nan      | nan      | nan | nan      |
| luna    | n_filter_like_responses_L | 28      | nan      | nan      | nan      | nan | nan      |
| sonnet  | style                     | -0.0086 |  -0.0247 |   0.0064 |   0.3414 | 233 |  -0.0727 |
| sonnet  | length                    |  0      |  -0.0161 |   0.015  |   1      | 233 |   0      |
| sonnet  | n_filter_like_responses_H | 50      | nan      | nan      | nan      | nan | nan      |
| sonnet  | n_filter_like_responses_L | 40      | nan      | nan      | nan      | nan | nan      |
| gemini  | style                     | -0.015  |  -0.0408 |   0.0097 |   0.2759 | 233 |  -0.0765 |
| gemini  | length                    |  0.0107 |  -0.0075 |   0.03   |   0.3234 | 233 |   0.0733 |
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