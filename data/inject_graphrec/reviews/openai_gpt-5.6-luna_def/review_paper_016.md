## Review

### Summary

This paper proposes SeqGate, a LightGCN-style model that multiplies messages on user–item edges by a learned scalar function of interaction age. The method is simple and computationally lightweight, and the reported results show modest improvements over LightGCN, SGL, and TiSASRec on three e-commerce datasets. However, the empirical evidence and methodological description are not yet sufficient to establish that the gains are robust or that the method represents a substantial advance over existing time-aware graph weighting approaches.

### Strengths

- The method is conceptually simple and easy to integrate into LightGCN.
- The paper addresses a practically relevant issue: temporal preference drift.
- Experiments include multiple datasets, several relevant baselines, and five random seeds.
- The leave-one-out temporal split is appropriate for next-interaction prediction.
- The reported computational overhead is small.
- The paper includes ablations and a history-length analysis.

### Major concerns

1. **Limited novelty**

   The proposed gate is a four-parameter scalar function of interaction age, shared across all edges. Conceptually, this is close to learning a global time-decay weighting of graph edges. The distinction from prior time-aware collaborative filtering methods is not developed sufficiently, and the paper does not compare against a learned exponential/power-law decay or other learned temporal weighting baselines. The contribution may be useful, but its novelty appears incremental.

2. **Insufficient experimental detail**

   Important implementation details are missing, including:

   - exact preprocessing and filtering procedures;
   - treatment of duplicate interactions and timestamps;
   - negative-sampling strategy;
   - precise gate initialization;
   - learning-rate and regularization search ranges;
   - hardware and wall-clock training cost;
   - whether graph normalization is performed before or after applying the gate;
   - whether the gate is recomputed dynamically or simply precomputed from static timestamps.

   These omissions make the experiments difficult to reproduce.

3. **Potentially unfair baseline comparison**

   SeqGate is tuned using a grid of 60 configurations per dataset, whereas baselines use settings recommended in their original papers or official implementations. This is not necessarily an apples-to-apples comparison, especially across datasets whose distributions differ substantially. Baseline tuning protocols, search spaces, and computational budgets should be matched.

4. **Weak statistical evidence**

   Although standard deviations are reported for the main table, the improvements are relatively small. No paired significance tests or confidence intervals are provided. The ablation table reports no variance at all, despite claims that the time gate accounts for most of the improvement. In particular, the difference between SeqGate and SGL is small and may not be statistically significant.

5. **Questionable interpretation of the ablation**

   The “fixed exponential decay” comparison uses a hand-set rate, but there is no learned-decay baseline or tuning procedure for the decay rate. This makes it difficult to determine whether the benefit comes from the neural gate specifically or simply from using a better temporal weighting. The paper should also test constant gates, monotonic constrained gates, and a learned one-dimensional decay function with comparable capacity.

6. **The “session-aware” characterization is unsupported**

   The method uses elapsed time from the end of the training period, not session boundaries or within-session temporal structure. It is therefore more accurately described as time-aware or recency-weighted graph collaborative filtering. Calling it “session-aware” overstates what the model represents.

7. **Possible arithmetic inconsistency**

   From Table 1, the average Recall@20 for LightGCN is approximately 0.08337 and for SeqGate approximately 0.08743, corresponding to a relative improvement of about 4.9%, not the stated 4.6%. The stated 2.1% improvement over SGL is approximately correct. This discrepancy should be corrected.

8. **Unclear propagation semantics**

   The paper states that the message is multiplied by the gate “before normalised aggregation,” but it does not specify whether the gate modifies only the message, the adjacency normalization, or both. These choices produce different models and should be formally defined. Since the gate is shared in both directions, the implications for the symmetric LightGCN propagation operator also need clarification.

9. **Limited scope of evaluation**

   All datasets are e-commerce datasets, and no comparison is made against stronger recent temporal graph or sequential recommendation methods beyond TiSASRec. The history-length result is potentially interesting, but the paper does not report group sizes, confidence intervals, or whether the same users/items are evaluated in each subgroup.

10. **Efficiency claim needs clarification**

    Since the gate depends only on fixed interaction timestamps and globally shared parameters, gate values could likely be cached or recomputed only when parameters change. The explanation that values are recomputed “at every step” needs clarification, as does the choice of implementation. Reported training time should include hardware, total training time, and memory usage.

### Minor concerns

- The notation uses scalar \(w_1,w_2,b_1,b_2\), but the dimensions and exact activation behavior should be stated explicitly.
- The gate is not constrained to be monotonic in age. Depending on the learned parameter signs, older interactions could receive larger weights. If recency is intended, a monotonic parameterization or an analysis of learned gate curves would be useful.
- The manuscript should show the learned gate as a function of interaction age for each dataset.
- Full-ranking evaluation should specify whether users’ training and validation items are excluded from candidate rankings.
- The claim that the method “adds only four parameters” is technically true but somewhat misleading because it also changes every edge message and the propagation operator.
- The paper should distinguish absolute-point improvements from relative percentage improvements.

## Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **62** | The core method is plausible and the evaluation setup is broadly reasonable, but missing details, weak statistical validation, ambiguous propagation normalization, and possible comparison imbalance limit confidence. |
| **Novelty** | ** fifty?** | Need numeric. **52** | The learned temporal edge weighting is a modest extension of LightGCN and prior time-decay methods. The combination is sensible but not highly novel. |
| **Significance** | **57** | The problem is important and the gains are potentially useful, but the improvements are small and the evidence does not establish broad or robust impact. |
| **Clarity** | **73** | The manuscript is generally readable and well organized, but several technical and experimental details are underspecified, and “session-aware” is misleading. |

### Final average

\[
\frac{62 + 52 + 57 + 73}{4} = 61.0
\]

**Final average score: 61.0/100**

## Recommendation: **Reject**

The paper presents a reasonable and potentially useful idea, but in its current form it does not provide sufficient evidence of substantial novelty or robust empirical superiority. A stronger revision should include carefully matched baseline tuning, learned-decay comparisons, complete implementation details, statistical significance testing, clearer propagation mathematics, corrected metric calculations, and a more accurate characterization as time-aware rather than session-aware recommendation.