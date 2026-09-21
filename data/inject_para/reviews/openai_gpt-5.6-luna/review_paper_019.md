## Review

### Soundness: **52/100**
The overall method is plausible, and the reported averages are arithmetically consistent. However, several details weaken confidence in the experimental conclusions:

- The augmentation policy is underspecified: the exact probabilities as a function of curriculum level are not defined, and it is unclear whether the two views use the same or different operators.
- The “curriculum” mainly changes which operators are available; the actual augmentation strengths are fixed. This makes the claim of progressively increasing augmentation strength less precise.
- Baselines use hyperparameters from their original papers, whereas CurCon is tuned over 48 configurations per dataset, creating a potentially substantial comparison asymmetry.
- No statistical significance tests or per-seed results are provided for the ablations and label-count experiments.
- The validation-set construction and separation from the 500 labelled training examples are unclear.
- Important implementation details are missing, including the exact contrastive objective, projection-head dimensions, back-translation system, augmentation randomness, and stopping protocol.
- The claimed improvement is relatively modest and could plausibly be affected by tuning variance in the low-resource setting.

### Novelty: **55/100**
Scheduling augmentation difficulty during contrastive training is a reasonable and potentially useful adaptation of curriculum learning. However, the conceptual contribution is fairly incremental: it combines established contrastive intermediate training with a hand-designed easy-to-hard augmentation schedule. The schedule is linear, threshold-based, and not technically sophisticated. The paper would benefit from a clearer distinction from prior work on augmentation curricula and adaptive contrastive learning.

### Significance: **54/100**
Low-resource text classification is important, and a reliable improvement over CERT could be practically useful. The reported gains are strongest in the most label-scarce condition, which supports the motivation. Nevertheless, the evaluation is limited to four relatively standard English datasets, one encoder, and one low-resource protocol. The lack of stronger statistical validation and limited analysis of domain and language transfer reduce the strength of the broader claims.

### Clarity: **78/100**
The paper is generally well organized and easy to follow. The motivation, training pipeline, and main results are presented clearly. However, reproducibility is hindered by underspecified augmentation probabilities, curriculum implementation, baseline configurations, validation sampling, and experimental variance. Some terminology—especially “augmentation strength” and the relationship between curriculum level and operator probabilities—should be made more precise.

## Final score

\[
\frac{52 + 55 + 54 + 78}{4} = \mathbf{59.75}
\]

**Average score: 59.8/100**

## Final recommendation: **Reject**

The idea is plausible and clearly presented, but the empirical evidence is not sufficiently rigorous to support acceptance. A stronger revision should provide a fully specified schedule, fairer baseline tuning, per-seed and significance analyses, clearer data splits, and broader experiments.