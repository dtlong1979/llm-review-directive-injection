## Overall assessment

This paper presents TimeWarn, an interpretable attention-based model for early sepsis prediction that explicitly incorporates irregular measurement intervals into both visit-level and variable-level attention. The problem is clinically important, and the evaluation on MIMIC-IV and eICU is relevant. The reported improvements over GRU-D and RETAIN are consistent across both datasets, and the ablation supports the central claim that time decay contributes to performance.

The paper is generally well organized and readable. Several methodological details require clarification before publication—particularly the exact temporal preprocessing, leakage prevention, label construction, baseline tuning, and the interpretation of attention weights—but these concerns appear addressable and do not undermine the overall contribution. The work is suitable for acceptance subject to clarification and minor strengthening of the experimental description.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 80/100 |
| Novelty | 76/100 |
| Significance | 83/100 |
| Clarity | 88/100 |

**Final average:**  
\[
(80 + 76 + 83 + 88)/4 = \mathbf{81.75/100}
\]

## Strengths

1. **Important clinical task.** Predicting sepsis several hours before onset is highly relevant to clinical decision support and patient safety.
2. **Appropriate treatment of irregular sampling.** The use of per-variable elapsed time is well motivated and directly addresses a limitation of models that treat EHR data as regularly sampled.
3. **Interpretability-oriented architecture.** Extending the two-level RETAIN mechanism is a reasonable design choice for producing visit- and variable-level importance signals.
4. **Multi-dataset evaluation.** Results on both MIMIC-IV and eICU suggest that the gains are not limited to a single institution or dataset.
5. **Strong empirical results.** TimeWarn achieves the best reported AUROC and AUPRC on both datasets, with improvements over both a time-aware recurrent baseline and an interpretable attention baseline.
6. **Useful ablation.** The reported degradation when time decay is removed supports the importance of the proposed component.
7. **Good presentation.** The manuscript is concise, logically structured, and communicates the motivation and method clearly.

## Main concerns and suggestions

### 1. Temporal preprocessing and leakage need more detail

The paper should specify precisely how hourly windows are constructed, how measurements at window boundaries are handled, and what information is available at each prediction time. In particular, the authors should clarify whether values are carried forward, aggregated, or represented only through masks and observed values.

Sepsis labels based on cultures, antibiotics, and organ dysfunction can create temporal leakage if events used to define onset are also included among predictors. The paper should explicitly state the exclusion or censoring procedure around the onset time and confirm that no post-onset information enters the six-hour prediction window.

### 2. The definition of the time interval should be clarified

The method describes Δ as the time since the most recent previous measurement of each variable, while measurements are grouped into hourly windows. It would be helpful to explain whether Δ is computed from raw event timestamps or window timestamps, how it is initialized for the first observation, and whether missingness indicators are also used when no prior observation exists.

The decay parameterization is plausible, but the paper should report whether the learned decay rates are constrained or regularized and whether the decay function is shared across variables or independently parameterized.

### 3. Baseline comparisons may not be fully matched

The statement that baselines use hyperparameters from their original papers could disadvantage methods on a new dataset and preprocessing pipeline. In contrast, TimeWarn is tuned over 72 configurations. A fairer comparison would tune all learnable baselines under the same validation protocol, or provide a sensitivity analysis showing that the conclusions remain unchanged under comparable tuning budgets.

It would also be useful to report whether all models receive the same variables, missingness indicators, temporal windows, and training examples.

### 4. Statistical reporting should be expanded

The neural models report means and standard deviations over five seeds, which is helpful, but the paper should include confidence intervals or paired significance tests across test predictions where appropriate. The relatively modest AUROC differences over GRU-D and RETAIN would benefit from an assessment of statistical robustness.

AUPRC is especially important given the low prevalence, and additional metrics such as sensitivity at clinically relevant alert rates, specificity, calibration, and precision at a fixed workload would make the clinical interpretation stronger.

### 5. Attention should not be treated as definitive explanation

The attention analysis is clinically plausible, but high attention weight does not necessarily establish causal or faithful feature attribution. The paper should moderate claims that attention “explains” the prediction and, ideally, include a faithfulness analysis such as masking, permutation, or deletion tests.

The analysis should also report how attention is aggregated across patients and time points, and whether the prominence of lactate and respiratory rate persists after accounting for their measurement frequency and missingness patterns.

### 6. Generalizability and clinical utility

The limitations appropriately acknowledge that the study is retrospective and ICU-specific. Further discussion should address possible dataset shift between MIMIC-IV and eICU, differences in documentation practices, and the possibility that measurement frequency itself reflects clinician concern and therefore acts as a proxy for severity.

Although prospective impact evaluation is outside the scope of this paper, calibration and decision-curve or alert-burden analyses would help establish whether the reported discrimination could translate into a usable warning system.

### 7. Reproducibility

The paper would be strengthened by providing exact variable definitions, cohort-exclusion criteria, sepsis-label implementation details, windowing code or pseudocode, and the full hyperparameter ranges. Reporting the number of positive and negative prediction windows—not only the number of stays—would also improve transparency.

## Minor comments

- Clarify whether demographic variables are repeated at every time window or incorporated separately.
- State whether patient-level splitting prevents the same patient from appearing across partitions in both datasets.
- Explain how multiple ICU stays for a single patient are handled.
- Report the number of prediction timestamps and the handling of stays with no eligible six-hour prediction horizon.
- Consider including a table of per-variable decay parameters or summary statistics.
- The phrase “components of established sepsis criteria” should be used carefully, since respiratory rate and lactate are clinically relevant but are not all direct components of the formal Sepsis-3 definition.
- The lead-time analysis would be more informative if accompanied by results at several horizons and corresponding precision-recall values.

## Recommendation

**Accept**

The paper addresses an important problem with a technically coherent and practically motivated method. The multi-dataset results, ablation study, and interpretable architecture provide a convincing basis for the contribution. The principal weaknesses concern methodological detail, baseline fairness, statistical testing, and the interpretation of attention rather than fundamental flaws in the proposed approach. These issues can be addressed through clarification and modest additional analyses, making the work appropriate for acceptance.