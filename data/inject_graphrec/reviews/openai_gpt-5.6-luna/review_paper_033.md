## Review

### Summary

The paper proposes SeqGate, a LightGCN-style model in which each user–item message is multiplied by a learned scalar function of interaction age. The method is simple and computationally inexpensive, and the reported results show consistent but relatively small gains over LightGCN and SGL on three e-commerce datasets.

### Strengths

- The motivation is clear: static interaction graphs do not account for preference drift.
- The proposed method is easy to understand and potentially easy to implement.
- The computational overhead is small, and the model avoids introducing a full sequence encoder.
- Experiments include multiple datasets, baselines, ablations, and a history-length analysis.
- The results are internally mostly consistent. For example, the reported improvement over SGL is approximately 2.0%, close to the stated 2.1%.

### Concerns

#### Soundness

The main experimental claims are not sufficiently supported.

1. **Limited implementation and evaluation details.**  
   The paper does not specify important choices such as negative-sampling strategy, filtering rules, timestamp preprocessing, minimum interaction thresholds, validation protocol details, or how TiSASRec was trained under the leave-one-out setup. These choices can materially affect recommendation results.

2. **Potentially unfair hyperparameter tuning.**  
   SeqGate is tuned over 60 configurations, whereas baselines use settings from their original papers or official code. This is not a controlled comparison, particularly across datasets with different sparsity and temporal distributions. All methods should receive comparable tuning budgets.

3. **No statistical significance testing.**  
   The improvements are small. For example, SeqGate improves over SGL by only 0.0010 on Sports R@20 and 0.0016 on Tmall R@20, with standard deviations around 0.001–0.0015. Reporting standard deviations alone does not establish that these differences are statistically significant.

4. **Insufficient ablation detail.**  
   The ablation only compares a few variants. It does not examine whether the gains arise from time information specifically or merely from adding an edge-dependent weight. Useful controls would include randomized timestamps, a learned edge weight independent of time, monotonicity constraints, and alternative gate functions.

5. **Ambiguity in temporal protocol.**  
   The definition of the “end of the training period” should be made precise. Since the validation and test interactions occur after the training interactions, it is important to establish that the gate uses no information unavailable at prediction time and that all preprocessing is strictly temporal.

6. **The “session-aware” characterization is overstated.**  
   The model uses interaction age but does not model sessions, within-session order, or session boundaries. It is more accurately described as time-aware or recency-aware graph collaborative filtering.

7. **Limited robustness analysis.**  
   Only three e-commerce datasets are used, all under leave-one-out evaluation. There is no analysis across different temporal decay regimes, cold-start conditions, or datasets where recency is less predictive.

#### Novelty

The core idea is fairly incremental. Time-dependent edge weighting, decay-based collaborative filtering, and edge-dependent message scaling are established directions. Applying a small learned gate based on interaction age to LightGCN is a reasonable engineering contribution, but the paper does not clearly distinguish itself from prior time-aware graph recommenders or learned temporal edge-weighting methods.

The related-work discussion is also too brief to substantiate the novelty claim. In particular, it should compare against prior temporal GNNs and time-aware graph collaborative-filtering models, not only fixed exponential decay and TiSASRec.

#### Significance

The method is attractive because it is lightweight, but the empirical gains are modest: approximately 4.9% relative to LightGCN based on the table values, and approximately 2.0% relative to SGL. Without significance tests, stronger baselines, or online evidence, it is difficult to determine whether the improvement is robust or practically important.

The long-history analysis is potentially useful, but the paper does not report subgroup sizes, confidence intervals, or absolute metrics. Consequently, the practical significance of the reported 7.9% gain is unclear.

#### Clarity

The paper is generally well organized and readable. The model equation and experimental narrative are concise. However, several aspects need clarification:

- The exact graph normalization used with gated messages is not specified.
- It is unclear whether the same gate is used in both propagation directions and whether the gate is applied before or after normalization.
- The construction of training, validation, and test graphs should be described more rigorously.
- The exact meaning of “session-aware” is misleading.
- The reported average improvement over LightGCN should be corrected or explained. From the table, the average R@20 is approximately 0.08337 for LightGCN and 0.08743 for SeqGate, corresponding to about a **4.88% relative improvement**, not 4.6%.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 52/100 |
| Novelty | 40/100 |
| Significance | 47/100 |
| Clarity | 74/100 |

### Final average

\[
\frac{52 + 40 + 47 + 74}{4} = 53.25
\]

**Final score: 53.25/100**

## Recommendation: Reject

The paper presents a clear and plausible lightweight method, but the contribution is currently too incremental and the empirical evaluation does not provide enough evidence to support acceptance. A substantially stronger revision would need fairer baseline tuning, complete reproducibility details, statistical significance testing, comparisons with more relevant temporal graph methods, clearer temporal-protocol specification, and a more accurate characterization of the method as recency-aware rather than session-aware.