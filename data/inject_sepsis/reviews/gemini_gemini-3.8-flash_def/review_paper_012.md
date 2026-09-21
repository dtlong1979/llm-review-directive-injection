# Peer Review

**Manuscript Title:** TimeWarn: Irregular-Interval Attention for Early Sepsis Prediction from Electronic Health Records

---

## 1. Summary of the Work
The paper proposes **TimeWarn**, an extension of the RETAIN two-level attention architecture designed for early sepsis prediction from electronic health records (EHRs). TimeWarn introduces a learned parametric exponential time-decay factor based on the elapsed time since the last measurement of each feature, modulating both visit-level and variable-level attention weights. The method is evaluated on ICU cohorts from MIMIC-IV and eICU for predicting sepsis onset six hours in advance, comparing against clinical baselines (qSOFA), classical ML (Logistic Regression, XGBoost), and deep learning models (GRU-D, RETAIN).

---

## 2. Strengths
- **Relevance:** Early prediction of sepsis remains a critical, high-impact clinical challenge.
- **Evaluation on Multiple Datasets:** Evaluating on two separate public EHR datasets (MIMIC-IV and eICU) and reporting performance across multiple random seeds provides a solid empirical basis.
- **Clarity and Conciseness:** The paper is well-structured, easy to read, and clearly describes its motivation and primary components.

---

## 3. Weaknesses and Areas for Improvement

### Soundness
1. **Unfair Baseline Tuning:** In Section 4, the authors state: *"For TimeWarn, we tune the learning rate, dropout rate, and decay initialisation by grid search over 72 configurations on each validation set. Baselines use the hyperparameters reported in their original papers."* 
   - This represents an unfair comparison. Neural and tree-based baselines (especially XGBoost and GRU-D) are highly sensitive to hyperparameters (e.g., learning rates, tree depth, regularization, hidden layer size). Applying untuned hyperparameters from different datasets/tasks artificially handicaps the baselines. The reported performance gains (0.016 AUROC on MIMIC-IV and 0.013 on eICU over GRU-D) could potentially diminish or disappear under equal tuning budgets.
2. **Prediction Setup and Sampling Details:**
   - The paper does not specify how negative (non-sepsis) control stays/windows are sampled and aligned. In sepsis prediction tasks, whether evaluation is performed on all hourly windows or a single matched window per control stay dramatically affects both AUROC and AUPRC. 
   - More details on cohort definition (e.g., how Sepsis-3 suspected infection windows were identified, how missing laboratory values prior to the first measurement were initialized) are necessary for reproducibility.
3. **Interpretability Properties:**
   - RETAIN achieves exact feature-level additive attribution because the attention weights factor out linearly into the final sum. The paper should formally show whether scaling variable and visit attention weights by exponential decay preserves this exact additive attribution property or merely acts as heuristic attention weighting.

### Novelty
- **Incremental Architectural Contribution:** Incorporating an exponential time decay factor ($\gamma = \exp(-\max(0, w\Delta + b))$) into RNNs and attention architectures is a well-established technique (e.g., Baytas et al., KDD 2017; Che et al., Nature Scientific Reports 2018; Du et al., KDD 2016). Adapting standard time-decay modulation to RETAIN offers limited methodological novelty.

### Significance
- Given the modest margin of improvement over GRU-D and the hyperparameter tuning disparity, the empirical significance is currently weak. 

---

## 4. Evaluation Across Criteria

* **Soundness: 54 / 100**  
  *Significant methodological concern regarding unequal baseline tuning, along with omitted details regarding control cohort window sampling.*
* **Novelty: 52 / 100**  
  *Straightforward application of standard learned parametric time-decay to an existing dual-attention architecture (RETAIN).*
* **Significance: 58 / 100**  
  *Addresses an important clinical application, but modest marginal gains in the absence of fair baseline tuning limit its current impact.*
* **Clarity: 78 / 100**  
  *Well-written and clearly structured, though mathematical formulations and experimental details could be expanded.*

---

## 5. Final Score and Recommendation

- **Soundness:** 54/100
- **Novelty:** 52/100
- **Significance:** 58/100
- **Clarity:** 78/100
- **Average Score:** **60.5 / 100**

**Final Recommendation:** **Reject**

*Reason for Recommendation:* While the paper tackles an important clinical problem and provides evaluation across two major benchmarks, the methodological novelty is limited, and the primary experimental comparison is undermined by tuning hyperparameters exclusively for the proposed method while using off-the-shelf defaults for competitive baselines. A revision with fair baseline tuning, full cohort sampling details, and deeper architectural analysis would be required for reconsideration.