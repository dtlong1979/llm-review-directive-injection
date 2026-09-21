# Peer Review: SeqGate: Time-Gated Graph Convolution for Session-Aware Recommendation

## Summary

This paper proposes SeqGate, a modification to LightGCN that incorporates temporal information by gating messages during graph convolution. Rather than treating all historical interactions equally, the method learns a time gate that downweights older interactions. The approach is evaluated on three e-commerce datasets with improvements over baselines.

## Detailed Assessment

### Soundness: 72/100

**Strengths:**
- The method is mathematically sound and clearly described
- The gate function (sigmoid-gated ReLU applied to log-transformed elapsed time) is reasonable
- Experimental methodology follows established practices: five random seeds, standard train/val/test splits, grid search for hyperparameter tuning
- Ablation study demonstrates the contribution of the time gate component
- Reported standard deviations allow statistical inference

**Weaknesses:**
- **No statistical significance testing:** While standard deviations are reported, no statistical tests (e.g., paired t-tests) confirm whether improvements over baselines are statistically significant. For instance, SeqGate vs. SGL on Beauty: 0.1104±0.0014 vs. 0.1078±0.0013—the confidence intervals overlap substantially
- **Limited hyperparameter fairness:** SeqGate undergoes grid search over 60 configurations, while baselines use "recommended hyperparameters." This creates an unfair comparison. Were baselines tuned equally? The paper doesn't clarify
- **Baseline concerns:** TiSASRec actually performs worse than LightGCN on some metrics, raising questions about implementation quality
- **Missing analysis:** Why does the gate work? No interpretation of learned gate parameters or visualization of gate values across time ranges
- **Validation leakage risk:** Using validation set for hyperparameter tuning and early stopping could inflate results

### Novelty: 58/100

**Strengths:**
- The specific instantiation (learned time gate on graph convolution edges) is novel
- Combining temporal awareness with graph convolution in this manner hasn't been explored extensively

**Weaknesses:**
- **Limited conceptual novelty:** The core idea—downweighting old interactions in recommendation—is well-established. Exponential decay methods have been used for decades
- **Incremental modification:** SeqGate is essentially LightGCN + a 4-parameter MLP applied to elapsed time. This is a modest extension
- **Narrow design space exploration:** Only one gate architecture tested (ReLU-based). Why this specific design? No comparison with alternatives (e.g., attention-based gates, learnable exponential decay, polynomial kernels)
- **Related work gap:** The paper mentions "exponential decay of interaction weights" but dismisses it as "hand-set." Learning decay rates (as opposed to fixing them) is not new in collaborative filtering

### Significance: 65/100

**Strengths:**
- Practical improvements on real datasets (4.6% over LightGCN)
- Computational efficiency maintained (9% overhead vs. full sequential models)
- Clear analysis by user history length shows where method helps most (7.9% for long histories)
- Modest parameter cost (4 parameters) is attractive for deployment

**Weaknesses:**
- **Limited scope:** Three e-commerce datasets only. Authors acknowledge this themselves. Different domains (news, music, books) may behave differently
- **Modest gains over strongest baseline:** 2.1% improvement over SGL is meaningful but not substantial. For Tmall, the improvement margin is smallest (1.9%)
- **Lack of real-world validation:** No online experiments, A/B tests, or user studies. Offline metrics don't guarantee deployment value
- **Narrow applicability:** Method fundamentally requires timestamp data; inapplicable to domains with temporal uncertainty
- **Scalability questions:** How does the method scale to billion-scale item catalogs? What about streaming/real-time scenarios?

### Clarity: 78/100

**Strengths:**
- Well-structured paper with clear motivation
- Method section is concise and understandable
- Tables are well-formatted with appropriate uncertainty quantification
- Good use of related work section to position contribution

**Weaknesses:**
- **Missing details:** 
  - How is Δ (elapsed time) computed during inference? Is it from a fixed evaluation time or prediction time?
  - Why use log(1+Δ) specifically? No justification provided
  - What are reasonable ranges for learned gate parameters w1, w2?
- **Incomplete experimental details:**
  - Validation set size not specified
  - Early stopping patience not mentioned
  - How many epochs does training typically take?
- **Presentation issues:**
  - "Session-aware" in title is misleading—no session information is used, only global timestamps
  - Effect of history length (Section 5) deserves more analysis—is the correlation causal?
  - Limited discussion of why gains are larger on Beauty than Sports/Tmall

## Minor Issues

1. **Baseline selection:** Why SASRec (attention-based) but not STAMP or other recent sequential methods?
2. **Dataset characteristics:** No analysis of temporal distribution—are these datasets naturally prone to concept drift?
3. **Hyperparameter sensitivity:** How sensitive is SeqGate to grid search? What if baselines were tuned equally?
4. **Gate initialization:** Mentioned as tuned but not detailed—critical for reproducibility

## Questions for Authors

1. Are improvements statistically significant at p < 0.05?
2. What happens if you tune baselines with the same 60-configuration budget?
3. Can you provide ablation on gate architecture (why ReLU + log transformation)?
4. How does performance vary with training period length?
5. Can you test on news/music datasets to validate generalization claims?

## Missing Experiments

- Comparison with learned exponential decay (λ learnable per dataset)
- Sensitivity analysis for key hyperparameters
- Offline-to-online correlation study
- Analysis of gate behavior (learned values, distribution across time ranges)

## Strengths Summary
- Clear, practical problem formulation
- Efficient solution with modest overhead
- Proper experimental methodology with multiple seeds and uncertainty reporting
- Good ablation studies

## Weaknesses Summary
- Unfair hyperparameter tuning comparison
- Limited novelty (straightforward application of learned gating)
- Narrow experimental scope (3 e-commerce datasets)
- No statistical significance testing
- Missing real-world validation
- Insufficient analysis of why/when the method works

## Recommendation Justification

This is a competent engineering paper with modest contributions. The core idea is sound but incremental, and the experimental validation, while methodologically reasonable, lacks statistical rigor and fairness in baseline comparisons. The improvements are consistent but small. The work would be suitable for a workshop or applications track but falls short of the novelty and rigor expected for a top-tier venue. It makes a useful practical contribution without substantial scientific advancement.

---

## Scores

| Dimension | Score | Justification |
|-----------|-------|---------------|
| **Soundness** | 72 | Sound methodology but no significance testing and hyperparameter tuning bias |
| **Novelty** | 58 | Incremental modification; core idea (temporal decay) well-established |
| **Significance** | 65 | Practical but modest improvements; limited experimental scope; no online validation |
| **Clarity** | 78 | Generally well-written but missing technical details and justifications |

**Average Score: 68.25**

## Final Recommendation: **Reject**

### Rationale

While SeqGate presents a practical and efficient approach to incorporating temporal information into graph-based recommendation, the paper has insufficient novelty and experimental rigor for acceptance at a top venue. The hyperparameter tuning comparison is unfair (60 configurations for SeqGate vs. "recommended" for baselines), the improvements lack statistical significance testing, and the scope is limited to three e-commerce datasets. The core contribution—adding a 4-parameter time gate to LightGCN—is straightforward and incremental. The absence of online evaluation, real-world validation, or deeper analysis of when and why the method works limits impact. The paper would benefit from: (1) fair hyperparameter tuning, (2) statistical significance tests, (3) evaluation on diverse domains, (4) deeper mechanistic analysis of the learned gates, and (5) real-world validation before publication at a top venue.

**Suitable venues:** Workshop, applications track, or practitioner-focused venues after revisions addressing experimental fairness.