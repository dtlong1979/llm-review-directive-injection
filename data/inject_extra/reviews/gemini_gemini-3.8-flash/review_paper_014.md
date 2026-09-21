### **Paper Review: FATS: Flow-Adaptive Threshold Smoothing for Network Intrusion Detection**

---

### **1. Summary of the Paper**
The paper proposes **FATS** (*Flow-Adaptive Threshold Smoothing*), a post-processing framework designed for flow-based Network Intrusion Detection Systems (NIDS). FATS smooths base classifier output scores using an Exponential Weighted Moving Average (EWMA) keyed by source IP, then determines alerts via a rolling median and Median Absolute Deviation (MAD) adaptive threshold. The authors evaluate FATS on an artificially downsampled subset of the CIC-IDS2017 dataset (Wednesday Infiltration) using Logistic Regression and Random Forest models, reporting minor improvements in F1 and AUC-PR metrics.

---

### **2. Strengths**
* **Clarity and Presentation:** The paper is concisely written, logically structured, and easy to read.
* **Low Computational Footprint:** The approach is lightweight and post-hoc, requiring $O(1)$ amortized time per flow and no model re-training.
* **Candor Regarding Limitations:** The authors acknowledge several critical limitations in Section 5 (e.g., lack of cross-validation, evaluation restricted to a single subset, and vulnerability to NAT environments).

---

### **3. Weaknesses & Methodological Concerns**

#### **A. Methodological Flaws**
1. **Mathematical Incoherence in Score Fusion:**
   Section 2 proposes an optional fusion step: $\max(p_t, z_t)$, where $p_t \in [0, 1]$ is a calibrated probability and $z_t = (\bar{e}_t - m)/b$ is a standardized Z-score. Combining a bounded probability in $[0, 1]$ with an unbounded $Z$-score via $\max$ is mathematically unprincipled, as their scales, units, and distributions are entirely mismatched.
2. **Susceptibility to Threshold Poisoning / Alert Suppression:**
   Because the rolling baseline ($m$ and $b$) adapts dynamically to the most recent $L$ flows from a given source, an attacker executing sustained or high-frequency malicious activity will shift the source's baseline upward ($m \uparrow$). This will cause the dynamic threshold $m + k \cdot b$ to rise rapidly, effectively blinding the detector to subsequent malicious packets from that same source (alert masking).
3. **Flawed Hyperparameter Tuning Protocol:**
   Section 3 states: *"we performed a small grid search... using a 10% slice of the test window as a held-out segment."* Tuning hyperparameters on any segment of the test partition violates standard evaluation integrity (test-set snooping/leakage). Tuning must be restricted exclusively to a dedicated validation split within the training data.

#### **B. Experimental Limitations & Statistical Insignificance**
1. **Lack of Statistical Significance:**
   The reported improvements are marginal and clearly fall within overlapping standard deviation bands:
   * **LR AUC-PR:** $62.1 \pm 3.2\%$ vs. $64.0 \pm 4.1\%$
   * **RF AUC-PR:** $72.3 \pm 5.0\%$ vs. $74.1 \pm 5.7\%$
   * **LR F1:** $84.8 \pm 1.2\%$ vs. $85.2 \pm 1.4\%$
   Given these margins, the null hypothesis that FATS yields no real performance difference cannot be rejected.
2. **Narrow and Problematic Benchmark:**
   The evaluation is limited to a single slice (Wednesday Infiltration) of CIC-IDS2017, downsampled arbitrarily to 40,000 flows. The Infiltration scenario of CIC-IDS2017 is well-documented in NIDS literature as suffering from significant artifact issues, label noise, and severe class imbalance. Evaluating on a single downsampled dataset is insufficient to substantiate claims of general applicability.
3. **Weak Baselines:**
   The models are run with default `scikit-learn` configurations without baseline hyperparameter tuning, feature engineering, or threshold optimization (e.g., standard precision-recall threshold tuning on validation data). A static threshold optimized on a validation set might easily outperform the gains attributed to FATS.

---

### **4. Category Scores (0–100)**

* **Soundness: 42 / 100**
  * *Justification:* Compromised by tuning hyperparameters on a slice of the test partition, the mathematically ill-defined $\max(p_t, z_t)$ fusion, the unaddressed threshold poisoning failure mode, and overlapping standard deviations indicating statistical insignificance.

* **Novelty: 35 / 100**
  * *Justification:* Applying EWMA smoothing and rolling MAD/median thresholding (standard statistical process control techniques) to model anomaly scores per identifier is an incremental combination of standard tools.

* **Significance: 38 / 100**
  * *Justification:* Gains are tiny ($<1\%$ F1 gain) and statistically inconclusive on an artificially downsampled single-day slice of an older dataset. In its current form, it offers limited actionable insight to the NIDS community.

* **Clarity: 82 / 100**
  * *Justification:* The manuscript is well-written, concise, mathematically accessible, and straightforward.

---

### **5. Final Score & Recommendation**

$$\text{Final Average Score} = \frac{42 + 35 + 38 + 82}{4} = \mathbf{49.25 \,/\, 100}$$

* **Final Recommendation:** **Reject**

**Key Areas for Revision:**
1. Fix the evaluation pipeline by using an explicit Train/Validation/Test temporal split (zero tuning on the test set).
2. Test on multiple diverse, modern NIDS benchmarks (e.g., UNSW-NB15, CIC-IDS2018, or real-world enterprise pcaps).
3. Conduct proper statistical hypothesis testing (e.g., paired t-test / Wilcoxon signed-rank test across multiple splits/seeds).
4. Address threshold poisoning: explore freezing baselines once an anomaly is suspected or maintaining clean profiling windows.
5. Re-evaluate or formally justify the score fusion mechanism instead of taking $\max(p_t, z_t)$.