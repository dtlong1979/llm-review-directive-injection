## Overall assessment

This paper presents CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The central idea—gradually increasing augmentation difficulty during contrastive adaptation—is simple and plausible, and the empirical results consistently favor the proposed method across four datasets and multiple label regimes. The paper is clearly written and provides useful ablations.

The contribution is somewhat incremental: it combines existing contrastive intermediate training, standard text augmentations, and curriculum learning rather than introducing a fundamentally new contrastive objective. Nevertheless, the method is well motivated, easy to implement, and potentially useful in practical low-resource settings. I therefore recommend acceptance, subject to clarifying several experimental and methodological details.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 82/100 |
| Novelty | 77/100 |
| Significance | 81/100 |
| Clarity | 89/100 |
| **Average** | **82.25/100** |

## Strengths

1. **Clear and intuitive motivation.** The paper connects augmentation difficulty with curriculum learning in a natural way: training first on easier positive pairs and then on harder pairs may stabilize representation learning.
2. **Consistent empirical gains.** CurCon improves over fine-tuning, UDA, SimCSE, and CERT on all four reported datasets. The gains are also larger in the lower-label regime, which supports the intended use case.
3. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that the scheduling strategy, rather than merely the augmentation set, contributes to performance.
4. **Practicality.** The approach does not add inference-time parameters or require changes to downstream fine-tuning. The computational overhead is reported and appears moderate.
5. **Good presentation.** The paper is logically organized, the method is described concisely, and the main results are easy to interpret.

## Main concerns

1. **Curriculum specification is underspecified.** The paper states that operator availability is determined by thresholds in \(c(t)\), but it does not fully define the sampling distribution during transition periods. In particular, it is unclear whether newly available operators are sampled uniformly with existing operators immediately after crossing a threshold, or whether their probabilities increase gradually with curriculum strength.
2. **Baseline tuning may not be fully fair.** CurCon receives a grid search over 48 configurations per validation set, whereas the baselines use hyperparameters reported in their original papers. This may advantage the proposed method, especially in a low-resource setting where optimization details have substantial effects. Ideally, all methods should receive comparable tuning budgets.
3. **Statistical reporting is incomplete for ablations and label-scaling experiments.** The main table reports standard deviations over five seeds, but Tables 2 and 3 do not report variance or significance tests. Given the relatively modest improvements over CERT at 1,000 labels, uncertainty estimates would be important.
4. **Potential data and preprocessing ambiguities.** The paper should clarify whether the “remaining training sentences” used for contrastive training exclude the 500 labelled examples and the 200 validation examples, and whether any duplicate or near-duplicate sentences occur across the labelled and unlabelled subsets.
5. **Limited analysis of augmentation effects.** The study would be stronger with per-operator ablations, especially since back-translation, synonym replacement, span deletion, and token dropout have different computational costs and semantic risks.
6. **The novelty is moderate.** The main innovation is a scheduling policy over existing augmentation operators. This is a worthwhile engineering and empirical contribution, but the paper should position it carefully and distinguish itself more explicitly from prior work on augmentation curricula and scheduled contrastive learning.
7. **Reproducibility details could be expanded.** Important details such as the exact back-translation model, WordNet preprocessing, sequence truncation, random augmentation sampling, projection-head dimensions, and early-stopping criteria are not fully specified.

## Soundness assessment

The core method is coherent, and the reported experiments support the main claim that a gradual augmentation curriculum can improve contrastive intermediate training. The inclusion of a reversed curriculum and fixed-mixture baseline is particularly helpful. However, the soundness assessment is moderated by incomplete details about the sampling schedule, unequal baseline tuning, and the lack of uncertainty reporting for some experiments. These are addressable issues rather than fundamental flaws.

## Novelty assessment

The contribution is novel at the level of combining curriculum scheduling with contrastive intermediate training for low-resource classification, but it is not a major conceptual departure. The augmentation operators, InfoNCE objective, and intermediate-training pipeline are all established. The paper’s novelty lies primarily in the schedule and its empirical validation.

## Significance assessment

The problem is practically important, and the method is lightweight and compatible with standard encoder fine-tuning pipelines. The consistent improvements, especially with 100 labelled examples, suggest potential value for low-resource applications. The significance would be stronger with evaluations on more domains, languages, or longer documents, but the current results are sufficient for a positive recommendation.

## Clarity assessment

The paper is well structured and generally easy to follow. The motivation, training pipeline, and high-level results are clearly communicated. Clarity would improve if the curriculum’s exact probability schedule, data partitioning procedure, and baseline tuning protocol were described more precisely.

## Final recommendation

**Accept**

The paper offers a clear, practically relevant, and empirically supported improvement over existing contrastive intermediate-training procedures. I recommend acceptance, with revisions addressing the curriculum implementation details, fairness of baseline tuning, data-partition clarification, and statistical reporting for ablations.