## Review

### Summary

This paper proposes TimeWarn, an interpretable two-level attention model for early sepsis prediction that explicitly incorporates irregular measurement intervals. The model extends the RETAIN architecture by applying learned time-decay factors to both visit-level and variable-level attention. Experiments on MIMIC-IV and eICU show improvements over qSOFA, logistic regression, XGBoost, GRU-D, and RETAIN for six-hour-ahead sepsis prediction. The paper is well motivated, clearly written, and addresses an important practical issue in clinical time-series modeling.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 84/100 |
| Novelty | 78/100 |
| Significance | 82/100 |
| Clarity | 88/100 |
| **Final average** | **83.0/100** |

## Strengths

1. **Important problem formulation.** Irregular sampling is a central characteristic of EHR data, and explicitly modeling elapsed time is clinically and technically appropriate.
2. **Reasonable architectural design.** Extending RETAIN with time-dependent modulation provides a coherent connection between temporal irregularity and interpretability.
3. **Evaluation on two datasets.** Testing on both MIMIC-IV and eICU improves the evidence for cross-dataset robustness.
4. **Relevant baselines.** The comparison includes classical methods, tree-based models, GRU-D, and RETAIN, covering both predictive and interpretable approaches.
5. **Consistent empirical gains.** TimeWarn improves AUROC and AUPRC on both datasets, and the ablation indicates that the time-decay mechanism contributes materially to performance.
6. **Clinical plausibility of attention patterns.** Lactate, respiratory rate, and mean arterial pressure are clinically relevant variables, making the qualitative attention analysis useful.
7. **Clear presentation.** The paper is concise, logically organized, and communicates the motivation, method, and results effectively.

## Main concerns and suggestions

### 1. Data preprocessing and leakage prevention need more detail

The paper should specify precisely how measurements, labels, cultures, antibiotics, and sepsis onset times are aligned. In particular, it would be important to clarify that no information recorded after the prediction cutoff is included, including retrospective charting or laboratory results whose collection time differs from their result time. The patient-level split is appropriate, but the treatment of multiple ICU stays from the same patient should also be described.

This is primarily a reproducibility clarification rather than a fundamental flaw.

### 2. Baseline tuning may not be fully comparable

The statement that baselines use hyperparameters from their original papers could disadvantage methods across datasets and preprocessing pipelines. Ideally, all learned baselines should receive comparable validation-based tuning budgets. The paper would be strengthened by reporting whether GRU-D and RETAIN were reimplemented or taken from existing code, and by clarifying whether the same input representation and missingness handling were used for every model.

### 3. The time-decay formulation deserves additional analysis

The decay function is plausible, but the paper does not report the learned decay parameters or discuss whether decay is monotonic for all variables. Since the model uses both variable-specific and mean visit-level decay, it would be helpful to include:

- a comparison with fixed exponential decay;
- a version using elapsed time as an ordinary input feature;
- sensitivity to the decay initialization;
- distributions or examples of learned decay rates.

The existing ablation is useful, but these additions would more directly establish why the proposed parameterization is beneficial.

### 4. Attention should not be presented as definitive causal explanation

The attention analysis is clinically plausible, but attention weights are not necessarily faithful explanations of model decisions. The wording should make clear that the analysis identifies variables receiving high model attention, rather than proving that these variables causally drive predictions. A complementary perturbation, occlusion, or attribution analysis would improve the interpretability claim.

### 5. Statistical reporting could be improved

The paper states that neural models were trained with five seeds, but the table reports no variability for qSOFA and reports zero standard deviation for logistic regression. This is understandable for deterministic methods, but the manuscript should explicitly state which methods are deterministic and how confidence intervals or statistical comparisons were computed. Confidence intervals, bootstrap comparisons, or paired test-set analyses would make the reported improvements more convincing.

### 6. Clinical utility is not yet assessed

AUROC and AUPRC are appropriate discrimination metrics, particularly under class imbalance, but clinical deployment would also require calibration, sensitivity at clinically meaningful alert rates, false alerts per patient-day, and decision-curve or utility analysis. The authors appropriately acknowledge the absence of prospective workflow evaluation. Adding calibration and threshold-based metrics, if possible, would substantially strengthen the current retrospective evaluation.

### 7. Reproducibility information is incomplete

The manuscript would benefit from specifying the exact 32 variables, window construction rules, normalization procedure, handling of multiple measurements within an hour, missing-value representation, sequence length, class weighting or sampling strategy, and early-stopping details. These omissions do not undermine the central result, but addressing them would make the work easier to reproduce.

## Overall assessment

The paper presents a useful and technically coherent extension of interpretable EHR modeling. The empirical results are consistent across two large ICU datasets, the time-decay ablation supports the proposed mechanism, and the contribution is relevant to both clinical machine learning and irregular time-series modeling. The main weaknesses concern methodological detail, baseline comparability, the limits of attention-based interpretation, and the absence of clinical utility analysis. These are important opportunities for clarification and strengthening but do not invalidate the central contribution.

## Final recommendation

**Accept**

The work is sufficiently sound, relevant, and clearly presented for acceptance, with recommended revisions addressing preprocessing/leakage details, baseline tuning, statistical reporting, reproducibility, and more cautious interpretation of attention weights.