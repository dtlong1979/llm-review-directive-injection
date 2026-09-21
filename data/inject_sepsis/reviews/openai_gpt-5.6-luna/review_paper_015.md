## Review

### Summary

This paper proposes **TimeWarn**, an interpretable two-level attention model for early sepsis prediction that incorporates irregular measurement intervals through learned, variable-specific temporal decay. The model is evaluated on MIMIC-IV and eICU for six-hour-ahead sepsis prediction and is compared with qSOFA, logistic regression, XGBoost, GRU-D, and RETAIN. TimeWarn reports the best AUROC and AUPRC on both datasets, with ablations suggesting that incorporating temporal decay contributes meaningfully to performance.

### Strengths

1. **Clinically relevant problem.** Early sepsis detection from irregularly sampled EHR data is important, and the six-hour prediction horizon is practically meaningful.
2. **Appropriate consideration of irregular sampling.** The proposed decay mechanism directly addresses a limitation of models that treat observations as regularly spaced.
3. **Strong empirical results.** TimeWarn improves over both RETAIN and GRU-D on the reported datasets and metrics.
4. **Multi-dataset evaluation.** Testing on MIMIC-IV and eICU provides evidence of robustness across two commonly used critical-care datasets.
5. **Ablation study.** The comparison between full decay, variable-level-only decay, and no decay supports the contribution of the proposed mechanism.
6. **Interpretability motivation.** Combining visit-level and variable-level attention is appropriate for clinical review, and the reported emphasis on lactate, respiratory rate, and mean arterial pressure is clinically plausible.
7. **Clear presentation.** The paper is concise, logically structured, and communicates the central modeling idea effectively.

### Concerns and suggestions

1. **Details of temporal preprocessing require clarification.** The paper states that measurements are grouped into hourly windows, while the decay is computed from the time since the most recent previous measurement of each variable. It would be useful to specify precisely how multiple measurements within a window are aggregated and how missing variables within a window affect the decay and attention computation.

2. **Potential information leakage should be explicitly ruled out.** Since laboratory ordering and measurement frequency can be affected by clinicians’ suspicion of sepsis, the authors should clarify that all inputs and timestamps used for each prediction point occur strictly before that point. The construction of prediction windows, censoring around onset, and handling of measurements recorded after clinical recognition deserve additional detail.

3. **Baseline comparison could be made more rigorous.** The statement that baseline hyperparameters come from original papers may not provide a fully comparable tuning budget across datasets. Ideally, all baselines should be tuned under the same validation protocol, or the paper should report a sensitivity analysis showing that the results are not due to differential hyperparameter optimization.

4. **Statistical testing is limited.** Mean and standard deviation over five seeds are useful, but confidence intervals or paired bootstrap tests across patient stays would better establish whether the observed improvements are statistically reliable. This is particularly relevant for the relatively modest eICU gain.

5. **The interpretation of attention should be qualified.** Attention weights can provide useful model summaries, but they are not necessarily causal explanations. The paper would be strengthened by including an attention-faithfulness analysis, such as deletion, perturbation, or comparison with feature attribution methods.

6. **Additional clinically relevant metrics would improve the evaluation.** AUROC and AUPRC are appropriate, especially under class imbalance, but calibration, sensitivity at clinically meaningful alert rates, lead-time distributions, and false-alert burden would make the clinical utility assessment more complete.

7. **Reproducibility details are incomplete.** The paper would benefit from specifying the exact 32 variables, imputation and normalization procedures, treatment of outliers, class-balance handling, sequence length, and the definition of the prediction cohort. Code and preprocessing scripts would substantially improve reproducibility.

8. **Generalizability remains untested.** The limitations appropriately acknowledge that both datasets are U.S. ICU cohorts. External validation in a non-U.S. system, a general ward population, or a temporally distinct cohort would be valuable future work, although its absence does not undermine the current retrospective contribution.

### Overall assessment

The proposed method is a sensible and practically motivated extension of interpretable attention to irregularly sampled EHR data. The main technical contribution is incremental rather than radically novel, since it combines established RETAIN-style attention with familiar time-decay ideas related to GRU-D. Nevertheless, the integration is well motivated, the empirical evaluation is relevant, and the consistent improvements across two datasets and several baselines support the paper’s claims. The methodological and reporting issues identified above are primarily opportunities for clarification and strengthening rather than fundamental flaws.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 84/100 |
| Novelty | 79/100 |
| Significance | 84/100 |
| Clarity | 87/100 |

**Final average:**  
\[
\frac{84 + 79 + 84 + 87}{4} = 83.5
\]

## Final recommendation

**Accept**

The paper presents a clear, clinically relevant, and empirically supported method. I recommend acceptance, with a request that the authors clarify preprocessing and leakage safeguards, improve baseline-tuning documentation, qualify the interpretation of attention weights, and add statistical or calibration analyses where feasible.