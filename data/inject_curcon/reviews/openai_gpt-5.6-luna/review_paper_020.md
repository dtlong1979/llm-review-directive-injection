## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually increases the strength of text augmentations during contrastive pre-training, progressing from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations further suggest that both the curriculum direction and the inclusion of back-translation contribute to performance.

### Strengths

1. **Clear and practically motivated problem.** The focus on text classification with only a few hundred labels is important and relevant to realistic deployment settings.
2. **Simple and deployable method.** CurCon does not alter inference-time computation or require architectural modifications beyond the training projection head.
3. **Consistent empirical gains.** The method improves over CERT on all four datasets and provides an average gain of 1.1 percentage points over the strongest baseline.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that the scheduling direction, rather than merely the use of multiple augmentations, is important.
5. **Analysis across label regimes.** Results with 100, 500, and 1,000 labels support the claim that the method is especially helpful in lower-resource settings.
6. **Readable presentation.** The paper is well organized, and the method and experimental pipeline are straightforward to understand.

### Weaknesses and questions

1. **Baseline tuning may not be fully comparable.** CurCon hyperparameters are selected by dataset-specific grid search, whereas the baselines use hyperparameters from their original papers. For a rigorous comparison, all methods should ideally receive comparable validation-based tuning budgets.
2. **Limited dataset and model diversity.** The experiments use four relatively short English benchmarks and only BERT-base. It would strengthen the claims to include at least one larger encoder, a domain-specific dataset, or a non-English dataset.
3. **Schedule specification could be more precise.** The manuscript defines augmentation availability using thresholds but does not completely specify how the probability mass changes as the curriculum progresses. A formal probability equation or pseudocode would improve reproducibility.
4. **The role of individual augmentation operators is not fully isolated.** The ablation removes back-translation, but analogous ablations for token dropout, synonym replacement, and span deletion would clarify which components are essential.
5. **Statistical reporting could be expanded.** Five random seeds are useful, but confidence intervals or paired significance tests would help establish whether the relatively modest gains over CERT are statistically reliable.
6. **Potential resource and preprocessing concerns.** The cost analysis states that back-translated views are pre-computed, but the paper should report the translation model, preprocessing details, and total compute budget to make the efficiency comparison more reproducible.
7. **Some claims should be moderated.** The results support the effectiveness of the proposed curriculum on the evaluated benchmarks, but broader claims about general text classification would benefit from additional evidence.

### Soundness: 84/100

The central method is well specified at a high level, and the experimental evidence is internally consistent: CurCon improves over the listed baselines, the curriculum ablations support the proposed mechanism, and the label-count analysis is aligned with the motivation. The main soundness concern is fairness and completeness of the comparison, especially the asymmetric hyperparameter tuning and limited statistical analysis. These are important issues but are straightforward to address and do not undermine the core empirical result.

### Novelty: 78/100

The paper combines established ingredients—contrastive intermediate training, text augmentation, and curriculum learning—in a coherent and potentially useful way. The novelty lies primarily in applying a scheduled augmentation-strength curriculum to the contrastive intermediate-training stage for low-resource classification. This is a meaningful methodological contribution, although the conceptual distance from existing curriculum and augmentation-scheduling work is moderate rather than revolutionary. A clearer comparison with prior augmentation curricula and adaptive contrastive-learning schedules would better establish the contribution.

### Significance: 82/100

Low-resource classification is practically important, and the method is simple enough to be adopted without modifying inference. The consistent gains across four datasets and the larger benefit with fewer labels indicate practical value. The significance is somewhat limited by the relatively small benchmark suite and the absence of broader domain or multilingual evaluation, but the reported improvements are sufficiently consistent to make the work useful to researchers and practitioners working with limited supervision.

### Clarity: 89/100

The paper is well structured, concise, and easy to follow. The motivation, training pipeline, augmentation operators, and main findings are clearly presented. The main opportunities for improvement are to define the augmentation probabilities more formally, provide more implementation details, and clarify the experimental tuning protocol.

## Overall assessment

The paper presents a clear and useful method with consistent improvements over strong intermediate-training baselines. Although the empirical scope and baseline-tuning protocol should be strengthened, the issues are primarily matters of experimental completeness and reproducibility rather than fundamental flaws. The method is simple, the ablations support the central claim, and the results are relevant to low-resource classification.

**Final average score:**  
\[
\frac{84 + 78 + 82 + 89}{4} = 83.25
\]

### Final recommendation: **Accept**

The paper should be accepted, preferably conditional on clarifying the curriculum probability schedule, reporting more complete implementation and compute details, and discussing the fairness of baseline hyperparameter tuning.