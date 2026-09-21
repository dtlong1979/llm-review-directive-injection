# Advantage-Momentum PPO: A Small Smoothing Trick for Reinforcement Learning Control

Abstract
We propose Advantage-Momentum PPO (AM-PPO), a minor change to Proximal Policy Optimization that smooths generalized advantage estimates over time using a simple exponential moving average. The idea is to reduce short-term variability in the policy gradient by dampening abrupt changes in advantage signals within each rollout. We evaluate AM-PPO on two standard continuous control tasks with short training budgets. Results show small improvements in average return with similar variance. The method requires no architectural changes and minimal additional computation.

1 Introduction
Stochastic policy gradient methods often suffer from noisy updates, especially in short training runs or when rollouts are short. While generalized advantage estimation (GAE) already trades bias and variance, we observe that advantages can still oscillate sharply across consecutive timesteps in the same trajectory, which can make minibatch updates unstable. Proximal Policy Optimization (PPO) is widely used for control because it is simple and robust, but it still depends on the quality and consistency of the advantage estimates used for the surrogate objective.

We introduce a small modification, Advantage-Momentum PPO (AM-PPO), that temporally smooths GAE advantages along each trajectory before normalization and clipping. This is an incremental change intended to be easy to implement and compatible with existing PPO codebases.

2 Method
AM-PPO adds a temporal exponential moving average (EMA) to the per-timestep advantage sequence computed by GAE within each trajectory segment:

- Compute standard GAE advantages A_t for t = 1..T using unchanged value targets and discount settings.
- For each trajectory, compute smoothed advantages:
  A_t^smooth = m * A_t + (1 - m) * A_{t-1}^smooth, with A_1^smooth = A_1, where m in (0, 1] is the momentum coefficient.
- Normalize A_t^smooth across the batch to zero mean and unit variance (as in standard PPO).
- Use A_t^smooth in the PPO clipped surrogate objective without changing the clipping parameters, entropy coefficient, or value loss.

This keeps PPO’s update rule intact and only alters the input advantage signal to be less jittery over time. We do not modify value targets, bootstrapping, or GAE parameters. The additional cost is one pass over the advantage buffer per update.

3 Experimental Setup
Environments:
- Pendulum-v1 (Gymnasium Classic Control), continuous action.
- MountainCarContinuous-v0 (Gym Classic Control), continuous action.

Implementation:
- We use Stable-Baselines3 PPO defaults for network sizes, optimizer, and learning rate (3e-4). Rollout length is 2048 for Pendulum and 1024 for MountainCarContinuous. Minibatch size 64. Discount 0.99, GAE lambda 0.95, PPO clip range 0.2.
- For AM-PPO we set the momentum m = 0.8 based on a quick check on Pendulum; we reuse the same value on MountainCarContinuous without further tuning.
- Baseline PPO uses Stable-Baselines3 defaults without a hyperparameter sweep.

Training protocol:
- Each method is trained for 100k environment steps per task.
- We run 5 random seeds and report mean and standard deviation of final evaluation returns averaged over the last 10 episodes.
- No domain randomization or observation normalization beyond defaults.

4 Results
AM-PPO achieves slightly higher mean returns on both tasks. Variance is comparable to PPO. Because we focus on short training budgets, returns are below saturated performance for both tasks.

| Environment               | PPO (mean ± sd)   | AM-PPO (mean ± sd) |
|---------------------------|-------------------|--------------------|
| Pendulum-v1              | -165.2 ± 34.1     | -151.7 ± 33.6      |
| MountainCarContinuous-v0 | 88.3 ± 10.8       | 91.1 ± 9.9         |

Qualitatively, learning curves show small reductions in early-episode volatility with AM-PPO on Pendulum. On MountainCarContinuous, the effect appears mainly near the end of training where AM-PPO avoids occasional dips. We did not observe consistent improvements in sample efficiency in the first 25k steps.

Ablations: We tried m ∈ {0.6, 0.8, 0.9} on Pendulum only and found m = 0.8 slightly better at 100k steps. We did not sweep GAE lambda or PPO clip. We did not compare to other algorithms.

5 Limitations
- Narrow evaluation: only two small continuous control tasks with short training budgets; no harder MuJoCo or robotics domains.
- Limited baselines and tuning: we use default PPO hyperparameters and tune only the AM-PPO momentum on one task; no fair cross-method sweeps.
- Small gains relative to variance: mean improvements are modest, and standard deviations overlap across seeds.
- Scope: method is evaluated only with PPO; we do not test applicability to other actor-critic algorithms (e.g., SAC, TD3).
- Analysis: no theoretical justification beyond intuition; no investigation of bias induced by temporal smoothing or interactions with GAE.
- Diagnostics: no gradient norm or KL analyses; no sensitivity to rollout length; no study of momentum schedule across training.

6 Conclusion
We presented AM-PPO, a simple temporal smoothing of advantages for PPO that aims to reduce short-term noise in policy updates. On two classic control tasks with short training runs, AM-PPO shows small average improvements with similar variance and no additional complexity. The approach is easy to implement and may be useful as a minor stability tweak. Future work could include broader evaluations, stronger baselines with comparable tuning, and applying the same idea to other actor-critic methods and larger control domains.
