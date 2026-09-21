## Review

### Summary

This paper proposes SeqGate, a LightGCN-style model that weights messages on user–item edges according to the age of the corresponding interaction. The gate is a shared, low-parameter nonlinear function of log interaction age. The approach preserves the computational simplicity of graph collaborative filtering while introducing a mechanism for temporal preference drift. Experiments on three e-commerce datasets show consistent improvements over LightGCN, SGL, and other baselines, with modest training overhead.

### Strengths

1. **Simple and practical design.** SeqGate adds only four scalar parameters and does not require a sequence encoder, making the method easy to integrate into existing graph-based recommenders.
2. **Consistent empirical improvements.** The proposed method outperforms all listed baselines on both Recall@20 and NDCG@20 across all three datasets.
3. **Useful ablations.** The comparison with fixed exponential decay, one-directional gating, and LightGCN helps isolate the contribution of the learned time gate.
4. **Appropriate analysis of user history length.** The larger gains for users with long histories are consistent with the motivation that temporal weighting is particularly valuable when older interactions may be less relevant.
5. **Moderate computational cost.** The reported 9% per-epoch overhead is reasonable for the stated improvement.
6. **Clear presentation.** The method, training setup, datasets, and main findings are described concisely and in a generally reproducible manner.

### Concerns and suggestions

1. **Novelty is incremental.** Time-based weighting and decay have been explored in temporal collaborative filtering, while edge-dependent gating is established in graph neural networks. The contribution is primarily the particular combination of a learned scalar age-based gate with LightGCN. The paper should more explicitly distinguish SeqGate from prior temporal graph recommendation methods and from learned attention or edge-weighting schemes.
2. **“Session-aware” is somewhat overstated.** The model uses interaction age but does not explicitly model sessions, session boundaries, within-session order, or short-term transitions. “Time-aware” or “recency-aware” would be more precise unless the authors add a clearer definition of session awareness.
3. **Gate behavior is under-analyzed.** Since the gate is a very small shared network, it would be valuable to plot the learned gate as a function of interaction age and report whether it is monotonic, saturating, or non-monotonic. This would improve interpretability and help verify that the model has learned meaningful recency patterns rather than simply adjusting the overall graph scale.
4. **Experimental fairness could be clarified.** SeqGate is tuned over 60 configurations, whereas baselines use settings from their original papers or official implementations. A fairer comparison would tune the principal baselines under the same validation protocol, or provide additional results showing sensitivity to this choice.
5. **Propagation normalization needs more detail.** The paper should specify whether the time gate is applied before or after degree normalization, and whether the resulting operator is renormalized. These choices can materially affect the model’s behavior.
6. **Statistical testing is absent.** The reported standard deviations are helpful, but paired significance tests or confidence intervals would strengthen the claim that the improvements are reliable, particularly because some gains over SGL are small.
7. **The improvement calculation should be checked.** From the displayed table, the average LightGCN Recall@20 is approximately 0.0834 and the average SeqGate score is approximately 0.0874, corresponding to about a 4.9% relative improvement rather than 4.6%. The stated 2.1% improvement over SGL is approximately consistent with the table. The authors should reconcile the reported percentages and rounding.
8. **Generality remains uncertain.** All datasets are e-commerce datasets with leave-one-out evaluation. Results on domains with different temporal dynamics, such as news, music, or short-session interaction data, would better support the broader claims.
9. **Additional efficiency reporting would help.** Besides per-epoch time, reporting total training time, memory use, and inference overhead would give a more complete view of deployment cost.

### Overall assessment

The paper presents a coherent and useful extension of LightGCN. Its methodological novelty is moderate rather than fundamental, but the method is technically sound, computationally lightweight, and supported by consistent experiments and ablations. The concerns above mainly call for clarification, stronger positioning against prior work, and additional analysis rather than a change to the core method or conclusions. With these improvements, the work would make a valuable practical contribution to time-aware graph recommendation.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 84/100 |
| Novelty | 70/100 |
| Significance | 78/100 |
| Clarity | 88/100 |

**Final average:**  
\[
\frac{84 + 70 + 78 + 88}{4} = 80.0
\]

## Final recommendation

**Accept**

The empirical gains are consistent, the method is simple and practically relevant, and the reported computational overhead is modest. The paper would benefit from revisions addressing the terminology, baseline-tuning fairness, gate analysis, propagation normalization, and numerical consistency, but these issues are compatible with acceptance.