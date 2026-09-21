## Overall assessment

The paper presents a straightforward curriculum over text augmentation operators for contrastive intermediate training. The topic is relevant and the reported results are promising, but the central method is not sufficiently well specified and the empirical evidence is not yet strong enough to support the claims. In particular, the curriculum is largely a manually ordered, threshold-based augmentation policy rather than a genuinely linear increase in augmentation strength, and the comparison may be affected by unequal hyperparameter tuning.

### Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **35** | The experimental design is plausible, but important methodological details are missing and some comparisons are potentially unfair. Statistical significance and robustness are not established. |
| **Novelty** | **42** | Applying a difficulty curriculum to contrastive text augmentation is a reasonable idea, but the method is a relatively simple thresholded ordering of existing operators. The distinction from standard augmentation scheduling is modest. |
| **Significance** | **45** | Low-resource classification is important, and the reported gains could be useful if reliable. However, the gains are moderate, the benchmark scope is narrow, and the evidence does not yet demonstrate broad impact. |
| **Clarity** | **74** | The paper is generally well organized and readable. Nevertheless, the augmentation probabilities, curriculum implementation, data splits, and tuning protocol are underspecified. |

### Final average

\[
\frac{35 + 42 + 45 + 74}{4} = \mathbf{49.0}
\]

## Recommendation: **Reject**

### Main strengths

- Addresses an important practical setting: text classification with few labeled examples.
- Uses a simple method that is potentially easy to integrate into existing contrastive-training pipelines.
- Includes several relevant baselines, multiple datasets, ablations, and a label-scarcity analysis.
- The paper is clearly structured and the reported trends are internally consistent.

### Main weaknesses

1. **The claimed linear curriculum is not actually linear.**  
   The curriculum level \(c(t)\) is linear, but the augmentation policy changes only when thresholds of 0.25, 0.5, and 0.75 are crossed. The resulting operator distribution is therefore staircase-like. Moreover, the strength of each individual operator is fixed: token dropout is always 10%, synonym replacement is always 15%, and so on. The method is more accurately described as a manually staged augmentation schedule.

2. **The policy is underspecified.**  
   The statement that “the probability of applying each operator is determined by \(c(t)\)” is not accompanied by an explicit probability formula. It is unclear whether the available operators are sampled uniformly, whether token dropout remains more likely than later operators, and whether different operators are independently applied or mutually exclusive. This matters substantially for reproducibility.

3. **Potentially unfair hyperparameter comparisons.**  
   CurCon is tuned over 48 configurations on each validation set, whereas the baselines use hyperparameters from their original papers. This gives CurCon a significant tuning advantage, especially in a low-resource setting. All methods should receive comparable tuning budgets, or the authors should report results under both original and tuned settings.

4. **Insufficient statistical analysis.**  
   The improvements over CERT are relatively small: 1.1 points on average and 0.5 points with 1,000 labels. No confidence intervals, paired tests, per-seed results, or significance tests are reported. The paper should establish whether the gains are statistically reliable across label subsets and random seeds.

5. **Limited evidence for generality.**  
   The experiments cover only four short English classification datasets and one encoder architecture. The reported gains may depend heavily on the chosen augmentation resources, especially WordNet and German back-translation.

6. **Important implementation details are missing.**  
   The paper should specify the exact back-translation model and decoding settings, tokenization and truncation rules, synonym-selection procedure, span-deletion behavior for short texts, data deduplication, and whether validation examples are included in unlabelled contrastive training.

7. **Some cost claims are unclear.**  
   The paper says back-translated views are pre-computed, but CurCon is still 12% slower than CERT because of on-the-fly operations. The computational comparison should report preprocessing time, training time, total GPU hours, and memory usage for every method.

8. **Ablations do not fully isolate the source of the gains.**  
   A stronger analysis would compare:
   - the same augmentation mixture with a randomized operator order;
   - a smooth probability schedule versus the threshold schedule;
   - fixed augmentation strength with the same total operator exposure;
   - curricula with different orderings and durations;
   - matched compute and matched numbers of views.

The results are suggestive, but the current manuscript does not adequately demonstrate that the improvement comes specifically from curriculum scheduling rather than from the selected augmentation mixture, tuning advantages, or other implementation choices. A substantially revised version with a more rigorous and fair experimental protocol could become publishable.