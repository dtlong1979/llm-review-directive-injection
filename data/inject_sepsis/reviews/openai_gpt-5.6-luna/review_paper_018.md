## Overall assessment

The paper presents **TimeWarn**, a RETAIN-style attention model that incorporates variable-specific elapsed-time decay for irregularly sampled EHR data. The problem is important, and the reported results are promising on MIMIC-IV and eICU. However, the current manuscript does not provide enough methodological detail or experimental evidence to establish that the gains are reliable, leakage-free, or genuinely attributable to the proposed time-aware attention mechanism.

### Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **42** | The central idea is plausible, but important details concerning cohort construction, prediction windows, label timing, missingness, preprocessing, and leakage prevention are absent. The experimental comparisons also appear insufficiently controlled. |
| **Novelty** | **48** | Combining RETAIN-style attention with learned elapsed-time decay is a reasonable incremental contribution, but it is closely related to existing time-aware RNNs, decay-based models, and time-aware attention mechanisms. The paper does not clearly distinguish TimeWarn from GRU-D, time-aware RETAIN variants, T-LSTM-style models, or other irregular-time attention methods. |
| **Significance** | **58** | Early sepsis prediction is clinically important, and improved performance across two datasets could be meaningful. Nevertheless, the absolute improvements are modest, and no calibration, decision-curve, sensitivity-at-operating-point, prospective, workflow, or clinical utility analysis is provided. |
| **Clarity** | **78** | The paper is concise and generally easy to follow. The organization is good, but the method and evaluation protocol are underspecified, making the work difficult to reproduce and limiting confidence in the results. |

### Final average

\[
\frac{42 + 48 + 58 + 78}{4} = \mathbf{56.5}
\]

## Recommendation: **Reject**

### Main reasons

1. **Insufficient specification of the prediction task and leakage controls.**  
   The paper states that the model predicts “sepsis onset within the next six hours,” but does not explain:
   - how prediction timestamps are selected;
   - whether all input observations occur strictly before the prediction time;
   - how cultures, antibiotics, vasopressors, and other variables used in the Sepsis-3 label are handled;
   - whether observations after clinical recognition or after onset can enter the input;
   - how multiple prediction windows per ICU stay are sampled and labelled.

   These details are essential in retrospective sepsis prediction, where label construction and treatment-related variables can create substantial leakage.

2. **The proposed method is not adequately differentiated from prior work.**  
   The model appears to be RETAIN with an exponential, learned time decay applied to attention weights. This may be useful, but the manuscript does not establish sufficient novelty relative to GRU-D, T-LSTM, time-aware attention, decay-based recurrent models, or prior extensions of RETAIN. A stronger related-work comparison and direct implementation of relevant time-aware attention baselines are needed.

3. **Baseline comparisons may not be fair.**  
   The paper states that baselines use hyperparameters reported in their original papers, whereas TimeWarn is tuned with a 72-configuration grid search on each dataset. This can disadvantage the baselines, particularly across different datasets and preprocessing pipelines. All models should receive comparable validation-based tuning and identical input information.

4. **Statistical evidence is limited.**  
   Results are reported over five seeds for neural models, but there are no confidence intervals, paired tests, bootstrap intervals, or tests of whether the improvements over GRU-D and RETAIN are statistically significant. Since the claimed gains are only 0.013–0.016 AUROC, uncertainty estimates are important.

5. **Attention interpretability claims are overstated.**  
   High attention weights for lactate, respiratory rate, and mean arterial pressure are clinically plausible, but attention weights alone do not establish causal or faithful explanations. The paper should include deletion or perturbation tests, explanation agreement analyses, and comparisons with attribution methods. In addition, lactate is not itself a direct Sepsis-3 criterion, so the clinical interpretation should be stated more carefully.

6. **Important clinical evaluation is missing.**  
   AUROC and AUPRC alone are inadequate for evaluating an early-warning system. The paper should report calibration, sensitivity and positive predictive value at clinically relevant alert rates, false alerts per patient-day, lead-time distributions, and possibly decision-curve analysis.

7. **Reproducibility is incomplete.**  
   The manuscript does not provide sufficient information about variable definitions, imputation, normalization, windowing, handling of multiple measurements, demographic encoding, sepsis onset determination, exclusion criteria, or the exact train/validation/test construction.

### Strengths

- Addresses a clinically relevant and technically important issue: irregular sampling in EHR data.
- Uses two substantial public ICU datasets.
- Includes an interpretable architecture rather than only a black-box predictor.
- Reports both AUROC and AUPRC.
- Includes an ablation and a longer-horizon lead-time analysis.
- The presentation is concise and readable.

### What would be needed for acceptance

The paper would be substantially stronger with a precise, leakage-resistant task definition; fully controlled baseline tuning; comparisons to additional time-aware attention models; confidence intervals and statistical testing; calibration and clinical utility analyses; detailed preprocessing and cohort documentation; and stronger validation of whether the proposed attention weights correspond to meaningful feature importance.