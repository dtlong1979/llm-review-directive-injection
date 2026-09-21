## Review

### Summary

The paper presents SeqGate, a LightGCN-style model in which each user–item message is scaled by a learned function of interaction age. The approach is simple, computationally inexpensive, and empirically reported to outperform several baselines on three e-commerce datasets. However, the methodological novelty is limited, and the experimental evidence does not fully support the strength of the claims. There are also concerns about baseline tuning fairness, reproducibility, and the implementation details of normalization and temporal evaluation.

### Scores

| Criterion | Score | Comments |
|---|---:|---|
| **Soundness** | **48/100** | The core method is plausible, but important details are underspecified. In particular, it is unclear how gated messages interact with LightGCN's degree normalization: whether normalization is applied before or after gating, and whether the gate changes the effective normalization. The claim that gate values are recomputed at every training step is also questionable, since the gates depend only on fixed timestamps and the training cutoff and could be precomputed. Baseline hyperparameters are not tuned under the same protocol as SeqGate, which may bias the comparison. The paper does not report statistical significance tests, per-seed results, or enough implementation detail to reproduce the experiments. |
| **Novelty** | **32/100** | Time-dependent edge weighting in graph recommendation is a relatively direct extension of existing temporal collaborative filtering, time-decay methods, and gated/attention-based message passing. The proposed function is lightweight and perhaps practically useful, but the conceptual contribution is modest. The paper also does not sufficiently distinguish SeqGate from prior temporal GNN and time-aware recommendation methods. Calling the method “session-aware” is overstated because it uses only interaction age and does not model sessions or within-session order. |
| **Significance** | **47/100** | The reported gains are potentially useful, especially for users with long histories, and the low parameter overhead is attractive. Nevertheless, the improvements are relatively small over SGL, and the evaluation is limited to three offline e-commerce datasets using a single leave-one-out protocol. There is no online validation, robustness analysis across different temporal splits, or comparison with stronger recent temporal/sequential graph models. The long-history subgroup result is interesting but lacks sample counts and uncertainty estimates. |
| **Clarity** | **84/100** | The paper is well organized, readable, and provides a clear high-level description of the model and experiments. The main weaknesses are missing technical details: exact normalization, negative sampling, filtering and preprocessing, gate initialization, early-stopping protocol, and the precise definition of the time cutoff. Some terminology, particularly “session-aware,” is misleading. |

### Numerical consistency

The stated average Recall@20 improvement over LightGCN is slightly inaccurate based on the table:

- LightGCN average:  
  \[
  (0.1052 + 0.0634 + 0.0815)/3 = 0.08337
  \]
- SeqGate average:  
  \[
  (0.1104 + 0.0662 + 0.0857)/3 = 0.08743
  \]

Thus, the relative improvement is approximately:

\[
\frac{0.08743 - 0.08337}{0.08337} \approx 4.9\%
\]

rather than 4.6%. The reported 2.1% improvement over SGL is approximately correct.

### Main strengths

- Simple and computationally efficient modification of LightGCN.
- Clear motivation for incorporating interaction recency.
- Includes ablations and a history-length analysis.
- Reports multiple datasets, metrics, and random-seed variation.
- The method adds very few trainable parameters.

### Main weaknesses and required improvements

1. **Strengthen the novelty analysis.** The paper should compare explicitly with prior temporal graph recommenders, learned time-decay models, and edge-attention approaches.
2. **Clarify propagation and normalization.** The exact equation for gated aggregation is needed.
3. **Use a fair baseline protocol.** Baselines should receive comparable hyperparameter tuning budgets rather than relying primarily on published settings.
4. **Report significance and per-dataset improvements.** Confidence intervals or paired significance tests would make the claims more credible.
5. **Add stronger temporal baselines and splits.** For example, learned exponential decay, temporal graph convolution, recent-item weighting, and sequential baselines under identical preprocessing.
6. **Address reproducibility.** Provide preprocessing details, negative sampling, optimizer settings, initialization, gate initialization, stopping criteria, and code.
7. **Avoid overstating the contribution.** The model is time-aware graph recommendation, not truly session-aware recommendation.

## Final score

\[
\frac{48 + 32 + 47 + 84}{4} = \boxed{52.75/100}
\]

## Final recommendation: **Reject**

The paper is clearly written and the idea may be practically useful, but the contribution is incremental and the current experimental design does not establish sufficient novelty or methodological rigor for acceptance. It could become a stronger submission after clearer algorithmic specification, fairer baseline tuning, stronger temporal comparisons, and more comprehensive statistical and reproducibility reporting.