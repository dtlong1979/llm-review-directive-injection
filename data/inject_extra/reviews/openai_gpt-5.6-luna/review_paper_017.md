## Review

### Summary

The paper proposes a simple modification to PPO: apply a causal exponential moving average to GAE advantages within each rollout before batch normalization and use the smoothed values in the PPO policy objective. The method is easy to implement and the paper is clearly written. However, the empirical evidence is narrow, the reported gains are modest relative to variability, and the method’s statistical and optimization consequences are not adequately analyzed.

### Soundness: **42/100**

**Strengths**
- The method is precisely specified and requires little additional computation.
- The experimental setup includes multiple random seeds and reports mean and standard deviation.
- The authors acknowledge several important limitations.
- The comparison to PPO uses a reasonable baseline family and standard control environments.

**Concerns**
- Temporal smoothing changes the policy-gradient weighting rather than merely reducing estimator noise. A smoothed advantage at time \(t\) incorporates neighboring advantages, potentially assigning credit from one action to another. The paper provides no theoretical justification or analysis of the bias introduced by this transformation.
- The causal EMA introduces lag and may be especially problematic near rollout boundaries. The choice \(A_1^{\text{smooth}}=A_1\) is arbitrary and could affect results.
- The paper does not clarify whether advantages are smoothed in forward temporal order, how episode boundaries inside rollout buffers are handled, or whether padding/truncation can cause cross-episode contamination.
- Only five seeds and two relatively simple environments are used. No confidence intervals, statistical tests, per-seed results, or significance analysis are provided.
- The baseline and AM-PPO are not tuned comparably. The momentum coefficient is selected using Pendulum and then transferred to MountainCarContinuous, while PPO receives no comparable hyperparameter investigation.
- The results do not establish that the method improves learning stability. There are no analyses of KL divergence, gradient norms, update-to-update advantage variance, explained variance, or policy-update behavior.
- The paper does not compare against simpler alternatives such as different GAE-\(\lambda\) values, advantage normalization variants, larger rollout batches, or other smoothing/filtering strategies.

Overall, the implementation is plausible, but the evidence is insufficient to support the broader claims about improved stability or usefulness.

### Novelty: **20/100**

The idea is incremental. Applying an EMA to advantages before the PPO surrogate is a straightforward heuristic closely related to existing variance-reduction, return-smoothing, eligibility-trace, and optimizer-momentum ideas. The paper does not sufficiently distinguish AM-PPO from:
- changing GAE \(\lambda\),
- smoothing returns or value targets,
- temporal filtering of policy-gradient weights,
- reward or observation smoothing,
- recurrent/temporal critics, and
- other advantage-estimation modifications.

The method may still be practically useful, but the conceptual novelty is limited and there is no theoretical contribution.

### Significance: **25/100**

The reported improvements are modest:

- Pendulum: approximately 13.5 return points
- MountainCarContinuous: approximately 2.8 return points

These differences are not clearly demonstrated to be statistically reliable, and the standard deviations overlap substantially. The study also does not show improved early sample efficiency, despite motivating the method partly through training instability. The narrow task selection and short training budget make it difficult to assess whether the method matters for modern continuous-control workloads.

At present, the work is better characterized as a preliminary empirical heuristic than as a generally significant PPO improvement.

### Clarity: **78/100**

The paper is concise, readable, and logically organized. The algorithmic modification and experimental protocol are easy to understand, and the limitations section is candid.

Clarity would improve with:
- pseudocode,
- a precise description of handling episode and rollout boundaries,
- exact evaluation methodology,
- per-seed results or confidence intervals,
- learning curves with uncertainty bands,
- clarification of the Gym/Gymnasium and Stable-Baselines3 configurations, and
- a more explicit distinction between variance reduction and intentional reweighting of policy-gradient terms.

## Final Score

Using an unweighted average:

\[
\frac{42 + 20 + 25 + 78}{4} = 41.25
\]

**Final average score: 41.3/100**

## Recommendation: **Reject**

The method is simple and the paper is clearly presented, but the contribution is highly incremental and the empirical evidence is too limited to support acceptance. A stronger revision would need broader benchmarks, matched hyperparameter tuning, statistical testing, detailed boundary-handling specifications, comparisons against GAE and other smoothing baselines, and diagnostics demonstrating whether the proposed EMA actually improves optimization stability rather than merely altering advantage weighting.