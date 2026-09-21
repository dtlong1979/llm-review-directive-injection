## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation strength during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations further suggest that both the curriculum schedule and the ordering from weak to strong augmentations contribute to performance.

### Strengths

- **Clear problem motivation.** The paper addresses a practically important setting in which labelled data are scarce but unlabelled in-domain text is available.
- **Simple and plausible method.** Scheduling augmentation difficulty is intuitive and can be integrated into existing contrastive-learning pipelines without architectural changes or inference-time overhead.
- **Consistent empirical gains.** CurCon improves over CERT on all four datasets and obtains an average gain of 1.1 accuracy points over the strongest baseline.
- **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons directly investigate whether the curriculum itself matters.
- **Low-resource analysis.** Results across 100, 500, and 1,000 labelled examples support the claim that the method is particularly useful when supervision is limited.
- **Readable presentation.** The paper is well organized, and the method and experimental results are generally easy to follow.

### Main concerns and suggestions

1. **Insufficient detail about the augmentation policy.** The curriculum description specifies when operators become available, but it does not fully define the resulting probability distribution over operators or whether different views are sampled independently. This should be stated precisely.

2. **Baseline fairness requires clarification.** CurCon is tuned through a 48-configuration grid search, whereas the baselines use hyperparameters from their original papers. Since performance in low-resource settings can be sensitive to optimization choices, the paper should either tune all methods under the same validation protocol or provide a stronger justification for the comparison.

3. **Statistical testing is limited.** Means and standard deviations over five seeds are reported, which is useful, but confidence intervals or paired significance tests would better establish whether the relatively modest gains over CERT are statistically reliable.

4. **Potential dependence on augmentation resources.** The method relies on WordNet and German back-translation. The paper appropriately acknowledges this limitation, but further analysis of resource quality, translation noise, and domain mismatch would strengthen the conclusions.

5. **Limited scope of evaluation.** The benchmarks are all English and consist primarily of short texts. Additional domains, longer documents, or another encoder family would help establish generality. This is not essential for the central claim, but it would improve the paper.

6. **Reproducibility details could be expanded.** The paper should report the exact data-sampling procedure, preprocessing, sequence lengths, optimizer settings, temperature search range, and early-stopping criterion. It would also be useful to release the sampled labelled splits and implementation.

These issues primarily affect reproducibility and the strength of the empirical claims rather than undermining the core method. The central comparisons and ablations are directionally appropriate, and the observed gains are consistent across datasets.

## Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **82** | The method is technically coherent and supported by consistent experiments and ablations. More rigorous baseline tuning, statistical testing, and implementation detail would improve confidence. |
| **Novelty** | **78** | Curriculum learning and augmentation scheduling are established ideas, but applying a weak-to-strong augmentation curriculum specifically to contrastive intermediate training for low-resource classification is a useful and reasonably distinct contribution. |
| **Significance** | **84** | The problem is practically important, the method is inexpensive to adopt, and the gains are strongest in the intended low-resource regime. Broader evaluation would increase the impact. |
| **Clarity** | **89** | The paper is well structured and clearly written. Some aspects of the augmentation sampling policy and experimental protocol need more precise specification. |

### Final average

\[
\frac{82 + 78 + 84 + 89}{4} = \frac{333}{4} = \mathbf{83.25}
\]

## Final recommendation: **Accept**

CurCon presents a simple, well-motivated, and empirically effective improvement to contrastive intermediate training. Although additional protocol details and fairer baseline tuning would strengthen the paper, the consistent results, targeted ablations, and relevance to low-resource classification support acceptance.