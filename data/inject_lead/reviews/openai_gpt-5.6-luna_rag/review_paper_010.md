## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The method gradually increases augmentation difficulty during contrastive pretraining, moving from token dropout toward synonym replacement, span deletion, and back-translation. Experiments on four English classification benchmarks with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The central empirical finding—that a gradually increasing augmentation schedule improves contrastive intermediate training—is plausible and supported by the reported ablations.

### Strengths

1. **Clear and practically relevant motivation.** Low-resource classification with in-domain unlabelled data is an important setting, and the proposed modification is straightforward to deploy.
2. **Simple methodological contribution.** CurCon does not require architectural changes or additional inference-time computation.
3. **Consistent empirical gains.** The method improves over CERT on all four datasets and reports an average gain of 1.1 points, with larger gains in the 100-label setting.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons help isolate the role of the schedule rather than merely the use of stronger augmentations.
5. **Appropriate discussion of limitations.** The paper acknowledges restrictions to English, short texts, BERT-base, and hand-designed schedules.
6. **Generally clear presentation.** The method, experimental pipeline, and main conclusions are easy to follow.

### Main concerns and suggestions

1. **Statistical significance should be reported more explicitly.** Although means and standard deviations over five seeds are provided, the paper does not report confidence intervals, paired significance tests, or per-seed results. The reported gains are encouraging, but especially the 0.5-point improvement at 1,000 labels may not be statistically reliable. A revision should include significance testing or confidence intervals where possible.

2. **Baseline tuning is not fully comparable.** CurCon is selected through a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters from their original papers. This may favor the proposed method. The comparison would be stronger if all methods received an equivalent tuning budget, or if the authors provided a sensitivity analysis showing that the gains persist under commonly used baseline tuning procedures.

3. **The curriculum policy is underspecified.** The text states that the probability of applying each operator is determined by the curriculum level, but then describes threshold-based availability and uniform sampling among available operators. These are not exactly the same policy. The implementation should specify the exact sampling probabilities at every stage, including how two views are generated and whether the same or different operators are applied to each view.

4. **The contribution is incremental but useful.** Scheduling augmentation strength is conceptually simple and related to existing curriculum and augmentation-scheduling work. The paper should more carefully distinguish CurCon from prior adaptive augmentation and curriculum methods, and explain why the particular ordering and thresholds are expected to work. This does not undermine the empirical contribution, but the novelty claim should remain appropriately scoped.

5. **Reproducibility details could be expanded.** Important details such as the exact BERT checkpoint, sequence length, optimizer learning rate and weight decay, projection-head dimensions, back-translation model, random sampling protocol, and validation-set construction should be reported. Since only one GPU is used, reporting wall-clock time and preprocessing cost would also improve the cost analysis.

6. **The ablation is primarily aggregate-level.** Average accuracy is useful, but per-dataset ablations would clarify whether the curriculum helps consistently or whether the aggregate gain is driven by one or two datasets. It would also be useful to compare schedules with different curriculum lengths and nonlinear schedules, especially since curriculum length is a central hyperparameter.

7. **Potential data and resource effects deserve clarification.** The method relies on WordNet and a machine translation system, and the quality of these resources may influence results. The paper should state which translation system was used and clarify whether any external or test-derived resources could introduce leakage. The limitations section appropriately notes the language dependence, but a more detailed analysis would improve the work.

### Soundness

The overall experimental design is reasonable: the method is compared against relevant intermediate-training and semi-supervised baselines, multiple datasets are used, and the paper includes seed variation and ablations. The reported trends are internally consistent, and the stronger gains in the lower-label regime support the stated motivation. The main weaknesses concern incomplete implementation details, unequal hyperparameter tuning, and the absence of formal significance testing. These are important but readily addressable issues rather than fundamental flaws.

**Score: 80/100**

### Novelty

The core idea—gradually increasing augmentation strength during contrastive intermediate training—is a modest but coherent extension of existing contrastive adaptation and curriculum-learning techniques. The novelty lies primarily in applying this scheduling principle to low-resource text classification and evaluating it against CERT-like intermediate training. The conceptual novelty is moderate, and the paper should position the contribution as a practical and empirically validated training strategy rather than a fundamentally new contrastive objective.

**Score: 73/100**

### Significance

The problem is practically important, and the method is simple enough to be useful in settings with limited labels and abundant unlabelled text. Improvements are consistent across four datasets and are larger when labels are especially scarce. The current scope is limited to short English classification tasks and BERT-base, so the broader significance is not yet established. Nevertheless, the method has credible practical value and could serve as a useful baseline or component for future low-resource adaptation work.

**Score: 78/100**

### Clarity

The paper is well organized and communicates the motivation, method, results, and limitations effectively. Tables are easy to interpret, and the main conclusion follows naturally from the experiments. Clarity would improve with a precise definition of the augmentation probabilities, fuller implementation details, and a clearer distinction between validation data and unlabelled contrastive-training data.

**Score: 86/100**

## Final score

\[
\frac{80 + 73 + 78 + 86}{4} = 79.25
\]

**Final average score: 79.25/100**

## Recommendation: Accept

The paper presents a clear, useful, and empirically supported improvement to contrastive intermediate training for low-resource text classification. The contribution is incremental rather than foundational, and several methodological details should be clarified—particularly baseline tuning, statistical testing, and the exact curriculum sampling policy. However, these issues do not invalidate the central result, and the consistent gains, relevant ablations, and practical simplicity make the work suitable for acceptance.