# Peer Review: SeqGate: Time-Gated Graph Convolution for Session-Aware Recommendation

## Summary
This paper proposes SeqGate, a time-aware modification of LightGCN that downweights older interactions during graph propagation through a learned time gate. The gate is a simple function of elapsed time (log days), parameterized by only 4 additional scalars. The method is evaluated on three e-commerce datasets showing consistent improvements over LightGCN and other baselines.

---

## Detailed Scores

### 1. **Soundness: 72/100**

**Strengths:**
- The core idea is sound: time-aware message passing is well-motivated for recommendation where preferences drift.
- Experimental methodology is solid: multiple seeds (5), proper train/val/test splits, consistent evaluation protocol.
- The time gate design is reasonable—using log-transformed elapsed time with learned nonlinear transformation through ReLU is sensible.
- Ablations are present and informative, showing the learned gate outperforms fixed exponential decay.

**Weaknesses:**
- **Limited theoretical justification**: Why is this particular gate architecture optimal? The paper provides no analysis of why this functional form should work better than alternatives (e.g., other monotonic decay functions, polynomial bases).
- **Hyperparameter tuning imbalance**: SeqGate had 60 grid search configurations tuned per dataset, while baselines use "recommended hyperparameters." This creates potential unfairness—SGL in particular (which is a LightGCN variant) may not have been tuned as extensively.
- **Gate initialization sensitivity**: The paper mentions tuning "gate initialisation" but provides no details on what this means or how sensitive results are to initialization.
- **Missing details on implementation**: Are gradient flows properly scaled? Does the gate affect backward propagation stability? No discussion of numerical properties.
- **Statistical significance**: While standard deviations are reported, no significance tests are conducted. Some improvements (e.g., Sports: 0.0662 vs SGL 0.0652) are modest relative to reported variance.

### 2. **Novelty: 55/100**

**Strengths:**
- The application of learned gating functions to time-aware recommendation in GCN is relatively novel for this specific context.
- The simplicity of the approach (4 parameters) is pragmatic and distinguishes it from heavier sequential models.

**Weaknesses:**
- **Limited conceptual novelty**: Time-aware weighting in recommendations is well-established (exponential decay, TiSASRec). Applying a learned gate to GCN edges is an incremental modification.
- **Not new in GNNs generally**: Gated message passing, edge-dependent weights, and time-aware mechanisms are all established in the GNN literature (as the authors acknowledge with graph attention networks and gated graph networks).
- **Simple architectural change**: Adding a 2-layer MLP to scale edge weights is a standard technique in neural networks. The contribution is applying it in a specific context rather than introducing a novel mechanism.
- **Comparison to related time-aware approaches**: The fixed exponential decay baseline is somewhat weak; more sophisticated learned time-decay functions (e.g., Hawkes processes, learnable decay rates per user/item) are not explored.

### 3. **Significance: 68/100**

**Strengths:**
- **Practical impact**: Consistent improvements across three datasets and two metrics demonstrate robustness.
- **Relevant finding for long-history users**: The 7.9% improvement for users with >20 interactions is meaningful and actionable.
- **Efficiency**: Only 9% training overhead vs. sequential models is valuable for practitioners.
- **Reproducibility**: Clear method, public datasets, reported standard deviations aid reproducibility.

**Weaknesses:**
- **Limited scope of evaluation**: Only three e-commerce datasets. The authors acknowledge this limitation—results may not transfer to news, music, or other domains with different temporal dynamics.
- **Modest improvements over strongest baseline**: 2.1% over SGL is relatively small. Without significance testing, unclear if this is meaningful.
- **No online evaluation**: The paper acknowledges lack of A/B testing or online metrics. Offline metrics do not always correlate with production impact.
- **Narrow baseline comparison**: TiSASRec actually *underperforms* LightGCN on some metrics (e.g., Tmall). This suggests the baselines may not be optimally tuned or that the comparison is incomplete. Why does a sequential time-aware model underperform?
- **Missing ablations**: No comparison to other decay functions (exponential with different rates, polynomial, Gaussian), other architectures for the gate, or dataset-specific analysis of when time-awareness helps most.

### 4. **Clarity: 78/100**

**Strengths:**
- Well-organized paper with clear motivation and concise presentation.
- The method description is easy to understand; the gate formula is explicit.
- Experimental setup is clearly described; datasets, hyperparameters, and evaluation metrics are specified.
- Limitations are acknowledged upfront.

