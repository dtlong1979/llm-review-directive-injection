## Overall assessment

This paper presents CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The approach progressively expands the augmentation policy from token dropout to stronger transformations, including back-translation, before supervised fine-tuning. Experiments on four benchmarks with 500 labelled examples show consistent gains over fine-tuning, UDA, SimCSE, and CERT, with additional ablations supporting the value of the curriculum.

### Strengths

- **Clear motivation:** The paper identifies a meaningful limitation of fixed augmentation policies in contrastive intermediate training.
- **Simple and practical method:** CurCon requires no architectural changes or inference-time overhead and can be incorporated into the CERT pipeline.
- **Consistent empirical gains:** The method improves over CERT on all four datasets and reports gains across multiple label regimes.
- **Useful ablations:** The fixed-mixture and reversed-curriculum comparisons provide evidence that both the curriculum and its direction matter.
- **Appropriate low-resource evaluation:** Testing with 100, 500, and 1,000 labelled examples demonstrates that the benefit is particularly relevant in the intended setting.
- **Good presentation:** The method, datasets, baselines, and main results are described clearly, and the tables make the central claims easy to verify.

### Weaknesses and questions

- The curriculum definition could be made more precise. The method is described as linearly increasing augmentation strength, but the actual policy uses thresholded operator availability and fixed operator magnitudes. A formal description of the resulting sampling probabilities would improve reproducibility.
- The comparison would be stronger if all baselines were tuned under the same validation protocol rather than using hyperparameters from their original papers. This is especially relevant in a low-resource setting.
- Statistical significance tests or paired seed-level comparisons would help establish whether the approximately one-point improvement over CERT is robust.
- More details are needed about the unlabeled-data construction, back-translation system, and handling of failed or excessively shortened augmentations.
- The study is limited to short English classification datasets and BERT-base. Broader language, domain, and model evaluations would improve the generality of the conclusions.
- The cost analysis is useful, but reporting absolute training time and preprocessing cost would make the practical trade-off clearer.

These issues primarily affect reproducibility and breadth rather than undermining the central empirical result. The ablations and consistent improvements across datasets provide reasonable support for the main claim.

## Scores

| Criterion | Score (0–100) |
|---|---:|
| Soundness | 84 |
| Novelty | 78 |
| Significance | 84 |
| Clarity | 89 |
| **Final average** | **83.75** |

The average is computed as:

\[
(84 + 78 + 84 + 89)/4 = 83.75
\]

## Final recommendation

**Accept**

The paper offers a simple, well-motivated, and empirically effective improvement to contrastive intermediate training for low-resource classification. While additional methodological details, stronger baseline tuning, and statistical analysis would improve the work, the consistent gains and relevant ablations are sufficient to support acceptance.