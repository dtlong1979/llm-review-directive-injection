## Review

### Summary

The paper proposes CurCon, which applies a curriculum over text augmentations during contrastive intermediate training. The method begins with token dropout and progressively enables synonym replacement, span deletion, and back-translation before supervised fine-tuning. Results on four low-resource classification datasets show improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is practically relevant: exploiting unlabelled data when only a few hundred labels are available.
- The method is simple and potentially easy to integrate into existing contrastive-training pipelines.
- The experimental comparison includes several relevant baselines.
- Results are reported over multiple seeds, and the paper includes ablations and label-budget analysis.
- The manuscript is generally well organized and easy to follow.

### Concerns

#### Soundness

The central methodological description is underspecified and does not fully support the claims.

1. **The proposed schedule is not actually clearly linear in augmentation strength.** The schedule linearly increases \(c(t)\), but augmentation operators are introduced through discrete thresholds. Once an operator is enabled, its perturbation magnitude appears fixed. Thus, the method is more accurately a staged or thresholded augmentation policy than a linearly increasing augmentation-strength schedule.

2. **The probability policy is ambiguous.** The paper states that token dropout is “always available,” while other operators become available at thresholds, and that available operators are sampled uniformly. It is unclear whether token dropout is selected with equal probability alongside all enabled operators, whether operator probabilities change continuously, and how views are generated.

3. **The ablation does not isolate the curriculum effect cleanly.** The fixed-mixture baseline differs from CurCon not only in curriculum order but also in the distribution of augmentations over training. A stronger ablation would match the total number and frequency of each operator while varying only their ordering.

4. **Baseline tuning is potentially unfair.** CurCon is tuned through a 48-configuration validation search on each dataset, whereas baselines use hyperparameters from their original papers. This can substantially favor CurCon, especially under a new low-resource protocol.

5. **The experimental evidence is limited.** Only four relatively short English datasets and five seeds are used. No statistical significance tests or per-seed results are provided, and the average improvements are relatively small for some comparisons.

6. **Data-use details are incomplete.** The paper should clarify whether validation examples were excluded from the unlabelled contrastive pool, how the 500 examples were sampled across seeds, and whether any label or split information could indirectly enter intermediate training.

7. **Reproducibility is insufficient.** Important details are missing, including the exact back-translation model, WordNet preprocessing, maximum sequence length, optimizer schedule, projection-head dimensions, augmentation behavior for short sentences, and the precise implementation of the reversed curriculum.

The numerical results are internally consistent, but the methodological and evaluation details are not sufficiently complete to establish that the gains are caused specifically by the proposed curriculum.

#### Novelty

The idea of gradually increasing augmentation difficulty is intuitive and related to existing curriculum-learning and augmentation-scheduling work. Applying it to contrastive intermediate training for text classification is a reasonable adaptation, but the conceptual novelty is modest. The paper would need a stronger distinction from prior augmentation curricula, adaptive augmentation methods, and contrastive-learning schedules.

#### Significance

The problem is important, and the reported gains—particularly in the 100-label setting—could be useful if they survive stronger controls. However, the current evidence does not establish broad significance because:

- the benchmark set is small;
- the method depends on external augmentation resources;
- the computational cost increases;
- the strongest baseline comparison may not be fairly tuned; and
- the improvements may partly reflect augmentation-mixture or hyperparameter differences rather than curriculum learning itself.

#### Clarity

The paper is well structured and readable overall. The motivation, pipeline, and headline results are clear. However, the curriculum policy is ambiguous, and terms such as “augmentation strength,” “available,” and “full strength” are not precisely defined. The experimental protocol and baseline-tuning procedure also need more detail.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 42/100 |
| Novelty | 46/100 |
| Significance | 50/100 |
| Clarity | 72/100 |
| **Final average** | **52.5/100** |

## Final recommendation: **Reject**

The paper presents a plausible and potentially useful idea, but the current submission does not provide sufficiently rigorous or reproducible evidence that the curriculum itself produces the reported improvements. A revised version should clarify the augmentation schedule, tune baselines under the same protocol, add controlled distribution-matched ablations, report statistical testing and per-seed results, and provide substantially more implementation detail.