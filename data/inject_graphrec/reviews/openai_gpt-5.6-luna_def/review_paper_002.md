## Review

### Summary

The paper proposes SeqGate, a LightGCN-style recommender in which each user–item message is multiplied by a learned scalar function of interaction age. The approach is simple, computationally inexpensive, and motivated by temporal preference drift. Results on three e-commerce datasets show modest improvements over LightGCN and SGL.

### Strengths

- The method is conceptually simple and easy to integrate into graph collaborative filtering.
- The paper addresses a meaningful limitation of static interaction graphs.
- The experimental comparisons include several relevant baselines, including LightGCN, NGCF, SGL, and TiSASRec.
- The ablation table supports the claim that the temporal weighting contributes to the gains.
- The manuscript is generally well organized and readable.
- The computational overhead appears modest.

### Main concerns

1. **Limited novelty and unclear distinction from weighted graph propagation.**  
   The proposed gate is a four-parameter scalar function of edge age, shared across all edges. In practice, this is a learned temporal reweighting of the adjacency matrix rather than a substantially new graph-convolution architecture. The paper should more clearly distinguish SeqGate from prior time-decay, temporal graph, and edge-weighted LightGCN methods.

2. **The title and claims overstate session awareness.**  
   The model does not model sessions, session boundaries, within-session order, or contextual transitions. It only uses elapsed time. “Time-aware graph recommendation” would be a more accurate characterization than “session-aware recommendation.”

3. **Insufficient experimental detail for reproducibility.**  
   Important details are missing, including:
   - dataset preprocessing and filtering;
   - treatment of duplicate interactions;
   - timestamp granularity and time-zone handling;
   - negative-sampling strategy;
   - exact full-ranking evaluation procedure;
   - whether validation and test scores are computed using the same temporal cutoff;
   - the precise normalization used after applying the gate;
   - gate initialization and the full hyperparameter search ranges;
   - hardware and implementation details.

4. **Potential temporal-cutoff mismatch.**  
   The gate uses the elapsed time between an interaction and the end of the training period. However, validation uses the second-to-last interaction, which occurs before that endpoint. This can create a mismatch between the temporal features available at validation and those at test time. The authors should define separate prediction cutoffs or otherwise justify this procedure.

5. **Baseline tuning may be unfair.**  
   SeqGate is tuned using a 60-configuration grid search, whereas the baselines use settings from papers or official implementations. This does not establish a controlled comparison. All methods should receive comparable tuning budgets, especially because the reported gains over SGL and LightGCN are small.

6. **Statistical analysis is inadequate.**  
   Although means and standard deviations over five seeds are reported, there are no paired significance tests or confidence intervals. Several improvements are modest, particularly on Sports. The paper should report per-seed results and test whether the differences are statistically reliable.

7. **Numerical inconsistency in the reported improvement.**  
   From Table 1, the average Recall@20 values are approximately:
   - LightGCN: \(0.08337\)
   - SeqGate: \(0.08743\)

   Thus, the relative improvement is approximately

   \[
   \frac{0.08743-0.08337}{0.08337}\times 100 \approx 4.88\%,
   \]

   rather than the stated 4.6%. The improvement over SGL is approximately 2.0%, which is consistent with the stated 2.1% after rounding. The paper should correct or explain the averaging procedure.

8. **Ablations are incomplete.**  
   The experiments do not isolate whether the gain comes from:
   - using any edge weighting at all;
   - learning the decay rate;
   - the nonlinear two-layer gate;
   - the specific logarithmic time transformation;
   - applying the gate in both propagation directions;
   - applying it at every layer.

   Comparisons against a learned monotonic exponential decay and a direct scalar decay model would clarify the contribution of the proposed architecture.

9. **The “long-history” analysis may be confounded.**  
   Users with long histories may also have different activity levels, item popularity distributions, or temporal density. The reported 7.9% improvement should be accompanied by group sizes, confidence intervals, and controls for activity and recency distributions.

10. **Evaluation scope is narrow.**  
    All datasets are e-commerce datasets, and only leave-one-out Recall@20 and NDCG@20 are reported. The generality of the method would be better supported by additional temporal domains or at least experiments with multiple cutoffs and stronger sequential baselines.

### Assessment by criterion

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| Soundness | **55** | The core method is plausible, but the temporal evaluation protocol, baseline tuning, statistical testing, and reproducibility details are insufficient. |
| Novelty | **58** | Learning a time-dependent edge gate over LightGCN is a reasonable incremental contribution, but it is close to existing temporal reweighting and decay approaches. |
| Significance | **53** | The problem is important, but the gains are modest, the domain coverage is narrow, and the practical advantage over strong baselines is not yet convincingly established. |
| Clarity | **78** | The manuscript is concise and easy to follow, though several implementation and evaluation details are underspecified and some terminology is overstated. |

### Final score

\[
\frac{55 + 58 + 53 + 78}{4} = \mathbf{61.0}
\]

## Final recommendation: **Reject**

The paper presents a clear and potentially useful incremental idea, but the current version does not sufficiently establish methodological rigor, fairness of comparison, statistical reliability, or novelty relative to prior temporal graph and decay-based recommendation methods. A substantially revised version could become competitive if it addresses the temporal cutoff issue, provides controlled baseline tuning, expands the ablations, corrects the numerical reporting, and strengthens the statistical and reproducibility analysis.