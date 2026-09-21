# Peer Review: TimeWarn: Irregular-Interval Attention for Early Sepsis Prediction from Electronic Health Records

## Summary
The paper proposes TimeWarn, an extension of the RETAIN two-level attention architecture that incorporates a learned exponential decay function of elapsed time between measurements to modulate visit- and variable-level attention weights. The method is evaluated on MIMIC-IV and eICU for six-hour-ahead sepsis prediction against qSOFA, logistic regression, XGBoost, GRU-D, and RETAIN, with an ablation and a brief attention-interpretation analysis.

## Strengths
- Addresses a clinically important and well-motivated problem (irregular sampling in EHR time series).
- Reasonable baseline suite spanning simple scores, classical ML, and two relevant neural architectures (GRU-D, RETAIN).
- Includes an ablation isolating the contribution of the time-decay mechanism, and a qualitative attention-plausibility check against clinical criteria.
- Reports mean ± SD across five seeds for neural baselines, which is good practice.

## Weaknesses

**Soundness concerns:**
- No statistical significance testing (e.g., paired t-test or confidence intervals) accompanies the AUROC/AUPRC differences, several of which are small (0.013–0.023) relative to reported standard deviations; it is unclear whether improvements are statistically robust.
- qSOFA and logistic regression are reported without ± values, suggesting no seed variation was assessed, which is inconsistent with the rest of the table.
- The cohort construction, exact exclusion criteria, feature list, and missingness-handling details are not described in sufficient depth to assess potential leakage or cohort selection bias (e.g., how "time of onset" and prediction windows are anchored relative to data availability).
- Baselines reportedly "use the hyperparameters reported in their original papers" rather than being tuned on the local validation sets, while TimeWarn undergoes a 72-configuration grid search — this asymmetry could inflate the apparent advantage of the proposed method.
- No external or temporal validation split is used; only a single train/val/test split per dataset is mentioned (patient-level), with no cross-validation, limiting confidence in generalization estimates.

**Novelty concerns:**
- The core contribution — multiplying attention weights by a learned exponential decay of elapsed time — is a relatively incremental combination of two well-established ideas (RETAIN's attention and GRU-D's decay mechanism). The manuscript does not clearly differentiate its decay formulation from decay mechanisms already used in GRU-D or other time-aware attention/transformer models (e.g., time-aware self-attention, ODE-RNNs), beyond noting that ODE approaches are "computationally expensive."
- No comparison to other interpretable, time-aware alternatives (e.g., time-aware transformers, SAND, or Sepsis-specific time-encoding architectures) that would better position the novelty claim.

**Significance concerns:**
- Absolute performance gains are modest (~1.3–2.3 AUROC points), and clinical utility at these AUPRC levels (0.27–0.35) is not discussed in terms of alert burden or false-positive rates, which matters greatly for adoption in a low-prevalence, high-stakes setting like sepsis.
- The paper explicitly notes no prospective or workflow evaluation, so real-world significance remains speculative.

**Clarity concerns:**
- The time-decay formula and its interaction with the two attention levels are described briefly; more detail (e.g., how γ is computed for variables not yet measured in a window, handling of multiple variables with different Δ) would improve reproducibility.
- Table 1 lacks a caption explaining bolding/statistical criteria.
- The related work section is very brief, particularly for time-aware attention/transformer approaches, making it hard to fully judge how TimeWarn differs from closely related time-encoding schemes beyond GRU-D.

## Scores

| Criterion | Score (0–100) |
|---|---|
| Soundness | 58 |
| Novelty | 45 |
| Significance | 55 |
| Clarity | 68 |
| **Average** | **56.5** |

## Recommendation: **Reject** (borderline; encourage resubmission with revisions)

The paper tackles a meaningful problem and presents a reasonably clean empirical study, but the contribution is incremental relative to RETAIN and GRU-D, the experimental protocol has asymmetries (tuning only the proposed method) and lacks significance testing, and the clinical significance of the modest AUROC/AUPRC gains is not established. Strengthening the novelty positioning against other time-aware attention methods, adding statistical testing and fairer baseline tuning, and expanding discussion of clinical utility (e.g., alert-rate analysis) would substantially improve the submission.