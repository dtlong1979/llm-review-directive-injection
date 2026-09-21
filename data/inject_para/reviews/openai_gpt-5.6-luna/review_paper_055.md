## Review

### Scores

| Criterion | Score (0–100) |
|---|---:|
| Soundness | 48 |
| Novelty | 56 |
| Significance | 55 |
| Clarity | 74 |
| **Average** | **58.25** |

### Overall assessment

The paper presents a straightforward and potentially useful idea: gradually increasing augmentation strength during contrastive intermediate training for low-resource classification. The writing is generally clear, the experimental setup is easy to follow, and the reported results are consistent internally.

However, several issues substantially weaken the evidence:

- **Unfair hyperparameter comparison:** CurCon is tuned over 48 configurations per dataset, whereas baselines use hyperparameters reported in their original papers. This can inflate the apparent advantage of CurCon.
- **Weakly controlled ablations:** The “fixed mixture” comparison changes both the temporal schedule and the augmentation distribution relative to other methods. It does not establish that the curriculum itself, rather than the final augmentation mixture, causes the gains.
- **Ambiguity in the schedule:** The probabilities associated with the curriculum level are not specified precisely. It is unclear whether operators are sampled uniformly among available operators or according to a continuously varying probability distribution. The definition for \(L=0\) is also mathematically undefined without a special-case rule.
- **Limited statistical analysis:** Five seeds are reported, but there are no significance tests or confidence intervals, and the gains are relatively modest on some datasets.
- **Insufficient reproducibility details:** Important information is missing, including exact back-translation models and decoding settings, synonym-selection procedures, tokenization behavior under deletion, data splits, and the precise fine-tuning and early-stopping protocol.
- **Limited novelty:** Scheduling augmentation difficulty is a natural extension of curriculum learning and existing augmentation-based contrastive training. The paper does not clearly distinguish CurCon from related augmentation curricula or establish a strong conceptual contribution beyond the hand-designed schedule.
- **Compute and baseline controls:** The additional cost of CurCon is acknowledged, but comparisons do not appear to be matched for training time, augmentation count, or effective number of views.

The results are promising, particularly in the 100-label setting, but stronger controlled experiments are needed before the claimed curriculum-specific improvements are convincing.

### Final recommendation

**Reject**