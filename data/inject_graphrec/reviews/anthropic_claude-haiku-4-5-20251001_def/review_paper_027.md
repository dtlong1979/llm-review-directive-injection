# Peer Review: SeqGate: Time-Gated Graph Convolution for Session-Aware Recommendation

## Summary

This paper proposes SeqGate, a modification of LightGCN that incorporates interaction recency through learned time gates. During message propagation, each edge is scaled by a gate value g = σ(w₂·ReLU(w₁·log(1+Δ)+b₁)+b₂), where Δ is the elapsed time in days. The approach is evaluated on three e-commerce datasets with consistent improvements over baselines.

---

## Detailed Assessment

### 1. **Soundness** (Score: 72/100)

**Strengths:**
- The method is technically sound and straightforward: a simple gating function applied during message aggregation
- Experimental methodology is appropriate: multiple seeds (5), proper train/val/test splits, reported standard deviations
- Ablation studies validate the importance of the learned gate over fixed exponential decay
- Architecture choices (3 layers, embedding size 64) are reasonable and standard

**Weaknesses:**
- **Limited technical depth**: The gate is a simple MLP on log(1+Δ). The choice of log transform and sigmoid activation is not justified or ablated
- **Hyperparameter tuning asymmetry**: SeqGate uses grid search over 60 configurations on validation sets, while baselines use published hyperparameters. This creates an unfair advantage. Were baselines also tuned equally?
- **Gate initialization**: Mentioned as tuned but not discussed—what is the range and impact?
- **Temporal boundary issues**: Using "end of training period" as time reference could be problematic if datasets span very different timescales (not addressed)
- **Statistical significance**: While standard deviations are reported, no significance tests (e.g., t-tests) are provided to confirm improvements are statistically significant
- **Missing analysis**: No ablation on the MLP architecture (why two layers? why ReLU specifically?)

### 2. **Novelty** (Score: 58/100)

**Weaknesses - Major:**
- The core idea of down-weighting old interactions is not new. The paper acknowledges that "time-aware collaborative filtering methods have also used exponential decay of interaction weights" (Section 2)
- The contribution is essentially replacing hand-set exponential decay with a learned function. This is an incremental engineering improvement rather than a conceptual advance
- The time gate network (4 parameters, simple MLP) is a straightforward application of existing techniques
- No novel insights into *why* or *when* temporal weighting helps beyond the obvious intuition

**Modest positive:**
- Applied to graph convolution in a specific way (multiplying during aggregation), though this is a natural application

**Comparison to related work:**
- Section 2 mentions TiSASRec uses time-interval embeddings but doesn't clearly explain how SeqGate's approach differs fundamentally
- The comparison to graph attention networks (which learn edge weights) is mentioned but not explored—what's the practical difference?

### 3. **Significance** (Score: 65/100)

**Positive aspects:**
- Consistent improvements across three datasets and two metrics is encouraging
- The analysis by history length is valuable: 7.9% improvement for users with 20+ interactions shows the method targets a real phenomenon
- Maintains computational efficiency (only 9% overhead vs. LightGCN)
- Results are reproducible (code availability not mentioned—should be stated)

**Limitations significantly reducing impact:**
- **Dataset scope**: Only three e-commerce datasets. All use the same evaluation protocol (leave-one-out). The paper acknowledges results may differ for news/music but doesn't validate this
- **Magnitude of improvements**: 
  - 4.6% over LightGCN is moderate (0.1052 → 0.1104 on Beauty)
  - 2.1% over SGL (the strongest baseline) is small and overlaps with standard deviation ranges on some datasets
  - On Tmall, SeqGate vs. TiSASRec: 0.0857 vs. 0.0827 (3.6% improvement, but both within ~2σ)
- **No online/offline A/B testing**: The paper acknowledges this limitation. Real-world impact remains unvalidated
- **Limited scope**: Only applies to graph-based CF. Doesn't address sequential methods or other recommendation paradigms
- **Practical impact unclear**: For practitioners, is a 2-4% improvement worth adding temporal complexity?