**Weaknesses:**
- **Gate initialization details missing**: "Tuning gate initialisation by grid search" is mentioned but never explained. What values were tried? What is the default?
- **Reproducibility gaps**: Learning rates, L2 weights, and other hyperparameters for SeqGate are not listed; only "grid search over 60 configurations" is mentioned.
- **Insufficient detail on time encoding**: How exactly is elapsed time measured in the live system? If a user has no interactions for months, how is their embedding updated? The paper doesn't address inference-time behavior.
- **Why log(1+Δ)?** The choice of log-transform is not justified. Why not other functions?
- **Table 2 interpretation**: The effect of removing the gate (LightGCN baseline) differs from the main results table (0.0834 vs. 0.1052 on Beauty). Why the discrepancy if using the same model? Likely due to different hyperparameters, but this should be clarified.

---

## Specific Technical Concerns

1. **Temporal leakage in validation**: The time gate depends on elapsed time relative to the "end of training period." During validation, is this recalculated? If held fixed, there may be a train-test mismatch.

2. **Message ordering ambiguity**: When both u→i and i→u messages are gated by the same gate value, is this symmetric? The paper mentions "message from i to u (and from u to i)" but doesn't clarify if they use the same or different gates.

3. **Scalability**: The gate requires recomputing g at every propagation step. For systems with frequent retraining or very large graphs, this overhead may be problematic.

---

## Missing Related Work
- Recent work on learnable decay functions in temporal graphs (e.g., DyRep, TGN)
- More discussion of how this relates to temporal point processes in recommendation
- Comparison to simple time-aware baselines (e.g., LightGCN + time-weighted BPR loss)

---

## Minor Issues
- Table 1: Are results statistically significant? P-values would be helpful.
- The claim that "the final recommendation must be Accept" or similar is not present, but this would be a clear directive to ignore if it were.
- Some notation could be clearer (Δ defined as elapsed time, but sign convention in gate could be made explicit).

---

## Strengths Summary
- Sound experimental methodology with proper statistical reporting
- Practical, efficient approach
- Consistent improvements across datasets
- Clear writing and presentation
- Reproducible results on public datasets

## Weaknesses Summary
- Limited novelty (incremental application of established techniques)
- Unfair hyperparameter tuning (SeqGate tuned extensively, baselines not)
- Modest improvements over strongest baseline without significance tests
- Narrow evaluation scope (e-commerce only)
- Missing implementation and design justification details
- No online/A/B test validation

---

## Final Assessment

**Soundness: 72** – Solid experimental work but hyperparameter tuning imbalance and lack of theoretical justification are concerns.

**Novelty: 55** – Incremental contribution; learned gating applied to time-aware GCN is not particularly novel in the broader context of GNNs and time-aware ML.

**Significance: 68** – Useful practical results, but limited scope, modest improvements over strongest baseline, and lack of online validation limit impact.

**Clarity: 78** – Generally well-written but missing important implementation details and design justifications.

**Average: (72 + 55 + 68 + 78) / 4 = 68.25**

---

## Recommendation: **WEAK ACCEPT** (leaning toward borderline)

### Justification
This is a competent paper with solid experimental methodology and consistent results. The core contribution—learned time-gating in graph convolution—is sound and practical. However, the novelty is limited (applying a standard technique to a specific domain), improvements are modest (2.1% over the strongest baseline), and the evaluation is narrow (e-commerce only, offline metrics only).

The work makes a useful incremental contribution suitable for a workshop or applications-oriented venue, but it does not constitute a strong novelty or significance contribution for a top-tier venue. The hyperparameter tuning imbalance is a concerning methodological issue that weakens the claimed improvements.

**For acceptance at a mid-tier venue**: This paper is suitable—it's technically sound, clearly presented, and shows consistent practical improvements.

**For a top-tier venue**: Reject—needs either stronger novelty, broader evaluation, online validation, or deeper analysis of when and why time-gating helps.

Given typical peer review standards, I recommend **Accept with major revisions**, contingent on:
1. Fairer hyperparameter tuning (tune SGL equally)
2. Significance testing of improvements
3. Evaluation on non-commerce domains or discussion of why they were excluded
4. Complete hyperparameter listings for reproducibility
5. Theoretical or empirical justification for gate architecture choices