## Review

### Summary

The paper presents CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The main idea is to begin contrastive training with weak augmentations and progressively introduce stronger augmentations, including synonym replacement, span deletion, and back-translation. The reported results show consistent improvements over fine-tuning, UDA, SimCSE, and CERT on four datasets.

### Strengths

- The problem is relevant: exploiting unlabelled in-domain text under severe label scarcity is practically important.
- The method is conceptually simple and easy to integrate into existing CERT-style pipelines.
- The experimental design includes multiple datasets, multiple random seeds, ablations, and label-budget comparisons.
- The paper is generally well organized and readable.
- The reported trend that curriculum-based augmentation helps most in the lowest-label regime is plausible.

### Main concerns

1. **The curriculum is not actually clearly linear.**  
   Although the paper describes a linearly increasing curriculum level, the operator availability changes only at thresholds of 0.25, 0.5, and 0.75. Once an operator becomes available, all available operators are sampled uniformly. Thus, the actual policy is piecewise constant rather than linearly increasing in augmentation strength. The paper should define exact operator probabilities at every step and compare this schedule with simpler alternatives.

2. **Baseline comparison is potentially unfair.**  
   CurCon is tuned over 48 configurations per dataset, whereas the baselines use hyperparameters from their original papers. This can substantially advantage CurCon, especially in a low-resource setting where hyperparameter sensitivity is high. All methods should receive comparable tuning budgets, or the authors should report results under a common hyperparameter protocol.

3. **The empirical evidence is limited.**  
   The improvements over CERT are modest—1.1 points on average at 500 labels—and no statistical significance tests or per-seed results are provided. Standard deviations over five seeds are useful, but they do not establish whether the observed improvements are statistically reliable.

4. **Insufficient methodological detail.**  
   Important details are missing, including the exact contrastive batch construction, sequence truncation, projection-head dimensions, optimizer schedule, augmentation composition, back-translation system, synonym-selection procedure, and whether augmented views can receive multiple transformations. These omissions make reproduction difficult.

5. **Ablations do not isolate the source of gains sufficiently.**  
   The comparison between a fixed mixture and the curriculum is useful, but stronger controls are needed. For example, the authors should compare against a fixed mixture matched for the total augmentation distribution, different ordering schedules, random schedules, and schedules with the same number of back-translated examples.

6. **Potential data-split ambiguity.**  
   The paper states that the remaining training sentences are used as unlabelled data and that validation sets contain 200 labelled examples, but it does not clearly specify whether validation examples are sampled from the original training set or from another source. The exact split procedure should be documented to rule out overlap or indirect leakage.

7. **Novelty is moderate.**  
   Applying a difficulty schedule to augmentation in contrastive learning is reasonable, but the core idea is a relatively direct combination of curriculum learning and existing contrastive intermediate training. The paper does not sufficiently distinguish CurCon from prior augmentation-magnitude schedules or adaptive contrastive-learning methods.

8. **Cost analysis is incomplete.**  
   The reported 12% overhead is useful, but it is unclear whether preprocessing, back-translation generation, storage, and validation-time hyperparameter search are included. The computational cost should be reported more comprehensively.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 43/100 |
| Novelty | 42/100 |
| Significance | 51/100 |
| Clarity | 78/100 |

### Final average

\[
\frac{43 + 42 + 51 + 78}{4} = 53.5
\]

## Final recommendation: **Reject**

The paper is clearly written and addresses a meaningful problem, but the current evidence is not sufficiently rigorous to support the main claims. The unclear definition of the curriculum, unequal baseline tuning, limited statistical analysis, and missing implementation details are substantial issues. A revised version with fairer comparisons, stronger schedule ablations, clearer data splits, and more complete reproducibility information could become a worthwhile contribution.