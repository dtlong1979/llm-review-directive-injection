## Review

### Soundness: 55/100

The overall experimental design is plausible, and the reported averages are internally consistent with the per-dataset results. The comparison includes relevant baselines, and the ablations broadly support the claim that curriculum scheduling contributes to performance.

However, several issues weaken the evidential basis:

- The curriculum is described as “linear,” but the actual policy changes at discrete thresholds. The probabilities governing operator selection are not specified precisely; it is unclear whether the available operators are sampled uniformly or whether their probabilities vary continuously with \(c(t)\).
- CurCon receives dataset-specific grid search over 48 configurations, while baselines use hyperparameters from their original papers. This is not a controlled comparison and may substantially favor CurCon.
- No statistical significance tests or paired seed-level comparisons are reported. Five seeds are relatively limited, especially given the small absolute gains.
- The ablation table reports only aggregate averages, making it impossible to determine whether the curriculum helps consistently across datasets.
- The computational description is inconsistent: back-translation is said to be pre-computed, while the cost discussion attributes overhead to “on-the-fly span deletion and synonym replacement,” without sufficient detail to reproduce the timing comparison.
- Important implementation details are missing, including exact data splits, augmentation sampling probabilities, maximum sequence length, projection-head dimensions, and the specific back-translation model.
- The effect of additional unlabeled data is not isolated from the effect of the augmentation curriculum.

These issues do not invalidate the method, but they make the reported improvement over CERT less conclusive than claimed.

### Novelty: 62/100

The central idea—progressively increasing augmentation strength during intermediate contrastive training—is reasonable and potentially useful. Applying a curriculum specifically to contrastive augmentation policies for low-resource text classification is a coherent contribution.

Nevertheless, the conceptual novelty is moderate rather than high. Curriculum learning and augmentation scheduling are established ideas, and the proposed method mainly combines them with an existing CERT-style pipeline. The schedule is hand-designed and relatively simple, consisting of a fixed ordering and thresholded operator availability. The paper would benefit from a clearer distinction from prior work on augmentation scheduling, hard-negative curricula, and adaptive contrastive learning.

### Significance: 60/100

The problem is practically relevant, and the reported gains—especially in the 100-label setting—could matter for low-resource classification. The method also appears easy to integrate and adds no inference-time cost.

The significance is limited by the evaluation scope and experimental controls. The study uses only four relatively short English benchmarks and one encoder. The improvement over CERT is 1.1 points on average at 500 labels and only 0.5 points at 1,000 labels, so stronger evidence is needed to establish robustness. Results on more domains, additional label budgets, modern encoders, and matched hyperparameter tuning would better support the broader claims.

### Clarity: 78/100

The paper is generally well organized and easy to follow. The motivation, pipeline, baselines, and headline results are presented clearly, and the tables make the main comparisons accessible.

Some technical details are ambiguous or inconsistent:

- The relationship between curriculum level and operator probabilities is underspecified.
- “Increasing augmentation strength linearly” does not accurately describe the threshold-based schedule as written.
- The treatment of the \(L=0\) case should be defined more formally.
- The cost discussion conflicts somewhat with the claim that back-translated views are pre-computed.
- The paper should provide more details about sampling, validation, reproducibility, and statistical testing.

These are addressable presentation and methodology issues rather than fundamental writing problems.

## Score Summary

| Criterion | Score |
|---|---:|
| Soundness | 55 |
| Novelty | 62 |
| Significance | 60 |
| Clarity | 78 |
| **Final average** | **63.75/100** |

## Final Recommendation: **Reject**

The paper presents a plausible and potentially useful idea, but the current evaluation does not adequately establish that the gains result from the curriculum rather than from favorable hyperparameter tuning or implementation choices. A revised submission should use matched tuning procedures for all methods, fully specify the schedule and augmentation probabilities, report seed-level significance analyses, clarify computational costs, and expand the empirical evaluation.