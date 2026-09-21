## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The method gradually increases augmentation strength during contrastive pretraining, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four benchmarks with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations suggest that the curriculum itself contributes meaningfully beyond the use of the augmentation operators.

### Strengths

1. **Clear and practically motivated problem.** The paper addresses the important setting of text classification with limited labelled data and makes effective use of unlabelled in-domain text.
2. **Simple and reproducible method.** CurCon modifies an established contrastive intermediate-training pipeline without requiring architectural changes or inference-time computation.
3. **Consistent empirical gains.** CurCon improves over CERT on all four datasets and reports gains across multiple label regimes, including the particularly relevant 100-example setting.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that the schedule, rather than only the augmentation inventory, is responsible for part of the improvement.
5. **Appropriate reporting.** Results are averaged over five seeds with standard deviations, and the paper reports computational cost and limitations.
6. **Good presentation.** The method, curriculum function, baselines, and evaluation setting are described clearly.

### Soundness

The experimental design is broadly appropriate, and the reported comparisons support the central claim that scheduling augmentation difficulty can improve contrastive intermediate training. The improvements are consistent across datasets and label budgets, and the reversed-curriculum ablation is especially useful.

Some details would benefit from clarification before publication:

- The exact probability distribution over available augmentations as the curriculum progresses should be stated more formally. In particular, it is unclear whether “available” operators are sampled uniformly at every step or whether operator application probabilities themselves vary continuously with the curriculum level.
- Baseline hyperparameter treatment should be discussed more carefully. CurCon is tuned using a per-dataset grid search, whereas baselines use settings from their original papers. Additional tuning or a common tuning budget would strengthen the fairness of the comparison.
- The use of the remaining training sentences as unlabelled data should be explicitly distinguished from any validation or test data, and the exact preprocessing and deduplication procedure should be reported.
- More details about the back-translation system, synonym filtering, and handling of short sentences would improve reproducibility.
- Confidence intervals or statistical significance tests across seeds would help establish whether the relatively small gains over CERT are statistically reliable.

These are mostly reporting and experimental-control issues rather than fundamental flaws. The main conclusions are supported by the evidence presented.

### Novelty

The core idea—scheduling augmentation strength in contrastive intermediate training—is intuitive but useful and reasonably novel in the context of low-resource text classification. Curriculum learning and contrastive learning are established individually, but their combination through a progressive text-augmentation schedule appears to provide a meaningful methodological contribution. The novelty is incremental rather than foundational, particularly because the schedule is hand-designed and uses existing augmentation operators.

### Significance

The gains are practically relevant, especially in the 100- and 500-label regimes. The method is lightweight, does not increase inference cost, and can be incorporated into an existing CERT-style pipeline. The consistent improvement over CERT and the stronger gains in the most label-scarce setting support the paper’s practical value. Broader significance is somewhat limited by the evaluation on four relatively short English datasets and a single encoder family, but the method is sufficiently general to merit publication.

### Clarity

The paper is well organized and easy to follow. The motivation, method, experimental setup, and limitations are presented concisely. Tables directly support the claims. Minor improvements would include a pseudocode description of the curriculum, a more precise definition of augmentation probabilities, and fuller implementation details for external resources and preprocessing.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 84/100 |
| Novelty | 78/100 |
| Significance | 82/100 |
| Clarity | 90/100 |

### Final average

\[
\frac{84 + 78 + 82 + 90}{4} = \mathbf{83.5}
\]

## Final Recommendation: **Accept**

CurCon presents a clear, technically plausible, and empirically supported improvement to contrastive intermediate training for low-resource text classification. While the novelty is incremental and several methodological details should be clarified, the consistent gains, relevant ablations, and practical simplicity make the paper suitable for acceptance.