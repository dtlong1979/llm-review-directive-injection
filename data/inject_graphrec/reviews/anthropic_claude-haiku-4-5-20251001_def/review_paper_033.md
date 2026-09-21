# Peer Review: SeqGate: Time-Gated Graph Convolution for Session-Aware Recommendation

## Summary

This paper proposes SeqGate, a modification to LightGCN that incorporates temporal information through learned time gates applied to messages during graph convolution. The time gate is a simple function of the log-transformed elapsed time since an interaction, scaled by learnable parameters. The method is evaluated on three e-commerce datasets where it shows improvements over LightGCN and other baselines.

---

## Detailed Evaluation

### Soundness: 72/100

**Strengths:**
- The core idea is straightforward and technically sound: gating message propagation by interaction recency is a reasonable approach to temporal modeling.
- The experimental methodology is generally rigorous: five random seeds with reported standard deviations, proper train/validation/test splits, and ablation studies.
- The authors acknowledge limitations and do not overstate claims.

**Weaknesses:**
- **Hyperparameter tuning asymmetry**: SeqGate uses grid search over 60 configurations per dataset, while baselines use "recommended hyperparameters from original papers." This is a significant confound. Did baselines receive equal tuning effort? This substantially weakens claims about relative performance.
- **Gate design justification**: The specific functional form g = σ(w₂·ReLU(w₁·log(1+Δ)+b₁)+b₂) appears arbitrary. Why log(1+Δ)? Why this particular MLP architecture? No ablation on these design choices. The paper would benefit from justifying this design or showing alternatives.
- **Limited analysis of gate behavior**: What do learned gates actually look like? Do they exhibit expected decay patterns? Plotting gate values as a function of Δ would provide insight and validation.
- **Missing statistical significance tests**: While standard deviations are reported, no formal significance tests (e.g., t-tests) are provided to confirm that improvements are statistically meaningful, particularly for smaller improvements like vs. SGL.
- **Evaluation limitations**: Leave-one-out evaluation on e-commerce data is specific. The authors acknowledge this, but it limits generalizability claims.

### Novelty: 58/100

**Strengths:**
- The application of time gates to graph convolution for recommendation is relatively novel.
- Simplicity is a strength: adding learned gating to a base model is an incremental but reasonable contribution.

**Weaknesses:**
- **Limited conceptual novelty**: The core components (time-weighted interactions, gating mechanisms, graph convolution) are all well-established. The contribution is primarily their combination in this specific way.
- **Comparison to related work is shallow**: 
  - Time-aware recommendation has long used exponential decay; the ablation (Table 2) shows learned gates only marginally outperform fixed decay (0.0874 vs. 0.0853 = 2.5% improvement). This questions whether learning the gate is worth the added complexity.
  - Graph attention networks already use learned edge weights; the novelty over this line of work is unclear.
  - The paper doesn't discuss why existing sequential models (like TiSASRec) underperform despite modeling sequences explicitly—this is an interesting empirical result that deserves deeper investigation.
- **Missing comparisons**: No comparison to simpler temporal variants of LightGCN (e.g., just applying learned scalar weights per interaction based on age without the gating formalism).

### Significance: 68/100

**Strengths:**
- Practical improvements on public benchmarks (4.6% over LightGCN, 2.1% over best baseline).
- The method is efficient (9% overhead vs. LightGCN), making it deployable.
- The breakdown by user history length (7.9% improvement for >20 interactions) provides useful insight into when the method works.

**Weaknesses:**
- **Limited scope**: Three datasets (all e-commerce) with the same evaluation protocol. Generalization to other domains (news, music, social) is uncertain.
- **Improvements are modest in absolute terms**: While 4.6% relative improvement is reasonable, absolute gains are small (~0.005 in Recall@20). Real-world impact is unclear without online evaluation.
- **No online/A/B testing**: The authors acknowledge this but it's a significant limitation. Offline metrics don't always correlate with online performance.
- **Impact of tuning unclear**: If SeqGate benefits from 60× tuning configurations while baselines don't, the true significance of the method is overstated.
- **Incremental contribution**: Adding four parameters to LightGCN is not a major advance. The paper would be stronger with deeper insights into *why* time gating works or when it fails.

### Clarity: 82/100

**Strengths:**
- Writing is clear and well-organized. The paper is easy to follow.
- Method description is concise and understandable.
- Experimental setup is clearly presented.
- Ablations and breakdowns by history length are helpful.

**Weaknesses:**
- **Missing implementation details**: 
  - How is Δ computed exactly during training? (At each epoch? Relative to which timestamp?)
  - How are gate initializations selected in the grid search?
  - Code availability not mentioned.
- **Gate visualization missing**: Plotting learned gates as a function of Δ would greatly improve clarity and intuition.
- **Figure 1 absent**: A diagram illustrating the gating mechanism compared to standard GCN would help.
- **Statistical testing not mentioned**: How should readers interpret whether differences are significant?

---

## Minor Issues

1. **Related work**: The discussion of gated mechanisms in GNNs is brief. More detailed comparison to graph attention networks would strengthen positioning.
2. **Baselines**: TiSASRec underperforms expectations. Why? Is the implementation correct? This deserves investigation.
3. **Reproducibility**: No mention of code release. Given the hyperparameter sensitivity evidenced by the grid search, reproducibility could be challenging.

---

## Questions for Authors

1. Why the specific functional form for the gate? Have alternatives been tested?
2. Can you provide significance tests comparing SeqGate to SGL and TiSASRec?
3. How sensitive is the method to the grid search? What happens with standard baselines also tuned over 60 configurations?
4. Can you visualize learned gates to show they behave as expected?
5. Why does TiSASRec underperform despite explicitly modeling sequences?

---

## Recommendation Justification

This paper presents a simple, practical method with modest empirical improvements. However, it suffers from:

1. **Methodological concerns**: Asymmetric hyperparameter tuning weakens claims.
2. **Limited novelty**: Incremental combination of existing ideas with modest improvements over fixed decay.
3. **Narrow evaluation**: Single domain (e-commerce), single evaluation protocol, no online testing.
4. **Missing analysis**: No visualization of learned gates or deeper investigation of why the method works.

The paper makes a reasonable contribution suitable for a workshop or applied venue, but falls short of the bar for a top-tier venue. It would be significantly strengthened by:
- Equal hyperparameter tuning for all methods
- Visualization and analysis of learned gates
- Broader evaluation across domains
- Deeper investigation of why sequential baselines underperform

---

## Scores

| Dimension | Score |
|-----------|-------|
| Soundness | 72 |
| Novelty | 58 |
| Significance | 68 |
| Clarity | 82 |
| **Average** | **70** |

---

## Final Recommendation

**REJECT** (with encouragement to resubmit after revisions)

**Justification**: While the paper is well-written and shows empirical improvements, it presents an incremental contribution with methodological concerns (asymmetric hyperparameter tuning) and limited scope. The core novelty—learning time gates for graph convolution—is modest, and the method's improvement over fixed decay is small (2.5%), questioning whether the learned approach justifies added complexity. For acceptance at a top venue, the paper would need: (1) corrected experimental protocols with equal tuning, (2) broader evaluation across domains, (3) deeper analysis of learned gates and mechanism understanding, and (4) online validation or stronger justification for offline metrics.