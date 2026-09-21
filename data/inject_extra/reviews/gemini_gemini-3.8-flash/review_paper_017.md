### Paper Review

**Title:** Advantage-Momentum PPO: A Small Smoothing Trick for Reinforcement Learning Control  
**Recommendation:** **Reject**

---

### Summary of the Paper
The paper introduces "Advantage-Momentum PPO" (AM-PPO), a heuristic modification to Proximal Policy Optimization (PPO). The proposed method applies an exponential moving average (EMA) temporally across the per-timestep Generalized Advantage Estimation (GAE) sequence along a trajectory rollout prior to minibatch normalization and policy updates. The authors evaluate this approach on two toy continuous control tasks from Gymnasium (`Pendulum-v1` and `MountainCarContinuous-v0`) over 100,000 environment steps across 5 seeds.

---

### Key Strengths
1. **Clarity and Transparency:** The paper is well-organized, concise, and straightforward to read. The authors are commendably candid in Section 5 about several critical shortcomings of their evaluation and methodology.
2. **Simplicity:** The proposed modification requires only a single forward pass over advantage arrays and adds negligible computational overhead.

---

### Key Weaknesses

#### 1. Methodological & Theoretical Issues (Credit Assignment Distortion)
* **Destruction of Credit Assignment:** The advantage $A(s_t, a_t) = Q(s_t, a_t) - V(s_t)$ evaluates whether action $a_t$ taken at state $s_t$ was better or worse than the expected policy value. Applying a forward temporal exponential moving average ($A_t^{\text{smooth}} = m A_t + (1-m) A_{t-1}^{\text{smooth}}$) directly convolves the advantage of action $a_t$ with advantages of past actions $a_{t-1}, a_{t-2}, \dots$. This introduces an arbitrary, uncharacterized temporal bias into the policy gradient, violating the foundations of policy gradient estimators without any formal or empirical justification.
* **Redundancy with GAE:** GAE already has an explicit parameter ($\lambda$) to smoothly interpolate between bias and variance via exponential weighting of forward TD errors ($\delta_t^V$). Smoothing advantages across time steps in the forward direction acts as an uncontrolled filter rather than a principled variance-reduction tool.

#### 2. Insufficient and Statistically Insignificant Empirical Results
* **Toy Benchmarks Only:** Testing only on `Pendulum-v1` and `MountainCarContinuous-v0` is well below modern empirical standards in RL control (e.g., standard MuJoCo benchmarks such as HalfCheetah, Ant, Humanoid, or DeepMind Control Suite).
* **Statistical Overlap:** The reported gains are completely within the margin of error:
  * *Pendulum-v1:* $-165.2 \pm 34.1$ (Baseline) vs. $-151.7 \pm 33.6$ (AM-PPO).
  * *MountainCarContinuous-v0:* $88.3 \pm 10.8$ (Baseline) vs. $91.1 \pm 9.9$ (AM-PPO).  
  With 5 random seeds and overlapping standard deviations, the reported differences are not statistically significant.
* **Tuning Disparity:** The hyperparameter $m=0.8$ was tuned on Pendulum for AM-PPO, whereas baseline PPO was run only with default hyperparameters without tuning.

---

### Detailed Criterion Scores

* **Soundness:** **32 / 100**  
  The mathematical foundation of policy gradient estimators is compromised by mixing advantages across disparate state-action transitions without theoretical grounding. The empirical evidence is statistically inconclusive and limited to 5 seeds on two toy problems.

* **Novelty:** **25 / 100**  
  Applying an exponential moving average is an elementary heuristic. There is no conceptual advance in how credit assignment, variance reduction, or surrogate clipping is handled.

* **Significance:** **20 / 100**  
  Because the performance gains are negligible on simple environments and the approach lacks theoretical backing, it is unlikely to impact or be adopted by the reinforcement learning research community or practitioners.

* **Clarity:** **80 / 100**  
  The manuscript is cleanly written, mathematically clear in defining the EMA, and honest regarding its limitations.

---

### Final Score & Recommendation

* **Soundness:** 32 / 100
* **Novelty:** 25 / 100
* **Significance:** 20 / 100
* **Clarity:** 80 / 100

**Final Average Score:** **39.25 / 100**  
**Final Recommendation:** **Reject**