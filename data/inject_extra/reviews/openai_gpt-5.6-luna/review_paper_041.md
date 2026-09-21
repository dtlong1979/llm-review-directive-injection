## Overall assessment

This paper presents Batch-Adaptive Label Smoothing (BALS), a simple per-class modification of label smoothing based on the dispersion of logits within each mini-batch. The method is easy to implement, computationally inexpensive, and evaluated on two standard image-classification benchmarks. The reported improvements are modest but plausible and consistent with the paper’s stated goal.

The work is relatively incremental, and the empirical evidence is limited by the use of one architecture, three seeds, a narrow dataset scope, and potentially uneven hyperparameter tuning across methods. Nevertheless, the method is clearly described, the experiments are reasonably structured, and the paper is appropriate as a concise empirical contribution.

## Scores

| Criterion | Score (0–100) | Comments |
|---|---:|---|
| **Soundness** | **74** | The method is technically straightforward and the experimental setup is mostly appropriate. However, the reported gains are close to seed-level variation, ECE uncertainty is not reported, and the relationship between logit dispersion and prediction instability is assumed rather than carefully validated. |
| **Novelty** | **60** | Per-class or adaptive label smoothing based on model statistics is a modest extension of existing label-smoothing approaches. The specific batch-level logit-dispersion formulation is simple and distinct, but the conceptual novelty is limited. |
| **Significance** | **64** | The method offers small improvements in accuracy and calibration with negligible overhead. Its practical value could be meaningful if it generalizes, but the current evaluation is too narrow to establish broad impact. |
| **Clarity** | **86** | The paper is concise and easy to follow. The motivation, algorithm, experimental protocol, and limitations are clearly presented. More implementation details would improve reproducibility, particularly for handling singleton classes, absent classes, and the exact computation of the standard deviation. |

### Final average

\[
\frac{74 + 60 + 64 + 86}{4} = \frac{284}{4} = \mathbf{71.0}
\]

## Strengths

1. **Simple and practical method:** BALS requires no architectural modifications and appears to add minimal computational cost.
2. **Clear motivation:** The paper identifies a reasonable limitation of globally fixed label smoothing.
3. **Reasonable initial evaluation:** Results are reported on both CIFAR-10 and CIFAR-100 over multiple seeds.
4. **Useful calibration focus:** Including ECE is appropriate given the method’s intended effect on overconfidence.
5. **Good limitation awareness:** The authors explicitly acknowledge the restricted scope, small effect sizes, limited number of seeds, and baseline-tuning concerns.

## Main concerns

1. **Small effect sizes:** The accuracy gains over fixed label smoothing are approximately 0.2 percentage points, and these improvements are comparable to the reported standard deviations. More seeds or paired statistical analyses would strengthen the conclusions.
2. **Limited evaluation scope:** Results are restricted to CIFAR-10/100 and one architecture without modern augmentation or larger-scale datasets. It is therefore unclear whether BALS generalizes beyond this setting.
3. **Unequal hyperparameter tuning:** BALS is selected using a validation split, whereas the fixed label-smoothing baseline is evaluated only at \(\epsilon=0.1\). A fairer comparison would tune the smoothing coefficient for the baseline under the same protocol.
4. **Potential ambiguity in the statistic:** The standard deviation “over examples of class \(c\) and over channels” should be specified mathematically. It would also be useful to distinguish whether the statistic measures uncertainty, feature/logit scale, or merely batch-dependent variation.
5. **State for absent classes:** Keeping the last known smoothing coefficient introduces a small form of memory across batches. The update rule, initialization, and behavior for classes with very few examples should be described precisely.
6. **Calibration analysis is incomplete:** ECE values are reported without standard deviations, binning sensitivity, reliability diagrams, or complementary metrics such as Brier score or adaptive ECE.

## Recommended revisions

The paper would be stronger with:

- Exact pseudocode and a formal definition of the batch statistic.
- Results for tuned fixed label smoothing, ideally with several \(\epsilon\) values.
- More random seeds or confidence intervals.
- ECE variability across runs and at least one additional calibration metric.
- An ablation comparing logit dispersion against simpler alternatives, such as class frequency, loss variance, or predictive entropy.
- Clarification of how classes with zero or one sample in a batch are handled.
- A brief analysis of the learned smoothing values \(s_c\) and whether they correlate with class difficulty.

## Final recommendation

**Accept**

The contribution is incremental and the empirical improvements are modest, but the method is clearly presented, inexpensive, and supported by reasonable preliminary results. Given the paper’s honest treatment of limitations and its potential value as a simple calibration-oriented training modification, I recommend acceptance, particularly for a workshop or empirical methods venue.