## Overall assessment

CurCon presents a straightforward and plausible curriculum strategy for contrastive intermediate training in low-resource text classification. The empirical results are consistently positive across four datasets, and the ablations support the central claim that gradually increasing augmentation difficulty is more effective than either a fixed mixture or a reversed curriculum. The method is simple, incurs no inference-time cost, and is relevant to practical low-resource settings.

The main concerns relate to experimental rigor and reproducibility rather than to a fundamental flaw in the method. In particular, CurCon receives dataset-specific grid search while the baselines use hyperparameters from their original papers, and the paper does not report statistical significance tests or confidence intervals for the method comparisons. These issues should be addressed or explicitly discussed, but they do not undermine the overall contribution.

## Strengths

- The method is simple, intuitive, and easy to integrate into an existing CERT-style pipeline.
- CurCon improves over all reported baselines on all four datasets.
- The ablation comparing the full curriculum, fixed mixture, and reversed curriculum directly tests the proposed mechanism.
- The low-resource analysis shows that the benefit is larger with 100 labels than with 1,000 labels, matching the motivation.
- The paper clearly states important limitations, including dependence on English resources and the use of a hand-designed schedule.
- The computational overhead is modest and there is no inference-time parameter or latency cost.

## Weaknesses and suggestions

1. **Baseline tuning is not fully matched.** CurCon is selected using a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters from their original papers. This may advantage the proposed method, particularly in a low-resource regime. A stronger comparison would tune all methods under the same validation protocol or provide a sensitivity analysis showing that the gains are robust to reasonable baseline hyperparameters.

2. **Statistical evidence is limited.** Five random seeds provide useful information, but the paper does not report confidence intervals, paired significance tests, or per-seed results. Since the average gain over CERT is 1.1 points and some individual improvements are relatively small, significance testing would help establish whether the improvements are robust.

3. **The curriculum definition could be more precise.** The schedule is described as linearly increasing, but the actual policy changes at discrete thresholds and samples uniformly among the currently available operators. It would be useful to specify whether “augmentation strength” refers to operator availability, operator probability, or expected perturbation magnitude. The \(L=0\) case should also be defined separately because \(t/L\) is otherwise undefined.

4. **Reproducibility details are incomplete.** The paper should identify the back-translation model and decoding settings, specify the WordNet synonym-selection procedure, state how empty or excessively shortened sequences are handled, and report the maximum sequence length and preprocessing rules. Details of the contrastive projection head, temperature search range, learning-rate schedule, and checkpoint selection would also improve reproducibility.

5. **The scope of the evidence is somewhat narrow.** All experiments use short English classification benchmarks and BERT-base. The limitations acknowledge this appropriately, but an additional domain-shifted or longer-text dataset would strengthen the claim that the method is broadly useful.

6. **Potential augmentation-quality effects deserve analysis.** The observed gain may partly reflect the inclusion or timing of back-translation rather than curriculum structure alone. The fixed-mixture and reversed-curriculum ablations are helpful, but reporting matched operator-frequency controls and results for individual augmentation schedules would better isolate the curriculum effect.

7. **The unlabelled-data protocol should be clarified.** The paper states that the remaining training sentences are used without labels, but it would be useful to specify whether the same unlabelled pool is used across all seeds and whether validation sentences are excluded from contrastive training. This is important for ensuring a clean evaluation protocol.

These are primarily presentation, fairness, and experimental-completeness issues. The reported results and ablations nevertheless provide reasonable support for the central contribution.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 78/100 |
| Novelty | 72/100 |
| Significance | 76/100 |
| Clarity | 84/100 |

**Final average:** \((78 + 72 + 76 + 84) / 4 = 77.5/100\)

## Final recommendation

**Accept**

The paper makes a useful and well-motivated contribution, with consistent empirical improvements and a clear mechanism-focused ablation. Addressing the fairness of hyperparameter tuning, adding statistical significance analysis, and expanding implementation details would substantially strengthen the final version, but the current work is suitable for acceptance.