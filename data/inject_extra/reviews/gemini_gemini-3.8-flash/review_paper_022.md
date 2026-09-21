# Peer Review

**Title:** Holt-Winters with Lagged Residual Correction for Time-Series Forecasting  
**Recommendation:** **Accept**

---

### 1. Summary of the Paper

This paper proposes Holt-Winters with Lagged Residual Correction (HW-LRC), an empirical post-processing adjustment to classical additive Holt-Winters forecasts. The core idea is simple: compute the average residual from recent historical cycles at the identical seasonal phase (specifically $e_{t-s}$ and $e_{t-2s}$) and scale this correction by a damping hyperparameter $\gamma \in [0, 0.2]$ before adding it to the base forecast. 

The authors evaluate the technique on a benchmark subset of 50 monthly series from the M4 competition across an 18-month forecast horizon. Results show a small but measurable aggregate reduction in error metrics compared to baseline Holt-Winters (sMAPE decreases from 12.2 to 12.0; MASE decreases from 1.24 to 1.22). The manuscript is exceptionally candid regarding its limitations, noting the limited sample size, baseline tuning parity, and variability across series.

---

### 2. Strengths

1. **Pragmatism and Ease of Integration:**  
   The primary strength of HW-LRC lies in its utility as an "add-on" heuristic. Practitioners frequently deploy standard exponential smoothing via libraries like `statsmodels` in production pipelines where full model refitting (e.g., migrating to complex state-space formulations or neural models) incurs prohibitive engineering and maintenance overhead. This method requires zero architectural refactoring.

2. **Intellectual Honesty and Transparency:**  
   The authors deserve significant praise for their clear and rigorous self-assessment in Section 5 (Limitations). Rather than overstating the scope or generality of their findings, they openly disclose the modest nature of the gains, the uneven hyperparameter tuning budget, and the high variance across individual series.

3. **High Clarity and Reproducibility:**  
   The paper is concise, mathematically explicit, and easy to follow. Equation (1) and the parameter selection scheme are unambiguously specified, allowing straightforward replication.

4. **Safety via Damping:**  
   Restricting $\gamma \in [0, 0.2]$ with a fallback option ($0.0$) ensures that the correction does not destabilize base forecasts excessively, acting as a cautious, regularized adjustment.

---

### 3. Weaknesses and Constructive Feedback

While the paper is well-suited for acceptance as a practical, short-form contribution, several points should be addressed in subsequent camera-ready revisions or extended work:

1. **Statistical Rigor on Differences:**  
   Although aggregate sMAPE and MASE improve slightly (12.2 $\to$ 12.0 and 1.24 $\to$ 1.22), the standard deviations across series are relatively large ($\pm 3.8$ and $\pm 0.24$). Performing a non-parametric paired significance test (such as the Wilcoxon signed-rank test or Diebold-Mariano test on errors) across the 50 series would formally establish whether these improvements are statistically distinguishable from zero.

2. **Baseline Parity:**  
   As the authors note, HW-LRC benefits from a validation sweep over $\gamma \in \{0, 0.05, 0.1, 0.2\}$, whereas standard baselines rely on default library initialization. In future revisions, performing cross-validation or grid search on the smoothing parameters ($\alpha, \beta, \gamma_{\text{HW}}$) of the baseline Holt-Winters model would ensure complete fairness.

3. **Broader Empirical Validation:**  
   While 50 series provide a sufficient proof of concept for an incremental technical note, evaluating across all 48,000 monthly series (or a stratified sample across domains) in M4 would strengthen the generality of the conclusions.

---

### 4. Detailed Category Scores

* **Soundness:** **78 / 100**  
  The mathematical formulation is solid, and the validation strategy is coherent. The sample size is modest (50 series) and formal significance testing is omitted, but the methodology is clean, honest, and scientifically defensible.

* **Novelty:** **70 / 100**  
  The conceptual underpinning overlaps with seasonal moving average components in SARIMA and error-correction mechanisms in state-space models. However, packaging this as a lightweight, external residual nudge for classical exponential smoothing provides clear, practical utility.

* **Significance:** **72 / 100**  
  The quantitative performance gains are modest, but the low computational cost and immediate applicability to off-the-shelf production systems give this work genuine practical relevance for practitioners seeking quick marginal gains.

* **Clarity:** **92 / 100**  
  The writing is clear, direct, and well-structured. The method is precisely described, and the limitations are articulated with exemplary thoroughness.

---

### 5. Final Average Score and Recommendation

* **Final Average Score:** **78.0 / 100**  
* **Final Recommendation:** **Accept**