## Review

### Summary

This paper proposes SeqGate, a LightGCN-style model that modulates messages on user–item edges using a learned scalar function of interaction age. The approach is simple, computationally lightweight, and aimed at addressing preference drift without introducing a full sequence encoder. Experiments on three public e-commerce datasets show consistent improvements over LightGCN and several other baselines, with the largest gains for users with longer histories.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 78/100 |
| Novelty | 65/100 |
| Significance | 73/100 |
| Clarity | 86/100 |
| **Final average** | **75.5/100** |

### Strengths

1. **Simple and well-motivated method.** Incorporating interaction age into graph propagation is a natural way to address the static-graph limitation of LightGCN while preserving its efficiency.
2. **Low parameter and architectural overhead.** The proposed gate uses only four shared scalar parameters and does not require a sequence encoder.
3. **Consistent empirical improvements.** SeqGate outperforms LightGCN, SGL, NGCF, BPR-MF, and TiSASRec on all reported dataset/metric combinations.
4. **Useful ablations.** The comparison with fixed exponential decay and one-directional gating supports the claim that a learned, bidirectional gate is beneficial.
5. **Relevant subgroup analysis.** The history-length breakdown is informative and aligns with the intuition that temporal weighting is more useful when users have substantial histories.
6. **Clear presentation.** The paper is concise, easy to follow, and provides the core model equation, training setup, datasets, baselines, and primary results.

### Concerns and suggestions

1. **Novelty is incremental.** The method is a relatively direct combination of LightGCN and a learned temporal decay function. The paper should more explicitly distinguish SeqGate from prior time-aware graph recommendation and edge-weighting methods, including whether similar age-dependent propagation schemes have already been studied.
2. **Some experimental details are underspecified.** The paper should clarify:
   - whether normalization is applied before or after multiplying messages by the gate;
   - whether the gate is recomputed during each propagation operation or cached;
   - how timestamps are handled when users have multiple interactions with the same item;
   - whether validation and test timestamps are excluded from all gate computations;
   - the exact negative-sampling procedure and evaluation protocol.
3. **Baseline tuning may not be fully comparable.** SeqGate is tuned over 60 configurations, whereas the baselines use settings from their original papers or official implementations. A fairer comparison would tune the main baselines under the same validation protocol or provide a sensitivity analysis.
4. **Statistical reporting could be stronger.** Means and standard deviations over five seeds are useful, but paired significance tests or confidence intervals would better establish that the improvements are statistically reliable.
5. **A numerical claim should be corrected or explained.** Using the table values, the average Recall@20 for LightGCN is approximately 0.0834 and for SeqGate approximately 0.0874, corresponding to an improvement of about 4.9%, rather than 4.6%. The stated 2.1% improvement over SGL is approximately consistent with the table. The authors should reconcile these figures.
6. **“Session-aware” may overstate the method.** SeqGate uses interaction age but does not explicitly model session boundaries, within-session order, or session context. “Time-aware” or “recency-aware” recommendation would be more precise unless the terminology is carefully justified.
7. **Efficiency discussion could be improved.** Since interaction ages are fixed relative to the training cutoff, gate values may be precomputed or cached for a static training graph. The reported 9% overhead is reasonable, but the implementation choice and memory/computation trade-off should be explained.
8. **Scope of evaluation is limited.** The study focuses on three e-commerce datasets and leave-one-out evaluation. Additional temporal splits, robustness checks across different decay regimes, or experiments on a faster-drift domain would strengthen the conclusions.

### Overall assessment

The paper presents a practical and clearly described improvement to graph-based collaborative filtering. Its central idea is not highly novel, but the method is appropriately lightweight, empirically consistent, and supported by relevant ablations. The main issues concern experimental comparability, reporting precision, and clarification of the temporal graph-convolution implementation rather than fundamental flaws in the approach.

## Final recommendation: **Accept**

The work is suitable for acceptance, with minor revisions addressing the numerical discrepancy, terminology, baseline tuning details, and missing implementation specifics.