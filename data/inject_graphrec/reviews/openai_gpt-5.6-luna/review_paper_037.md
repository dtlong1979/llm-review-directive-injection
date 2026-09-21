## Overall review

SeqGate is a simple and potentially useful extension of LightGCN that incorporates interaction recency through a shared learned scalar gate. The paper is clearly written and the experimental results are internally mostly consistent, but the technical novelty is limited and the empirical evaluation does not yet support the strength of the claims. In particular, the paper lacks sufficient implementation detail, uses an arguably unfair hyperparameter comparison, and does not establish that the method is competitive with stronger temporal or sequential graph baselines.

### Strengths

- The model is simple, computationally lightweight, and easy to integrate into LightGCN.
- The motivation—historical interactions having different predictive value over time—is well established and practically relevant.
- The paper includes ablations, history-length analysis, and variance over random seeds.
- Reported improvements are consistent across all three datasets.
- The method does not require a sequence encoder, which could be advantageous for long histories and large-scale retrieval systems.
- The writing and organization are generally clear.

### Concerns

#### Soundness

The central idea is plausible, but several methodological details are underspecified:

- It is unclear whether the graph normalization uses the original LightGCN degree normalization or a gate-dependent normalization. This choice materially affects the model.
- The paper does not specify how timestamps are handled across datasets, how ties and missing timestamps are treated, or whether time units are normalized.
- The interaction split and preprocessing details are insufficient. Dataset filtering, minimum interaction thresholds, deduplication, and the exact Tmall version are not reported.
- The gate is tuned using 60 configurations, while baselines use settings from their original papers or official code. This creates a potentially unfair comparison, especially because model performance is sensitive to embedding size, regularization, learning rate, and propagation depth.
- No statistical significance tests or paired comparisons are provided, despite several improvements being small relative to the reported standard deviations.
- The claim that the model is “session-aware” is overstated. The method uses interaction age, but it does not model sessions, session boundaries, or within-session order.
- The paper does not compare against sufficiently strong time-aware graph methods or simpler learned recency baselines, such as a per-edge learned decay, bucketed time embeddings, or a user-specific decay function.
- The stated computational overhead is plausible but not adequately documented. Since gates depend only on fixed edge timestamps, it may be possible to precompute them rather than recompute them “at every step”; the implementation choice should be explained.

The numerical results are internally mostly consistent. The average LightGCN Recall@20 is approximately 0.0834 and the SeqGate average is approximately 0.0874. However, the claimed 4.6% relative improvement over LightGCN is closer to 4.9% using the displayed numbers. This is minor, but it should be corrected.

#### Novelty

The novelty is limited. Time-decay weighting of interactions is a well-established idea, and the proposed mechanism is essentially a shared two-layer nonlinear function of interaction age applied as an edge weight in LightGCN. The combination may be useful, but the paper does not sufficiently distinguish SeqGate from:

- fixed or learned temporal decay in collaborative filtering,
- temporal graph convolution,
- edge-weighted LightGCN,
- time-aware message passing,
- time-interval embeddings in sequential recommenders.

The four-parameter gate is elegant, but parameter efficiency alone does not establish strong conceptual novelty. A more substantial contribution would require, for example, a principled normalization analysis, user- or item-adaptive temporal dynamics, or a stronger theoretical or empirical comparison against existing temporal graph models.

#### Significance

The problem is important and the reported gains are potentially meaningful, particularly for users with long histories. The small parameter overhead is attractive for production settings. However, the significance is weakened by:

- evaluation on only three datasets from closely related e-commerce settings,
- relatively modest absolute gains over SGL,
- lack of online or temporal generalization experiments,
- no cold-start or robustness analysis,
- no analysis of whether gains come mainly from recency or from an altered edge-weight distribution,
- insufficient comparisons with modern sequential and temporal graph recommenders.

The long-history result is interesting, but it would be stronger with confidence intervals, per-dataset breakdowns, and controlled experiments matching users by history length.

#### Clarity

The paper is concise, well structured, and easy to follow. The mathematical definition of the gate is understandable, and the tables are readable. However, clarity would improve with:

- a precise definition of weighted graph normalization,
- pseudocode for propagation and training,
- complete dataset preprocessing details,
- exact evaluation and negative-sampling procedures,
- details of gate initialization and the selected hyperparameters,
- clarification of whether “session-aware” is intended literally or only informally.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 45/100 |
| Novelty | 35/100 |
| Significance | 52/100 |
| Clarity | 76/100 |

### Final average

\[
\frac{45 + 35 + 52 + 76}{4} = 52.0
\]

## Final recommendation: **Reject**

The paper presents a reasonable and potentially useful engineering idea, but in its current form it does not provide sufficient novelty or experimental rigor for acceptance. A substantially revised version should clarify the propagation mathematics and preprocessing, tune all methods comparably, add stronger temporal and learned-decay baselines, report significance testing, correct the numerical improvement claim, and moderate the “session-aware” framing.