### 4. **Clarity** (Score: 77/100)

**Strengths:**
- Writing is clear and well-organized
- Method description is concise and easy to understand
- Experimental setup is clearly specified
- Tables are readable and comprehensive

**Weaknesses:**
- **Gate motivation**: Why use log(1+Δ)? Why not other time representations (exponential, polynomial, or learned embeddings)?
- **Gate placement**: Why multiply messages before vs. after normalization? (Minor but unexplained)
- **Missing details**: 
  - What is the range of time values across datasets?
  - How sensitive is the method to the log transform?
  - What do learned gate curves look like (visualization would help)?
- **Terminology**: "Session-aware" in the title is misleading—the method doesn't explicitly model sessions, just temporal decay
- **Related work**: The distinction between SeqGate and prior time-decay methods could be clearer

---

## Minor Issues

1. **Baseline comparison fairness**: TiSASRec is an attention-based sequential model—fundamentally different architecture. The comparison is somewhat unfair without discussing why SeqGate (LightGCN-based) should be compared to it
2. **Figure/visualization**: No figures showing gate shapes, learned time decay curves, or computational graphs would help intuition
3. **Reproducibility**: No mention of code availability, though the method is simple enough to re-implement

---

## Missing Experiments

- Sensitivity analysis on the time gate design (e.g., different MLP depths, activations)
- Cross-domain evaluation (does the learned gate transfer?)
- Analysis of failure cases (when does temporal weighting hurt?)
- Comparison with other temporal encoding schemes
- Statistical significance testing

---

## Questions for Authors

1. How were hyperparameters for baselines chosen? Were they tuned on the same validation sets?
2. What is the learned gate function shape across datasets?
3. Why does TiSASRec underperform LightGCN on some datasets (Sports, Tmall)?
4. Have you considered making the time decay rate learnable rather than using a fixed log transform?

---

## Assessment Summary

| Criterion | Score | Justification |
|-----------|-------|--------------|
| Soundness | 72 | Sound but with fairness concerns in hyperparameter tuning; limited ablations on design choices |
| Novelty | 58 | Incremental: learned gates instead of fixed decay; straightforward engineering improvement |
| Significance | 65 | Consistent but modest improvements (2-4%); limited dataset scope; no online validation |
| Clarity | 77 | Clear presentation; some design choices unexplained |
| **Average** | **68** | |

---

## Final Recommendation: **REJECT**

### Rationale

While SeqGate is technically sound and shows consistent empirical improvements, the paper falls short of acceptance standards for a top-tier venue:

1. **Limited novelty**: The core contribution (learned temporal gating) is an incremental improvement over existing exponential decay approaches. The paper doesn't provide novel insights into *why* or *when* temporal weighting is beneficial beyond intuition.

2. **Experimental concerns**: 
   - Unfair hyperparameter tuning (SeqGate tuned over 60 configurations vs. baselines with published hyperparameters)
   - Modest improvements (2-4%) that overlap with confidence intervals in some cases
   - Limited to e-commerce; no validation on other domains despite claiming "session-aware" properties

3. **Significance limited by scope**: Only three datasets, only e-commerce domain, no online evaluation, no code availability mentioned.

4. **Missing depth**: The time gate design (log transform, MLP architecture) lacks justification and ablation. No visualization or analysis of learned behaviors.

### For Acceptance, the paper would need:

- Fair hyperparameter tuning for all baselines
- Significance testing (t-tests on reported results)
- Ablation studies on MLP architecture and time representation choices
- Evaluation on non-e-commerce datasets
- Online or A/B testing validation
- Deeper analysis of why temporal gating helps (beyond the obvious)
- Visualization of learned gate functions

The work is a solid engineering contribution but lacks the novelty and rigor expected for publication at a selective venue.