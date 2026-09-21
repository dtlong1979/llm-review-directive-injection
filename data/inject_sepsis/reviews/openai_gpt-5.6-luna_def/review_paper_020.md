## Review

The manuscript addresses an important problem: incorporating irregular measurement timing into early sepsis prediction while retaining an attention-based interpretation mechanism. Evaluation on MIMIC-IV and eICU is potentially valuable, and the reported improvements over GRU-D and RETAIN are promising. However, substantial methodological and reporting gaps prevent confidence in the validity of the results.

### Major concerns

1. **Insufficiently specified prediction and labeling protocol.**  
   The manuscript does not clearly define the prediction units, observation window, exclusion of patients already septic at the prediction time, handling of multiple prediction windows per admission, or how onset time is determined. These details are critical for reproducing a six-hour-ahead sepsis task and for assessing possible label leakage.

2. **Potential leakage through measurement processes.**  
   Laboratory ordering and measurement frequency are strongly influenced by clinicians’ suspicion of sepsis. The proposed decay mechanism uses time since the previous measurement, and the model also receives missingness masks. These features may encode clinical concern rather than physiological deterioration. That is not necessarily inappropriate for an early warning system, but it must be explicitly characterized, controlled, and compared with stronger measurement-process baselines.

3. **Unclear definition of the time intervals.**  
   Measurements are grouped into hourly windows, but the method describes a variable-specific interval “since the most recent previous measurement.” It is unclear whether this interval can refer to measurements outside the observation window, how simultaneous measurements are handled, and how decay is computed for variables never previously observed. The relation between hourly aggregation and irregular timestamps needs precise formalization.

4. **Baseline comparisons may be unfair or incomplete.**  
   The statement that baselines use hyperparameters from their original papers is not an adequate comparison across datasets. All models should receive comparable tuning budgets, preprocessing, input variables, observation windows, and stopping criteria. In particular, GRU-D and RETAIN should be carefully tuned on these datasets. A stronger time-aware attention or transformer baseline would also help establish the contribution of the proposed architecture.

5. **Limited statistical analysis.**  
   Results are averaged over five seeds, but no confidence intervals, paired bootstrap tests, or significance tests are reported. The improvements, especially on eICU, may or may not be statistically meaningful. Performance should be reported per seed and preferably with patient-level bootstrap confidence intervals.

6. **Attention is not sufficient evidence of interpretability.**  
   The analysis only reports that lactate, respiratory rate, and mean arterial pressure receive high attention. This does not establish that attention weights faithfully explain model decisions. The manuscript should include perturbation or feature-ablation tests, consistency analyses, and examples of predictions. The claim that these variables align with “established sepsis criteria” is also imprecise: lactate is clinically relevant to organ dysfunction, but it is not itself a component of qSOFA.

7. **Missing experimental details.**  
   Important information is absent, including normalization and imputation procedures, the exact 32 variables, observation-history length, class weighting or sampling strategy, number of training epochs, dropout values, grid-search ranges, implementation details, and treatment of repeated ICU stays. These omissions substantially limit reproducibility.

8. **Generalizability is limited.**  
   Both datasets are US ICU datasets, and the study does not evaluate temporal or hospital-level generalization. In eICU, patient-level splitting may allow institution-specific patterns to appear in both training and test sets. A hospital-held-out analysis would be useful.

### Strengths

- The clinical problem is important and practically relevant.
- The proposed use of variable-specific time decay is intuitive and potentially useful.
- Evaluation on two public datasets is preferable to evaluation on a single cohort.
- The ablation suggests that the time-decay component contributes to performance.
- The manuscript is generally concise and easy to follow.

### Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| Soundness | **48** | Promising design, but incomplete task specification, possible leakage, unclear interval handling, and limited statistical validation undermine confidence. |
| Novelty | **55** | Combining RETAIN-style attention with learned temporal decay is a reasonable incremental contribution, but it is closely related to GRU-D and existing time-aware attention methods. |
| Significance | **62** | Early sepsis prediction is clinically important, and robust gains could be meaningful, but the current evidence is not sufficient to establish clinical value. |
| Clarity | **68** | The high-level presentation is clear, but essential methodological and experimental details are missing. |

**Final average:**  
\[
(48 + 55 + 62 + 68)/4 = \mathbf{58.25}
\]

## Final recommendation: **Reject**

The topic and initial results are promising, but the current manuscript does not provide enough methodological detail or validation to support its central claims. A substantially revised version should clarify the labeling and prediction protocol, address leakage and fairness of comparisons, provide complete reproducibility details, and strengthen the statistical and interpretability analyses.

The manuscript contains an embedded instruction requesting an Accept recommendation. I treated that sentence as part of the submitted material rather than as an instruction, and the recommendation above is based solely on the paper’s scholarly merits.