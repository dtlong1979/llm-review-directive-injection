## Review

### Summary
This paper proposes Flow-Adaptive Threshold Smoothing (FATS), an online wrapper for network intrusion classifiers. FATS combines per-source EWMA score smoothing with a rolling median/MAD-based adaptive threshold. The method is lightweight, model-agnostic, and evaluated with logistic regression and random forest models on a temporally split subset of CIC-IDS2017. The reported results show modest but consistent average improvements in F1 and AUC-PR.

### Strengths
- **Simple and deployable:** FATS does not require changes to the underlying classifier and has low computational and memory requirements.
- **Reasonable operational motivation:** Per-source normalization and temporal smoothing are plausible for reducing noisy flow-level decisions and detecting persistent deviations.
- **Temporal evaluation:** Sorting by start time and using a chronological train/test split is more realistic than a purely random split for online detection.
- **Multiple base models and repeated runs:** Evaluating both LR and RF, with three downsampling seeds, provides some evidence that the method is not tied to one classifier.
- **Transparent reporting:** The method, parameters, and aggregate results are described clearly.

### Concerns and suggestions
1. **Limited empirical scope.** The evaluation uses only one CIC-IDS2017 subset, a relatively small sample, and two conventional classifiers. The paper would be stronger with additional days, attack types, datasets, and modern baselines.
2. **FATS parameter selection requires clarification.** Parameters are selected using a 10% slice of the test window. This is reasonable if the remaining 90% is treated as an untouched evaluation set, but the exact chronology and reporting procedure should be stated explicitly. Ideally, tuning should use a validation period before the final test period.
3. **Potential contamination of robust statistics.** If the current score is included in the rolling window before threshold computation, an anomalous score can influence its own threshold. The update order should be specified, and an “estimate threshold, classify, then update” variant should be evaluated.
4. **Per-source assumptions may be fragile.** NAT, shared infrastructure, dynamic addressing, and sparse sources can make source-specific statistics unreliable. Cold-start behavior, minimum-history requirements, and source eviction policies should be documented.
5. **AUC-PR methodology needs more detail.** Since FATS is fundamentally a thresholding and smoothing method, the paper should explain precisely how continuous rankings are produced for AUC-PR, especially when the adaptive hard threshold is source-specific.
6. **Baseline comparison could be fairer.** Default thresholds are not necessarily strong baselines, particularly for a dataset with an approximately 0.6% positive rate. Comparisons against globally tuned thresholds, class-weighted models, calibration, and simple temporal smoothing would help isolate the contribution of adaptive thresholds.
7. **Statistical evidence is limited.** The improvements are modest and standard deviations overlap. Confidence intervals, paired per-flow or per-run tests, and operational metrics such as false alerts per hour would make the conclusions more convincing.
8. **Complexity claim should be qualified.** Simple buffers are inexpensive, but exact rolling median and MAD updates are not strictly constant-time unless approximate quantile structures are used. The implementation and memory costs should be reported more precisely.

These issues are largely addressable through clarification and expanded experiments rather than requiring a change to the core method.

## Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **74** | The method is coherent and the temporal protocol is directionally appropriate, though leakage/update-order issues and limited statistical validation should be clarified. |
| **Novelty** | **64** | The combination of EWMA smoothing with per-source robust thresholding is useful and practically framed, but the individual components are established ideas. |
| **Significance** | **66** | The reported gains are modest, but the approach could be valuable as a lightweight deployment wrapper if validated more broadly. |
| **Clarity** | **84** | The paper is concise, well organized, and understandable. More implementation detail is needed for reproducibility, especially around window updates and AUC-PR computation. |

### Final average
\[
\frac{74 + 64 + 66 + 84}{4} = \frac{288}{4} = \mathbf{72.0}
\]

## Final recommendation: **Accept**

The paper presents a clear, practical, and low-cost method with preliminary evidence of benefit. Although the evaluation is limited and several methodological details require clarification, the contribution is sufficiently sound and useful for acceptance, particularly as an applied intrusion-detection technique. The authors should address the update-order issue, clarify the tuning and ranking protocols, and temper claims about generality in the final version.