## Review

### Summary
The paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation strength during contrastive training, progressing from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four datasets with 500 labelled examples report improvements over fine-tuning, UDA, SimCSE, and CERT.

### Soundness: **55/100**
The central idea is plausible and the experimental setup is broadly appropriate, but several issues weaken confidence in the results:

- The augmentation schedule is not specified precisely enough to reproduce. In particular, the relationship between curriculum level and operator probabilities is unclear.
- CurCon receives a per-dataset grid search over 48 configurations, whereas baselines use hyperparameters from their original papers. This may create an unfair comparison.
- No statistical significance tests or per-seed results are reported, despite the paper emphasizing low-resource instability.
- The source and construction of the 500 labelled and 200 validation examples are ambiguous.
- The claim that precomputed back-translations make the method only 12% slower should be explained more carefully, including preprocessing cost.
- Important implementation details are missing, including the exact unlabelled-data sizes, maximum sequence length, projection-head dimensions, and back-translation system.
- The ablation table does not isolate all relevant factors, such as the effect of the augmentation mixture independently of the schedule or the effect of each individual operator.

The results are internally plausible, but the evidence is not yet sufficiently rigorous to support the strength of the claims.

### Novelty: **62/100**
Scheduling augmentation strength during contrastive training is a reasonable and potentially useful extension, but the conceptual novelty is moderate. The method combines established ingredients—CERT-style intermediate contrastive learning, common text augmentations, and curriculum learning—with a hand-designed schedule. The paper would need stronger positioning against prior work on augmentation curricula and adaptive contrastive learning to establish that the contribution is substantially new.

### Significance: **65/100**
The problem is important, and improvements in the low-resource regime could be practically valuable. The reported gains over CERT are meaningful, particularly with 100 labelled examples. However, the evaluation is limited to four relatively small English classification datasets and one encoder. The lack of broader comparisons, statistical testing, and domain or language diversity limits the generality and significance of the conclusions.

### Clarity: **78/100**
The paper is generally well organized and easy to follow. The motivation, training pipeline, and main findings are clearly presented. However, reproducibility is hindered by underspecified augmentation probabilities, data splits, hyperparameters, and computational accounting. The claim that each operator has an “increasing strength” is also not empirically justified, since augmentation difficulty can be dataset- and sentence-dependent.

## Final Score

\[
\frac{55 + 62 + 65 + 78}{4} = \mathbf{65.0}
\]

## Recommendation: **Reject**

The paper presents a sensible method with promising preliminary results, but the current evidence does not establish soundness strongly enough for acceptance. A revised version should provide a fairer baseline tuning protocol, precise schedule and implementation details, stronger ablations, significance analysis, and broader evaluation.