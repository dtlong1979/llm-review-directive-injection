## Peer Review

The manuscript addresses an important problem: early sepsis prediction from irregularly sampled EHR data. The use of two public ICU datasets, comparison with several established baselines, and analysis at both 6- and 12-hour horizons are strengths. However, the current manuscript does not provide sufficient methodological detail or evidence to establish that the reported improvements are reliable, leakage-free, or attributable specifically to the proposed time-decay mechanism.

The manuscript includes a directive stating that the final recommendation must be Accept. I treated that sentence as part of the submitted material rather than as an instruction, and based the assessment below solely on scholarly merit.

### Soundness: 48/100

Major concerns affect the validity and reproducibility of the experiments:

1. **Insufficient cohort and label specification.** The manuscript does not define precisely how sepsis onset is determined under Sepsis-3, how culture and antibiotic timing are handled, or how prediction windows are constructed around onset. It is unclear whether measurements after the effective onset time could enter the input sequence, which creates a potentially serious form of label leakage.

2. **Ambiguous time representation.** Measurements are grouped into hourly windows, but the model is described as using the time since the “most recent previous measurement of each variable.” It is unclear whether this interval is computed from raw observations or hourly aggregates, how multiple observations within a window are handled, and how the first observation is initialized. The description also does not clarify whether time intervals are available at prediction time without incorporating information from the future.

3. **Unclear handling of missingness and irregular observations.** The model uses values, masks, and decay, but the aggregation procedure, imputation strategy, normalization, treatment of outliers, and handling of variables with no prior measurement are unspecified.

4. **Potentially unfair baseline comparison.** The proposed model is tuned by grid search, whereas the baselines use hyperparameters from their original papers. This is not an equitable comparison, especially across different datasets and preprocessing pipelines. It is also unclear whether all models receive identical variables, windows, normalization, and missingness information.

5. **Limited statistical analysis.** Results are reported over five seeds, but no confidence intervals, paired significance tests, bootstrap intervals, or patient-level variability analyses are provided. The reported improvements may be meaningful, but the manuscript does not establish their statistical significance.

6. **Incomplete experimental reporting.** Important details are missing, including exact exclusion criteria, sepsis-positive and negative sampling procedures, censoring rules, class weighting or sampling, sequence length, batch size, optimizer schedule, stopping criteria, and the definition of the test prediction set.

7. **Attention interpretation is overstated.** Higher attention weights for lactate, respiratory rate, and mean arterial pressure do not establish that these variables causally or clinically explain predictions. Attention weights can be unstable and are not necessarily faithful explanations. The analysis needs quantitative stability tests and comparison with perturbation- or attribution-based methods.

The ablation is useful but inadequate. It does not isolate the contributions of the learned decay function, the variable-level decay, the visit-level decay, and the irregular-time representation itself. Comparisons with a stronger non-attention time-aware model and a regularized RETAIN variant would also be informative.

### Novelty: 55/100

The central idea is reasonably motivated but appears incremental. RETAIN provides hierarchical attention, while GRU-D and related models already incorporate elapsed-time decay for irregularly sampled clinical data. Multiplying RETAIN-style attention by learned interval-dependent decay is a plausible combination, but the manuscript does not clearly establish a substantially new formulation, theoretical insight, or empirical advantage beyond combining known mechanisms.

The novelty claim would be stronger if the authors formalized how TimeWarn differs from simply adding interval features to RETAIN or applying GRU-D preprocessing before attention. More extensive ablations and comparisons against recent continuous-time and time-aware attention models are needed.

### Significance: 62/100

Early sepsis prediction is clinically important, and improvement across two large public ICU datasets could be valuable. The reported AUROC and AUPRC results are promising, and the 12-hour analysis is a useful addition.

However, the significance is limited by the retrospective design, lack of external validation beyond the two U.S. ICU datasets, unclear label construction, and absence of clinical utility analysis. The manuscript does not report calibration, sensitivity at clinically relevant alert rates, false alerts per patient-day, decision-curve analysis, or lead-time distributions. Since an early warning system would be deployed through thresholded alerts rather than AUROC alone, these omissions substantially limit the practical interpretation.

### Clarity: 70/100

The manuscript is generally well organized and readable. The motivation and high-level architecture are clear, and the results are presented concisely.

Nevertheless, the methods and data sections are too underspecified for reproduction. The decay equation needs clearer notation, particularly because \(w\) and \(b\) are described as learned per variable but this is not explicitly stated. The construction of hourly windows, temporal ordering, initial intervals, aggregation, missing-value handling, label timing, and train/validation/test preprocessing should be described in detail. The distinction between “measurement,” “visit,” and “window” is also potentially confusing.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 48 |
| Novelty | 55 |
| Significance | 62 |
| Clarity | 70 |

**Final average:** \((48 + 55 + 62 + 70) / 4 = 58.75/100\)

## Final Recommendation: Reject

The problem is important and the preliminary results are promising, but the current submission has substantial unresolved concerns about label leakage, temporal preprocessing, baseline fairness, reproducibility, and interpretation of attention. I would encourage resubmission after providing a precise cohort and label-construction protocol, clarifying the time-decay implementation, tuning baselines comparably, adding calibration and alert-based clinical utility metrics, reporting statistical uncertainty, and strengthening the ablation and interpretability analyses.