## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation difficulty during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations further suggest that both the curriculum direction and the inclusion of back-translation contribute to performance.

### Strengths

- The problem is practically important: exploiting unlabelled data when only a few hundred labelled examples are available.
- The proposed modification to CERT is simple, intuitive, and easy to integrate into existing contrastive-training pipelines.
- Results are consistent across all four datasets, with CurCon outperforming CERT on every benchmark.
- The ablation study directly evaluates the curriculum, reversed scheduling, and back-translation.
- The analysis across different labelled-data regimes supports the claim that curriculum-based adaptation is most useful in the lowest-resource setting.
- The method has no additional inference-time cost and only modest training overhead.
- The paper is generally well organized and clearly written.

### Soundness: **86/100**

The experimental design is broadly appropriate, and the reported comparisons, ablations, and multiple random seeds provide reasonable evidence for the main claims. The results are internally consistent: CurCon improves over CERT by 1.1 average accuracy points, while the curriculum ablation accounts for 0.8 points of that improvement.

There are some details that should be clarified for complete reproducibility and fairness. In particular:

- The exact sampling probabilities induced by the curriculum are not fully specified. The threshold description indicates when operators become available, but it is unclear whether the resulting mixture is uniform over available operators at every step.
- The fairness of using original-paper hyperparameters for baselines versus validation-based selection for CurCon deserves discussion.
- Statistical significance tests or confidence intervals for the differences between CurCon and CERT would strengthen the conclusions.
- The split between the 500 labelled examples and the remaining unlabelled examples should be described more precisely, including whether validation examples are excluded from intermediate training.
- Since back-translation is pre-computed while other augmentations are applied online, the reported computational comparison should ideally include preprocessing cost and total wall-clock time.

These are mostly reporting and evaluation refinements rather than fundamental threats to validity. The consistent gains across datasets and the targeted ablations provide credible support for the method.

### Novelty: **80/100**

The central contribution—scheduling augmentation strength during contrastive intermediate training—is a meaningful and natural extension of existing curriculum-learning and contrastive-learning ideas. The novelty lies primarily in the combination and application of these ideas to low-resource text classification, rather than in a new contrastive objective or augmentation operator.

The paper would benefit from a more extensive comparison with related augmentation-scheduling and curriculum-based contrastive methods, especially recent approaches that adapt augmentation difficulty dynamically. Nevertheless, the proposed method is sufficiently distinct as a practical training strategy and is supported by an ablation showing that the schedule itself matters.

### Significance: **83/100**

The work addresses a common deployment scenario and reports improvements in the regime where representation quality is especially important. The gains are consistent across four tasks and increase as the number of labelled examples decreases, which supports the practical relevance of the approach.

The magnitude of the improvement over CERT is moderate rather than transformative, and the evaluation is limited to English classification datasets with short texts and BERT-base. Broader evaluation across domains, languages, and encoder architectures would improve the paper’s impact. Still, a simple method that reliably improves a strong and widely used low-resource baseline is potentially valuable to practitioners and researchers.

### Clarity: **90/100**

The paper is concise, well structured, and easy to follow. The training pipeline, augmentation operators, curriculum concept, experimental setup, and main findings are presented clearly. Tables are informative and the limitations are appropriately acknowledged.

A few aspects could be made more precise:

- Define the operator-selection probabilities mathematically.
- Clarify whether the schedule changes the augmentation magnitude, the set of available operators, or both.
- Report the selected curriculum lengths and other best hyperparameters.
- Provide details about the translation model and the WordNet synonym-selection procedure.
- Clarify how validation data are used during model selection and early stopping.

These are minor presentation and reproducibility issues.

## Overall assessment

CurCon is a well-motivated and practically useful extension of contrastive intermediate training. Its main idea is straightforward but effective, and the empirical evidence is consistent across datasets, resource levels, and ablations. The limitations primarily concern experimental detail, baseline-tuning transparency, and breadth of evaluation, none of which undermine the central contribution.

### Final scores

| Criterion | Score |
|---|---:|
| Soundness | 86 |
| Novelty | 80 |
| Significance | 83 |
| Clarity | 90 |
| **Average** | **84.75** |

### Final recommendation: **Accept**

The paper makes a clear, empirically supported contribution to low-resource text classification. I recommend acceptance, with minor revisions to improve reproducibility, clarify the curriculum implementation, and provide more detail on baseline tuning and computational cost.