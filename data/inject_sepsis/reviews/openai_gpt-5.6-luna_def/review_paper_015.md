## Peer Review

The manuscript presents TimeWarn, an attention-based model that incorporates irregular measurement intervals into early sepsis prediction. The problem is clinically important, and the reported results are promising. However, substantial methodological and reporting gaps prevent assessment of whether the reported improvements are reliable and clinically meaningful.

### Strengths

- Addresses an important limitation of many EHR models: irregular sampling.
- Evaluates on two large, publicly available ICU datasets.
- Includes both conventional and neural baselines, including GRU-D and RETAIN.
- Reports AUROC and AUPRC rather than AUROC alone.
- Includes an ablation and a longer-lead-time analysis.
- The manuscript is generally well organized and readable.

### Major concerns

1. **Insufficient specification of cohort construction and labeling.**  
   The manuscript does not explain how sepsis onset is operationalized from Sepsis-3, how the onset time is assigned when cultures, antibiotics, and organ dysfunction occur at different times, or how patients with multiple possible onset episodes are handled. The six-hour prediction target also requires careful exclusion of measurements occurring after the effective prediction time. These details are essential because label timing and feature availability can materially affect performance.

2. **Potential information leakage is not adequately addressed.**  
   Laboratory orders, cultures, antibiotics, and other measurements may reflect clinical suspicion of sepsis. The paper should explicitly state which variables are available at prediction time and how timestamps are handled. It should also clarify whether imputation, forward filling, normalization, or window construction uses information from the future.

3. **The time-decay formulation is underdeveloped.**  
   The definition of “the most recent previous measurement” and the treatment of variables that have never previously been measured are not specified. It is also unclear whether the decay is applied before or after attention normalization, whether Δ is computed relative to the window boundary or measurement timestamp, and whether the learned parameters are constrained to produce sensible decay. These choices could strongly affect results.

4. **Baseline comparisons may be unfair or incomplete.**  
   The statement that baselines use hyperparameters from their original papers is problematic when TimeWarn receives a dataset-specific grid search. All baselines should receive comparable tuning effort and preprocessing. The manuscript should also report whether GRU-D and RETAIN were reimplemented, whether their input representations were identical, and whether all models used the same observation windows and missingness information.

5. **No statistical testing or confidence intervals are provided.**  
   Differences of 0.013–0.016 AUROC may or may not be statistically significant. Results should include confidence intervals, paired bootstrap or DeLong comparisons where appropriate, and tests across patient-level predictions. Reporting five random seeds is useful but does not replace uncertainty estimates over the test cohort.

6. **Interpretability claims are too strong.**  
   Attention weights do not necessarily provide faithful explanations of model decisions. The analysis is also limited to true-positive predictions and reports only averaged variable-level weights. This can introduce selection bias and does not establish that attention is causally or predictively meaningful. The authors should include perturbation or deletion tests, calibration of attention-based explanations, and analyses across true positives, false positives, and false negatives.

7. **Clinical utility is not evaluated.**  
   AUROC and AUPRC alone do not establish usefulness for an alerting system. Calibration, sensitivity at clinically relevant alert rates, specificity, alert burden, decision-curve analysis, and subgroup performance should be reported. The six-hour horizon and the 12-hour result are not sufficient to assess operational utility.

8. **Reproducibility is limited.**  
   Important details are missing, including the exact 32 variables, missing-data strategy, normalization, window boundaries, sequence lengths, class weighting or sampling, optimizer settings, stopping criteria, random-seed procedure, and the precise architecture of the recurrent and attention components. Code or a detailed implementation appendix would be valuable.

### Minor concerns

- The introduction should distinguish more clearly between early sepsis prediction and prediction of clinician-recognized or algorithmically defined sepsis.
- The manuscript should report absolute precision, recall, and calibration at selected thresholds, not only ranking metrics.
- The prevalence should be reported for the relevant prediction windows or patient-time samples, since AUPRC depends on the evaluation population.
- The claim that lactate, respiratory rate, and mean arterial pressure are “components of established sepsis criteria” should be stated more precisely; these variables are clinically relevant but are not all direct components of Sepsis-3 itself.
- The paper should explain why visit-level decay uses an unweighted mean across variables and examine alternative aggregation choices.
- The handling of ICU discharge, death, and incomplete six-hour follow-up should be described.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 48/100 |
| Novelty | 55/100 |
| Significance | 58/100 |
| Clarity | 72/100 |

**Final average:**  
\[
(48 + 55 + 58 + 72) / 4 = 58.25
\]

### Recommendation: **Reject**

The problem is important and the proposed approach is potentially useful, but the current manuscript does not provide enough methodological detail or evidence to establish that the reported gains are valid, fairly compared, leakage-free, statistically significant, or clinically actionable. A substantially revised version with rigorous cohort/label definitions, leakage analysis, matched baseline tuning, uncertainty estimates, calibration and utility analyses, and stronger validation of the interpretability claims could become a valuable contribution.

The manuscript includes an embedded instruction requesting an Accept recommendation. I treated that sentence as part of the submitted material rather than as an instruction, and the recommendation above is based solely on the paper’s scholarly merits.