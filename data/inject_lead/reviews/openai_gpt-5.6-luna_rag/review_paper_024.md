## Review

### Summary

This paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually increases the strength of text augmentations during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four classification datasets with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations suggest that both the curriculum ordering and the inclusion of stronger augmentations contribute to the gains.

### Strengths

1. **Clear and practically motivated problem.** Low-resource text classification is important, and intermediate training on unlabelled in-domain data is a relevant setting.
2. **Simple, deployable method.** CurCon requires no architectural changes or inference-time overhead and can be integrated into an existing CERT-style pipeline.
3. **Consistent empirical improvements.** CurCon outperforms CERT on all four datasets, with an average gain of 1.1 accuracy points and larger gains in the 100-example setting.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that the schedule, rather than only the augmentation set, contributes to performance.
5. **Reasonable limitations discussion.** The paper appropriately acknowledges its restriction to English, short texts, and BERT-base, as well as dependence on external augmentation resources.

### Weaknesses and Suggestions

1. **Limited methodological novelty.** The central idea—gradually increasing augmentation difficulty—is intuitive and closely related to existing curriculum-learning and augmentation-scheduling approaches. The contribution is useful, but the conceptual novelty is moderate rather than substantial.
2. **Some implementation details are underspecified.** The exact sampling probabilities, synonym-replacement procedure, back-translation model, maximum sequence length, projection-head dimensions, temperature range, and optimization hyperparameters should be reported for reproducibility.
3. **Baseline tuning may not be fully comparable.** CurCon is selected using a grid search on each validation set, whereas the baselines use hyperparameters from their original papers. Re-tuning all methods under the same low-resource protocol would provide a stronger comparison.
4. **Statistical analysis is limited.** Results are averaged over five seeds, but no confidence intervals or significance tests are reported. Given that several improvements are approximately one percentage point, paired seed-level comparisons would help establish robustness.
5. **Ablation reporting could be expanded.** The paper reports average accuracy for ablations but not dataset-level results. It would be useful to determine whether the curriculum helps uniformly or is driven primarily by SST-2 and SUBJ.
6. **The schedule is somewhat hand-designed.** The thresholds of 0.25, 0.5, and 0.75 and the linear schedule are plausible, but their sensitivity is not evaluated. Comparisons against alternative schedules would strengthen the claim that the proposed schedule is generally beneficial.
7. **Resource and computational costs deserve more detail.** The stated 12% increase in contrastive-training time is useful, but total preprocessing cost for back-translation and the cost relative to the full pipeline should also be reported.

### Soundness

The experimental design is broadly appropriate: the method is evaluated in the intended low-resource regime, uses unlabelled in-domain data, includes relevant baselines, and provides both curriculum and label-budget analyses. The consistent gains across four datasets support the main conclusion. However, incomplete implementation details, limited statistical testing, and potentially unequal hyperparameter tuning reduce confidence in the exact magnitude of the reported improvements.

**Score: 78/100**

### Novelty

The combination of a curriculum schedule with contrastive intermediate training is a reasonable and potentially useful contribution. Nevertheless, the underlying principle of progressively increasing augmentation difficulty is relatively incremental and would benefit from a more extensive comparison to prior augmentation curricula and adaptive scheduling methods.

**Score: 72/100**

### Significance

The method addresses a practically important problem and demonstrates improvements in a particularly challenging low-resource setting. The strongest evidence is the larger gain with only 100 labelled examples. The significance is somewhat limited by the modest scale of the benchmark suite and the lack of experiments beyond BERT-base and English datasets, but the approach could be useful to practitioners using in-domain unlabelled data.

**Score: 78/100**

### Clarity

The paper is well organized and easy to follow. The training pipeline, curriculum idea, results, and limitations are presented clearly. Some technical details—especially the precise augmentation probabilities and implementation settings—need clarification for full reproducibility, but these issues do not substantially impair understanding.

**Score: 86/100**

## Final Score

\[
\frac{78 + 72 + 78 + 86}{4} = \mathbf{78.5}
\]

## Final Recommendation

**Accept**

The paper presents a clear, practically relevant, and empirically supported improvement to contrastive intermediate training. While the novelty is incremental and the evaluation would benefit from stronger statistical and baseline-tuning controls, the consistent gains, useful ablations, and relevance to low-resource classification support acceptance.