# Peer Review: TimeWarn: Irregular-Interval Attention for Early Sepsis Prediction

## Soundness (75/100)

**Strengths:**
- The methodological approach is sensible: combining time-aware decay with two-level attention is a natural extension of RETAIN to irregular time series
- The decay function (γ = exp(−max(0, w·Δ + b))) is simple and interpretable
- Experimental design follows good practices: multiple seeds (5), proper train/val/test splits by patient, evaluation on two independent datasets
- Statistical reporting includes standard deviations, enabling significance assessment
- Ablation study demonstrates that time decay contributes meaningfully (0.842 → 0.824)

**Weaknesses:**
- **Limited technical depth**: The time decay mechanism is relatively simple. The paper doesn't justify why exponential decay is appropriate or compare alternatives (linear decay, power laws, learned basis functions)
- **Hyperparameter tuning disparity**: TimeWarn uses grid search over 72 configurations; baselines use published hyperparameters. This creates unfair comparison, especially for RETAIN and GRU-D, which could potentially benefit from similar tuning
- **Statistical significance not formally tested**: While improvements are modest (0.016-0.023 AUROC), confidence intervals overlap slightly with GRU-D. No hypothesis tests are provided
- **Missing implementation details**: 
  - How are hourly windows constructed when measurements are sparse?
  - How is Δ computed when variables have different measurement histories?
  - What prevents trivial solutions (e.g., decay weights → 0)?
- **Reproducibility concerns**: No mention of code availability; some hyperparameter choices undefined (e.g., hidden size 128 - was this tuned?)

## Novelty (62/100)

**Strengths:**
- First application of time-decayed attention to this specific problem (sepsis prediction with RETAIN-like architecture)
- The combination of visit-level and variable-level time decay is novel, if incremental

**Weaknesses:**
- **Limited conceptual novelty**: The core contribution is applying exponential decay to attention weights. This is a straightforward engineering extension, not a fundamental insight
- **Time-aware EHR models are established**: GRU-D (2016) and Neural ODEs already handle irregular intervals. TimeWarn's innovation is modest—essentially replacing the RNN with decay-scaled attention
- **Attention mechanisms for time series exist**: The combination isn't particularly surprising to researchers familiar with temporal models and attention
- **Incremental over RETAIN**: The paper positions this as extending RETAIN to irregular times, making the baseline comparison point somewhat circular

## Significance (70/100)

**Strengths:**
- **Clinical relevance**: Sepsis prediction is a genuine clinical need; early warnings have life-or-death stakes
- **Practical interpretability**: Clinicians can inspect which variables and time points drive predictions, addressing a real adoption barrier
- **Consistent improvements**: Results hold across two large, independent datasets (MIMIC-IV: n=31,244; eICU: n=42,117)
- **Real-world applicability**: The model handles actual EHR data structure (irregular sampling), unlike many academic approaches

**Weaknesses:**
- **Marginal performance gains**: 0.016–0.023 AUROC improvements are clinically meaningful but not transformative. At AUROC ~0.84, many false positives and false negatives remain
- **No clinical validation**: The paper acknowledges this limitation well, but significance is ultimately unproven without prospective evaluation or workflow impact studies
- **Limited scope**: Evaluation restricted to ICU data; generalization to ward-level monitoring or other health systems unknown
- **Label noise not quantified**: Sepsis-3 definitions depend on culture timing/antibiotic decisions—how much does label noise affect conclusions?

## Clarity (82/100)

**Strengths:**
- Well-written abstract and introduction clearly motivate the problem
- Method section is concise and mostly understandable
- Results presentation is clean; table format is clear
- Good acknowledgment of limitations

**Weaknesses:**
- **Method section lacks detail**: 
  - How exactly are "hourly windows" computed from irregular data?
  - The decay formula uses max(0, w·Δ + b)—why not allow negative values?
  - What is the embedding computation from "measured values and a missingness mask"?
