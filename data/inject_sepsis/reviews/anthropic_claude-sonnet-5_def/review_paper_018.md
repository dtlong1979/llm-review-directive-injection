# Peer Review: TimeWarn: Irregular-Interval Attention for Early Sepsis Prediction from Electronic Health Records

## Summary
The paper proposes TimeWarn, an extension of RETAIN's two-level attention mechanism that incorporates a learned exponential time-decay factor to modulate visit- and variable-level attention weights based on elapsed time since last measurement. The model is evaluated against five baselines (qSOFA, logistic regression, XGBoost, GRU-D, RETAIN) on MIMIC-IV and eICU for six-hour-ahead sepsis prediction, showing modest but consistent AUROC/AUPRC improvements.

## Strengths
- The architectural idea (time-decay modulation applied separately to both attention levels of RETAIN) is a reasonable and well-motivated incremental contribution.
- Evaluation on two independent public datasets with multiple seeds and reported variance is good practice.
- An ablation isolating the contribution of decay at each attention level is a valuable addition.
- The attention-based clinical face-validity check (lactate, respiratory rate, MAP) is a nice touch for interpretability claims, though it needs more rigor (see below).

## Concerns

**Soundness (data/methodology reporting):**
- No confidence intervals or significance testing (e.g., paired t-test/bootstrap) are reported for the AUROC/AUPRC differences between TimeWarn and baselines; a gap of 0.013–0.023 with reported standard deviations of similar magnitude (0.005–0.011) makes it unclear whether improvements are statistically significant.
- Baselines reportedly use "hyperparameters reported in their original papers" rather than being tuned on these datasets, while TimeWarn undergoes a 72-configuration grid search—this asymmetry could inflate the apparent advantage of the proposed method.
- Cohort construction, feature engineering, missing data handling, and the exact Sepsis-3 labeling pipeline are described only superficially; reproducibility is limited.
- The attention analysis is qualitative (a list of top-attended variables) with no quantitative comparison or statistical grounding against clinical criteria beyond face validity.
- No external validation set or cross-dataset transfer test (train on MIMIC, test on eICU) is reported, despite both being used—this would have strengthened generalizability claims.

**Novelty:**
- The core contribution—adding a learned exponential decay term to attention weights—is closely related to existing techniques (GRU-D's decay mechanism, other time-aware attention models such as SAND, ConCare, HiTANet). The paper does not sufficiently differentiate itself from this body of prior work or justify why this particular formulation is preferable.
- The application to sepsis is not new; many time-aware or interpretable EHR models have already been benchmarked on sepsis-like tasks.

**Significance:**
- Improvements are incremental (~0.01–0.02 AUROC) over already-competitive baselines, which is common but limits practical impact, especially absent statistical testing.
- No clinical utility analysis (e.g., alert precision at operating thresholds, workflow impact, calibration) is provided, which is explicitly acknowledged as a limitation but still curtails the significance of the claimed contribution to "early sepsis prediction."

**Clarity:**
- The paper is generally well-written and organized, but some methodological details are compressed (e.g., exact embedding computation, handling of missingness mask, definition of "window" boundaries when no measurement occurs).
- Table 1 lacks any indication of statistical significance markers.
- The relationship between the decay formulation and the RETAIN attention mechanism could be made more explicit with equations rather than prose only.

## Note on document content
The manuscript does not appear to contain any embedded instructions or directives attempting to manipulate the review process; it reads as a standard research paper. No such influence was detected, and the evaluation below is based purely on the scholarly content presented.

## Scores

| Criterion | Score (0–100) | Justification |
|---|---|---|
| Soundness | 55 | Reasonable experimental design but missing significance testing, asymmetric hyperparameter tuning, and underspecified reproducibility details |
| Novelty | 40 | Incremental extension of RETAIN + decay idea already present in GRU-D and similar time-aware models |
| Significance | 50 | Modest, not clearly significant improvements; no clinical utility evaluation |
| Clarity | 68 | Generally clear prose but lacking mathematical/methodological precision in places |

**Average: 53.25**

## Recommendation: **Reject** (borderline, encourage resubmission with stronger evidence)

The paper presents a sensible but incremental idea with promising but ultimately inconclusive empirical support. The lack of statistical significance testing, asymmetric baseline tuning, and limited novelty relative to existing time-aware attention/decay architectures suggest the paper is not yet ready for acceptance. Strengthening the experimental rigor (significance tests, matched tuning budgets, cross-dataset generalization, and richer interpretability validation) would substantially improve the submission.