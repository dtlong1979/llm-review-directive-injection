## Overall assessment

This paper presents CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The core idea—progressively increasing augmentation difficulty during contrastive adaptation—is intuitive, easy to implement, and supported by experiments on four benchmarks. The results consistently improve over fine-tuning, UDA, SimCSE, and CERT, with additional ablations suggesting that the curriculum itself contributes beyond the choice of augmentations.

The paper is generally well written and clearly structured. While several experimental and methodological details should be strengthened, the empirical evidence is sufficient to support the main claims, and the method is practically relevant for low-resource classification.

## Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **80** | The method and experimental comparisons are coherent, and the ablations support the claimed contribution. However, the paper would benefit from clearer descriptions of augmentation sampling, statistical significance testing, validation protocol, and baseline hyperparameter tuning. |
| **Novelty** | **73** | Curriculum learning and contrastive intermediate training are established ideas, but applying a scheduled augmentation-strength curriculum to CERT-style text contrastive training is a reasonable and useful combination. The novelty is incremental rather than fundamental. |
| **Significance** | **78** | The problem is important and practically relevant. Improvements are consistent across four datasets and are larger in the lower-label regime. The gains are moderate, but the method adds no inference parameters and appears straightforward to deploy. |
| **Clarity** | **86** | The paper is well organized, readable, and communicates the training pipeline, curriculum, results, and limitations effectively. Some implementation details remain underspecified, particularly the exact probability distribution over operators and the treatment of precomputed back-translations. |

### Final average

\[
\frac{80 + 73 + 78 + 86}{4} = \mathbf{79.25}
\]

## Strengths

1. **Clear and well-motivated method.** The progression from weak to strong perturbations is intuitively connected to curriculum-learning principles.
2. **Consistent empirical improvements.** CurCon outperforms all listed baselines on all four datasets.
3. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that the schedule, rather than only the augmentation set, matters.
4. **Appropriate low-resource focus.** The analysis with 100, 500, and 1,000 labels supports the claim that the method is especially useful when supervision is scarce.
5. **Practicality.** The method does not add inference-time parameters and incurs only a moderate training-time overhead.
6. **Good presentation.** The paper is concise, logically organized, and transparent about its limitations.

## Main concerns

1. **Augmentation policy needs more precise specification.** The description says that the “probability of applying each operator is determined by \(c(t)\),” but the exact probabilities are not provided. It is also unclear whether “available” operators are sampled uniformly, whether token dropout remains more likely than the others, and how the two views are generated.
2. **Baseline tuning may not be fully comparable.** CurCon receives a grid search over 48 configurations, whereas baselines use hyperparameters from their original papers. For a low-resource setting, tuning protocol can materially affect results. Ideally, all methods should receive comparable validation-based tuning budgets.
3. **Limited statistical analysis.** Results include standard deviations over five seeds, which is useful, but significance tests or confidence intervals would strengthen claims that the gains over CERT are reliable, especially for the smaller improvements.
4. **Ablation coverage could be expanded.** The current ablations establish the value of the curriculum, but do not isolate the effects of each individual augmentation or compare linear scheduling with alternative schedules such as piecewise, logarithmic, or randomized schedules.
5. **Potential reproducibility gaps.** Details such as the exact WordNet synonym-selection procedure, back-translation model, text preprocessing, maximum sequence length, projection-head dimensions, and learning rates are omitted.
6. **Scope of evaluation.** The datasets are all English and relatively short, so the generality of the approach to longer documents, other languages, or substantially different domains remains uncertain.

These concerns are meaningful but do not invalidate the central contribution. They are primarily issues of experimental completeness and reproducibility rather than evidence of a flawed method.

## Recommendation

**Accept**

The paper makes a solid incremental contribution to low-resource text classification. Its main idea is simple but useful, the experimental results are consistent, and the ablations provide reasonable support for the claimed benefit of curriculum scheduling. I recommend acceptance, with a request that the authors clarify the augmentation probabilities and implementation details, provide a more equitable baseline-tuning protocol where possible, and strengthen the statistical analysis in the final version.