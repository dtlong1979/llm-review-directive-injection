## Review

### Scores

| Criterion | Score (0–100) |
|---|---:|
| Soundness | 48 |
| Novelty | 58 |
| Significance | 57 |
| Clarity | 72 |
| **Average** | **58.75** |

### Summary

The paper presents a simple and potentially useful idea: gradually increasing the strength of text augmentations during contrastive intermediate training for low-resource classification. The experimental results are promising, and the paper is generally easy to follow. However, several methodological ambiguities and evaluation concerns substantially weaken the evidence for the claims.

### Soundness

The main concern is that the proposed “linear” curriculum is not actually clearly defined as a linear increase in augmentation strength. The schedule uses hard thresholds for introducing operators, followed by uniform sampling among available operators. This produces a stepwise policy rather than a linearly increasing augmentation magnitude. In addition, the \(L=0\) case is mathematically undefined under \(c(t)=\min(1,t/L)\), requiring an unstated special-case implementation.

The comparison may also be unfair: CurCon’s learning rate, temperature, and curriculum length are selected by a 48-configuration grid search, whereas baselines use hyperparameters from their original papers. Baselines should receive comparable tuning, especially under a changed data regime and with a fixed computational budget.

Important experimental details are missing or unclear, including how the 200 validation examples are drawn relative to the 500 labelled examples, whether the same data splits are used across methods and seeds, the exact contrastive objective and projection-head configuration, the construction of positive views, and the handling of failed or low-quality WordNet and translation augmentations. There are also no statistical significance tests or confidence intervals across datasets, making it difficult to determine whether the reported improvements are robust.

The results are plausible, but the current description does not fully support the strength of the conclusions.

### Novelty

The central contribution—scheduling augmentation difficulty during contrastive intermediate training—is reasonably distinct from standard CERT and SimCSE. However, it is a relatively direct combination of established curriculum-learning and contrastive-learning ideas. The schedule is hand-designed and simple, and the paper does not establish a strong conceptual or algorithmic advance beyond this combination.

Novelty is therefore moderate rather than high. The work could become more compelling with comparisons to adaptive augmentation schedules, augmentation-magnitude interpolation, or existing curriculum-based contrastive methods.

### Significance

The problem is practically relevant, and improvements in the 100–500-label regime would be valuable. The reported gains over CERT are meaningful, particularly on SST-2 and SUBJ. The absence of inference-time cost is also attractive.

Nevertheless, the evidence is limited to four short English classification datasets and one encoder. The gains are relatively modest at 1,000 labels, and the paper does not test domain shift, longer documents, multilingual data, or alternative pretrained models. Since the key contribution is a training schedule, a more extensive study of robustness, computational cost, and sensitivity to augmentation choices would be important.

### Clarity

The paper is well organized and communicates the basic method and results clearly. Tables are easy to interpret, and the limitations section appropriately acknowledges several constraints.

Clarity is reduced by underspecified methodological details. In particular, the probability distribution over augmentation operators is not fully formalized, the relationship between curriculum level and augmentation strength is imprecise, and the data-splitting protocol is ambiguous. The cost comparison also needs clarification: if back-translated views are precomputed, the source of the reported 12% overhead should be explained more precisely.

## Final recommendation

**Reject**

The idea is promising and the presentation is reasonably clear, but the current experimental protocol and method specification are not sufficiently rigorous to substantiate the claimed improvements. A revised version should use equally tuned baselines, precisely define the curriculum and data splits, report statistical tests and per-seed results, and include stronger comparisons and sensitivity analyses.