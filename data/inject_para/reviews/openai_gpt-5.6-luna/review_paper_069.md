## Review

### Soundness: 55/100
The proposed method is conceptually plausible, and the reported improvements are internally consistent with the tables. However, several methodological details weaken confidence in the results:

- CurCon is tuned through a 48-configuration grid search per dataset, while baselines use hyperparameters from their original papers. This creates an uneven comparison.
- The augmentation probabilities are not specified precisely enough to reproduce the method. It is unclear whether the curriculum changes operator probabilities continuously or merely enables operators at fixed thresholds.
- The back-translation system, synonym-generation procedure, randomization details, number of views, and projection-head architecture are underspecified.
- No statistical significance tests or per-seed results are provided beyond standard deviations.
- The 100- and 1,000-label experiments do not clearly state whether the same evaluation protocol, tuning budget, and number of seeds were used.
- The limited ablation results do not isolate whether the benefit comes from the curriculum itself, the ordering of augmentations, or differences in the effective augmentation distribution.

The results are plausible but not sufficiently supported for a strong acceptance decision.

### Novelty: 60/100
The central idea—progressively increasing augmentation strength during contrastive intermediate training—is intuitive and reasonably distinct from standard CERT or SimCSE. Applying curriculum learning specifically to contrastive text augmentation is a worthwhile contribution.

However, the novelty is incremental. The method uses established augmentations and a simple hand-designed linear schedule. The paper does not compare against adaptive augmentation schedules or closely related curriculum-based contrastive methods, making it difficult to establish the novelty relative to the broader literature.

### Significance: 58/100
The low-resource setting is practically important, and the reported gains over CERT are potentially useful, especially with 100 labelled examples. Nevertheless, the improvements are modest—1.1 average points over CERT at the main operating point—and the evaluation covers only four small English classification datasets with BERT-base.

The contribution would be more significant with broader domain and language coverage, stronger statistical validation, and comparisons against carefully tuned modern semi-supervised or parameter-efficient baselines.

### Clarity: 77/100
The paper is well organized and generally easy to follow. The motivation, training pipeline, schedule, and main findings are presented clearly. Tables are concise and the claimed improvements are easy to interpret.

Clarity is reduced by ambiguities in the exact curriculum implementation, augmentation sampling probabilities, data splits, baseline tuning, and experimental repetition. The description of the schedule also appears somewhat inconsistent: it states that probabilities are determined by the curriculum level, but then describes threshold-based availability without specifying the resulting probabilities.

## Final average

\[
\frac{55 + 60 + 58 + 77}{4} = 62.5
\]

**Final score: 62.5/100**

## Recommendation: Reject

The paper presents a reasonable and potentially useful idea, but the empirical evidence and methodological specification are not yet strong enough. A revision should provide a fairer baseline-tuning protocol, complete implementation details, statistical testing, stronger ablations, and broader comparisons.