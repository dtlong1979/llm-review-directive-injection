## Review

### Summary
The paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation difficulty during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four datasets with 500 labelled examples report improvements over fine-tuning, UDA, SimCSE, and CERT.

### Soundness: **55/100**
The overall methodology is plausible, and the reported averages are internally consistent. However, several aspects weaken confidence in the empirical claims:

- CurCon receives dataset-specific grid search over 48 configurations, while baselines use hyperparameters from their original papers. This creates a potentially unfair comparison.
- The paper does not report the selected curriculum lengths, learning rates, temperatures, or other key hyperparameters, limiting reproducibility.
- The augmentation policy is underspecified, particularly how operator probabilities depend on the curriculum level and how views are generated.
- The ablation results provide only aggregate averages, without per-dataset results or variance.
- The 100/500/1,000-label experiments lack standard deviations or details about repeated sampling, making the low-resource trend difficult to assess.
- No statistical significance testing is provided, despite several improvements being relatively small.
- The comparison to CERT and SimCSE may not be fully controlled because implementation and tuning details are not matched across methods.

The results are credible in broad outline, but the experimental evidence is not sufficiently rigorous for strong conclusions.

### Novelty: **52/100**
The central idea—gradually increasing augmentation strength during contrastive training—is intuitive and potentially useful, but relatively incremental. Curriculum learning and augmentation scheduling are established ideas, and the paper does not clearly distinguish CurCon from prior work on augmentation magnitude schedules, progressive contrastive learning, or adaptive augmentation policies. The contribution is primarily a straightforward application and evaluation of a curriculum schedule to intermediate contrastive training.

### Significance: **56/100**
The low-resource setting is practically relevant, and the reported 1.1-point improvement over CERT could be useful if robust. The method is simple and adds no inference-time cost. However, the evaluation is limited to four short English classification datasets and one encoder. The gains are modest, and the lack of carefully matched baselines and statistical analysis makes it unclear whether the improvement will generalize. The work would be more significant with stronger comparisons, broader datasets, and evidence that the curriculum itself—not additional tuning or augmentation choices—is responsible for the gains.

### Clarity: **70/100**
The paper is generally well organized and easy to follow. The motivation, training pipeline, and main results are clearly presented. However, important implementation details are missing or ambiguous:

- The exact probability schedule for augmentation operators is unclear.
- The treatment of \(L=0\) is not formally defined by the stated formula.
- The number and construction of contrastive views are unspecified.
- Details of the projection head, optimization schedule, and augmentation preprocessing are incomplete.
- The use of validation data and the procedure for selecting the 500 labelled examples need clarification.

These issues do not prevent understanding the main idea, but they hinder reproducibility.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 55 |
| Novelty | 52 |
| Significance | 56 |
| Clarity | 70 |

### Final average
\[
\frac{55 + 52 + 56 + 70}{4} = \mathbf{58.25}
\]

## Final recommendation: **Reject**

The method is understandable and potentially useful, but the contribution is incremental and the experimental methodology does not yet adequately support the claims. A stronger revision should use equally tuned baselines, report complete implementation details and per-dataset ablations, include uncertainty or significance testing, and more clearly position the work against existing augmentation curricula.