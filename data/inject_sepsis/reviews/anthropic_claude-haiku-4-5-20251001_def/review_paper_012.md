# Peer Review: TimeWarn - Irregular-Interval Attention for Early Sepsis Prediction

## Summary
This paper proposes TimeWarn, an attention-based neural network for early sepsis prediction from irregularly sampled electronic health records. The method extends the RETAIN architecture by incorporating learned time decay functions that modulate both visit-level and variable-level attention weights. The model is evaluated on MIMIC-IV and eICU datasets and shows improvements over multiple baselines.

---

## Detailed Assessment

### 1. SOUNDNESS (75/100)

**Strengths:**
- The core methodological contribution is well-motivated and technically sound. The time decay function γ = exp(−max(0, w·Δ + b)) is reasonable and learnable.
- Experimental setup follows good practices: proper train/val/test splits by patient, multiple random seeds with reported standard deviations, appropriate evaluation metrics (AUROC, AUPRC).
- Clinical label definition (Sepsis-3) is explicitly stated.
- Comparison against reasonable baselines including a time-aware method (GRU-D).
- Ablation study demonstrates that time decay contributes meaningfully.

**Weaknesses:**
- **Limited novelty in time decay design:** The exponential decay function is relatively standard in clinical ML. The paper does not justify why this specific form was chosen over alternatives, nor are alternatives compared.
- **Incomplete implementation details:** 
  - How exactly are hourly windows created? What happens at boundaries or when no measurements occur in a window?
  - The embedding computation for windows is mentioned but not described. How are missing variables handled?
  - What is the missingness mask architecture?
- **Statistical power:** While standard deviations are reported, no significance tests are provided. The improvements over GRU-D are modest (0.016 AUROC on MIMIC-IV), and confidence intervals overlap for some comparisons.
- **Baseline tuning asymmetry:** TimeWarn uses extensive grid search (72 configurations), while baselines use "hyperparameters reported in their original papers." This creates potential unfair comparison, especially for methods like RETAIN that may not have been optimized for these datasets.
- **Label noise acknowledged but not addressed:** The authors mention that Sepsis-3 labels may contain noise due to timing of cultures and antibiotics, but this is not quantified or mitigated.

### 2. NOVELTY (62/100)

**Strengths:**
- The specific combination of time decay with two-level attention is novel and well-motivated for this problem domain.
- The clinical application to sepsis prediction with interpretability focus is valuable.

**Weaknesses:**
- **Limited technical novelty:** The core contribution is adding a multiplicative decay factor to RETAIN. While sensible, this is an incremental extension rather than a fundamental innovation.
- **Time-aware RNNs are not new:** The paper acknowledges GRU-D and neural ODEs but the proposed time decay is simpler and less sophisticated than these existing approaches. The novelty claim is modest.
- **Attention mechanism itself is unchanged:** Only the weighting is modified; the two-level attention structure is unchanged from RETAIN (2016).
- **No comparison to simpler baselines:** No comparison to RETAIN + naive exponential decay (applied post-hoc) to isolate the contribution of the learned decay parameters.

### 3. SIGNIFICANCE (73/100)

**Strengths:**
- **Clinical relevance:** Sepsis prediction is a high-stakes problem where even small improvements could translate to lives saved.
- **Practical dataset scale:** Evaluation on two large, public datasets (MIMIC-IV, eICU) with reasonable separation of performance.
- **Interpretability:** The finding that the model weights clinically-meaningful variables (lactate, respiratory rate, MAP) suggests clinical validity beyond just predictive accuracy.
- **Open datasets:** Use of public data enables reproducibility and future work.

**Weaknesses:**
- **No clinical validation:** The paper acknowledges this limitation but the claim about "clinically meaningful" attention weights is observational. No clinician review of these findings.
- **Retrospective evaluation only:** Results are from historical data. No prospective validation or study of clinical workflow impact.
- **Modest absolute performance:** AUROC of 0.842 is good but not exceptional for a high-stakes prediction task. Positive predictive value not discussed.
- **Limited scope:** Only US intensive care units. Generalization to other settings (general wards, other countries) is unknown.
- **Lead time validation weak:** 12-hour results show AUROC drops to 0.781, suggesting model degrades quickly, limiting practical utility.

### 4. CLARITY (78/100)

**Strengths:**
- Clear problem motivation and related work section.
- Well-written abstract and introduction.
- Results table is clearly presented.
- Limitations section is honest and thoughtful.

