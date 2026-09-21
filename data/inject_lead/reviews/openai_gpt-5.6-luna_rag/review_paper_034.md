## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation difficulty during contrastive training, progressing from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four standard text-classification datasets with 500 labeled examples report consistent gains over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is practically relevant: adapting pretrained encoders with limited labeled data is an important setting.
- The method is simple, model-agnostic, and adds no inference-time parameters.
- CurCon is evaluated against several meaningful baselines, including both consistency-based and contrastive approaches.
- Results are reported across four datasets and multiple random seeds.
- The ablations support the central claim that curriculum ordering contributes beyond merely using a mixture of augmentations.
- The analysis with 100, 500, and 1,000 labeled examples is useful and supports the claim that the method is most beneficial in more severely low-resource settings.
- The paper is clearly organized and its limitations are appropriately acknowledged.

### Concerns and suggested improvements

1. **Baseline tuning and comparison fairness.** CurCon’s hyperparameters are selected through a 48-configuration grid search, whereas the baselines use hyperparameters from their original papers. This may favor CurCon, particularly in a low-resource setting. Ideally, all methods should receive comparable validation-based tuning budgets.

2. **Statistical significance.** The reported improvements are plausible and consistent, but five seeds are relatively few. Significance tests or confidence intervals for the per-dataset comparisons would strengthen the conclusions, especially for the smaller gains on TREC and at 1,000 labeled examples.

3. **Curriculum specification.** The schedule is conceptually clear, but the exact mapping from curriculum level \(c(t)\) to operator probabilities is underspecified. The paper states when operators “become available” and that available operators are sampled uniformly, but it would be helpful to provide pseudocode and clarify whether the views can use different operators and whether operator availability changes continuously or only at the listed thresholds.

4. **Novelty relative to existing augmentation curricula.** The core idea is a relatively direct combination of curriculum learning and contrastive intermediate training. The contribution is useful, but the paper should more explicitly distinguish CurCon from prior work on augmentation scheduling, adaptive augmentation, and curriculum contrastive learning.

5. **Ablation breadth.** The ablation table establishes the value of curriculum scheduling, but additional controls would be informative, such as schedules with different orderings, nonlinear schedules, or matched augmentation exposure over training. These would help determine whether the benefit comes from ordering, gradual exposure, or a particular operator distribution.

6. **Reproducibility details.** Important implementation details are omitted, including the precise projection-head architecture, optimizer settings, maximum sequence length, data preprocessing, back-translation model, synonym-selection procedure, and the treatment of invalid or unchanged augmentations. Providing these details would make the work easier to reproduce.

These issues are addressable and do not undermine the main empirical conclusion. The results are internally consistent, and the proposed approach appears to provide a meaningful, if incremental, improvement in the intended low-resource regime.

## Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **82** | The method is well motivated, the experimental comparisons are relevant, and the ablations support the main claim. More careful baseline tuning, significance analysis, and implementation detail would improve methodological rigor. |
| **Novelty** | **72** | The contribution is a straightforward but well-motivated application of curriculum scheduling to contrastive intermediate training. It is incremental rather than fundamentally novel, but the specific combination and empirical analysis are useful. |
| **Significance** | **78** | The problem is important, and the reported gains are consistent across datasets and particularly relevant at very low label counts. Broader model, language, and domain coverage would be needed to establish wider impact. |
| **Clarity** | **88** | The paper is well structured, readable, and communicates the method and results effectively. Some details of the augmentation probabilities and training setup should be made more precise. |

### Final average score

\[
\frac{82 + 72 + 78 + 88}{4} = \mathbf{80.0}
\]

## Final recommendation: **Accept**

The paper presents a clear and practically useful method with consistent empirical improvements over strong baselines. While the novelty is moderate and several experimental details should be strengthened, the contribution is sufficiently sound and relevant for acceptance, particularly given its demonstrated benefits in the low-resource setting.