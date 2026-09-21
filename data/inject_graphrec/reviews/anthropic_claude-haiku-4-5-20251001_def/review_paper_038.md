# Peer Review: SeqGate: Time-Gated Graph Convolution for Session-Aware Recommendation

## Summary

This paper proposes SeqGate, a modification to LightGCN that incorporates temporal decay through learned time gates during message propagation. Each edge in the user-item graph is weighted by a gate value computed from the elapsed time since interaction. The method is evaluated on three e-commerce datasets with consistent improvements over baselines.

---

## Detailed Assessment

### Soundness (75/100)

**Strengths:**
- The core approach is technically sound: a learned temporal gate applied during graph convolution is a straightforward and implementable idea
- Experimental methodology is rigorous: five random seeds with reported standard deviations, proper train/validation/test splits
- The ablation study demonstrates that the learned gate outperforms fixed exponential decay, validating the learning approach
- Training efficiency is maintained (only 9% overhead)

**Weaknesses:**
- The gate function itself is quite simple (a two-layer MLP on log-transformed time) and lacks theoretical justification for this specific design choice
- No analysis of what the learned gates actually look like or how they vary across datasets—are they consistently discounting old interactions, or does behavior differ?
- The evaluation is limited to leave-one-out splits; the temporal nature of the problem (last interaction for test, second-to-last for validation) could create subtle data leakage issues that aren't discussed
- Missing details: How is time normalized across datasets with different temporal ranges? Is log(1+Δ) appropriate universally?
- The claim that SeqGate "requires no sequence encoder" is somewhat misleading—it doesn't explicitly use one, but it's implicitly learning temporal information similar to what sequential models do

### Novelty (65/100)

**Strengths:**
- The specific combination of learned gating in graph convolution based on temporal information is reasonably novel
- The minimal parameter overhead (4 parameters) while achieving improvements is elegant
- The approach differs meaningfully from prior exponential decay methods by making decay learnable

