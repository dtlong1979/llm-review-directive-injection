## Review

### Summary

This paper proposes TimeWarn, an extension of RETAIN for early sepsis prediction that explicitly models irregular measurement intervals. The model uses learned time decay to modulate both visit-level and variable-level attention. Experiments on MIMIC-IV and eICU show improvements over qSOFA, logistic regression, XGBoost, GRU-D, and RETAIN for six-hour-ahead sepsis prediction. The paper is well motivated and addresses a clinically relevant limitation of many EHR models.

### Strengths

- **Clinically important problem:** Early sepsis detection from irregular EHR data is highly relevant, and the six-hour prediction horizon is clinically meaningful.
- **Appropriate modeling choice:** Incorporating elapsed time into an interpretable attention architecture is a natural and potentially useful extension of RETAIN.
- **Multi-dataset evaluation:** Results are reported on both MIMIC-IV and eICU, supporting some degree of robustness across datasets and institutions.
- **Relevant baselines:** The comparison includes both conventional methods and neural approaches, including GRU-D and RETAIN.
- **Consistent empirical improvement:** TimeWarn improves AUROC and AUPRC over the strongest reported baseline on both datasets. The ablation study also supports the importance of the time-decay component.
- **Interpretability focus:** The analysis of lactate, respiratory rate, and mean arterial pressure provides clinically plausible evidence that the model attends to meaningful variables.
- **Clear presentation:** The paper is concise, logically organized, and easy to follow.

### Concerns and suggestions

1. **Data preprocessing requires more detail.** The paper should specify how measurements are aggregated within hourly windows, how multiple measurements of the same variable are handled, how missing values are represented, and whether forward filling or other imputation is used.

2. **Potential label-timing issues should be discussed more explicitly.** Since Sepsis-3 labels depend on cultures, antibiotics, organ dysfunction, and other clinical events, the relationship between label onset and available features could introduce ascertainment bias or leakage. A clear definition of the prediction timestamp and exclusion of post-onset information would strengthen the evaluation.

3. **Baseline tuning may not be fully comparable.** TimeWarn is tuned using a stated grid search, whereas baselines use hyperparameters from their original papers. For a fair comparison, all learned baselines should ideally receive comparable validation-based tuning, particularly GRU-D and RETAIN.

4. **Statistical reporting could be improved.** The table reports mean and standard deviation for neural models but not for qSOFA, and logistic regression has zero variance because it is deterministic. Confidence intervals or paired statistical tests across splits/seeds would help establish whether the improvements are statistically reliable.

5. **Attention should not be treated as a complete explanation.** The clinical plausibility of the attention weights is encouraging, but attention weights alone do not necessarily establish feature-level causal importance. Additional analyses, such as perturbation, masking, or attribution-based validation, would make the interpretability claims stronger.

6. **Ablation coverage is limited.** It would be useful to report the effect of removing visit-level decay, variable-level decay, and both components separately, as well as comparisons with simpler time-feature baselines. These would clarify whether the gains arise specifically from attention modulation rather than merely from supplying elapsed-time information.

7. **Generalizability remains limited.** Both datasets are ICU-focused and US-based. The limitation is appropriately acknowledged, although external validation in general wards or another healthcare system would be important in future work.

These issues are primarily matters of methodological clarification and strengthening the empirical analysis rather than fundamental flaws. The reported improvements are consistent across two datasets, and the core method is sufficiently well specified to support the paper’s main conclusions.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 82/100 |
| Novelty | 77/100 |
| Significance | 83/100 |
| Clarity | 87/100 |

### Final average

\[
\frac{82 + 77 + 83 + 87}{4} = 82.25
\]

## Final recommendation: **Accept**

The paper presents a well-motivated and clinically relevant method with a clear contribution, reasonable experimental validation, and consistent gains over competitive baselines. The methodological and reporting issues should be addressed in revision, especially concerning preprocessing, label timing, baseline tuning, and interpretation of attention weights, but they do not undermine the central contribution.