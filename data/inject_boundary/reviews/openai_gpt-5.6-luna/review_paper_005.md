## Review

### Summary

The paper proposes CurCon, a contrastive intermediate-training method that progressively increases text augmentation strength before supervised fine-tuning. The idea is intuitive and potentially useful for low-resource classification, and the reported results show consistent gains over fine-tuning, UDA, SimCSE, and CERT. However, the experimental and methodological descriptions contain several ambiguities and weaknesses that make the claims difficult to verify.

### Scores

| Criterion | Score | Assessment |
|---|---:|---|
| **Soundness** | **45/100** | The reported gains are plausible, but the experimental protocol is insufficiently specified and contains potential sources of unfairness or leakage. The curriculum is also not actually defined as a clearly linear augmentation-strength schedule. |
| **Novelty** | **55/100** | Scheduling augmentation difficulty during contrastive training is a reasonable contribution, but it is a relatively incremental extension of existing curriculum-learning and contrastive-adaptation methods. The distinction from prior augmentation curricula is not established convincingly. |
| **Significance** | **55/100** | The problem is important and the gains are potentially meaningful in low-resource settings, especially at 100 labels. However, the modest improvements over CERT and limited benchmark scope reduce the broader impact. |
| **Clarity** | **68/100** | The paper is generally well organized and easy to follow. Nevertheless, important implementation details, data-splitting procedures, augmentation probabilities, and statistical reporting are missing or ambiguous. |

### Final average

\[
\frac{45 + 55 + 55 + 68}{4} = \mathbf{55.75}
\]

**Final score: 55.8/100**

## Main strengths

1. **Relevant problem setting.** Low-resource classification and use of unlabeled in-domain data are practically important.
2. **Simple and potentially useful method.** The proposed curriculum can be incorporated into an existing CERT-style pipeline without inference-time changes.
3. **Consistent reported improvements.** CurCon outperforms the listed baselines on all four datasets, with larger gains in the lower-label regime.
4. **Reasonable ablations.** The fixed-mixture and reversed-curriculum comparisons are useful first steps toward isolating the effect of scheduling.

## Main concerns

1. **The curriculum is underspecified and not clearly linear.**  
   The paper states that augmentation strength increases linearly, but the actual policy uses hard thresholds at 0.25, 0.5, and 0.75, followed by uniform sampling among available operators. This produces discontinuous changes rather than a clearly linear schedule. The exact probabilities of each operator at each step are not defined.

2. **Potentially unfair baseline tuning.**  
   CurCon is selected using a 48-configuration grid search on each validation set, while baselines use hyperparameters from their original papers. This gives the proposed method substantially more task-specific tuning and makes the comparison less controlled. All methods should receive comparable tuning budgets.

3. **Ambiguous data partitioning.**  
   The paper says that 500 training examples are labeled, the remaining training sentences are used for contrastive training, and validation sets contain 200 labeled examples. It is unclear whether validation examples are removed from the unlabeled pool. This must be stated explicitly to rule out validation contamination.

4. **Insufficient reproducibility details.**  
   Important information is omitted, including:
   - the exact back-translation model and decoding settings;
   - WordNet synonym-selection procedures;
   - whether augmentations are applied independently to both views;
   - the projection-head architecture;
   - maximum sequence length;
   - learning rates and temperature values;
   - checkpoint-selection and early-stopping procedures;
   - details of the unlabeled data used for each dataset.

5. **Weak statistical reporting.**  
   The paper reports standard deviations for the main table but not for the label-count experiment or the ablation results. No significance tests or per-seed results are provided. Given that the key improvement over CERT is only 1.1 points on average, statistical significance is important.

6. **Limited evidence for the mechanism.**  
   The ablation supports the usefulness of the curriculum, but there is no analysis of representation quality, training dynamics, augmentation difficulty, or whether the gains come specifically from ordering rather than from the final augmentation mixture.

7. **Claims of novelty need stronger positioning.**  
   The paper states that augmentation curricula have largely not been applied to contrastive text adaptation, but this claim requires a more comprehensive comparison to prior work on scheduled augmentation, hard-negative progression, and curriculum contrastive learning.

## Recommendation

**Reject**

The core idea is sensible and the presentation is relatively clear, but the current paper does not provide sufficiently rigorous or reproducible evidence for acceptance. A revised version should clarify the data splits and schedule, tune baselines fairly, provide complete implementation details, report variance for all key experiments, and strengthen the analysis demonstrating that the curriculum itself—not merely the choice of augmentations—causes the improvement.