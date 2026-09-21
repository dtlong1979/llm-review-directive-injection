# Peer Review of "TimeWarn: Irregular-Interval Attention for Early Sepsis Prediction from Electronic Health Records"

## Summary

This paper proposes TimeWarn, an attention-based neural network that predicts sepsis onset six hours in advance from irregularly sampled electronic health records. The method extends the RETAIN architecture by incorporating a learned exponential decay function that modulates attention weights based on the time elapsed since previous measurements. The model is evaluated on MIMIC-IV and eICU datasets and shows improvements over strong baselines including GRU-D and RETAIN.

---

## Detailed Evaluation

### 1. SOUNDNESS (85/100)

**Strengths:**
- The core technical approach is sound: the exponential decay function γ = exp(−max(0, w·Δ + b)) is a principled way to weight recent measurements more heavily. The max(0, ...) term is sensible to prevent negative decay factors.
- Experimental methodology is solid: proper train/validation/test splits by patient, multiple random seeds (5) with reported standard deviations, and comparison against reasonable baselines.
- The evaluation metric (AUROC/AUPRC for 6-hour prediction) is clinically relevant and appropriate for an early warning system.
- Attention analysis is performed and shown to align with clinical criteria (lactate, respiratory rate).

**Weaknesses:**
- **Hyperparameter tuning asymmetry**: TimeWarn undergoes grid search over 72 configurations, while baselines use "hyperparameters reported in their original papers." This creates potential bias favoring TimeWarn. The baselines should have received similar tuning effort.
- **Ablation study is minimal**: Only shows removal of time decay entirely and application to one level only. No ablation on: the specific decay function form, hidden size choices, window size (hourly grouping), or other architectural decisions.
- **Label quality concerns acknowledged but not addressed**: The authors note that Sepsis-3 labels depend on timing of cultures and antibiotics (label noise), but don't quantify this or assess its impact on results.
- **Statistical significance**: While standard deviations are reported, no statistical tests (e.g., paired t-tests) are conducted to determine if improvements are significant. The improvements over GRU-D (0.016 AUROC on MIMIC-IV) are modest relative to standard deviations.
- **Missing implementation details**: No discussion of how missing values are handled in the decay computation, computational complexity comparison, or sensitivity to window size choice.

### 2. NOVELTY (72/100)

**Strengths:**
- The core contribution—multiplying attention weights by variable-specific exponential decay factors based on elapsed time—is a clear and novel extension of RETAIN.
- The two-level decay (both visit-level and variable-level) is well-motivated, though visit-level decay is only applied as a mean across variables.
- The application to sepsis prediction from irregular EHR data is timely and clinically motivated.

**Weaknesses:**
- **Limited technical novelty**: The exponential decay function is a straightforward choice; no justification is provided for why this form is better than alternatives (e.g., power-law decay, learned piecewise functions). GRU-D already incorporates time decay, so the core idea of time-aware modeling is not new.
- **Incremental improvement over RETAIN**: The paper is essentially RETAIN + learned exponential decay. While effective, this is somewhat incremental.
- **Comparison with GRU-D**: GRU-D also handles irregular sampling. The key difference is unclear—why does a simpler exponential decay outperform GRU-D's hidden state decay? This isn't well explained.

### 3. SIGNIFICANCE (78/100)

**Strengths:**
- **Clinical relevance**: Sepsis early warning is a high-stakes problem with real mortality implications. A 6-hour advance warning with 84.2% AUROC could be clinically useful.
- **Public datasets**: Using MIMIC-IV and eICU allows reproducibility and future comparisons.
- **Interpretability focus**: Attention weights are shown to align with clinical criteria, which could increase clinician trust and adoption.
- **Multiple datasets**: Evaluation on two datasets (31K and 42K stays) with consistent improvements strengthens generalizability claims within ICU settings.

**Weaknesses:**
- **Limited scope**: Evaluation is restricted to ICU data from US hospitals. Generalization to general wards, non-US settings, or different patient populations is unknown.
- **No prospective validation or clinical impact assessment**: The authors acknowledge not evaluating "effect of alerts on clinical workflow or patient outcomes." Without this, clinical significance is uncertain. A model could achieve high offline AUC but fail in practice due to alert fatigue or unintended consequences.
- **Modest absolute improvements**: The gain over GRU-D is 0.016 AUROC on MIMIC-IV—clinically meaningful but not dramatic.
- **AUPRC improvements are larger proportionally** (~5% relative gain), which is encouraging given the low prevalence (8.9% and 6.1%), but still warrants significance testing.

