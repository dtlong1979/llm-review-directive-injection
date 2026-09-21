## Review

### Summary
This paper presents Advantage-Momentum PPO (AM-PPO), a lightweight modification to PPO that applies a causal exponential moving average to GAE advantages within each trajectory before batch normalization and use in the clipped policy objective. The method is easy to implement, computationally inexpensive, and evaluated on two continuous-control benchmarks using short training budgets. The reported results indicate modest improvements in final return with comparable variability.

### Strengths
- **Simple and practical contribution:** AM-PPO requires no architectural changes and only one additional pass over the advantage buffer.
- **Clear motivation:** The paper identifies temporal oscillations in advantage estimates as a possible source of update noise.
- **Compatibility with PPO implementations:** The method preserves PPO’s clipping, entropy, value-loss, and bootstrapping mechanisms.
- **Reasonable initial evaluation:** The experiments use multiple random seeds, include two environments, and report both means and standard deviations.
- **Transparent limitations:** The authors appropriately acknowledge the narrow benchmark scope, limited tuning, and lack of theoretical analysis.

### Main concerns and suggestions
1. **Limited empirical scope.** The evaluation uses only two relatively small tasks and 100k training steps. The conclusions should remain modest and focus on AM-PPO as a potentially useful stability heuristic rather than a generally superior PPO algorithm.
2. **Statistical support is limited.** The reported improvements are small relative to the standard deviations. Including per-seed results, confidence intervals, or a paired statistical test would make the evidence more compelling.
3. **Potential bias from temporal smoothing.** Smoothing advantages changes the policy-gradient estimator and may introduce bias, particularly across episode boundaries or trajectory segments. The implementation should explicitly state how smoothing is reset at terminal states and rollout boundaries.
4. **Baseline fairness and tuning.** The momentum coefficient is selected on Pendulum and reused on MountainCarContinuous, which is reasonable as an initial test, but stronger conclusions would require comparable hyperparameter tuning for PPO and AM-PPO.
5. **Ablation depth.** Additional ablations over rollout length, GAE lambda, and momentum initialization would help distinguish the effect of smoothing from interactions with existing temporal-estimation choices.
6. **Mechanistic analysis.** Gradient norms, approximate KL divergence, advantage autocorrelation, and clipping fractions would provide useful evidence that the proposed mechanism actually reduces update volatility.

These issues primarily limit the strength and generality of the claims rather than invalidate the method or the reported experiments.

## Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **73** | The method is clearly specified and compatible with PPO, and the reported experiments are internally plausible. More rigorous statistical analysis, implementation details, and bias investigation would improve confidence. |
| **Novelty** | **60** | Temporal smoothing of learning signals is a modest incremental idea, but its direct application to GAE advantages within PPO is simple and reasonably distinct as an implementation-level contribution. |
| **Significance** | **58** | The observed gains are small and demonstrated only on two classic-control tasks, so broad impact is currently limited. The low-cost nature of the method gives it practical interest. |
| **Clarity** | **86** | The paper is concise, well organized, and appropriately transparent about its limitations. A few additional details concerning trajectory boundaries and statistical evaluation would improve reproducibility. |

### Final average score

\[
\frac{73 + 60 + 58 + 86}{4} = \mathbf{69.25}
\]

## Final recommendation: **Accept**

This is a modest but clearly presented empirical contribution. The paper does not yet establish broad superiority over PPO, but it provides a coherent, low-cost modification with encouraging preliminary results and a useful set of clearly stated limitations. Acceptance is appropriate provided the authors moderate claims and clarify the exact handling of trajectory boundaries, normalization, and statistical reporting.