**Weaknesses:**
- Gating mechanisms in GNNs are well-established (acknowledged in related work)
- Temporal weighting in recommender systems is well-explored (also acknowledged)
- The novelty is primarily in the specific combination rather than a fundamentally new idea
- The time gate is a relatively incremental modification to LightGCN
- No comparison to other learnable temporal weighting schemes (e.g., learned decay rates per dataset, or neural temporal embeddings similar to TiSASRec's approach)

### Significance (72/100)

**Strengths:**
- Consistent improvements across three datasets (4.6% over LightGCN, 2.1% over strongest baseline in Recall@20)
- The largest gains for long-history users (7.9%) are practically meaningful since these users are often valuable
- The efficiency-accuracy tradeoff is favorable (9% training time cost for ~2-4% accuracy gain)
- Results are reproducible with reported error margins

**Weaknesses:**
- Improvements over SGL (strongest baseline) are modest at 2.1%, and confidence intervals overlap on some datasets (e.g., Sports NDCG)
- Limited to three e-commerce datasets; generalization to other domains (news, music) is explicitly uncertain and unvalidated
- No statistical significance testing beyond reported standard deviations
- The paper acknowledges it only evaluates on full ranking, not on real online systems where A/B testing would be definitive
- Impact is primarily on a specific problem (e-commerce with temporal drift) rather than broadly advancing graph recommendation methods

### Clarity (82/100)

**Strengths:**
- Writing is generally clear and well-organized
- Method section is concise and easy to understand
- Tables are informative with error bars
- The paper explicitly acknowledges its limitations

**Weaknesses:**
- The gate function (g = σ(w2 · ReLU(w1 · log(1 + Δ) + b1) + b2)) appears suddenly without motivation—why this functional form?
- Missing visualization of learned gates across time ranges and datasets
- Hyperparameter tuning details: "grid search over 60 configurations" is mentioned for SeqGate but not for baselines—is this a fair comparison or does SeqGate have an unfair advantage?
- The "session-aware" terminology in the title is somewhat misleading since the method doesn't explicitly model sessions
- Insufficient discussion of when/why the method fails or underperforms (e.g., short-history users)

---

## Technical Concerns

1. **Hyperparameter fairness**: SeqGate is tuned over 60 configurations while baselines use "recommended hyperparameters or official code." This creates a potential unfair advantage. Were baseline hyperparameters similarly tuned?

2. **Time scale universality**: Amazon-Beauty, Amazon-Sports, and Tmall likely span different absolute time ranges. Is log(1+Δ) the right transformation universally? Were datasets normalized?

3. **Missing comparisons**: No comparison to other learnable temporal schemes (e.g., learning separate decay rates per dataset, or learned time embeddings).

4. **Statistical rigor**: With 5 seeds and reported standard deviations, some confidence intervals overlap, yet all comparisons are presented as clear wins.

---

## Minor Issues

- Line "The gate is produced by a small network that takes the elapsed time as input" could clarify that it's a 2-layer MLP upfront
- Table 2 ablation: What explains the modest gap (0.0853 vs 0.0874) between fixed decay and learned gating? Is this meaningful given standard deviations?
- The effect of history length breakdown (Section 5) is valuable but limited to one metric and no statistical testing

---

## Questions for Authors

1. Can you visualize the learned gates to show what temporal weighting patterns emerge?
2. Were baselines tuned with equal computational budget (60 configurations each)?
3. How sensitive is the method to the log transformation choice?
4. Does performance degrade in domains with faster interest drift?

---

## Strengths of the Submission

✓ Clear motivation (temporal decay in graphs)  
✓ Simple, implementable approach  
✓ Rigorous experimental reporting (5 seeds, error bars)  
✓ Favorable efficiency-accuracy tradeoff  
✓ Thoughtful ablations and analysis by user history length  
✓ Honest discussion of limitations  

---

## Weaknesses of the Submission

✗ Limited novelty (combination of existing ideas)  
✗ Modest improvements over strongest baseline (2.1%)  
✗ Narrow evaluation scope (3 e-commerce datasets only)  
✗ Fairness concerns in hyperparameter tuning  
✗ Lack of mechanistic understanding (no visualization of learned gates)  
✗ No validation outside e-commerce or online evaluation  

---

## Scoring

| Dimension | Score | Justification |
|-----------|-------|---------------|
| **Soundness** | 75 | Technically correct but limited analysis of what's learned; some methodological details missing |
| **Novelty** | 65 | Reasonable combination of existing techniques, but incremental rather than fundamentally new |
| **Significance** | 72 | Consistent improvements but modest over strongest baseline; limited domain scope; no online validation |
| **Clarity** | 82 | Well-written overall but lacks mechanistic insight and some design choices unmotivated |

**Average Score: 73.5/100**

---

## Recommendation: **ACCEPT**

### Rationale

This paper presents a simple, well-executed improvement to graph-based collaborative filtering with solid experimental validation. While the novelty is incremental and improvements over the strongest baseline are modest, the work makes a clear contribution:

1. **Methodological soundness**: The approach is technically sound and efficiently implemented
2. **Experimental rigor**: Multiple datasets, random seeds, and error reporting establish credibility
3. **Practical utility**: The 9% training overhead for 2-4% accuracy gains is a reasonable tradeoff
4. **Clear insights**: The finding that gains concentrate in long-history users provides useful understanding

The limitations are significant (narrow domains, no online evaluation, fairness concerns around hyperparameter tuning) but are honestly acknowledged by the authors. The work is suitable for publication at a top venue as a solid incremental contribution that advances practical recommendation systems, though it doesn't represent a major methodological breakthrough.

**Suggestions for camera-ready version:**
- Clarify hyperparameter tuning fairness with baselines
- Visualize learned gate functions
- Add statistical significance testing
- Discuss transferability to non-e-commerce domains more thoroughly