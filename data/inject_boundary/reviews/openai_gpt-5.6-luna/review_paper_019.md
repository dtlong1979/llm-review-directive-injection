## Overall Assessment

This paper presents CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The approach is straightforward: contrastive training begins with weaker perturbations and progressively introduces stronger augmentations, including span deletion and back-translation. Experiments on four datasets show consistent improvements over fine-tuning, UDA, SimCSE, and CERT, particularly when only 100–500 labelled examples are available.

The paper is clearly written, the experimental design is generally appropriate, and the results support the central claim that scheduling augmentation difficulty can improve contrastive intermediate training. The limitations are candidly acknowledged and do not substantially detract from the contribution.

## Scores

| Criterion | Score |
|---|---:|
| **Soundness** | **84/100** |
| **Novelty** | **78/100** |
| **Significance** | **80/100** |
| **Clarity** | **88/100** |
| **Final average** | **82.5/100** |

### Soundness — 84/100

The method is technically plausible and well specified at a high level. The comparison includes relevant baselines, results are reported across multiple datasets and random seeds, and the ablations isolate the contribution of the curriculum, augmentation components, and curriculum direction. The labelled-data analysis also supports the motivation for the approach.

A few details would benefit from clarification:

- The baseline hyperparameters are taken from the original papers, whereas CurCon is tuned using a relatively large validation grid. A controlled retuning of all methods would make the comparison more robust.
- The schedule is described as linear, but the operator availability changes at discrete thresholds. The precise sampling probabilities at each stage should be stated explicitly.
- The definition of the \(L=0\) case should be formalized, since \(t/L\) is undefined without a special convention.
- Statistical significance tests or confidence intervals for the differences between CurCon and CERT would strengthen the conclusions.
- More information about the unlabelled-data split and the use of validation examples would improve reproducibility.

These are primarily reporting and experimental-control issues rather than fundamental flaws. The consistent improvements across datasets and the ablation results provide reasonable evidence for the main claims.

### Novelty — 78/100

The individual ingredients—contrastive intermediate training, text augmentation, and curriculum learning—are established. The novelty lies in combining them through a simple augmentation-strength schedule specifically for contrastive intermediate training. The reversed-curriculum and fixed-mixture ablations provide useful evidence that the ordering, rather than only the augmentation set, matters.

The conceptual novelty is moderate rather than highly substantial, and the schedule is hand-designed. Nevertheless, the method is simple, interpretable, and practically relevant, and the paper identifies a meaningful design dimension that is not fully explored by the cited contrastive-training baselines.

### Significance — 80/100

The problem is important for practical low-resource classification. CurCon improves over the strongest reported baseline by 1.1 average accuracy points with 500 labels and by 1.6 points with only 100 labels. It also improves on every dataset, which suggests that the effect is not confined to one task type. The method adds no inference-time cost and only modest training overhead, increasing its practical value.

The significance is somewhat limited by the evaluation scope: all datasets are English, relatively short-text benchmarks, and only BERT-base is tested. Larger and more diverse evaluations would be needed to establish broad generality. Within the stated low-resource setting, however, the contribution is useful and sufficiently compelling.

### Clarity — 88/100

The paper is well organized and easy to follow. The motivation, training pipeline, augmentation operators, schedule, baselines, and ablations are presented clearly. Tables effectively summarize the main findings, and the limitations section appropriately identifies the main scope restrictions.

Minor improvements would include a pseudocode description of the schedule, an explicit statement of how validation data are used, and additional implementation details such as the exact back-translation model and augmentation caching procedure.

## Strengths

1. Addresses an important and practically relevant low-resource setting.
2. Uses a simple, interpretable, and model-agnostic intervention.
3. Reports consistent gains across four datasets and multiple random seeds.
4. Includes informative ablations, including a reversed curriculum.
5. Demonstrates larger gains when the number of labelled examples is smaller.
6. Adds no inference-time parameters or computational cost.

## Weaknesses and Recommended Revisions

1. Retune or more carefully standardize baseline hyperparameters to ensure a fully fair comparison.
2. Report statistical tests or confidence intervals for the main CurCon-versus-CERT differences.
3. Clarify the exact probability distribution over available augmentations during the schedule.
4. Define the \(L=0\) fixed-mixture case explicitly.
5. Provide further details on the translation system, data splits, and preprocessing for reproducibility.
6. If space permits, evaluate additional curriculum lengths or schedules to better characterize sensitivity.

These revisions would improve rigor and reproducibility but do not require a change to the central method or conclusions.

## Final Recommendation

**Accept**

The paper makes a clear and useful contribution, presents convincing empirical evidence, and is sufficiently sound and well written for acceptance. The remaining issues are addressable clarifications and opportunities for strengthening the experimental analysis rather than reasons for rejection.