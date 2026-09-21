## Review

### Summary

This manuscript presents TimeWarn, an extension of RETAIN that incorporates variable-specific elapsed-time decay into visit- and variable-level attention for six-hour-ahead sepsis prediction. The reported results on MIMIC-IV and eICU are promising, with improvements over the listed baselines. However, the experimental description is insufficient to establish validity, and several methodological choices raise substantial concerns about label construction, temporal leakage, baseline fairness, and the interpretation of attention weights.

### Strengths

- Addresses an important clinical prediction problem and a real limitation of regularly sampled EHR models.
- Evaluates on two widely used public ICU datasets.
- Includes both conventional and neural baselines, including GRU-D and RETAIN.
- Reports both AUROC and AUPRC, which is appropriate for imbalanced sepsis prediction.
- Includes an ablation of the proposed decay mechanism and a longer lead-time experiment.
- The model concept is relatively simple and potentially computationally practical.

### Major concerns

1. **Insufficient specification of cohort construction and label timing.**  
   The manuscript does not explain how Sepsis-3 onset is operationalized, how culture and antibiotic timestamps are handled, how patients with multiple sepsis episodes are treated, or how observations after onset are excluded. These choices can materially affect performance.

2. **Potential temporal and treatment-related leakage.**  
   The 32 input variables are not listed in sufficient detail. If medication orders, cultures, or measurements obtained in response to suspected sepsis are included near the prediction time, the model may be detecting clinician recognition rather than predicting future onset. The temporal alignment of all features relative to the prediction cutoff must be explicitly described.

3. **Unclear construction of irregular intervals.**  
   Measurements are grouped into hourly windows, yet the decay is defined using the time since the most recent previous measurement of each variable. It is unclear whether this interval is computed at the raw-observation level or after window aggregation, how multiple measurements within a window are summarized, and how variables never previously observed are handled.

4. **Baseline comparison is potentially unfair.**  
   TimeWarn is tuned by grid search, whereas the baselines use hyperparameters from their original papers. This does not constitute a controlled comparison, especially across datasets with different preprocessing and feature definitions. All methods should receive comparable tuning and preprocessing treatment.

5. **Limited statistical evidence.**  
   The manuscript reports five seeds for neural models but provides no confidence intervals, paired statistical tests, or patient-level bootstrap estimates. The performance differences, particularly on eICU, may not be statistically significant. The ablation and lead-time results also lack variability estimates.

6. **Interpretability claims are overstated.**  
   Attention weights are not automatically faithful explanations. The analysis only reports that lactate, respiratory rate, and mean arterial pressure receive high average attention among true positives. This does not establish that the weights identify causal or clinically decisive evidence. Faithfulness tests, perturbation analyses, calibration of explanations, and comparisons with feature attribution methods would strengthen this claim.

7. **Reproducibility is inadequate.**  
   Important details are missing, including the complete variable list, preprocessing and normalization, observation history length, handling of missing values and outliers, class weighting or sampling, sequence truncation, exact train/test construction, early-stopping criteria, and the definition of the prediction index. These omissions make the reported results difficult to reproduce.

8. **Ablation coverage is narrow.**  
   The central design includes both visit-level and variable-level decay, but only limited variants are reported. It would be useful to compare no decay, variable-only decay, visit-only decay, alternative decay functions, fixed versus learned decay, and a model that uses elapsed time as an explicit covariate.

### Novelty and significance

The problem is significant, and handling irregular sampling is clinically relevant. However, the methodological novelty appears incremental: the proposed model combines RETAIN-style attention with a learned GRU-D-like exponential decay applied to attention weights. The paper should more clearly distinguish its contribution from existing time-aware recurrent and attention models. The empirical improvements are potentially meaningful, but their credibility depends on resolving the data-processing and comparison issues above.

### Clarity

The manuscript is generally readable and logically organized. Nevertheless, the method and experimental protocol are described too briefly for a clinical machine-learning paper. In particular, the definitions of sepsis onset, prediction windows, feature availability, and interval computation need substantially more detail.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 35/100 |
| Novelty | 50/100 |
| Significance | 58/100 |
| Clarity | 68/100 |

**Final average:** \((35 + 50 + 58 + 68) / 4 = 52.75/100\)

## Final recommendation: **Reject**

The clinical problem and preliminary results are promising, but the current manuscript does not provide enough methodological detail or experimental control to support its claims. A substantially revised version should clarify label and feature timing, rule out leakage, tune baselines fairly, provide uncertainty estimates, and moderate or validate its interpretability claims.