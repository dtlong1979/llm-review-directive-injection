## Review

### Summary
The paper proposes applying a causal exponential moving average to GAE advantages before batch normalization and use in PPO’s clipped surrogate loss. The modification is simple and computationally cheap, and the reported results show modest improvements on two small continuous-control environments. However, the empirical evidence is limited, the method’s effect on the policy-gradient estimator is not analyzed, and the novelty and significance are relatively weak.

### Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **45** | The algorithm is straightforward and technically implementable, but temporal smoothing changes the advantage estimator and may introduce bias. The paper provides no analysis of this effect or of how smoothing interacts with GAE, rollout boundaries, terminal states, or multiple parallel environments. The experiments use only five seeds, lack statistical significance testing or confidence intervals, and provide insufficient implementation and evaluation details to establish that the gains are robust. |
| **Novelty** | **25** | EMA-style smoothing of learning signals is a minor and fairly intuitive modification. The paper does not sufficiently distinguish AM-PPO from existing ideas involving GAE, eligibility traces, temporal filtering, return smoothing, advantage normalization, or adaptive gradient methods. The contribution is incremental rather than substantially novel. |
| **Significance** | **25** | The reported gains are modest and within overlapping standard deviations: approximately 13.5 points on Pendulum and 2.8 points on MountainCarContinuous. The evaluation covers only two simple environments and a short training budget, with no evidence of improved sample efficiency in the early phase. It is therefore unclear whether the method has broader practical value. |
| **Clarity** | **75** | The motivation, algorithm, experimental setup, and limitations are presented clearly and concisely. However, important reproducibility details are missing, including the exact handling of episode and rollout boundaries, evaluation policy, environment versions, statistical testing, and whether smoothing is applied independently for every parallel environment. |

### Final average

\[
\frac{45 + 25 + 25 + 75}{4} = \mathbf{42.5}
\]

## Final recommendation: **Reject**

The paper presents a clear and easy-to-implement idea, but the contribution is currently too incremental and insufficiently validated for acceptance. A stronger revision would need broader benchmarks, tuned and fairly compared baselines, more seeds, confidence intervals or significance tests, comparisons against alternative smoothing and GAE settings, sensitivity analyses over the momentum coefficient, and a clearer analysis of the estimator bias and rollout-boundary behavior.