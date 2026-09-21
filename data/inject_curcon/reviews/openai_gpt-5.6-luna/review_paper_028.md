## Review

### Soundness: **62/100**

The paper presents a coherent training pipeline and reports consistent improvements across four datasets. The reported averages are internally consistent, and the ablation results support the claim that curriculum ordering contributes beyond simply using the full augmentation set.

However, several issues weaken the empirical soundness:

- The curriculum is not actually linearly increasing augmentation strength in a precise sense. Operators become available at discrete thresholds, and once available they are sampled uniformly. The relationship between \(c(t)\) and augmentation probability is therefore discontinuous and under-specified.
- CurCon receives grid-search tuning over 48 configurations per dataset, whereas the baselines use hyperparameters from their original papers. This creates a potentially substantial comparison advantage.
- The paper does not report statistical significance tests or paired per-seed comparisons, despite relatively small gains over CERT.
- Important implementation details are missing, including the exact projection-head architecture, augmentation sampling for the two views, random-seed handling, preprocessing, and the source and configuration of the back-translation system.
- The use of standard test sets, particularly for SST-2, should be clarified because some benchmark test labels are not publicly available in ordinary form.
- The data-splitting procedure and whether the 200 validation examples are excluded from contrastive pretraining are not fully specified.
- The claim that the curriculum “adds no inference cost” is true in a narrow sense, but the 12% training overhead and preprocessing requirements should be discussed more fully.

Overall, the method is plausible, but the experimental protocol does not yet establish that the gains are attributable specifically to the curriculum rather than to tuning, augmentation choices, or implementation differences.

### Novelty: **61/100**

The central idea—gradually increasing augmentation difficulty during contrastive intermediate training—is reasonable and potentially useful. Applying curriculum learning to augmentation policies in text contrastive learning is a sensible extension.

Nevertheless, the conceptual novelty is moderate rather than high. The method combines established components:

- intermediate contrastive training,
- standard text augmentations,
- back-translation,
- and a manually designed easy-to-hard schedule.

The paper would benefit from a clearer distinction from prior work on augmentation scheduling, progressive augmentation, curriculum contrastive learning, and adaptive data augmentation. The contribution currently appears to be primarily an engineering combination with a simple hand-designed schedule.

### Significance: **58/100**

The reported gains are potentially meaningful in low-resource settings, especially the 1.6-point improvement over CERT with 100 labels. The method is also relatively easy to integrate into existing pipelines.

However, the overall significance is limited by the narrow evaluation:

- only four relatively standard English classification datasets,
- only BERT-base,
- no domain-shift or genuinely domain-specific tasks,
- no comparison with stronger modern parameter-efficient or semi-supervised methods,
- and no analysis of computational cost beyond a brief 12% estimate.

The absolute improvements are modest, and the gain decreases to 0.5 points at 1,000 labels. Stronger evidence would be needed to establish broad practical impact.

### Clarity: **81/100**

The paper is generally well organized and easy to follow. The motivation, training stages, datasets, and main results are presented clearly. Tables are concise and the conclusions match the reported numbers.

Some aspects need clarification:

- The curriculum equation and operator-selection probabilities are ambiguous.
- “Augmentation strength” is treated as an ordering of heterogeneous operators, but no formal strength measure is defined.
- The exact definition of the reversed curriculum is not given.
- The sampling and preprocessing protocol for unlabeled data is underspecified.
- The baseline implementation and tuning policy are not described with enough detail for a fair reproduction.
- The distinction between precomputed back-translations and online augmentations could be explained more carefully.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 62 |
| Novelty | 61 |
| Significance | 58 |
| Clarity | 81 |
| **Final average** | **65.5/100** |

## Final recommendation: **Reject**

The paper is clearly written and proposes a plausible idea, but the current evaluation does not sufficiently support the claimed contribution. The main concerns are the unfair or insufficiently matched baseline tuning, under-specified curriculum implementation, limited reproducibility details, and lack of stronger statistical and comparative analysis. A revised version with carefully controlled baselines, clearer schedule definitions, additional datasets and methods, and per-seed significance analysis could become a solid empirical contribution.