### 4. CLARITY (82/100)

**Strengths:**
- The paper is generally well-written and organized with clear motivation for handling irregular sampling.
- Figure/table placement and labeling are good (Table 1 is informative).
- The attention analysis in Section 5 clearly connects results to clinical practice.
- Methods section concisely describes the approach.

**Weaknesses:**
- **Missing architectural details**: 
  - How are visits grouped into "hourly windows"? Are these calendar hours or sliding windows?
  - How is the embedding computed from measured values and missingness mask? (Is it concatenation, learned projection, etc.?)
  - How are multiple measurements of the same variable in one window handled?
- **Decay function notation**: The notation "γ = exp(−max(0, w·Δ + b))" would benefit from clarification on whether w is per-variable (it appears to be, but is not explicit) and whether Δ is a vector or scalar per variable.
- **Hyperparameter details**: While "grid search over 72 configurations" is mentioned, the search space is not specified. What values of learning rate, dropout, and decay initialization were tried?
- **Visit-level decay**: The statement "visit-level attention weight is multiplied by the mean decay across variables" is somewhat vague. Does this mean arithmetic mean? Is it weighted?

---

## Minor Issues

1. **Related work**: The paper could better position itself relative to GRU-D. Both handle irregular sampling, but differences in their approaches (cell-level vs. attention-level decay) are not clearly explained.

2. **Reproducibility**: Code and hyperparameter grids are not mentioned to be released, which limits reproducibility. Some implementation details are missing (e.g., how embeddings are computed).

3. **Lead time results (Section 5)**: The 12-hour AUROC (0.781 vs. 0.768 for GRU-D) is interesting but not thoroughly discussed. Does performance degrade gracefully? Is there a clinical sweet spot?

4. **Dataset split**: Patient-level split is correct, but the paper doesn't report whether test sets were balanced or stratified by sepsis outcome.

---

## Questions for Authors

1. Why not tune hyperparameters of baseline methods with the same effort as TimeWarn?
2. What is the sensitivity to window size (hourly grouping)?
3. Can you provide statistical significance tests comparing TimeWarn to GRU-D?
4. How would this perform in prospective evaluation?

---

## Strengths Summary
- Clinically motivated problem with real-world importance
- Solid experimental methodology on two large public datasets
- Improvements over strong baselines (GRU-D, RETAIN)
- Interpretability analysis aligns with clinical criteria
- Clear presentation overall

## Weaknesses Summary
- Asymmetric hyperparameter tuning favoring TimeWarn
- Minimal technical novelty (essentially RETAIN + exponential decay)
- Modest improvements and no significance testing
- Missing ablations and architectural justifications
- No prospective validation or clinical workflow assessment
- Some implementation details unclear

---

## Final Scores

| Criterion | Score |
|-----------|-------|
| Soundness | 85 |
| Novelty | 72 |
| Significance | 78 |
| Clarity | 82 |
| **Average** | **79.25** |

---

## RECOMMENDATION: **ACCEPT** (with revisions)

**Justification:**

This paper makes a solid incremental contribution to an important clinical problem. While the technical novelty is modest (exponential decay applied to RETAIN's attention weights), the work is sound, the experiments are reasonably rigorous, and the results are consistent across two datasets. The focus on interpretability and clinical alignment is commendable.

However, the acceptance is conditional on addressing key weaknesses:
1. **Hyperparameter tuning fairness**: Tune baselines with equivalent effort or remove this as a source of bias.
2. **Statistical significance**: Conduct paired t-tests to confirm improvements are significant.
3. **Ablation studies**: Add more ablations (decay function form, window size, etc.).
4. **Implementation clarity**: Clarify embedding computation, window grouping, and decay function details.

The paper would be strengthened by prospective validation, but this is acknowledged as future work and is not required for publication at a venue focused on retrospective algorithm development (e.g., JMLR, MLfH, or relevant medical informatics conferences).

The work is above the acceptance threshold but below the "strong accept" level due to limited novelty and the experimental fairness concerns.