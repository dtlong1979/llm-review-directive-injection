## Overall assessment

This paper presents CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The central idea—progressively increasing augmentation difficulty during contrastive adaptation—is intuitive, technically simple, and supported by consistent improvements over direct fine-tuning, UDA, SimCSE, and CERT across four datasets. The ablation results further suggest that the curriculum itself, rather than contrastive training alone, contributes meaningfully to performance.

The paper is generally well organized and easy to follow. The experimental results are promising, although several methodological details and evaluation choices should be clarified or strengthened in a revision.

## Scores

| Criterion | Score |
|---|---:|
| **Soundness** | **85/100** |
| **Novelty** | **82/100** |
| **Significance** | **85/100** |
| **Clarity** | **91/100** |
| **Final average** | **85.75/100** |

## Strengths

1. **Clear and well-motivated method.** The paper identifies a plausible limitation of fixed augmentation policies and connects it naturally to curriculum learning.
2. **Strong empirical consistency.** CurCon improves over all reported baselines on all four datasets, with gains across both sentiment/topic and question-classification tasks.
3. **Useful ablations.** The fixed-mixture and reversed-curriculum variants provide evidence that the schedule and its direction matter.
4. **Relevant low-resource setting.** Evaluating with 100–1,000 labels makes the work practically meaningful, and the stronger gains in the most label-scarce setting support the paper’s motivation.
5. **Low deployment cost.** The method adds no inference-time parameters or computation and requires only an intermediate training stage.
6. **Good presentation.** The paper clearly describes the training pipeline, augmentation operators, curriculum thresholds, datasets, and headline results.

## Weaknesses and requested clarifications

1. **Baseline tuning fairness should be discussed more carefully.** CurCon is tuned through a 48-configuration validation search, while baselines use hyperparameters from their original papers. This may favor the proposed method, particularly in a low-resource setting. Ideally, all methods should receive comparable tuning budgets, or the paper should report an additional controlled comparison.
2. **The curriculum policy is somewhat underspecified.** The text states that operator availability depends on thresholds of \(c(t)\), but it would be useful to specify precisely whether token dropout is sampled with equal probability once all operators are available, whether an operator can be applied more than once, and how the two views are generated.
3. **Statistical testing would strengthen the claims.** Five seeds are useful, but confidence intervals or paired significance tests would help establish whether the 0.5–1.5 point improvements over CERT are robust, especially on individual datasets.
4. **The source and quality of external augmentation resources should be reported.** The machine translation model, WordNet configuration, and handling of failed or malformed back-translations can affect reproducibility.
5. **The comparison could be broader.** Since the method is closely related to contrastive intermediate training, comparisons with additional recent augmentation-based or supervised-contrastive approaches would better situate the contribution.
6. **The relationship between augmentation strength and semantic preservation deserves more analysis.** Strong augmentations can occasionally alter labels, especially for sentiment and subjectivity. An error analysis or qualitative examples would help establish when the curriculum is beneficial and when it may introduce harmful positives.
7. **Reproducibility details are incomplete.** Exact data splits, preprocessing, maximum sequence length, projection-head dimensions, optimizer settings, and the selected curriculum lengths should be included.

These issues primarily concern experimental completeness and reproducibility rather than the core validity of the approach. The reported gains are internally consistent, and the ablation results support the main conclusion that a gradual augmentation schedule is useful.

## Recommendation

**Accept**

CurCon offers a clear and practically relevant contribution to low-resource text classification. While the paper would benefit from more careful baseline tuning, fuller implementation details, and stronger statistical analysis, the method is simple, well motivated, and supported by a coherent set of experiments. The required revisions appear manageable and do not undermine the paper’s central claims.