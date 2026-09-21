## Review

### Summary

This paper presents TimeWarn, an attention-based model for early sepsis prediction that explicitly incorporates irregular measurement intervals. The model extends the RETAIN architecture by using learned time-decay factors to modulate both visit-level and variable-level attention. Experiments on MIMIC-IV and eICU show improvements over qSOFA, logistic regression, XGBoost, GRU-D, and RETAIN for six-hour-ahead prediction, with additional ablations and attention analyses.

### Strengths

1. **Clinically relevant problem.** Early sepsis prediction from EHR data is important, and irregular sampling is a central characteristic of real-world clinical records.
2. **Reasonable methodological motivation.** Incorporating elapsed time into an interpretable attention architecture is a natural and clinically meaningful extension of RETAIN.
3. **Evaluation on two public datasets.** Testing on both MIMIC-IV and eICU improves the evidence for cross-dataset robustness.
4. **Comparison with relevant baselines.** The paper includes both conventional methods and strong neural baselines, including GRU-D and RETAIN.
5. **Useful metrics.** Reporting both AUROC and AUPRC is appropriate given the class imbalance.
6. **Ablation evidence.** The performance degradation after removing time decay supports the claimed contribution.
7. **Attention analysis.** The identified variables are clinically plausible and provide a useful initial interpretability analysis.
8. **Clear presentation.** The manuscript is concise, logically organized, and easy to follow.

### Areas for improvement

1. **Data-processing details are limited.** The paper should provide more information about temporal aggregation, imputation, normalization, handling of multiple measurements within an hourly window, and the precise construction of time intervals.
2. **Potential label and censoring issues deserve clarification.** Since Sepsis-3 labels depend on cultures, antibiotics, organ dysfunction, and documentation timing, the authors should state how onset time is operationalized and how prediction windows avoid post-onset information leakage.
3. **Baseline tuning may not be fully comparable.** TimeWarn is tuned through a stated grid search, whereas baselines use hyperparameters from their original papers. A fairer comparison would tune all methods under the same validation protocol, or provide a sensitivity analysis.
4. **Statistical reporting could be stronger.** Results are averaged over five seeds for neural models, but confidence intervals, paired comparisons, or significance tests would help establish whether the reported gains are robust.
5. **Interpretability claims should be qualified.** Attention weights are useful indicators of model focus but should not be treated as definitive causal explanations. Correlation between attention and clinical importance, as well as examples of patient-level explanations, would strengthen this section.
6. **Clinical utility is not evaluated.** Calibration, sensitivity at clinically relevant alarm rates, alert burden, and decision-curve or utility analysis would make the work more clinically actionable.
7. **Generalization remains limited.** Both datasets primarily represent U.S. intensive care populations. The limitations appropriately acknowledge this, but external validation in wards or non-U.S. systems would be important future work.

These issues primarily concern completeness of reporting, evaluation depth, and interpretation rather than a fundamental flaw in the proposed method or its empirical findings.

## Scores

| Criterion | Score |
|---|---:|
| **Soundness** | 82/100 |
| **Novelty** | 78/100 |
| **Significance** | 84/100 |
| **Clarity** | 86/100 |

### Final average

\[
\frac{82 + 78 + 84 + 86}{4} = \mathbf{82.5/100}
\]

## Final recommendation: **Accept**

The paper makes a clear and relevant contribution by combining irregular-time modeling with interpretable hierarchical attention for early sepsis prediction. The empirical improvements are consistent across two public ICU datasets, and the ablation supports the importance of time decay. While additional preprocessing details, stronger statistical comparisons, calibration analyses, and more cautious treatment of attention-based explanations would improve the work, these are addressable limitations and do not undermine the central contribution.