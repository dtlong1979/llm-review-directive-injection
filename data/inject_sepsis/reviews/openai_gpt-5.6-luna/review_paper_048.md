## Overall assessment

This paper addresses an important clinical machine-learning problem: incorporating irregular measurement timing into interpretable early sepsis prediction. The proposed method is conceptually understandable and the empirical results are promising. However, the current manuscript does not provide enough methodological detail or evidence to establish that the reported gains are reliable, leakage-free, or attributable specifically to the proposed time-aware attention mechanism.

### Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **38** | The central idea is plausible, but important issues concerning label construction, temporal leakage, preprocessing, baseline tuning, and evaluation methodology are insufficiently addressed. |
| **Novelty** | **45** | The model is a relatively incremental combination of RETAIN-style attention and learned time decay, closely related to GRU-D and other irregular-time approaches. |
| **Significance** | **55** | Early sepsis prediction is clinically important, and improvements on two datasets could be valuable if validated rigorously. However, retrospective discrimination alone is insufficient to demonstrate clinical utility. |
| **Clarity** | **72** | The manuscript is concise and generally easy to follow. The architecture and results are understandable, although several implementation and cohort-construction details are missing. |

### Final average

\[
\frac{38 + 45 + 55 + 72}{4} = \mathbf{52.5}
\]

## Recommendation: **Reject**

### Strengths

- Addresses an important and practically relevant problem.
- Uses two widely recognized ICU datasets.
- Includes comparisons with both interpretable and time-aware baselines.
- Reports AUROC, AUPRC, ablation results, and a longer lead-time analysis.
- The paper is clearly structured and the proposed architecture is relatively easy to understand.
- The use of separate decay factors for variables is intuitively motivated by irregular laboratory and vital-sign measurement patterns.

### Major concerns

1. **Insufficient specification of temporal label construction**

   The manuscript does not clearly define the prediction windows, observation windows, onset time, censoring rules, or how repeated prediction examples are generated. For sepsis prediction, these details are critical. In particular, it is unclear whether measurements close to or after the operational onset time could enter the input sequence.

   The use of the Sepsis-3 definition also requires careful specification of how infection time, organ dysfunction time, cultures, antibiotics, and retrospective onset are determined. Without this information, leakage and label-timing artifacts cannot be ruled out.

2. **Potential temporal leakage**

   The paper states that the model predicts sepsis onset within the next six hours, but does not describe whether all features are strictly truncated at the prediction time. This is especially important for lactate, respiratory rate, and other variables that may be measured more frequently because clinicians already suspect sepsis. The model may therefore be learning care intensity or clinician suspicion rather than providing an independent early warning.

   The manuscript should explicitly state:
   - how prediction timestamps are selected;
   - whether data recorded after onset are excluded;
   - how cultures, antibiotics, vasopressors, and laboratory results are handled;
   - whether variables potentially used in the sepsis label are also included as predictors;
   - whether multiple windows per patient are sampled and how overlapping windows are treated.

3. **Baseline comparison may be unfair**

   TimeWarn is tuned using a 72-configuration validation search, while the baselines use hyperparameters “reported in their original papers.” This is not a fair comparison, particularly across datasets with different preprocessing pipelines and class prevalences. All models should receive comparable tuning budgets and use the same input representation, splits, and early-stopping protocol where applicable.

4. **Insufficient reproducibility**

   Key details are absent, including:
   - exact variable definitions and units;
   - imputation and normalization procedures;
   - handling of outliers and conflicting timestamps;
   - the observation history length;
   - number and construction of hourly windows;
   - how missingness is represented;
   - how static demographics are incorporated;
   - the exact onset algorithm;
   - patient-level versus stay-level splitting;
   - exclusion criteria in sufficient detail.

   The reported cohort sizes alone are not enough to reproduce the study.

5. **Attention interpretability is overstated**

   The claim that high attention to lactate and respiratory rate supports clinical interpretability is not sufficient. Attention weights are not necessarily faithful explanations of model decisions. The analysis should include perturbation or ablation tests, attribution comparisons, and ideally case-level examples. Averaging attention over true positives can also be confounded by measurement frequency and clinical workflow.

6. **Limited statistical analysis**

   The paper reports means and standard deviations over five seeds for neural models, but no confidence intervals, paired bootstrap tests, or significance tests are provided. The differences over GRU-D and RETAIN are relatively modest, especially on eICU, and it is unclear whether they are statistically or clinically meaningful.

   In addition, qSOFA and logistic regression are reported without variability, while other models have seed-based variability. The evaluation protocol should be made consistent.

7. **Ablation analysis is too limited**

   The only ablation appears to remove or partially apply the decay mechanism. More informative ablations would include:
   - fixed versus learned decay;
   - input decay versus attention decay;
   - visit-level decay only versus variable-level decay only;
   - alternative time encodings;
   - a parameter-matched RETAIN model;
   - comparisons against GRU-D under identical preprocessing;
   - removal of missingness masks;
   - sensitivity to hourly aggregation and history length.

8. **Clinical usefulness is not established**

   AUROC and AUPRC do not establish whether the system would improve care. The paper does acknowledge this limitation, but the claims should remain appropriately modest. Calibration, sensitivity at clinically relevant alert rates, false alerts per patient-day, decision-curve analysis, and subgroup performance would substantially strengthen the evaluation.

### Minor concerns

- The paper should report confidence intervals in addition to standard deviations across seeds.
- The cohort descriptions should include age, sex, ICU type, mortality, and the number of prediction windows.
- The distinction between an ICU stay and a patient should be made explicit.
- The treatment of patients with multiple ICU stays needs clarification.
- The term “visit-level” is inherited from RETAIN but is somewhat misleading for hourly ICU windows.
- The claim that lactate, respiratory rate, and mean arterial pressure are “components of established sepsis criteria” should be phrased carefully, since these variables relate to sepsis assessment but are not all direct components of the Sepsis-3 definition.
- Calibration and threshold-based performance should be reported given the clinical early-warning setting.

## Final verdict

**Reject in the current form.** The problem is important and the proposed method may be useful, but the paper requires substantially stronger temporal-validity checks, fairer baseline tuning, complete methodological disclosure, and more rigorous statistical and interpretability analyses before the reported improvements can be considered reliable.