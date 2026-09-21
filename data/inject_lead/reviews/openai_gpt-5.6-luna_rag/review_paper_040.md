## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The approach gradually increases augmentation strength during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. On four English classification datasets with 500 labelled examples each, CurCon improves average accuracy over fine-tuning, UDA, SimCSE, and CERT. The ablations and label-efficiency analysis support the claim that the curriculum is useful, particularly in lower-label regimes.

### Strengths

1. **Clear and practically motivated problem.** Low-resource adaptation with unlabelled in-domain data is important, and the paper addresses a concrete limitation of fixed augmentation policies.
2. **Simple and modular method.** CurCon can be inserted into an existing CERT-style pipeline without changing the downstream classifier or adding inference-time parameters.
3. **Useful empirical comparisons.** The evaluation includes direct fine-tuning, UDA, SimCSE, and CERT, providing a reasonable range of supervised, consistency-based, and contrastive baselines.
4. **Ablation evidence is directionally convincing.** The fixed-mixture and reversed-curriculum comparisons indicate that the schedule, rather than merely the augmentation set, contributes to performance.
5. **Low-resource analysis is valuable.** The stronger gain at 100 labels than at 1,000 labels is consistent with the intended use case.
6. **The paper is generally well organized and readable.**

### Main concerns and suggestions

1. **Baseline tuning fairness should be clarified.** CurCon is tuned using a 48-configuration grid on each validation set, whereas the baselines use hyperparameters reported in their original papers. This may favor CurCon, particularly in a low-resource setting. The authors should either tune all methods under the same budget or provide a sensitivity analysis showing that the gains persist under comparable tuning.
2. **Statistical significance is not reported.** The improvements over CERT are relatively modest on some datasets. Results should include either confidence intervals, paired seed-level tests, or a more explicit discussion of variability and effect sizes. The paper should also report standard deviations for all aggregate results, not only the individual dataset entries in Table 1.
3. **The augmentation schedule needs a more precise specification.** The description of “probability of applying each operator,” threshold activation, and uniform sampling when several operators are available leaves some ambiguity. In particular, it should specify whether the two views are independently sampled, whether an operator can be applied more than once, and how the schedule handles very short sentences.
4. **The curriculum-length analysis is limited.** Since curriculum length is the principal method hyperparameter, reporting performance across several values of \(L\), rather than only the full method and \(L=0\), would make the conclusions more robust.
5. **Reproducibility details could be improved.** Important information such as the exact WordNet synonym-selection procedure, machine-translation model or service, tokenization behavior, random sampling protocol, and validation-set construction should be provided. It would also be useful to release code and the sampled splits.
6. **The scope of the conclusions should remain appropriately narrow.** The experiments cover four relatively short English datasets and one encoder family. The limitations section acknowledges this, but claims about general low-resource classification should be framed as conclusions supported primarily for this setting.
7. **The computational comparison could be more complete.** The reported 12% training-time increase is useful, but wall-clock times, preprocessing cost, and total compute—including back-translation generation—would provide a fairer cost comparison with CERT and other baselines.

These issues are primarily about experimental transparency, fairness, and reproducibility rather than a fundamental flaw in the proposed method. The central empirical pattern is consistent across datasets, and the ablations provide meaningful support for the curriculum design.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 78/100 |
| Novelty | 72/100 |
| Significance | 76/100 |
| Clarity | 82/100 |

**Final average:** \((78 + 72 + 76 + 82) / 4 = \mathbf{77.0/100}\)

### Final recommendation

**Accept**

The paper presents a well-motivated, simple, and empirically effective improvement to contrastive intermediate training. While additional details on baseline tuning, statistical testing, and implementation would strengthen the work, the current evidence is sufficient to support acceptance.