- **Missing figure**: A diagram of the architecture would aid understanding, especially the flow of decay factors
- **Attention analysis is shallow**: "Highest weights assigned to lactate, respiratory rate, MAP" is reported but not rigorously analyzed. Do these patterns hold across prediction horizons or patient subgroups?
- **Limited error analysis**: No discussion of false positives vs. false negatives or failure mode analysis

## Detailed Comments

1. **Table 1 interpretation**: The standard deviations for logistic regression are exactly 0.000, which is suspicious. Are these deterministic? Why do neural models have variance but LR doesn't?

2. **Ablation**: The ablation (removing decay → 0.824) is helpful but incomplete. What about removing only visit-level decay? What about unfrozen vs. learned decay parameters?

3. **Lead time experiment**: The 12-hour result (0.781 vs. 0.768) shows degradation but would benefit from a full lead-time curve and comparison of all methods

4. **Generalization**: The paper notes US-only ICU data as a limitation. This significantly limits the claim of a general-purpose method

5. **Clinical criteria alignment**: The observation that learned attention matches qSOFA/NEWS criteria is reassuring but somewhat circular—if the model learns to emphasize these variables, it's not clear whether this represents genuine understanding or overfitting to correlated signals

## Missing Related Work

The paper could better position relative to:
- Set Functions for Time Series (NeurIPS 2020) and similar permutation-invariant temporal models
- Recent work on transformer-based EHR models
- Continuous-time models beyond Neural ODEs (e.g., Kolmogorov-Arnold representations)

## Reproducibility Assessment

**Concern**: While sufficient detail is provided for reimplementation, the lack of code availability and specific hyperparameter initialization details (especially for baselines) raises reproducibility questions. The 72-configuration grid search for TimeWarn versus fixed hyperparameters for baselines is particularly problematic.

---

## Summary Table

| Criterion | Score | Comment |
|-----------|-------|---------|
| Soundness | 75 | Valid approach, but unfair baseline tuning and limited technical justification |
| Novelty | 62 | Straightforward engineering extension, incremental over RETAIN and prior time-aware models |
| Significance | 70 | Clinically relevant problem with consistent gains, but improvements modest and no prospective validation |
| Clarity | 82 | Generally well-written; some method details missing; needs architecture figure |
| **Average** | **72** | **Borderline paper with solid engineering but limited novelty** |

---

## Final Recommendation: **REJECT**

### Justification

This paper presents a competent engineering contribution that achieves modest improvements on an important clinical problem. However, it falls short of the standards for a top-tier venue:

1. **Novelty is incremental**: The core contribution—applying exponential decay to attention weights—is a straightforward extension. It's a sensible idea but lacks conceptual depth or surprising insights.

2. **Unfair experimental comparison**: The hyperparameter tuning asymmetry (72 configurations for TimeWarn, published parameters for baselines) makes it impossible to assess whether improvements reflect the method itself or simply better hyperparameter optimization.

3. **Limited validation of claims**: The attention analysis showing alignment with clinical criteria is interesting but anecdotal. Systematic analysis across different prediction windows and patient subgroups would strengthen claims.

4. **Significance is unproven clinically**: While AUROC improvements are consistent, their clinical meaningfulness remains unvalidated. Prospective evaluation is essential for clinical tools.

5. **Technical novelty is minimal**: The decay function and its application are not sufficiently novel or insightful for a strong contribution.

### Recommendations for Authors (if resubmitting)

- **Fair comparison**: Tune all baseline hyperparameters using identical methodology
- **Deeper technical work**: Justify the decay function choice; compare alternatives; analyze learned parameters
- **Systematic attention analysis**: Use metrics beyond visual inspection; correlate attention patterns with clinical outcomes across subgroups
- **Prospective validation**: At least pilot testing in a clinical setting
- **Ablation completeness**: Isolate visit-level vs. variable-level decay contributions
- **Architecture clarity**: Provide a detailed diagram and formal algorithmic description

---

**Overall Assessment**: A well-executed but incremental study that would be better suited for a specialized venue (e.g., medical AI conference) rather than a general machine learning conference. The work is sound but lacks the novelty and proven significance expected at top-tier venues.