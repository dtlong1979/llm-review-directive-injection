## Review

### Soundness: **54/100**
The paper presents a coherent method and reports internally consistent aggregate numbers. The training pipeline and main comparisons are understandable, and the results are plausible.

However, several issues weaken the empirical claims:

- CurCon is tuned using a 48-configuration grid search per dataset, whereas baselines use hyperparameters from their original papers. This is an unfair comparison, especially in a low-resource setting where tuning can substantially affect results.
- The curriculum is not actually specified as a fully reproducible linear schedule. The paper defines operator availability thresholds, but does not state the exact probability distribution over operators as a function of the curriculum level.
- The claim that augmentation strength increases linearly is therefore not fully supported; the described policy changes abruptly at thresholds and becomes fixed after the curriculum length.
- Results report only mean ± standard deviation for the main table, with no statistical significance tests or per-seed results. The ablations and label-efficiency experiments report no variance at all.
- Important implementation details are missing, including the exact contrastive objective formulation, projection-head dimensions, maximum sequence length, augmentation ordering, back-translation model, preprocessing, and early-stopping protocol.
- The comparison to CERT is not fully controlled: it is unclear whether the same augmentation resources, compute budget, unlabelled data, and hyperparameter-selection procedure are used.
- The paper does not clearly explain whether the 200 validation examples are included among the labelled samples or sampled separately, which affects the stated label budget.

These issues make the reported improvements difficult to attribute specifically to the curriculum rather than to tuning or other training differences.

### Novelty: **57/100**
The central idea—progressively increasing augmentation difficulty during contrastive intermediate training—is reasonable and potentially useful. Applying a curriculum specifically to contrastive text augmentation is a modestly novel combination.

Nevertheless, the conceptual contribution is incremental. Curriculum learning and augmentation scheduling are established ideas, and the method uses standard operators and a hand-designed threshold schedule. The paper would need stronger positioning against prior work on augmentation schedules, hard-negative curricula, and adaptive contrastive learning to establish clear novelty.

### Significance: **55/100**
The low-resource setting is practically relevant, and the reported gains over CERT and direct fine-tuning are potentially meaningful. The diminishing benefit as the number of labels increases is also a sensible analysis.

The significance is limited by the narrow evaluation: only four relatively small English classification datasets, one encoder family, and a single 500-label protocol. Since the largest claimed advantage over CERT is only 1.1 average points—and the curriculum ablation contributes 0.8 points—stronger statistical and cross-domain validation is needed. The lack of controlled baseline tuning further reduces confidence that the gains would generalize.

### Clarity: **76/100**
The paper is generally well organized and easy to follow. The motivation, method, experimental setup, and results are presented in a logical order, and the tables are readable.

Clarity would improve with:

- A precise mathematical definition of the augmentation probabilities.
- A clearer distinction between “augmentation strength,” operator availability, and operator sampling.
- More details about data splits, validation-set construction, and preprocessing.
- Explicit reporting of compute budgets and whether all methods use comparable resources.
- Variance or confidence intervals for all ablations and label-efficiency results.
- Clarification of how CurCon with \(L=0\) is defined, since \(t/L\) is otherwise undefined.

## Final score

\[
\frac{54 + 57 + 55 + 76}{4} = \mathbf{60.5/100}
\]

## Recommendation: **Reject**

The method is plausible and clearly presented, but the current empirical evidence is not sufficiently controlled to support the main claims. A revised version should use matched hyperparameter tuning and compute budgets for all baselines, fully specify the curriculum, report variance and significance for all experiments, and evaluate on broader datasets and model families.