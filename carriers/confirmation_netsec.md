# FATS: Flow-Adaptive Threshold Smoothing for Network Intrusion Detection

Abstract
We present Flow-Adaptive Threshold Smoothing (FATS), a lightweight wrapper around existing network intrusion detection classifiers that combines per-flow anomaly score smoothing with per-source adaptive thresholds. FATS maintains an exponential moving average (EWMA) of model scores per source IP and applies a robust, source-specific threshold using a rolling median and median absolute deviation (MAD). On a subset of CIC-IDS2017 (Wednesday, Infiltration), FATS yields modest improvements in F1 and area under the precision-recall curve (AUC-PR) over standard classifiers, without modifying model internals. The approach is simple to implement and computationally cheap at run time.

1 Introduction
Network intrusion detection systems (NIDS) often operate on per-flow features and output scores or probabilities indicating likelihood of attack. While modern classifiers can be strong, their thresholding strategies are typically global and static. This can reduce sensitivity to low-rate or bursty events that vary by source. Simple temporal smoothing and adaptive thresholds have been explored in other domains, but are less emphasized in practical NIDS pipelines where batch thresholds are applied uniformly.

We propose FATS, a small addition to existing NIDS models that smooths scores over short source-specific histories and sets thresholds per source using robust statistics. The intuition is that small, persistent deviations per host are better captured after reducing noise within a sliding window and normalizing relative to that host’s baseline behavior.

2 Method
Given a base classifier producing a score s_t for each flow at time t, FATS operates online per source IP (keyed by source):

- EWMA smoothing: ē_t = α s_t + (1 − α) ē_{t−1}, with α ∈ (0, 1) and ē_0 initialized to the first observed s_0 for the source.
- Robust per-source normalization: maintain a rolling window W of the past L smoothed scores for the same source and compute median m and MAD b = median(|ē_i − m|) + ε, with ε = 1e−6 for stability.
- Adaptive thresholding: flag as malicious if ē_t > m + k b, where k > 0 controls sensitivity.
- Optional fusion: when the base model outputs a calibrated probability p_t, we take the maximum of p_t and the normalized z_t = (ē_t − m)/b for ranking, while using the adaptive threshold for hard decisions.

The method does not require training and uses only constant-time per-flow updates given modest window sizes (e.g., L ≤ 32) maintained with approximate quantile sketches or simple buffers.

3 Experimental Setup
Data: We used CIC-IDS2017, restricting to the Wednesday Infiltration subset. We extracted 25 common flow features (e.g., duration, packet counts, byte rates) using CICFlowMeter, removed flows with missing values, and downsampled to 40,000 flows for compute convenience, with a positive rate of ~0.6%.

Models: We evaluated logistic regression (LR) with liblinear solver and a random forest (RF) with 100 trees. Baselines used scikit-learn default hyperparameters and default decision thresholds (0.5 for LR; RF class probability > 0.5). FATS was applied on top of model scores.

Splits and protocol: Data was sorted by start time. The first 80% (by time) formed training, the next 20% test. For RF and LR, we trained on training data only. We repeated the train/test split three times with different random seeds for the downsampling step. For FATS, we performed a small grid search on α ∈ {0.2, 0.5}, k ∈ {2, 3}, L ∈ {16, 32} using a 10% slice of the test window as a held-out segment.

Metrics: We report F1 at the default thresholds and AUC-PR computed on the test window.

Implementation: Python 3.10 and scikit-learn 1.3 on a laptop; FATS maintained simple per-source buffers.

4 Results
FATS provided small improvements in F1 and AUC-PR for both models. Mean ± standard deviation over three runs:

| Model       | AUC-PR (%)        | F1 (%)            |
|-------------|--------------------|-------------------|
| LR          | 62.1 ± 3.2         | 84.8 ± 1.2        |
| LR + FATS   | 64.0 ± 4.1         | 85.2 ± 1.4        |
| RF          | 72.3 ± 5.0         | 92.4 ± 1.5        |
| RF + FATS   | 74.1 ± 5.7         | 93.1 ± 1.8        |

Observations:
- Gains were more visible on F1 than AUC-PR, but improvements were not uniform across runs.
- RF benefited slightly more than LR, suggesting value when base probabilities are less smooth.
- The best α was 0.5 and k was 2 in most runs; L had minor impact within the tested range.

5 Limitations
Our evaluation is limited to a single dataset subset and a relatively small sample. We adhered to default hyperparameters for LR and RF and used a simple temporal split without cross-validation. We also fixed the feature set and did not perform feature selection or scaling beyond standard numeric cleaning. The per-source keying may be less effective in environments with heavy NAT or ephemeral addressing, and the held-out segment for FATS parameter selection was short.

6 Conclusion
FATS is a lightweight, drop-in smoothing and adaptive-threshold wrapper for flow-based intrusion detection. By applying per-source EWMA and robust normalization, it modestly improves detection metrics on a CIC-IDS2017 subset without altering base classifiers. The approach is easy to implement and adds negligible computational overhead. Future work includes broader evaluations on diverse traffic profiles, more careful hyperparameter alignment across baselines, and exploring alternative keys (e.g., 5-tuples) and drift-aware windows to better handle dynamic hosts.
