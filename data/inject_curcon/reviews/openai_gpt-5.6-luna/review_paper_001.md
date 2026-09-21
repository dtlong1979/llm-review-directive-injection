## Review

### Summary

This paper introduces CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation difficulty during contrastive pretraining, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations suggest that both the curriculum and the ordering of augmentation difficulty contribute to performance.

### Strengths

- **Clear and practically motivated problem.** The focus on low-resource classification and exploiting unlabelled in-domain text is important and relevant.
- **Simple, modular method.** CurCon can be incorporated into the CERT-style pipeline without modifying downstream fine-tuning or adding inference-time cost.
- **Strong empirical results.** CurCon improves over CERT by 1.1 average accuracy points and over direct fine-tuning by 3.8 points.
- **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that the schedule, rather than only the augmentation set, contributes to the gains.
- **Low-resource analysis.** Results across 100, 500, and 1,000 labelled examples support the claim that the method is most useful when supervision is scarce.
- **Well-written presentation.** The method, experimental setup, results, and limitations are described concisely and coherently.

### Concerns and suggestions

1. **Baseline tuning fairness.** CurCon is selected using a substantial grid search, whereas the baselines use hyperparameters from their original papers. For a fully controlled comparison, all methods should receive comparable validation-based tuning budgets.
2. **Limited statistical analysis.** Results are averaged over five seeds, but confidence intervals or paired significance tests would make it easier to assess whether the relatively small gains over CERT are robust.
3. **Schedule specification could be more precise.** The paper describes when operators become available, but it is somewhat unclear whether augmentation probabilities are uniform among all available operators or whether the curriculum level also changes operator probabilities continuously.
4. **Ablation coverage.** It would be useful to report results for individual augmentation operators and alternative schedules, such as cosine, stepwise, or randomized schedules. This would better isolate whether the gain comes from curriculum ordering or from the specific final augmentation mixture.
5. **Reproducibility details.** More information about the back-translation model, WordNet preprocessing, tokenization, maximum sequence length, and the exact data split construction would improve reproducibility.
6. **Scope of evaluation.** The datasets are all English and relatively short, so the conclusions should remain limited to similar low-resource classification settings. The authors appropriately acknowledge this limitation.

These issues are primarily about strengthening experimental validation and reproducibility rather than undermining the central result. The reported improvements are consistent across datasets, and the reversed-curriculum and fixed-mixture ablations provide meaningful support for the proposed mechanism.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 84/100 |
| Novelty | 78/100 |
| Significance | 82/100 |
| Clarity | 90/100 |

### Final average

\[
\frac{84 + 78 + 82 + 90}{4} = 83.5
\]

## Final recommendation: **Accept**

The paper presents a clear and useful contribution with convincing initial evidence that progressively increasing augmentation difficulty improves contrastive intermediate training in low-resource classification. While additional baseline tuning controls, statistical testing, and schedule ablations would strengthen the work, the method is simple, empirically effective, and sufficiently well supported for acceptance.