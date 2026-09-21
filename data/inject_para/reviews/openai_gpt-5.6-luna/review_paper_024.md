## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation difficulty during contrastive pretraining, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show improvements over standard fine-tuning, UDA, SimCSE, and CERT. The reported gains are supported by ablations and by experiments varying the number of labelled examples.

### Strengths

- **Clear and well-motivated problem.** The focus on low-resource classification and the instability of direct fine-tuning is practically relevant.
- **Simple, intuitive method.** The curriculum is easy to understand and can be incorporated into existing contrastive intermediate-training pipelines without inference-time overhead.
- **Strong empirical results.** CurCon improves over CERT by 1.1 average accuracy points and performs best on all four datasets.
- **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that the training schedule, rather than only the augmentation set, contributes to the gains.
- **Low-resource analysis.** Results across 100, 500, and 1,000 labelled examples support the claim that the method is particularly useful when supervision is scarce.
- **Good presentation.** The method, experimental setup, and conclusions are clearly described.

### Concerns and weaknesses

1. **Limited comparison breadth.** The evaluation uses only four relatively standard English datasets and one encoder architecture. Results on longer documents, domain-shifted data, multilingual data, or larger models would strengthen the claims.
2. **Potential baseline fairness issues.** CurCon hyperparameters are selected by grid search on each validation set, whereas the baselines use hyperparameters reported in their original papers. This may give CurCon an advantage, especially in a low-resource setting. Ideally, all methods should receive comparable tuning budgets.
3. **Insufficient statistical analysis.** Results report mean and standard deviation over five seeds, but there are no significance tests or confidence intervals for the relatively modest 0.5–1.1 point differences over CERT.
4. **Ablation granularity.** The paper does not isolate the contributions of the individual operators, the exact transition thresholds, or the linear schedule itself. Consequently, it is difficult to determine whether the benefit comes from curriculum learning specifically or from another augmentation mixture.
5. **Possible implementation ambiguity.** The schedule describes when operators become available, but the relationship between “augmentation strength,” operator probability, and the generation of two views could be specified more precisely. Details such as whether operators can be composed, how empty or very short views are handled, and the exact back-translation system are also important for reproducibility.
6. **Unlabelled-data assumptions.** The setup uses the remaining training sentences as unlabelled data, but the paper should clarify whether the amount of unlabelled data is held constant across datasets and whether external data or pretrained translation resources introduce additional task-specific information.
7. **Compute and efficiency reporting.** The 12% training-time overhead is useful, but total preprocessing cost for back-translation and the cost of the hyperparameter search should also be reported.

These issues do not invalidate the central result, but they limit the strength and generality of the conclusions.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 80/100 |
| Novelty | 72/100 |
| Significance | 78/100 |
| Clarity | 87/100 |
| **Final average** | **79.25/100** |

### Overall assessment

The paper presents a coherent and empirically effective extension of contrastive intermediate training. The core idea—gradually increasing augmentation difficulty—is relatively incremental, but it is well matched to the low-resource setting and is supported by consistent improvements across datasets and label regimes. The main limitations concern baseline tuning fairness, limited experimental breadth, and insufficient statistical and schedule-specific analysis. These are appropriate targets for revision rather than fundamental flaws.

## Final recommendation: **Accept**

The empirical gains, clear motivation, practical simplicity, and useful ablations make the paper suitable for acceptance, with revisions addressing experimental fairness, reproducibility details, and stronger statistical analysis.