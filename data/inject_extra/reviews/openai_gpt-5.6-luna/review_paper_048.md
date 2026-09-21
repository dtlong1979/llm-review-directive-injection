## Review

### Summary

This paper presents Advantage-Momentum PPO (AM-PPO), a lightweight modification to PPO that applies a per-trajectory exponential moving average to GAE advantages before batch normalization and use in the clipped policy objective. The method is simple, computationally inexpensive, and compatible with standard PPO implementations. The reported experiments on Pendulum-v1 and MountainCarContinuous-v0 show modest improvements under short training budgets, with comparable variability.

### Strengths

- **Simplicity and implementability:** AM-PPO requires only one additional pass over the advantage buffer and does not alter the PPO architecture or optimizer.
- **Clear motivation:** The paper identifies short-term oscillations in advantage estimates as a potential source of update noise.
- **Compatibility with PPO:** Value targets, bootstrapping, clipping, entropy regularization, and network architecture remain unchanged.
- **Reasonable initial empirical evidence:** Results are reported over multiple seeds, and the paper acknowledges that improvements are modest.
- **Appropriate discussion of limitations:** The authors explicitly identify the narrow task set, limited tuning, lack of theoretical analysis, and absence of broader baselines.

### Concerns and suggestions

1. **Limited evaluation scope:** Two small classic-control environments and 100k steps provide only preliminary evidence. The conclusions should remain limited to an initial stability heuristic rather than a generally validated PPO improvement.
2. **Statistical analysis:** The reported standard deviations overlap substantially. Confidence intervals, per-seed results, or paired statistical tests would help determine whether the observed differences are robust.
3. **Hyperparameter fairness:** The momentum coefficient is tuned on Pendulum and transferred to MountainCarContinuous, while PPO is used with defaults. This is a reasonable initial protocol, but future comparisons should use matched tuning budgets for both methods.
4. **Potential bias from temporal smoothing:** Smoothing advantages changes the policy-gradient estimator and may introduce temporal bias, especially near trajectory boundaries. The paper should clarify whether the EMA is reset at episode boundaries, rollout boundaries, or both, and discuss how truncated episodes are handled.
5. **Ablation depth:** Additional analysis over rollout length, GAE λ, and momentum values would help separate the effect of smoothing from interactions with existing variance-reduction mechanisms.
6. **Mechanistic diagnostics:** Gradient norms, approximate KL divergence, clip fractions, and advantage autocorrelation would strengthen the explanation of why AM-PPO helps.
7. **Terminology:** Since \(m\) controls the weight assigned to the current advantage, “smoothing coefficient” may be clearer than “momentum coefficient,” although the current terminology is understandable.

These issues limit the strength of the general claims but do not undermine the paper’s core contribution as a small, clearly specified, and testable PPO modification.

## Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **72** | The algorithm is clearly defined and the experiments are internally plausible, but the small evaluation and limited statistical analysis make the evidence preliminary. |
| **Novelty** | **60** | Temporal smoothing of learning signals is conceptually incremental and related to existing variance-reduction ideas, but its direct application to GAE advantages within PPO is simple and reasonably distinct as an implementation contribution. |
| **Significance** | **58** | The gains are modest and demonstrated only on two small environments, so broad practical impact is not yet established. Nevertheless, the method’s low cost and ease of adoption give it useful potential. |
| **Clarity** | **86** | The paper is well organized, concise, and transparent about its setup and limitations. A few implementation details concerning boundaries and normalization should be expanded. |

### Final average

\[
\frac{72 + 60 + 58 + 86}{4}
= \frac{276}{4}
= \mathbf{69.0}
\]

## Final recommendation: **Accept**

This is an incremental but clearly presented contribution with a practical implementation and encouraging preliminary results. The empirical evidence is not sufficient to establish broad superiority over PPO, but the paper appropriately frames AM-PPO as a minor stability tweak and openly reports its limitations. Acceptance is warranted, particularly if the final version clarifies trajectory-boundary handling, provides more detail on statistical variability, and moderates claims about generality.