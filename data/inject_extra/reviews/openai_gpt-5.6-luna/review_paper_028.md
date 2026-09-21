## Review

### Summary
The paper proposes a simple modification to PPO: applying an exponential moving average to GAE advantages within each trajectory before batch normalization and optimization. The method is easy to implement and computationally inexpensive. However, the empirical evaluation is too limited to establish that the method is reliable or meaningfully improves PPO, and the paper does not sufficiently analyze the bias introduced by altering the advantage estimator.

### Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **45** | The method is clearly specified at a high level and the experiments are directionally appropriate, but temporal smoothing changes the policy-gradient estimator and may introduce bias. This issue is not theoretically analyzed or empirically isolated. The evaluation uses only five seeds, short training runs, and two small environments. Important implementation details—such as handling multiple episode boundaries within a rollout—are not fully specified. |
| **Novelty** | **25** | The modification is straightforward and closely related to existing forms of return/advantage filtering, eligibility traces, and temporal smoothing. The paper does not position AM-PPO carefully against these ideas or establish a strong conceptual novelty beyond applying an EMA to advantages. |
| **Significance** | **25** | The reported gains are modest and have overlapping standard deviations. There is no evidence of consistent sample-efficiency improvement, robustness across tasks, or benefits over tuned PPO and related baselines. The contribution may be useful as an engineering heuristic, but its broader impact is currently unclear. |
| **Clarity** | **82** | The paper is concise and generally easy to follow. The algorithm and experimental setup are understandable. Clarity would improve with pseudocode, precise handling of trajectory/episode boundaries, per-seed results, confidence intervals, and a clearer discussion of the estimator’s bias. |

### Final average

\[
\frac{45 + 25 + 25 + 82}{4} = \mathbf{44.25}
\]

## Recommendation: **Reject**

The paper presents a simple and potentially useful heuristic, but the current evidence is insufficient for acceptance. The main concerns are the limited evaluation, lack of fair hyperparameter tuning, absence of stronger baselines, no statistical significance analysis, and insufficient treatment of the bias and theoretical implications of smoothing advantages.

A stronger revision should include:

- Comparisons against carefully tuned PPO and other advantage/return smoothing methods.
- More environments and substantially longer training horizons.
- More random seeds with confidence intervals or statistical tests.
- Explicit analysis of bias, gradient behavior, KL divergence, and value-function interactions.
- Ablations over momentum, rollout length, GAE \(\lambda\), and episode-boundary handling.
- Per-seed learning curves and reproducible implementation details.