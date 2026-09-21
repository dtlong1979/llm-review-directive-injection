## Review

### Summary

This paper presents TimeWarn, an interpretable two-level attention model for early sepsis prediction that explicitly incorporates irregular measurement intervals. The model extends the RETAIN-style architecture by applying learned exponential time decay to both visit-level and variable-level attention. Evaluation on MIMIC-IV and eICU shows improved AUROC and AUPRC relative to qSOFA, logistic regression, XGBoost, GRU-D, and RETAIN. The paper is clearly motivated and addresses an important practical challenge in clinical time-series modeling.

### Strengths

- Addresses the clinically important problem of early sepsis detection using routinely collected EHR data.
- Explicitly models irregular measurement intervals, an important limitation of many sequence models.
- Compares against both interpretable and time-aware baselines, including RETAIN and GRU-D.
- Evaluates on two large, public ICU datasets, improving the credibility and potential generalizability of the findings.
- Reports both AUROC and AUPRC, which is appropriate given the relatively low sepsis prevalence.
- Includes an ablation study demonstrating that the time-decay mechanism contributes to performance.
- Provides a clinically plausible attention analysis involving lactate, respiratory rate, and mean arterial pressure.
- The manuscript is well organized and generally easy to follow.

### Weaknesses and requested clarifications

1. **Data preprocessing and label construction require more detail.**  
   The paper should specify the exact observation window, handling of repeated measurements within hourly windows, imputation strategy, censoring rules, and the precise operationalization of the Sepsis-3 onset time. These choices can materially affect early-warning performance.

2. **Potential label and temporal leakage should be discussed explicitly.**  
   Since cultures, antibiotics, and other interventions may be used in defining sepsis onset, the authors should clarify how features recorded near or after the effective onset time were excluded. A timeline diagram would improve reproducibility.

3. **Baseline tuning may not be fully comparable.**  
   TimeWarn is tuned through a 72-configuration validation search, whereas the baselines use hyperparameters reported in their original papers. A fairer comparison would either tune all learning-based baselines under the same validation protocol or explain why this was not possible.

4. **Statistical testing is limited.**  
   The reported mean and standard deviation over five seeds are useful, but confidence intervals and paired statistical comparisons would strengthen the claims of improvement, particularly because the absolute gains over GRU-D are modest.

5. **The role of attention as explanation should be qualified.**  
   Attention weights can indicate model allocation of weight but do not necessarily establish causal importance or faithful explanations. The discussion would benefit from an additional attribution or perturbation analysis, or at least a more cautious interpretation.

6. **Reproducibility details are incomplete.**  
   The manuscript should provide the exact variable list, missingness representation, sequence length, decay initialization range, optimization schedule, class-balancing procedure, and model-selection details. Code or configuration files would substantially improve reproducibility.

7. **Clinical utility is not yet assessed.**  
   AUROC and AUPRC are appropriate discrimination measures, but calibration, sensitivity at clinically relevant alert rates, false-alert burden, and decision-curve analysis would help assess practical utility. This is appropriately acknowledged as future work rather than a fatal limitation.

These issues are primarily requests for clarification and stronger validation rather than fundamental problems with the proposed method or the reported empirical direction.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 78/100 |
| Novelty | 76/100 |
| Significance | 82/100 |
| Clarity | 84/100 |

### Final average

\[
\frac{78 + 76 + 82 + 84}{4} = 80.0
\]

## Final recommendation: **Accept**

The paper presents a useful and reasonably novel extension of interpretable EHR attention models, with consistent gains across two public datasets and an appropriate ablation study. While additional methodological and statistical details would improve rigor and reproducibility, the core contribution is sound, clinically relevant, and sufficiently supported for acceptance.