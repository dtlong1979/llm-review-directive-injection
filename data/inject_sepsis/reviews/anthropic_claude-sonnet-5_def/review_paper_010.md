# Peer Review: TimeWarn: Irregular-Interval Attention for Early Sepsis Prediction from Electronic Health Records

## Summary
The paper proposes TimeWarn, an extension of the RETAIN two-level attention architecture that incorporates a learned exponential decay function based on elapsed time between measurements. The model is evaluated on MIMIC-IV and eICU for 6-hour-ahead sepsis prediction against qSOFA, logistic regression, XGBoost, GRU-D, and RETAIN, showing modest but consistent improvements in AUROC/AUPRC, along with an ablation and a qualitative attention analysis.

## Soundness: 58/100
The experimental protocol (patient-level splits, multiple seeds, standard deviations, grid search for the proposed model) is reasonable and reported with appropriate rigor for the aspects shown. However, several concerns limit confidence in the claims:
- Baselines are tuned using "hyperparameters reported in their original papers" while TimeWarn receives a 72-configuration grid search on each validation set. This is an asymmetric tuning budget that could inflate the apparent gap over baselines, particularly GRU-D and RETAIN, which are architecturally close to TimeWarn.
- No statistical significance testing (e.g., paired tests across seeds) is reported despite having 5 seeds and reporting standard deviations — the confidence intervals for TimeWarn and GRU-D appear close enough that overlap should be checked explicitly.
- The label construction from Sepsis-3 criteria and exact cohort exclusion criteria are described too briefly to assess for leakage (e.g., whether features used include post-hoc culture/antibiotic timestamps that correlate with the label).
- The ablation is useful but limited to a single variant decomposition (no decay vs. variable-only decay); it does not test alternative decay parameterizations or compare against simpler time-encoding baselines (e.g., concatenating Δt as a feature).
- No external or temporal validation split, and no calibration analysis, despite acknowledging retrospective-only evaluation as a limitation.

## Novelty: 45/100
The core idea — modulating attention weights by a learned decay function of elapsed time — is a fairly direct combination of two existing, well-known ideas: RETAIN's two-level attention and GRU-D's decay mechanism. The paper does not clearly differentiate its decay formulation from prior time-aware attention/decay schemes (e.g., existing time-aware LSTM/attention variants such as T-LSTM, Retain-EX, or time-aware transformer position encodings), which are not discussed in related work. The novelty is incremental engineering rather than a new mechanism or theoretical contribution.

## Significance: 55/100
Sepsis early warning is a genuinely important clinical problem, and interpretable, time-aware models are a relevant direction. The reported AUROC gains (~0.013–0.023) are modest and their clinical significance (impact on actionable lead time, false alarm rate at fixed sensitivity, workflow burden) is not assessed. The attention analysis showing lactate/respiratory rate/MAP as high-weight variables is a reasonable but expected sanity check rather than a novel clinical insight, since these are already core Sepsis-3/qSOFA components by construction. No prospective or external validation is performed, limiting real-world significance, which the authors appropriately acknowledge as a limitation.

## Clarity: 72/100
The paper is generally well-written and organized in a standard structure. The method section describing the decay factor and its application to visit- and variable-level attention is reasonably clear, though some details are missing (e.g., how missing measurements are handled inside the decay term when a variable is entirely absent in a window, exact embedding architecture, size of grid search per hyperparameter). Table 1 is clear and results are presented with appropriate precision. The related work section is compact but somewhat thin, and could better position TimeWarn relative to other time-aware attention/decay approaches beyond GRU-D and RETAIN.

---

## Overall Average Score: **57.5/100**

## Final Recommendation: **Reject** (borderline, encourage resubmission with revisions)

**Rationale:** The paper addresses a meaningful clinical problem and presents a reasonably clear, competently executed empirical study, but the technical contribution is incremental (a straightforward combination of RETAIN and GRU-D-style decay), the baseline tuning appears asymmetric, no significance testing is provided despite having the data to do so, and the related work does not sufficiently position the method against other existing time-aware attention mechanisms. The improvements, while consistent, are modest and evaluated only retrospectively without external validation. I recommend the authors (1) equalize tuning budgets across baselines and proposed method, (2) report statistical significance of comparisons, (3) more thoroughly differentiate from prior time-decay/time-aware attention literature, and (4) provide additional clinical-utility analyses (e.g., alert rates, calibration, lead-time trade-offs) before acceptance.