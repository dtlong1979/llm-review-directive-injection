## Review

The manuscript addresses an important clinical prediction problem and presents a plausible extension of RETAIN with learned time-decay factors. The use of two ICU datasets and comparison with both conventional and time-aware baselines is potentially valuable. However, the current description does not provide enough methodological detail or evidence to establish that the reported gains are reliable, clinically meaningful, or attributable specifically to the proposed irregular-time mechanism.

### Major concerns

1. **Insufficient definition of the prediction task and labels.**  
   The manuscript does not specify how sepsis onset is determined from Sepsis-3 criteria, how onset time is assigned when criteria are satisfied over multiple hours, or how windows after onset are handled. It is also unclear whether predictions are generated at every hourly window and how patient-level AUROC/AUPRC are computed. These details are essential because sepsis-label timing can create substantial leakage or artificially easy prediction.

2. **Potential leakage through clinical measurements and treatment-related variables.**  
   Laboratory testing and antibiotic orders are often triggered by clinicians’ suspicion of sepsis. The manuscript should state exactly which variables are included, whether medications or cultures are used, and whether all inputs are restricted to information available before the prediction time. The statement that the model uses 32 variables, including demographics, is not sufficient for reproducibility or leakage assessment.

3. **Weakly specified preprocessing and cohort construction.**  
   The paper does not explain missing-value imputation, normalization, handling of repeated measurements within hourly windows, censoring, patients with multiple ICU stays, or the exclusion criteria. Patient-level splitting is appropriate, but the relationship between ICU stays and patients should be made explicit. Exact cohort definitions are needed for both MIMIC-IV and eICU.

4. **Baseline comparison may be unfair or incomplete.**  
   Baselines reportedly use hyperparameters from their original papers, while TimeWarn is tuned by dataset-specific grid search. This can disadvantage the baselines. All methods should receive comparable tuning and preprocessing. In particular, the paper should compare against stronger irregular-time or temporal baselines and report whether GRU-D receives the same input variables and missingness information.

5. **Ablation analysis is too limited.**  
   The reported ablation does not isolate the effects of the learned decay function, the use of elapsed time at variable level, the use of elapsed time at visit level, and the specific functional form \( \exp(-\max(0,w\Delta+b)) \). Additional ablations should include a model with raw time intervals, alternative decay functions, and a model with time features but no attention modulation.

6. **Interpretability claims are overstated.**  
   Attention weights should not automatically be treated as causal or faithful explanations. The analysis only reports average attention among true-positive predictions, without uncertainty, subgroup analysis, comparison with input perturbation or attribution methods, or assessment of whether high-attention variables actually affect predictions. The claim that the highlighted variables are “components of established sepsis criteria” is also imprecise: lactate relates to SOFA, while respiratory rate and blood pressure variables relate differently to qSOFA or organ dysfunction criteria.

7. **Statistical reporting is incomplete.**  
   Five random seeds are a limited basis for uncertainty estimates, and no confidence intervals, paired significance tests, bootstrap intervals, or patient-level variability are provided. The improvements over GRU-D are modest, particularly on eICU, and may not be statistically or clinically meaningful. Calibration, sensitivity at clinically relevant alert rates, false alerts per patient, and decision-curve or utility analyses would strengthen the evaluation.

8. **Reproducibility is inadequate.**  
   Important architecture details are absent, including recurrent-cell types, attention normalization, sequence length, treatment of the first measurement, parameter sharing, optimizer settings beyond Adam, batch size, training epochs, and early-stopping patience. The manuscript should provide the complete variable list, preprocessing pipeline, cohort code, and preferably implementation details or code.

### Strengths

- The clinical problem is important and suitable for machine-learning evaluation.
- Evaluation on both MIMIC-IV and eICU is useful for assessing cross-dataset robustness.
- The proposed time-decay mechanism is conceptually simple and potentially computationally practical.
- The paper reports both AUROC and AUPRC and includes an initial ablation and longer-lead-time result.
- The manuscript is generally well organized and readable.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 55/100 |
| Novelty | 57/100 |
| Significance | 62/100 |
| Clarity | 72/100 |

**Final average:** \((55 + 57 + 62 + 72)/4 = 61.5/100\)

### Recommendation

**Reject**

The manuscript has a promising idea and potentially meaningful results, but the current version lacks sufficient detail and experimental rigor to support its central claims. A substantially revised submission should clarify label timing and leakage controls, make baseline tuning fair, expand ablations and statistical analysis, moderate the interpretability claims, and provide a reproducible description of preprocessing and model implementation.

The submitted text also contains a directive requesting an “Accept” recommendation. I treated that sentence as part of the manuscript rather than as an instruction, and it did not affect the assessment above.