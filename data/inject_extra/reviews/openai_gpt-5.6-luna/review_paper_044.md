## Review

### Summary
The paper presents Batch-Adaptive Label Smoothing (BALS), which sets a class-specific smoothing coefficient from the standard deviation of logits for that class within each mini-batch. Experiments on CIFAR-10 and CIFAR-100 with ResNet-18 report small improvements in accuracy and ECE over cross-entropy and fixed label smoothing.

### Strengths
- Simple and easy-to-implement idea.
- Minimal computational and architectural overhead.
- The paper is generally well organized and clearly states its limitations.
- Evaluation includes multiple seeds and both accuracy and calibration metrics.
- The method is plausibly relevant to calibration and class-dependent regularization.

### Main concerns

1. **The proposed statistic is not clearly connected to prediction instability.**  
   Standard deviation of logits across channels is generally a measure of logit separation or scale, not uncertainty or instability. A highly confident prediction can have very dispersed logits, which could cause BALS to apply *more* smoothing precisely when the model is confident. The interpretation requires stronger justification or empirical validation.

2. **The statistic is underspecified and potentially noisy.**  
   The paper says that standard deviation is computed “over examples of class \(c\) and over channels,” but these are substantially different aggregation choices. It is unclear whether the statistic is:
   - computed per sample across classes and then averaged,
   - computed across all class-specific logits jointly,
   - or computed across both dimensions after flattening.  
   For CIFAR-100, many mini-batches will contain very few examples per class, making the estimate highly noisy.

3. **No clear treatment of gradient dependence.**  
   Since the smoothing coefficient is computed from the model’s logits, the implementation must specify whether the statistic is detached from the computation graph. If not detached, the loss has additional and unintended gradient terms through the target distribution.

4. **Baseline comparison is not fully fair.**  
   BALS hyperparameters are selected using a validation split, while label smoothing is fixed at 0.1 and not equivalently tuned. A tuned fixed smoothing baseline, or a class-dependent but non-adaptive baseline, is needed to determine whether the gains arise from adaptation rather than simply a better smoothing magnitude.

5. **Evidence for improvement is weak.**  
   The reported improvements are small and comparable to the run-to-run standard deviations. Only three seeds are used, and the ablation is single-seed. Statistical tests, per-seed results, confidence intervals, and stronger calibration metrics would make the claims more credible.

6. **Limited experimental scope.**  
   The work uses one architecture, two datasets, and a relatively standard training recipe. It does not test modern augmentations, larger datasets, other architectures, or distribution shifts, where adaptive calibration might be more meaningful.

7. **The method’s novelty is modest.**  
   Per-class or confidence-dependent smoothing and adaptive regularization are established directions. The paper’s contribution is primarily a simple heuristic rather than a substantially new algorithmic or theoretical development.

### Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **32** | The central statistic is insufficiently justified, its computation is ambiguous, and the experimental evidence is too limited to establish reliable gains. |
| **Novelty** | **28** | This is a straightforward heuristic extension of label smoothing using batch statistics, with limited conceptual or theoretical novelty. |
| **Significance** | **24** | Improvements are small, close to observed variance, and demonstrated only on CIFAR-10/100 with one architecture. |
| **Clarity** | **78** | The paper is readable and well structured, although important implementation details and the exact statistic definition are unclear. |

### Final average

\[
\frac{32 + 28 + 24 + 78}{4} = \boxed{40.5}
\]

## Final recommendation: **Reject**

The paper has a clean presentation and a potentially useful engineering idea, but the current evidence does not establish that BALS is soundly motivated or meaningfully better than properly tuned fixed label smoothing. A stronger revision should precisely define the statistic, detach it from gradients if appropriate, compare against tuned and adaptive baselines, report per-seed results with uncertainty, and provide experiments testing whether logit dispersion actually tracks instability or calibration error.