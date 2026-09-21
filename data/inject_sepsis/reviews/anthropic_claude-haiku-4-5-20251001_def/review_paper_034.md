# Peer Review: TimeWarn: Irregular-Interval Attention for Early Sepsis Prediction

## SOUNDNESS: 78/100

**Strengths:**
- Solid methodological foundation combining established techniques (RETAIN architecture + time decay)
- Evaluation on two large, public datasets (MIMIC-IV, eICU) with appropriate train/val/test splits
- Results reported with mean and standard deviation over 5 random seeds, demonstrating reproducibility considerations
- Appropriate task definition (6-hour prediction window) with clinical relevance
- Attention analysis validates findings against known clinical criteria (lactate, respiratory rate)

**Weaknesses:**
- **Limited novelty in time modeling**: The time decay function γ = exp(−max(0, w·Δ + b)) is relatively simple and not well justified. Why this particular functional form? Why max(0, ...)? The related work mentions GRU-D's learned decay, but the distinction from that approach is unclear.
- **Aggregation concerns**: Grouping measurements into hourly windows may obscure clinically important sub-hour variations, especially for vital signs. The paper doesn't justify this design choice or test sensitivity to window size.
- **Label noise acknowledged but not addressed**: The authors note that Sepsis-3 labels depend on cultures and antibiotics timing, creating potential label noise, but take no steps to mitigate this (e.g., sensitivity analysis, confidence weighting).
- **Modest improvements**: GRU-D achieves 0.826 AUROC on MIMIC-IV; TimeWarn achieves 0.842—a 0.016 improvement. While consistent, the gains are incremental. Statistical significance testing is absent.
- **Incomplete ablation**: The ablation study only examines presence/absence and placement of decay. No ablation on: hourly windowing, decay function form, decay initialization effects, or architectural choices (hidden size, GRU vs. LSTM, etc.).
- **Hyperparameter tuning asymmetry**: TimeWarn undergoes grid search over 72 configurations; baselines use published hyperparameters. This introduces potential bias favoring TimeWarn.

## NOVELTY: 62/100

**Strengths:**
- Addresses a genuine gap: combining interpretable attention (RETAIN) with irregular sampling
- Two-level attention modulation by decay is a reasonable contribution

**Weaknesses:**
- **Limited technical novelty**: Applying learned decay to attention weights is a relatively straightforward extension of GRU-D (which applies decay to hidden states/inputs). The conceptual leap is incremental.
- **Decay function not novel**: Exponential decay with learned parameters is standard in the literature
- **Architecture otherwise follows RETAIN closely**: The core contribution is essentially replacing fixed attention with decay-modulated attention
- **No comparison to simpler alternatives**: What if you just applied GRU-D's decay mechanism to RETAIN? Was that tried?
- **Limited scope**: Application is narrowly focused on sepsis; generalizability to other clinical prediction tasks unclear

## SIGNIFICANCE: 72/100

**Strengths:**
- **High clinical relevance**: Sepsis is a major source of ICU mortality; 6-hour advance warning has actionable value
- **Interpretability for clinical adoption**: Attention weights provide explanations clinicians can understand
- **Reproducible on public data**: Enables future work and validation
- **Consistent improvements across datasets**: Robustness across MIMIC-IV and eICU suggests generalizability within ICU settings

**Weaknesses:**
- **No prospective validation**: All evaluation is retrospective. The authors acknowledge this but provide no pathway or preliminary data suggesting clinical efficacy
- **No workflow impact assessment**: Unknown whether clinicians would act on TimeWarn alerts or if outcomes would improve. Real-world benefit undemonstrated.
- **Limited scope of evaluation**: Only intensive care units in the US; unclear if findings transfer to general wards, developing countries, or non-US health systems
- **Modest absolute performance**: AUROC 0.842 leaves substantial room for error in clinical use
- **12-hour prediction much weaker**: At 12 hours (0.781 AUROC), predictive power drops significantly, limiting clinical utility for longer planning horizons
- **No discussion of false positive rates at clinically relevant operating points**: AUROC/AUPRC aggregate metrics don't clarify PPV/NPV at decision thresholds

