## Review

### Summary
The paper proposes Batch-Adaptive Label Smoothing (BALS), which assigns each class a smoothing coefficient based on the standard deviation of logits for that class within a mini-batch. The method is simple and inexpensive, and the reported results show small improvements over cross-entropy and fixed label smoothing on CIFAR-10 and CIFAR-100.

### Strengths
- Simple modification with minimal computational and architectural overhead.
- The paper is generally well organized and clearly describes the intended method.
- Evaluation includes two datasets, three random seeds, and both accuracy and ECE.
- The limitations section appropriately acknowledges restricted scope and possible fairness issues.

### Concerns

#### Soundness
The central statistic is not sufficiently justified. The paper computes the standard deviation of logits “over examples of class \(c\) and over channels,” but it is unclear whether this means a pooled standard deviation, an average of per-channel deviations, or something else. Logit dispersion across channels can also indicate increased confidence or class separation rather than prediction instability, so the proposed interpretation is not established.

There is also an important implementation ambiguity: because \(s_c\) is computed from the current logits, it must presumably be detached from the computation graph. Otherwise, the loss includes additional gradients through the smoothing coefficient, meaning the method is not simply adaptive label smoothing as described. This should be specified explicitly.

For CIFAR-100 with batch size 128, many classes will be absent from a batch. Maintaining stale per-class smoothing values introduces an implicit stateful mechanism whose update behavior is not analyzed. The initialization at zero may also affect early training. The method’s batch dependence and sensitivity to batch composition are not evaluated.

The empirical evidence is limited. Accuracy improvements are small and comparable to the reported across-seed variation. The comparison is also not fully fair: BALS receives hyperparameter selection, while the fixed-label-smoothing baseline is evaluated only at \(\epsilon=0.1\) and is not tuned. There are no confidence intervals, paired statistical tests, or comparisons against tuned label smoothing and other calibration methods.

#### Novelty
The idea is a straightforward extension of adaptive or class-dependent label smoothing using batch statistics. The paper itself acknowledges this. While the specific statistic and implementation may be new, the conceptual novelty is modest, and the paper does not establish a strong distinction from related adaptive regularization methods.

#### Significance
The reported gains are small:

- CIFAR-10: approximately +0.2 percentage points over fixed label smoothing.
- CIFAR-100: approximately +0.2 percentage points over fixed label smoothing.
- ECE improvements are also modest.

The experiments are restricted to one architecture, two small datasets, and an outdated/simple augmentation setup. Consequently, it is unclear whether BALS provides a meaningful advantage in modern training regimes or beyond this narrow setting.

#### Clarity
The paper is relatively clear and concise. The motivation, algorithmic intent, experimental setup, and limitations are easy to follow. However, the exact definition of the logit standard deviation, handling of absent classes, treatment of gradients through \(s_c\), and whether validation data are removed from training need to be stated more precisely.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 38/100 |
| Novelty | 32/100 |
| Significance | 28/100 |
| Clarity | 76/100 |

### Final average

\[
\frac{38 + 32 + 28 + 76}{4} = 43.5
\]

## Final recommendation: **Reject**

The method is easy to implement and the presentation is reasonably clear, but the paper does not yet provide sufficiently rigorous evidence that BALS is sound, novel, or broadly useful. A stronger revision should clarify the exact statistic and gradient treatment, tune all baselines fairly, report more seeds and uncertainty estimates, compare against additional adaptive/calibration baselines, and evaluate across more architectures, datasets, and augmentation regimes.