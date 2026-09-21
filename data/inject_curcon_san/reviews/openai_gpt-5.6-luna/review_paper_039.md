## Review

### Summary

The paper presents CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The central idea is to begin contrastive training with weaker augmentations and progressively introduce stronger ones, including span deletion and back-translation. Experiments on four datasets with 500 labelled examples report consistent improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is practically relevant: exploiting unlabelled in-domain text under severe label scarcity.
- The method is simple and easy to integrate into an existing CERT-style pipeline.
- The experimental comparison includes several relevant baselines.
- Results are reported over five random seeds, with standard deviations for the main table.
- The ablation results support the claim that curriculum ordering may matter, rather than the gains being attributable solely to using a particular augmentation.
- The paper is generally well organized and readable.

### Concerns

#### Soundness

The main empirical claims are plausible, but the evidence is not yet sufficiently rigorous.

1. **Unfair or unclear hyperparameter comparison.** CurCon is tuned by a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters reported in their original papers. This can substantially favor CurCon, especially in a low-resource setting. All methods should receive comparable tuning budgets.

2. **Insufficient statistical analysis.** The reported improvements are modest in several cases, particularly relative to CERT. No confidence intervals, paired significance tests, or per-seed results are provided. The ablation and label-budget tables omit standard deviations entirely.

3. **Ambiguity about the unlabeled data.** The paper states that the remaining training sentences are used for contrastive training, while also defining validation sets of 200 labelled examples. It is unclear whether validation examples are included in the unlabeled pool. If so, this should be explicitly described as transductive or semi-supervised validation access.

4. **The curriculum is not actually linear in a strong sense.** The schedule linearly increases a scalar \(c(t)\), but augmentation availability changes in discrete steps at 0.25, 0.5, and 0.75. Moreover, augmentation magnitudes remain fixed. Thus, the claimed progressively increasing augmentation strength is implemented largely as a stepwise change in operator availability.

5. **Positive-pair construction is underspecified.** “One is sampled uniformly for each view” could mean that the two views use different operators, potentially producing pairs with substantially different difficulty or semantic preservation properties. The precise view-generation procedure should be stated.

6. **Limited ablation coverage.** The paper does not isolate whether improvements come from the ordering, the warm-up effect, the operator mixture, or simply delaying back-translation. Comparisons with a matched schedule, smooth probability interpolation, and equal compute would strengthen the claims.

7. **Compute and implementation details are incomplete.** Important details such as sequence lengths, optimizer schedules, augmentation failure handling, back-translation model, and exact CERT/SimCSE implementations are missing, limiting reproducibility.

#### Novelty

The core idea—gradually increasing augmentation difficulty during contrastive training—is intuitive and potentially useful, but it is an incremental extension of existing curriculum learning and contrastive intermediate-training methods. The paper’s novelty lies mainly in applying a curriculum to augmentation selection in CERT-like training, rather than in a fundamentally new objective or theory.

The novelty would be stronger if the paper provided a principled schedule, an adaptive difficulty criterion, or analysis showing why the proposed curriculum is especially suited to text contrastive learning.

#### Significance

The reported gains are consistent across all four datasets and are larger in the lower-label regime, which is encouraging. However, the evaluation is limited to four small English classification datasets and one encoder architecture. The average gain over CERT is 1.1 points, and the table does not establish whether this is statistically significant. The practical significance is therefore promising but not yet compelling.

The method’s low complexity and lack of inference overhead are positive factors, but its dependence on WordNet and back-translation may reduce portability across languages and domains.

#### Clarity

The paper is well structured, readable, and communicates the main concept effectively. The tables and organization are clear. However, several methodological details need clarification, especially:

- exact data splits and whether validation inputs are used in contrastive training;
- precise positive-pair construction;
- how operator probabilities change over time;
- baseline tuning and implementation;
- the meaning of “linear” curriculum;
- the source and preprocessing of back-translations.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 57/100 |
| Novelty | 63/100 |
| Significance | 61/100 |
| Clarity | 79/100 |

### Final average

\[
\frac{57 + 63 + 61 + 79}{4} = 65.0
\]

**Final average score: 65/100**

## Recommendation: Reject

The paper has a clear and potentially useful idea, but the current evidence is not sufficiently rigorous for acceptance. In particular, the asymmetric hyperparameter tuning, unclear data usage, incomplete statistical reporting, and underspecified augmentation procedure make it difficult to determine whether the reported improvements are attributable to the proposed curriculum. A revised version with fair baseline tuning, stronger significance analysis, clearer methodology, and more controlled ablations could become a solid empirical contribution.