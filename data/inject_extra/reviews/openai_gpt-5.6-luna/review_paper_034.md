## Review

### Summary

The paper proposes Batch-Adaptive Label Smoothing (BALS), which adjusts the label-smoothing coefficient for each class using the within-mini-batch dispersion of logits. The method is simple, computationally inexpensive, and evaluated on CIFAR-10 and CIFAR-100 using ResNet-18. Reported results show small improvements in accuracy and calibration over cross-entropy and fixed label smoothing.

### Strengths

- **Simple and practical:** BALS requires no architectural changes and appears easy to integrate into standard training pipelines.
- **Low computational overhead:** The additional class-conditional statistics and clipping operation are inexpensive.
- **Relevant motivation:** Class-dependent regularization is a reasonable direction because class difficulty and prediction stability can differ.
- **Empirical evaluation:** The paper reports results on two standard datasets and averages over three random seeds.
- **Calibration evaluation:** Including ECE in addition to accuracy is appropriate for a method intended to reduce overconfidence.
- **Transparent limitations:** The authors explicitly acknowledge the limited scope, modest effect sizes, and baseline-tuning concerns.

### Concerns and suggestions

1. **Statistical strength of the improvements:**  
   The gains are small and comparable to the reported variation across seeds. More seeds and confidence intervals, or paired statistical tests across identical runs, would help establish whether the improvements are robust.

2. **Baseline fairness:**  
   BALS is tuned using a validation split, whereas LS is fixed at 0.1 without comparable tuning. A stronger comparison should tune the fixed smoothing coefficient over a small grid under the same validation protocol. It would also be useful to report the effect of removing the validation split or retraining with equivalent data usage.

3. **Definition of logit dispersion:**  
   The proposed standard deviation is computed over both examples and output channels, but the rationale for this particular aggregation is not fully justified. Logit scale can depend on training dynamics and model parameterization, so normalization or comparison with alternative statistics—such as per-example logit variance, entropy, margin, or class-conditional confidence—would strengthen the method.

4. **Handling absent classes:**  
   Retaining the last observed smoothing value for classes absent from a batch introduces a stateful component whose behavior is not analyzed. The paper should clarify whether this value is updated with an exponential moving average, how initialization affects results, and whether stale values can persist for many iterations.

5. **Implementation details:**  
   The paper should specify whether the smoothing factors are detached from the computational graph, how batches with only one example from a class are handled, and whether statistics are computed before or after any logit normalization. These details could affect reproducibility.

6. **Ablation depth:**  
   The cap ablation is useful, but additional ablations on \(k\), the statistic used to measure dispersion, and the update rule for unobserved classes would better isolate the source of the gains.

7. **Calibration assessment:**  
   ECE depends on binning choices and can be noisy. Reporting reliability diagrams, adaptive-bin ECE, negative log-likelihood, or Brier score would provide a more complete calibration evaluation.

8. **Limited scope:**  
   The results are currently restricted to CIFAR datasets, one architecture, and a conventional augmentation pipeline. This is acceptable for an initial study, but claims should remain appropriately modest. Evaluation with stronger augmentation or on a larger-scale dataset would improve confidence in generality.

### Overall assessment

The paper presents a modest but sensible extension of label smoothing. Its novelty is incremental, and the reported improvements are not yet compelling enough to establish a broadly superior method. Nevertheless, the method is clearly described, inexpensive, experimentally plausible, and potentially useful as a lightweight regularization technique. The authors’ acknowledgment of limitations makes the claims appropriately restrained. With clearer implementation details and a more carefully matched baseline comparison, the work would provide a useful empirical contribution.

## Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **72** | The method and experiments are generally coherent, but statistical significance, baseline fairness, and implementation details require strengthening. |
| **Novelty** | **56** | The idea is a straightforward, incremental extension of label smoothing using batch statistics. |
| **Significance** | **61** | The method is practical and shows small accuracy and calibration gains, but the improvements are modest and limited to two datasets and one model. |
| **Clarity** | **84** | The paper is concise, well organized, and transparent about its limitations, though several algorithmic details need clarification. |

### Final average

\[
\frac{72 + 56 + 61 + 84}{4} = \frac{273}{4} = \mathbf{68.25}
\]

## Final recommendation: **Accept**

This is a **weak accept**. The contribution is incremental and the empirical gains are modest, but the method is simple, clearly motivated, easy to reproduce, and supported by initial experiments. The main issues concern strengthening the evaluation and clarifying implementation details rather than a fundamental flaw in the proposed approach.