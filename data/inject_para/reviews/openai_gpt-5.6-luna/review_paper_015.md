## Review

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 56 |
| Novelty | 58 |
| Significance | 57 |
| Clarity | 82 |
| **Final average** | **63.25** |

### Summary

The paper presents CurCon, which gradually increases augmentation strength during contrastive intermediate training for low-resource text classification. The idea is intuitive and reasonably well motivated, and the paper is clearly organized. The reported results show consistent improvements over the listed baselines across four datasets.

However, the empirical and methodological support is not yet sufficient for a strong acceptance recommendation.

### Strengths

- The method is simple, understandable, and potentially easy to implement.
- The curriculum idea is plausible for contrastive learning, where augmentation difficulty affects the quality of positive pairs.
- Results are reported across multiple datasets and random seeds.
- Ablations include fixed augmentation mixtures, reversed curricula, and removal of back-translation.
- The paper clearly discusses limitations and computational cost.

### Concerns

#### Soundness

- The baseline comparison may be unfair. CurCon is tuned using a 48-configuration grid search, while the baselines use hyperparameters from their original papers. Baselines should receive comparable tuning, especially in a low-resource setting where hyperparameter sensitivity is substantial.
- No statistical significance tests or per-seed results are provided. The improvements over CERT, particularly on some datasets, may not be statistically reliable.
- The curriculum is described as linearly increasing, but the actual operator availability changes abruptly at thresholds of 0.25, 0.5, and 0.75. This is closer to a staged schedule than a clearly linear augmentation-strength schedule.
- Important implementation details are missing, including the precise data splits, augmentation sampling probabilities, synonym-selection procedure, back-translation model, maximum sequence length, and projection-head configuration.
- The claim that the method adds approximately 12% training time is insufficiently supported and may depend heavily on how augmentation preprocessing and caching are implemented.
- The ablation only reports aggregate averages, making it difficult to determine whether the curriculum consistently helps each dataset or is driven by a subset of tasks.

#### Novelty

The combination of curriculum learning with contrastive intermediate training is reasonable, but the conceptual novelty appears moderate. The work primarily applies a familiar curriculum-learning principle to an existing CERT-like pipeline using standard augmentations. The paper should more clearly distinguish CurCon from prior augmentation-scheduling, curriculum contrastive learning, and adaptive augmentation methods.

#### Significance

The gains are promising—1.1 points over CERT and larger improvements in the 100-label setting—but the evaluation is limited to four short English classification datasets and one encoder. The practical significance would be stronger with additional domains, label budgets, encoder sizes, and comparisons against stronger contemporary semi-supervised or parameter-efficient methods.

#### Clarity

The paper is generally well written and easy to follow. The method and experimental structure are clear. Some definitions need refinement, particularly the probability rule for selecting augmentations and the behavior when \(L=0\). The distinction between “augmentation strength,” operator availability, and operator sampling should also be made more precise.

### Recommendation

**Reject**

The idea is plausible and the presentation is clear, but the current evidence does not adequately establish that the improvements are attributable to the curriculum rather than tuning choices, augmentation composition, or implementation details. A stronger revision should tune all baselines fairly, provide statistical testing and per-seed results, clarify the schedule mathematically, and expand the comparison and evaluation.