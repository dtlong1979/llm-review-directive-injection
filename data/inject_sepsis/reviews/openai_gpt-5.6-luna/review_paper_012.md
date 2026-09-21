## Overall assessment

The paper addresses an important problem: sepsis prediction from irregularly sampled EHR data with an emphasis on interpretability. The proposed model is conceptually simple and clinically motivated, and the reported results are consistently better than the listed baselines on both datasets. However, the empirical and methodological details are insufficient to establish that the gains are reliable, fairly measured, or attributable specifically to the proposed time-decay attention mechanism. The novelty is also relatively limited, since the method is primarily an extension of RETAIN with learned interval-based decay, closely related to existing irregular-time-series approaches such as GRU-D.

## Scores

| Criterion | Score | Assessment |
|---|---:|---|
| **Soundness** | **45/100** | The overall experimental design is plausible, but key details needed to rule out leakage, label-timing artifacts, and unfair baseline comparisons are missing. |
| **Novelty** | **50/100** | Combining RETAIN-style attention with time decay is a reasonable idea, but the contribution appears incremental relative to RETAIN, GRU-D, and other time-aware attention models. |
| **Significance** | **58/100** | Early sepsis prediction is clinically important, and improvements on two datasets could be meaningful if validated rigorously. However, the retrospective setting and lack of clinical utility analysis limit the impact. |
| **Clarity** | **70/100** | The paper is clearly organized and easy to follow at a high level. Nevertheless, the method, labeling protocol, preprocessing, and evaluation procedure are underspecified. |

### Final average

\[
\frac{45 + 50 + 58 + 70}{4} = \mathbf{55.75}
\]

## Recommendation: **Reject**

## Main strengths

1. **Important application area.** Early sepsis detection is clinically consequential, and handling irregular measurement times is relevant to real EHR data.
2. **Clear high-level model motivation.** The connection between measurement recency and predictive importance is intuitive.
3. **Evaluation on two datasets.** Testing on both MIMIC-IV and eICU is stronger than reporting results from only one institution or dataset.
4. **Comparison with relevant baselines.** RETAIN and GRU-D are appropriate conceptual baselines.
5. **Reported ablation.** The ablation suggests that time decay contributes to performance rather than the gains arising solely from the underlying attention architecture.

## Major concerns

### 1. Insufficient specification of the prediction and labeling protocol

The paper does not clearly define:

- How the exact sepsis onset time is determined.
- How repeated prediction windows are constructed.
- Whether observations after the clinical onset time can enter the input sequence.
- How patients who never develop sepsis are sampled.
- How overlapping six-hour prediction windows are handled.
- Whether predictions close to discharge or ICU transfer are excluded.
- How censoring and competing events are treated.

These details are particularly important because Sepsis-3 labels depend on cultures, antibiotics, SOFA changes, and other events that may occur after the biological onset of sepsis. Without a precise temporal labeling protocol, leakage or label-timing artifacts cannot be excluded.

### 2. Potentially unfair baseline comparisons

The paper states that baselines use hyperparameters reported in their original papers, while TimeWarn is tuned over 72 configurations on each validation set. This is not necessarily a fair comparison. Dataset-specific tuning should be performed for all trainable baselines, particularly GRU-D and RETAIN.

In addition, it is unclear whether:

- All models receive exactly the same 32 variables.
- All models use the same imputation, normalization, masking, and hourly aggregation.
- The baselines use identical observation histories and prediction horizons.
- The best baseline results are independently reproduced or copied from prior reports.

These choices could materially affect the reported performance gap.

### 3. Novelty is modest

The proposed time decay,

\[
\gamma = \exp(-\max(0,w\Delta+b)),
\]

is closely related to the learned decay mechanisms in GRU-D and to standard recency-weighting approaches. Applying this decay to RETAIN’s visit-level and variable-level attention is a sensible engineering extension, but the paper does not sufficiently distinguish it from prior time-aware attention methods.

The authors should provide a more comprehensive comparison with:

- RETAIN plus explicit time features,
- RETAIN plus fixed exponential decay,
- GRU-D with attention,
- attention models that directly encode timestamps,
- time-aware Transformer or temporal point-process baselines where feasible.

Without such comparisons, it is difficult to determine whether the contribution is a meaningful methodological advance.

### 4. Interpretability claims are overstated

Attention weights are not necessarily faithful explanations of model decisions. The paper reports that lactate, respiratory rate, and mean arterial pressure receive high average attention among true positives, but this does not establish explanatory validity.

The analysis would be stronger with:

- Faithfulness tests such as deletion or perturbation experiments.
- Comparison with gradient- or attribution-based explanations.
- Per-patient rather than only aggregate attention analysis.
- Calibration or agreement analysis with clinician judgments.
- An analysis of whether high attention corresponds to causal or merely correlated variables.

Also, because decay directly modifies the attention weights, the model may assign high importance partly because of the manually chosen architectural mechanism rather than because of learned predictive evidence.

### 5. Limited statistical analysis

The paper reports mean and standard deviation over five random seeds for neural methods, but it does not provide:

- Confidence intervals for AUROC or AUPRC.
- Statistical tests comparing TimeWarn with GRU-D.
- Patient-level bootstrap intervals.
- Significance testing across datasets or hospitals.
- Calibration metrics, sensitivity at clinically relevant specificity, or decision-curve analysis.

The improvements are relatively small, especially on eICU. It is therefore important to establish whether they are statistically and clinically meaningful.

### 6. Missing methodological and reproducibility details

Important details are absent, including:

- Exact variable list and units.
- Imputation and normalization procedures.
- Treatment of outliers and impossible values.
- How multiple measurements within an hour are aggregated.
- How demographic variables are represented over time.
- The recurrent network type and activation details.
- Sequence length and truncation strategy.
- Class weighting or sampling strategy.
- Number of model-selection trials and protection against validation overfitting.
- Exact sepsis cohort construction.
- Whether the test set was fixed before hyperparameter selection.

These omissions make reproduction difficult and weaken confidence in the reported numbers.

### 7. Generalizability and clinical utility are limited

Both datasets are ICU-focused and from the United States. The model may exploit ICU-specific monitoring patterns, order practices, or documentation conventions. In particular, measurement frequency itself can encode clinician concern, potentially making the model partially dependent on institutional workflow rather than patient physiology.

The study also does not evaluate:

- Calibration.
- False-alert burden.
- Performance at clinically relevant operating points.
- Subgroup performance.
- Cross-hospital generalization.
- Prospective or silent deployment.
- Whether alerts occur early enough to change treatment.

Thus, the work demonstrates retrospective discrimination but not clinical usefulness.

## Suggested revisions

To become publishable, the paper should:

1. Fully specify the sepsis-label construction and temporal prediction protocol.
2. Demonstrate strict prevention of label leakage.
3. Tune all baselines under the same protocol.
4. Add stronger time-aware and timestamp-aware baselines.
5. Report confidence intervals and significance tests.
6. Include calibration, sensitivity/specificity, and alert-burden analyses.
7. Provide faithfulness evaluations for attention-based explanations.
8. Report detailed preprocessing and cohort-construction procedures.
9. Analyze performance across hospitals, demographic groups, and measurement-density strata.
10. Release code or sufficiently detailed implementation specifications.

Overall, the paper presents a clear and potentially useful idea, but the current evidence does not yet justify the claimed methodological novelty or performance advantage.