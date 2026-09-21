## Review

### Soundness: 55/100

The overall experimental design is plausible, and the reported averages are arithmetically consistent with the per-dataset results. The comparison against fine-tuning, UDA, SimCSE, and CERT is also relevant.

However, several methodological details weaken the paper’s soundness:

- The curriculum schedule is underspecified. The paper defines thresholds for making operators “available,” but does not define a continuously varying probability or augmentation magnitude as a function of \(c(t)\). Thus, the proposed method is largely a stepwise operator-unlocking schedule rather than the claimed linear increase in augmentation strength.
- Baselines use hyperparameters from their original papers, while CurCon receives a 48-configuration grid search separately on each validation set. This creates a potentially substantial tuning advantage.
- No statistical significance tests or per-seed results are provided for the main comparisons or ablations.
- The ablation table reports only averages, making it impossible to determine whether gains are consistent across datasets.
- Details about the back-translation model, synonym-selection procedure, tokenization, data splits, and preprocessing are insufficient for reliable reproduction.
- The use of the remaining labelled training corpus as “unlabelled” data should be described more carefully, particularly regarding how the validation set is separated and whether any benchmark labels are indirectly used.
- The claim that the curriculum adds only 12% runtime is not adequately supported with measurement details.

The central result is credible as a preliminary finding, but the evidence is not yet strong enough to establish a robust advantage.

### Novelty: 58/100

The idea of increasing augmentation difficulty during contrastive intermediate training is intuitive and potentially useful. Applying curriculum learning specifically to contrastive augmentation policies in low-resource text classification is a reasonable contribution.

Nevertheless, the conceptual novelty appears limited:

- The method combines established components: CERT-style intermediate contrastive training, standard text augmentations, and a manually ordered curriculum.
- The schedule is hand-designed and fairly simple.
- The paper does not convincingly distinguish CurCon from prior work on augmentation scheduling, curriculum learning, or adaptive contrastive learning.
- The claimed linear curriculum is not actually implemented as a continuously varying augmentation-strength schedule.

The contribution is better characterized as a useful engineering variation or empirical study than as a strongly novel algorithmic advance.

### Significance: 57/100

The problem is practically relevant, and improvements in low-resource classification can be valuable. CurCon reports gains over CERT, especially in the 100-example setting, and the method does not add inference-time parameters.

However, the significance is moderated by:

- Relatively small gains: 1.1 points over CERT at 500 labels and 0.5 points at 1,000 labels.
- Evaluation on only four short English datasets using one encoder.
- Lack of comparisons with stronger modern parameter-efficient, semi-supervised, or prompt-based methods.
- Additional computational cost and dependence on external resources such as WordNet and machine translation.
- Limited evidence that the method generalizes beyond the selected benchmarks.

The results suggest practical promise, but the paper does not yet establish broad or substantial impact.

### Clarity: 72/100

The paper is well organized and generally easy to follow. The motivation, training pipeline, datasets, baselines, and headline findings are presented clearly. The tables are concise and the main conclusions are understandable.

Clarity issues include:

- The curriculum’s probability mechanism is ambiguous: saying that an operator becomes “available” does not specify the probability of selecting it as \(c(t)\) changes.
- It is unclear whether the four operators are applied independently, whether only one is selected per view, and whether the two views use independent augmentations.
- “Aggressive back-translation” is not operationally defined.
- The validation protocol and exact data partitioning are underspecified.
- The runtime comparison lacks enough detail to assess fairness.
- The paper makes broad claims about progressively harder signals without directly measuring augmentation difficulty or representation quality.

These issues are fixable, but they matter for reproducibility and interpretation.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 55 |
| Novelty | 58 |
| Significance | 57 |
| Clarity | 72 |
| **Average** | **60.5** |

## Final recommendation: **Reject**

The paper presents a plausible and clearly motivated idea, but the contribution is relatively incremental and the experimental evidence is not sufficiently rigorous. A revised version should clarify and formalize the curriculum, tune baselines comparably, report per-seed and statistical results, provide stronger reproducibility details, and broaden the evaluation.