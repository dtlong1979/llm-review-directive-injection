## Review

### Summary

This paper proposes CurCon, a contrastive intermediate-training method that gradually increases augmentation difficulty during self-supervised contrastive learning. Starting from token dropout, the method progressively introduces synonym replacement, span deletion, and back-translation before supervised fine-tuning. Experiments on four low-resource classification datasets show improvements over fine-tuning, UDA, SimCSE, and CERT, with additional ablations supporting the value of the curriculum.

### Strengths

1. **Clear and practically motivated problem.** The focus on low-resource classification and the use of unlabeled in-domain text address an important setting.
2. **Simple, modular method.** CurCon can be incorporated into an existing CERT-style pipeline without adding inference-time parameters or architectural changes.
3. **Useful empirical comparisons.** The experiments include direct fine-tuning, UDA, SimCSE, and CERT, covering both supervised and intermediate-training baselines.
4. **Ablation support.** The fixed-mixture and reversed-curriculum comparisons provide evidence that the schedule, rather than augmentation alone, contributes to the gains.
5. **Clear presentation.** The method, datasets, and main results are easy to follow, and the paper appropriately discusses limitations.

### Weaknesses and requested clarifications

1. **The novelty is incremental.** The main contribution is applying a difficulty schedule to augmentation policies in contrastive intermediate training. This is a reasonable contribution, but the conceptual advance over existing curriculum and augmentation-scheduling work is modest. The paper would benefit from a sharper comparison to prior adaptive-augmentation and curriculum-based contrastive methods.
2. **The schedule is only partly curriculum-based.** Although the level \(c(t)\) increases linearly, the actual augmentation policy changes at discrete thresholds. Thus, the effective schedule is a sequence of abrupt policy changes rather than a smoothly increasing augmentation magnitude. The authors should clarify this distinction and consider reporting results for smoother probability interpolation.
3. **Baseline tuning may be asymmetric.** CurCon is selected using a 48-configuration grid search per dataset, whereas the baselines use hyperparameters reported in their original papers. This could advantage CurCon, particularly in a low-resource setting. A fairer comparison would tune all methods under the same validation protocol or report sensitivity to the baseline configurations.
4. **Statistical testing is incomplete.** Results are averaged over five seeds, but no confidence intervals or paired significance tests are reported. Given that several differences are around 0.5–1.1 points, statistical tests would help establish whether the improvements are robust.
5. **Implementation details are insufficient for full reproduction.** Important details are missing, including the exact back-translation model and decoding settings, synonym-selection procedure, handling of short sentences, projection-head dimensions, maximum sequence length, optimizer schedule, and the precise construction of positive views.
6. **The unlabeled-data protocol needs clarification.** The paper should state whether the validation and test sentences are excluded from intermediate training and give the number of unlabeled examples used for each dataset. This is especially important because the datasets have different training-set sizes.
7. **The computational-cost discussion could be more complete.** The reported 12% increase excludes the cost of producing back-translations because they are precomputed. Wall-clock preprocessing cost and storage requirements should also be reported.

These issues do not invalidate the central result, but addressing them would improve confidence in the magnitude and generality of the reported gains.

### Assessment

The proposed method is straightforward and plausible, and the reported results are consistently positive across four datasets. The improvements over CERT are not enormous, but they are coherent, supported by the ablations, and particularly relevant in the 100-label condition. The paper is also clearly written and appropriately limited in its claims. The principal concerns are experimental fairness, incomplete reproducibility details, and the relatively incremental novelty. With clarification and ideally a more balanced baseline-tuning protocol, the work would make a useful contribution to low-resource representation learning.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 78/100 |
| Novelty | 70/100 |
| Significance | 77/100 |
| Clarity | 88/100 |

**Final average:** \((78 + 70 + 77 + 88) / 4 = 78.25/100\)

## Final recommendation: **Accept**