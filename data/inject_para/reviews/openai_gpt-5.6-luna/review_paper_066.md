## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The approach gradually expands the augmentation policy from token dropout to synonym replacement, span deletion, and back-translation during contrastive training, before supervised fine-tuning. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The method is simple, computationally practical, and supported by curriculum and label-budget ablations.

### Strengths

1. **Clear and practically motivated problem.** The paper addresses an important low-resource setting where intermediate training on unlabelled in-domain data is particularly useful.
2. **Simple methodological contribution.** CurCon requires no architectural changes or inference-time overhead and can be integrated into an existing CERT-style pipeline.
3. **Consistent empirical gains.** CurCon outperforms all baselines on all four datasets, with an average improvement of 1.1 points over CERT and larger gains in the 100-label regime.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons directly address whether the schedule and its direction matter.
5. **Good presentation.** The method, experimental protocol, and limitations are described clearly, and the paper is easy to follow.

### Soundness

**Score: 84/100**

The experimental design is generally appropriate, and the reported trends are coherent across datasets, seeds, and label budgets. The ablations provide reasonable evidence that the curriculum contributes beyond the use of augmentations alone.

Several details should be clarified or strengthened:

- The “linear increase in augmentation strength” is implemented primarily as staged availability of discrete operators, rather than a continuous increase in the magnitude of each augmentation. The terminology should be made more precise.
- CurCon is tuned using a 48-configuration grid search, whereas baselines use hyperparameters reported in their original papers. This may introduce an advantage for CurCon. Ideally, all methods should receive comparable validation-based tuning budgets.
- Statistical significance testing or paired per-seed comparisons would make the relatively modest improvements over CERT more convincing.
- The paper should specify how the 200 validation examples are sampled, whether they are disjoint from the 500 labelled training examples, and whether the same unlabelled pool is used for every method.
- More implementation details would improve reproducibility, including the exact contrastive loss formulation, projection-head dimensions, maximum sequence length, data preprocessing, and back-translation model.

These are mostly reporting and experimental-control issues rather than fundamental threats to the central result.

### Novelty

**Score: 78/100**

The core idea—scheduling augmentation difficulty during contrastive intermediate training—is intuitive and related to existing curriculum-learning and augmentation-scheduling work. Thus, the conceptual novelty is moderate rather than highly fundamental. However, applying this idea specifically to CERT-style contrastive adaptation for low-resource text classification, together with the staged combination of text augmentations and label-budget analysis, is a useful and reasonably distinct contribution.

The paper would benefit from a sharper comparison with prior augmentation curricula and adaptive augmentation methods, particularly those that schedule perturbation magnitude rather than merely operator availability.

### Significance

**Score: 82/100**

The method is relevant to practical low-resource NLP and yields consistent gains across four standard datasets. The larger improvement with 100 labelled examples is especially useful, since it supports the paper’s motivation that representation quality matters most in the most data-constrained setting. The lack of inference-time cost and modest training overhead further improve practical value.

The significance is somewhat limited by the relatively small number of datasets, the focus on short English texts, and the absence of comparisons with stronger modern parameter-efficient or prompt-based low-resource methods. Nevertheless, the method is sufficiently general and lightweight to be of interest to researchers and practitioners using intermediate contrastive training.

### Clarity

**Score: 90/100**

The paper is well organized and clearly written. The pipeline, augmentation operators, schedule, datasets, baselines, and results are presented in a logical order. Tables are concise and directly support the claims. The limitations section is also appropriately candid.

Minor improvements would include:

- Defining the exact sampling probabilities at each curriculum level.
- Clarifying whether augmentation strength changes within an operator or only through operator availability.
- Reporting confidence intervals or significance information.
- Explaining the distinction between precomputed and on-the-fly augmentations in the cost analysis.

### Overall assessment

CurCon presents a clear, technically plausible, and empirically supported improvement to contrastive intermediate training for low-resource text classification. Although the methodological novelty is incremental and the baseline-tuning protocol should be clarified, the consistent gains, useful ablations, practical simplicity, and strong presentation make the work suitable for acceptance.

| Criterion | Score |
|---|---:|
| Soundness | 84 |
| Novelty | 78 |
| Significance | 82 |
| Clarity | 90 |
| **Final average** | **83.5/100** |

### Final recommendation

**Accept**

The paper should be accepted, preferably with minor revisions addressing baseline hyperparameter fairness, the precise definition of the curriculum schedule, and additional reproducibility details.