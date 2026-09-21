# Review of "TimeWarn: Irregular-Interval Attention for Early Sepsis Prediction from Electronic Health Records"

## Soundness: 75/100

**Strengths:**
- Solid experimental design with proper train/validation/test splits by patient
- Evaluation on two independent, public datasets (MIMIC-IV and eICU)
- Multiple random seeds reported with standard deviations
- Reasonable ablation study demonstrating the value of time decay
- Clear baseline comparisons including relevant methods (GRU-D, RETAIN)

**Weaknesses:**
- The time decay function is relatively simple (exponential with learned linear scaling). Limited justification for why this particular form is optimal
- Grouping measurements into hourly windows may lose temporal resolution; sensitivity to this choice is not explored
- Label noise acknowledged but not addressed (Sepsis-3 labels depend on culture/antibiotic timing)
- No discussion of computational complexity or inference time compared to baselines
- The improvement over GRU-D, while consistent, is modest (1.6% AUROC on MIMIC-IV)
- Missing details on how demographic variables are incorporated into the time-decay mechanism

## Novelty: 65/100

**Strengths:**
- Extending interpretable attention (RETAIN) to handle irregular intervals is a meaningful contribution
- The specific approach of modulating both visit-level and variable-level attention with learned time decay is novel
- Application to sepsis prediction with careful attention to clinical relevance

**Weaknesses:**
- The core innovation is relatively incremental: combining existing ideas (RETAIN's two-level attention + GRU-D's time decay)
- Time decay functions in temporal models are well-established (GRU-D, Neural ODEs)
- The architecture closely mirrors RETAIN with time modulation added
- Limited conceptual innovation beyond engineering two existing approaches together

## Significance: 70/100

**Strengths:**
- Sepsis is a critical clinical problem with high mortality; early prediction is clinically important
- Results are consistent across two datasets with different characteristics
- Attention analysis aligns with clinical criteria (lactate, respiratory rate, MAP), supporting clinical validity
- Modest improvements maintained at 12-hour lead time, suggesting robustness

**Weaknesses:**
- Retrospective evaluation only; no prospective validation or assessment of clinical impact
- Improvements over strong baselines are modest (1-2% AUROC)
- No evaluation of false positive rate impact on clinical workflow
- Limited to intensive care units; generalization to general wards unclear
- The clinical significance of 0.842 vs. 0.826 AUROC is not discussed—what does this mean for patient outcomes?
- No cost-benefit analysis of alerts (sensitivity vs. specificity trade-offs)

## Clarity: 82/100

**Strengths:**
- Well-structured paper with clear motivation
- Good use of tables and results presentation
- Method section is generally understandable
- Related work properly contextualizes contributions
- Limitations section is honest and thorough

**Weaknesses:**
- The hourly windowing procedure could be explained more clearly upfront
- How exactly are embeddings computed from measured values? More detail needed
- The "missingness mask" is mentioned but not explained
- Decay function notation could be clearer (why max(0, w·Δ + b)? When would this be negative?)
- Missing implementation details (e.g., attention softmax, how predictions are mapped to binary classification)
- Limited discussion of why decay performs better on variable-level vs. visit-level attention

## Minor Issues:
- Table 1: Standard deviations for qSOFA and logistic regression are suspiciously zero
- No discussion of statistical significance testing
- Hyperparameter tuning was extensive for TimeWarn (72 configurations) but baselines use published hyperparameters—potential fairness concern

---

## Final Average Score: 73/100

## Recommendation: **Accept with Minor Revisions**

### Justification:

This paper makes a solid incremental contribution to an important clinical problem. The combination of interpretable attention with time-decay modulation is sensible and well-executed, with consistent improvements over strong baselines on two datasets. The attention analysis provides clinical interpretability, which is valuable for adoption.

However, the novelty is primarily engineering-focused rather than conceptual, improvements are modest, and the work is purely retrospective without demonstrated clinical impact. The paper would be strengthened by:
1. Prospective validation or simulation studies of alert impact
2. More thorough ablation on design choices (hourly windowing, decay function form)
3. Deeper analysis of the modest improvements and their clinical significance
4. Better clarity on implementation details

The work is technically sound and addresses a real problem with a principled approach. It merits publication as a solid empirical contribution to the clinical ML literature, though it is not groundbreaking.