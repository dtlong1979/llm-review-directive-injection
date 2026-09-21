## Overall assessment

This paper presents a straightforward curriculum for contrastive intermediate training: augmentation strength is increased during the unsupervised contrastive stage, followed by low-resource supervised fine-tuning. The motivation is plausible and the paper is generally readable. However, the empirical evidence is not sufficiently rigorous to support the claims, and the methodological novelty appears limited. Several important implementation and comparison details are underspecified, and the baseline tuning protocol is potentially unfair.

### Strengths

- Addresses a practically relevant low-resource classification problem.
- The proposed curriculum is simple, interpretable, and potentially easy to implement.
- Includes multiple datasets, ablations, and label-budget comparisons.
- Reports variation across random seeds rather than only single-run results.
- The paper is clearly organized and the main idea is easy to understand.

### Major concerns

1. **Limited methodological novelty.** The contribution is primarily a hand-designed schedule over known augmentation operators. The connection between curriculum learning and increasing augmentation strength is intuitive, and the paper does not clearly distinguish CurCon from prior augmentation curricula or contrastive-learning schedules.

2. **Unfair or insufficiently controlled baselines.** CurCon is tuned over 48 configurations separately for each dataset, whereas the baselines use hyperparameters from their original papers. This can substantially favor the proposed method, especially in a low-resource setting. All methods should receive comparable tuning budgets.

3. **Insufficient statistical evidence.** Five seeds are relatively few, and no significance tests or paired per-seed comparisons are provided. The improvements over CERT are only 0.5–1.5 points on individual datasets, so it is unclear whether they are statistically reliable.

4. **Ambiguity in the curriculum definition.** The paper describes a linear schedule, but the actual operator availability changes through abrupt thresholds at 0.25, 0.5, and 0.75. It is not clear whether augmentation strength changes continuously, whether each view receives independently sampled operators, or how positive pairs are constructed.

5. **Weak ablation design.** The fixed-mixture baseline is not necessarily matched to the curriculum in expected augmentation severity or compute. Additional controls are needed, including:
   - fixed weak, medium, and strong policies;
   - random operator schedules;
   - schedules with the same operator frequencies but shuffled order;
   - schedules matched for total augmentation severity;
   - multiple curriculum lengths.

6. **Potential label and data-split ambiguity.** The manuscript should clearly specify whether the 500 labelled examples, 200 validation examples, and unlabelled examples are disjoint, and whether the remaining training examples are treated as unlabelled after their labels are discarded. It should also report results across multiple sampled labelled subsets, not merely multiple optimization seeds.

7. **Reproducibility gaps.** Important details are missing, including the precise back-translation model, synonym-selection procedure, handling of short sentences, tokenization behavior after deletion, projection-head dimensions, temperature values, learning rates, and early-stopping protocol. No code or data-sampling protocol is indicated.

8. **Scope of evidence.** Results cover only four short English classification datasets and one encoder family. The reported gains may reflect dataset-specific interactions with WordNet, back-translation, or sentence length rather than a generally useful curriculum principle.

## Scores

| Criterion | Score (0–100) |
|---|---:|
| Soundness | 35 |
| Novelty | 43 |
| Significance | 44 |
| Clarity | 72 |

**Final average:** \((35 + 43 + 44 + 72)/4 = 48.5\)

## Final recommendation: **Reject**

The idea is understandable and potentially useful, but the current submission does not establish that the curriculum itself is responsible for the reported gains. A substantially stronger experimental design, fairer baseline tuning, clearer methodological specification, and statistical validation would be needed for acceptance.