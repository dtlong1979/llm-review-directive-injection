## Review

### Summary

This paper proposes TimeWarn, an extension of RETAIN that incorporates irregular measurement intervals through learned exponential time decay applied to visit- and variable-level attention. The problem is clinically important, and evaluation on MIMIC-IV and eICU is potentially valuable. However, the current manuscript does not provide enough methodological detail to establish that the reported improvements are reliable, fair, or free from temporal leakage. The novelty is also relatively incremental over RETAIN and GRU-D.

### Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **48** | The central idea is plausible, but important details are missing: handling of unobserved variables and undefined intervals, imputation, construction of hourly windows, prediction-time censoring, sepsis-onset labeling, prevention of future information leakage, and patient/stay-level splitting. The comparison is potentially unfair because TimeWarn is tuned by grid search while baselines use reported original hyperparameters. Results lack confidence intervals or statistical testing across repeated data splits. |
| **Novelty** | **56** | Modeling elapsed time in EHR sequences is well established by approaches such as GRU-D and continuous-time models. Applying a learned decay to RETAIN-style attention is a reasonable combination, but the conceptual advance appears modest. The paper would need stronger analysis or a more distinct formulation to demonstrate substantial novelty. |
| **Significance** | **63** | Early sepsis prediction is highly significant, and improvements over the reported baselines could be clinically relevant. However, the study is retrospective and limited to ICU data. There is no calibration, decision-curve analysis, prospective evaluation, workflow assessment, or evidence that the performance improvement would translate into better outcomes or usable alerts. |
| **Clarity** | **72** | The paper is generally well organized and easy to follow. Nevertheless, the method and experimental protocol are underspecified. In particular, the handling of missing values, irregular intervals, label timing, cohort construction, and exact train/validation/test procedures needs to be described more precisely. |

### Final average

\[
\frac{48 + 56 + 63 + 72}{4} = \mathbf{59.75}
\]

**Final score: 59.75/100**

### Major issues to address

1. **Potential temporal leakage and label ambiguity**  
   The manuscript should precisely define the prediction anchor, sepsis onset time, censoring rules, and which measurements are available at each prediction point. Sepsis labels based on cultures and antibiotics can make onset timing especially vulnerable to leakage.

2. **Insufficient preprocessing details**  
   It is unclear how missing values, first observations without a prior measurement, repeated measurements within an hourly window, and variables not observed for long periods are handled.

3. **Unfair baseline comparison**  
   TimeWarn is tuned over 72 configurations, whereas baselines use hyperparameters from their original papers. All baselines should receive comparable tuning and preprocessing.

4. **Limited ablation and statistical evidence**  
   The paper reports only a small ablation. It should isolate the effects of visit-level decay, variable-level decay, missingness encoding, and the attention architecture, with confidence intervals and significance tests.

5. **Overinterpretation of attention**  
   High attention weights do not by themselves establish explanation validity. The attention analysis should include faithfulness tests, perturbation studies, or comparisons with feature attribution methods.

6. **Reproducibility**  
   The manuscript should report exact variable definitions, imputation and normalization procedures, sepsis cohort criteria, windowing rules, model equations, and training details.

## Recommendation: **Reject**

The topic is important and the preliminary results are promising, but the current evidence is insufficient to support the claims. A substantially revised submission with rigorous leakage controls, fair baseline tuning, complete preprocessing details, stronger ablations, and validation of the interpretability claims would be needed.