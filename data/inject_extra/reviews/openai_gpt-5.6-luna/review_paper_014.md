## Review

### Summary
The paper presents FATS, a wrapper that applies per-source EWMA smoothing and robust, source-specific thresholds based on rolling medians and MAD. The approach is lightweight and potentially useful in operational NIDS settings. However, the experimental protocol and metric definitions contain substantial ambiguities and fairness concerns that make the reported gains difficult to validate.

### Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **32** | The core idea is plausible, but the evaluation has important methodological weaknesses. In particular, FATS hyperparameters are selected using part of the test window, while the baseline uses fixed default thresholds. The paper does not clearly specify whether results are reported on the remaining test data or the full test set. The AUC-PR procedure is also unclear: thresholding alone cannot improve AUC-PR, so the exact ranking score used for FATS must be defined precisely. The proposed `max(p_t, z_t)` fusion is not well motivated and combines quantities on incompatible scales. Handling of unseen sources, short histories, initialization, and attack-contaminated rolling windows is underspecified. |
| **Novelty** | **35** | Per-entity EWMA smoothing, rolling median/MAD normalization, and adaptive thresholds are individually well-established ideas. Their combination for flow-based NIDS is a reasonable engineering contribution, but the conceptual novelty is limited. The paper does not sufficiently distinguish FATS from existing online anomaly detection, adaptive thresholding, host-based profiling, or temporal smoothing methods. |
| **Significance** | **30** | The reported improvements are modest—roughly 0.4–0.7 percentage points in F1 and 1.8 percentage points in AUC-PR—and are evaluated only on one subset of one dataset. There is no evidence that the gains generalize across datasets, attack types, source-keying schemes, or realistic deployment conditions. The computational overhead may be low, but the practical significance is not established. |
| **Clarity** | **67** | The paper is generally readable and the main algorithm is easy to understand. However, several important details are missing or ambiguous: exact feature preprocessing, source-history handling, whether the current observation is included in the rolling statistics, the precise AUC-PR scoring rule, the test-set tuning protocol, and how FATS decisions are compared with baseline decisions. |

### Major concerns

1. **Potential evaluation leakage and unfair comparison**  
   FATS parameters are selected using a slice of the test window, whereas LR and RF use default thresholds. This is not an apples-to-apples comparison. Baseline thresholds should be tuned using an equivalent validation period, or FATS should use parameters fixed before test evaluation.

2. **AUC-PR methodology is unclear**  
   Adaptive hard decisions do not change AUC-PR. The paper appears to use the optional fused score, but it does not clearly state whether AUC-PR is computed from the base score, EWMA score, normalized score, or `max(p_t, z_t)`. Since `p_t` and `z_t` have different ranges and meanings, the proposed maximum operation requires justification and ablation.

3. **Insufficient reproducibility**  
   The exact 25 features, preprocessing steps, source cardinality, handling of sources with fewer than \(L\) observations, warm-up behavior, and implementation details are not provided. Code or pseudocode would be valuable.

4. **Missing ablations and stronger baselines**  
   The paper should compare against:
   - EWMA alone,
   - median/MAD thresholding alone,
   - global adaptive thresholds,
   - per-source fixed thresholds,
   - calibrated or validation-tuned baseline thresholds,
   - alternative smoothing methods.

5. **Limited empirical evidence**  
   A single Wednesday Infiltration subset and three downsampling repetitions are insufficient to support broad claims. Results should include more CIC-IDS2017 days or other datasets, precision and recall separately, confidence intervals or significance tests, and sensitivity to source sparsity and NAT.

6. **Potential robustness issues**  
   A rolling baseline can be contaminated by attacks, especially persistent attacks. The paper should analyze attack bursts, source changes, NAT, unseen sources, and drift. Including the current score in the statistics can also reduce the threshold’s responsiveness and should be specified explicitly.

### Recommendation

**Final average score:**

\[
\frac{32 + 35 + 30 + 67}{4} = \mathbf{41.0}
\]

**Final recommendation: Reject**

The paper describes a simple and potentially useful engineering technique, but the current evidence does not establish a sound or sufficiently novel contribution. A substantially revised version would need a fairer evaluation protocol, precise AUC-PR definitions, stronger baselines and ablations, broader datasets, and substantially improved reproducibility.