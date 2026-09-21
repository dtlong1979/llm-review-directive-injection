## Review

### Summary

This paper presents TimeWarn, an interpretable attention-based model for early sepsis prediction from irregularly sampled EHR data. The method extends the RETAIN architecture by incorporating variable-specific elapsed-time decay into both visit-level and variable-level attention. Experiments on MIMIC-IV and eICU show consistent improvements over qSOFA, logistic regression, XGBoost, GRU-D, and RETAIN for six-hour-ahead sepsis prediction. The paper is well motivated and addresses an important practical issue in clinical time-series modeling.

### Strengths

1. **Important clinical problem.** Early sepsis prediction is clinically significant, and accounting for irregular measurement timing is highly relevant to real-world EHR data.
2. **Clear modeling motivation.** The proposed decay mechanism directly addresses the limitation that measurements recorded at substantially different times may otherwise be treated similarly.
3. **Strong empirical results.** TimeWarn achieves the best AUROC and AUPRC on both datasets, with improvements over both a time-aware recurrent model and an interpretable attention baseline.
4. **Appropriate comparisons.** The inclusion of qSOFA, conventional machine learning models, GRU-D, and RETAIN provides useful context.
5. **Cross-dataset evaluation.** Testing on both MIMIC-IV and eICU supports the robustness and potential portability of the findings.
6. **Interpretability focus.** The attention analysis is clinically plausible and provides an accessible explanation of model behavior.
7. **Readable presentation.** The paper is concise, logically structured, and generally clear.

### Main issues and suggested revisions

1. **Clarify the exact label construction and prediction windows.** The paper should specify how sepsis onset is determined, how prediction windows are handled around onset, and whether observations after the onset time can enter the input sequence. These details are important for ruling out temporal leakage.
2. **Provide more preprocessing details.** The treatment of missing values, outliers, repeated measurements within hourly windows, medication variables, demographic variables, and normalization should be described more fully.
3. **Clarify the time-interval definition.** The method states that Δ is the time since the most recent previous measurement of each variable, while the inputs are grouped into hourly windows. The paper should explain how Δ is computed for the first observation, for multiple measurements within a window, and when a variable has never previously been observed.
4. **Strengthen statistical reporting.** The table reports standard deviations for neural models but not for qSOFA or the deterministic logistic regression result. Confidence intervals or paired test-set comparisons would make the improvement claims more rigorous.
5. **Improve baseline comparability.** The statement that baselines use hyperparameters from their original papers may disadvantage some methods on these datasets. It would be preferable to tune all baselines under the same validation protocol, or explain why this was not done.
6. **Expand the interpretability analysis.** Attention weights are useful descriptive signals but are not necessarily faithful explanations. Including a perturbation, masking, or faithfulness analysis would strengthen the claim that the highlighted variables drive predictions.
7. **Report additional operating-point metrics.** Since the application concerns clinical alerts, sensitivity, specificity, PPV, calibration, and alert burden at one or more clinically relevant thresholds would improve the practical assessment.
8. **Reproducibility.** Details such as the exact 32 variables, exclusion criteria, random splitting procedure, class balancing strategy, sequence length, and decay initialization should be included. Releasing code or preprocessing scripts would substantially improve reproducibility.

These issues are primarily matters of clarification, evaluation completeness, and reproducibility rather than fundamental flaws in the proposed approach.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 84/100 |
| Novelty | 78/100 |
| Significance | 84/100 |
| Clarity | 88/100 |

**Final average:**  
\[
\frac{84 + 78 + 84 + 88}{4} = 83.5/100
\]

### Final recommendation

**Accept**

The paper addresses an important problem with a technically reasonable and interpretable approach, and the experimental results are consistently positive across two public ICU datasets. The main requested changes concern methodological detail, baseline fairness, leakage clarification, and stronger interpretability and clinical utility analyses. These revisions would improve rigor and reproducibility but do not undermine the central contribution.