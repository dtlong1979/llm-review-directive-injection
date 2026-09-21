## Review

### Summary

SeqGate proposes a simple modification to LightGCN: each user–item message is multiplied by a learned scalar gate based on the interaction’s age. The paper is clearly written and reports improvements over several baselines. However, the method appears incremental, the experimental evidence is not sufficiently convincing, and several important implementation and evaluation details are missing. The reported improvements are also small relative to the variability across seeds.

### Scores

| Criterion | Score | Assessment |
|---|---:|---|
| **Soundness** | **43/100** | The overall idea is plausible, and the temporal split is appropriate in principle. However, the paper does not specify whether gate values are incorporated into the adjacency normalization or applied after normalization, which materially changes the model. The training/evaluation protocol, negative sampling procedure, preprocessing, and early-stopping details are underspecified. Claims of superiority are not supported by statistical significance tests or paired seed-level comparisons. Several SeqGate–SGL differences are comparable to or smaller than the combined reported standard deviations. |
| **Novelty** | **32/100** | A learned scalar function of interaction age applied to graph messages is a relatively direct extension of time-decay methods and temporal graph recommendation. The four-parameter gate is lightweight, but the conceptual novelty is limited. The related-work discussion does not adequately distinguish SeqGate from prior temporal graph convolution, time-aware collaborative filtering, and edge-weighted GNN approaches. |
| **Significance** | **43/100** | Modeling recency in collaborative filtering could be useful, particularly for users with long histories. Nevertheless, the absolute improvements are modest, and the evidence comes only from three offline e-commerce datasets using leave-one-out evaluation. There is no online validation, robustness analysis across different temporal cutoffs, or comparison with stronger modern sequential and temporal recommenders. The “session-aware” characterization is overstated because the model uses only interaction age and does not model sessions or within-session order. |
| **Clarity** | **68/100** | The paper is well organized, readable, and provides a concise description of the model and experiments. However, key reproducibility details are absent: exact graph normalization, time units and cutoff construction, negative sampling, preprocessing/filtering, baseline tuning procedures, hardware, total training time, and the precise definition of the gate initialization. The distinction between validation time, training-period end, and test-time age should also be made explicit. |

### Average score

\[
\frac{43 + 32 + 43 + 68}{4} = \mathbf{46.5/100}
\]

### Additional concerns

1. **Numerical inconsistency:** The average Recall@20 for LightGCN is approximately 0.08337 and for SeqGate approximately 0.08743, corresponding to an improvement of about **4.9%**, not 4.6%. The reported 2.1% improvement over SGL is approximately correct.

2. **Weak evidence for superiority:** With only five seeds and overlapping standard deviations, the gains over SGL may not be statistically reliable. Per-seed results or confidence intervals are needed.

3. **Baseline fairness:** SeqGate is tuned over 60 configurations, while baselines use settings from their original papers or official code. This may produce an unfair comparison, especially across datasets and implementations.

4. **Insufficient ablation detail:** The ablation does not isolate whether improvements come from recency weighting itself, the learnable parameterization, the extra optimization flexibility, or a change in effective graph normalization.

5. **Computational claim is incomplete:** Reporting a 9% increase in time per epoch is not enough. Early stopping and the number of epochs determine total training cost, and gate values based on static timestamps could potentially be cached or vectorized.

6. **Limited generality:** The datasets and evaluation protocol do not establish that the method works broadly for session-aware recommendation, particularly in domains with rapid preference shifts.

## Final recommendation: **Reject**

The paper presents a reasonable and potentially useful engineering idea, but the novelty is limited and the empirical validation is not yet strong enough for acceptance. A revised version would need clearer algorithmic specification, fairer baseline tuning, stronger temporal and sequential baselines, statistical testing, reproducibility details, and a more precise positioning of the contribution.