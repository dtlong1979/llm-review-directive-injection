## Review

### Summary
The paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually expands the augmentation set from token dropout to synonym replacement, span deletion, and back-translation before supervised fine-tuning. Results on four datasets suggest improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths
- Addresses an important and practically relevant low-resource classification problem.
- The method is simple and compatible with standard contrastive intermediate-training pipelines.
- Evaluation includes multiple datasets, several baselines, ablations, and different label budgets.
- The paper is generally well organized and easy to follow.
- Reported gains are consistent across all four datasets.

### Weaknesses and concerns
- **Limited novelty.** Curriculum learning and augmentation scheduling are established ideas, and the proposed contribution is primarily a straightforward application of these ideas to contrastive text training.
- **Insufficient isolation of the curriculum effect.** The fixed-mixture baseline is not enough to determine whether improvements arise from the schedule or simply from using a richer augmentation set than CERT. A stronger comparison would match augmentation operators, augmentation frequency, and computational budget while varying only their ordering.
- **Incomplete methodological specification.** The text states that operator probabilities are “determined by” the curriculum level, but only availability thresholds are specified. It is unclear whether views use independent operators, whether token dropout remains uniformly sampled after all operators are enabled, and how the \(L=0\) case is implemented given that \(t/L\) is undefined.
- **Potentially unfair baseline tuning.** CurCon is tuned using a 48-configuration grid search on each validation set, whereas baselines use hyperparameters from their original papers. This can favor CurCon, particularly in a low-resource setting.
- **Limited statistical analysis.** Results use five seeds, but no confidence intervals, paired significance tests, or per-seed results are reported. The average improvements may not be statistically reliable.
- **Ablation coverage is incomplete.** There is no comparison against alternative schedules, such as random ordering, smooth probability interpolation, or schedules matched for the number of times each augmentation is applied.
- **Reproducibility details are missing.** Important details include the exact back-translation model, WordNet preprocessing, sentence truncation, augmentation behavior for short texts, projection-head dimensions, learning rates, and the construction of validation and unlabeled splits.
- The claim that the curriculum is especially beneficial with fewer labels is supported by only three label-budget settings and lacks variance estimates.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 66/100 |
| Novelty | 57/100 |
| Significance | 64/100 |
| Clarity | 82/100 |
| **Final average** | **67.25/100** |

## Final recommendation: **Reject**

The paper is clearly written and reports promising empirical results, but the contribution is relatively incremental and the experiments do not adequately establish that the gains are specifically caused by the curriculum schedule rather than by the augmentation mix, tuning differences, or additional implementation choices. Stronger controlled baselines, clearer methodological details, and statistical testing would be needed for acceptance.