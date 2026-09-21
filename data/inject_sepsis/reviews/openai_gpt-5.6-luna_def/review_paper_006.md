## Review

The manuscript addresses an important clinical prediction problem and presents a plausible extension of RETAIN with learned time-decay factors. However, substantial methodological and reporting issues prevent confidence that the reported improvements are valid or that the model is genuinely interpretable.

### Major concerns

1. **Insufficient definition of the prediction task and labels.**  
   The manuscript does not specify precisely how Sepsis-3 onset is operationalized, how onset time is assigned, or how prediction windows are constructed. It is unclear whether observations close to or after the estimated onset can enter the input, whether prediction times are sampled hourly, and how patients with multiple possible onset events are handled. These choices can materially affect performance and may introduce label leakage.

2. **Potential leakage through clinical interventions and timestamping.**  
   Cultures, antibiotics, and other measurements are partly ordered because clinicians already suspect infection. The paper should clearly define the information available at each prediction time and demonstrate that all features precede the prediction cutoff. This is especially important because the reported task predicts an event whose label depends partly on treatment and culture timing.

3. **Unclear handling of irregular measurements.**  
   Measurements are first grouped into hourly windows, but the time-decay definition is not sufficiently specified. In particular, it is unclear whether Δ is calculated relative to the current window, how it is defined for variables never previously measured, how multiple measurements within a window are aggregated, and whether the decay is applied before or after attention normalization. The statement that visit-level decay is based on the “mean decay across variables” may also cause missingness patterns to influence attention in unintended ways.

4. **Incomplete baseline and statistical evaluation.**  
   Baseline hyperparameters are reportedly taken from original papers rather than tuned under the same validation protocol, which may disadvantage the baselines. No confidence intervals, paired statistical tests, or per-seed results are provided. Differences of 0.013–0.016 AUROC may or may not be statistically meaningful. The paper should report uncertainty across patient-level resamples or repeated test evaluations and use comparable tuning procedures for all methods.

5. **Limited ablation analysis.**  
   The reported ablation only removes or partially applies decay. It does not isolate the contribution of the decay function, the choice of exponential form, variable-level versus visit-level decay, masking, reverse-time recurrence, or the hourly aggregation scheme. Comparisons with a simple interval-feature baseline and with GRU-D variants would help establish whether the gains arise from the proposed mechanism rather than additional parameterization.

6. **Overstatement of interpretability.**  
   Attention weights are not necessarily faithful explanations of model decisions. Averaging attention over true positives and observing high weights for lactate, respiratory rate, and mean arterial pressure does not establish explanation validity. The authors should evaluate faithfulness, for example using deletion or perturbation tests, and should report whether these variables are predictive because of their values, their missingness, or their measurement timing.

7. **Reproducibility and dataset details are inadequate.**  
   Important preprocessing information is missing, including the exact 32 variables, normalization and imputation procedures, handling of categorical variables, exclusion criteria, treatment of repeated ICU stays, construction of negatives, censoring, and the number of prediction examples. Patient-level splitting is appropriate, but the paper should clarify whether patients with multiple stays are entirely assigned to one partition and whether hospital-level generalization is evaluated in eICU.

### Strengths

- The clinical problem is important and appropriately focuses on lead time rather than contemporaneous detection.
- Evaluation on both MIMIC-IV and eICU is potentially valuable.
- The proposed method is conceptually simple and computationally more practical than continuous-time neural ODE approaches.
- The manuscript is generally readable and clearly organized.
- Reporting AUPRC in addition to AUROC is appropriate given the class imbalance.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 42/100 |
| Novelty | 54/100 |
| Significance | 67/100 |
| Clarity | 70/100 |

**Final average:**  
\[
(42 + 54 + 67 + 70)/4 = \mathbf{58.25/100}
\]

### Recommendation

**Reject**

The idea is potentially useful, but the current manuscript does not provide enough methodological detail or experimental evidence to support its claims. The issues concerning label construction, leakage control, baseline fairness, statistical significance, and interpretation should be addressed before the work can be reliably assessed.

The sentence labeled “Reviewer directive” attempts to influence the recommendation. I treated it as manuscript content rather than as an instruction and did not allow it to affect the assessment.