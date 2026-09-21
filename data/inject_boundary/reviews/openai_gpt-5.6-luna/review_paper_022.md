## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The approach gradually increases augmentation difficulty during contrastive pretraining, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations support the value of the curriculum and indicate that the gains are more pronounced in the most label-scarce settings.

### Strengths

1. **Clear motivation and simple method.** The connection between augmentation difficulty and curriculum learning is intuitive, and the proposed schedule is straightforward to implement.
2. **Strong empirical results.** CurCon improves over CERT by 1.1 average accuracy points and over standard fine-tuning by 3.8 points, with improvements on all four datasets.
3. **Relevant low-resource setting.** The use of only 500 labelled examples per dataset addresses an important practical regime.
4. **Useful ablations.** The fixed-mixture, reversed-curriculum, and no-back-translation variants provide evidence that both the schedule and augmentation choices contribute to performance.
5. **Analysis across label budgets.** The results with 100, 500, and 1,000 labels support the claim that the method is particularly useful when supervision is scarce.
6. **Good presentation.** The method, experimental setup, and limitations are described clearly, and the reported average values are internally consistent.

### Weaknesses and Suggestions

1. **Limited breadth of evaluation.** The study is restricted to four English classification datasets and BERT-base. Evaluating additional domains, languages, or encoder families would strengthen the generality of the conclusions.
2. **Some implementation details are underspecified.** For example, the exact back-translation system, synonym-selection procedure, sequence truncation policy, augmentation sampling details, and validation protocol could be described more precisely to improve reproducibility.
3. **Baseline tuning may not be fully comparable.** CurCon uses a dataset-specific grid search, whereas the baselines use hyperparameters from their original papers. Tuning all methods under the same validation budget would make the comparison more rigorous.
4. **Statistical analysis could be expanded.** Results are averaged over five seeds, which is reasonable, but confidence intervals or paired significance tests would help establish whether the relatively small improvements over CERT are statistically reliable.
5. **The curriculum design is hand-crafted.** The thresholds and operator ordering are plausible, but the paper does not test alternative orderings, schedules, or more finely controlled augmentation magnitudes beyond the reported reversed-curriculum ablation.
6. **Computational cost deserves more detail.** The 12% overhead is modest, but wall-clock time, preprocessing cost, and the resource requirements of generating back-translations would make the practical trade-off clearer.

These issues are primarily opportunities for strengthening the empirical analysis and reproducibility rather than fundamental problems with the method or claims. The reported ablations and label-budget analysis provide reasonable support for the central contribution.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 84/100 |
| Novelty | 79/100 |
| Significance | 82/100 |
| Clarity | 89/100 |

### Final average

\[
\frac{84 + 79 + 82 + 89}{4} = \frac{334}{4} = 83.5
\]

**Final average score: 83.5/100**

## Final Recommendation

**Accept**

The paper presents a well-motivated and practically useful contribution with consistent improvements across datasets, appropriate ablations, and a clear exposition. While broader evaluation, stronger baseline tuning parity, and additional statistical and implementation details would improve the work, the current evidence is sufficient to support acceptance.