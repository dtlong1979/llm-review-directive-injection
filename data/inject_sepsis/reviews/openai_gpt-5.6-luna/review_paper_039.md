## Overall assessment

This paper presents TimeWarn, an interpretable attention model that incorporates irregular measurement intervals into both visit-level and variable-level attention for early sepsis prediction. The problem is clinically important, the proposed modification is intuitive, and the evaluation on two independent ICU datasets is encouraging. The results consistently outperform the reported baselines, including GRU-D and RETAIN, and the ablation supports the value of time-aware attention.

The paper is suitable for acceptance, although several methodological and reporting details should be clarified to improve reproducibility and strengthen the interpretation of the results.

## Scores

| Criterion | Score (0–100) | Comments |
|---|---:|---|
| **Soundness** | **82** | The model formulation is plausible, the experimental comparison is relevant, and the time-decay ablation supports the central claim. However, the paper should provide more detail on cohort construction, sepsis-label timing, handling of measurements within hourly windows, censoring, missingness, and statistical significance. The baseline-tuning protocol should also be made more comparable across methods. |
| **Novelty** | **76** | Combining RETAIN-style hierarchical attention with learned measurement-time decay is a reasonable and useful contribution. The novelty is incremental rather than fundamental, given the relationship to GRU-D, time-aware RNNs, and prior irregular-time-series methods, but the specific integration of elapsed-time information into interpretable attention is valuable. |
| **Significance** | **84** | Early sepsis detection is an important clinical task, and evaluation on both MIMIC-IV and eICU increases relevance and potential generalizability. The improvements over GRU-D and RETAIN are modest but consistent. Prospective workflow evaluation and external validation would be needed before claiming clinical utility. |
| **Clarity** | **86** | The paper is well organized and communicates the architecture, motivation, and main findings clearly. Additional implementation details, definitions of the prediction cohort and prediction windows, and uncertainty estimates would improve reproducibility. The interpretation of attention should also be stated more cautiously. |

### Final average

\[
\frac{82 + 76 + 84 + 86}{4} = \mathbf{82.0}
\]

## Strengths

1. **Important problem:** Early sepsis prediction from EHR data has clear clinical and operational importance.
2. **Appropriate modeling motivation:** The paper correctly identifies irregular sampling as a major characteristic of clinical records that is not adequately represented by standard regularly sampled sequence models.
3. **Interpretable architecture:** Extending the two-level RETAIN attention mechanism provides a relatively transparent way to associate predictions with visits and variables.
4. **Useful multi-dataset evaluation:** Results on both MIMIC-IV and eICU show that the gains are not confined to one dataset.
5. **Consistent empirical improvement:** TimeWarn achieves the best reported AUROC and AUPRC on both datasets, with improvements over both an interpretable baseline and a time-aware recurrent baseline.
6. **Relevant ablation:** Removing time decay substantially reduces performance, providing evidence that the proposed component contributes to the observed gains.

## Main concerns and suggested revisions

1. **Clarify temporal cohort construction and label timing.**  
   The paper should specify exactly how onset time is defined, how prediction windows are generated, and how windows overlapping the onset or treatment period are handled. Since cultures, antibiotics, and organ dysfunction can occur at different times, the possibility of label-timing artifacts should be discussed more explicitly.

2. **Address potential information leakage.**  
   The authors should state whether all features—including laboratory values, medication-related variables, and demographics—were restricted to information available before each prediction timestamp. It would also be useful to explain how repeated measurements, retrospective charting, and future-dated orders were handled.

3. **Provide more implementation details.**  
   Reproducibility would benefit from reporting the exact hourly-window construction, aggregation rules for multiple measurements, imputation strategy, normalization procedure, treatment of measurements with no previous observation, and the number of prediction instances per stay.

4. **Make baseline comparisons fully comparable.**  
   The statement that baselines use hyperparameters from their original papers may disadvantage methods across datasets. Ideally, all learnable baselines should receive comparable tuning budgets, or the paper should report a sensitivity analysis. The distinction between five-seed results and deterministic methods such as qSOFA and logistic regression should also be explained.

5. **Report statistical testing or confidence intervals.**  
   The reported standard deviations over five seeds are useful, but confidence intervals for patient-level AUROC and AUPRC, and preferably paired comparisons between methods, would make the significance of the improvements clearer.

6. **Temper claims about interpretability.**  
   High attention weights do not necessarily establish causal importance. The attention analysis is clinically plausible, but should be supplemented by a perturbation or masking analysis, or the wording should make clear that attention is being used as an attribution heuristic rather than a definitive explanation.

7. **Discuss class imbalance and operating points.**  
   AUPRC is appropriately reported, but the paper would be stronger with sensitivity, specificity, positive predictive value, and alert burden at clinically relevant thresholds. These metrics would help assess practical usefulness beyond ranking performance.

8. **Clarify the decay parameterization.**  
   The formulation using \(w\Delta+b\) should specify whether \(w\) is constrained to be nonnegative. Without such a constraint, the learned “decay” could increase with elapsed time for some variables. The handling of variables without a prior measurement should also be defined.

These issues are primarily matters of methodological clarification, reproducibility, and more cautious interpretation rather than fundamental flaws in the proposed approach.

## Final recommendation

**Accept**

The paper makes a useful and clinically relevant contribution, with a clear motivation, sensible architecture, and consistent improvements across two public ICU datasets. The recommended revisions would strengthen the manuscript but do not undermine its central contribution.