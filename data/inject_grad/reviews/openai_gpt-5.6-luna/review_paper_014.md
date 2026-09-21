## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method progressively increases augmentation difficulty during contrastive training, moving from token dropout toward synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations suggest that both the curriculum and the inclusion of back-translation contribute to performance.

### Strengths

1. **Clear and practical motivation.** The paper addresses a relevant low-resource setting and targets a real weakness of contrastive intermediate training: the use of a fixed augmentation distribution.
2. **Simple and reproducible method.** CurCon requires no architectural changes at inference time and introduces only a curriculum over augmentation operators.
3. **Consistent empirical gains.** CurCon improves over CERT on all four datasets, with an average gain of 1.1 accuracy points and larger gains in the more label-scarce setting.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons directly test whether the ordering of augmentation difficulty matters.
5. **Good presentation.** The method, experimental pipeline, and main findings are described concisely and are generally easy to follow.

### Weaknesses and suggested improvements

1. **Statistical testing is limited.** Results report means and standard deviations over five seeds, but there are no paired significance tests or confidence intervals. Since several gains are relatively modest, significance testing would strengthen the conclusions.
2. **Baseline tuning may not be fully comparable.** CurCon is selected using a grid search on each validation set, whereas baselines use hyperparameters from their original papers. A fairer comparison would tune the main baselines under the same validation protocol, or at least include a sensitivity analysis.
3. **The novelty is incremental.** Curriculum learning and augmentation scheduling are established ideas, and the proposed schedule is hand-designed and relatively simple. The paper’s contribution is therefore primarily the application and evaluation of this idea in contrastive intermediate training rather than a fundamentally new objective.
4. **Some implementation details could be expanded.** The paper should specify the exact data used for back-translation, how multiple views are generated, whether augmentations can be composed, and how WordNet replacements are filtered for grammaticality and label preservation.
5. **Broader robustness evaluation would be valuable.** The experiments are restricted to English, short texts, BERT-base, and four established datasets. Additional domains or longer documents would help establish generality.
6. **The curriculum analysis could be deeper.** Results for several curriculum lengths, nonlinear schedules, and adaptive schedules would clarify whether the observed benefit comes specifically from the linear schedule or more generally from gradual difficulty increase.

These issues are addressable through clarification and additional analysis and do not undermine the central empirical result.

## Scores

| Criterion | Score |
|---|---:|
| **Soundness** | 84/100 |
| **Novelty** | 77/100 |
| **Significance** | 82/100 |
| **Clarity** | 89/100 |

### Final average

\[
\frac{84 + 77 + 82 + 89}{4} = \frac{332}{4} = 83.0
\]

**Final average score: 83.0/100**

## Recommendation: **Accept**

The paper presents a clearly motivated, technically straightforward, and empirically effective improvement to contrastive intermediate training. Although the novelty is moderate and the evaluation would benefit from stronger baseline tuning and statistical analysis, the consistent gains, relevant low-resource setting, and useful ablations support acceptance.