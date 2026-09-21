# Peer Review: TimeWarn - Irregular-Interval Attention for Early Sepsis Prediction

## Summary

This paper proposes TimeWarn, an attention-based neural network model for predicting sepsis onset 6 hours in advance using irregularly sampled electronic health records. The method extends the RETAIN architecture by incorporating learned time decay functions to modulate attention weights. The authors evaluate on MIMIC-IV and eICU datasets, showing improvements over strong baselines including GRU-D and RETAIN.

## Detailed Assessment

### Soundness: 78/100

**Strengths:**
- The core methodological contribution is technically sound: incorporating time decay into attention weights is a reasonable approach to handle irregular sampling
- The experimental setup follows appropriate practices: patient-level splits, multiple random seeds, reporting of standard deviations
- Ablation study (Section 5) validates that time decay contributes meaningfully to performance
- Honest discussion of limitations (Section 6) acknowledges retrospective nature and label noise concerns
- Clinical alignment (attention to lactate, respiratory rate) provides face validity

**Weaknesses:**
- **Time decay formulation lacks justification**: The choice of γ = exp(−max(0, w·Δ + b)) appears ad-hoc. Why this specific functional form? Why per-variable decay? Why multiply variable-level but average for visit-level? No theoretical or empirical justification is provided.
- **Limited analysis of learned decay parameters**: What values do w and b converge to? Do they make clinical sense? Are they interpretable? This is never reported.
- **Hyperparameter tuning asymmetry**: TimeWarn undergoes extensive grid search (72 configurations), while baselines use published hyperparameters. This could bias results in favor of TimeWarn. Did authors tune baselines equally?
- **Statistical significance**: While standard deviations are provided, confidence intervals and significance tests are absent. Are 0.016 AUROC improvements statistically significant?
- **Missing details**: 
  - How are multiple measurements of the same variable within a window aggregated?
  - How is the decay initialized? What is the initialization scheme?
  - Computational complexity not discussed
- **Label noise**: The Sepsis-3 definition can produce noisy labels (acknowledged), but no analysis of label reliability or impact is provided

### Novelty: 72/100

**Strengths:**
- Combining learned time decay with two-level attention is novel and well-motivated
- The specific approach of separately scaling variable-level and visit-level attention with time information is a reasonable extension of RETAIN
- The problem (irregular sampling in sepsis prediction) is clinically important and previously underexplored

**Weaknesses:**
- The core ideas are incremental: RETAIN provides the architecture; GRU-D demonstrates time decay in RNNs; this work combines these existing concepts
- The novelty is primarily engineering-focused rather than introducing new principles or theory
- The time decay mechanism is relatively simple; more sophisticated approaches (e.g., Neural ODEs mentioned but dismissed without comparison) exist
- The contribution feels more like a targeted improvement than a fundamental advance

### Significance: 75/100

**Strengths:**
- Sepsis prediction is a high-impact clinical problem with clear mortality implications
- Retrospective improvement of 0.016 AUROC on MIMIC-IV, 0.013 on eICU demonstrates measurable gains
- The interpretability angle (attention visualization) addresses clinical adoption barriers
- Attention analysis showing clinically relevant variables (lactate, respiratory rate) strengthens practical value
- Two-dataset evaluation shows some generalization

**Weaknesses:**
- **No prospective validation**: The paper explicitly acknowledges this limitation. Retrospective improvements don't guarantee clinical utility.
- **Unclear clinical impact**: A 0.016 AUROC improvement translates to what in terms of sensitivity/specificity trade-offs? How many additional true cases would be caught? How many false alarms?
- **Missing downstream analysis**: No discussion of operating points, cost-benefit analysis, or usability in clinical workflows
- **Limited scope**: Evaluation restricted to US intensive care units; generalizability to other settings unknown
- **Timing assumption**: Why 6 hours specifically? How sensitive are results to prediction horizon? Limited lead time analysis (only 12 hours shown).

### Clarity: 82/100

**Strengths:**
- Paper is well-written and organized logically
- Clear problem statement and motivation
- The method section is generally clear, and results are presented cleanly
- Appropriate use of tables and structured presentation

**Weaknesses:**
- **Method section underspecifies details**:
  - How exactly is the hourly window embedding computed from multiple measurements?
  - What happens when a variable has no measurement in a window?
  - The masking approach deserves more detail
- **Time decay explanation could be clearer**: The per-variable decay formulation is introduced briefly without intuitive explanation. Why does taking max(0, w·Δ + b) make sense?
- **Missing notation**: Mathematical notation could be more formal/precise in places
- **Attention analysis superficial**: "Averaged over true positive predictions" — how many examples? What is the variance? How were variables selected?
- **Figure missing**: A visualization of the architecture or attention weights over time would strengthen understanding

### Minor Issues

1. Related work section is adequate but could better position against recent temporal modeling work
2. The claim that models "treat a lactate value recorded ten minutes ago the same as one recorded eight hours ago" is somewhat strawman-ish; many statistical methods do implicitly account for recency
3. Table 1: Logistic regression shows ±0.000 which seems suspicious — likely a reporting/rounding artifact
4. No discussion of computational cost or inference time
5. Reproducibility: Code availability not mentioned

## Questions for Authors

1. How were the 72 grid search configurations chosen? What was the parameter space?
2. Were baselines (especially GRU-D and RETAIN) hyperparameter-tuned equally?
3. What are the learned w and b values? Do they have clinical interpretation?
4. What is the sensitivity/specificity at AUROC-optimal operating points?
5. How many additional true positives does the 0.016 improvement represent at a fixed specificity?
6. Why use simple exponential decay rather than more sophisticated temporal models?

## Missing Comparisons

- No comparison with temporal point processes or other recent irregular time series methods
- Neural ODE models mentioned but not compared (computational cost is cited as reason, but no numbers provided)

## Reproducibility Concerns

- Code availability not mentioned
- Some hyperparameter initialization details missing
- Exact Sepsis-3 inclusion/exclusion criteria could be clearer

## Recommendation Justification

This is a competent paper that makes a solid incremental contribution to an important clinical problem. The time-decay enhanced attention approach is sensible and shows consistent improvements over baselines on two datasets. The attention-based interpretability is valuable for clinical adoption.

However, the novelty is primarily engineering-focused rather than conceptual, the improvements are modest (0.016 AUROC), and most importantly, **there is no prospective validation or evidence of clinical impact**. The paper honestly acknowledges this, but it significantly limits significance for a clinical application paper.

The technical soundness has concerns around hyperparameter tuning fairness and lack of justification for design choices. The significance would be substantially strengthened by prospective validation, sensitivity/specificity analysis at clinically relevant operating points, or at least analysis of what the AUROC improvement means in practice.

This paper is above the acceptance threshold for a machine learning venue (solid technical work on an important problem), but not by a large margin. For a clinical venue, the lack of prospective validation would be more problematic.

---

## Scores

| Dimension | Score |
|-----------|-------|
| Soundness | 78 |
| Novelty | 72 |
| Significance | 75 |
| Clarity | 82 |
| **Average** | **76.75** |

## Final Recommendation

**ACCEPT** (with reservations)

This paper merits publication as a solid technical contribution to clinical machine learning on an important problem. The work is sound, the results are positive and consistent across datasets, and interpretability analysis is appreciated. However, it is not a strong accept due to limited novelty, modest improvements, and lack of prospective validation. The authors should be encouraged to pursue clinical validation as follow-up work.