## Review

### Summary

This paper proposes TimeWarn, an attention-based model for early sepsis prediction that incorporates variable-specific elapsed time through a learned exponential decay. The model is evaluated on MIMIC-IV and eICU and is reported to outperform qSOFA, logistic regression, XGBoost, GRU-D, and RETAIN. The problem is clinically important, and explicitly modeling irregular sampling is relevant to EHR prediction. However, the manuscript does not provide enough methodological detail to establish that the reported gains are reliable, clinically meaningful, or free from label and temporal leakage.

### Strengths

- Addresses an important clinical prediction problem.
- Recognizes the irregular sampling structure of EHR data.
- Evaluates on two widely used ICU datasets.
- Includes both time-aware and interpretable baselines.
- Reports AUROC, AUPRC, multiple seeds, an ablation, and a longer lead-time analysis.
- The manuscript is generally well organized and readable.

### Major concerns

1. **Insufficient definition of the prediction task and cohort construction.**  
   The manuscript does not specify the observation window, the exact prediction time points, handling of patients with multiple ICU stays, exclusion criteria, censoring, or how prediction windows are sampled. These details can substantially affect sepsis results.

2. **Potential label leakage.**  
   Sepsis-3 labels involve suspected infection, antibiotics, cultures, and organ dysfunction. Several of these signals can be recorded close to or after clinical recognition. The paper must clearly state which variables are available at prediction time and how measurements occurring after onset, treatment, or recognition are excluded. This is particularly important because lactate and other organ-dysfunction variables may directly overlap with the label construction.

3. **Ambiguity in the proposed time representation.**  
   Measurements are grouped into hourly windows, but the paper does not explain whether Δ refers to the exact timestamp of the last measurement, the window boundary, or the time since the previous nonmissing observation. It is also unclear how variables never previously observed are handled, whether Δ is capped, and whether the learned parameters are constrained to produce meaningful decays.

4. **Weakly supported interpretability claims.**  
   Attention weights are treated as explanations, but attention is not necessarily a faithful measure of causal or predictive importance. The paper provides no faithfulness tests, perturbation analysis, counterfactual evaluation, or comparison with feature attribution methods. Reporting that lactate and respiratory rate receive high attention is also not sufficient to establish interpretability.

5. **Incomplete and potentially unfair baseline comparison.**  
   Baselines use hyperparameters from their original papers, whereas TimeWarn is tuned separately on each dataset. This may disadvantage the baselines. The manuscript should report tuning procedures, preprocessing, input representations, and training details for every model. In particular, the advantage over GRU-D is modest and requires stronger experimental controls.

6. **Limited statistical analysis.**  
   Mean and standard deviation over five seeds are reported, but no confidence intervals, paired tests, bootstrap comparisons, or per-patient evaluation details are given. It is therefore unclear whether improvements of 0.013–0.016 AUROC are statistically reliable. Logistic regression has zero standard deviation, which is expected if it is deterministic, but this should be explained.

7. **Insufficient reproducibility.**  
   Important details are missing, including the precise 32 variables, normalization and imputation procedures, sequence length, handling of missingness, class weighting or sampling, architecture dimensions beyond hidden size, dropout values, decay initialization, optimization schedule, and the exact sepsis-label implementation.

8. **Clinical significance is not established.**  
   The retrospective discrimination results do not demonstrate that the model improves treatment timing or outcomes. The paper appropriately acknowledges this limitation, but the claims should be more restrained, particularly given the likely dataset and label biases.

### Minor concerns

- The related-work section is too brief and lacks full citations for the methods and datasets.
- The manuscript should report calibration, sensitivity at clinically relevant alert rates, and possibly decision-curve or workload analyses.
- AUPRC should be interpreted relative to each dataset’s prevalence.
- The attention analysis should include confidence intervals, subgroup analyses, and comparisons with negative or false-positive predictions.
- The conclusion somewhat overstates the evidence for clinical interpretability.

## Scores

| Criterion | Score (0–100) |
|---|---:|
| Soundness | 42 |
| Novelty | 55 |
| Significance | 62 |
| Clarity | 67 |

**Final average:** \((42 + 55 + 62 + 67) / 4 = 56.5\)

## Final recommendation: **Reject**

The topic is significant and the proposed modification is plausible, but the current manuscript lacks the methodological and experimental detail needed to validate the central claims. A substantially revised version would need rigorous leakage controls, a precise cohort and task definition, fair baseline tuning, stronger statistical evaluation, and more appropriate validation of the interpretability claims.