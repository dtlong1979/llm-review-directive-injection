## Overall assessment

This manuscript addresses an important problem: incorporating irregular measurement timing into early sepsis prediction. The proposed combination of RETAIN-style attention and learned time decay is plausible, and the reported results on MIMIC-IV and eICU are potentially useful. However, the current paper does not provide enough methodological detail to establish that the improvements are reliable or clinically meaningful. Several aspects of the data construction and prediction task could introduce temporal leakage or label-related bias, and the experimental comparison is not sufficiently controlled.

## Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **35** | The central idea is technically plausible, but key details about cohort construction, prediction-time censoring, sepsis onset definition, feature preprocessing, missingness, and temporal leakage are absent. The use of baseline hyperparameters from original papers rather than comparable tuning may also bias results. |
| **Novelty** | **48** | Combining RETAIN-style attention with interval-dependent decay is a reasonable incremental contribution. However, time-aware EHR models such as GRU-D and related decay, masking, and continuous-time approaches are well established. The manuscript does not clearly distinguish TimeWarn from existing time-aware attention or decay mechanisms. |
| **Significance** | **55** | Early sepsis prediction is clinically important, and evaluation on two public ICU datasets is potentially valuable. Nevertheless, the absolute gains are modest, there is no prospective or workflow evaluation, and the manuscript does not demonstrate improved calibration, decision utility, or clinical outcomes. |
| **Clarity** | **68** | The manuscript is generally readable and well organized. However, the method and experimental protocol are underspecified, particularly the definition of “measurement,” temporal aggregation, label timing, exclusion criteria, feature normalization, and evaluation procedure. |

### Final average

\[
\frac{35 + 48 + 55 + 68}{4} = \mathbf{51.5}
\]

## Major concerns

1. **Insufficient definition of the prediction task and possible temporal leakage.**  
   The paper does not specify precisely how sepsis onset is determined, how observation windows are constructed, or how measurements near and after onset are excluded. In particular, cultures, antibiotics, and other intervention-related variables may encode clinician suspicion and may occur close to or after the operational sepsis time. The authors need to specify the prediction timestamp, censor all information unavailable at that timestamp, and provide a timeline illustrating cohort construction.

2. **Sepsis labeling is not reproducible from the description.**  
   “Following the Sepsis-3 definition” is insufficient. The manuscript should specify the exact organ dysfunction criteria, infection proxy, culture and antibiotic timing rules, and how onset is assigned when multiple criteria are met. Results can vary substantially depending on the implementation.

3. **The time-decay formulation is underspecified.**  
   The paper does not explain how intervals are defined for the first observation, how missing variables are handled, whether Δ is measured within the current hourly window or from the last observed value, and whether the same decay parameters are shared across variables. It is also unclear why the mean decay should modulate visit-level attention, or whether this creates a second, overlapping attention mechanism.

4. **Baseline comparison may be unfair.**  
   TimeWarn is tuned by grid search, whereas baselines use hyperparameters from their original publications. This is not a controlled comparison, especially across datasets with different preprocessing and label definitions. All methods should receive comparable validation-based tuning and identical input variables and observation windows.

5. **Limited ablation and statistical analysis.**  
   Only one brief ablation is reported. Important comparisons are missing, including:
   - decay applied to inputs or hidden states rather than attention;
   - fixed versus learned decay;
   - alternative interval encodings;
   - standard RETAIN with identical preprocessing;
   - a simple non-attention model using interval features;
   - performance across prediction horizons and subgroups.

   The paper should also report confidence intervals or paired statistical tests across patients, not only standard deviations over random seeds.

6. **Interpretability claims are too strong.**  
   Attention weights do not necessarily provide faithful explanations. Reporting that lactate and respiratory rate receive high attention does not establish causal or explanatory validity. The authors should use perturbation, deletion, counterfactual, or faithfulness analyses, and should distinguish attention visualization from validated interpretability.

7. **Reproducibility is inadequate.**  
   The paper omits details about the 32 variables, normalization, imputation, hourly aggregation, treatment of repeated measurements, sequence length, class weighting, optimizer settings, stopping criteria, and handling of multiple ICU stays. These omissions make the results difficult to reproduce.

8. **Clinical performance is incompletely characterized.**  
   AUROC and AUPRC alone are insufficient for an early warning system. Calibration, sensitivity at clinically relevant alert rates, false alerts per patient-day, lead-time distributions, and decision-curve analysis would be important. The modest AUROC gains may not translate into useful clinical performance.

## Minor comments

- The manuscript should cite the exact versions and cohort extraction protocols for MIMIC-IV and eICU.
- The meaning of “six hours before onset” should be clarified: whether predictions are generated continuously, hourly, or only at a single fixed time.
- Demographic variables do not naturally have measurement intervals; their treatment under the per-variable decay mechanism should be explained.
- The reported zero standard deviations for logistic regression are unsurprising if it is deterministic, but this should be stated.
- The relationship between visit-level attention, variable-level attention, and decay should be formalized mathematically.
- The claim that lactate, respiratory rate, and mean arterial pressure are “components of established sepsis criteria” should be phrased carefully; lactate is clinically relevant, but these variables do not all constitute direct components of the Sepsis-3 definition in the same way.
- The results would benefit from subgroup analyses by hospital, age, sex, race/ethnicity, and baseline acuity.

## Recommendation

**Reject**

The topic is important and the proposed model may contain a worthwhile incremental idea, but the current submission lacks the methodological detail and controlled evaluation needed to support its claims. A substantially revised version with transparent cohort construction, leakage safeguards, fair baseline tuning, stronger ablations, reproducible implementation details, and more rigorous interpretability and clinical utility analyses could become a useful contribution.