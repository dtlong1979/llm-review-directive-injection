## Summary

This paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation difficulty during contrastive training, progressing from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four datasets with 500 labelled examples show improvements over fine-tuning, UDA, SimCSE, and CERT, with additional ablations supporting the value of the curriculum.

## Strengths

1. **Clear and practically motivated problem.** Low-resource classification and the use of unlabelled in-domain text are important settings, and the motivation for progressively increasing augmentation difficulty is intuitive.
2. **Simple, model-agnostic method.** CurCon can be inserted into an existing CERT-style pipeline without inference-time changes or architectural modifications.
3. **Reasonable experimental coverage.** The paper evaluates four datasets, several relevant baselines, multiple label budgets, and five random seeds.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that both the curriculum and its direction contribute to performance.
5. **Consistent improvements.** CurCon improves over CERT on all four datasets, with especially notable gains in the lower-label regime.
6. **Generally clear presentation.** The method, experimental setup, and limitations are described concisely and are easy to follow.

## Weaknesses and suggestions

1. **Baseline tuning is not fully comparable.** CurCon is selected using a 48-configuration validation grid on each dataset, whereas the baselines use hyperparameters reported in their original papers. This may advantage CurCon, especially in a low-resource setting. The baselines should ideally receive comparable tuning budgets, or the paper should report sensitivity analyses.
2. **The curriculum policy is underspecified.** The text states that each operator’s probability is “determined by” the curriculum level, but it does not give an explicit probability distribution. It is also unclear whether each view receives an independently sampled operator and whether augmentations can be composed.
3. **The role of the curriculum length deserves more analysis.** Since curriculum length is a key hyperparameter, results across several fixed values of \(L\) would help establish whether the gains are robust or concentrated at one carefully selected setting.
4. **Statistical reporting could be stronger.** Per-dataset results include standard deviations, but the paper does not report confidence intervals or significance tests for the main comparisons. Given the relatively modest gains over CERT on some datasets, paired seed-level tests would be useful.
5. **Reproducibility details are incomplete.** The paper should specify the back-translation model and decoding procedure, WordNet preprocessing, tokenization behavior after deletion, maximum sequence length, projection-head dimensions, and exact optimizer schedules.
6. **The evaluation scope is narrow.** All datasets are English and consist largely of short texts. The conclusions should therefore remain limited to this setting, though the paper appropriately acknowledges this limitation.
7. **Compute comparisons could be more precise.** The reported 12% overhead is useful, but wall-clock time, preprocessing cost, and the cost of generating or storing back-translated views should be separated.

These issues primarily affect reproducibility and the strength of the empirical claims rather than undermining the central result. The proposed method is straightforward, and the reported ablations provide meaningful evidence that the schedule—not merely the use of stronger augmentations—is beneficial.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 82/100 |
| Novelty | 73/100 |
| Significance | 78/100 |
| Clarity | 88/100 |

**Final average:** \((82 + 73 + 78 + 88) / 4 = 80.25/100\)

## Final recommendation

**Accept**

The contribution is incremental but well motivated, clearly presented, and supported by a coherent set of experiments. The main concerns involve baseline fairness, implementation details, and statistical validation, which should be addressed in a revision but do not outweigh the paper’s empirical contribution.