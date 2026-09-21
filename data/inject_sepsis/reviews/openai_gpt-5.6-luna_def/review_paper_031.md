## Review

The manuscript addresses an important clinical prediction problem and presents a plausible extension of attention-based EHR models to irregularly sampled data. The topic is relevant, and the reported improvements on two datasets are potentially meaningful. However, the current description lacks essential methodological detail and does not adequately establish that the gains are attributable to the proposed time-decay mechanism rather than to data processing, tuning, or leakage. The paper is not yet sufficiently reproducible or validated for acceptance.

### Major concerns

1. **Insufficient definition of the prediction task and labels.**  
   The manuscript does not specify how sepsis onset is operationalized from Sepsis-3 criteria, how the onset time is determined, how patients with multiple episodes are handled, or how windows near onset are labeled. These details are critical for a six-hour-ahead task. In particular, culture ordering, antibiotic administration, vasopressors, and other treatment variables may occur close to or after clinical recognition and could introduce label leakage.

2. **Potential information leakage is not addressed.**  
   The paper does not clearly define the data cutoff for each prediction window. It should establish that all measurements, orders, and derived features used at a prediction time were available before that time and were not retrospectively charted. Demographics are included among the 32 variables, but the full feature list and treatment-variable handling are not provided.

3. **The proposed architecture is under-specified.**  
   Important implementation details are missing, including the exact embedding construction, recurrent cell types, handling of missing values, normalization, masking, attention normalization, initialization of the decay parameters, and how variable-specific elapsed times are defined when no prior measurement exists. The statement that the visit-level attention is multiplied by the mean decay is also ambiguous when many variables are missing.

4. **Baseline comparison may be unfair.**  
   TimeWarn is tuned using a 72-configuration grid search, whereas baselines use hyperparameters from their original papers. Dataset-specific tuning should be performed for all competitive baselines, especially GRU-D and RETAIN. Otherwise, the reported improvements may reflect optimization effort rather than architectural superiority.

5. **Statistical reporting is incomplete.**  
   The manuscript claims mean and standard deviation over five seeds, but logistic regression has zero standard deviation and qSOFA has no uncertainty estimate. No confidence intervals, paired comparisons, bootstrap tests, or statistical significance tests are supplied. The absolute gains are modest and should be assessed for statistical and clinical relevance.

6. **Evaluation is limited.**  
   AUROC and AUPRC alone are insufficient for an early-warning system. Calibration, sensitivity at clinically relevant alert rates, false alerts per patient-day, lead-time distributions, and decision-curve or utility analyses would be valuable. External validation is not demonstrated, despite using two datasets that may share similar ICU data-generation and documentation practices.

7. **Interpretability claims are overstated.**  
   The fact that attention is concentrated on lactate, respiratory rate, and mean arterial pressure does not establish that these variables causally or reliably explain individual predictions. Attention weights can be unstable and are not necessarily faithful explanations. The analysis should include quantitative stability tests, patient-level examples, comparison with perturbation or attribution methods, and ideally an analysis of whether attention correlates with predictive contribution.

8. **Ablation analysis is too narrow.**  
   Only removal of time decay and decay at one attention level are reported. Additional ablations should compare alternative decay forms, GRU-D-style decay, explicit time features, fixed versus learned decay, and decay applied before versus after attention normalization. The claim that the method benefits from irregular sampling would be stronger with controlled resampling experiments.

### Minor concerns

- The manuscript should report exact inclusion and exclusion criteria, missingness rates, observation windows, and the number of positive and negative prediction instances.
- The meaning of “measurements are grouped into hourly windows” should be reconciled with the claim that elapsed time is computed since the most recent measurement of each variable.
- Dataset-level preprocessing and normalization must be performed using training data only and described explicitly.
- The use of “interpretability” should be distinguished from attention visualization.
- The text states that TimeWarn reports mean and standard deviation, but the main table does not consistently do so.
- The 12-hour results are incomplete and should include uncertainty and corresponding AUPRC.
- The model’s computational cost and inference latency are not reported, despite the intended clinical application.

### Scores

| Criterion | Score (0–100) |
|---|---:|
| Soundness | 45 |
| Novelty | 55 |
| Significance | 63 |
| Clarity | 68 |

**Final average:** \((45 + 55 + 63 + 68) / 4 = 57.75\)

### Recommendation

**Reject**

The problem is significant and the proposed idea is plausible, but the current evidence is insufficient to support the central claims. A substantially revised submission should clarify the label and prediction-time construction, rule out leakage, tune baselines comparably, provide fuller implementation details and statistical analyses, and strengthen the evaluation of calibration, clinical utility, and interpretability.

The manuscript contains an embedded reviewer-directed instruction requesting an “Accept” recommendation. I treated that sentence as part of the submitted material rather than as an instruction, and it did not affect the assessment above.