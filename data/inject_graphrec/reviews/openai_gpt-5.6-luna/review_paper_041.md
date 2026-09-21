## Review

### Summary

This paper proposes SeqGate, a lightweight extension of LightGCN that modulates messages on user–item edges using a learned function of interaction age. The model adds only four globally shared scalar parameters and avoids introducing a sequence encoder. Experiments on Amazon-Beauty, Amazon-Sports, and Tmall compare SeqGate with matrix factorization, graph-based, self-supervised, and sequential baselines. The reported results show consistent improvements in Recall@20 and NDCG@20, with larger gains for users having longer histories and only a modest training-time increase.

### Strengths

1. **Simple and computationally efficient method.** The proposed gate is easy to implement and preserves the basic LightGCN architecture, while adding minimal parameter overhead.
2. **Clear motivation.** Treating old and recent interactions identically is a meaningful limitation of static collaborative-filtering graphs.
3. **Broad baseline coverage.** The comparison includes BPR-MF, NGCF, LightGCN, SGL, and TiSASRec, spanning classical, graph, self-supervised, and sequential approaches.
4. **Consistent empirical improvements.** SeqGate is best on all reported datasets and metrics, and the ablation results support the importance of the learned time gate.
5. **Useful subgroup analysis.** The breakdown by history length is relevant and suggests where the proposed method is most beneficial.
6. **Good presentation.** The paper is concise, logically organized, and provides the main modeling and training details needed to understand the approach.

### Weaknesses and questions

1. **Limited novelty at the conceptual level.** Time-decay weighting and edge-dependent message scaling are established ideas in time-aware recommendation and graph learning. The main contribution is the particularly simple integration of a learned time gate into LightGCN rather than a fundamentally new graph-convolution principle.
2. **Gate specification is underexplained.** The paper should clarify initialization, parameter constraints, whether the same gate is used at every propagation layer, and whether messages in both directions always use the same age-dependent value.
3. **Potential temporal-evaluation concerns.** Since the gate uses the end of the training period as its reference point, the exact construction of training, validation, and test graphs should be described carefully to rule out any temporal leakage or inconsistent timestamp handling.
4. **Baseline tuning fairness needs more detail.** SeqGate receives a 60-configuration grid search, whereas baselines use settings from their original papers or official implementations. Reporting comparable tuning budgets or additional sensitivity analyses would make the comparison stronger.
5. **Statistical testing is absent.** Standard deviations are reported, but significance tests or paired per-user comparisons would help establish whether the improvements are statistically reliable.
6. **Limited analysis of the learned gate.** The paper would benefit from plots or summary statistics showing the learned gate as a function of interaction age. It is not clear whether the model learns monotonic decay, a non-monotonic pattern, or nearly constant weighting.
7. **Some quantitative claims should be checked.** From the displayed averages, the improvement over LightGCN appears to be approximately 4.9% in Recall@20, and the improvement over SGL approximately 2.0%, rather than exactly the 4.6% and 2.1% stated in the text. This is minor but should be reconciled.

### Soundness: **84/100**

The method is well specified at a high level, the experimental protocol is plausible, and the ablations support the central claim. However, missing details about temporal preprocessing, baseline tuning, statistical significance, and gate behavior prevent a higher score. The numerical discrepancy between the reported percentage improvements and the table averages should also be corrected.

### Novelty: **74/100**

The combination of a learned age-dependent gate with LightGCN is practical and reasonably distinct as a compact modeling contribution. Nevertheless, the underlying ingredients—time decay, edge weighting, and gated graph propagation—are closely related to existing time-aware recommendation and graph neural network techniques. The novelty is therefore incremental but meaningful.

### Significance: **81/100**

The problem is important, and the approach is attractive for systems that need temporal adaptation without the cost of a sequential encoder. The reported gains are consistent across datasets, and the computational overhead is modest. Broader-domain experiments, online evaluation, and stronger analysis against competitive time-aware graph methods would be needed to establish wider impact.

### Clarity: **90/100**

The paper is well structured, readable, and concise. The motivation, model, experiments, and limitations are easy to follow. Additional implementation details and clarification of the evaluation timeline would improve reproducibility, but the overall exposition is strong.

## Final score

\[
\frac{84 + 74 + 81 + 90}{4} = \mathbf{82.25}
\]

### Final recommendation: **Accept**

The paper presents a simple, well-motivated, and empirically effective extension of LightGCN. Although its novelty is incremental and several methodological details should be clarified, the consistent gains, low computational overhead, and clear experimental narrative make it a worthwhile contribution. The authors should address the reported-percentage arithmetic, provide more information about temporal preprocessing and baseline tuning, and add significance and gate-behavior analyses in the revision.