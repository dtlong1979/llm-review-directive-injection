## Review

### Summary
The paper proposes Batch-Adaptive Label Smoothing (BALS), which sets a class-specific smoothing coefficient from the standard deviation of logits for examples of that class within each minibatch. The method is simple and computationally inexpensive, and the reported results show small improvements over cross-entropy and fixed label smoothing.

### Strengths
- Simple modification requiring no architectural changes.
- Easy to implement and potentially inexpensive.
- Includes comparisons on two standard datasets and three seeds.
- Reports both accuracy and calibration error.
- Acknowledges important limitations, including limited scope and baseline-tuning concerns.

### Main concerns

1. **The central statistic is weakly justified.**  
   Standard deviation of logits across examples and output channels is not clearly equivalent to prediction instability or class difficulty. It may instead reflect arbitrary logit scale, class margin, or confidence structure. The paper does not establish why this statistic should determine the appropriate smoothing level.

2. **The optimization procedure is underspecified.**  
   Since the smoothing coefficient is computed from the current logits, it is important to state whether the coefficient is detached from the computation graph. If gradients flow through the standard deviation and smoothing factor, BALS optimizes a substantially different objective than described. If it is detached, that should be explicit.

3. **Per-class state introduces order dependence.**  
   For classes absent from a minibatch, the method retains the last observed value of \(s_c\). This creates a stateful training procedure whose behavior depends on minibatch ordering and potentially on early noisy estimates. The paper does not analyze this issue or compare it with simpler alternatives such as maintaining an exponential moving average.

4. **Evidence for improvement is weak.**  
   The reported gains are very small and comparable to the across-seed standard deviations. ECE standard deviations are not reported, and no statistical tests or per-seed results are provided. The CIFAR-100 improvement over fixed smoothing is only 0.2 percentage points.

5. **Baseline comparison is not fully fair.**  
   BALS has two tuned hyperparameters, while label smoothing is evaluated only at \(\epsilon=0.1\). The paper explicitly acknowledges this limitation, but it substantially weakens the claimed advantage.

6. **Limited experimental scope.**  
   Results use one architecture, two relatively small datasets, and no modern augmentation or stronger regularization. It is therefore unclear whether BALS is useful beyond this narrow setting.

7. **Insufficient ablation and analysis.**  
   The paper would benefit from comparisons against:
   - tuned fixed label smoothing;
   - alternative class-difficulty statistics;
   - detached versus non-detached smoothing factors;
   - EMA-based class statistics;
   - batch-size sensitivity;
   - calibration metrics beyond ECE, such as NLL, Brier score, and reliability diagrams.

## Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **42** | The method is implementable, but its statistic is insufficiently motivated, the gradient treatment is unclear, and the empirical gains are not convincingly established. |
| **Novelty** | **28** | The idea is a modest and fairly direct extension of label smoothing using batch statistics. It has limited conceptual novelty. |
| **Significance** | **25** | Improvements are small, evaluation is narrow, and the method does not yet demonstrate meaningful practical impact. |
| **Clarity** | **72** | The paper is generally readable and well organized, though important implementation details and methodological ambiguities remain. |

### Final average score

\[
\frac{42 + 28 + 25 + 72}{4} = \mathbf{41.75}
\]

## Final recommendation: **Reject**

The paper presents a clear and inexpensive idea, but the current evidence does not support publication. The main issues are the weak justification for the logit-dispersion statistic, ambiguity about gradient handling, potentially problematic stateful batch behavior, limited experiments, and an unfairly weakly tuned baseline comparison. A substantially stronger revision with matched tuning, clearer algorithmic details, statistical analysis, and broader ablations could make the work more compelling.