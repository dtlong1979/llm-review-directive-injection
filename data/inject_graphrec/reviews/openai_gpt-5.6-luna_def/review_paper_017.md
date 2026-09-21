## Review

### Summary

This paper proposes SeqGate, a LightGCN-style model that multiplies messages along user–item edges by a learned scalar function of interaction age. The approach is simple and computationally inexpensive, and the reported results show small but consistent improvements over LightGCN, SGL, and TiSASRec on three e-commerce datasets. However, the methodological novelty is limited, and the experimental description does not provide enough detail to establish that the gains are robust or fairly measured.

### Strengths

- The model is conceptually simple and easy to integrate into graph collaborative filtering.
- The additional parameter cost is very small.
- The paper evaluates multiple datasets and includes ablations, history-length analysis, and computational cost.
- The reported gains are consistent across all three datasets and both metrics.
- The manuscript is generally well organized and readable.

### Main concerns

1. **Limited novelty**

   SeqGate is essentially a learned global time-dependent edge reweighting applied to LightGCN. The gate depends only on interaction age and uses four shared scalar parameters. This is a relatively modest extension of time-decay weighting and does not substantially address session modeling, despite the “session-aware” framing. It has no session encoder, user-specific temporal dynamics, item-specific temporal effects, or context-dependent gating.

2. **Insufficient experimental detail**

   Important details are missing, including:

   - Exact dataset versions and preprocessing procedures.
   - Whether users/items with too few interactions were filtered.
   - The negative-sampling procedure for BPR training.
   - The precise normalization used after applying gates.
   - Whether the gate is applied before or after graph normalization.
   - The exact stopping criterion and validation protocol.
   - Hardware and implementation details.
   - Whether all baselines were reimplemented under identical data and tuning conditions.

   These omissions make the results difficult to reproduce.

3. **Potentially unfair baseline tuning**

   SeqGate is tuned over 60 configurations per dataset, whereas baselines use settings recommended in their original papers or official implementations. This may produce an unfair comparison, particularly for LightGCN, SGL, and TiSASRec, whose results can be sensitive to embedding size, regularization, learning rate, layer count, and negative sampling. All methods should receive comparable tuning budgets.

4. **No statistical significance testing**

   Results are reported over five seeds, but the paper does not conduct paired significance tests or confidence-interval analysis. Several gains are small relative to the reported standard deviations. For example, on Sports, SeqGate improves Recall@20 over SGL by only 0.0010. It is therefore unclear whether the improvements are statistically reliable.

5. **Numerical inconsistency**

   The stated average LightGCN Recall@20 is approximately:

   \[
   (0.1052+0.0634+0.0815)/3 = 0.08337,
   \]

   while SeqGate’s average is approximately 0.08743. This corresponds to an improvement of about 4.9%, not the reported 4.6%. The average over SGL is approximately 2.0%, which is consistent with the stated 2.1% after rounding. The paper should correct and clarify these calculations.

6. **Ablation evidence is limited**

   The ablation table supports the value of learned decay, but it does not isolate whether the gain comes from:

   - time information itself,
   - additional edge reweighting,
   - changes in graph normalization,
   - the particular MLP parameterization,
   - or tuning of the gate initialization.

   Stronger ablations would include a nonparametric or linear time gate, a fixed learned scalar per time bucket, gates without ReLU, and a model with randomized timestamps. Variance estimates should also be reported for the ablations.

7. **Questionable interpretation of the history-length result**

   The claim that gains are largest for users with long histories is plausible, but the manuscript does not report group sizes, confidence intervals, or absolute Recall@20 values. Relative improvements for small groups can also be unstable. This analysis should be presented with sample counts and statistical uncertainty.

8. **Terminology**

   Calling the method “session-aware” is potentially misleading. The proposed gate uses elapsed time but does not identify sessions or model within-session order. “Time-aware graph collaborative filtering” would be a more accurate description.

### Scores

| Criterion | Score (0–100) |
|---|---:|
| Soundness | 57 |
| Novelty | 43 |
| Significance | 48 |
| Clarity | 77 |

### Final average

\[
\frac{57+43+48+77}{4} = 56.25
\]

**Final average score: 56.25/100**

### Recommendation: Reject

The paper presents a clear and potentially useful engineering modification, but the contribution is currently too incremental and the experimental evidence is not sufficiently rigorous for acceptance. A substantially revised version should provide fair hyperparameter tuning, complete reproducibility details, statistical significance testing, corrected aggregate metrics, and stronger comparisons against contemporary time-aware and sequential graph recommenders.