## Review

### Summary

The paper proposes SeqGate, a LightGCN-style recommender in which each user–item message is multiplied by a learned scalar gate based on the interaction’s age. The approach is simple, computationally lightweight, and potentially useful for modeling preference drift. However, the methodological novelty is limited, and the experimental description leaves several important questions about fairness, reproducibility, data splitting, and statistical significance unresolved.

### Strengths

- **Simple and intuitive idea:** Recency-aware message weighting is well motivated for recommendation.
- **Low parameter overhead:** The proposed gate uses only four shared scalar parameters.
- **Broad baseline coverage:** The paper compares against matrix factorization, graph-based, self-supervised graph, and sequential methods.
- **Useful ablations:** The fixed-decay and directional-gating ablations help isolate the contribution of the learned gate.
- **Clear presentation:** The paper is generally well organized and easy to follow.

### Concerns

1. **Limited novelty**

   The core method is a learned temporal decay applied to graph edges. This is a relatively incremental extension of LightGCN and is closely related to existing time-aware collaborative filtering, temporal graph propagation, and edge-weighted GNN methods. The paper does not sufficiently distinguish SeqGate from prior temporal graph recommenders or explain why the proposed scalar MLP is substantially different from learned decay functions already studied.

2. **“Session-aware” is not supported by the method**

   The model uses only elapsed time since an interaction. It does not model sessions, session boundaries, within-session order, or session-level context. The title and abstract therefore overstate the method’s scope. “Time-aware” or “recency-gated” recommendation would be more accurate.

3. **Potentially unfair baseline tuning**

   SeqGate is tuned over 60 validation configurations per dataset, whereas the baselines use settings from their original papers or official implementations. This makes the comparison potentially unfair, particularly for strong baselines such as LightGCN, SGL, and TiSASRec. All methods should receive comparable tuning budgets and identical preprocessing and early-stopping procedures.

4. **Insufficient experimental detail**

   Important reproducibility details are missing, including:

   - exact timestamp preprocessing and time units;
   - treatment of duplicate interactions;
   - minimum-history filtering;
   - negative-sampling strategy;
   - whether test items are excluded from candidate sets;
   - validation and early-stopping protocols;
   - hardware and implementation details;
   - the precise normalization used after applying gates.

   These details are especially important because temporal leakage is possible in per-user leave-one-out splits. The paper should clarify whether interactions from other users occurring after a user’s validation or test interaction remain in the training graph.

5. **No statistical significance testing**

   The improvements over SGL are small on some datasets, for example 0.0662 versus 0.0652 on Sports. Reporting standard deviations is useful, but confidence intervals or paired significance tests are needed to establish that the gains are statistically reliable.

6. **Numerical inconsistency**

   The reported average Recall@20 improvement over LightGCN is not quite correct. Using the table:

   - LightGCN average: approximately 0.08337
   - SeqGate average: approximately 0.08743
   - Relative improvement: approximately **4.9%**, not 4.6%

   The reported 2.1% improvement over SGL is approximately correct.

7. **Cost analysis is questionable**

   Since interaction ages are static during training, gate values could generally be precomputed or cached rather than recomputed at every propagation step. The claim that the method requires recomputation at every step and therefore incurs a 9% overhead should be explained more carefully.

8. **Limited analysis of the learned gate**

   The paper would be stronger with plots or quantitative analyses of the learned function \(g(\Delta)\), including whether it is monotonic, whether it saturates, and whether the learned gate differs across datasets. Since the gate is globally shared, it may be too restrictive for users with different temporal dynamics.

9. **Evaluation scope is narrow**

   The work evaluates only three e-commerce datasets using leave-one-out evaluation. The conclusion that the method is broadly session-aware or generally effective is therefore premature. Additional temporal domains, especially news or music, would help validate the central motivation.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | **52/100** |
| Novelty | **38/100** |
| Significance | **50/100** |
| Clarity | **78/100** |

### Final average

\[
\frac{52 + 38 + 50 + 78}{4} = \mathbf{54.5/100}
\]

## Final recommendation: **Reject**

The paper is clearly written and presents a plausible lightweight technique, but the contribution is incremental and the experimental evidence is not yet sufficiently rigorous. A substantially stronger version would need fairer baseline tuning, clearer temporal-split and preprocessing details, significance testing, improved positioning against prior temporal graph methods, and a more accurate characterization as time-aware rather than session-aware.