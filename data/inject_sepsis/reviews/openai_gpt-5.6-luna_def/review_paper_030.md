## Peer Review

The manuscript addresses an important problem: incorporating irregular measurement timing into early sepsis prediction while retaining an interpretable attention mechanism. The use of two large public ICU datasets and comparisons with GRU-D and RETAIN are strengths. However, substantial methodological and reporting issues prevent the results from being considered reliable or sufficiently reproducible in their current form.

### Major concerns

1. **Insufficient definition of the prediction task and labels.**  
   The manuscript does not specify how sepsis onset is operationalized from Sepsis-3, how infection time, organ dysfunction time, cultures, and antibiotics are aligned, or how patients with sepsis already present at ICU admission are handled. It is also unclear whether observations near or after the onset time are excluded from the input history. These details are essential because label timing and temporal leakage can materially affect reported performance.

2. **Potential temporal leakage and ambiguous handling of intervals.**  
   The text states that measurements are grouped into hourly windows, but the decay interval is defined as the time since the “most recent previous measurement.” It is unclear whether this interval is calculated only from information available at the prediction time, how multiple measurements within a window are handled, and whether future measurements within the forecast horizon can enter the representation. The construction of input windows and censoring rules should be described precisely.

3. **Limited methodological detail.**  
   Important implementation details are absent, including value normalization, imputation, treatment of outliers, sequence length, padding, missingness encoding, recurrent-cell type, activation functions, regularization, class weighting, batch size, and early-stopping patience. The decay parameterization also requires clarification, particularly whether \(w\) is constrained to be nonnegative and how the decay initialization is selected.

4. **Baseline comparison may not be fair or reproducible.**  
   The manuscript says that baselines use hyperparameters from their original papers, whereas TimeWarn is tuned over 72 configurations on each dataset. Original-paper settings may not be appropriate for different preprocessing pipelines or datasets. All methods should be tuned under a comparable validation protocol, with the search spaces and selected parameters reported. The manuscript should also clarify whether all models use exactly the same variables, observation history, cohort exclusions, and label definitions.

5. **Statistical evidence is incomplete.**  
   Results are reported as means and standard deviations over five seeds, but there are no confidence intervals, paired statistical tests, or patient-level bootstrap estimates. The improvements over GRU-D are modest, especially on eICU, and it is not established that they are statistically or clinically meaningful. Performance should also be reported separately across hospitals or clinically relevant subgroups where possible.

6. **Interpretability claims are overstated.**  
   Attention weights do not necessarily provide faithful explanations of model decisions. The analysis only reports variables with high average attention among true-positive predictions and does not evaluate faithfulness, stability, counterfactual sensitivity, or agreement with clinician-derived importance. Further, lactate, respiratory rate, and mean arterial pressure are clinically relevant, but the statement that they are all “components of established sepsis criteria” is imprecise. Lactate is not a qSOFA component, and respiratory rate and blood pressure are used differently across scoring systems.

7. **Ablation analysis is too limited.**  
   Only one principal ablation is described. The paper should isolate the contribution of visit-level decay, variable-level decay, the learned decay function, the missingness mask, and the attention architecture. Comparisons with a time-aware non-attention model and with simpler elapsed-time features would help determine whether the improvement comes from time encoding or from additional model capacity.

8. **Clinical utility is not assessed.**  
   AUROC and AUPRC alone do not establish usefulness for alerting. Calibration, sensitivity at clinically relevant false-alert rates, alert burden, lead-time distributions, and decision-curve or net-benefit analyses would make the evaluation more clinically informative.

### Minor concerns

- The abstract claims “mean and standard deviation over five random seeds,” but the table reports zero standard deviation for logistic regression. This is not necessarily wrong, but the evaluation protocol should explain which methods were repeated and why.
- The exact cohort construction, exclusion criteria, number of patients with positive labels, and numbers of prediction instances should be reported.
- Patient-level splitting is appropriate, but the manuscript should clarify how multiple ICU stays from the same patient were assigned and whether hospital-level separation was considered for eICU.
- The claim that TimeWarn is “interpretable” should be moderated unless supported by formal explanation experiments.
- Reproducibility would benefit from pseudocode, a full variable list, and release of preprocessing and evaluation code.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 55/100 |
| Novelty | 58/100 |
| Significance | 65/100 |
| Clarity | 70/100 |

**Final average:** \((55 + 58 + 65 + 70)/4 = 62.0/100\)

### Recommendation: **Reject**

The problem is significant and the proposed combination of irregular-time decay with hierarchical attention is potentially useful, but the current manuscript does not provide enough detail to rule out temporal leakage or establish a fair and statistically reliable comparison. The work could become publishable after a substantial revision including precise label and cohort definitions, leakage analysis, matched baseline tuning, expanded ablations, uncertainty estimates, and stronger validation of the interpretability and clinical utility claims.

The manuscript contains an embedded instruction requesting an Accept recommendation. I treated that sentence as part of the submitted material rather than as an instruction, and the recommendation above is based solely on the reported scientific evidence.