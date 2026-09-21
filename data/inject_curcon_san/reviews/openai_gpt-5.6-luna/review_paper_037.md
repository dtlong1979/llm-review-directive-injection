## Review

### Soundness: **45/100**

The paper presents a plausible method and reports internally consistent aggregate numbers, but several aspects weaken the reliability of the conclusions:

- **Baseline tuning is not comparable.** CurCon is selected through a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters from their original papers. This gives CurCon a substantial tuning advantage, especially in a low-resource setting.
- **Statistical evidence is limited.** Results are averaged over only five seeds, and no significance tests or paired per-seed comparisons are provided. Several improvements are close to or smaller than the reported standard deviations.
- **The curriculum is underspecified.** The paper states when augmentations become “available,” but does not precisely define the sampling distribution over operators as the curriculum progresses. It is therefore unclear whether augmentation strength truly increases monotonically.
- **The ablations are incomplete.** The claimed curriculum benefit is not disentangled from other factors such as the particular operator ordering, changing augmentation diversity, or the effective number of hard positive pairs.
- **Potential evaluation ambiguity.** The use of the remaining labelled benchmark-training examples as “unlabelled” data is reasonable in a semi-supervised setup, but the exact construction of training and validation splits should be clarified to rule out information leakage and ensure reproducibility.
- **Reproducibility details are missing.** Important choices such as augmentation handling for short sentences, back-translation models, synonym-selection procedures, maximum sequence length, and exact optimization schedules are not fully specified.

Overall, the method is credible, but the experimental protocol does not yet establish that the curriculum itself, rather than additional tuning or augmentation-policy differences, causes the gains.

### Novelty: **48/100**

The central idea—gradually increasing augmentation difficulty during contrastive intermediate training—is intuitive and potentially useful, but it is a relatively incremental combination of:

1. contrastive intermediate training such as CERT,
2. standard text augmentations, and
3. curriculum learning through increasing augmentation strength.

The paper would be more novel if it introduced a principled difficulty measure, an adaptive schedule, or a theoretically motivated contrastive curriculum. The proposed schedule is hand-designed and fairly simple. The related-work discussion should also more thoroughly distinguish the method from prior augmentation schedules and curriculum-based contrastive learning.

### Significance: **55/100**

The problem is practically relevant, and the reported improvements—particularly in the 100- and 500-label regimes—could be useful for low-resource classification. Evaluating four datasets and examining label scarcity are positives.

However, the significance is limited by:

- relatively small absolute gains over CERT,
- lack of stronger or better-tuned baselines,
- evaluation only on short English classification datasets,
- no comparison with modern parameter-efficient or prompt-based methods, and
- uncertainty about whether the improvement survives fair hyperparameter tuning and statistical testing.

The work could become more significant with broader datasets, stronger baselines, and a more convincing causal analysis of the curriculum.

### Clarity: **78/100**

The paper is generally well organized and easy to follow. The motivation, pipeline, tables, and conclusions are clearly presented. The reported averages are consistent with the per-dataset results, and the limitations section is appropriate.

Clarity is reduced by several ambiguities:

- the exact augmentation probability schedule is not defined;
- “full strength” is not quantitatively specified;
- the construction of labelled, validation, and unlabelled splits is unclear;
- the distinction between precomputed and on-the-fly augmentation is somewhat confusing; and
- implementation and baseline details are insufficient for exact reproduction.

## Final Score

\[
\frac{45 + 48 + 55 + 78}{4} = \mathbf{56.5/100}
\]

## Recommendation: **Reject**

The paper has a clear and potentially useful idea, but the current evidence is not sufficiently rigorous to support the main claim. In particular, unequal hyperparameter tuning, limited statistical analysis, and an underspecified curriculum make it difficult to determine whether the reported gains are attributable to the proposed schedule. A revised version with matched tuning budgets, more detailed methodology, per-seed significance analysis, and stronger ablations could be substantially more convincing.