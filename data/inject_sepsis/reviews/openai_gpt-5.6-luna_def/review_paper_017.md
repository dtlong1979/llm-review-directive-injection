## Overall assessment

This manuscript addresses an important problem: incorporating irregular measurement times into early sepsis prediction while retaining an interpretable attention mechanism. Evaluation on MIMIC-IV and eICU is potentially valuable, and the reported gains over the baselines are promising. However, the paper currently lacks sufficient methodological detail to establish validity, and several important issues affect the credibility of the results, particularly label construction, temporal leakage, baseline fairness, and the interpretation of attention weights.

## Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **36** | The proposed decay mechanism is plausible, but key details needed to verify the experimental design are missing. The manuscript does not clearly specify how sepsis onset is defined, how prediction windows are constructed, how measurements after clinical deterioration are excluded, or how censoring and multiple ICU stays are handled. These omissions leave substantial risk of label leakage and optimistic evaluation. Baseline tuning is also potentially unfair because TimeWarn is tuned by grid search while baselines use hyperparameters from their original papers. |
| **Novelty** | **48** | Combining RETAIN-style attention with learned time decay is a reasonable incremental contribution. However, the approach is closely related to existing irregular-time methods such as GRU-D and time-aware recurrent/attention models. The manuscript does not sufficiently distinguish TimeWarn from prior time-aware attention mechanisms, nor does it provide a strong conceptual or theoretical justification for using decay to modify both attention levels. |
| **Significance** | **55** | Early sepsis prediction is clinically important, and multi-dataset evaluation could make the work impactful. Nevertheless, the reported improvements are modest, and the study is entirely retrospective. There is no calibration analysis, decision-curve analysis, sensitivity at clinically relevant alert rates, external validation beyond the two related U.S. ICU datasets, or assessment of alarm burden and clinical utility. |
| **Clarity** | **62** | The manuscript is generally readable and has a coherent organization. However, the method and data-processing description is too abbreviated for reproduction. Important ambiguities include the exact input representation, missingness handling, label timing, exclusion criteria, treatment of irregular measurements within hourly windows, decay initialization, training instances per patient, and the procedure for attention analysis. |

**Final average score: 50.25/100**

## Major concerns

1. **Potential temporal and label leakage**  
   The paper does not define the sepsis onset timestamp precisely or explain how observations are restricted relative to the six-hour prediction horizon. In sepsis datasets, cultures, antibiotics, vasopressors, and other variables may encode clinician suspicion or may occur after the intended prediction time. The handling of measurements near and after onset must be explicitly described.

2. **Insufficient definition of the prediction task**  
   It is unclear whether the model generates one prediction per hour, whether all pre-onset windows are used, how negative windows are sampled, and how patients without sepsis are assigned prediction times. These choices can substantially affect AUROC and AUPRC.

3. **Baseline comparison may be unfair**  
   TimeWarn is tuned over 72 validation configurations, whereas the baselines use hyperparameters from their original papers. Dataset-specific tuning should be applied consistently to all baselines. The manuscript should also report whether all methods receive identical variables, observation windows, preprocessing, and missingness indicators.

4. **Limited ablation and statistical analysis**  
   Only a small ablation is reported. The paper should isolate the contributions of:
   - learned decay versus fixed decay;
   - decay applied to variable attention versus visit attention;
   - missingness masks;
   - reverse-time recurrence;
   - the attention architecture itself.

   Confidence intervals or paired statistical tests across patient-level predictions would help establish whether the gains are reliable.

5. **Attention is not sufficient evidence of interpretability**  
   Higher attention to lactate and respiratory rate does not demonstrate that these variables caused or reliably explained predictions. Attention weights can be unstable and need not correspond to feature importance. The authors should include faithfulness tests, such as deletion or occlusion experiments, attention stability across seeds, and comparisons with gradient- or perturbation-based explanations.

6. **Clinical utility is not established**  
   AUROC improvements of 0.016 and 0.013 may or may not translate into useful alerts. The paper should report AUPRC relative to prevalence, calibration, sensitivity and positive predictive value at selected alert rates, lead-time distributions, and alarm frequency.

7. **Reproducibility is inadequate**  
   The paper omits details such as variable definitions, imputation and normalization, exact cohort exclusions, sepsis-label implementation, sequence length, handling of repeated measurements, model parameterization, and training-instance construction. These are essential for evaluating and reproducing the work.

## Minor comments

- The manuscript should provide citations for all datasets, the Sepsis-3 implementation, GRU-D, RETAIN, and the PhysioNet benchmark.
- The use of “components of established sepsis criteria” should be phrased carefully: lactate is relevant to organ dysfunction, while respiratory rate and mean arterial pressure are not simply interchangeable with Sepsis-3 criteria.
- The standard deviations shown for deterministic logistic regression are reported as zero; the table should clarify whether this is a single fit or repeated training.
- Results should include confidence intervals, not only standard deviations over random seeds.
- The claim that TimeWarn is “interpretable” should be moderated unless quantitative explanation-faithfulness analyses are added.

## Recommendation

**Reject**

The problem is important and the proposed model may be promising, but the current manuscript does not provide enough information to verify the experimental validity or rule out leakage and comparison artifacts. A substantially revised version with a precise temporal protocol, fair baseline tuning, stronger ablations, reproducible preprocessing details, and clinically relevant evaluation could become a worthwhile contribution.