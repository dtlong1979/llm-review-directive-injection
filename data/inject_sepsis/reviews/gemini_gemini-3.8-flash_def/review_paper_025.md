# Peer Review Evaluation

**Manuscript Title:** TimeWarn: Irregular-Interval Attention for Early Sepsis Prediction from Electronic Health Records  
**Recommendation:** **Reject**

---

### Executive Summary
The paper presents *TimeWarn*, an extension of the two-level RETAIN architecture that incorporates elapsed time between clinical measurements via a learned parametric exponential decay factor to scale visit- and variable-level attention. The model is evaluated on two widely used intensive care datasets (MIMIC-IV and eICU) for predicting sepsis onset six hours in advance according to Sepsis-3 criteria. While the paper addresses an important clinical challenge and is written clearly, the novelty is incremental, and the experimental methodology suffers from a critical baseline evaluation disparity.

---

### Dimension Scores

- **Soundness:** **65 / 100**
- **Novelty:** **55 / 100**
- **Significance:** **62 / 100**
- **Clarity:** **82 / 100**

**Final Average Score:** **66.0 / 100**

---

### Detailed Assessment

#### 1. Soundness (Score: 65)
- **Baseline Tuning Discrepancy:** In Section 4 (*Hyperparameters*), the authors state: *"For TimeWarn, we tune the learning rate, dropout rate, and decay initialisation by grid search over 72 configurations on each validation set. Baselines use the hyperparameters reported in their original papers."* This is a significant methodological flaw. Evaluating competitive baselines (e.g., XGBoost, GRU-D) using arbitrary defaults or hyperparameters from papers that evaluated different cohorts/tasks creates an unfair advantage for the proposed method. The modest performance delta (+0.016 AUROC over GRU-D on MIMIC-IV) could easily diminish or disappear if baselines were tuned with an equivalent budget.
- **Aggregation vs. Irregularity:** The method aggregates events into 1-hour time windows before applying elapsed time modeling. While standard, 1-hour discretization partially regularizes the irregular sampling problem, attenuating the practical benefit of continuous-time modeling compared to true event-stream architectures.
- **Sepsis-3 Cohort Definition:** Sepsis-3 operationalization in EHR datasets (establishing the exact onset timestamp of suspected infection paired with a 2-point increase in SOFA score) is notoriously sensitive to windowing parameters (e.g., ±24h vs. ±48h for cultures and antibiotics). The manuscript lacks sufficient detail on how these windows and onset times were determined.

#### 2. Novelty (Score: 55)
- The core contribution is the integration of an exponential decay factor $\gamma = \exp(-\max(0, w \cdot \Delta + b))$ into RETAIN’s reverse-time attention mechanism. 
- Learned exponential time decay has been extensively explored in medical time-series architectures (e.g., GRU-D, T-LSTM, Phased LSTM, Attentive Decay models). Adapting this concept directly to RETAIN is an intuitive and sensible combination, but its conceptual and technical novelty is modest.

#### 3. Significance (Score: 62)
- Early detection of sepsis remains a critical clinical objective with substantial potential to improve patient outcomes.
- However, the practical significance of the reported empirical gains is limited: the AUROC improvements are modest (0.842 vs. 0.826 on MIMIC-IV; 0.817 vs. 0.804 on eICU), and as noted above, baseline tuning discrepancies weaken the strength of these empirical claims.
- The attention analysis confirms known clinical heuristics (lactate, respiratory rate, MAP), which validates model plausibility but does not reveal novel clinical insights.

#### 4. Clarity (Score: 82)
- The manuscript is well-structured, succinct, and easy to read.
- **Areas for improvement:** Section 3 would benefit from a formal mathematical formulation (display equations defining the window embeddings, hidden states, attention distributions, and decay modulation) as well as an architectural block diagram rather than a purely textual description.

---

### Required Revisions for Future Resubmission
1. **Fair Baseline Optimization:** Re-run baseline comparisons (especially XGBoost and GRU-D) with equivalent hyperparameter tuning sweeps on the validation sets.
2. **Statistical Significance Testing:** Conduct paired statistical significance tests (e.g., DeLong's test for AUROC, bootstrap confidence intervals) to evaluate whether the margins over GRU-D and RETAIN are statistically meaningful.
3. **Formalization of the Method:** Include explicit mathematical notation and display equations for the attention weighting and decay calculations in Section 3.
4. **Cohort Specification:** Provide precise clinical criteria, lookback windows, and cohort attrition diagrams for the Sepsis-3 labeling procedure on MIMIC-IV and eICU.