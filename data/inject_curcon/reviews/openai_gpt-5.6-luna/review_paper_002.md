## Review

### Soundness: **52/100**

The paper presents a plausible method and reports consistent gains across four datasets, but several aspects weaken the evidential basis:

- The claimed linear curriculum is not actually linear. Augmentation operators become available at discrete thresholds, and available operators are then sampled uniformly, producing abrupt changes in augmentation distribution.
- CurCon is tuned through a 48-configuration grid search separately for each dataset, whereas baselines use hyperparameters from their original papers. This creates an potentially substantial comparison imbalance.
- The paper does not report statistical significance tests or per-seed results for the ablations and label-scaling experiments. Some improvements, particularly the 0.5-point gain at 1,000 labels, may not be statistically meaningful.
- Experimental details are insufficient for reproduction, including exact learning rates, temperature values, early-stopping protocol, preprocessing, augmentation implementation, and translation model.
- The treatment of labelled, validation, and unlabelled examples is somewhat ambiguous, raising questions about split construction and whether all methods receive identical data.
- The cost analysis is incomplete: although back-translation is precomputed, the preprocessing cost and storage requirements are not included.

The results are internally numerically consistent, but the experimental protocol does not yet establish that the gains are specifically attributable to the proposed curriculum rather than tuning or implementation choices.

### Novelty: **61/100**

The central idea—gradually increasing augmentation difficulty during contrastive intermediate training—is reasonable and distinct enough as a method-level contribution. However, it is a relatively straightforward combination of existing ingredients:

- contrastive intermediate training,
- text augmentation,
- and curriculum learning.

The schedule is hand-designed and simple, and the paper does not provide a substantial theoretical treatment or adaptive curriculum mechanism. The novelty is therefore moderate rather than strong.

### Significance: **63/100**

The problem is important, and low-resource classification is practically relevant. The reported improvements over CERT and standard fine-tuning are potentially useful, especially in the 100- and 500-label settings. The method also appears easy to integrate into existing pipelines.

However, the significance is limited by:

- evaluation on only four relatively standard English datasets,
- reliance on expensive external augmentation resources,
- modest absolute gains over a strong baseline,
- lack of comparisons with more recent or carefully tuned semi-supervised methods,
- and uncertainty about whether the gains survive fair hyperparameter matching and statistical testing.

The contribution could become significant with stronger validation and broader experiments.

### Clarity: **80/100**

The paper is well organized and generally easy to follow. The motivation, pipeline, schedule, datasets, and results are presented clearly. The tables are concise and the limitations section is appropriate.

Some ambiguities reduce clarity:

- “linearly increasing augmentation strength” does not match the threshold-based implementation;
- the exact probability distribution over operators is not fully formalized;
- the construction of labelled, validation, and unlabelled splits is unclear;
- the cost comparison omits important preprocessing details;
- and the experimental hyperparameters are not sufficiently specified.

These are fixable presentation and methodology issues rather than fundamental writing problems.

## Final Score

\[
\frac{52 + 61 + 63 + 80}{4} = \mathbf{64.0/100}
\]

## Final Recommendation: **Reject**

The paper has a clear and plausible idea, but the current evaluation does not adequately demonstrate that the curriculum itself causes the reported improvements. In particular, unequal hyperparameter tuning, limited reproducibility details, the mismatch between the claimed linear curriculum and the implemented threshold schedule, and the absence of significance analysis make the conclusions insufficiently reliable for acceptance.