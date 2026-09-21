## Review

### Summary

This paper proposes SeqGate, a lightweight extension of LightGCN that weights user–item messages according to the age of each interaction. The gate is a shared scalar function of log-transformed interaction age and is applied in both propagation directions. The approach is simple, computationally inexpensive, and evaluated on three public datasets against matrix-factorization, graph-based, self-supervised, and sequential baselines.

### Strengths

- **Simple and well-motivated idea.** Modeling recency directly in graph propagation addresses a clear limitation of static collaborative-filtering graphs.
- **Good efficiency–accuracy trade-off.** The method adds only four scalar parameters and reports a modest 9% training-time increase.
- **Broad baseline comparison.** The inclusion of BPR-MF, NGCF, LightGCN, SGL, and TiSASRec provides useful coverage across traditional, graph, self-supervised, and sequential approaches.
- **Ablation analysis is informative.** The comparisons with fixed exponential decay, one-directional gating, and LightGCN support the claim that learning the time transformation is beneficial.
- **Results are consistent across datasets.** SeqGate achieves the best reported Recall@20 and NDCG@20 on all three datasets, with particularly stronger gains for users with long histories.
- **Clear presentation.** The model definition, training setup, and evaluation protocol are concise and easy to follow.

### Main concerns and suggestions

1. **Novelty is incremental but meaningful.** Time decay and temporal weighting have been explored in collaborative filtering, and edge gating is established in graph neural networks. The contribution is the particularly simple integration of a learned temporal gate into LightGCN. The paper should sharpen this positioning and more explicitly distinguish SeqGate from prior temporal graph recommenders and time-aware LightGCN variants.

2. **“Session-aware” may be too strong a description.** The current method uses interaction age but does not model session boundaries, within-session order, or session context. “Time-aware” or “recency-aware” recommendation would more precisely describe the method unless the authors add a clearer definition of session awareness.

3. **Statistical testing should be strengthened.** Results include standard deviations over five seeds, which is useful, but paired significance tests or confidence intervals would make the claims of improvement more robust, especially because some gains over SGL are relatively small.

4. **Experimental details could be expanded.** Reproducibility would benefit from reporting negative-sampling details, exact data preprocessing and filtering criteria, the number of interactions retained per user, hardware, gate initialization values, and whether baseline hyperparameters were tuned under the same validation budget. The comparison may otherwise favor SeqGate because it receives an explicitly described 60-configuration search while baselines use settings from prior work or official code.

5. **The propagation normalization needs clarification.** The paper states that messages are multiplied by the gate “before normalised aggregation.” It should specify whether the gate is incorporated into the adjacency matrix, whether the weighted adjacency is renormalized, and whether degree normalization remains the original LightGCN normalization. These choices can materially affect the model.

6. **Temporal evaluation deserves additional analysis.** Since the gate is based on time relative to the end of training, it would be useful to report performance by temporal span, cold-start level, or test-interaction recency. A learned gate curve or visualization of gate values over age would also improve interpretability.

7. **The method is globally shared.** A single scalar gate function for all users and items is attractive for efficiency, but it cannot represent users with different preference-drift rates or item categories with different temporal dynamics. A discussion or ablation of user-specific, dataset-specific, or category-specific gates would help establish the limits of the approach.

8. **Arithmetic should be stated precisely.** Based on the table, the average Recall@20 is approximately 0.0834 for LightGCN, 0.0857 for SGL, and 0.0874 for SeqGate. Thus, SeqGate improves over LightGCN by approximately 4.9% and over SGL by approximately 2.0%; the reported 4.6% and 2.1% figures may result from unrounded values, but the calculation should be clarified.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 84/100 |
| Novelty | 76/100 |
| Significance | 79/100 |
| Clarity | 89/100 |

**Final average:**  
\[
\frac{84 + 76 + 79 + 89}{4} = 82.0
\]

### Final recommendation: **Accept**

The paper presents a technically sound and well-motivated lightweight improvement to graph-based recommendation. Although the novelty is primarily an effective combination of existing ideas rather than a fundamentally new graph architecture, the consistent empirical gains, low overhead, and useful ablations make the contribution suitable for acceptance. The main issues concern positioning, reproducibility details, normalization clarification, and stronger statistical validation; these are addressable through revision and do not undermine the central contribution.