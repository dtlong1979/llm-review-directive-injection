### **Review of "Advantage-Momentum PPO: A Small Smoothing Trick for Reinforcement Learning Control"**

---

### **1. Summary of the Paper**
The paper introduces **Advantage-Momentum PPO (AM-PPO)**, a heuristic modification to Proximal Policy Optimization (PPO). The proposed method applies an exponential moving average (EMA) forward in time across the Generalized Advantage Estimation (GAE) sequence within a trajectory rollout ($A_t^{\text{smooth}} = m A_t + (1-m) A_{t-1}^{\text{smooth}}$) prior to minibatch normalization. The author evaluates AM-PPO on two classic control environments (Pendulum-v1 and MountainCarContinuous-v0) over 100k environment steps across 5 seeds, reporting marginal improvements in mean evaluation returns.

---

### **2. Strengths**
* **Clarity and Transparency:** The manuscript is clearly written, straightforward to read, and remarkably honest about its empirical limitations.
* **Simplicity:** The proposed modification is trivially simple to implement (a single line of code) and adds virtually zero computational overhead.

---

### **3. Weaknesses**

#### **A. Theoretical Grounding & Credit Assignment Flaw (Major)**
* The policy gradient theorem relies on the expected advantage $A^\pi(s_t, a_t) = Q^\pi(s_t, a_t) - V^\pi(s_t)$ representing the relative quality of taking action $a_t$ in state $s_t$. 
* Smoothing $A_t$ forward in time with $A_{t-1}^{\text{smooth}}$ inextricably entangles the credit/blame of action $a_{t-1}$ with action $a_t$. If an agent takes a disastrous action at $t-1$ followed by an optimal recovery action at $t$, the EMA dampens the positive advantage of $a_t$, actively penalizing the correct action.
* Generalized Advantage Estimation (GAE) already smooths temporal-difference (TD) residuals *backward* from future rewards ($\sum (\gamma \lambda)^l \delta_{t+l}$). Smoothing *forward* across past timesteps introduces uncontrolled, non-stationary bias into the policy gradient without any mathematical justification.

#### **B. Empirical Insufficiency & Statistical Insignificance (Major)**
* **Toy Benchmarks Only:** The evaluation is restricted to two low-dimensional classic control tasks (`Pendulum-v1` and `MountainCarContinuous-v0`). Standard continuous control benchmarks (e.g., MuJoCo, Gymnasium Box2D, or Brax) are entirely absent.
* **No Statistically Significant Gain:** 
  * Pendulum-v1: PPO ($-165.2 \pm 34.1$) vs. AM-PPO ($-151.7 \pm 33.6$).
  * MountainCarContinuous-v0: PPO ($88.3 \pm 10.8$) vs. AM-PPO ($91.1 \pm 9.9$).
  In both tasks, the performance difference is well within one standard deviation ($\approx 0.1\text{--}0.4\sigma$). Across only 5 seeds, these results are statistically indistinguishable from baseline noise.
* **Premature Training Cutoff:** 100k steps is extremely short, and as the authors acknowledge, neither method converged to asymptotic performance.

#### **C. Lack of Diagnostic Evidence**
* The core premise is that temporal smoothing stabilizes gradients and reduces variance. However, no diagnostic evidence is provided (e.g., policy gradient variance, cosine similarity of gradients across minibatches, or policy entropy/KL divergence plots).

---

### **4. Category Scores (0–100)**

* **Soundness: 35/100**  
  *The core mechanism introduces systematic credit assignment bias that violates standard policy gradient derivations. Empirical results show overlapping error margins with no statistical significance.*

* **Novelty: 25/100**  
  *Applying an EMA across advantage signals is an incremental heuristic and conceptually conflates past actions with present decisions.*

* **Significance: 20/100**  
  *Tested on only two toy environments over short horizons; does not provide convincing evidence that the method generalizes or offers real utility to the RL community.*

* **Clarity: 85/100**  
  *The manuscript is well-structured, concise, and commendably forthright about its limitations.*

---

### **5. Final Score & Recommendation**

$$\text{Final Score} = \frac{35 + 25 + 20 + 85}{4} = \mathbf{41.25 / 100}$$

* **Recommendation:** **Reject**