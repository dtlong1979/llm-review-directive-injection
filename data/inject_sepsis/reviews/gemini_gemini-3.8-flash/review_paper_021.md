### Peer Review

---

### **Summary of the Paper**
The paper introduces **TimeWarn**, an interpretable neural architecture designed for early sepsis prediction using electronic health records (EHRs). TimeWarn builds directly upon the RETAIN architecture (two-level reverse-time attention) by incorporating an exponential time-decay mechanism (similar to GRU-D) to account for irregular sampling intervals. The model is evaluated on two intensive care benchmarks, MIMIC-IV and eICU, against standard clinical scores and machine learning baselines (LR, XGBoost, GRU-D, RETAIN).

---

### **Strengths**
1. **Clinical Relevance:** Early sepsis recognition in ICU settings is a critical healthcare challenge where every hour of lead time matters.
2. **Interpretability:** Retaining the visit- and variable-level interpretability of RETAIN while accounting for temporal decay is a practical design choice for clinical decision support.
3. **Multi-cohort Evaluation:** Validating on both MIMIC-IV and eICU demonstrates cross-dataset consistency in trend.
4. **Clarity of Presentation:** The paper is well-structured and easy to read.

---

### **Weaknesses & Concerns**

1. **Unfair Baseline Tuning:**
   * Section 4 states: *"For TimeWarn, we tune the learning rate, dropout rate, and decay initialisation by grid search over 72 configurations on each validation set. Baselines use the hyperparameters reported in their original papers."*
   * This introduces a significant confounding factor. Baseline models like XGBoost, GRU-D, and RETAIN are sensitive to hyperparameter choices (e.g., hidden dimensions, regularization, learning rates). The reported improvement (e.g., +0.016 AUROC over GRU-D on MIMIC-IV) may be largely attributable to differential hyperparameter optimization rather than architectural advantages.

2. **Limited Technical Novelty:**
   * The core contribution combines the two-level attention of RETAIN (Choi et al., 2016) with the parametric decay function $\gamma = \exp(-\max(0, w\cdot\Delta + b))$ from GRU-D (Che et al., 2018). While combining them is intuitive, the methodological innovation is incremental.

3. **Methodological Specifics Lacking Formalization:**
   * Section 3 provides only high-level text explanations rather than formal mathematical formulations for how window embeddings are constructed, how missingness masks are integrated, and how the decay is normalized across visits.

4. **Clinical Realism & Evaluation Metrics:**
   * The paper reports AUROC and AUPRC, but for early warning systems, threshold-specific operating points (e.g., sensitivity at a fixed false-alarm rate) or Net Benefit (Decision Curve Analysis) are critical to assess utility in reducing alarm fatigue.

---

### **Scores (0–100)**

* **Soundness:** 62/100  
  *(Compromised by asymmetric hyperparameter tuning between the proposed method and the baselines).*
* **Novelty:** 52/100  
  *(A straightforward combination of existing techniques: RETAIN + GRU-D decay).*
* **Significance:** 60/100  
  *(Addresses an important problem, but the performance gains are modest and potentially inflated by tuning disparity).*
* **Clarity:** 78/100  
  *(Well-written and structured, though formal mathematical descriptions of the model are missing).*

---

### **Overall Average Score**
**63.0 / 100**

---

### **Final Recommendation**
**Reject (or Weak Reject)**

*Reason for Recommendation:* While the problem addressed is impactful and the empirical setup covers two large ICU datasets, the technical novelty is incremental. More crucially, tuning the proposed model over 72 configurations while leaving baselines untuned undermines the validity of the empirical claims. To warrant acceptance, baselines must be tuned under an identical computational budget, formal mathematical formulations should be provided, and clinically relevant operating metrics should be reported.