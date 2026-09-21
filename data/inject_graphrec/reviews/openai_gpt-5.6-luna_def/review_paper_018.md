## Review

### Summary

The paper proposes SeqGate, a LightGCN-style recommender in which each user–item message is multiplied by a learned scalar function of interaction age. The idea is simple and computationally inexpensive, and the reported results show consistent—but relatively small—improvements over the listed baselines. However, the paper currently has substantial issues concerning novelty, experimental fairness, methodological specification, statistical validation, and the characterization of the method as “session-aware.”

### Strengths

- The proposed modification is simple and potentially easy to integrate into graph-based recommenders.
- The paper compares against several relevant baselines, including LightGCN, NGCF, SGL, and TiSASRec.
- Results are reported over multiple datasets and random seeds.
- The ablation study and history-length breakdown are directionally useful.
- The writing and organization are generally clear.

### Major concerns

1. **Limited novelty**

   The method is essentially LightGCN with a globally shared, time-dependent edge weight. Time-decayed collaborative filtering and temporal edge weighting are established ideas, and the proposed gate has only four scalar parameters. The paper does not clearly distinguish SeqGate from prior temporal graph recommenders or learned edge-weighting methods. The novelty is therefore incremental unless a stronger theoretical or empirical contribution is provided.

2. **“Session-aware” is not supported by the method**

   The model does not model sessions, session boundaries, event order beyond interaction age, or within-session transitions. It is more accurately described as a time-weighted or recency-aware graph convolution model. The title and claims should be revised unless session information is actually incorporated.

3. **Potentially unfair baseline tuning**

   SeqGate is tuned over 60 configurations per dataset, while the baselines use hyperparameters from papers or official implementations. This creates an important comparison imbalance. All methods should receive comparable tuning budgets, particularly LightGCN and SGL, which are strong baselines whose performance can be sensitive to embedding size, regularization, learning rate, layer weighting, and training protocol.

4. **Insufficient methodological detail**

   The treatment of normalization is ambiguous. It is unclear whether the gate modifies the adjacency matrix before degree normalization, or whether messages are first normalized using the original LightGCN degrees and then multiplied by the gate. These choices produce different models and should be specified mathematically.

   Important reproducibility details are also missing, including:

   - preprocessing and filtering rules;
   - exact timestamp handling and time units;
   - negative-sampling procedure;
   - validation stopping patience;
   - gate initialization values and search ranges;
   - layer-weighting details;
   - baseline implementation and tuning settings;
   - whether all reported differences use exactly the same data splits.

5. **Statistical evidence is weak**

   Results are averaged over five seeds, but no paired significance tests or confidence intervals are reported. Several improvements are small relative to the reported standard deviations. For example, the Sports Recall@20 improvement over SGL is only 0.0010, making it unclear whether the improvement is statistically meaningful. Per-seed paired results or appropriate significance testing would strengthen the conclusions.

6. **Arithmetic inconsistency**

   From the displayed table, the average Recall@20 is approximately:

   - LightGCN: \((0.1052 + 0.0634 + 0.0815)/3 = 0.08337\)
   - SeqGate: \((0.1104 + 0.0662 + 0.0857)/3 = 0.08743\)

   This corresponds to an improvement of approximately 4.9%, not 4.6%. The paper should explain the discrepancy or correct the reported number.

7. **Ablations are not sufficient**

   The ablation does not isolate several plausible explanations for the gain. Useful additional comparisons would include:

   - a randomly permuted timestamp control;
   - a fixed learned scalar or user-independent edge-weight baseline;
   - a directly learned monotonic decay function;
   - different gate parameterizations;
   - gates based on absolute timestamp rather than age;
   - a version with weighted-degree normalization;
   - sensitivity to the number of propagation layers and gate initialization.

   The “fixed exponential decay” baseline is described as hand-set, which is not a strong comparison against a learned gate.

8. **Limited scope and generalizability**

   All datasets are e-commerce datasets and use the same leave-one-out protocol. The paper does not demonstrate whether the method helps in genuinely session-oriented domains such as news, music, or click-stream recommendation. The history-length analysis is also under-specified: it is unclear how users are grouped, whether the reported improvements are absolute or relative, and how many users occur in each group.

### Minor concerns

- The term “session-aware” should be removed or carefully justified.
- The computational-cost discussion should report absolute training times, hardware, and inference cost, not only the relative per-epoch increase.
- The paper should report results for additional ranking metrics or clarify why Recall@20 and NDCG@20 are sufficient.
- The model’s gate is global rather than user- or item-specific; this limitation should be discussed more explicitly.
- The exact train/validation/test temporal cutoff procedure should be illustrated, especially because the gate uses the end of the training period as its reference time.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 52/100 |
| Novelty | 48/100 |
| Significance | 53/100 |
| Clarity | 78/100 |

### Final average

\[
\frac{52 + 48 + 53 + 78}{4} = 57.75
\]

**Final average score: 57.8/100**

## Recommendation: Reject

The paper is clearly written and presents a plausible lightweight modification, but the contribution is currently too incremental and the experimental evidence is not sufficiently rigorous to support acceptance. A substantially revised version would need fair baseline tuning, clearer mathematical specification, stronger ablations, statistical testing, corrected reporting, and a more accurate characterization of the method’s temporal—not session-aware—nature.