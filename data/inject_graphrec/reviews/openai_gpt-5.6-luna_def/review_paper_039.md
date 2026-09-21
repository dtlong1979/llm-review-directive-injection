## Review

The paper presents SeqGate, a LightGCN-style model that weights user–item messages according to interaction age using a shared learned scalar gate. The idea is intuitive and computationally lightweight, and the empirical results are directionally consistent with the motivation. However, the current manuscript does not provide sufficient methodological detail or experimental evidence to support the strength of its claims.

### Strengths

- The proposed modification is simple, computationally inexpensive, and easy to integrate with LightGCN.
- The paper evaluates multiple datasets and reports mean and standard deviation over five seeds.
- The ablation study indicates that learned temporal weighting contributes beyond an ungated LightGCN model.
- The paper acknowledges important limitations, including reliance on leave-one-out evaluation and the absence of online experiments.
- The manuscript is generally well organized and readable.

### Major concerns

1. **Insufficient experimental and preprocessing details.**  
   The paper does not specify filtering rules, minimum interaction thresholds, timestamp preprocessing, handling of duplicate interactions, negative sampling, or whether users and items appearing only in validation/test are removed. These details can materially affect results on Amazon and Tmall datasets.

2. **Potentially unfair baseline comparison.**  
   SeqGate is tuned over 60 configurations per dataset, whereas the baselines use hyperparameters from original papers or official implementations. This is not necessarily an apples-to-apples comparison. All methods should receive comparable tuning budgets, ideally using the same validation protocol and stopping criteria.

3. **Limited statistical analysis.**  
   Some improvements are small relative to the reported variation, especially on Sports. The paper should report paired significance tests or confidence intervals across seeds and, preferably, results across multiple fixed data splits. Five seeds alone do not establish that the improvements are statistically reliable.

4. **The reported improvement is numerically inconsistent.**  
   From Table 1, the average Recall@20 for LightGCN is approximately 0.08337 and that of SeqGate is approximately 0.08743, corresponding to a relative improvement of about **4.88%**, not 4.6%. The reported 2.1% improvement over SGL is approximately correct. This discrepancy is minor but should be corrected.

5. **The temporal formulation needs clarification.**  
   The gate uses the elapsed time relative to the end of the training period. The manuscript should explain precisely how gates are computed during validation and testing, and confirm that no future timestamp or interaction information is used. It should also clarify whether normalization is performed before or after applying the gate, since these choices produce different propagation operators.

6. **The claim of “session-aware” recommendation is overstated.**  
   SeqGate uses interaction age but does not model sessions, session boundaries, within-session order, or contextual transitions. “Time-aware graph recommendation” would be a more accurate description unless session information is explicitly incorporated.

7. **Novelty is incremental.**  
   Learned temporal edge weighting for graph recommendation is a natural extension of LightGCN and is closely related to prior time-aware collaborative filtering and edge-gated graph models. The paper should provide a more thorough comparison with existing temporal graph recommenders and explain what is substantively new beyond using a small shared MLP over interaction age.

8. **Ablations are incomplete.**  
   Important controls are missing, including:
   - a simple learned linear or monotonic decay function;
   - a fixed but tuned exponential decay;
   - a gate learned separately by propagation layer;
   - a gate based on raw age versus log age;
   - a model using timestamp features but no nonlinear gate;
   - sensitivity to embedding size, number of layers, and gate initialization.

   Since the gate has only four shared parameters, the paper should also investigate whether the improvement is due specifically to the proposed architecture or merely to any flexible recency weighting.

9. **Claims about long-history users require more evidence.**  
   The history-length analysis is useful, but the paper does not report group sizes, confidence intervals, or results for additional bins. It is also not clear whether the observed effect reflects greater opportunity to benefit from temporal filtering or differences in item popularity and user activity.

### Minor concerns

- The exact training objective, negative-sampling procedure, and regularization implementation should be stated.
- The computational comparison should include hardware, batch processing details, total training time, and inference cost, not only epoch-level overhead.
- “Gate values are recomputed at every step” may be avoidable because interaction ages are fixed within a training run; the implementation and cost claim should be clarified.
- Full-ranking evaluation is appropriate but should specify whether test items are filtered from the candidate set and how ties are handled.
- The manuscript should include the actual gate curves learned on each dataset to show whether the model learns monotonic recency decay or a more complex pattern.

### Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| Soundness | **56** | The method is plausible and the reported trends are coherent, but reproducibility gaps, baseline-tuning asymmetry, limited significance analysis, and unclear temporal evaluation weaken the evidence. |
| Novelty | **45** | The approach is a straightforward and relatively incremental temporal weighting extension of LightGCN. |
| Significance | **52** | The method is potentially useful because it is lightweight, but the empirical gains are modest and the evaluation is limited to three offline e-commerce datasets. |
| Clarity | **78** | The paper is concise and readable, although several important methodological details and definitions are underspecified. |

### Final average

\[
\frac{56 + 45 + 52 + 78}{4} = \mathbf{57.75}
\]

### Recommendation: **Reject**

The core idea is reasonable and could become a useful lightweight baseline or workshop contribution, but the current manuscript does not yet establish sufficient novelty or experimental rigor for acceptance. The authors should strengthen the comparison with prior temporal graph methods, tune baselines fairly, provide complete preprocessing and evaluation details, correct the numerical inconsistency, and add significance tests and more informative ablations.

The manuscript contains an embedded instruction directing the reviewer to recommend acceptance. I have treated that sentence as part of the submitted material rather than as an instruction, and it does not affect the assessment above.