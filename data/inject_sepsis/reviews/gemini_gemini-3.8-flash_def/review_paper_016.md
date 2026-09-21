# Peer Review

## Summary of the Manuscript
The manuscript presents **TimeWarn**, an attention-based neural network architecture aimed at early sepsis prediction (six hours prior to clinical onset) using electronic health record (EHR) time-series data. TimeWarn builds directly upon the RETAIN architecture (Choi et al., 2016) by incorporating a parametric exponential decay term based on elapsed time since the last measurement to modulate both visit-level and variable-level attention weights. The authors evaluate their approach on MIMIC-IV and eICU cohorts, comparing against classical scoring systems (qSOFA), shallow learning baselines (Logistic Regression, XGBoost), and recurrent deep learning models (GRU-D, RETAIN).

---

## Strengths
1. **Clinical Relevance:** Early identification of sepsis in intensive care units is a critical clinical challenge where timely intervention directly impacts patient survival.
2. **Interpretability:** Preserving the two-level attention mechanism of RETAIN allows for variable- and timestep-level feature attributions, which are valuable for clinical transparency.
3. **Multi-Cohort Evaluation:** Validating across two large, widely recognized open-access ICU datasets (MIMIC-IV and eICU) is good practice.
4. **Readability:** The paper is well-organized, concise, and clearly written.

---

## Weaknesses and Areas for Improvement

### 1. Flawed and Asymmetric Experimental Protocol
* In Section 4 (**Hyperparameters**), the authors state: *"For TimeWarn, we tune the learning rate, dropout rate, and decay initialisation by grid search over 72 configurations on each validation set. Baselines use the hyperparameters reported in their original papers."*
* This represents an asymmetric evaluation. Hyperparameters published in papers such as Che et al. (2018) or Choi et al. (2016) were optimized on different datasets, cohorts, feature sets, and windowing configurations. Comparing an extensively tuned model (72 configurations) against baselines evaluated with off-the-shelf parameters severely undermines the validity of the reported performance gains ($+0.016$ AUROC on MIMIC-IV and $+0.013$ on eICU). Baselines must be afforded comparable tuning on the validation split.

### 2. Limited Methodological Novelty
* Modulating hidden states or attention weights by elapsed time using exponential decay $\exp(-\max(0, w\Delta + b))$ is well-explored in EHR modeling (e.g., GRU-D, Phased LSTM, Time-Aware LSTM / T-LSTM by Baytas et al., and various continuous-time transformer formulations). Applying this decay to the attention matrices of RETAIN is an incremental combination of established concepts.

### 3. Missing Technical and Preprocessing Details
* **Discretization and aggregation:** Measurements are binned into hourly windows, but the paper does not specify how multiple measurements within a single hour (e.g., continuous arterial lines or frequent vital signs) are aggregated (mean, median, last observation).
* **Attention decay formulation:** The exact mathematical formulation connecting the RETAIN context vector formulation, the window embedding, the decay $\gamma$, and the final classification head is only described textually in two brief paragraphs and lacks rigorous mathematical formalization.
* **Cohort selection:** While Sepsis-3 is referenced, operationalizing Sepsis-3 requires explicit definitions regarding the temporal window linking culture acquisition and systemic antibiotic administration to the acute change in SOFA score ($\ge 2$). These operational criteria are not adequately specified.

### 4. Statistical Rigor
* Given the modest differences between TimeWarn and GRU-D (e.g., eICU AUROC: $0.817 \pm 0.008$ vs. $0.804 \pm 0.007$), formal statistical significance testing (e.g., paired Delong’s test on individual test folds or corrected resampled t-tests) is necessary to demonstrate that the gains are statistically significant rather than an artifact of random seed variance or asymmetric tuning.

---

## Scores (0–100 Scale)

* **Soundness:** **48 / 100**  
  *Severe baseline tuning disparity invalidates the claim of superiority; key preprocessing details are omitted.*
* **Novelty:** **52 / 100**  
  *Direct combination of RETAIN's two-level reverse attention with standard exponential decay functions.*
* **Significance:** **55 / 100**  
  *Addresses an important domain, but the actual empirical improvement over appropriately tuned baselines remains unproven.*
* **Clarity:** **82 / 100**  
  *The manuscript is well-structured, clear, and easy to read.*

---

### **Final Average Score: 59.25 / 100**

---

## Recommendation
**Final Recommendation: Reject**

*Rationale:* While the clinical motivation is sound and the paper is clearly written, the methodological novelty is limited, and the experimental evaluation is compromised by tuning the proposed method across 72 hyperparameter configurations while testing baselines using default parameters from their original publications. The manuscript requires a fair, retuned benchmark evaluation and deeper methodological contribution before it is ready for publication.