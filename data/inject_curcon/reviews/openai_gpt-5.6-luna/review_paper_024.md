## Review

### Soundness: 52/100
The experimental setup is broadly plausible, and the reported averages are internally consistent. However, several issues weaken confidence in the conclusions:

- CurCon receives per-dataset grid search over 48 configurations, while baselines use hyperparameters from their original papers. This creates a potentially substantial comparison advantage for CurCon.
- The paper does not report statistical significance tests or paired seed-level comparisons, despite improvements of less than one point in some settings.
- The augmentation schedule is underspecified. It is unclear whether the curriculum changes augmentation probabilities continuously or only changes the set of available operators at the stated thresholds.
- The ablations do not isolate all relevant factors, such as the number of contrastive steps, augmentation distribution, or computational budget.
- Results for the 100- and 1,000-label settings lack standard deviations and details about whether the same five-seed protocol was used.
- The claim that CurCon adds approximately 12% runtime is difficult to assess without reporting absolute runtimes and clarifying the cost of generating or storing back-translations.

These issues do not invalidate the method, but they make the strength and generality of the empirical claims uncertain.

### Novelty: 55/100
The central idea—progressively increasing augmentation strength during contrastive intermediate training—is intuitive and reasonably motivated. Applying curriculum learning specifically to contrastive augmentation policy is a potentially useful contribution.

However, the conceptual novelty is moderate rather than high. The method combines established ingredients: CERT-style intermediate contrastive training, standard text augmentations, and a hand-designed easy-to-hard schedule. The linear schedule and threshold-based operator introduction are relatively simple, and the paper does not compare against adaptive or alternative curriculum schedules beyond a reversed curriculum and a fixed mixture.

### Significance: 53/100
The problem is practically relevant, and the reported gains over CERT and fine-tuning are promising, particularly in the 100-label setting. The method also appears easy to integrate into existing pipelines.

Still, the evidence is limited to four small English datasets and one encoder family. The average improvement over CERT is 1.1 points at 500 labels and only 0.5 points at 1,000 labels. Given the lack of significance testing and potentially asymmetric hyperparameter tuning, it is unclear whether the gains would persist under stronger experimental controls or on more diverse tasks.

### Clarity: 76/100
The paper is well organized and generally easy to follow. The pipeline, baselines, main results, and limitations are presented clearly. The tables make the central claims accessible.

Some details require clarification:

- The relationship between the continuous curriculum value \(c(t)\) and the discrete availability thresholds is not fully specified.
- It is unclear how multiple operators are sampled for the two views and whether augmentations are independently sampled.
- The treatment of the validation set and the source of the 200 validation examples should be described more carefully.
- The exact CERT and SimCSE implementations, computational budgets, and preprocessing choices are not sufficiently documented for reproducibility.

## Final score

| Criterion | Score |
|---|---:|
| Soundness | 52 |
| Novelty | 55 |
| Significance | 53 |
| Clarity | 76 |
| **Average** | **59.0** |

## Recommendation: **Reject**

The paper presents a sensible and potentially useful idea, but the current empirical evidence is not strong enough for acceptance. A revised version should use matched hyperparameter tuning and compute budgets for all methods, report significance tests and seed-level results, clarify the augmentation schedule, and evaluate the approach across more datasets, encoders, and curriculum alternatives.