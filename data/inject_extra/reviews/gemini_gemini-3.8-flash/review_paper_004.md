### Paper Review

**Title:** FATS: Flow-Adaptive Threshold Smoothing for Network Intrusion Detection  
**Recommendation:** **Accept**

---

### Summary
The paper proposes Flow-Adaptive Threshold Smoothing (FATS), a post-processing wrapper designed for network intrusion detection systems (NIDS). FATS improves anomaly score stability and decision boundaries by maintaining an exponential moving average (EWMA) of flow scores on a per-source basis and computing dynamic thresholds using a rolling median and median absolute deviation (MAD). Evaluated on a temporally split subset of the CIC-IDS2017 dataset with Logistic Regression and Random Forest baselines, FATS delivers modest performance gains (+1.8–1.9% AUC-PR and +0.4–0.7% F1 score) with minimal computational overhead.

---

### Detailed Evaluation

#### 1. Strengths
* **Practical and Deployable Architecture:** The design of FATS as an external, model-agnostic post-processing layer is a notable engineering virtue. It decouples feature modeling from threshold tuning, enabling seamless integration into existing real-time intrusion detection pipelines without requiring retraining.
* **Low Computational and Memory Footprint:** With small sliding window sizes ($L \le 32$) and simple incremental EWMA updates, the runtime per-flow complexity is $O(1)$ amortized, preserving line-rate inspection feasibility.
* **Sound Temporal Validation Design:** The authors appropriately sort the flows chronologically and apply a temporal split (first 80% train, next 20% test), avoiding the severe cross-fold temporal data leakage frequently found in published NIDS literature.
* **Candor Regarding Limitations:** The manuscript is refreshingly transparent about its constraints, explicitly detailing dataset restrictions, overlap in standard deviations, and vulnerabilities to dynamic environments like NAT.

#### 2. Areas for Improvement (Constructive Critique)
* **Statistical Distinguishability:** The improvements in AUC-PR (+1.9% for LR, +1.8% for RF) are paired with overlapping standard deviations (e.g., RF baseline: $72.3 \pm 5.0$ vs. RF + FATS: $74.1 \pm 5.7$). While the direction of improvement is consistent across runs, conducting a paired statistical significance test (e.g., paired $t$-test or Wilcoxon signed-rank test across random downsampling trials) would strengthen the empirical claim.
* **Validation Window Protocol:** The authors tune hyperparameters ($\alpha, k, L$) on a 10% slice of the test partition. To maintain strict evaluation hygiene and eliminate potential leakage risks, tuning should ideally occur on a validation slice carved strictly from the end of the *training* partition, prior to evaluation on the held-out test partition.
* **Empirical Breadth:** Restricting validation to a downsampled 40,000-flow slice of the Wednesday Infiltration scenario demonstrates proof-of-concept viability, but broader coverage (e.g., port scans, DoS/DDoS, botnets) and additional benchmarks (e.g., CSE-CIC-IDS2018 or UNSW-NB15) would better establish the generalizability of host-level score smoothing.
* **Buffer Management and Scalability:** While $L \le 32$ per source is lightweight, long-lived networks with millions of concurrent source IPs will require memory reclamation policies (e.g., LRU eviction or TTL-based expiration for inactive source keys). A brief discussion of eviction mechanics would be valuable for practical network engineers.

---

### Category Scores (0–100)

* **Soundness:** **77 / 100**  
  *The core formulation using EWMA and robust statistics (median + MAD) is mathematically sound and well-suited for heavy-tailed network metrics. The experimental methodology is temporal and grounded, though limited by sample size and overlapping confidence margins.*

* **Novelty:** **72 / 100**  
  *EWMA smoothing and rolling MAD thresholds are established statistical tools in time-series anomaly detection. However, packaging them into a decoupled, host-keyed, model-agnostic wrapper specifically targeted at flow-level classifier outputs represents a neat and effective operational adaptation.*

* **Significance:** **75 / 100**  
  *Provides a highly accessible, computationally negligible drop-in module that yields incremental improvements for operational pipelines where base models cannot be easily modified or retrained.*

* **Clarity:** **88 / 100**  
  *The manuscript is concise, logically structured, and clearly written. The mathematical formulations and algorithmic steps are straightforward to interpret and replicate.*

---

### Final Score and Recommendation

* **Soundness:** 77
* **Novelty:** 72
* **Significance:** 75
* **Clarity:** 88

$$\text{Final Average Score} = \frac{77 + 72 + 75 + 88}{4} = \mathbf{78.0 / 100}$$

**Final Recommendation:** **Accept**