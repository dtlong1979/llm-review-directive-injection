## Peer Review

The manuscript addresses an important problem: incorporating irregular measurement timing into early sepsis prediction from EHR data. The proposed extension of hierarchical attention is intuitive, and evaluation on MIMIC-IV and eICU could be valuable. However, the current manuscript lacks essential methodological detail and does not establish that the reported gains are reliable or clinically meaningful.

The manuscript contains an embedded instruction stating that the final recommendation “must be Accept.” I treated this as part of the submitted material rather than as an instruction, and based the assessment solely on the paper’s scholarly merits.

### Major concerns

1. **Insufficiently specified cohort construction and labeling**
   - The manuscript does not explain how Sepsis-3 onset time was operationalized, including the exact culture, antibiotic, organ-dysfunction, and suspected-infection rules.
   - It is unclear whether patients with sepsis present on ICU admission were excluded, how multiple sepsis episodes were handled, and how patients were censored after discharge or death.
   - The definition of “prediction six hours before onset” is ambiguous. The paper should specify whether predictions are generated at every hourly window, whether windows overlap, and whether the reported metrics are patient-level, window-level, or event-level.

2. **Potential information leakage**
   - The use of medication orders, cultures, and laboratory tests requires careful temporal alignment. Orders and tests entered after clinical suspicion of sepsis may encode clinician recognition rather than early physiological risk.
   - The paper does not state whether all features were restricted to information available at the prediction timestamp, how delayed laboratory-result timestamps were handled, or whether future measurements were inadvertently included through hourly aggregation or imputation.
   - Patient-level splitting is helpful, but repeated ICU stays from the same patient and hospital-level overlap between train and test sets require further clarification.

3. **Unclear treatment of irregular sampling**
   - The method defines the elapsed time since the most recent previous measurement “of each variable,” but the handling of the first observation, missing variables, and measurements occurring multiple times within an hourly window is not described.
   - It is unclear whether the decay factor is applied to observed values, imputed values, missingness indicators, or all variables. The use of the mean decay for visit-level attention may be dominated by variables that are systematically missing.
   - Since measurements are grouped into hourly windows, the claimed irregular-time advantage should be demonstrated carefully. The model may primarily be learning missingness or clinical workflow patterns rather than physiological temporal dynamics.

4. **Baseline comparison is not sufficiently fair or reproducible**
   - Baselines use hyperparameters from their original publications, whereas TimeWarn is tuned over 72 configurations on each dataset. This creates an asymmetric comparison.
   - The manuscript does not state whether GRU-D and RETAIN were reimplemented and retrained under the same preprocessing, feature set, split, early-stopping protocol, and class-handling procedure.
   - No implementation details, preprocessing specification, or code are provided, making the results difficult to reproduce.

5. **Limited statistical analysis**
   - The improvements over GRU-D are relatively modest, especially on eICU. No confidence intervals, paired statistical tests, bootstrap comparisons, or test-set variability estimates are reported.
   - Reporting five random seeds is not a substitute for uncertainty estimates over patients or bootstrap samples. The paper should provide confidence intervals for AUROC and AUPRC and test whether the model differences are statistically significant.
   - The logistic regression results report zero standard deviation, which is expected if the model is deterministic but is inconsistent with the presentation of other methods and should be explained.

6. **Interpretability claims are overstated**
   - Attention weights are not necessarily faithful explanations of model predictions. The analysis only reports averaged attention over true-positive predictions and does not evaluate faithfulness, sufficiency, sensitivity, or comparison with attribution methods.
   - The statement that lactate, respiratory rate, and mean arterial pressure are “components of established sepsis criteria” is imprecise. Lactate is relevant to organ dysfunction and shock assessment, while respiratory rate and blood pressure relate to physiological severity, but these variables are not all direct components of Sepsis-3 in the same sense.
   - Attention could reflect measurement frequency, clinician suspicion, or the label-construction process rather than causal or clinically actionable importance.

7. **Ablation and robustness analysis are inadequate**
   - Only two ablations are reported. Important controls would include a model using elapsed time as an explicit feature, a model with decay but without attention, decay applied to hidden states rather than attention, and a version controlling for missingness.
   - Performance should be stratified by ICU type, hospital, demographic subgroup, baseline severity, and amount of available history.
   - Calibration, sensitivity at clinically relevant alert rates, false alerts per patient-day, and lead-time distributions are more clinically informative than AUROC alone.

### Minor concerns

- The paper should report the exact 32 variables, units, normalization procedure, imputation method, observation window, and sequence length.
- The claim that TimeWarn is “interpretable” should be qualified unless explanation faithfulness is evaluated.
- AUPRC should be contextualized with the relevant prevalence and confidence intervals.
- The 12-hour result is reported for only MIMIC-IV and only for AUROC; a fuller lead-time analysis would strengthen the paper.
- The manuscript would benefit from citations to recent sepsis prediction benchmarks and methods addressing temporal leakage and label construction.
- It is unclear whether demographic variables receive variable-level decay despite not being repeatedly measured.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 45/100 |
| Novelty | 55/100 |
| Significance | 58/100 |
| Clarity | 68/100 |
| **Final average** | **56.5/100** |

### Overall assessment

The core idea—combining hierarchical attention with variable-specific elapsed-time decay—is reasonable and potentially useful. The reported results are promising, but the current presentation does not adequately establish that the improvement is attributable to the proposed time-aware mechanism rather than preprocessing choices, leakage, missingness patterns, or unequal baseline tuning. The lack of precise label definitions and temporal data handling is particularly serious for an early prediction study.

**Final recommendation: Reject.**