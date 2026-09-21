## Review

### Summary

This paper introduces CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The approach begins contrastive training with relatively mild augmentations and progressively enables stronger augmentations, including synonym replacement, span deletion, and back-translation. Across four classification benchmarks with 500 labelled examples, CurCon outperforms fine-tuning, UDA, SimCSE, and CERT, with an average accuracy of 88.9 versus 87.8 for CERT. The ablations suggest that the curriculum itself contributes approximately 0.8 accuracy points over a fixed augmentation mixture.

### Strengths

1. **Clear and practically motivated problem.** The focus on improving intermediate contrastive training in low-label regimes is relevant, and the motivation for gradually increasing augmentation difficulty is intuitive.
2. **Simple, model-agnostic method.** CurCon does not alter the downstream fine-tuning procedure or add inference-time parameters.
3. **Consistent empirical gains.** CurCon achieves the best result on all four datasets and improves over CERT by 1.1 average accuracy points.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that the schedule, rather than only the set of augmentations, contributes to performance.
5. **Low-resource analysis.** Results at 100, 500, and 1,000 labelled examples support the claim that the method is especially useful in more label-scarce settings.
6. **The limitations are appropriately acknowledged.** The paper clearly notes the restricted language, model, and domain coverage.

### Weaknesses and Suggestions

1. **Statistical reporting could be strengthened.** The main table reports standard deviations over five seeds, but no confidence intervals or significance tests are provided. Since some gains are relatively modest, especially on TREC, paired seed-level comparisons would better establish robustness. This is a reporting improvement rather than a fundamental concern.

2. **Baseline tuning is not fully symmetric.** CurCon is tuned using a 48-configuration grid on each validation set, whereas the baselines use hyperparameters from their original papers. This may advantage the proposed method. A stronger comparison would tune all methods under the same computational budget and validation protocol, or at least include a sensitivity analysis for CERT and the other baselines.

3. **The curriculum definition is somewhat ambiguous.** The paper describes augmentation strength as increasing linearly, but the actual policy enables operators at discrete thresholds of 0.25, 0.5, and 0.75. Moreover, once multiple operators are available, they are sampled uniformly, so the resulting augmentation distribution is piecewise constant rather than linearly varying. The authors should clarify the exact sampling probabilities and formally define the \(L=0\) case, since \(t/L\) is otherwise undefined.

4. **The augmentation-strength ordering could use additional justification.** Token dropout, synonym replacement, span deletion, and back-translation are plausibly ordered by difficulty, but this ordering is not empirically validated. An experiment comparing alternative operator orderings or measuring semantic similarity between positive pairs would make the curriculum interpretation more convincing.

5. **Reproducibility details are incomplete.** The paper would benefit from reporting the exact sampling procedure for labelled and validation subsets, the number of unlabelled examples, temperature and learning-rate ranges, early-stopping criteria, projection-head dimensions, and the translation model used for back-translation. These omissions do not undermine the central results but would make replication easier.

6. **Scope is currently limited.** All datasets are English, relatively short, and conventional benchmarks, and only BERT-base is evaluated. The claims should remain framed around this setting. A larger or more domain-diverse evaluation would strengthen the paper’s broader applicability, but the current experiments are sufficient to support the stated contribution.

7. **The computational comparison could be more complete.** CurCon is reported to be approximately 12% slower than CERT, but wall-clock times and preprocessing costs are not provided. Since back-translation is precomputed, separating preprocessing time from training time would clarify the practical trade-off.

8. **The gain attributable specifically to curriculum scheduling is moderate.** The 0.8-point improvement over the fixed mixture is meaningful but not large. The paper appropriately presents the curriculum as an incremental improvement over contrastive intermediate training; it should avoid implying that the curriculum alone accounts for the full improvement over fine-tuning.

### Overall Assessment

The paper presents a coherent and useful improvement to contrastive intermediate training. Its methodological novelty is incremental—the core ingredients are contrastive adaptation, standard text augmentations, and curriculum learning—but their combination is well motivated and supported by consistent results and targeted ablations. The experimental design has several limitations, particularly concerning symmetric hyperparameter tuning, statistical testing, and incomplete implementation details. These issues are addressable through clarification and additional reporting and do not invalidate the main conclusion.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 83/100 |
| Novelty | 77/100 |
| Significance | 80/100 |
| Clarity | 87/100 |

**Final average:** \((83 + 77 + 80 + 87) / 4 = 81.75\), or **81.8/100**

## Final Recommendation

**Accept**

The method is clearly described, empirically effective, and relevant to low-resource text classification. The requested clarifications and stronger statistical/baseline reporting would improve the paper, but the contribution is sufficiently sound and useful for acceptance.