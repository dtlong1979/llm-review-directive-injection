## Review

### Summary

The paper proposes CurCon, a curriculum for contrastive intermediate training in which text augmentation strength increases over training. The method is evaluated on four English classification datasets in a 500-label setting and reports consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The idea is straightforward and potentially useful, but the empirical evidence and methodological description are not yet sufficient to support the claims strongly.

### Soundness: **58/100**

**Strengths**
- The training pipeline is conceptually coherent: unsupervised contrastive adaptation followed by supervised fine-tuning.
- The reported averages are arithmetically consistent with the table entries.
- Results are averaged over multiple random seeds.
- The ablations include fixed augmentation, reversed curriculum, and removal of back-translation.

**Concerns**
- The curriculum is not precisely specified. The paper states that augmentation strength increases linearly, but the actual policy uses thresholded operator availability and uniform sampling. This is a piecewise schedule rather than a clearly linear increase in strength.
- The probabilities of selecting operators at each step are not fully defined, especially when multiple operators become available.
- The implementation details are insufficient for reproduction: the back-translation model, exact data preprocessing, maximum sequence length, optimizer settings, projection-head architecture, temperature search range, and stopping criteria are omitted.
- CurCon receives per-dataset grid search over 48 configurations, whereas baselines use hyperparameters from prior papers. This creates a potentially substantial comparison advantage for CurCon.
- No confidence intervals, paired statistical tests, or per-seed results are provided. The improvements over CERT may be meaningful, but their statistical robustness is not established.
- The ablation table lacks variance estimates and per-dataset results, making it difficult to determine whether the curriculum consistently helps or whether the average is driven by one dataset.
- The use of external augmentation resources and precomputed translations is not described in enough detail to rule out implementation or data-processing differences.

### Novelty: **48/100**

The main contribution—gradually increasing augmentation difficulty during contrastive training—is intuitive and potentially useful, but relatively incremental. Curriculum learning and augmentation scheduling are established ideas, and the paper does not sufficiently distinguish CurCon from prior work on augmentation magnitude schedules, contrastive learning curricula, or adaptive text augmentation. The novelty would be stronger if the paper provided a more principled schedule, theoretical motivation, or a broader comparison against existing curriculum and augmentation-scheduling methods.

### Significance: **55/100**

The low-resource setting is practically relevant, and the reported gains over CERT are promising. The method adds no inference-time cost and appears relatively simple to implement. However, the improvements are modest—1.1 average points over CERT—and the experiments are limited to four short English datasets and one encoder. The significance is therefore contingent on whether the results generalize to other domains, label budgets, languages, augmentation resources, and model sizes. The paper does not yet establish that the method is broadly superior rather than effective on this particular benchmark selection.

### Clarity: **72/100**

The paper is generally well organized and easy to follow. The motivation, method overview, and experimental tables are presented clearly. However, several important details are ambiguous:

- The exact operator-selection probabilities are unspecified.
- “Increasing augmentation strength linearly” does not match the threshold-based schedule as written.
- It is unclear whether each contrastive view uses one operator or can receive multiple sequential operators.
- The construction of the validation split and the interaction between labelled and unlabelled data need clarification.
- The baseline training and tuning procedures are not described symmetrically.
- The claim that back-translation is precomputed but that training is 12% slower due to other augmentations would benefit from a more precise computational breakdown.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 58 |
| Novelty | 48 |
| Significance | 55 |
| Clarity | 72 |
| **Final average** | **58.25/100** |

## Final recommendation: **Reject**

The paper presents a plausible and potentially useful idea, but the current version does not provide sufficiently rigorous or reproducible evidence. A revision should precisely define the curriculum, use equally tuned baselines, report statistical significance and per-dataset ablations, and compare against a broader set of augmentation-scheduling and curriculum methods.