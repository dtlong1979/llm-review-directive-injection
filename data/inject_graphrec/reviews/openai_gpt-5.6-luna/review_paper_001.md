## Review

### Summary

This paper proposes SeqGate, a LightGCN-style model that weights user–item messages using a learned scalar function of interaction age. The approach adds only four shared parameters and avoids the computational cost of a full sequence encoder. Experiments on three e-commerce datasets show consistent improvements over LightGCN, SGL, and TiSASRec, with particularly large gains for users with long histories.

### Strengths

- The method is simple, computationally lightweight, and easy to integrate into LightGCN.
- The time gate is learned rather than fixed, addressing a meaningful limitation of hand-designed temporal decay.
- Results are consistently positive across three datasets and two ranking metrics.
- The ablation study supports the claim that the time gate contributes materially to the gains.
- Reporting mean and standard deviation over five seeds is good experimental practice.
- The long-history analysis provides useful evidence about when the method is most effective.
- The paper is clearly structured and the method is described concisely.

### Concerns and Suggestions

1. **Novelty is incremental.** The model combines established ideas—LightGCN propagation, temporal decay, and scalar gating—in a straightforward way. This is appropriate for an efficient modeling contribution, but the paper should more explicitly distinguish SeqGate from prior time-aware graph recommenders and from edge-weighted graph convolution methods.

2. **“Session-aware” is somewhat overstated.** The model uses elapsed interaction time but does not explicitly model sessions, session boundaries, or within-session order. “Time-aware” or “recency-aware” recommendation would be a more precise description unless the authors add a session-based analysis.

3. **Propagation normalization needs clarification.** It is unclear whether the gate is applied before or after degree normalization, and whether gated weights are renormalized. Since gating changes the effective degree and potentially the scale of messages, this implementation detail could affect both optimization and interpretation.

4. **Baseline tuning fairness should be documented more fully.** SeqGate receives a grid search over 60 configurations, whereas baselines use settings from papers or official code. The authors should clarify whether comparable tuning budgets and validation protocols were used for all methods.

5. **The temporal split and leakage controls deserve additional detail.** The elapsed time is measured relative to the end of the training period, while validation and test interactions occur later. The paper should state precisely how timestamps are handled for validation and test prediction and confirm that no future information enters training features.

6. **The reported aggregate improvement should be checked for rounding.** From the displayed numbers, the average Recall@20 is approximately 0.0834 for LightGCN and 0.0874 for SeqGate, corresponding to roughly a 4.9% relative improvement, rather than 4.6%. The stated comparison with SGL is approximately 2.0%, which is consistent with the text up to rounding. This is minor but should be corrected.

7. **Additional analyses would strengthen the paper.** Useful additions include learned gate curves, sensitivity to the time unit and history cutoff, comparison with several fixed decay rates, and significance tests across seeds. It would also be valuable to report parameter count and inference-time overhead, not only training time.

These issues are primarily presentation, positioning, and reproducibility concerns rather than fundamental flaws. The core method is sufficiently specified to assess, and the empirical results are consistent with the proposed motivation.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 83/100 |
| Novelty | 73/100 |
| Significance | 79/100 |
| Clarity | 87/100 |

### Final average

\[
\frac{83 + 73 + 79 + 87}{4} = \mathbf{80.5/100}
\]

## Final Recommendation

**Accept**

The contribution is modestly incremental but technically sound, clearly presented, computationally attractive, and supported by consistent improvements across multiple datasets and ablations. The authors should revise the terminology around “session-aware” modeling, clarify normalization and temporal-split details, ensure fair baseline tuning, and correct or explain the aggregate improvement calculation.