## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually expands the augmentation policy during contrastive training, beginning with token dropout and progressively enabling synonym replacement, span deletion, and back-translation. The adapted encoder is then fine-tuned on a small labelled set. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show consistent gains over fine-tuning, UDA, SimCSE, and CERT. Ablations suggest that both the curriculum and the ordering from weak to strong augmentation contribute to performance.

### Strengths

1. **Clear and practically motivated problem.** The focus on low-resource classification and exploiting unlabelled in-domain text is important and relevant.
2. **Simple, modular method.** CurCon can be incorporated into existing contrastive intermediate-training pipelines without changing inference or fine-tuning.
3. **Consistent empirical gains.** The method improves over CERT on all four datasets and reports gains across multiple label budgets.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons directly test whether the schedule and its direction matter.
5. **Appropriate reporting of seed variation.** Results include means and standard deviations over five seeds, which is valuable in the low-resource setting.
6. **Good presentation.** The paper is well organized, concise, and its method can be implemented from the description.

### Concerns and suggestions

1. **Baseline tuning fairness should be clarified.** CurCon is selected using a grid search over 48 configurations per dataset, whereas the baselines use hyperparameters from their original papers. This may advantage CurCon, especially in a low-resource setting. A stronger evaluation would tune all methods under the same validation protocol or report sensitivity analyses.
2. **The schedule is not fully “linear” in the operational sense.** The curriculum level is linear, but operators are introduced through discrete thresholds and then sampled uniformly. The paper should distinguish more clearly between a linear curriculum variable and a piecewise-constant augmentation policy.
3. **Statistical testing would strengthen the conclusions.** The reported standard deviations are useful, but paired significance tests across seeds or confidence intervals would help establish whether the relatively small gains over CERT, particularly on some datasets, are statistically reliable.
4. **The unlabelled-data protocol deserves more detail.** The paper should specify precisely whether validation examples, test examples, and any duplicated sentences are excluded from contrastive training. This is especially important when using standard benchmark corpora.
5. **A broader analysis of augmentation interactions would be useful.** The current ablation removes back-translation but does not isolate each operator or test alternative orderings. Such experiments would better identify whether the benefit comes from curriculum scheduling itself or from the particular augmentation sequence.
6. **Reproducibility details are somewhat incomplete.** Important details such as maximum sequence length, projection-head dimensions, exact learning rates, number of fine-tuning runs, and the back-translation model should be reported.

These issues are primarily about experimental rigor and reproducibility rather than the central validity of the approach. The consistent improvements, direct curriculum ablations, and label-budget analysis provide a sufficiently convincing empirical basis for the paper’s main claims.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 80/100 |
| Novelty | 74/100 |
| Significance | 78/100 |
| Clarity | 86/100 |

**Final average:**  
\[
\frac{80 + 74 + 78 + 86}{4} = 79.5
\]

## Final recommendation: **Accept**

The paper presents a straightforward but useful extension of contrastive intermediate training, supported by consistent results and relevant ablations. While baseline tuning fairness, statistical testing, and implementation details should be improved in the final version, these concerns do not undermine the main contribution.