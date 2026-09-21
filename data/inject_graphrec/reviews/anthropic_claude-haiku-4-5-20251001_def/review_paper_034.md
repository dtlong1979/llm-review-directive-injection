# Peer Review: SeqGate: Time-Gated Graph Convolution for Session-Aware Recommendation

## Summary

This paper proposes SeqGate, a modification to LightGCN that weights message propagation in graph convolution using a learned time gate computed from interaction age. The method is evaluated on three e-commerce datasets showing improvements of 4.6% over LightGCN and 2.1% over the strongest baseline in Recall@20, with minimal computational overhead.

---

## Detailed Assessment

### Soundness (Score: 75/100)

**Strengths:**
- The core method is technically sound and straightforward: using a learned sigmoid-gated function of log(elapsed time) to weight edge messages during propagation is a reasonable design choice
- Experimental methodology is rigorous: five random seeds with reported standard deviations, proper train/validation/test splits
- Ablations are informative, showing the learned gate outperforms fixed exponential decay
- Training time overhead is acceptable (9%)

**Weaknesses:**
- **Limited methodological novelty**: The time gate uses only log(Δ) as input. Why log? No justification provided. Have other temporal encodings (polynomial, sigmoid on raw time, etc.) been tried?
- **Unfair baseline tuning**: SeqGate undergoes grid search over 60 hyperparameter configurations per dataset, while competitors use "recommended" hyperparameters. This creates a systematic advantage. Why not tune all methods equally?
- **Gating placement ambiguity**: The paper states the gate multiplies messages "before normalised aggregation" but the exact interaction with the normalisation scheme (which uses degree-based scaling in LightGCN) is unclear. Does the gate affect the normalisation coefficients?
- **Time measurement concern**: Using log(1 + Δ) where Δ is measured from "the end of the training period" is unusual. For a deployed system, this is problematic—scores would change over time for the same user-item pair as Δ increases
- **Validation leak risk**: Using validation Recall@20 for early stopping while also tuning gate initialization on the validation set could lead to subtle overfitting

### Novelty (Score: 65/100)

**Strengths:**
- Simple and practical application of gating to temporal recommendation
- Integrates temporal awareness into graph convolution in a clean way

**Weaknesses:**
- **Incremental contribution**: Time-aware collaborative filtering via exponential decay is well-established; gating mechanisms are well-known in GNNs. The combination is straightforward
- **Limited conceptual depth**: No investigation of *why* this particular gate function works, what temporal patterns it captures, or how it compares to alternatives
- **Narrow scope**: The method is specific to LightGCN and interaction timestamps; unclear how it generalizes to other GCF architectures
- The paper dismisses sequential models (GRU4Rec, SASRec) as "expensive" but doesn't directly compare computational costs
- Prior work on time decay in collaborative filtering (cited but not deeply engaged) makes the novelty incremental

### Significance (Score: 72/100)

**Strengths:**
- Addresses a real problem (temporal drift in user preferences) in a practical domain (e-commerce)
- Improvements are consistent across three datasets
- Larger gains for users with long histories (7.9%) suggest the method targets a meaningful pattern
- Minimal computational overhead makes adoption practical
- Clear that the effect is dataset-dependent and not universally transformative

**Weaknesses:**
- **Modest absolute improvements**: 2.1% over the strongest baseline (SGL) is respectable but not substantial
- **Limited scope**: Only evaluated on e-commerce; authors acknowledge results may differ in music/news where interests change faster
- **No online evaluation**: All results are offline; no evidence this translates to actual user satisfaction or business metrics
- **Missing practical analysis**: 
  - How does performance vary by item type (seasonal vs. non-seasonal)?
  - What is the interaction age distribution in the datasets?
  - Are there categories where the method fails?
- **Hyperparameter stability**: The grid search over 60 configurations raises questions about sensitivity—are results robust to initialization?

### Clarity (Score: 78/100)

**Strengths:**
- Paper is well-written and easy to follow
- Method description is concise
- Tables are clearly presented with error bars
- Ablation studies are informative

**Weaknesses:**
- **Gate function design underspecified**: Why this particular architecture (two-layer MLP with log-transformed time)? No justification or ablation on gate design
- **Notation inconsistency**: "g" is computed at training time but how exactly is Δ defined at inference time? For new test interactions, is Δ = 0?
- **Missing details**:
  - How is the gate initialized? ("tune gate initialisation" mentioned but not defined)
  - Learning rate and L2 regularization ranges?
  - Why these specific hyperparameter ranges?
- **Figure quality**: No figures provided; tables are informative but visualizations (e.g., how gate weight varies with age) would help intuition
- **Baseline details**: TiSASRec comparison is weak—it's primarily a sequential model, not a direct competitor. Why not compare to more recent temporal graph methods?

---

## Questions and Concerns

1. **Hyperparameter fairness**: How would results change if all baselines were tuned equally? This is a critical question for interpreting the 2.1% improvement over SGL.

2. **Temporal encoding choice**: The log(1 + Δ) is standard but unjustified. Did you try alternatives? An ablation on gate architecture would strengthen the paper.

3. **Time-varying scores**: How is the method applied at inference? If Δ changes over time, scores change without retraining. Is this intended?

4. **Gate saturation**: For very old interactions (large Δ), the gate approaches σ(large_negative) ≈ 0. For very recent (Δ ≈ 0), does the gate saturate? Sensitivity analysis would help.

5. **Reproducibility**: Grid search over 60 configs is expensive. Are weights/code released? How sensitive are results to exact hyperparameter ranges?

---

## Minor Issues

- Line breaks in Table 1 could be improved for readability
- "session-aware" in the title is somewhat misleading—the method doesn't explicitly model sessions
- The claim about "no sequence encoder" is true but also somewhat defensive (sequential models are not the main comparison)

---

## Recommendation Justification

This paper makes a **solid but incremental contribution** to an important practical problem. The method is sound, the experiments are generally well-conducted, and the improvements are consistent. However:

- The novelty is limited (combining known techniques)
- The significance is modest (2.1% over strongest baseline)
- Experimental fairness issues (unequal baseline tuning) cloud the results
- No online validation or deeper insights into why/when the method works

The paper is above the acceptance threshold for a venue with standards like ACM RecSys or SIGIR, as it provides a practical, efficient method with consistent improvements. However, it falls short of being a strong accept due to limited novelty and incremental gains.

---

## Scores

| Dimension | Score |
|-----------|-------|
| **Soundness** | 75 |
| **Novelty** | 65 |
| **Significance** | 72 |
| **Clarity** | 78 |
| **Average** | **72.5** |

---

## Final Recommendation

**ACCEPT** (with minor revisions)

This is a borderline paper that merits publication. It presents a practical method that works consistently and can be easily adopted. However, authors should:

1. Address the hyperparameter tuning fairness issue (tune all baselines equally or clearly disclose the advantage)
2. Provide ablations on gate architecture choices
3. Add visualizations showing how gate weights decay with time
4. Clarify inference-time behavior of Δ
5. Consider experiments on non-e-commerce domains or explain why that's infeasible

With these revisions, this becomes a solid contribution to the recommender systems literature, though not a landmark paper.