## Review

### Summary
This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation strength during contrastive pretraining, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four classification benchmarks with 500 labelled examples show improvements over fine-tuning, UDA, SimCSE, and CERT, with supporting ablations and label-efficiency analysis.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 84/100 |
| Novelty | 78/100 |
| Significance | 83/100 |
| Clarity | 88/100 |
| **Final average** | **83.25/100** |

### Strengths

- The problem is practically important: exploiting unlabelled data under severe label scarcity.
- The proposed curriculum is simple, intuitive, and easy to implement within an existing CERT-style pipeline.
- The evaluation includes multiple datasets, several relevant baselines, multiple random seeds, ablations, and experiments with different numbers of labelled examples.
- The reported improvements are consistent across all four datasets and are largest in the most label-limited setting.
- The manuscript is clearly organized, and the method, schedule, experimental setup, and limitations are described concisely.
- The ablation comparing the forward curriculum, fixed-mixture training, and reversed curriculum provides useful evidence that the training schedule—not merely the set of augmentations—is contributing to performance.

### Weaknesses and suggestions

- The novelty is incremental: the main contribution combines established augmentation operators, contrastive intermediate training, and curriculum learning. The empirical validation is therefore particularly important.
- More detail would be useful concerning the exact sampling probabilities, the implementation of back-translation, preprocessing, and how unavailable or low-quality WordNet substitutions are handled.
- Baseline fairness could be strengthened by tuning all methods under comparable validation procedures rather than relying primarily on hyperparameters from prior work.
- Statistical significance tests or confidence intervals across seeds would provide stronger support for relatively small gains such as the 0.5-point improvement at 1,000 labels.
- The paper could clarify whether the unlabelled pool excludes the selected labelled examples and whether the validation data are used in any part of intermediate training.
- Additional comparisons against alternative curriculum schedules or augmentation-strength parameterizations would help isolate the effect of the linear schedule.

These are mostly presentation and experimental-completeness issues rather than fundamental flaws. The reported results are coherent, the ablations support the central claim, and the method appears useful for low-resource classification.

## Final recommendation

**Accept**

The paper presents a clear and practically relevant method with consistent empirical improvements and an appropriately scoped analysis. The contribution is somewhat incremental, but the curriculum design and supporting experiments provide sufficient value for acceptance.