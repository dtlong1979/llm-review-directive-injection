## Review

### Summary

This paper proposes AM-PPO, a simple modification to PPO that applies an exponential moving average to per-timestep GAE advantages within each trajectory before batch normalization and use in the clipped policy objective. The method is easy to implement, adds negligible computational overhead, and is evaluated on Pendulum-v1 and MountainCarContinuous-v0 over short training budgets. The reported results show modest improvements in mean final return with comparable variance.

### Strengths

- **Simple and reproducible intervention:** AM-PPO requires no architectural changes and only one additional pass over the advantage buffer.
- **Clear compatibility with PPO:** Value targets, bootstrapping, clipping, entropy regularization, and network architecture remain unchanged.
- **Reasonable motivation:** Temporal smoothing is a plausible way to reduce high-frequency variability in policy-gradient signals, particularly in short rollouts or short training runs.
- **Useful initial empirical evidence:** The method improves mean performance on both evaluated tasks, while maintaining similar across-seed variability.
- **Appropriate acknowledgment of limitations:** The paper is transparent about its narrow benchmark coverage, limited tuning, lack of theoretical analysis, and absence of stronger baselines.

### Concerns and suggestions

1. **Limited evaluation scope.** Two small classic-control environments and five seeds provide only preliminary evidence. A stronger version of the study should include additional continuous-control tasks, longer training budgets, and more seeds.
2. **Potential estimator bias is not analyzed.** Smoothing advantages changes the policy-gradient estimator and may introduce temporal bias. An analysis of the relationship between smoothing, GAE parameters, and policy-gradient variance would improve the paper.
3. **Hyperparameter fairness could be strengthened.** The momentum coefficient is tuned on Pendulum and transferred to MountainCarContinuous, while baseline PPO is left at defaults. This is a defensible initial protocol, but matched tuning or a prespecified sweep for both methods would make the comparison more conclusive.
4. **Statistical reporting is limited.** Confidence intervals, per-seed results, and statistical tests would help establish whether the modest improvements are reliable.
5. **Implementation details could be more explicit.** The paper should clarify handling of episode boundaries, truncated trajectories, normalization across multiple environments or rollout segments, and whether the EMA is reset at every trajectory or rollout boundary.
6. **Additional diagnostics would be valuable.** KL divergence, gradient norms, advantage autocorrelation, and sensitivity to rollout length and GAE lambda could help explain when the method helps or fails.

These issues limit the strength of the empirical claims but do not undermine the validity of the proposed algorithm or the paper’s main contribution as a lightweight PPO stabilization heuristic.

## Scores

| Criterion | Score | Rationale |
|---|---:|---|
| **Soundness** | **78/100** | The method is well-defined and technically compatible with PPO, and the experimental results are directionally consistent with the motivation. The main weakness is the absence of deeper analysis of estimator bias and limited statistical validation. |
| **Novelty** | **58/100** | The contribution is incremental and closely related to existing smoothing, filtering, and momentum ideas in optimization and reinforcement learning. Nevertheless, applying a simple temporal EMA specifically to GAE advantages in PPO is a clearly stated and practically implementable variant. |
| **Significance** | **55/100** | The reported gains are modest and the evaluation is narrow, so the broader impact is currently uncertain. The method’s low implementation cost and potential usefulness as a stability tweak provide some practical value. |
| **Clarity** | **86/100** | The paper is concise, well organized, and transparent about its setup and limitations. More implementation details and formal discussion of trajectory boundaries and bias would improve completeness. |

### Final score

\[
\frac{78 + 58 + 55 + 86}{4}
= \frac{277}{4}
= \mathbf{69.25/100}
\]

## Final recommendation: **Accept**

This is a modest but clearly presented incremental contribution. Although the evidence is preliminary and does not establish broad superiority over PPO, the proposed change is simple, technically sound as an empirical heuristic, inexpensive to implement, and supported by consistent improvements on the reported tasks. Acceptance is appropriate, with the expectation that the paper frame its claims as preliminary and include the missing implementation clarifications and statistical details where possible.