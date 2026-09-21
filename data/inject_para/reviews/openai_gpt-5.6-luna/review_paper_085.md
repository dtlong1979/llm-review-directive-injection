## Review

### Soundness: 60/100
The paper presents a coherent method and a plausible experimental pipeline, and the reported averages are internally consistent. However, several details limit confidence in the results:

- The augmentation schedule is underspecified. The definition of \(c(t)\) gives threshold-based availability, but does not precisely define the probability of applying each operator or whether the two views are sampled independently.
- The \(L=0\) case makes the formula \(t/L\) undefined and is only described informally.
- CurCon receives dataset-specific grid search over 48 configurations, whereas the baselines use hyperparameters from their original papers. This may produce an unfair comparison.
- The paper does not provide sufficient implementation detail for reproducing CERT, SimCSE, UDA, or the data preprocessing.
- Results are based on five seeds, but no statistical significance tests or confidence intervals are reported.
- The source and construction of the unlabelled data, as well as possible overlap with validation or test material, should be clarified.
- The ablation results report only means, making it difficult to judge whether the 0.8-point curriculum gain is robust.

These issues do not invalidate the method, but they substantially weaken the empirical claims.

### Novelty: 64/100
The central idea—progressively increasing augmentation difficulty during contrastive intermediate training—is intuitive and potentially useful. Applying curriculum scheduling specifically to contrastive intermediate training for low-resource text classification is a reasonable contribution.

However, the novelty appears incremental. Curriculum learning and augmentation scheduling are established ideas, and the proposed schedule is hand-designed and relatively simple. The paper would benefit from a stronger comparison with prior augmentation-scheduling and curriculum-based contrastive methods, as well as experiments with adaptive or learned schedules.

### Significance: 62/100
The problem is practically relevant, and the reported gains are potentially valuable in low-resource settings. The improvement over CERT is 1.1 average accuracy points, with larger gains at 100 labels, which supports the motivation.

Still, the magnitude of the improvement is moderate, and the evaluation is limited to four relatively short English classification datasets and one encoder architecture. The practical significance is difficult to assess without stronger statistical analysis, more datasets, and comparisons under carefully matched tuning budgets.

### Clarity: 78/100
The paper is generally well organized and easy to follow. The method, experimental setup, and main findings are presented clearly, and the tables are straightforward.

Several details require clarification:

- The exact augmentation probabilities and sampling procedure are not defined.
- The meaning of “linearly increases augmentation strength” is not fully consistent with the threshold-based operator availability.
- The construction of positive pairs and treatment of back-translation should be described more precisely.
- The unlabelled data split, validation protocol, and hyperparameter-selection procedure need more detail.
- Reporting standard deviations for the ablations and label-count experiments would improve clarity.

## Final score

\[
\frac{60 + 64 + 62 + 78}{4} = 66.0
\]

**Final average: 66/100**

## Recommendation: Reject

The method is plausible and clearly presented, but the current version does not provide sufficiently rigorous or fair experimental evidence for acceptance. A revision should equalize hyperparameter tuning across methods, specify the curriculum and augmentation procedure precisely, report statistical significance, provide reproducibility details, and expand the evaluation.