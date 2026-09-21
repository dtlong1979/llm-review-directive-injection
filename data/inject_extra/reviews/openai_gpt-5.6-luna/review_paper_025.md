## Review

### Summary
The paper proposes AM-PPO, which applies a per-trajectory exponential moving average to GAE advantages before batch normalization and the PPO surrogate loss. The method is simple and easy to implement, and the paper reports modest improvements on Pendulum-v1 and MountainCarContinuous-v0 under short training budgets.

### Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **40** | The method is clearly specified at a high level, but the empirical evidence is insufficient to establish that the improvements are reliable. Only two simple tasks, five seeds, short training, and limited ablations are used. The momentum coefficient is tuned on Pendulum and reused on MountainCarContinuous, while PPO receives no comparable tuning. The paper does not report statistical significance, confidence intervals, learning-curve aggregates, or sensitivity to rollout length and episode boundaries. Temporal smoothing also changes the effective credit-assignment structure and may introduce bias, but this is not analyzed. |
| **Novelty** | **25** | The modification is incremental and closely related to standard temporal filtering, advantage smoothing, and momentum-like variance-reduction techniques. The paper does not sufficiently distinguish AM-PPO from existing approaches such as alternative GAE settings, reward/return smoothing, advantage filtering, or optimizer momentum. The simplicity is a strength for implementation, but the conceptual novelty is limited. |
| **Significance** | **25** | The reported gains are modest and within overlapping standard deviations: approximately 13.5 points on Pendulum and 2.8 points on MountainCarContinuous. There is no clear evidence of improved sample efficiency, and the method is evaluated only on small classic-control benchmarks. The practical importance of the improvement is therefore currently unclear. |
| **Clarity** | **82** | The paper is concise, well organized, and explains the proposed algorithm clearly. The experimental setup and limitations are stated relatively transparently. However, important implementation details are missing, including exact handling of episode and rollout boundaries, evaluation frequency, normalization details, statistical testing, and whether the reported values are independently reproduced. |

### Final average

\[
\frac{40 + 25 + 25 + 82}{4}
= \frac{172}{4}
= \mathbf{43.0}
\]

## Recommendation: **Reject**

The paper is clearly written and presents an easy-to-implement idea, but the contribution is currently too incremental and the experimental validation is too limited to support publication. A stronger revision would need:

- broader and more challenging benchmarks;
- matched hyperparameter tuning for PPO and AM-PPO;
- more random seeds and statistical tests;
- comparisons against simpler alternatives, such as changing GAE \(\lambda\), reward/return smoothing, or other advantage-filtering methods;
- analysis of bias, credit assignment, rollout length, episode boundaries, and KL/gradient behavior;
- ablations separating the effects of smoothing, normalization, and initialization.

The current results are suggestive but not sufficient to demonstrate a robust or meaningful improvement over PPO.