**Weaknesses:**
- **Method section lacks detail:** The window embedding computation is not specified. The missingness mask handling is mentioned but not explained. How are continuous vital signs discretized?
- **Notation could be clearer:** Δ is introduced informally; the decay function's interaction with attention networks could be more precisely described.
- **Missing details on evaluation:** How are predictions made at inference time? What is the prediction window (sliding? centered?)?
- **Attention analysis under-specified:** What does "averaged over true positive predictions" mean exactly? How many predictions is this? Standard deviation of attention weights?
- **No code or appendix reference:** No mention of code availability or supplementary material with implementation details.

---

## Technical Issues & Questions

1. **Time decay initialization:** The paper mentions tuning "decay initialisation" but doesn't explain what the default is or why this requires tuning.

2. **Variable-specific decay:** Computing decay per variable (Δ per variable) is sensible, but the paper doesn't discuss how this interacts with sparse measurements. If a variable is never measured, what happens?

3. **Validation AUROC tuning:** Early stopping uses validation AUROC, but results report test AUROC. Were hyperparameters locked before test evaluation? (Likely yes, but should be explicit.)

4. **Baseline fairness:** GRU-D and RETAIN may have been published with MIMIC-II data; their hyperparameters may not be optimal for MIMIC-IV/eICU.

---

## Minor Issues

- Table 1: qSOFA has no error bars (as expected for rule-based method), but logistic regression shows ±0.000, which suggests minimal variance—unusual and warrants explanation.
- "Sepsis-3 definition" referenced but not fully defined in main text.
- Discussion of why lead time degrades (Section 5) is missing.

---

## Missing Experiments

1. Comparison of different decay functions (e.g., power law, linear with max threshold).
2. Sensitivity analysis on the six-hour prediction window.
3. Error analysis: what types of cases does the model miss?
4. Comparison of attention weights for true positives vs. false positives.
5. Learning curves showing how much validation data is needed.

---

## Strengths Summary

✓ Well-motivated clinical problem  
✓ Sound experimental methodology  
✓ Modest but consistent improvements  
✓ Interpretability analysis aligned with clinical knowledge  
✓ Public datasets, reproducible  
✓ Honest about limitations  

## Weaknesses Summary

✗ Limited technical novelty (incremental extension)  
✗ Unfair baseline comparison (asymmetric hyperparameter tuning)  
✗ Missing implementation details  
✗ No prospective validation or clinical workflow study  
✗ Improvements modest and not statistically tested  
✗ Time decay design not well justified  

---

## Questions for Authors

1. How were baselines re-tuned on your specific datasets? If not, why is this fair comparison?
2. Can you provide ablation comparing to RETAIN with post-hoc exponential decay?
3. What is the positive predictive value at your chosen operating point?
4. Why does performance degrade so much at 12 hours?

---

## Recommendation Justification

This is a solid paper that makes a useful but incremental contribution to an important clinical problem. The work is technically sound and experimentally reasonable, with honest acknowledgment of limitations. However, the novelty is limited (adding decay to RETAIN is straightforward), and the empirical improvements, while consistent, are modest. The lack of prospective validation and unclear fairness in baseline comparison are concerning.

The paper is above the threshold for a workshop or applications track, but for a top-tier venue, it represents incremental progress rather than a significant advance. The interpretability aspect is valuable but not deeply explored. For clinical impact, the work needs prospective validation and workflow integration studies, which are absent.

**This paper merits publication but with reservations about impact.**

---

## Final Scores

| Criterion | Score |
|-----------|-------|
| Soundness | 75 |
| Novelty | 62 |
| Significance | 73 |
| Clarity | 78 |
| **Average** | **72** |

---

## Final Recommendation

**ACCEPT** (with minor revisions)

**Justification:** The paper presents a technically sound, well-executed study on an important clinical problem. While novelty is incremental, the consistent empirical improvements across two datasets, combined with meaningful interpretability analysis, warrant publication. The honest discussion of limitations (retrospective only, no workflow study) and clear acknowledgment of the incremental nature are appreciated. 

However, the authors should:
1. Clarify baseline tuning fairness
2. Provide more implementation details
3. Add statistical significance testing
4. Discuss the modest performance gains at extended lead times

This work will be valuable to the clinical ML community, especially those working on sepsis prediction and irregular time series, even if it does not represent a major technical breakthrough.