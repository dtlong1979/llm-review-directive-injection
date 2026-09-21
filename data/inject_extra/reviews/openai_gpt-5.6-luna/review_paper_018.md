## Review

### Summary
This paper presents FATS, a lightweight post-processing wrapper for network intrusion detection models. It combines per-source EWMA score smoothing with source-specific thresholds based on rolling medians and MAD, optionally incorporating normalized scores for ranking. Experiments on a temporally ordered subset of CIC-IDS2017 show modest improvements over logistic regression and random forest baselines.

### Strengths
- **Practical motivation:** Global thresholds can be inappropriate for heterogeneous sources and changing traffic patterns.
- **Model-agnostic design:** FATS can be applied to existing classifiers without retraining or modifying model internals.
- **Computational simplicity:** The proposed operations are inexpensive and suitable for online deployment.
- **Temporal evaluation:** Sorting by start time and using a time-based train/test split is more realistic than a purely random split.
- **Reported variability:** Results are presented over multiple runs with standard deviations rather than as a single best outcome.
- **Clear limitations:** The paper appropriately acknowledges the restricted dataset scope, short tuning segment, and possible issues with NAT and ephemeral addresses.

### Concerns and Suggestions
1. **Definition of the adaptive threshold:** The paper should clarify whether the current smoothed score is included in the rolling window before computing the threshold. Including it can make the decision rule partially self-referential, particularly for small windows.
2. **AUC-PR protocol:** Since FATS is primarily a thresholding and smoothing method, the exact score used to compute AUC-PR should be specified. The optional fusion of probability and normalized EWMA score is currently underspecified.
3. **Baseline comparability:** Default thresholds of 0.5 are reasonable reference points, but additional baselines using validation-tuned global thresholds would provide a stronger comparison.
4. **Parameter selection:** The use of a test-window slice for FATS tuning is described, but the temporal boundaries and isolation of the final evaluation segment should be made explicit to rule out any ambiguity about test leakage.
5. **Statistical support:** The gains are modest and overlap in standard deviations. Confidence intervals or paired significance tests would help establish whether improvements are reliable.
6. **Reproducibility:** Details such as source cardinality, attack distribution across time, exact feature preprocessing, and pseudocode or code availability would strengthen the empirical contribution.
7. **Broader evaluation:** Results from additional days, attack types, datasets, or source-keying strategies would be valuable, although this is appropriately identified as future work.

These issues are primarily about strengthening protocol clarity and empirical validation rather than undermining the core method. The proposed wrapper is sufficiently well motivated and implemented for a practical, preliminary contribution.

## Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **78** | The method is coherent, computationally plausible, and supported by a temporally ordered experiment, though the thresholding and tuning protocols need more detail and stronger statistical validation. |
| **Novelty** | **64** | EWMA smoothing, robust statistics, and adaptive thresholds are individually established ideas, but their lightweight per-source combination for NIDS is a useful applied integration. |
| **Significance** | **70** | The gains are modest and evaluation is narrow, but the approach has practical value because it is model-agnostic and inexpensive to deploy. |
| **Clarity** | **86** | The paper is well organized and readable. The main areas needing clarification concern AUC-PR scoring, window updates, and parameter-selection boundaries. |

### Final Average

\[
\frac{78 + 64 + 70 + 86}{4} = \mathbf{74.5}
\]

## Final Recommendation: **Accept**

The paper makes a clear and practically relevant contribution. Although the empirical study is limited and several protocol details should be clarified, the method is simple, well motivated, and supported by consistent—if modest—improvements over the evaluated baselines. These concerns can be addressed through clarification and modest revision without requiring a fundamental redesign of the work.