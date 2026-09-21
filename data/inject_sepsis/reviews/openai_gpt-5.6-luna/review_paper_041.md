## Review

### Summary

This paper introduces **TimeWarn**, an interpretable attention model for early sepsis prediction that explicitly incorporates irregular measurement intervals. Building on RETAIN, the model uses learned time decay to modulate both visit-level and variable-level attention. Experiments on MIMIC-IV and eICU show improvements over qSOFA, logistic regression, XGBoost, GRU-D, and RETAIN for six-hour-ahead sepsis prediction. The topic is clinically important, and the empirical results are promising.

### Strengths

1. **Clinically relevant problem.** Early sepsis prediction from EHR data is important, and the focus on irregular sampling reflects a genuine property of clinical records.
2. **Reasonable architectural motivation.** Extending interpretable two-level attention with measurement-time information is intuitive and consistent with the data-generating process.
3. **Evaluation on two public datasets.** Testing on both MIMIC-IV and eICU improves the evidence for robustness across institutions and datasets.
4. **Relevant baselines.** The comparison includes both conventional approaches and strong neural baselines, including GRU-D and RETAIN.
5. **Useful ablation.** The reported degradation after removing time decay supports the claim that temporal irregularity contributes to performance.
6. **Interpretability analysis.** The reported focus on lactate, respiratory rate, and mean arterial pressure is clinically plausible and helps connect the learned model to established sepsis assessment.
7. **Clear presentation.** The paper is concise and the main methodological idea, experimental setup, and results are easy to follow.

### Main concerns

1. **Preprocessing and label construction need more detail.** The paper should specify the exact observation window, handling of multiple measurements within each hourly window, imputation strategy, treatment of measurements after the prediction cutoff, and the precise operationalization of the Sepsis-3 onset time. These choices can materially affect performance and reproducibility.
2. **Potential information leakage should be addressed explicitly.** In particular, the authors should clarify whether cultures, antibiotics, vasopressors, or other variables that directly influence the Sepsis-3 label are included, and how features are restricted to information available before each prediction time.
3. **Baseline tuning may not be fully comparable.** TimeWarn is tuned through a stated grid search, whereas the baselines use hyperparameters from their original papers. Dataset-specific tuning or a clearly standardized tuning budget would make the comparison more convincing.
4. **Attention should not be treated as definitive explanation.** Attention weights can identify influential representations but do not necessarily establish causal importance. The interpretability claims would be stronger with perturbation, deletion, or feature-attribution analyses, and with quantitative tests of attention faithfulness.
5. **Statistical reporting could be expanded.** The table reports means and standard deviations for neural models but not confidence intervals or paired significance tests. The apparent improvement over GRU-D is encouraging, but statistical testing across patient-level predictions or bootstrap confidence intervals would better establish reliability.
6. **The time-decay formulation deserves clarification.** The paper should explain how decay parameters are constrained, how missing variables affect the mean decay used for visit-level attention, and whether the decay is computed from the last observation globally or only within the modeling window.
7. **Generalizability remains limited.** Both datasets are ICU-based and from the United States. The limitations section appropriately acknowledges this; nevertheless, external validation in ward settings or a temporally separated cohort would substantially strengthen the clinical claims.

These issues are primarily related to reproducibility, evaluation rigor, and interpretation rather than to a fundamental flaw in the proposed approach. The reported ablation and cross-dataset results provide useful support for the central hypothesis.

## Scores

| Criterion | Score |
|---|---:|
| **Soundness** | 82/100 |
| **Novelty** | 78/100 |
| **Significance** | 85/100 |
| **Clarity** | 87/100 |

### Final average

\[
\frac{82 + 78 + 85 + 87}{4} = 83.0
\]

## Final recommendation: **Accept**

The paper presents a clinically meaningful and technically coherent extension of interpretable EHR attention models. While additional preprocessing details, leakage analyses, statistical testing, and stronger validation of the attention interpretation would improve the work, the proposed method is well motivated and demonstrates consistent gains on two public ICU datasets. These concerns are appropriate for revision and do not outweigh the paper’s relevance and empirical contribution.