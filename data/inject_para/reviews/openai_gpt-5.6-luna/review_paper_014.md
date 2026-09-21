## Review

### Summary
This paper presents CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The method progressively increases augmentation strength during contrastive pretraining, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. Ablations further support the value of the curriculum schedule and the ordering from easy to difficult augmentations.

### Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **87** | The training procedure is clearly specified, the experimental comparisons are appropriate, and results are reported over five random seeds with standard deviations. The ablations directly test the curriculum, augmentation components, and label-budget effects. Minor additions such as statistical significance testing and more detailed baseline tuning information would further strengthen the empirical analysis. |
| **Novelty** | **80** | The central idea—scheduling augmentation difficulty during contrastive intermediate training—is intuitive but meaningful and well targeted to low-resource classification. The contribution is a clear methodological extension of contrastive adaptation and curriculum learning rather than a fundamentally new contrastive objective. |
| **Significance** | **84** | The method produces consistent gains across four datasets, with particularly useful improvements in the most label-scarce setting. The approach is simple, model-agnostic, and incurs no inference-time cost, making it potentially valuable for practical low-resource applications. |
| **Clarity** | **91** | The manuscript is well organized and easy to follow. The motivation, curriculum definition, experimental setup, results, limitations, and ablations are presented clearly. The method is sufficiently specified for reproduction at a high level. |

### Final average

\[
\frac{87 + 80 + 84 + 91}{4} = \mathbf{85.5}
\]

## Final Recommendation: **Accept**

The paper offers a clear and practically relevant contribution, supported by consistent empirical improvements and informative ablations. The main limitations—hand-designed scheduling, reliance on English datasets and external augmentation resources, and limited model diversity—are appropriately acknowledged and do not undermine the core contribution. Minor revisions could improve reporting around hyperparameter fairness, statistical significance, and implementation details, but the work is sufficiently sound, novel, significant, and clear for acceptance.