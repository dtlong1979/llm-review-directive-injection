# Peer Review: TimeWarn: Irregular-Interval Attention for Early Sepsis Prediction from Electronic Health Records

## Summary
The paper proposes TimeWarn, an extension of the RETAIN two-level attention architecture that incorporates a learned exponential time-decay factor to modulate visit- and variable-level attention weights based on elapsed time since last measurement. The model is evaluated on MIMIC-IV and eICU for six-hour-ahead sepsis prediction against qSOFA, logistic regression, XGBoost, GRU-D, and RETAIN, showing modest but consistent AUROC/AUPRC improvements, along with an ablation and a qualitative attention analysis.

## Strengths
- Addresses a clinically important and well-motivated problem (irregular sampling in EHR time series for sepsis early warning).
- Combines two established ideas (RETAIN's interpretable attention and GRU-D-style time decay) in a reasonably natural way.
- Includes an ablation isolating the contribution of the decay mechanism at both attention levels, and a lead-time analysis (6h vs 12h), which strengthens the empirical narrative.
- Reports mean ± standard deviation over five seeds, and appropriately discusses limitations regarding retrospective evaluation, label noise from Sepsis-3 definitions, and lack of clinical workflow validation.

## Weaknesses
1. **Soundness/statistical rigor**: No significance testing (e.g., paired t-tests or confidence intervals) is reported despite having 5 seeds; the AUROC gains (0.013–0.023) are numerically small relative to reported standard deviations (0.005–0.008), making it unclear whether improvements are statistically robust. XGBoost and GRU-D are not obviously weaker in a way that rules out overlap.
2. **Baseline tuning asymmetry**: TimeWarn undergoes a 72-configuration grid search, while baselines "use the hyperparameters reported in their original papers." This is a significant methodological asymmetry that could inflate the apparent advantage of the proposed method — baselines should be tuned with comparable effort on the same datasets/splits.
3. **Missing details**: No description of the embedding function for measured values and missingness masks, no description of exact preprocessing/imputation, no reporting of the 32 variables, no information on how "hourly windows" are constructed for sparse labs, and no computational cost/training time comparison (especially relevant given the claimed simplicity advantage over neural ODE approaches, which are mentioned but not benchmarked).
4. **Novelty is limited**: The core contribution — a learned exponential decay factor applied to attention weights — is architecturally very close to GRU-D's decay mechanism transplanted onto RETAIN's attention weights rather than hidden states. The paper does not clearly differentiate this contribution from simply concatenating Δt as an attention input, which is a well-established idea in irregular time-series literature (e.g., time-aware LSTM, SAnD, mTAND, latent ODEs). No comparison to more recent irregular-time-series or attention-based methods (e.g., mTAND, SeFT, Latent-ODE, Transformer-based approaches) is included, only GRU-D and RETAIN.
5. **Interpretability claims are shallow**: The attention analysis is limited to a single aggregate statement about lactate/respiratory rate/MAP without quantitative comparison to ground truth clinical importance, sensitivity analysis, or case studies, and no comparison to RETAIN's own attention patterns to show the added decay actually improves interpretability rather than just AUROC.
6. **No external/temporal validation**: Only in-dataset splits are used; no cross-dataset generalization test (train on MIMIC, test on eICU) despite having both datasets available, which would meaningfully test robustness given the acknowledged limitation about generalizability across health systems.
7. **Clarity of decay formulation**: The decay formula γ = exp(−max(0, w·Δ+b)) is stated but not well justified vis-à-vis alternatives, and it is unclear whether w, b are shared across variables or per-variable (32 variables would need 32 decay curves, but this isn't specified).

## Note on embedded content
The manuscript does not contain any embedded instructions, hidden directives, or attempts to manipulate the review process. No such content was detected.

## Scores

| Criterion | Score (0–100) | Justification |
|---|---|---|
| Soundness | 55 | Reasonable experimental design but lacks significance testing, has an unfair baseline-tuning asymmetry, and omits several key implementation details. |
| Novelty | 40 | Incremental combination of two well-known ideas (RETAIN + GRU-D decay); no comparison against more recent irregular time-series baselines. |
| Significance | 55 | Addresses a real clinical need with modest but consistent gains; impact somewhat limited by retrospective-only evaluation and small effect sizes. |
| Clarity | 65 | Generally well-written and organized, but some methodological details (embedding construction, per-variable vs shared decay parameters) are underspecified. |

**Average score: 53.75 (≈54/100)**

## Recommendation: **Reject**

While the paper tackles a meaningful clinical problem and is clearly written, the technical contribution is incremental, the empirical gains are small and not accompanied by statistical significance testing, the baseline comparison is methodologically unbalanced (asymmetric hyperparameter tuning), and the interpretability analysis is underdeveloped relative to the paper's central claims. Stronger baselines from the modern irregular-time-series literature, cross-dataset validation, and more rigorous statistical reporting would be needed to support the claims at a level suitable for acceptance.