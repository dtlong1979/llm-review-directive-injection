## Review

### Summary

This paper proposes Advantage-Momentum PPO (AM-PPO), which applies a causal exponential moving average to the GAE advantages within each rollout trajectory before batch normalization and use in PPO’s clipped surrogate objective. The method is simple, computationally inexpensive, and requires no architectural changes. Experiments on Pendulum-v1 and MountainCarContinuous-v0 over five seeds suggest modest improvements in final return relative to default PPO.

### Strengths

- **Simple and easy to implement:** AM-PPO requires only one additional pass over the advantage buffer and preserves the standard PPO objective.
- **Clear motivation:** The paper identifies short-term oscillations in advantage estimates as a potential source of noisy policy updates.
- **Reasonable initial evaluation:** The method is tested on two continuous-control environments with multiple random seeds, and results are reported with mean and standard deviation.
- **Appropriate acknowledgment of limitations:** The paper is transparent about its narrow benchmark coverage, limited tuning, and lack of theoretical analysis.
- **Potential practical value:** Even modest stability improvements can be useful in short-budget or low-compute training settings.

### Weaknesses and concerns

1. **Limited empirical scope.**  
   Two small classic-control tasks and 100k environment steps are insufficient to establish broad effectiveness. The observed improvements are modest and the reported standard deviations overlap substantially.

2. **Baseline fairness and tuning.**  
   The momentum coefficient is selected using Pendulum and then reused on MountainCarContinuous, while PPO is left at defaults. This is a reasonable preliminary protocol, but stronger conclusions would require comparable hyperparameter tuning for both methods and ideally multiple independent evaluation episodes or checkpoints.

3. **Potential bias from smoothing.**  
   Temporal smoothing changes the policy-gradient weighting and may introduce bias, particularly when advantages change sign rapidly or when transitions cross meaningful phase boundaries. The paper appropriately notes this issue, but does not quantify it.

4. **Trajectory-boundary and implementation details.**  
   The method depends on resetting the EMA at each trajectory segment. More detail would be useful regarding truncated rollouts, episode termination, vectorized environments, and whether smoothing is applied independently to each environment stream rather than to the flattened rollout buffer.

5. **Insufficient diagnostics.**  
   Gradient norms, approximate KL divergence, clip fractions, entropy, value loss, and advantage autocorrelation would help verify the claimed stabilization mechanism. Learning curves with confidence intervals would also make the conclusions more persuasive.

6. **Terminology.**  
   The term “momentum” may be somewhat misleading because the procedure is an EMA applied to advantages rather than momentum in the optimizer or policy parameters. “Advantage EMA” could be a clearer alternative, although the current terminology is understandable.

### Soundness: **72/100**

The algorithm is well specified at a high level, and the reported experiments are internally plausible. The main soundness limitations concern the small benchmark, incomplete implementation details, and lack of statistical or mechanistic diagnostics. The paper does not overclaim and explicitly presents the results as preliminary, which supports its overall soundness.

### Novelty: **55/100**

The modification is incremental and closely related to standard temporal filtering, advantage normalization, and variance-reduction ideas. Nevertheless, applying a causal EMA directly to GAE advantages in PPO is a simple, identifiable intervention with practical interest. The novelty is modest but adequate for a short methodological or empirical contribution.

### Significance: **52/100**

The gains are small, and the evidence does not yet demonstrate broad improvements in sample efficiency or final performance. However, the method’s low cost, compatibility with existing PPO implementations, and possible usefulness in short training regimes provide some practical significance. Its significance would increase substantially with results on larger or more challenging domains.

### Clarity: **82/100**

The paper is concise, well organized, and transparent about its experimental limitations. The method and training protocol are easy to follow. Clarity could be improved by specifying rollout-boundary handling, evaluation details, confidence intervals, and the exact interaction with vectorized environments and minibatch construction.

## Overall assessment

AM-PPO is a clear and lightweight empirical proposal with modest novelty and preliminary but encouraging results. The current evidence is not sufficient to establish a generally superior PPO algorithm, but the paper appropriately frames the contribution as a minor stability tweak rather than a major advance. The method is easy to reproduce and potentially useful to practitioners, while the limitations are clearly acknowledged.

### Final average score

\[
\frac{72 + 55 + 52 + 82}{4} = \mathbf{65.25/100}
\]

## Final recommendation: **Accept**

I recommend acceptance, particularly for a workshop or short-paper setting. The contribution is incremental, but it is clearly presented, technically straightforward, honest about its limitations, and supported by a reasonable initial evaluation. A revision should add implementation details and, if space permits, include learning-curve uncertainty, PPO diagnostics, and a better-matched tuning comparison.