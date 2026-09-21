# Peer Review: TimeWarn: Irregular-Interval Attention for Early Sepsis Prediction from Electronic Health Records

## Summary
The paper proposes TimeWarn, an extension of RETAIN's two-level attention architecture that incorporates a learned exponential decay function based on inter-measurement time intervals to modulate visit- and variable-level attention. The method is evaluated on MIMIC-IV and eICU for 6-hour-ahead sepsis prediction, with reported improvements over qSOFA, logistic regression, XGBoost, GRU-D, and RETAIN.

## Strengths
- Addresses a clinically important and well-motivated problem (irregular sampling in EHR time series).
- The proposed decay mechanism is simple, interpretable, and clearly described mathematically.
- Comparison against a reasonable set of baselines including both classical (qSOFA, logistic regression) and modern time-aware/interpretable models (GRU-D, RETAIN).
- Includes an ablation isolating the contribution of the decay mechanism at each attention level.
- Reports variance across seeds and includes a lead-time analysis, which is good practice.

## Weaknesses

**Soundness concerns:**
- No confidence intervals or statistical significance testing (e.g., paired t-test, bootstrap) are reported despite having 5 seeds; the AUROC gaps (0.016–0.023) are not clearly shown to be significant given the reported standard deviations, which are of similar or comparable magnitude in some cases.
- qSOFA and baseline hyperparameters are stated to use "originally reported" values without dataset-specific tuning, which may unfairly disadvantage baselines while TimeWarn undergoes a 72-configuration grid search — an inconsistent experimental protocol that biases comparison.
- No description of how missing data/imputation is handled beyond a "missingness mask," and no sensitivity analysis on the choice of hourly windowing, which could materially affect irregularity handling.
- Cohort exclusion criteria are not detailed, limiting reproducibility and making it hard to assess selection bias in the 8.9%/6.1% prevalence figures.
- The "attention analysis" claiming clinical alignment is only qualitative (top-3 variables) without quantitative validation, robustness checks, or comparison to attention weights of RETAIN for contrast.
- No external or temporal validation split (e.g., by year or site) — patient-level split alone doesn't test generalization across institutions within eICU's 208 hospitals, which would be a stronger and more informative test given the multi-center nature of the data.

**Novelty concerns:**
- The core contribution — multiplying attention weights by an exponential decay of elapsed time — is conceptually very close to GRU-D's decay mechanism and to prior work combining time-aware decay with attention (e.g., Dipole, RETAIN variants, T-LSTM). The novelty here is largely the specific combination/application rather than a fundamentally new mechanism.
- The paper does not discuss or compare against other interpretable irregular-time attention models (e.g., SAND, RAIM, or time-aware transformer variants) that would be natural competitors, leaving the novelty claim insufficiently contextualized.

**Significance concerns:**
- Absolute improvements (1.3–2.3 AUROC points) are modest and their clinical significance (e.g., effect on decision thresholds, false alarm rates) is not discussed.
- No analysis of calibration, alarm fatigue, or false-positive rate at clinically relevant operating points, which matters more than AUROC for early-warning deployment.
- The paper appropriately acknowledges retrospective-only evaluation and lack of clinical workflow impact in limitations, but this limits real-world significance substantially.

**Clarity:**
- The paper is generally well-written and organized, but some methodological details are underspecified (e.g., exact embedding architecture for window features, how variable-level decay γ is combined across variables with different measurement frequencies, exact definition of "recent" in attention analysis).
- Table only reports single-decimal ablation results without variance, inconsistent with the main table's reporting standard.

## Scores

| Criterion | Score (0–100) | Justification |
|---|---|---|
| Soundness | 55 | Reasonable experimental design but lacks statistical testing, inconsistent baseline tuning, insufficient reproducibility detail, and only qualitative interpretability validation. |
| Novelty | 45 | Incremental combination of established ideas (RETAIN + GRU-D-style decay); limited engagement with closely related time-aware attention literature. |
| Significance | 50 | Modest, plausible improvements on a clinically important task, but unclear practical impact without calibration/alarm-rate analysis or external validation. |
| Clarity | 70 | Generally clear and well-organized, though some technical and experimental details are missing. |

**Average score: 55**

## Recommendation: **Reject** (borderline, encourage resubmission with revisions)

The paper tackles a meaningful clinical problem with a reasonably designed method, but the incremental novelty, lack of statistical rigor around the reported gains, inconsistent baseline tuning protocol, and limited depth of interpretability/significance analysis fall short of the bar for acceptance in current form. Strengthening statistical validation, expanding related-work comparisons, and adding calibration/operating-point analysis would substantially improve the submission.