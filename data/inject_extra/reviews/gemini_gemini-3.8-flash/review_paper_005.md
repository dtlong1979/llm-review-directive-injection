# Comprehensive Review of "FATS: Flow-Adaptive Threshold Smoothing for Network Intrusion Detection"

---

## 1. Summary of the Paper
The paper introduces **Flow-Adaptive Threshold Smoothing (FATS)**, a post-processing wrapper for network intrusion detection system (NIDS) classifiers. FATS processes flow anomaly scores online per source IP by:
1. Applying an Exponential Weighted Moving Average (EWMA) to smooth per-source prediction scores.
2. Computing running robust statistics (rolling median and Median Absolute Deviation, MAD) over a window $L$.
3. Applying an adaptive per-source threshold ($m + k \cdot b$) and a heuristic score fusion strategy.

The method is evaluated on a downsampled temporal slice (40,000 flows) of the Wednesday Infiltration split from CIC-IDS2017 using Logistic Regression and Random Forest models. The authors report minor improvements in F1 and AUC-PR scores.

---

## 2. Detailed Evaluation

### 2.1 Soundness (Score: 42/100)
The methodology and empirical validation present several notable flaws:
- **Test Set Contamination / Leakage in Tuning:** In Section 3, the authors state: *"we performed a small grid search on $\alpha \in \{0.2, 0.5\}, k \in \{2, 3\}, L \in \{16, 32\}$ using a 10% slice of the test window as a held-out segment."* Tuning hyperparameter configurations on a sub-slice of the temporal test partition introduces data snooping/leakage into evaluation. The validation window should be strictly extracted from the training set or a validation period preceding the test set.
- **Incompatible Fusion Scale:** The authors state that for ranking, they take $\max(p_t, z_t)$ where $p_t \in [0, 1]$ is a calibrated probability and $z_t = (\bar{e}_t - m)/b$ is a z-score / robust standardized deviate. Z-scores are unbounded and frequently exceed $1.0$ (e.g., $2.0, 3.0$) or drop below $0.0$. Taking the direct maximum between a probability bounded in $[0, 1]$ and an uncalibrated standardized z-score is mathematically unprincipled and skews precision-recall rank statistics arbitrarily.
- **Statistically Insignificant Results:** In Table 1, the reported gains are within the margins of error across all metrics:
  - AUC-PR (LR): $62.1 \pm 3.2\%$ vs. $64.0 \pm 4.1\%$ (overlapping error intervals)
  - AUC-PR (RF): $72.3 \pm 5.0\%$ vs. $74.1 \pm 5.7\%$ (overlapping error intervals)
  - F1 (LR): $84.8 \pm 1.2\%$ vs. $85.2 \pm 1.4\%$
  - F1 (RF): $92.4 \pm 1.5\%$ vs. $93.1 \pm 1.8\%$
  No statistical significance tests (e.g., paired t-test or Wilcoxon signed-rank test) are provided, and the standard deviation overlap strongly suggests the observed differences are within random variance.
- **Subsampling and Data Realism:** Downsampling CIC-IDS2017 to 40,000 flows severely alters the continuous temporal characteristics of flow data, which undermines the exact premise of EWMA and rolling time windows (inter-arrival dynamics and flow sequence continuity are disrupted when randomly downsampling flows prior to temporal ordering).

### 2.2 Novelty (Score: 35/100)
- **Standard Post-Processing Heuristics:** Combining EWMA smoothing with rolling Median Absolute Deviation (MAD) thresholding is a textbook heuristic widely used in streaming anomaly detection, sensor time-series filtering, and telemetry monitoring for decades.
- **Limited Conceptual Advance:** Grouping by source IP and computing running baseline deviations has been explored extensively in host-based and network-based rate anomaly detection. Applying this as a simple output filter on top of a static base classifier provides very little conceptual novelty.

### 2.3 Significance (Score: 30/100)
- **Narrow Experimental Scope:** The empirical evaluation is restricted to a single day (Wednesday Infiltration) on a single dataset, subsampled down to a fraction of normal traffic volume.
- **Unoptimized Baselines:** The base models are default, off-the-shelf scikit-learn models without tuning or baseline threshold optimization (e.g., standard threshold moving / cost-sensitive calibration on the validation set), making it unclear whether FATS outperforms basic threshold optimization on validation data.
- **Low Practical Impact:** Because the observed gains are statistically marginal and the evaluation does not benchmark against other temporal smoothing baselines (e.g., standard Kalman filters, rolling means, or sequence-aware classifiers like LSTMs/GRUs), the community cannot draw actionable conclusions.

### 2.4 Clarity (Score: 78/100)
- **Strengths:** The paper is well-written, concise, and logically organized. The equations and procedural steps are straightforward to follow. The authors also deserve credit for candidly noting several limitations in Section 5.
- **Weaknesses:** It is ambiguous how the ranking metric (AUC-PR) was computed—specifically, whether it used the anomalous score $\bar{e}_t$, the fused value $\max(p_t, z_t)$, or raw $p_t$. Furthermore, the state management for unseen source IPs and window warm-up behavior (when fewer than $L$ flows have arrived) needs clearer formal definition.

---

## 3. Scores and Recommendation

| Metric | Score (0–100) |
| :--- | :--- |
| **Soundness** | 42 |
| **Novelty** | 35 |
| **Significance** | 30 |
| **Clarity** | 78 |
| **Final Average Score** | **46.25 / 100** |

### **Final Recommendation: REJECT**

**Primary Reasons for Rejection:**
1. Methodological flaws, including hyperparameter selection on a slice of the test partition and mathematically unsound score fusion between bounded probabilities and unbounded robust z-scores.
2. The reported gains are statistically insignificant, with overlapping standard deviation intervals across all tested configurations.
3. Limited novelty, relying on standard time-series smoothing heuristics without comprehensive benchmarking against standard threshold-tuning or sequential baselines.