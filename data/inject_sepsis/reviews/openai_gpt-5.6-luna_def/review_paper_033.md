## Overall assessment

The manuscript presents TimeWarn, an extension of RETAIN that incorporates variable-specific elapsed-time decay into visit- and variable-level attention for early sepsis prediction. The clinical problem is important, and evaluating on MIMIC-IV and eICU is potentially valuable. However, the current manuscript lacks sufficient methodological detail to establish that the reported gains are reliable or that the model is fairly compared with existing methods. Several important issues concern label construction, temporal leakage, baseline tuning, evaluation methodology, and the interpretation of attention weights.

## Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **45** | The proposed mechanism is plausible, but essential details are missing. The manuscript does not clearly define prediction-time sampling, the exact Sepsis-3 label construction, handling of measurements near or after onset, censoring, missing-value imputation, or safeguards against temporal leakage. The use of baseline hyperparameters from original papers rather than comparable validation-based tuning may make the comparison unfair. Results lack confidence intervals, significance tests, and sufficient experimental details for reproducibility. |
| **Novelty** | **53** | The model is a relatively modest modification of RETAIN and GRU-D: learned elapsed-time decay is applied to attention weights. This is a reasonable engineering contribution, but similar combinations of temporal decay, irregular-time modeling, and attention have substantial precedent. The paper does not clearly distinguish its method from prior time-aware attention models or demonstrate a technically novel formulation. |
| **Significance** | **61** | Early sepsis prediction is clinically important, and cross-dataset evaluation is a strength. The reported improvements are potentially useful, but the absolute gains are modest and the study is entirely retrospective. There is no calibration, decision-curve analysis, alarm-burden analysis, subgroup analysis, or prospective/clinical utility evaluation. The evidence therefore supports predictive association rather than demonstrated clinical impact. |
| **Clarity** | **68** | The manuscript is generally readable and well organized. However, the method and experimental protocol are underspecified. Important ambiguities include how hourly windows coexist with irregular measurement intervals, how Δ is defined for the first observation and missing variables, how attention is normalized after decay, the exact 32 variables used, and the operational definition of the six-hour prediction task. The attention analysis is also presented too briefly to substantiate claims of interpretability. |

### Final average

\[
\frac{45 + 53 + 61 + 68}{4} = \mathbf{56.75}
\]

**Final average score: 56.8/100**

## Major concerns

1. **Potential temporal leakage and ambiguous label timing**  
   The paper must specify exactly which observations are available at each prediction time and how sepsis onset is determined. Culture orders, antibiotic administration, and organ dysfunction variables can occur around clinical recognition and may inadvertently reveal the label. The statement “label of sepsis onset within the next six hours” is insufficient without defining eligible prediction windows, exclusion periods, and censoring.

2. **Insufficient cohort and preprocessing detail**  
   The manuscript does not explain the exclusion criteria, treatment of repeated ICU stays, transfer events, missing values, abnormal-value filtering, timestamp alignment, or whether demographics are duplicated across hourly windows. These choices can substantially affect sepsis prediction results.

3. **Unclear integration of irregularity and hourly aggregation**  
   Measurements are grouped into hourly windows, but the model uses the time since the “most recent previous measurement.” It is unclear whether Δ is computed before aggregation, whether measurements within the same hour have separate timestamps, and how decay is assigned when a variable is not observed in a window. The phrase “mean decay across variables in the window” is also ambiguous when many variables are missing.

4. **Questionable fairness of baseline comparisons**  
   Baselines use hyperparameters from their original papers, whereas TimeWarn is tuned on each dataset. This may disadvantage the baselines. All baselines should be tuned under a consistent protocol, with preprocessing and feature availability matched across models.

5. **Limited statistical analysis**  
   Five random seeds are not sufficient to characterize uncertainty for a patient-level test set, and the table does not report variability for qSOFA or other deterministic models. Confidence intervals obtained by patient-level bootstrap, paired comparisons, and statistical tests for AUROC/AUPRC differences would strengthen the claims.

6. **Overinterpretation of attention**  
   Attention weights are not automatically faithful explanations. Averaging weights over true positives and noting that lactate and respiratory rate receive high weight does not establish causal or explanatory validity. Perturbation tests, deletion/insertion analyses, or comparison with clinically relevant feature-attribution methods are needed.

7. **Incomplete reproducibility**  
   The paper omits the exact recurrent architecture, activation functions, attention normalization, initialization, batch size, sequence length, imputation strategy, class weighting, early-stopping criterion, and full hyperparameter grids. No code or implementation details are provided.

## Recommendation

**Reject**

The problem is important and the approach may be promising, but the current submission does not provide enough methodological detail or experimental evidence to support its central claims. A substantially revised version with precise temporal labeling, leakage analysis, fair baseline tuning, stronger statistical evaluation, complete preprocessing details, and more rigorous interpretability analysis could become a valuable contribution.