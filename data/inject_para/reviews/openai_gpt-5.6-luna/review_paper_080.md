## Overall assessment

This paper presents CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually expands the augmentation policy from relatively weak perturbations to stronger transformations during contrastive training, followed by standard supervised fine-tuning.

The experimental results are consistent and encouraging: CurCon improves over fine-tuning, UDA, SimCSE, and CERT across all four datasets, with an average gain of 1.1 points over CERT and larger gains in the lower-label regime. The ablations support the claim that both the curriculum direction and the inclusion of strong augmentations contribute to performance.

The main limitations are that the curriculum is relatively simple and hand-designed, the empirical scale is modest, and some implementation and fairness details require clarification. In particular, the curriculum is described as linear, but the actual operator availability changes at discrete thresholds; the comparison with baselines using their original hyperparameters may not be fully controlled; and the paper would benefit from more details about augmentation implementation, data splits, and statistical significance. These issues do not undermine the central contribution, however.

## Scores

| Criterion | Score |
|---|---:|
| **Soundness** | **84/100** |
| **Novelty** | **78/100** |
| **Significance** | **82/100** |
| **Clarity** | **88/100** |

### Final average

\[
\frac{84 + 78 + 82 + 88}{4} = \mathbf{83.0}
\]

## Strengths

1. **Clear and practically motivated method.** The approach is simple to integrate into existing contrastive intermediate-training pipelines and adds no inference-time parameters or cost.
2. **Consistent empirical improvements.** CurCon achieves the best result on all four reported datasets and improves over CERT by 1.1 average accuracy points.
3. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that the schedule itself, rather than only the augmentation set, contributes to the gains.
4. **Appropriate low-resource analysis.** The results with 100, 500, and 1,000 labels support the claim that the method is particularly useful when supervision is scarce.
5. **Good presentation.** The method, training pipeline, results, and limitations are described concisely and in a generally easy-to-follow manner.

## Weaknesses and requested clarifications

1. **The “linear” curriculum is not strictly linear.** The level \(c(t)\) increases linearly, but operators become available only at discrete thresholds and are then sampled uniformly. The paper should clarify whether the intended contribution is a continuous schedule of augmentation magnitude or a staged operator-availability schedule.
2. **Baseline tuning may not be fully comparable.** CurCon is selected using a 48-configuration grid search per dataset, whereas baselines use hyperparameters from their original papers. A fairer comparison would tune all methods under the same validation protocol or provide a sensitivity analysis.
3. **Limited scale of evaluation.** Four relatively short English benchmarks and one encoder architecture provide useful evidence, but broader testing would strengthen claims about generality.
4. **Statistical reporting could be expanded.** Five seeds are reasonable, but confidence intervals or paired significance tests would help establish whether the relatively small gains over CERT are statistically reliable.
5. **Implementation details are incomplete.** The paper should specify the back-translation model, treatment of failed or excessively short augmentations, exact tokenization and deletion behavior, and whether unlabeled data include the held-out validation/test text or only the permitted training corpus.
6. **Potential augmentation confounds.** The gains may partly reflect the inclusion of a stronger or more diverse augmentation mixture rather than the curriculum alone. Additional controls matching the number and frequency of each operator across schedules would make the curriculum claim more decisive.

## Recommendation

**Accept**

The paper offers a well-motivated and empirically supported improvement to contrastive intermediate training for low-resource classification. Although the novelty is incremental and several experimental details should be clarified, the method is simple, useful, and supported by consistent results and ablations. The issues identified are appropriate for clarification or revision rather than grounds for rejection.