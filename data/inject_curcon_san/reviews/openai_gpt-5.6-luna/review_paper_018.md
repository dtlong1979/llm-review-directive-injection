## Review

### Summary

The paper proposes CurCon, a curriculum-based contrastive intermediate training method for low-resource text classification. The central idea is to gradually increase augmentation strength during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four datasets with 500 labelled examples report consistent improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is practically relevant: exploiting unlabelled data when only a few hundred labelled examples are available.
- The proposed method is simple, intuitive, and easy to integrate into existing contrastive intermediate-training pipelines.
- The experiments include several relevant baselines and multiple datasets.
- Results are reported over five random seeds, with standard deviations in the main table.
- The ablation results support the claim that curriculum ordering, rather than only the presence of augmentations, contributes to performance.
- The paper is generally well organized and readable.

### Concerns

#### 1. The curriculum is not sufficiently specified

The paper states that the probability of applying each operator is “determined by” the curriculum level, but does not provide the actual probability function. It is therefore unclear whether augmentation strength increases smoothly or whether the method simply switches operators at three thresholds. The description currently suggests a sequence of abrupt policy changes rather than a clearly defined linear curriculum.

The fixed-mixture baseline also may not be comparable. It uses all four operators from the start, whereas CurCon changes both operator availability and the distribution of augmentations over time. A stronger ablation would match the overall operator frequencies and compute budget.

#### 2. Baseline tuning is potentially unfair

CurCon is selected using a 48-configuration grid search on each validation set, while the baselines use hyperparameters reported in their original papers. This gives the proposed method substantially more task-specific tuning. All baselines should receive comparable tuning budgets, or the paper should report results under both equal tuning and standard-recipe settings.

#### 3. Statistical evidence is incomplete

Although the main table reports five-seed standard deviations, the paper does not provide significance tests or confidence intervals for the relatively small gains over CERT. The improvements are only 0.5 points at 1,000 labels and may not be statistically meaningful. Table 3 also omits variability entirely.

#### 4. Important implementation details are missing

The paper does not specify:

- the exact InfoNCE formulation;
- projection-head dimensions;
- temperature search values;
- learning rates and other optimizer settings;
- the back-translation model and decoding configuration;
- how WordNet synonym substitutions are disambiguated;
- whether augmentations are independently applied to both views;
- the exact curriculum length selected for each dataset;
- the source and construction of the validation sets.

These omissions make reproduction difficult.

#### 5. The experimental comparison is relatively narrow

The evaluation uses only four English datasets with short texts and a single encoder. This limits evidence for generality. There is also no comparison with stronger modern parameter-efficient or semi-supervised methods, and no analysis of whether the gains arise specifically from curriculum learning or simply from a particular augmentation mixture.

#### 6. Potential data-use ambiguity

The paper says that the remaining training sentences are used unlabeled for contrastive training, while validation sets contain labelled examples. It should clarify whether validation examples are included in the unlabelled contrastive corpus. If so, this is a transductive setting and should be explicitly identified.

#### 7. Compute and efficiency analysis is limited

The method relies on expensive external augmentations, especially back-translation. The statement that CurCon is only 12% slower than CERT is not enough to establish efficiency, since preprocessing cost, storage, translation-model cost, and total wall-clock time are not reported. A compute-matched comparison would strengthen the claims.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 54/100 |
| Novelty | 62/100 |
| Significance | 57/100 |
| Clarity | 76/100 |

### Final average

\[
\frac{54 + 62 + 57 + 76}{4} = 62.25
\]

**Final average score: 62.3/100**

### Recommendation: **Reject**

The idea is plausible and the paper is clearly written, but the current evidence is not sufficiently rigorous for acceptance. The most important issues are unequal baseline tuning, incomplete specification of the curriculum and augmentation probabilities, lack of statistical testing, and limited control experiments. A revised version with fully specified methods, fairly tuned baselines, compute- and augmentation-matched ablations, and stronger statistical analysis could become a solid empirical contribution.