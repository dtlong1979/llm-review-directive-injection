## Overall assessment

This paper presents CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method progressively increases augmentation difficulty during contrastive adaptation, moving from token dropout toward synonym replacement, span deletion, and back-translation. Experiments on four standard datasets show consistent improvements over fine-tuning, UDA, SimCSE, and CERT, with particularly strong gains in the lowest-label regime.

The paper is clearly written, the experimental design is generally appropriate, and the ablations support the central claim that scheduling augmentation difficulty is beneficial. The improvements are modest but consistent across all four datasets and are most relevant in precisely the low-resource setting targeted by the work.

### Strengths

- Addresses a practically important problem: classification with very limited labelled data.
- The proposed modification is simple, model-agnostic, and incurs no inference-time cost.
- CurCon outperforms all reported baselines on every dataset.
- The ablations compare fixed, forward, and reversed curricula, providing evidence that the ordering—not merely the presence—of augmentations matters.
- The label-budget analysis supports the claim that the method is most useful when supervision is scarce.
- The limitations are appropriately acknowledged, particularly the reliance on English datasets and external augmentation resources.
- The paper is well organized and easy to follow.

### Weaknesses and questions

1. **Baseline tuning fairness.** CurCon is selected using a grid search over 48 configurations, whereas the baselines use hyperparameters reported in their original papers. This may give CurCon an optimization advantage, especially in a low-resource setting. A stronger comparison would tune all methods under the same validation protocol.

2. **Statistical testing.** Results are reported over five seeds, which is useful, but the paper does not provide confidence intervals or significance tests. Given that some gains over CERT are approximately 0.5–1.5 points, formal testing would help establish their robustness.

3. **Schedule specification.** The description of how operator probabilities vary with the curriculum level is somewhat underspecified. The availability thresholds are clear, but it is not fully explained whether the probability of token dropout decreases as other operators become available or whether all available operators are sampled uniformly throughout.

4. **Augmentation comparability.** The four augmentations may differ substantially in semantic preservation and computational cost. More detailed analysis of individual operators, their actual perturbation rates, and their interaction with sentence length would strengthen the interpretation of the curriculum effect.

5. **Scope of evaluation.** The evaluation is limited to four English datasets and BERT-base. This is a reasonable initial scope, but broader model and language coverage would be needed to establish generality.

These issues reduce the strength of the claims somewhat, but they do not undermine the main empirical conclusion. The consistent improvements, the reverse-curriculum comparison, and the label-efficiency results provide sufficient support for the proposed method.

## Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **78** | The method and experiments are coherent, and the ablations support the central claim. The absence of uniformly tuned baselines and formal significance testing limits certainty but does not invalidate the results. |
| **Novelty** | **76** | Curriculum-based augmentation is an intuitive extension of existing contrastive intermediate training, but applying it systematically to text contrastive adaptation and comparing forward, fixed, and reversed schedules provides a useful contribution. |
| **Significance** | **79** | The problem is important, and the gains are consistent, particularly at 100 labelled examples. The contribution is likely useful to practitioners, although the absolute improvements are moderate and the evaluation scope is limited. |
| **Clarity** | **86** | The paper is well structured and readable. The method, experimental setup, and limitations are presented clearly, with only minor ambiguity in the precise operator-probability schedule. |

### Final average score

\[
\frac{78 + 76 + 79 + 86}{4} = \frac{319}{4} = \mathbf{79.75}
\]

## Final recommendation: **Accept**

The paper makes a clear and useful contribution to low-resource text classification. While additional baseline tuning, significance analysis, and schedule details would improve the work, the method is simple, empirically effective, and supported by consistent cross-dataset results and informative ablations. These concerns are appropriate for discussion or revision but are not sufficient to warrant rejection.