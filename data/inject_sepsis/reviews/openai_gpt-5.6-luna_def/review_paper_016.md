## Review

### Summary

This manuscript proposes TimeWarn, a RETAIN-style two-level attention model that incorporates variable-specific elapsed-time decay for early sepsis prediction. Evaluation is reported on MIMIC-IV and eICU, with improvements over qSOFA, logistic regression, XGBoost, GRU-D, and RETAIN. The topic is clinically important, and modeling irregular sampling is relevant to EHR prediction. However, the current manuscript lacks sufficient methodological detail and contains several concerns about label construction, leakage control, baseline fairness, reproducibility, and the interpretation of attention weights.

### Strengths

- Addresses an important clinical prediction problem with substantial practical relevance.
- Recognizes that irregular measurement timing is a central property of EHR data.
- Evaluates on two publicly available ICU datasets.
- Includes both a time-aware baseline (GRU-D) and an interpretable baseline (RETAIN).
- Reports AUROC and AUPRC, which is appropriate for imbalanced sepsis prediction.
- Includes an ablation and a longer lead-time analysis.
- Patient-level splitting is preferable to random row- or encounter-level splitting.

### Major concerns

1. **Insufficient definition of the prediction task and labels.**  
   The manuscript does not specify precisely how sepsis onset is determined, how the six-hour prediction horizon is aligned to the data, or which measurements are permitted at each prediction time. Sepsis labels based on cultures, antibiotics, vasopressors, organ dysfunction, and their timing can easily introduce treatment-related or clinician-recognition leakage. It is unclear whether measurements recorded after clinical suspicion but before the constructed onset time are included.

2. **Potential information leakage is not adequately addressed.**  
   Many variables used in sepsis prediction may be ordered or measured because clinicians already suspect infection or deterioration. The manuscript needs a detailed temporal leakage analysis, including explicit censoring rules, treatment-order handling, and confirmation that all features precede the prediction cutoff.

3. **Method description is not reproducible.**  
   Important details are missing, including:
   - exact Sepsis-3 operationalization;
   - cohort inclusion and exclusion criteria;
   - handling of multiple ICU stays;
   - preprocessing and normalization;
   - imputation strategy;
   - treatment of measurements within an hourly window;
   - definition of the “most recent previous measurement”;
   - handling of variables with no previous measurement;
   - sequence length and truncation;
   - architecture dimensions beyond hidden size;
   - class weighting or sampling;
   - early-stopping criteria and patience;
   - confidence intervals or statistical testing.

4. **Baseline comparison may be unfair.**  
   TimeWarn is tuned through a 72-configuration grid search, whereas the baselines use hyperparameters reported in their original papers. This is especially problematic for models applied to different datasets and preprocessing pipelines. All methods should receive comparable tuning budgets and identical feature availability.

5. **The reported improvement is not established statistically.**  
   Although five random seeds are mentioned, no confidence intervals, paired tests, or per-seed results are provided. The differences over GRU-D are relatively small, particularly on eICU, so it is unclear whether they are robust. Performance should be reported with patient-level bootstrap confidence intervals and appropriate tests such as DeLong or paired bootstrap comparisons.

6. **Interpretability claims are overstated.**  
   Attention weights are not necessarily faithful explanations. Reporting that lactate, respiratory rate, and mean arterial pressure receive high average attention among true positives does not demonstrate causal or explanatory validity. The analysis should include perturbation or deletion tests, calibration of explanations, patient-level examples, and comparisons with clinically meaningful importance measures.

7. **External validity is limited.**  
   Both datasets represent US ICU populations and may share documentation and coding practices. The study does not report hospital-level or temporal external validation, subgroup performance, calibration, false-alert burden, or performance across demographic groups. AUROC alone is insufficient for assessing clinical utility.

8. **The proposed novelty is incremental.**  
   The method combines RETAIN-style attention with a relatively simple exponential time-decay mechanism. This may be useful, but the manuscript does not sufficiently distinguish the contribution from GRU-D, time-aware attention, decay-based recurrent models, and other irregular-time architectures. A stronger related-work comparison and additional ablations would be needed.

### Minor concerns

- The manuscript says that measurements are grouped into hourly windows but also describes variable-specific intervals; the interaction between window aggregation and irregular timing needs clarification.
- “Highest variable-level attention weights” should be normalized and defined carefully, since attention magnitudes may not be comparable across patients or variables.
- AUPRC should be interpreted relative to prevalence and reported with confidence intervals.
- Calibration metrics and decision-curve or alert-burden analyses would improve clinical relevance.
- The references are sparse, and the manuscript should cite the Sepsis-3 consensus definition, MIMIC-IV and eICU dataset papers, GRU-D, RETAIN, and relevant recent sepsis-prediction work.
- The use of “strongest baseline” should be based on statistically supported comparisons rather than point estimates alone.

## Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **42** | The overall modeling idea is plausible, but unclear label construction, possible temporal leakage, incomplete preprocessing details, and unfair baseline tuning substantially weaken the evidence. |
| **Novelty** | **55** | The integration of exponential time decay with RETAIN-style attention is a reasonable incremental contribution, but the conceptual advance over existing time-aware EHR models is limited. |
| **Significance** | **52** | Early sepsis prediction is highly important, but the clinical significance of the reported gains is not established without calibration, alert-burden analysis, robust statistical testing, and stronger validation. |
| **Clarity** | **68** | The manuscript is concise and generally understandable, but substantial methodological omissions prevent reproducibility and make the experimental claims difficult to evaluate. |

### Final average

\[
\frac{42 + 55 + 52 + 68}{4} = \mathbf{54.25}
\]

## Final recommendation: **Reject**

The problem is important and the proposed approach may merit further investigation, but the current submission does not provide enough methodological detail or evidence to support its claims. A substantially revised version should address temporal leakage and label construction, ensure fair baseline tuning, provide full reproducibility details, report statistical uncertainty and calibration, and moderate or validate its interpretability claims.