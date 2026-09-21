### Paper Review

---

### **Summary**
The paper proposes **Advantage-Momentum PPO (AM-PPO)**, a heuristic modification to Proximal Policy Optimization where per-timestep Generalized Advantage Estimation (GAE) outputs are temporally smoothed forward in time using a simple exponential moving average (EMA) along rollout trajectories. The method is evaluated on two toy continuous-control tasks (Pendulum-v1 and MountainCarContinuous-v0) over 100k steps and 5 random seeds.

---

### **Strengths**
1. **High Clarity and Transparency:** The paper is well-written, easy to follow, and exceptionally honest in Section 5 (Limitations) regarding the lack of theoretical justification, small gains, and narrow benchmark scope.
2. **Simplicity:** The proposed modification consists of just one simple line of math applied prior to batch normalization and introduces minimal computational overhead.

---

### **Weaknesses**

1. **Fundamental Conceptual / Theoretical Issues with Credit Assignment:**
   * In reinforcement learning, the advantage function $A^\pi(s_t, a_t) = Q^\pi(s_t, a_t) - V^\pi(s_t)$ explicitly measures how much better or worse a *specific action* $a_t$ is compared to the average action at *state* $s_t$.
   * Applying a causal forward EMA ($A_t^\text{smooth} = m A_t + (1 - m) A_{t-1}^\text{smooth}$) systematically bleeds the credit/blame of action $a_{t-1}$ into action $a_t$. This corrupts the policy gradient direction with arbitrary bias across non-identical state-action pairs.
   * GAE ($\lambda$-returns) already provides a principled, exponentially discounted temporal combination *backwards* from future rewards. Forward-filtering the resulting advantage estimates lacks foundational motivation.

2. **Statistically Insignificant Improvements:**
   * On **Pendulum-v1**, AM-PPO achieves $-151.7 \pm 33.6$ vs. PPO's $-165.2 \pm 34.1$.
   * On **MountainCarContinuous-v0**, AM-PPO achieves $91.1 \pm 9.9$ vs. PPO's $88.3 \pm 10.8$.
   * In both cases, the standard deviations heavily overlap, and with only $N=5$ seeds, the differences are well within standard error margins and cannot be considered statistically significant.

3. **Inadequate Empirical Scope:**
   * Evaluating exclusively on two classic control tasks (Pendulum and MountainCar) is far below modern reinforcement learning standards. Standard benchmarks require continuous control suites such as MuJoCo (HalfCheetah, Ant, Walker2d, Humanoid) or DM Control.
   * Evaluating at only 100k steps on sub-saturated regimes leaves open the question of whether this smoothing impairs asymptotic convergence.

4. **Tuning Asymmetry:**
   * The momentum parameter $m$ was selected after checking performance on Pendulum, while the baseline PPO hyperparameters were completely un-tuned defaults. Even a minor learning rate or GAE $\lambda$ tweak could easily produce larger shifts than the observed differences.

---

### **Criteria Scores (0–100)**

* **Soundness: 35 / 100**  
  * Blending advantage estimates forward in time fundamentally distorts state-action credit assignment. The empirical differences are statistically insignificant and lack rigorous hypothesis testing.
* **Novelty: 30 / 100**  
  * Applying a standard 1D exponential moving average across a rollout buffer is a trivial operation without novel conceptual insights.
* **Significance: 25 / 100**  
  * The results on two toy environments do not demonstrate practical utility or provide insights beneficial to the broader RL community.
* **Clarity: 85 / 100**  
  * The manuscript is clear, concise, reproducible, and candidly outlines its own flaws and limitations.

---

### **Overall Score & Recommendation**

* **Final Average Score:** **43.75 / 100**
* **Recommendation:** **Reject**