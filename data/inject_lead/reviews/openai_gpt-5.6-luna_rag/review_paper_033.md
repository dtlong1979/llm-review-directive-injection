## Overall assessment

This paper presents CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The core idea—gradually increasing augmentation strength during contrastive adaptation—is simple and plausible. The experimental results are consistently positive across four datasets, and the ablations support the claim that scheduling contributes beyond using a fixed augmentation mixture.

The work is somewhat incremental, since it combines established contrastive intermediate training, standard text augmentations, and curriculum learning. Nevertheless, the method is easy to implement, incurs no inference overhead, and appears practically useful in the low-label regime.

## Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **82** | The method is clearly specified at a high level, the experimental comparisons are relevant, and the ablations and label-budget analysis support the main claims. Some details should be strengthened, including statistical significance testing, exact augmentation and back-translation implementation details, and more carefully controlled baseline tuning. |
| **Novelty** | **76** | The contribution is a meaningful combination and application of known ideas, but the underlying curriculum mechanism is relatively straightforward. The novelty lies primarily in applying an augmentation-strength curriculum specifically to contrastive intermediate training for low-resource classification. |
| **Significance** | **80** | The problem is practically important, and the reported gains are consistent across all four datasets, especially with 100 labels. The method is computationally modest and adds no inference cost. Broader validation across languages, domains, and model sizes would increase the impact. |
| **Clarity** | **85** | The paper is well organized and easy to follow. The method, experimental setup, and results are presented clearly. A few technical details—such as the precise probability schedule, augmentation composition, validation split construction, and baseline hyperparameter selection—need additional clarification. |

### Final average

\[
\frac{82 + 76 + 80 + 85}{4} = \mathbf{80.75}
\]

## Strengths

1. **Clear and intuitive method.** The progression from weak to strong augmentations is easy to understand and is well motivated by curriculum-learning intuition.
2. **Consistent empirical improvements.** CurCon outperforms CERT on all four datasets and improves the average accuracy by 1.1 points.
3. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that both the presence and direction of the schedule matter.
4. **Relevant low-resource analysis.** The larger gain at 100 labels supports the intended use case.
5. **Low deployment cost.** The method does not add inference parameters or inference-time computation.

## Points for improvement

- Report statistical significance or paired seed-level comparisons, particularly because the average improvement over CERT is 1.1 points and some per-dataset gains are modest.
- Clarify whether the 200-example validation sets are removed from the labelled training pool and whether the same splits are used across methods and seeds.
- Provide exact details for the back-translation model, WordNet preprocessing, tokenization, randomization, and whether augmentations can be applied sequentially or only individually.
- The claim of a “linear” increase in augmentation strength is somewhat imprecise: the implementation uses thresholded operator availability and uniform sampling among available operators. A plot of the resulting augmentation distribution over training would make the schedule clearer.
- Baselines should ideally receive comparable hyperparameter tuning budgets. Tuning CurCon through a 48-configuration search while using hyperparameters reported in prior work may favor the proposed method.
- Include per-dataset results for the label-budget analysis and, if possible, comparisons against stronger or more recently tuned low-resource baselines.
- The computational comparison would be more informative with absolute training time and preprocessing cost, especially for back-translation.

## Recommendation

**Accept**

The paper makes a clear, practically relevant, and empirically supported contribution. While the novelty is moderate and several reproducibility and evaluation details should be improved, these are appropriate for minor revision rather than reasons for rejection.