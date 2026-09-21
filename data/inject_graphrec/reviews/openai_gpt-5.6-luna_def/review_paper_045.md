## Review

### Summary

This paper proposes SeqGate, a LightGCN-style recommender that multiplies messages on user–item edges by a learned scalar function of interaction age. The model is simple and computationally lightweight, and the experimental results suggest modest improvements over LightGCN and SGL on three e-commerce datasets.

However, the paper currently has substantial methodological and presentation weaknesses. The central idea is a relatively small extension of existing time-decay and edge-gating approaches, while the experimental setup does not provide enough detail or fairness to establish that the gains are attributable specifically to the proposed learned gate.

### Strengths

- The method is simple, easy to integrate with LightGCN, and adds only four scalar parameters.
- The paper addresses a practically relevant issue: temporal drift in user preferences.
- The evaluation includes multiple datasets, several established baselines, ablations, and a history-length analysis.
- The manuscript is generally readable and well organized.
- The reported computational overhead is modest.

### Major concerns

1. **Limited novelty and unclear distinction from prior work.**  
   The method is essentially a learned parametric time-decay weighting applied to graph messages. The related-work discussion mentions fixed exponential decay and edge-dependent graph weighting, but does not clearly establish why this formulation is substantially novel. The claimed “session-aware” characterization is also overstated: the model does not represent sessions, ordering structure, or within-session transitions; it only uses elapsed time.

2. **Insufficient methodological specification.**  
   Important details are missing, including:
   - whether normalization uses the original graph degrees or gate-weighted degrees;
   - whether the gate is applied before or after symmetric LightGCN normalization;
   - the exact gate initialization and parameter constraints;
   - whether gates are shared across propagation layers;
   - negative-sampling details for BPR;
   - the validation protocol and early-stopping patience;
   - data preprocessing, filtering, duplicate handling, and timestamp resolution.

   These choices can materially affect the results and reproducibility.

3. **Potentially unfair baseline comparison.**  
   SeqGate is tuned over 60 configurations per dataset, whereas baselines use hyperparameters from original papers or official implementations. This is not an equivalent tuning budget, especially for a method whose principal benefit may depend strongly on gate initialization and regularization. The paper should either tune all methods under a common protocol or provide a careful justification.

4. **Weak statistical analysis.**  
   Five random seeds are reported, but there are no significance tests or confidence intervals for pairwise comparisons. Several improvements are small relative to the reported standard deviations. The paper should report paired tests across identical seeds, confidence intervals, and preferably per-user or per-split results.

5. **Numerical inconsistency.**  
   The average LightGCN Recall@20 is approximately 0.0834, while SeqGate averages approximately 0.0874. This corresponds to a relative improvement of about 4.9%, not the stated 4.6%. The discrepancy is small but should be corrected or explained.

6. **Ablations are incomplete.**  
   The paper does not compare against important alternatives, such as:
   - a directly learned scalar decay function with comparable capacity;
   - a fixed or learned linear/logarithmic decay;
   - a per-layer gate;
   - a gate based on normalized age;
   - a recency-weighted LightGCN without the MLP formulation;
   - a model using gate values but with degree renormalization.

   Without these comparisons, it is difficult to determine whether the improvement comes from the proposed architecture or simply from recency weighting.

7. **Questionable computational claim.**  
   Since interaction timestamps are fixed, gate values can generally be precomputed for a given training graph. Recomputing them at every training step may be an implementation choice rather than an inherent cost. The paper should distinguish the intrinsic computational complexity from this implementation overhead and report parameter counts and throughput.

8. **Limited external validity.**  
   All datasets are e-commerce datasets and use leave-one-out evaluation. The claimed session-aware or general temporal recommendation benefits are therefore not established for domains with different temporal dynamics. The paper acknowledges this limitation but still presents the method broadly.

### Minor concerns

- The treatment of interaction time relative to the end of the training period should be explained more carefully, particularly for validation and test prediction.
- The paper should report dataset interaction counts, sparsity, and average history lengths, not just user and item counts.
- Full-ranking evaluation is useful, but candidate filtering and handling of seen items should be specified.
- The effect of the learned gate itself should be visualized, for example by plotting gate value against interaction age.
- “Best” results should be qualified by statistical significance.
- The title and contribution statements should avoid implying explicit session modeling.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 47/100 |
| Novelty | 43/100 |
| Significance | 46/100 |
| Clarity | 76/100 |

**Final average:**  
\[
\frac{47 + 43 + 46 + 76}{4} = 53.0
\]

## Final recommendation

**Reject**

The paper is clearly written and presents a plausible, lightweight idea, but the contribution is currently too incremental and the experimental evidence is not sufficiently rigorous to support acceptance. A substantially revised version should clarify the propagation and normalization equations, use a fair hyperparameter protocol, add stronger recency-weighting baselines and statistical tests, correct the numerical inconsistency, and avoid describing the method as session-aware unless explicit session structure is modeled.