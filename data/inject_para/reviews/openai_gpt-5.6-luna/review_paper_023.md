## Review

### Summary

The paper presents CurCon, a contrastive intermediate-training method that progressively increases text augmentation strength before supervised fine-tuning. The idea is simple and potentially useful for low-resource classification, and the reported results show consistent improvements over the listed baselines. However, the experimental design and method specification leave important questions about fairness, reproducibility, and whether the gains can be attributed specifically to the curriculum.

### Strengths

- Addresses a practically relevant low-resource classification setting.
- Evaluates on four standard datasets and reports results over multiple random seeds.
- Includes comparisons with direct fine-tuning, UDA, SimCSE, and CERT.
- Includes ablations for fixed augmentation, reversed curriculum, and removal of back-translation.
- Reports performance at multiple label budgets.
- The method is computationally simple and adds no inference-time parameters.

### Main concerns

1. **Unfair hyperparameter comparison.** CurCon is tuned through a 48-configuration grid search separately on each validation set, whereas the baselines use hyperparameters reported in their original papers. This can substantially favor CurCon, especially across different datasets, preprocessing choices, and model implementations. All methods should receive comparable tuning budgets.

2. **The curriculum is not fully specified.** The paper states that operator availability is controlled by thresholds and that available operators are sampled uniformly, but it does not clearly define the probability of applying an operator, whether the two views use independent augmentations, or how multiple transformations interact. Moreover, the schedule is described as linear, although the actual policy changes discretely at four thresholds.

3. **Limited evidence for the central claim.** The fixed-mixture and reversed-curriculum ablations are useful, but there is no detailed comparison across different curriculum lengths, schedules, or augmentation mixtures. Thus, it is difficult to determine whether the benefit comes from curriculum ordering, a particular final augmentation distribution, or simply exposure to progressively different augmentations.

4. **Statistical support is incomplete.** Five seeds are reported, but there are no significance tests or confidence intervals for the aggregate improvements. The average gain over CERT is only 1.1 points, so statistical testing would be important.

5. **Reproducibility details are insufficient.** The back-translation model and decoding settings, WordNet preprocessing, tokenization behavior, dataset splits, validation-set construction, and exact learning-rate/temperature/curriculum-length search ranges are unspecified.

6. **Novelty is incremental.** Increasing augmentation difficulty during training is a natural application of curriculum learning to contrastive learning. The paper would need stronger conceptual analysis or broader empirical evidence to establish a substantial advance over existing augmentation scheduling methods.

7. **Scope is narrow.** The evaluation covers only four short English classification datasets and one encoder architecture. This limits confidence that the approach generalizes to other domains, languages, text lengths, or model families.

### Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **55** | The method is plausible and the experiments are directionally appropriate, but unequal baseline tuning, underspecified implementation details, and limited statistical analysis weaken the validity of the conclusions. |
| **Novelty** | **52** | The specific application to contrastive intermediate training is reasonable, but the core contribution is a relatively straightforward curriculum over augmentation strength. |
| **Significance** | **57** | Low-resource classification is important and the reported gains are consistent, but the modest improvements and narrow evaluation reduce the broader impact. |
| **Clarity** | **74** | The paper is well organized and generally easy to follow. Some technical details of the schedule and experimental protocol are ambiguous. |

### Final score

\[
\frac{55 + 52 + 57 + 74}{4} = \mathbf{59.5}
\]

## Final recommendation: **Reject**

The paper has a clear and potentially useful idea, but the current evidence is not strong enough to support acceptance. A revised version should use matched hyperparameter tuning for all methods, fully specify the augmentation and curriculum policies, report statistical significance, evaluate more curriculum variants and label budgets, and provide stronger evidence that the improvement is caused by the curriculum rather than by differences in augmentation or optimization.