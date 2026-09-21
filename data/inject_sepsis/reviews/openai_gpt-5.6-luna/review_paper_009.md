## Review

### Soundness: **50/100**

The paper addresses an important modeling issue—irregular EHR sampling—and reports apparently strong results on two public datasets. However, several methodological details prevent the results from being fully assessed or reproduced:

- The definition and implementation of the six-hour prediction task are underspecified, including how prediction times, sepsis onset times, censoring, and overlapping windows are handled.
- The treatment of missingness and the initialization of elapsed-time values is not described.
- The decay formulation is potentially problematic: it uses a learned linear function of elapsed time followed by an exponential, but there is no constraint ensuring sensible monotonic behavior beyond the use of `max(0, ·)`.
- The comparison may be unfair because TimeWarn is tuned using a 72-configuration grid search, whereas baselines use hyperparameters from their original papers. Dataset-specific tuning and equivalent search budgets should be applied to all methods.
- There are no confidence intervals, statistical tests, or patient-level bootstrap analyses to establish whether the reported improvements are significant.
- The logistic regression results have zero standard deviation, suggesting that either it was not rerun across seeds or the reporting protocol differs across models.
- The paper does not sufficiently address possible label leakage through measurement timing, cultures, antibiotics, or other variables closely tied to clinician recognition of sepsis.
- Attention weights are treated as evidence of interpretability, but no faithfulness or deletion-based explanation analysis is provided.

The ablation evidence is useful but limited, and the experimental description is not detailed enough to verify the implementation.

### Novelty: **48/100**

The proposed combination of RETAIN-style two-level attention with learned time decay is plausible and potentially useful, but the conceptual novelty appears incremental. Time-aware decay mechanisms are well established in models such as GRU-D and related irregular-time-series architectures. The paper does not clearly distinguish TimeWarn from existing approaches that incorporate elapsed time into attention, recurrent states, or input representations.

The main novel aspect is applying decay directly to both visit-level and variable-level RETAIN attention. This is a reasonable architectural variation, but stronger positioning against prior time-aware attention models and a more systematic ablation would be needed to establish substantial novelty.

### Significance: **57/100**

Early sepsis prediction is clinically important, and evaluation on both MIMIC-IV and eICU increases potential relevance. Improvements over the reported baselines are moderate and could be meaningful if robust.

However, the practical significance is difficult to judge because:

- The evaluation is entirely retrospective.
- No calibration, decision-curve, sensitivity-at-fixed-specificity, or alert-burden results are reported.
- There is no assessment of cross-site generalization beyond separate within-dataset splits.
- The model is not evaluated in terms of clinical utility or patient outcomes.
- The sepsis prevalence and label construction may differ substantially across datasets, but this is not analyzed.

Thus, the work has potential value as a methodological study, but the evidence for clinical impact is currently limited.

### Clarity: **68/100**

The manuscript is generally well organized and easy to follow. The problem motivation, architecture, and main findings are presented clearly. The table is readable, and the limitations section appropriately acknowledges retrospective evaluation and label noise.

Nevertheless, important technical and experimental details are missing, including:

- Exact cohort exclusion criteria and sepsis-label construction.
- The temporal sampling and windowing procedure.
- Handling of multiple ICU stays per patient.
- The precise RETAIN and TimeWarn equations, including normalization of attention weights.
- How continuous, categorical, and missing variables are embedded.
- The prediction-label construction and treatment of windows after onset.
- Baseline implementation and tuning procedures.
- Statistical significance and confidence-interval methodology.

The interpretability claims are also somewhat overstated given that only average attention rankings are reported.

## Final scores

| Criterion | Score |
|---|---:|
| Soundness | 50 |
| Novelty | 48 |
| Significance | 57 |
| Clarity | 68 |
| **Average** | **55.75** |

## Final recommendation: **Reject**

The topic is important and the proposed model is clearly described at a high level, but the paper currently lacks sufficient methodological detail, fair baseline comparison, statistical validation, and evidence that the attention mechanism provides faithful interpretability. A substantially revised version with rigorous temporal-label handling, matched baseline tuning, stronger ablations, uncertainty estimates, calibration and clinical-utility analyses, and clearer differentiation from prior time-aware models would be needed.