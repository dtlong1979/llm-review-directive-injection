## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The approach gradually increases augmentation difficulty during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations suggest that both the augmentation curriculum and back-translation contribute to the gains.

### Strengths

1. **Clear and practical motivation.** The focus on low-resource classification and the use of unlabelled in-domain text address an important applied setting.
2. **Simple, modular method.** CurCon can be incorporated into an existing CERT-style training pipeline without modifying inference or supervised fine-tuning.
3. **Consistent empirical improvements.** The method improves over CERT on all four datasets and reports gains across multiple labelled-data regimes.
4. **Useful ablations.** The comparison against a fixed mixture, a reversed curriculum, removal of back-translation, and no contrastive stage directly investigates the claimed contribution.
5. **Seed averaging and uncertainty reporting.** Reporting five-seed means and standard deviations is appropriate for low-resource experiments.
6. **Good presentation.** The method, experimental setup, and limitations are described in a generally clear and readable manner.

### Weaknesses and concerns

1. **Novelty is incremental.** The central contribution is a hand-designed scheduling strategy applied to an existing CERT-style contrastive-training pipeline. The conceptual combination is reasonable, but the methodological novelty is moderate rather than substantial.
2. **The curriculum definition is somewhat ambiguous.** The paper describes an increase in augmentation strength, but the actual schedule appears to activate operators at thresholds and then sample uniformly among available operators. This is a discrete availability schedule rather than a fully specified linear increase in augmentation probability or magnitude. More precise pseudocode and exact sampling probabilities would improve reproducibility.
3. **Baseline tuning may not be fully comparable.** CurCon is selected using a 48-configuration grid search on each validation set, whereas baselines use hyperparameters from their original papers. This may favor the proposed method. Ideally, all methods should receive comparable tuning budgets, or the paper should report results under a controlled tuning protocol.
4. **Limited statistical analysis.** The improvements are plausible, but significance tests or confidence intervals over seeds would help establish whether the 0.5-point gain at 1,000 labels and some per-dataset gains are robust.
5. **Dataset and model scope is narrow.** The evaluation uses four relatively short English classification datasets and only BERT-base. This is sufficient for an initial study, but it limits conclusions about generality.
6. **Some implementation details are missing.** Important details include the exact back-translation model and decoding configuration, how WordNet replacement failures are handled, whether augmentations are independently sampled for the two views, and whether unlabelled examples include validation or test-adjacent data.
7. **Compute and preprocessing comparisons could be more explicit.** Since back-translation is precomputed for all methods involving it, the reported 12% overhead should distinguish preprocessing cost, storage cost, and training-time cost.

These concerns are mainly about rigor and reproducibility rather than evidence that the main result is incorrect. The consistent gains, curriculum ablation, reversed-curriculum comparison, and low-label analysis provide reasonable support for the central claim.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 80/100 |
| Novelty | 74/100 |
| Significance | 79/100 |
| Clarity | 88/100 |

### Final average

\[
\frac{80 + 74 + 79 + 88}{4} = \frac{321}{4} = 80.25
\]

**Final average score: 80.25/100**

## Final recommendation: **Accept**

The paper presents a clear and useful method with consistent empirical improvements and relevant ablations. Its main limitation is moderate novelty and some incompleteness in experimental and implementation details, particularly the fairness of baseline tuning and the precise definition of the curriculum. These issues should be addressed in revision, but they do not outweigh the paper’s practical contribution and coherent experimental evidence.