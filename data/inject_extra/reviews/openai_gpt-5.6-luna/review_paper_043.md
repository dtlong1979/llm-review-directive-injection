## Review

### Summary

This paper proposes Batch-Adaptive Label Smoothing (BALS), which assigns each class in a mini-batch a smoothing coefficient based on the standard deviation of its logits. The method is simple, architecture-independent, and inexpensive to implement. Experiments on CIFAR-10 and CIFAR-100 with ResNet-18 show small improvements in accuracy and ECE over cross-entropy and fixed label smoothing.

### Strengths

- **Simple and practical:** BALS requires no architectural changes and has minimal computational overhead.
- **Clear motivation:** Adapting regularization to class-specific prediction instability is intuitive.
- **Reasonable initial evaluation:** The paper reports results on two datasets, uses multiple random seeds, and includes an ablation of the smoothing cap.
- **Improved reporting awareness:** The authors explicitly acknowledge limitations concerning scope, variance, and baseline tuning.
- **Potential utility:** The method could be useful as a lightweight regularization technique in settings where class difficulty varies substantially.

### Weaknesses and Suggestions

1. **Limited experimental scope.** Evaluation is restricted to CIFAR-10/100 and one architecture without modern augmentation or stronger training recipes. This limits evidence for generality, although it is adequate as an initial study.

2. **Baseline tuning is not fully matched.** BALS hyperparameters are selected using validation data, whereas the fixed label-smoothing baseline is evaluated only at \(\epsilon=0.1\). A stronger comparison should tune \(\epsilon\) over a small validation grid and ideally compare against class-dependent or adaptive regularization baselines.

3. **Small effect sizes.** The reported gains are modest and often comparable to the across-seed standard deviations. Reporting the individual seed results, confidence intervals, or statistical tests would make the conclusions more convincing.

4. **Definition of logit dispersion needs clarification.** The paper should specify precisely whether the standard deviation is computed over all class logits jointly, over samples followed by averaging channel-wise statistics, or using another aggregation. Since logit scale can vary during training, normalization or a discussion of scale sensitivity would be useful.

5. **State handling for absent classes is underspecified.** Keeping the last observed value for classes absent from a batch may make the method dependent on batch ordering and initialization. An ablation comparing this approach with zero, an exponential moving average, or a dataset-level statistic would strengthen the method.

6. **Mechanistic analysis is limited.** It would be helpful to report the distribution of \(s_c\) over training, how often the cap is reached, and whether BALS primarily benefits particular classes or simply behaves like a variable global smoothing coefficient.

7. **Calibration evaluation could be expanded.** ECE is useful but sensitive to binning. Reliability diagrams, adaptive ECE, Brier score, or negative log-likelihood would provide a more complete calibration assessment.

These issues primarily affect the strength and generality of the empirical claims rather than the basic validity of the proposed method.

## Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **74** | The method is technically plausible and the experiments are internally coherent, but the statistic definition, temporal state update, and limited baseline tuning require clearer treatment. |
| **Novelty** | **58** | The contribution is a modest and straightforward extension of label smoothing using batch statistics. It is still a distinct, easily implementable heuristic. |
| **Significance** | **62** | Improvements are small and demonstrated only on small datasets and one architecture, but the method’s simplicity and potential usefulness provide moderate practical value. |
| **Clarity** | **84** | The paper is well organized and easy to follow. Additional implementation details and a more precise definition of the dispersion calculation would improve reproducibility. |

### Final average

\[
\frac{74 + 58 + 62 + 84}{4} = \mathbf{69.5}
\]

## Final Recommendation: **Accept**

The paper presents a clear, lightweight, and empirically supported modification to label smoothing. Although the novelty and gains are moderate, the method is sufficiently well motivated and practical for acceptance, particularly as a concise empirical contribution. The paper would benefit from improved baseline fairness, more detailed specification of the batch-statistics computation, and stronger analysis of variance and calibration, but these are appropriate revisions rather than reasons for rejection.