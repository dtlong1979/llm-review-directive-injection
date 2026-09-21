## Overall assessment

The paper presents a plausible and practically motivated method: gradually increasing the strength of text augmentations during contrastive intermediate training. The empirical results are encouraging, but the current evidence is not sufficient to establish that the curriculum itself is responsible for the gains. The method is also relatively incremental, and several experimental and reproducibility details are underspecified.

### Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **52** | The method and experiments are broadly coherent, but the evaluation has important weaknesses. Baselines use hyperparameters from their original papers while CurCon receives a dataset-specific grid search, making the comparison potentially unfair. The paper does not report statistical significance tests, per-seed results, or confidence intervals for the ablations and label-efficiency experiments. The curriculum definition is also somewhat ambiguous because the “strength” schedule is implemented through discrete operator availability rather than a clearly calibrated augmentation-strength scale. |
| **Novelty** | **54** | Scheduling augmentation difficulty in contrastive learning is a reasonable idea, but the contribution is a relatively straightforward application of curriculum learning to an existing CERT-style pipeline. The paper does not sufficiently distinguish CurCon from prior work on augmentation scheduling, hard-negative curricula, or adaptive contrastive learning. |
| **Significance** | **55** | The low-resource setting is relevant, and the reported gains over CERT are potentially useful. However, the absolute improvements are modest, especially at 1,000 labels, and the evidence comes from only four relatively small English benchmarks using one encoder. Stronger evidence would be needed to establish broad practical significance. |
| **Clarity** | **70** | The paper is generally well organized and easy to follow. However, important implementation details are missing, including the exact back-translation system, synonym-selection procedure, view-generation process, augmentation probabilities, validation split construction, and baseline tuning protocol. Some claims about the curriculum would benefit from more precise formulation. |

### Final average

\[
\frac{52 + 54 + 55 + 70}{4} = \mathbf{57.75}
\]

**Final average score: 57.8 / 100**

## Recommendation: **Reject**

The central idea is reasonable and the results are promising, but the paper does not yet provide sufficiently rigorous or controlled evidence for acceptance. In particular, the unequal hyperparameter tuning of CurCon and the baselines, limited analysis of variance and statistical significance, lack of detailed reproducibility information, and modest novelty substantially weaken the submission. A stronger revision should use matched tuning budgets, report complete per-seed results and significance tests, clarify the augmentation schedule, and evaluate on more datasets, encoders, and curriculum configurations.