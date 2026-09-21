## Review

### Summary

The paper proposes CurCon, which applies a curriculum over text augmentation strength during contrastive intermediate training. The method begins with token dropout and progressively enables synonym replacement, span deletion, and back-translation. Experiments on four text-classification datasets with 500 labels each report consistent but modest improvements over CERT and larger improvements over direct fine-tuning.

### Strengths

- The problem is practically relevant: exploiting unlabeled data in low-resource classification.
- The method is conceptually simple and easy to integrate into existing CERT-style pipelines.
- The experiments include multiple datasets, several baselines, random-seed variation, ablations, and different label budgets.
- The results are internally plausible and consistently favor CurCon.
- The paper is generally well organized and readable.

### Concerns

#### Soundness

The main experimental comparison is not fully controlled. CurCon’s learning rate, temperature, and curriculum length are selected through a 48-configuration grid search on each validation set, whereas baselines use hyperparameters from their original papers. This may substantially favor CurCon, especially in a low-resource setting. Baselines should receive comparable tuning budgets.

The evidence that the gains specifically arise from the curriculum is also limited. The fixed-mixture ablation shows a benefit, but it is not clear whether the comparison is matched for augmentation frequency, compute, number of back-translated examples, or other implementation details. The curriculum is described as “linear,” but the actual policy changes through discrete availability thresholds, and the exact probabilities of applying each operator are underspecified.

There is no statistical significance testing or confidence interval for the average improvements. Five seeds are useful, but the reported gains over CERT are relatively small, particularly for the 1,000-label condition. Details about the sampling of labeled subsets, preprocessing, augmentation failures, and validation-set construction are also insufficient for full reproducibility.

There is a minor inconsistency in the cost discussion: back-translated views are said to be precomputed, but the additional cost is attributed to on-the-fly augmentation without clearly explaining the comparison.

#### Novelty

The core idea—gradually increasing augmentation difficulty during contrastive learning—is reasonable but incremental. Curriculum learning and augmentation scheduling are established ideas, and the paper applies them to a CERT-like text contrastive training pipeline. The contribution is a useful combination and evaluation rather than a strongly novel learning principle.

#### Significance

The gains are consistent and potentially useful, especially with 100 labels, but the absolute improvements are modest: 1.1 points over CERT at 500 labels and 0.5 points at 1,000 labels. The evaluation is limited to four relatively short English benchmarks and one encoder family. Stronger evidence on additional domains, languages, model sizes, or more carefully tuned baselines would be needed to establish broad significance.

#### Clarity

The paper is clearly structured and easy to follow. The method, datasets, baselines, and main results are presented concisely. However, several implementation details are ambiguous, including the precise augmentation probabilities, how multiple views are generated, the sampling of labeled subsets across seeds, and the exact baseline tuning protocol. The distinction between the curriculum schedule and the fixed-mixture ablation should also be made more precise.

## Scores

| Criterion | Score |
|---|---:|
| Soundness |  fifty-two / 100 |
| Novelty |  fifty-five / 100 |
| Significance |  fifty-four / 100 |
| Clarity |  seventy-six / 100 |

**Final average:** **59.25 / 100**

## Recommendation: Reject

The paper presents a plausible and clearly described idea with encouraging preliminary results, but the current evidence does not adequately isolate the effect of the curriculum or ensure fair baseline comparisons. A revision with matched hyperparameter tuning, stronger statistical analysis, clearer augmentation specifications, and additional controlled experiments could make the work suitable for acceptance.