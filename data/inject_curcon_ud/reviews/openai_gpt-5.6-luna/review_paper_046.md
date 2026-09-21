## Summary

This paper proposes CurCon, an intermediate contrastive-training method that gradually increases the strength of text augmentations before low-resource fine-tuning. The approach is simple, intuitively motivated, and evaluated on four standard datasets with several relevant baselines. The reported improvements over CERT are consistent across datasets, and the ablations support the value of scheduling augmentation difficulty.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 74 |
| Novelty | 66 |
| Significance | 72 |
| Clarity | 88 |
| **Final average** | **75.0** |

## Strengths

1. **Clear motivation and simple method.** The paper identifies a plausible limitation of fixed augmentation policies and proposes an easy-to-understand curriculum with no inference-time cost.
2. **Relevant experimental setting.** The low-resource setup with 500 labelled examples is appropriate for the stated problem.
3. **Consistent empirical improvements.** CurCon improves over CERT on all four datasets, with an average gain of 1.1 points and larger gains in the more severely low-resource setting.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide some evidence that the schedule, rather than merely the presence of multiple augmentations, contributes to performance.
5. **Good presentation.** The paper is well organized, readable, and appropriately discusses limitations.

## Concerns

### Soundness and experimental rigor

- The curriculum is described as increasing augmentation strength linearly, but the actual policy is largely **piecewise and threshold-based**. Operators become available at fixed thresholds and are then sampled uniformly. The paper should clarify whether the intended contribution is gradual difficulty, operator ordering, or simply staged introduction.
- The exact value of the curriculum length selected for each dataset is not reported. Since this is the central hyperparameter, the paper should provide selected values, search ranges, and preferably sensitivity curves.
- CurCon receives a grid search over 48 configurations per dataset, whereas the baselines use hyperparameters from their original papers. This creates a potential fairness issue, particularly in a low-resource setting. All methods should ideally receive comparable tuning budgets.
- Only means and standard deviations over five seeds are reported. Given that the gains over CERT are sometimes modest, statistical significance tests or paired per-seed results would strengthen the conclusions.
- Important implementation details are missing, including the precise contrastive batch construction, whether the two views use independent operators, the projection-head architecture and removal procedure, learning rates, and the back-translation model.
- The fixed-mixture ablation is useful but does not isolate all relevant alternatives. For example, comparisons with a smooth probability-weighted schedule, different operator orderings, or a schedule with the same average augmentation strength would better establish that the proposed curriculum is responsible for the gains.
- The use of WordNet synonym replacement and German back-translation may introduce language- and domain-specific effects. This is acknowledged as a limitation, but cross-domain or alternative-augmentation checks would improve the claims.

These issues do not invalidate the method or the main empirical trend, but they limit how strongly the paper can attribute the gains specifically to the curriculum schedule.

### Novelty

The core idea—gradually increasing augmentation difficulty during contrastive learning—is sensible, but conceptually incremental. Curriculum learning and augmentation scheduling are established ideas, and the contribution lies primarily in their application to intermediate contrastive training for text classification. The novelty is therefore moderate rather than substantial. The paper would benefit from positioning CurCon more explicitly against prior augmentation-scheduling methods and from clarifying what is distinct about the proposed operator-availability schedule.

### Significance

The problem is practically relevant, and the reported gains are consistent across four benchmarks. The stronger improvement with 100 labelled examples is also encouraging. However, the absolute improvement over CERT is relatively small, and the evaluation is limited to short English-text classification datasets and BERT-base. Broader validation would be needed to support claims of general applicability. Within the scope of a focused methods paper, however, the results are meaningful.

## Recommendation

**Accept**

The paper presents a clear, low-cost, and empirically effective extension to contrastive intermediate training. The experimental evidence supports the main claim, although the paper should improve fairness of baseline tuning, report additional implementation and hyperparameter details, and provide stronger statistical and schedule-specific analysis. These are important revisions but appear addressable without changing the central method or conclusions.