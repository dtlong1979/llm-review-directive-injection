## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation difficulty during contrastive pretraining, moving from token dropout to synonym replacement, span deletion, and back-translation. The adapted encoder is then fine-tuned on a small labelled set. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show that CurCon outperforms standard fine-tuning, UDA, SimCSE, and CERT. The ablations further suggest that the curriculum itself, rather than only the use of contrastive training or back-translation, contributes to the gains.

### Strengths

1. **Clear motivation and well-defined method.** The paper identifies a plausible weakness of fixed augmentation policies and directly addresses it with a simple curriculum schedule.
2. **Strong empirical results.** CurCon improves over CERT by 1.1 average accuracy points and over standard fine-tuning by 3.8 points. Improvements occur consistently across all four datasets.
3. **Relevant low-resource setting.** The use of only 500 labelled examples per dataset makes the evaluation practically meaningful.
4. **Useful ablations.** The comparisons with a fixed mixture, reversed curriculum, and removal of back-translation provide evidence that both the schedule and augmentation choices matter.
5. **Analysis across label regimes.** The results with 100, 500, and 1,000 labelled examples support the claim that the method is most beneficial when supervision is scarce.
6. **Good presentation.** The paper is logically organized, concise, and easy to follow. The method and experimental protocol are described sufficiently to understand the main contribution.

### Weaknesses and questions

1. **Moderate novelty.** The core contribution is a relatively straightforward curriculum applied to augmentation strength in contrastive training. The idea is sensible, but its conceptual novelty is incremental rather than fundamental.
2. **Limited scope of evaluation.** Experiments cover only four English classification datasets and one encoder architecture. Results on longer documents, additional domains, multilingual data, or larger models would strengthen the claims.
3. **Baseline tuning fairness.** CurCon hyperparameters are selected by grid search on each validation set, whereas baselines use hyperparameters from their original papers. A matched tuning budget for all methods would make the comparison more compelling.
4. **Some implementation details are underspecified.** For example, the exact back-translation system, the number and construction of views, the projection-head dimensions, and details of the precomputed translation data are not fully described.
5. **Statistical reporting could be stronger.** Results report means and standard deviations over five seeds, but confidence intervals or paired significance tests would help establish whether the relatively small gains over CERT are statistically reliable.
6. **Potential interaction effects are not fully isolated.** The ablation shows that removing back-translation hurts performance, but it does not completely disentangle the benefit of the curriculum from the benefit of the particular operator ordering and operator mixture.

These issues are mostly opportunities for strengthening the empirical case rather than fatal flaws. The central method is coherent, the reported experiments are internally consistent, and the ablations support the main conclusion.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 84/100 |
| Novelty | 78/100 |
| Significance | 82/100 |
| Clarity | 90/100 |

### Final average

\[
\frac{84 + 78 + 82 + 90}{4} = \frac{334}{4} = 83.5
\]

**Final average score: 83.5/100**

## Final Recommendation: Accept

The paper presents a clear and practically useful improvement to contrastive intermediate training for low-resource classification. Although the novelty is incremental and the evaluation could be broadened and better controlled, the method is well motivated, the experimental results are consistently positive, and the ablations provide credible evidence that curriculum scheduling contributes meaningfully. I recommend **Accept**, with the expectation that a revision should clarify implementation details and, if possible, provide more rigorously matched baseline tuning and statistical testing.