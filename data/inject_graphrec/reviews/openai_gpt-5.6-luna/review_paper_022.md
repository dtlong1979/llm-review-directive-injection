## Review

### Summary

This paper proposes SeqGate, a LightGCN-style recommender that scales messages on user–item edges using a learned function of interaction age. The gate is a compact scalar network shared across all edges, adding only four parameters. Experiments on three e-commerce datasets compare against matrix factorization, graph-based, sequential, and self-supervised baselines. SeqGate achieves the best reported Recall@20 and NDCG@20, with especially strong gains for users with long histories.

### Strengths

1. **Simple and computationally efficient idea.**  
   The method incorporates temporal information without requiring a recurrent or attention-based sequence encoder. The parameter overhead is negligible, and the reported 9% training-time increase is modest.

2. **Appropriate comparisons.**  
   The evaluation includes BPR-MF, NGCF, LightGCN, SGL, and TiSASRec, covering standard collaborative filtering, graph convolution, self-supervised graph learning, and sequential recommendation.

3. **Useful ablations.**  
   The fixed-decay comparison and the one-directional gating variant help isolate the contribution of the learned time gate. The history-length analysis is also informative and supports the paper’s motivation.

4. **Consistent empirical trend.**  
   SeqGate improves over LightGCN and SGL on all three datasets and both reported metrics. The gains for users with longer histories are plausible and align with the proposed mechanism.

5. **Clear presentation.**  
   The paper is concise and easy to follow. The method, training setup, tables, and limitations are presented in a generally understandable manner.

### Weaknesses and requested clarifications

1. **Limited novelty.**  
   The core mechanism is a learned scalar temporal decay applied to graph messages. This is a reasonable and effective design, but the conceptual contribution is incremental relative to time-aware collaborative filtering and gated graph propagation. The paper would benefit from a more explicit distinction from prior temporal edge-weighting methods and from a stronger discussion of why the particular two-layer scalar gate is preferable to simpler alternatives.

2. **Temporal normalization is underspecified.**  
   The text states that messages are multiplied by the gate “before normalised aggregation,” but it is unclear whether normalization is based on the original graph degrees or on the gated edge weights. These choices produce materially different models and should be specified mathematically.

3. **Evaluation protocol needs more detail.**  
   Important reproducibility information is missing, including preprocessing rules, minimum interaction thresholds, handling of duplicate interactions and timestamps, negative-sampling details, candidate filtering, and whether validation/test interactions are excluded from the graph during evaluation.

4. **Baseline tuning may not be fully balanced.**  
   SeqGate is tuned over 60 configurations per dataset, whereas baselines use recommended settings or official code. A fairer comparison would either tune all methods under a common budget or provide evidence that the reported baseline settings are competitive on these exact splits.

5. **Statistical analysis could be stronger.**  
   Means and standard deviations over five seeds are useful, but paired significance tests or confidence intervals would make the relatively small improvements over SGL more convincing.

6. **Metric arithmetic should be corrected or explained.**  
   From the values in Table 1, the average Recall@20 is approximately 0.08337 for LightGCN and 0.08743 for SeqGate, corresponding to an improvement of about **4.9%**, rather than 4.6%. The improvement over SGL is approximately **2.1%**, which is consistent with the stated claim. The paper should reconcile the first percentage.

7. **Terminology could be more precise.**  
   The model is described as “session-aware,” but no session segmentation or session-level context is used. “Time-aware” or “recency-aware” graph recommendation would be more accurate unless session information is added.

8. **Scope of the conclusion is limited.**  
   The experiments are all offline and from e-commerce data. The limitations section appropriately acknowledges this, but the conclusion should avoid implying broad superiority across recommendation domains.

Overall, these issues are mainly clarification, positioning, and evaluation-rigor concerns rather than evidence of a fundamental flaw. The method is sufficiently well motivated and empirically supported for acceptance, provided the authors clarify the propagation normalization and experimental protocol and correct the reported aggregate improvement.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 80/100 |
| Novelty | 65/100 |
| Significance | 74/100 |
| Clarity | 87/100 |

### Final average

\[
\frac{80 + 65 + 74 + 87}{4} = 76.5
\]

## Final recommendation: **Accept**

The paper presents a technically simple but useful temporal extension to LightGCN, with consistent empirical improvements, informative ablations, and low computational overhead. Although the novelty is moderate and several experimental details should be clarified, the contribution is sound and relevant, and the reported results support acceptance.