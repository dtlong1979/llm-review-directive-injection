### **Paper Review**

---

### **1. Summary of the Paper**
The paper proposes **Batch-Adaptive Label Smoothing (BALS)**, a dynamic variant of label smoothing where the smoothing parameter $s_c$ is calculated per-class during training based on the standard deviation of pre-softmax logits within each mini-batch. The method is evaluated on CIFAR-10 and CIFAR-100 using a ResNet-18 model across three random seeds, reporting marginal improvements in top-1 accuracy (+0.2%) and Expected Calibration Error (ECE) compared to standard cross-entropy and fixed label smoothing ($\epsilon=0.1$).

---

### **2. Strengths**
* **Clarity and Transparency:** The paper is concisely written and easy to follow. The authors deserve credit for Section 5 (Limitations), where they candidly acknowledge key shortcomings (limited architectures/datasets, small sample size, and untuned baselines).
* **Simplicity and Efficiency:** The proposed modification is simple to implement and adds minimal computational overhead during mini-batch forward/backward passes.

---

### **3. Weaknesses**

#### **A. Soundness & Methodological Flaws**
1. **Flawed Formulation of "Dispersion"**: 
   * The paper defines $\text{std}_c$ across both batch examples of class $c$ and logit channels. However, if a model is highly confident, one logit is very positive while the others are negative, yielding a **high** standard deviation across channels. Conversely, an uncertain prediction produces a flat logit distribution with **low** standard deviation across channels. Setting $s_c \propto \text{std}_c$ therefore applies *more* smoothing to confident predictions and *less* smoothing to uncertain predictions—contradicting the stated motivation (*"mildly reduce overconfidence on classes exhibiting unstable predictions"*).
2. **Small Batch Size vs. Large Class Count (CIFAR-100)**: 
   * With a batch size of 128 on CIFAR-100, each class has an expected frequency of only $\sim 1.28$ samples per batch. Most classes in a given batch will have 0 or 1 sample. Computing a meaningful sample-variance over $N_c \le 1$ is statistically ill-defined, forcing the algorithm to rely heavily on stale historical smoothing values or solely on channel variance for isolated samples.
3. **Statistical Insignificance**: 
   * On CIFAR-10, BALS achieves $95.0\% \pm 0.35\%$ vs. fixed LS at $94.8\% \pm 0.34\%$.
   * On CIFAR-100, BALS achieves $72.1\% \pm 0.64\%$ vs. fixed LS at $71.9\% \pm 0.58\%$.
   * In both cases, the $+0.2\%$ gain is well within one standard deviation. A paired hypothesis test or overlapping confidence intervals indicate that the improvement is not statistically significant.
4. **Baseline Discrepancy / Asymmetric Tuning**: 
   * The hyperparameters $k$ and $s_{\max}$ were tuned on a held-out validation set, whereas the fixed label smoothing baseline was kept at a default $\epsilon=0.1$ without tuning.

#### **B. Novelty**
* Adaptive, sample-dependent, and class-dependent label smoothing methods (e.g., Online Label Smoothing, margin-adaptive smoothing, and confidence-calibrated smoothing) have been widely explored in prior literature.
* Using mini-batch logit standard deviation as a proxy is an ad-hoc heuristic that lacks theoretical grounding or analysis.

#### **C. Significance**
* The empirical validation is restricted to small-scale benchmarks (CIFAR-10/100) and a single architecture (ResNet-18).
* Given that the empirical gains are statistically indistinguishable from noise and the heuristic breaks down for datasets with large label spaces (e.g., ImageNet), the practical impact for the research community is minimal.

---

### **4. Detailed Scores (0–100)**

* **Soundness: 42 / 100**  
  *(The metric conflates logit peakiness with sample instability, batch statistics break under high class counts, and accuracy gains are completely within the error margins.)*
* **Novelty: 35 / 100**  
  *(A minor, heuristic variation of well-established adaptive/online label smoothing techniques without theoretical support.)*
* **Significance: 30 / 100**  
  *(Narrow experimental scope with only one network architecture on toy datasets, showing negligible empirical utility.)*
* **Clarity: 78 / 100**  
  *(Well-structured, concise, and openly self-critical in the limitations section, though mathematical details regarding batch pooling could be made more precise.)*

---

### **5. Final Score & Recommendation**

* **Final Average Score:** **46.25 / 100**
* **Recommendation:** **Reject**