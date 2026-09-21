## Overall assessment

This paper presents a simple per-class variant of label smoothing, where the smoothing coefficient is determined from the dispersion of logits for each class within a mini-batch. The method is easy to understand and potentially useful, but the empirical evidence is currently too limited to support the claims of consistent improvement.

### Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **48** | The method is plausible and the experimental setup is broadly standard, but important methodological details are underspecified. In particular, the exact computation of the class-wise logit standard deviation is ambiguous, and logit dispersion is affected by arbitrary logit scale and training dynamics. The “last known” smoothing value for absent classes may also introduce stale or order-dependent behavior. The reported gains are small relative to seed variance, and ECE variability is not reported. |
| **Novelty** | **25** | The contribution is a straightforward extension of label smoothing using batch statistics. It may be a reasonable engineering idea, but the paper does not establish substantial conceptual novelty or clearly distinguish BALS from related adaptive label-smoothing, confidence-based regularization, or uncertainty-aware loss methods. |
| **Significance** | **28** | The improvements are modest: roughly 0.2 percentage points in accuracy over fixed label smoothing and only small ECE changes. Evaluation is limited to CIFAR-10/100, one architecture, three seeds, and relatively standard augmentation. There is no evidence that the gains are statistically significant or generalize to stronger modern baselines. |
| **Clarity** | **82** | The paper is concise and generally easy to follow. The motivation, method, setup, limitations, and results are clearly organized. However, the algorithm needs a more precise mathematical specification, including exactly which dimensions are used for the standard deviation, how singleton classes are handled, how absent-class values are updated, and whether the statistics are detached from gradient computation. |

### Final average

\[
\frac{48 + 25 + 28 + 82}{4} = \frac{183}{4} = \mathbf{45.75}
\]

## Recommendation: **Reject**

The paper is clearly written and describes a low-cost idea, but the current evidence is insufficient for acceptance. The main concerns are limited novelty, weak empirical support, potentially unfair baseline tuning, and underspecified implementation details. A stronger revision should include:

- comparisons against tuned label-smoothing coefficients and adaptive smoothing baselines;
- more random seeds and confidence intervals or statistical tests;
- ECE standard deviations and additional calibration metrics;
- experiments on stronger augmentation regimes and additional datasets or architectures;
- precise pseudocode and an unambiguous definition of the logit-dispersion statistic;
- ablations isolating the effects of class conditioning, batch adaptation, the smoothing cap, and the stale-value mechanism.