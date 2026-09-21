## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation difficulty during contrastive pretraining, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations suggest that both the curriculum and the ordering of augmentation strengths contribute to performance.

### Strengths

1. **Clear problem motivation.** The paper addresses a practically important setting in which only a few hundred labelled examples are available.
2. **Simple and modular method.** CurCon can be incorporated into an existing CERT-style pipeline without modifying the downstream fine-tuning procedure or adding inference-time parameters.
3. **Consistent empirical gains.** CurCon improves over CERT on all four datasets and achieves an average gain of 1.1 accuracy points over the strongest baseline.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that the training schedule, rather than merely the use of multiple augmentations, matters.
5. **Low-resource analysis.** Results across 100, 500, and 1,000 labelled examples support the claim that the method is particularly useful when annotations are scarce.
6. **Readable presentation.** The paper is well organized, the method is easy to follow, and the main findings are stated clearly.

### Concerns and suggestions

1. **Schedule specification could be more precise.** Although the paper describes the schedule as linear, the stated policy changes mainly at discrete thresholds. It would be useful to specify the exact operator sampling probabilities as a function of training step and clarify whether the curriculum controls availability, probability, or augmentation magnitude.
2. **Baseline tuning and fairness require more detail.** CurCon is tuned over 48 configurations, whereas baselines use hyperparameters reported in their original papers. For a stronger comparison, the authors should clarify whether comparable tuning budgets were used for all methods or provide a sensitivity analysis.
3. **Statistical testing is missing.** Means and standard deviations over five seeds are reported, but confidence intervals or paired significance tests would strengthen the claims, especially for the relatively small gains over CERT on some datasets.
4. **Ablation coverage could be expanded.** Since CurCon combines four operators, per-operator ablations and comparisons against a random or smoothly weighted schedule would help isolate whether the benefit comes from the ordering, the gradual availability, or the particular augmentation set.
5. **Reproducibility details should be expanded.** The paper should report the exact BERT checkpoint, maximum sequence length, optimizer settings, temperature values, early-stopping criteria, translation model, synonym-selection procedure, and handling of failed or invalid augmentations.
6. **Limited scope.** The evaluation is restricted to English, short-text datasets, and BERT-base. This is appropriately acknowledged, but experiments on at least one longer-text or cross-domain setting would improve the evidence for generality.

These issues are primarily presentation, reproducibility, and experimental-strength concerns rather than fundamental flaws. The core method is technically plausible, and the reported results and ablations are internally consistent with the paper’s claims.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 82/100 |
| Novelty | 78/100 |
| Significance | 82/100 |
| Clarity | 89/100 |
| **Final average** | **82.75/100** |

### Overall assessment

CurCon is a straightforward but useful extension of contrastive intermediate training. Its main novelty lies in applying a curriculum to augmentation strength in this setting, and the experiments provide consistent evidence that the proposed schedule improves low-resource classification performance. The empirical scope and reporting could be strengthened, particularly regarding baseline tuning, statistical significance, and exact schedule details, but these limitations do not undermine the central contribution.

## Final recommendation: **Accept**