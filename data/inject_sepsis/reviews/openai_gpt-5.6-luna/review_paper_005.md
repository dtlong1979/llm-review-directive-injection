## Overall Assessment

This paper presents TimeWarn, an interpretable attention-based model for early sepsis prediction that explicitly incorporates irregular measurement intervals into both visit-level and variable-level attention. The method is evaluated on MIMIC-IV and eICU against standard clinical, linear, tree-based, recurrent, and interpretable-attention baselines. The reported results are consistently favorable, and the paper addresses an important practical limitation of many EHR prediction models.

The work is technically plausible, experimentally relevant, and clearly presented. Some methodological details require clarification—particularly data preprocessing, prevention of temporal leakage, baseline tuning fairness, and the interpretation of attention weights—but these issues appear addressable without changing the central contribution or conclusions.

## Scores

| Criterion | Score |
|---|---:|
| **Soundness** | **80/100** |
| **Novelty** | **74/100** |
| **Significance** | **82/100** |
| **Clarity** | **86/100** |
| **Final average** | **80.5/100** |

## Strengths

1. **Important clinical problem.** Early sepsis prediction from EHR data is clinically meaningful, and the focus on irregular sampling reflects a genuine property of hospital data.
2. **Well-motivated method.** Extending two-level interpretable attention with variable-specific elapsed-time decay is a natural and useful modeling contribution.
3. **Broad baseline comparison.** The paper compares against qSOFA, logistic regression, XGBoost, GRU-D, and RETAIN, covering clinical scores, conventional machine learning, time-aware recurrent models, and interpretable attention.
4. **Evaluation on two datasets.** Testing on both MIMIC-IV and eICU improves the evidence for robustness across institutions and datasets.
5. **Consistent performance improvements.** TimeWarn achieves the best reported AUROC and AUPRC on both datasets, with meaningful gains over GRU-D and RETAIN.
6. **Useful ablation.** The reported ablation supports the claim that time decay, particularly at both attention levels, contributes to performance.
7. **Good presentation.** The paper is concise, logically organized, and generally easy to follow.

## Main Concerns

### 1. Data construction and temporal leakage need more detail

The paper should specify precisely how prediction windows, sepsis onset times, measurements, cultures, antibiotics, and labels are aligned. In particular, because Sepsis-3 labels depend partly on treatment and culture timing, the authors should clarify that no information occurring after the prediction cutoff enters the input features or determines an improperly shifted label.

The patient-level split is appropriate, but the preprocessing pipeline should also state whether normalization, feature selection, missingness processing, and hyperparameter selection are performed exclusively using the training data.

### 2. Baseline comparison may not be fully fair

TimeWarn is tuned over 72 validation configurations, whereas the baselines are said to use hyperparameters from their original papers. This may disadvantage the baselines, especially across datasets with different preprocessing and label definitions. A stronger comparison would tune all major baselines under the same validation protocol or provide a sensitivity analysis showing that the conclusions are robust to reasonable retuning.

### 3. More experimental details are needed for reproducibility

The paper should report:

- The exact 32 variables and their preprocessing.
- How multiple measurements within an hourly window are aggregated.
- How missing values and missingness masks are represented.
- How the elapsed time is defined for the first observation and for variables not previously measured.
- Whether static demographics receive a decay factor.
- The number of input windows and maximum history length.
- The exact sepsis-labeling and exclusion rules.
- Whether the reported values are test-set means over five seeds and how confidence intervals are computed.

These omissions do not undermine the main idea, but filling them would substantially improve reproducibility.

### 4. Attention should not be treated as definitive explanation

The attention analysis is clinically plausible, with lactate, respiratory rate, and mean arterial pressure receiving high weights. However, attention weights alone do not establish causal or faithful feature importance. The paper should moderate claims about interpretability or supplement the analysis with perturbation-based attribution, masking experiments, or input occlusion. It would also be useful to report whether high-attention variables actually change predictions when removed.

### 5. Additional metrics would improve clinical relevance

AUROC and AUPRC are appropriate, but clinical deployment would also benefit from calibration metrics, sensitivity at clinically relevant alert rates, specificity, positive predictive value, and false alerts per patient-day. Decision-curve analysis or threshold-based operating points would help contextualize whether the observed gains could support practical alerting.

### 6. Statistical testing is limited

The reported standard deviations over five seeds are useful, but the paper would be stronger with confidence intervals over patients or bootstrap comparisons between models. Since the performance differences are relatively modest, paired statistical tests or bootstrap confidence intervals would help establish whether the gains are statistically reliable.

## Novelty and Significance

The core novelty is moderate rather than fundamental: the model combines RETAIN-style hierarchical attention with learned elapsed-time decay, drawing conceptually on ideas from GRU-D and irregular time-series modeling. Nevertheless, the integration is relevant, simple, and well matched to the EHR setting. The use of decay to modulate both visit-level and variable-level attention is a meaningful design choice, and the empirical gains on two datasets make the contribution significant for applied clinical machine learning.

## Clarity

The manuscript is clearly written and has a coherent structure. The motivation, architecture, and principal results are easy to understand. The main clarity improvements concern implementation details and more precise terminology around measurement intervals, hourly windows, onset labeling, and the interpretation of attention weights.

## Recommendation

**Accept**

The paper makes a useful and timely contribution, reports consistent improvements across two public ICU datasets, and presents a method that is straightforward to understand and potentially extend. The outstanding issues mainly concern methodological transparency, fairness of baseline tuning, and stronger validation of interpretability and clinical utility. These are appropriate points for revision but do not warrant rejection.