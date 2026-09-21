## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The approach gradually increases augmentation strength during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples demonstrate improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations suggest that both the curriculum and the inclusion of back-translation contribute to performance.

### Strengths

1. **Clear problem motivation.** The paper addresses a practically important setting in which only a small number of labelled examples are available but unlabelled in-domain text can be used.
2. **Simple and implementable method.** CurCon is a modest modification to an established CERT-style pipeline and does not add inference-time parameters or complexity.
3. **Comprehensive baseline comparison.** The evaluation includes direct fine-tuning, UDA, SimCSE, and CERT, covering both supervised and self-/semi-supervised alternatives.
4. **Useful ablations.** The fixed-mixture, reversed-curriculum, and no-back-translation comparisons provide evidence that the schedule, rather than only the augmentation set, matters.
5. **Consistent empirical gains.** CurCon improves over CERT on all four datasets and shows larger gains in the most label-scarce setting.
6. **Good presentation.** The method, datasets, training pipeline, and main results are described clearly, and the paper is easy to follow.

### Weaknesses and questions

1. **Limited scope of evaluation.** The experiments cover only four English, relatively short-text datasets and one encoder family. Broader validation across domains, languages, longer documents, and more modern encoders would strengthen the conclusions.
2. **Potential baseline tuning imbalance.** CurCon is selected using a grid search on each validation set, whereas the baselines use hyperparameters from their original papers. For a fully controlled comparison, all methods should ideally receive comparable tuning budgets.
3. **Insufficient detail about augmentation sampling.** The curriculum specifies when operators become available, but the exact probability distribution over strengths and the handling of multiple views could be described more precisely. It would also help to report how often each operator is ultimately sampled.
4. **Unclear use of unlabelled data and validation data.** The paper should clarify whether validation examples are excluded from contrastive training and whether any preprocessing or back-translation process could expose information from test or validation sets.
5. **Statistical reporting could be stronger.** Results are averaged over five seeds, but confidence intervals or significance tests would make it easier to assess whether the relatively modest gains over CERT are robust.
6. **Ablation granularity.** The study removes back-translation but does not isolate the effects of each augmentation operator or compare alternative schedules with matched average augmentation strength. Such experiments would better establish why the curriculum works.
7. **Curriculum hyperparameter sensitivity.** Since curriculum length is selected by validation search, a sensitivity plot or performance breakdown across several values of \(L\) would help assess whether the method is robust or dependent on careful tuning.

These issues are primarily about strengthening experimental validation and reproducibility rather than undermining the central result. The reported improvements are consistent across tasks, and the main ablations support the proposed explanation.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 84/100 |
| Novelty | 75/100 |
| Significance | 80/100 |
| Clarity | 88/100 |

### Final average

\[
\frac{84 + 75 + 80 + 88}{4} = 81.75
\]

**Final average score: 81.75/100**

## Recommendation

**Accept**

The paper presents a clear, practically useful, and empirically supported improvement to contrastive intermediate training for low-resource classification. While the novelty is incremental and the evaluation would benefit from stronger tuning controls, statistical analysis, and broader datasets, the method is simple, the gains are consistent, and the ablations provide reasonable evidence that curriculum scheduling is beneficial. The limitations are appropriate for discussion in a final version and do not outweigh the contribution.