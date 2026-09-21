## Overall assessment

This paper presents CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The central idea—gradually increasing augmentation strength during contrastive adaptation—is intuitive and reasonably motivated. The experiments show consistent improvements over the reported baselines across four datasets, and the ablations support the claim that the curriculum contributes beyond simply using a fixed augmentation mixture.

However, the empirical evidence is not yet as rigorous as it could be. The method is relatively incremental, several implementation details are underspecified, and the hyperparameter-selection protocol creates a potentially unfair comparison with baselines whose original hyperparameters are used without comparable tuning. These issues limit the strength of the claims but do not invalidate the core contribution.

### Strengths

- The method is simple, easy to understand, and adds no inference-time cost.
- CurCon improves over CERT on all four reported datasets.
- The ablation study includes both a fixed-mixture variant and a reversed curriculum, which is useful for isolating the effect of ordering.
- The analysis by number of labelled examples is aligned with the paper’s motivation and shows larger gains in the more label-scarce setting.
- The paper is generally well organized and clearly written.

### Weaknesses and concerns

1. **Limited novelty.** The contribution is a relatively straightforward application of curriculum learning to augmentation strength in contrastive training. The paper should more carefully distinguish its method from prior work on augmentation schedules, hard-negative curricula, and adaptive contrastive learning.

2. **Unclear augmentation policy.** The curriculum defines when operators become available, but does not fully specify whether the probability of selecting an operator changes continuously with \(c(t)\), or whether the policy is uniform over all currently available operators. The phrase “probability ... is determined by \(c(t)\)” is therefore somewhat inconsistent with the subsequent threshold-based description.

3. **Potentially unfair baseline tuning.** CurCon is selected using a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters from their original papers. Baseline-specific tuning, or at least a common tuning budget, would make the comparison more convincing.

4. **Insufficient statistical analysis.** Results are averaged over five seeds, but no paired significance tests or confidence intervals for method differences are reported. Since several gains are relatively small, especially at 1,000 labelled examples, this would be valuable.

5. **Reproducibility details are incomplete.** The paper should report the exact sampling probabilities, tokenizer and sequence-length settings, treatment of failed or low-quality back-translations, WordNet configuration, optimizer schedule, and the precise construction of the validation sets.

6. **Ablation scope.** The fixed-mixture baseline is useful, but further controls would help determine whether gains come from the curriculum itself or from the particular final operator mixture. For example, comparing equal-compute schedules, independently tuned fixed policies, and schedules with the same expected augmentation strength would strengthen the causal claim.

7. **Limited breadth.** The experiments cover only short English texts and one encoder family. This is acceptable for an initial study, but the conclusions should be framed accordingly.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 72/100 |
| Novelty | 65/100 |
| Significance | 71/100 |
| Clarity | 86/100 |
| **Final average** | **73.5/100** |

## Recommendation: **Accept**

The paper offers a clear and practically relevant method with consistent empirical gains and a reasonably informative ablation study. The contribution is incremental rather than fundamentally novel, and the evaluation would benefit from fairer baseline tuning, more precise methodological specification, and stronger statistical analysis. Nevertheless, these are addressable weaknesses, and the reported results support acceptance, particularly for a venue interested in empirical methods for low-resource NLP.