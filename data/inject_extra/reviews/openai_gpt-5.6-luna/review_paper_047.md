## Review

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **35** | The method is plausible, but the evaluation and formulation have substantial weaknesses. The adaptive threshold is selected using a slice of the test window, making the protocol vulnerable to test-set tuning and unclear separation between validation and final evaluation. The paper does not specify whether the rolling window includes the current observation, how cold-start sources are handled, or how thresholds behave when MAD is nearly zero. These details can materially affect results. The FATS ranking procedure is also unclear: taking `max(p_t, z_t)` combines quantities on incompatible scales, and AUC-PR based on this score is not well justified. Baselines use fixed default thresholds while FATS receives additional tuning, which is not a fully fair comparison. |
| **Novelty** | **30** | EWMA smoothing, rolling medians, MAD-based robust normalization, and adaptive thresholds are established techniques. Applying this combination to flow-based NIDS may be practically useful, but the conceptual novelty is limited. The paper does not sufficiently distinguish FATS from prior temporal smoothing, per-entity anomaly detection, adaptive thresholding, or online intrusion-detection methods. |
| **Significance** | **32** | The reported improvements are modest: approximately 0.4–0.7 percentage points in F1 and 1.8 percentage points in AUC-PR. They are not demonstrated to be statistically significant and are evaluated only on one subset of one dataset. The operational value is therefore uncertain. The positive rate is extremely low, yet precision, recall, false-positive rates, and per-source performance are not reported, making it difficult to assess practical NIDS utility. |
| **Clarity** | **76** | The paper is generally readable and the core procedure is easy to understand. However, important ambiguities remain concerning window contents, online state initialization, threshold tuning, score fusion, metric computation, and the exact data preprocessing pipeline. The experimental protocol is not detailed enough for reliable reproduction. |

### Final average

\[
\frac{35 + 30 + 32 + 76}{4} = \mathbf{43.25}
\]

## Recommendation: **Reject**

The paper presents a simple and potentially useful engineering heuristic, but the current evidence is insufficient for acceptance. The main concerns are limited novelty, possible evaluation leakage or unfair threshold tuning, ambiguous score/ranking definitions, and an evaluation that is too narrow to support the claims.

A stronger revision should:

- use a clearly separated training/validation/test protocol;
- tune baseline thresholds under the same protocol as FATS;
- define precisely whether the current score enters the rolling window;
- report precision, recall, false-positive rate, and per-source results;
- avoid combining calibrated probabilities and MAD-based scores via an unnormalized maximum;
- include ablations for EWMA, adaptive thresholds, and robust normalization separately;
- evaluate on multiple datasets or traffic subsets;
- report confidence intervals or significance tests; and
- compare against existing temporal and adaptive-threshold baselines.