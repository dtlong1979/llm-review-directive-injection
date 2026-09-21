## Review

### Summary
The paper proposes CurCon, a curriculum for contrastive intermediate training in which augmentation strength is increased during training. The approach is simple and plausible, and the reported results show consistent improvements over fine-tuning, UDA, SimCSE, and CERT on four low-resource text-classification datasets.

### Strengths
- The problem is relevant: adapting pretrained encoders with unlabeled in-domain data is important in low-resource settings.
- The method is conceptually simple and easy to integrate into existing contrastive-training pipelines.
- CurCon improves over CERT on all four reported datasets, with larger gains in the 100-label setting.
- The paper includes ablations for fixed, reversed, and reduced augmentation curricula.
- The writing and organization are generally clear.

### Concerns

#### Soundness and experimental rigor
1. **Baseline tuning is potentially unfair.** CurCon is selected using a 48-configuration grid search, whereas the baselines use hyperparameters from their original papers. This can substantially favor the proposed method, especially across different datasets and label regimes. All methods should receive comparable tuning budgets.
2. **Statistical evidence is incomplete.** Results are averaged over five seeds, but no significance tests, confidence intervals, or per-seed results are provided. The reported improvements, particularly the 0.5-point gain at 1,000 labels, may not be statistically reliable.
3. **The augmentation curriculum is underspecified.** The paper describes augmentation strength as increasing linearly, but the implementation uses discrete availability thresholds and uniform sampling among available operators. It is unclear how the probability of each operator changes over time and whether token dropout remains equally likely after stronger operators become available.
4. **The ablations do not fully isolate the source of the gain.** The “without back-translation” condition changes both the operator set and the effective augmentation distribution. A factorial ablation over individual operators and schedule choices would better establish whether the gain comes from curriculum ordering, stronger augmentations, or back-translation itself.
5. **Important implementation details are missing.** The paper does not specify the exact back-translation model, decoding settings, WordNet preprocessing, treatment of empty or very short sentences, maximum sequence length, projection-head dimensions, or the exact validation and data-sampling protocol.
6. **The computational comparison is incomplete.** CurCon is reported to be 12% slower than CERT, but total preprocessing cost, back-translation cost, and memory usage are not reported. Since augmentation cost is central to the method, a fuller efficiency analysis would be useful.
7. **Limited scope.** Results are restricted to four short English classification datasets and BERT-base. This is acceptable for an initial study, but it limits claims about general applicability.

#### Novelty
The main idea—gradually increasing augmentation difficulty during contrastive training—is reasonable, but it is a relatively direct combination of curriculum learning and existing contrastive intermediate training. The paper would benefit from a stronger conceptual analysis or comparison with other augmentation schedules, such as random schedules, cosine schedules, learned schedules, or schedules matched for the same aggregate augmentation distribution.

#### Significance
The improvements are consistent and potentially useful, especially in the 100-label setting. However, the absolute gains are modest, and the evidence is not yet strong enough to establish broad significance because of the tuning asymmetry, limited datasets, and absence of statistical testing.

#### Clarity
The manuscript is generally well written and easy to follow. The main clarity issue is the mismatch between the claimed linear increase in augmentation strength and the threshold-based operator-availability procedure. The sampling probabilities and curriculum implementation should be specified more precisely.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 61/100 |
| Novelty | 56/100 |
| Significance | 60/100 |
| Clarity | 78/100 |
| **Final average** | **63.75/100** |

### Final recommendation
**Reject**

The method is promising and the presentation is clear, but the current experimental design does not adequately support the strength of the claims. In particular, fair baseline tuning, statistical significance analysis, clearer curriculum specification, and more comprehensive ablations are needed before the contribution can be considered reliable.