## Review

### Summary

This paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation strength during contrastive pretraining, moving from token dropout to synonym replacement, span deletion, and back-translation. Across four benchmarks and multiple label budgets, CurCon outperforms direct fine-tuning, UDA, SimCSE, and CERT, with particularly strong gains in the most label-scarce setting.

### Strengths

- **Clear and practically motivated problem.** The focus on low-resource classification and use of unlabeled in-domain data is relevant and important.
- **Simple, modular method.** The curriculum can be incorporated into existing contrastive intermediate-training pipelines without modifying the downstream classifier or adding inference-time parameters.
- **Consistent empirical improvements.** CurCon improves over CERT on all four reported datasets and across all three label budgets.
- **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that the schedule, rather than only the augmentation set, contributes to the gains.
- **Good presentation.** The method, experimental setup, limitations, and computational cost are described clearly and concisely.

### Concerns and suggestions

1. **Statistical testing is limited.** Results are reported with standard deviations over five seeds, but the paper does not provide paired significance tests or confidence intervals for the main comparisons. Adding such tests would strengthen the claim that the gains are reliable, especially because the improvements on TREC and at 1,000 labels are relatively modest.

2. **Baseline tuning should be clarified.** CurCon is selected using a grid search, while the baselines use hyperparameters from their original papers. This may disadvantage the baselines, particularly under a changed low-resource sampling protocol. Ideally, all methods should receive comparable tuning budgets, or the paper should report results under both original and tuned settings.

3. **The curriculum definition could be more precise.** The paper states that augmentation operators “become available” at thresholds, but it would help to specify whether the probability distribution is uniform over available operators, whether token dropout remains equally likely throughout, and whether augmentation is independently sampled for each view.

4. **The role of augmentation composition is not fully isolated.** The method samples one operator per view, so the gains may reflect the particular operator mixture as well as the curriculum. Additional comparisons with a fixed mixture matched exactly to the curriculum’s marginal operator frequencies would better separate curriculum effects from distributional effects.

5. **Reproducibility details could be expanded.** Important details such as the back-translation model and decoding settings, WordNet preprocessing, maximum sequence length, and exact fine-tuning and contrastive learning schedules are not fully specified.

6. **Scope is appropriately acknowledged but narrow.** The experiments cover only English, short-text classification, and BERT-base. This does not undermine the central contribution, but evaluation on at least one longer-text or cross-domain task would improve confidence in generality.

These are mainly evaluation and reproducibility improvements rather than fundamental flaws. The central method is straightforward, the experimental trends are coherent, and the ablations support the main claim.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 84/100 |
| Novelty | 78/100 |
| Significance | 82/100 |
| Clarity | 90/100 |

### Final average

\[
\frac{84 + 78 + 82 + 90}{4} = 83.5
\]

## Final recommendation: **Accept**

CurCon presents a clear and practically useful improvement to contrastive intermediate training for low-resource classification. Although the paper would benefit from stronger statistical analysis, more carefully matched baseline tuning, and additional reproducibility details, the proposed curriculum is simple, well motivated, and supported by consistent improvements across datasets and label regimes.