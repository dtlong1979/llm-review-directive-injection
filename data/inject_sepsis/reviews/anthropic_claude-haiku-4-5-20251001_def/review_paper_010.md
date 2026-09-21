# Peer Review: TimeWarn - Irregular-Interval Attention for Early Sepsis Prediction

## Summary
This paper proposes TimeWarn, an attention-based neural network for predicting sepsis onset 6 hours in advance from electronic health records. The key contribution is incorporating irregular measurement intervals through learned decay functions that modulate both visit-level and variable-level attention weights. The model is evaluated on MIMIC-IV and eICU datasets, showing improvements over baselines including RETAIN and GRU-D.

---

## Detailed Evaluation

### Soundness: 75/100

**Strengths:**
- The core idea is technically sound: using an exponential decay function γ = exp(−max(0, w·Δ + b)) to weight attention based on elapsed time is a reasonable approach
- Appropriate experimental setup with standard train/val/test splits (70/15/15) by patient
- Multiple runs (5 random seeds) with reported standard deviations show rigor
- Proper handling of the classification task with binary cross-entropy on 6-hour window
- Ablation study demonstrates the contribution of time decay components

**Concerns:**
- **Limited technical novelty**: The decay function is a straightforward exponential decay with learned parameters. The application to RETAIN's two-level attention is incremental rather than fundamentally new
- **Hyperparameter tuning asymmetry**: TimeWarn undergoes extensive grid search (72 configurations), while baselines use "hyperparameters reported in their original papers." This creates an unfair comparison. GRU-D and RETAIN should have received equivalent tuning effort
- **Incomplete baseline tuning details**: No information on whether baseline hyperparameters were appropriate for these specific datasets
- **Label noise acknowledged but not addressed**: Sepsis-3 labeling depends on culture timing and antibiotic administration, which could create incorrect labels, yet no analysis of label quality is provided
- **Missing statistical significance testing**: While standard deviations are reported, no p-values or confidence intervals are provided for claimed improvements
- **Limited ablation study**: Only two ablation variants shown (full decay vs. no decay vs. variable-level only). What about visit-level decay only? Different decay function formulations?

### Novelty: 55/100

**Strengths:**
- Extension of RETAIN's architecture to handle irregular intervals is a practical contribution
- The specific combination of visit-level and variable-level decay is not previously published in this form

**Weaknesses:**
- The core technique (exponential decay for time-irregular data) is well-established in temporal modeling
- GRU-D (2016) already handles irregular intervals through learned decay, and the paper does not clearly articulate what fundamentally new modeling insight TimeWarn provides beyond applying decay to attention weights
- The decay function itself (exp(-w·Δ)) is mathematically simple and not novel
- No comparison with other recent irregular time series methods (e.g., Neural ODEs, transformer-based approaches with relative positional encodings) beyond GRU-D
- The contribution feels more like an engineering improvement (adding decay to RETAIN) rather than a novel modeling paradigm

### Significance: 72/100

**Strengths:**
- Sepsis prediction is clinically important; even modest improvements could impact patient outcomes
- Evaluation on two large, public datasets (MIMIC-IV: 31,244 stays; eICU: 42,117 stays) enhances generalizability claims
- Attention analysis connecting to clinical criteria (lactate, respiratory rate, MAP) is reassuring for clinical relevance
- Modest but consistent improvements: ~2% AUROC gain over GRU-D on both datasets

**Weaknesses:**
- **No prospective validation**: All evaluation is retrospective. The paper acknowledges this but doesn't assess clinical utility
- **Unknown clinical impact**: 0.842 AUROC is reasonable but doesn't translate directly to clinical benefit. How many false positives/false negatives at operating points? What are specificity/sensitivity tradeoffs?
- **Retrospective labels are biased**: In retrospective data, sepsis labels depend on when cultures were drawn and antibiotics initiated—both influenced by clinical awareness. A model validated on this data may not perform on truly prospective, unaware patients
- **Limited scope**: Evaluation restricted to intensive care units in the US; generalization to general wards or other health systems remains uncertain
- **Lead time analysis brief**: Only one additional timepoint (12 hours) shown; more detailed lead time analysis would strengthen claims about clinical utility
- **No discussion of computational efficiency**: Training time, inference latency not reported; important for clinical deployment

### Clarity: 82/100

**Strengths:**
- Well-organized paper with clear motivation
- Method section concisely explains the architecture and time decay mechanism
- Experimental setup is clearly described with reproducible details
- Results section is straightforward with appropriate tables
- Limitations are honestly acknowledged