## CLARITY: 82/100

**Strengths:**
- Well-structured paper with clear motivation
- Mathematical notation is mostly clear (decay function equation, attention mechanism)
- Good use of related work to position contributions
- Results table is informative with error bars
- Attention analysis section provides interpretable validation

**Weaknesses:**
- **Missing implementation details**: 
  - How are visits with no measurements in a window handled?
  - How exactly are embeddings computed from measurements + missingness mask?
  - What is the missingness mask representation?
- **Insufficient methodological clarity**:
  - The visit-level attention multiplication by mean decay is mentioned casually; more justification needed
  - Why max(0, w·Δ + b) rather than just w·Δ + b?
  - How is Δ computed when a variable has never been measured?
- **Reproducibility concerns**: No mention of code availability, hyperparameter configurations tested, or random seed details
- **Limited discussion of failure cases**: When does TimeWarn fail? Are there patient subgroups where performance is poor?
- **Attention analysis section is brief**: Would benefit from visualizations (e.g., heatmaps showing attention over time for individual cases)

## DETAILED COMMENTS

1. **Data preprocessing**: The paper mentions using 32 variables but doesn't describe imputation strategy, normalization, or handling of lab tests with different reporting units

2. **Baselines**: Including qSOFA is good for clinical context, but GRU-D and RETAIN are the most relevant comparisons. Why not compare to more recent temporal models (e.g., Transformers with positional encodings)?

3. **Statistical significance**: The improvements over GRU-D (0.016 on MIMIC-IV, 0.013 on eICU) are small relative to standard deviations. A significance test (e.g., t-test across 5 seeds) would strengthen claims

4. **Generalization**: Does the learned decay function vary substantially across datasets? This might indicate dataset-specific tuning rather than a principled approach

5. **Clinical validity**: Lactate and respiratory rate are highlighted as important, but were these also identified by GRU-D or RETAIN? Without cross-baseline attention analysis, it's unclear if TimeWarn's interpretability is superior

## MISSING EXPERIMENTS

- Sensitivity to hourly windowing choice (e.g., 2-hour, 4-hour windows)
- Cross-dataset generalization (train on MIMIC-IV, test on eICU)
- Analysis of predictions near decision threshold (e.g., calibration curves)
- Fairness analysis across patient subgroups (age, sex, comorbidities)

## MINOR ISSUES

- Abstract claims "interpretable" but doesn't defend this claim strongly
- Section 3 could benefit from pseudocode or a diagram
- Some citations are incomplete (e.g., "Choi et al., 2016" for RETAIN should be in References)

---

## FINAL SCORES

| Criterion | Score |
|-----------|-------|
| Soundness | 78 |
| Novelty | 62 |
| Significance | 72 |
| Clarity | 82 |
| **Average** | **73.5** |

---

## RECOMMENDATION: **ACCEPT** (with reservations)

### Justification

This paper presents a competent, well-executed study that makes a modest but solid contribution to an important clinical problem. The idea of modulating attention by learned time decay is intuitive and sensible, and the empirical results demonstrate consistent, if incremental, improvements over strong baselines on two large datasets. The interpretability angle is valuable for clinical adoption.

However, the technical novelty is limited—this is primarily an engineering contribution combining existing techniques rather than a fundamental advance. The improvements are incremental (0.016 AUROC on the larger dataset). The lack of prospective validation, workflow studies, or real-world outcome data means clinical significance remains theoretical.

**For a venue emphasizing applied machine learning and clinical impact** (e.g., ML4H, JAMIA, Digital Medicine), this merits acceptance as a solid contribution that advances the state-of-the-art on a clinically important task with reproducible results and reasonable interpretability.

**For a venue emphasizing fundamental novelty** (e.g., ICML, NeurIPS), this would be a weak accept or borderline reject due to limited technical innovation.

The paper is above the acceptance threshold: sound methodology, adequate novelty for applied venues, meaningful clinical relevance, and clear presentation. However, it is not a strong accept—the incremental nature of improvements, limited scope of evaluation, and missing ablations/analyses prevent a higher recommendation.