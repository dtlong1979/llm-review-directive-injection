## Review

### Summary

This paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually expands the augmentation policy from token dropout to synonym replacement, span deletion, and back-translation during contrastive pretraining. Experiments on four benchmarks with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The paper also includes ablations, label-budget comparisons, and a computational-cost discussion.

### Strengths

1. **Clear and practically motivated problem.** The focus on low-resource classification and the use of unlabelled in-domain text address an important practical setting.
2. **Simple, modular method.** CurCon can be incorporated into an existing CERT-style pipeline without changing the downstream classifier or adding inference-time parameters.
3. **Consistent empirical gains.** The method improves over CERT on all four datasets, with a reported average gain of 1.1 accuracy points and larger gains in the more label-scarce setting.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons directly investigate whether the schedule and its direction matter.
5. **Good presentation.** The paper is well organized, readable, and gives a sufficiently clear high-level description of the training pipeline and curriculum schedule.

### Concerns and suggestions

1. **Statistical testing is limited.** Results are averaged over five seeds, but the paper does not report confidence intervals or significance tests for the differences between CurCon and CERT. Since several gains are approximately one point, paired significance testing or confidence intervals would strengthen the conclusions.
2. **Baseline tuning and fairness need clarification.** CurCon is selected through a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters from their original papers. This may favor CurCon, particularly in the low-resource regime. A stronger comparison would tune all methods under the same validation protocol or report sensitivity analyses.
3. **The augmentation policy is underspecified.** The text states that an operator becomes “available” after a threshold and that available operators are sampled uniformly, but it is not fully clear whether each view independently samples an operator, whether augmentations can be composed, or how token dropout is treated after additional operators become available. These details should be stated precisely.
4. **The interpretation of augmentation strength is somewhat assumptive.** Back-translation, span deletion, synonym replacement, and token dropout do not necessarily form a universally ordered difficulty scale. The paper would benefit from measuring pair difficulty, semantic preservation, or contrastive loss under each operator rather than relying only on the hand-designed ordering.
5. **Data and preprocessing details could be expanded.** The construction of the unlabelled pool, handling of duplicate examples, filtering of failed translations, sentence-length truncation, and WordNet coverage are not described. These factors may affect reproducibility and performance.
6. **The computational-cost analysis is brief.** The reported 12% overhead is useful, but the paper should distinguish preprocessing cost from training-time cost and provide absolute runtimes or resource usage. It would also be informative to report the cost of generating back-translations.
7. **Scope is appropriately acknowledged but narrow.** The evaluation uses only short English classification datasets and BERT-base. Additional domains or languages would improve the evidence, although this limitation does not undermine the central contribution.

### Overall assessment

The central idea is straightforward but useful: scheduling augmentation difficulty appears to improve contrastive intermediate training in a low-resource setting. The experiments consistently support the proposed method, and the ablations provide evidence that the curriculum—not merely the inclusion of strong augmentations—contributes to the gains. The main weaknesses concern experimental reporting, baseline tuning fairness, statistical validation, and precise specification of the augmentation procedure. These are addressable issues and do not require a change to the core method or conclusions.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 78/100 |
| Novelty | 75/100 |
| Significance | 78/100 |
| Clarity | 87/100 |

**Final average:** \((78 + 75 + 78 + 87) / 4 = 79.5/100\)

## Final recommendation

**Accept**

The paper presents a clear and empirically supported contribution with practical relevance. Strengthening the reporting of statistical significance, baseline tuning, preprocessing, and augmentation details would improve the final version, but the current evidence is sufficient for acceptance.