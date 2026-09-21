## Review

### Summary
The paper proposes TimeWarn, an extension of RETAIN that incorporates variable-specific elapsed time through a learned exponential decay and applies this decay to both variable- and visit-level attention. It reports improved AUROC and AUPRC over qSOFA, logistic regression, XGBoost, GRU-D, and RETAIN on MIMIC-IV and eICU.

### Strengths
- Addresses a clinically relevant problem: early sepsis prediction from irregularly sampled EHR data.
- Evaluates on two widely used public ICU datasets.
- Includes both time-aware and interpretable baselines, including GRU-D and RETAIN.
- Reports both AUROC and AUPRC, which is appropriate for imbalanced outcomes.
- Includes an ablation and a longer-lead-time experiment.
- The manuscript is generally concise and readable.

### Major concerns

1. **Insufficient methodological detail**
   Critical aspects of the experimental protocol are underspecified, including:
   - Exact sepsis-label construction and onset-time definition.
   - How prediction windows, censoring, and multiple sepsis episodes are handled.
   - The precise 32 variables and their preprocessing.
   - Missing-value imputation, normalization, clipping, and measurement aggregation within hourly windows.
   - Whether measurements recorded after clinical recognition or treatment initiation can enter the input.
   - Handling of ICU discharge and variable-length sequences.
   - The exact architecture and parameterization of the recurrent networks.

   These omissions make the results difficult to reproduce and raise concerns about label leakage.

2. **Potential leakage and confounding**
   Measurement frequency, laboratory ordering, antibiotic administration, and culture collection can themselves reflect clinician suspicion of sepsis. The proposed elapsed-time features may therefore exploit care intensity or impending diagnosis rather than provide a robust physiologic signal. The paper does not clarify whether treatment-related variables or measurements obtained after recognition are excluded, nor does it discuss this issue experimentally.

3. **Limited evidence for the claimed contribution**
   The principal methodological contribution is a relatively modest combination of RETAIN-style attention with learned time decay. The comparison to GRU-D is useful, but the paper does not include stronger or more targeted ablations, such as:
   - decay applied to representations rather than attention;
   - fixed versus learned decay;
   - separate decay functions for variables;
   - time-aware RETAIN without the proposed visit-level decay;
   - models using only missingness and elapsed-time features.

   Consequently, it is difficult to determine whether the improvement comes from the proposed mechanism, additional modeling capacity, or time-related proxies.

4. **Potentially unfair baseline treatment**
   TimeWarn is tuned using a 72-configuration validation search, whereas the baselines use hyperparameters from their original publications. This is not a balanced comparison, especially across datasets with different preprocessing and outcome definitions. Baseline tuning procedures and parameter counts should be reported consistently.

5. **Statistical reporting is incomplete**
   Only five random seeds are used, and no confidence intervals or statistical significance tests are provided. The absolute improvements are modest, particularly on eICU. The manuscript should report paired bootstrap confidence intervals or equivalent tests, and ideally repeat evaluation across patient- or hospital-level resamples. The table also gives zero standard deviation for deterministic models without explaining the evaluation procedure.

6. **Interpretability claims are overstated**
   Attention weights are not necessarily faithful explanations of model decisions. Averaging attention over true-positive predictions can obscure heterogeneity and may reflect correlated variables or measurement frequency. The paper provides no faithfulness analysis, perturbation test, calibration analysis, or clinician evaluation. Moreover, the statement that lactate, respiratory rate, and mean arterial pressure are “components of established sepsis criteria” is imprecise: these variables relate to sepsis assessment but are not all direct components of the same Sepsis-3 criterion.

7. **Generalizability is limited**
   Both datasets are ICU-focused and US-based, and the manuscript does not describe hospital-level validation on eICU. Random patient splitting may allow institution-specific patterns to be shared across splits. A hospital-held-out evaluation would better assess transportability.

8. **Clinical utility is not evaluated**
   AUROC and AUPRC alone do not establish whether the model would produce useful or safe alerts. Calibration, sensitivity at clinically relevant false-alert rates, alert burden, decision-curve analysis, and lead-time distributions would substantially strengthen the work.

### Minor concerns
- The abstract and introduction should distinguish prediction of sepsis onset from prediction of clinician recognition or treatment.
- The exact operational definition of “six hours before onset” needs clarification.
- The model’s use of “visit-level” attention is somewhat inconsistent with hourly windows; “window-level” attention would be clearer.
- Results should include standard deviations for the ablation and 12-hour experiment.
- The paper would benefit from reporting parameter counts, computational cost, and training details.

## Scores

| Criterion | Score (0–100) |
|---|---:|
| Soundness | 43 |
| Novelty | 51 |
| Significance | 56 |
| Clarity | 68 |

### Final average
\[
\frac{43 + 51 + 56 + 68}{4} = 54.5
\]

## Final recommendation: **Reject**

The problem is important and the manuscript is clearly written, but the current evidence is insufficient to support the central claims. Major revisions are needed regarding cohort and label construction, leakage prevention, fair baseline tuning, statistical validation, reproducibility, and the interpretation of attention weights.