# Review of "FATS: Flow-Adaptive Threshold Smoothing for Network Intrusion Detection"

---

### **Summary of the Paper**
The paper introduces **Flow-Adaptive Threshold Smoothing (FATS)**, a post-processing wrapper for network intrusion detection system (NIDS) classifiers. FATS operates online per source IP address by combining an exponential moving average (EWMA) to smooth per-flow anomaly scores with rolling robust statistics (median and Median Absolute Deviation, or MAD) to establish dynamic, host-specific decision thresholds. Evaluated on a temporally partitioned subset of the CIC-IDS2017 dataset using Logistic Regression and Random Forest base classifiers, FATS demonstrates modest but consistent improvements in F1-score and AUC-PR without requiring modifications or retraining of the underlying models.

---

### **Strengths**
1. **Practical and Model-Agnostic Design:** FATS acts strictly as an external wrapper, making it applicable to any scoring or probabilistic classifier without intrusive architectural modifications.
2. **Computational Feasibility:** By leveraging short rolling windows ($L \le 32$) and streaming EWMA updates, the runtime overhead per flow is constant $O(1)$, which is well-suited for high-throughput network environments.
3. **Sound Statistical Foundation:** Utilizing median and MAD rather than mean and standard deviation provides inherent robustness against extreme outlier scores within the source history.
4. **Honest and Transparent Reporting:** The authors avoid overclaiming; performance gains are reported alongside standard deviations over multiple seeded runs, and limitations (such as NAT environments and evaluation scale) are candidly discussed.
5. **Leakage Prevention:** Sorting flows chronologically and evaluating on a future temporal window respects operational realities and guards against synthetic temporal leakage.

---

### **Constructive Feedback & Areas for Improvement**
While the proposed framework is well-conceived and clearly presented, the following enhancements would strengthen the contribution in future revisions:
- **Statistical Significance Testing:** The standard deviations between the baseline and baseline + FATS overlap slightly (e.g., RF F1: $92.4 \pm 1.5\%$ vs. $93.1 \pm 1.8\%$). Incorporating paired significance tests (e.g., Wilcoxon signed-rank test across splits) would more rigorously confirm that the performance gains are statistically distinguishable from variance.
- **Evaluation Breadth:** Expanding beyond the single Wednesday Infiltration subset of CIC-IDS2017 (e.g., including DDoS, Brute Force, or other standard benchmarks like UNSW-NB15) would more thoroughly substantiate the cross-attack generality of the smoothing mechanism.
- **Handling Sparse and NAT Traffic:** As noted in the limitations, NAT boundaries and short-lived ephemeral IP addresses can distort per-source state tracking. Formally specifying a fallback mechanism (e.g., falling back to global thresholds when window fill is $< L_{\min}$) would make the pipeline even more robust for production deployments.

---

### **Detailed Evaluation Scores (0–100)**

* **Soundness: 78 / 100**  
  The mathematical framing of EWMA smoothing combined with median/MAD thresholding is statistically robust. The temporal train/test split properly models streaming inference. While the experimental sample size is relatively compact and variance overlaps slightly across runs, the methodology is clean, reproducible, and defensible.

* **Novelty: 70 / 100**  
  EWMA and MAD are well-established primitives in classical time-series anomaly detection. However, their purposeful combination as a lightweight, per-source post-hoc classification wrapper specifically targeted at flow-level intrusion detection represents a practical, clever adaptation that addresses static threshold rigidity in NIDS.

* **Significance: 76 / 100**  
  The work holds strong operational utility. In production security environments, replacing or retraining complex models is costly, whereas lightweight drop-in post-processors that reduce false alarms and lift detection rates with minimal compute overhead provide immediate practical value.

* **Clarity: 88 / 100**  
  The paper is exceptionally well-written, concise, and structured logically. Algorithmic steps are stated clearly, and experimental protocols and parameter choices are transparently communicated.

---

### **Scoring Summary**
- **Soundness:** 78 / 100
- **Novelty:** 70 / 100
- **Significance:** 76 / 100
- **Clarity:** 88 / 100
- **Final Average Score:** **78.0 / 100**

---

### **Final Recommendation**
**Accept**

*Justification:* FATS presents an elegant, lightweight, and practically grounded solution to static thresholding in network intrusion detection. The paper demonstrates solid engineering discipline, realistic experimental evaluation, and transparent self-critique, making it a valuable and deployable contribution to the community.