## Review

### Summary

This paper introduces CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method progressively increases augmentation difficulty during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. Across four datasets and several baselines, CurCon reports consistent improvements, especially when only 100–500 labelled examples are available.

### Strengths

- **Clear motivation:** The paper identifies a plausible limitation of fixed augmentation policies and connects it to curriculum-learning principles.
- **Simple and practical method:** CurCon is easy to understand, adds no inference-time parameters, and can be integrated into existing CERT-style pipelines.
- **Empirical consistency:** CurCon improves over CERT on all four datasets and shows gains across multiple label regimes.
- **Useful ablations:** The fixed-mixture and reversed-curriculum comparisons support the claim that both curriculum scheduling and schedule direction matter.
- **Appropriate low-resource focus:** The analysis with 100, 500, and 1,000 labels provides evidence that the method is particularly useful in scarce-label settings.
- **Good presentation:** The paper is well organized, technically readable, and provides sufficient high-level implementation details to understand the experimental pipeline.

### Weaknesses and requested clarifications

1. **Baseline fairness and tuning:** CurCon is tuned through a 48-configuration grid search, whereas the baselines use hyperparameters from their original papers. This may favor CurCon, particularly in a low-resource setting. Ideally, all methods should receive comparable validation-based tuning budgets.
2. **Schedule specification:** The description of operator availability is somewhat ambiguous. It would be useful to specify the exact probability distribution over operators at each curriculum level, including whether token dropout remains equally likely after stronger operators become available.
3. **Statistical testing:** The reported standard deviations are helpful, but paired significance tests or confidence intervals would strengthen the claims that the improvements over CERT are reliable.
4. **Ablation completeness:** The paper would benefit from reporting single-augmentation baselines and alternative schedules, such as nonlinear or randomly ordered curricula. This would better isolate whether the gains arise from curriculum structure rather than simply from the augmentation mixture.
5. **Unlabelled-data protocol:** The paper should clarify whether the validation and test sentences, or any externally sourced data, are excluded from contrastive training. This is important for assessing possible transductive effects.
6. **Reproducibility details:** Exact model checkpoints, tokenizer settings, maximum sequence length, augmentation implementation details, and the back-translation system should be provided.

These issues primarily concern experimental transparency and evaluation rigor rather than the core idea. They appear addressable without changing the central conclusions.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 85 |
| Novelty | 78 |
| Significance | 83 |
| Clarity | 90 |

**Final average:** \((85 + 78 + 83 + 90) / 4 = 84.0\)

### Final recommendation

**Accept**

The paper presents a well-motivated, simple, and empirically effective contribution. Although additional detail on baseline tuning, augmentation probabilities, data separation, and statistical significance would improve the evaluation, the consistent gains and informative ablations provide sufficient support for acceptance.