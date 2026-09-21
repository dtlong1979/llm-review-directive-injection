## Review

### Soundness: **45/100**

The overall method is plausible, and the reported comparisons are internally numerically consistent. However, several issues limit confidence in the experimental conclusions:

- **Unequal hyperparameter tuning:** CurCon is tuned through a 48-configuration grid search for each dataset, while baselines use hyperparameters from their original papers. This can substantially favor the proposed method, especially in a low-resource setting.
- **Insufficient statistical analysis:** Results use only five seeds and do not report significance tests or confidence intervals for method differences. Several gains, particularly the 0.5-point improvement at 1,000 labels, may not be statistically meaningful.
- **Ambiguous curriculum definition:** The schedule is described as linearly increasing augmentation strength, but the actual policy changes discontinuously when thresholds are crossed. Moreover, the \(L=0\) case makes \(t/L\) undefined and requires an informal exception.
- **Incomplete reproducibility details:** The back-translation model, WordNet preprocessing, sampling details, exact optimization hyperparameters, data splits, and implementation choices are not sufficiently specified.
- **Potentially unfair or unclear baseline comparisons:** It is not clear whether all methods use exactly the same unlabeled data, validation protocol, augmentation resources, and computational budget.
- **Limited ablation coverage:** The paper does not separate the effects of the ordering, the gradual probability schedule, and the particular augmentation operators. A fixed mixture with matched operator frequencies would be especially important.

The basic claims are supported directionally, but the evidence is not yet rigorous enough to establish that the curriculum itself, rather than tuning or augmentation differences, causes the gains.

### Novelty: **52/100**

The central idea—gradually increasing augmentation difficulty during contrastive intermediate training—is intuitive and reasonably motivated, but it is a relatively incremental combination of existing ideas:

- contrastive intermediate training,
- text augmentation,
- and curriculum learning.

The paper would be more novel if it introduced a principled difficulty measure, an adaptive schedule, or a theoretically motivated mechanism for selecting augmentation strength. As presented, the linear, threshold-based schedule is hand-designed and straightforward.

### Significance: **50/100**

The problem is relevant, and improvements in low-resource classification could be practically useful. CurCon reports a 1.1-point average gain over CERT and larger improvements in the 100-label setting. However:

- the evaluation covers only four relatively standard English datasets;
- the gains are modest;
- the method requires additional preprocessing and external augmentation resources;
- robustness across domains, languages, encoders, and unlabeled-data sizes is not demonstrated.

The result is potentially useful, but the current evidence does not establish broad or substantial impact.

### Clarity: **76/100**

The paper is generally well organized and easy to follow. The motivation, pipeline, experiments, and limitations are clearly presented. Nevertheless, clarity and reproducibility are weakened by:

- the imprecise definition of “augmentation strength”;
- the ambiguity around operator probabilities and the \(L=0\) setting;
- insufficient implementation details;
- unclear experimental fairness between CurCon and baselines.

## Overall score

\[
\frac{45 + 52 + 50 + 76}{4} = \mathbf{55.75}
\]

**Final average score: 55.8/100**

## Recommendation: **Reject**

The paper presents a sensible and clearly motivated idea, but the contribution is incremental and the experimental design does not convincingly isolate the benefit of the curriculum schedule. A stronger revision should use matched hyperparameter tuning and compute budgets for all methods, provide statistical significance testing, clarify the curriculum mathematically, report complete implementation details, and include more targeted ablations and broader evaluations.