## Review

### Summary
This paper introduces CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The method gradually increases augmentation difficulty during contrastive pretraining, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations further suggest that the curriculum schedule itself contributes to the gains.

### Strengths
- Addresses an important and practically relevant setting: text classification with very limited labelled data.
- The proposed method is simple, intuitive, and compatible with standard contrastive intermediate-training pipelines.
- The curriculum idea is well motivated and supported by comparisons with a fixed augmentation mixture and a reversed curriculum.
- Results are consistent across all four datasets and random seeds.
- The paper includes useful analyses across different labelled-data regimes and reports computational cost.
- The method introduces no inference-time overhead and only modest training-time overhead.

### Soundness: **86/100**
The methodology is coherent, the experimental design includes multiple datasets, several baselines, five random seeds, and relevant ablations. The reported results support the central claim that gradually increasing augmentation strength can improve contrastive intermediate training.

Some implementation details could be clarified, particularly how operator probabilities vary continuously with the curriculum level and how the fixed-mixture baseline is matched in terms of augmentation frequency and compute. The baseline hyperparameter selection procedure could also be made more comparable, since CurCon is tuned through a per-dataset grid search while baseline settings are taken from prior work. These are relatively minor concerns and do not undermine the main conclusions.

### Novelty: **78/100**
The core contribution—scheduling augmentation strength during contrastive intermediate training—is a meaningful and reasonably distinct application of curriculum learning to text contrastive adaptation. The individual augmentation operators and the CERT-style pipeline are not new, but their scheduled combination is clearly formulated and experimentally isolated.

The novelty is moderate rather than groundbreaking, since curriculum learning and augmentation scheduling have been explored in adjacent settings. Nevertheless, the paper identifies a relevant gap and provides a useful, simple method for low-resource text classification.

### Significance: **82/100**
The problem is important, and the method obtains consistent improvements over strong and relevant baselines. The gains are especially compelling in the 100-example setting, where CurCon improves over CERT by 1.6 points. The method is straightforward to implement and has no inference cost, increasing its practical value.

The significance is somewhat limited by the relatively small benchmark suite, short English texts, and use of a single encoder family. Broader multilingual, domain-specific, or larger-model evaluations would better establish generality. Still, the current results provide a convincing demonstration of value.

### Clarity: **90/100**
The paper is well organized and easy to follow. The motivation, training pipeline, curriculum definition, baselines, and empirical findings are presented clearly. Tables directly support the central claims, and the limitations section appropriately identifies the main scope constraints.

A few details warrant additional precision, including the exact sampling probabilities under the curriculum, the implementation of back-translation and precomputation, and the validation protocol. These clarifications would improve reproducibility but do not materially affect readability.

### Overall assessment
CurCon is a clear and empirically supported contribution. Its main idea is simple but useful, and the experimental evidence indicates that the curriculum—not merely the use of stronger augmentations—contributes to the improvement. While the novelty and scope are moderate, the paper meets the standard for acceptance due to its sound methodology, consistent gains, practical relevance, and clear presentation.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 86 |
| Novelty | 78 |
| Significance | 82 |
| Clarity | 90 |
| **Final average** | **84.0** |

## Final recommendation: **Accept**