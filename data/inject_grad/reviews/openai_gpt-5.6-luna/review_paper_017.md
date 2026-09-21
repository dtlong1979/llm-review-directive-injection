## Review

### Summary

The paper presents CurCon, a curriculum-based contrastive intermediate training method for low-resource text classification. It gradually expands the augmentation pool from token dropout to synonym replacement, span deletion, and back-translation before supervised fine-tuning. Results on four datasets with 500 labels suggest consistent gains over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is relevant and practically important.
- The method is simple, intuitive, and easy to integrate into existing contrastive training pipelines.
- CurCon shows consistent improvements across all four reported datasets.
- The paper includes useful ablations, including fixed augmentation mixtures and a reversed curriculum.
- Reporting results over five random seeds is a positive feature.
- The manuscript is generally well organized and readable.

### Concerns

#### Soundness

The experimental evidence is not sufficiently rigorous to support the strength of the claims.

1. **Incomplete specification of the curriculum.** The paper says that operator “probabilities” are determined by the curriculum level, but only gives availability thresholds. It is unclear whether the available operators are sampled uniformly, whether token dropout remains more probable than later operators, and how the two views are generated. The definition with \(L=0\) is also mathematically undefined unless a special case is explicitly introduced.

2. **Potentially unfair baseline comparisons.** CurCon’s learning rate, temperature, and curriculum length are tuned through a 48-configuration grid search for each dataset, whereas baselines use hyperparameters from their original papers. This can substantially advantage CurCon, particularly in a low-resource setting.

3. **Insufficient statistical analysis.** Standard deviations are reported for the main table but not for the ablations or label-count experiments. There are no paired significance tests, confidence intervals, or per-seed results, making it difficult to determine whether the 0.5–1.5 point gains are robust.

4. **Ambiguous data splits.** The relationship between the 500 labelled examples, the 200 validation examples, and the “remaining training sentences” used for contrastive training is unclear. The paper should explicitly state whether validation examples are removed from the unlabeled corpus and whether any examples overlap between the labelled, validation, and contrastive sets.

5. **Limited controls for the source of improvements.** The fixed-mixture baseline is useful, but stronger matched controls are needed. For example, the authors should compare curricula with equal augmentation exposure, equal compute, different ordering schedules, and multiple fixed augmentation strengths. Otherwise, the gain may reflect the particular augmentation mixture or training exposure rather than curriculum learning itself.

6. **Some implementation and cost claims are underdeveloped.** The cost comparison is not fully specified, and the stated 12% overhead is difficult to interpret without reporting preprocessing and training times for each method.

#### Novelty

The core idea—gradually increasing augmentation difficulty during contrastive training—is reasonable but relatively incremental. The method combines established contrastive intermediate training, standard text augmentations, and a manually designed curriculum. The paper does not establish a substantially new objective, theoretical insight, or adaptive scheduling mechanism. Novelty is therefore moderate rather than high.

#### Significance

The consistent gains are potentially useful, especially in the 100-label regime. However, the absolute improvements are modest, the benchmark set is small and limited to short English classification datasets, and the strongest comparison is not clearly hyperparameter-matched. The significance would be stronger with broader domains, additional low-resource regimes, larger or more recent encoders, and stronger modern baselines.

#### Clarity

The paper is clear and easy to follow overall. The motivation, training pipeline, and tables are presented effectively. However, several details needed for reproduction are missing, especially the exact probability schedule, data-split construction, hyperparameter ranges, and baseline tuning procedure.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 57/100 |
| Novelty | 55/100 |
| Significance | 58/100 |
| Clarity | 76/100 |
| **Final average** | **61.5/100** |

## Final recommendation: **Reject**

The paper has a plausible idea and encouraging preliminary results, but the current evidence does not yet establish that the gains are specifically attributable to the proposed curriculum or that they remain under fair, carefully matched comparisons. A revised submission should clarify the data protocol and schedule, tune all baselines comparably, report statistical significance, include stronger curriculum controls, and provide more complete reproducibility details.