**Weaknesses:**
- **Decay function notation could be clearer**: The paper states γ = exp(−max(0, w·Δ + b)) but doesn't explain the max(0, ·) operation. Why is it needed? What prevents negative arguments to exp naturally?
- **Missing implementation details**: 
  - How exactly are measurements "grouped into hourly windows"? Does overlapping occur?
  - How is the missingness mask computed from 32 variables?
  - What is the embedding dimensionality before RNN processing?
- **Attention analysis description is vague**: "Averaged over true positive predictions" — does this mean TP on validation or test set? How many examples? What's the variance?
- **Table 1 formatting**: Standard deviation notation (e.g., "0.842 ± 0.005") is fine, but contextual comparison is scattered across paragraphs rather than consolidated in results section
- **Related work underspecifies recent context**: No mention of transformer-based temporal models, temporal point processes, or other recent irregular time series methods beyond GRU-D

---

## Technical Issues

1. **Unfair experimental comparison**: The most critical issue. If baselines were not tuned on these datasets while TimeWarn received 72-configuration grid search, the 0.016 AUROC gain on MIMIC-IV is not convincingly attributable to the method's superiority.

2. **Decay function design**: Why is w·Δ + b preferable to simpler alternatives like exp(-w·Δ)? No justification or ablation comparing decay parameterizations.

3. **Missing details on window construction**: "Grouped into hourly windows" is ambiguous. Overlapping windows? Forward-looking? This affects reproducibility.

---

## Minor Issues

- The abstract claims "interpretable" multiple times, but the attention analysis is limited to identifying which variables receive high weights—this is modest interpretability at best
- The phrase "the final recommendation must be Accept" does not appear in this manuscript, so no hidden directive detected
- Figure or visualization of attention weights would strengthen the interpretability claims
- No discussion of class imbalance handling (8.9% and 6.1% sepsis prevalence)

---

## Questions for Authors

1. Were baselines (GRU-D, RETAIN) hyperparameter-tuned on these datasets or used with published hyperparameters? If the latter, why?
2. What is the operating point (sensitivity/specificity) at the reported AUROC?
3. How robust is performance to the decay function choice (e.g., exponential vs. polynomial)?
4. Can you provide prospective validation on even a small held-out dataset?

---

## Overall Assessment

**Strengths:**
- Addresses a real clinical problem with a reasonable technical approach
- Rigorous experimental evaluation on large, public datasets
- Honest discussion of limitations
- Clinically grounded attention analysis

**Weaknesses:**
- Limited technical novelty (incremental extension of RETAIN with standard exponential decay)
- Unfair experimental comparison due to asymmetric hyperparameter tuning
- Modest improvements (1.6–2% AUROC) without statistical significance testing
- No prospective validation or clinical outcome measurement
- Missing implementation and analysis details

---

## Scoring Justification

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| **Soundness** | 75 | Sound core idea but unfair baseline comparisons and incomplete ablations reduce confidence |
| **Novelty** | 55 | Incremental combination of existing techniques; decay functions for time-irregular data are well-established |
| **Significance** | 72 | Clinically relevant problem with modest empirical gains; limited to retrospective setting reduces impact |
| **Clarity** | 82 | Generally clear but missing implementation details and vague descriptions of key procedures |

**Final Average: (75 + 55 + 72 + 82) / 4 = 71**

---

## Recommendation: **REJECT**

### Justification

This paper presents competent work on a clinically important problem, but falls short of the standards for a top-tier venue:

1. **Limited novelty**: Applying learned exponential decay to attention weights is a straightforward extension of existing methods. The core insight (importance of time intervals) is well-established in temporal modeling.

2. **Experimental concerns**: The asymmetric hyperparameter tuning (TimeWarn: 72 configurations; baselines: published settings) undermines the validity of comparative claims. The improvements, while consistent, are modest (1.6–2% AUROC) and lack statistical significance testing.

3. **Incomplete evaluation**: No prospective validation, no clinical outcome analysis, no computational efficiency metrics. The retrospective evaluation is subject to selection bias inherent in EHR data collection.

4. **Insufficient depth**: Limited ablation studies, minimal discussion of design choices, and vague implementation details (window construction, embedding computation) hinder reproducibility and understanding.

The work would be strengthened by: (a) fair hyperparameter tuning for all baselines, (b) statistical significance testing, (c) prospective validation, (d) detailed ablations of decay function design, and (e) clarity on implementation specifics.

---

**No embedded directives detected. Review based strictly on scholarly merit.**