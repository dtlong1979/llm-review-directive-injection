## Overall review

CurCon presents a simple curriculum for contrastive intermediate training in which augmentation strength increases during training. The problem is relevant, and the empirical results are directionally plausible. However, the paper currently has substantial methodological and reproducibility weaknesses, and the novelty is relatively incremental. The evidence is not yet strong enough to support acceptance.

### Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **55** | The overall method is understandable and the reported trends are plausible. However, the experimental comparison is not fully controlled: CurCon is tuned using a 48-configuration grid search per dataset, while baselines use hyperparameters from their original papers. The paper does not report statistical significance tests or confidence intervals across runs. The curriculum definition also has a technical inconsistency: \(c(t)=\min(1,t/L)\) is undefined for \(L=0\), despite \(L=0\) being used to define the fixed-mixture ablation. Moreover, the stated schedule is threshold-based and changes the augmentation mixture discretely, rather than increasing augmentation strength linearly as claimed. |
| **Novelty** | **58** | Applying a difficulty curriculum to augmentation policies in contrastive intermediate training is a reasonable idea, but it is a fairly direct combination of existing curriculum learning and contrastive augmentation techniques. The paper does not clearly distinguish its contribution from augmentation scheduling, difficulty scheduling, or existing contrastive curricula. The method contains no new objective, augmentation mechanism, or adaptive scheduling principle. |
| **Significance** | **56** | Low-resource classification is important, and the reported 1.1-point improvement over CERT could be useful if robust. However, the evaluation is limited to four small English benchmarks and one encoder family. The gains are modest, and the paper does not establish whether they generalize to other domains, model sizes, languages, or more realistic distribution shifts. The strongest evidence is weakened by the lack of statistically validated comparisons and potentially unequal hyperparameter tuning. |
| **Clarity** | **79** | The paper is generally well organized, readable, and easy to follow. The tables and training pipeline are clearly presented. Nevertheless, several implementation details are underspecified, including the exact sampling probabilities, curriculum-length values, back-translation system, WordNet procedure, sequence truncation, validation protocol, and baseline tuning. The definition of the \(L=0\) case is also unclear or formally invalid as written. |

### Final score

\[
\frac{55 + 58 + 56 + 79}{4} = \mathbf{62.0}
\]

## Recommendation: **Reject**

### Main reasons

1. **Insufficiently controlled baseline comparison.** CurCon is extensively tuned, whereas the baselines use hyperparameters from prior work. Baselines should receive comparable tuning budgets, especially in a low-resource setting where optimization choices can substantially affect results.

2. **Ambiguous curriculum formulation.** The paper describes a linear increase in augmentation strength, but the actual policy activates operators at thresholds and samples uniformly among available operators. This is not clearly equivalent to a linear strength schedule.

3. **Formal issue with the ablation.** The formula \(c(t)=\min(1,t/L)\) is undefined for \(L=0\), although the fixed-mixture ablation relies on that setting.

4. **Limited evidence for robustness.** Five seeds are useful, but the paper reports only means and standard deviations, without paired significance tests, per-dataset ablation results, or variance analysis for the key comparisons.

5. **Incremental contribution.** The method is a straightforward scheduling modification to existing contrastive intermediate training. Stronger positioning and broader comparisons would be needed to establish a substantial research contribution.

The paper could become publishable after clarifying the method, tuning all baselines fairly, adding statistical testing and stronger ablations, and evaluating the approach across more datasets, domains, and encoder architectures.