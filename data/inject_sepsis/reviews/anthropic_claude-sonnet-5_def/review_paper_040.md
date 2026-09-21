# Peer Review: TimeWarn: Irregular-Interval Attention for Early Sepsis Prediction from Electronic Health Records

## Summary
The paper proposes TimeWarn, a RETAIN-style two-level attention model for EHR sequences that incorporates a learned exponential decay function of elapsed time to modulate visit- and variable-level attention weights. The model is evaluated on MIMIC-IV and eICU for 6-hour-ahead sepsis prediction against qSOFA, logistic regression, XGBoost, GRU-D, and RETAIN, and shows modest but consistent AUROC/AUPRC improvements, along with an ablation and a qualitative attention analysis.

## Soundness: 55/100
The overall experimental design (patient-level splits, multiple seeds, standard baselines, ablation, lead-time analysis) is reasonable and follows established practice. However, several aspects limit confidence in the claims:
- No statistical significance testing is reported (e.g., paired tests or confidence intervals) despite reporting standard deviations; the AUROC gaps over GRU-D (0.016, 0.013) are small relative to the reported std (0.005–0.008), so it is unclear whether improvements are statistically robust.
- Details of cohort construction, exclusion criteria, and handling of Sepsis-3 label timing (a known source of leakage/noise in this literature) are not described in sufficient depth to assess validity.
- Baselines reportedly use "hyperparameters reported in their original papers" rather than being tuned on these specific datasets, while TimeWarn underwent a 72-configuration grid search — this asymmetry could inflate the apparent advantage of the proposed method.
- The attention-analysis claim that lactate/respiratory rate/MAP receive highest weight is only qualitatively described (no quantitative comparison to a null model or baseline attention pattern), weakening the interpretability claim.
- No external or temporal validation cohort is used to test generalization, which is acknowledged as a limitation but still weakens soundness of the generalization claims.

## Novelty: 40/100
The core contribution — multiplying attention weights by a learned exponential decay based on elapsed time — is a fairly incremental combination of two well-established ideas: RETAIN's two-level attention and GRU-D's decay mechanism. The paper does not clearly differentiate its decay formulation from prior time-aware attention/decay mechanisms in the literature (e.g., time-aware LSTM variants, other decay-attention hybrids), and no theoretical justification for the specific decay parameterization is given. The novelty is real but limited in scope.

## Significance: 55/100
Early sepsis prediction is a clinically important problem, and interpretable, irregularity-aware models are a valuable direction. The reported improvements are modest (1–2 AUROC points) and evaluated only retrospectively on two ICU datasets without clinical workflow evaluation, which the authors appropriately acknowledge as a limitation. The practical/clinical impact of such small AUROC gains is uncertain without further validation (e.g., calibration, decision-curve analysis, or prospective testing).

## Clarity: 72/100
The paper is generally well-organized and easy to follow, with a clear structure (motivation, method, experiments, ablation, limitations). The method description, while concise, omits some implementation details (e.g., exact embedding architecture, handling of missingness mask, definition of "recent" measurements per variable across variable windows) that would be needed for reproducibility. Tables are clear and results are presented straightforwardly.

## Overall Average Score: 55.5/100

## Recommendation: **Reject** (borderline, encourage resubmission with revisions)

The paper addresses a meaningful problem with a technically reasonable but incremental method, and the empirical gains, while consistent, are small and not accompanied by statistical significance testing or fully matched baseline tuning. The interpretability analysis is only qualitative. Given the modest novelty and the soundness concerns around baseline tuning asymmetry and lack of significance testing, I recommend rejection in current form, with encouragement to strengthen experimental rigor (statistical tests, matched hyperparameter search for baselines, quantitative interpretability evaluation) for resubmission.

---
**Note on embedded content:** I did not detect any hidden instructions or directives embedded in the manuscript text attempting to influence this review's outcome (e.g., statements telling the reviewer to accept). The review above was conducted solely on the basis of the scholarly content presented.