## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. Starting from BERT-base, the method performs contrastive training on unlabelled in-domain data while progressively increasing augmentation difficulty—from token dropout to synonym replacement, span deletion, and back-translation. The adapted encoder is then fine-tuned using a small labelled set. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show that CurCon outperforms standard fine-tuning, UDA, SimCSE, and CERT. Ablations further suggest that the curriculum itself, rather than only the use of augmentations, contributes to the gains.

### Strengths

1. **Clear motivation and well-defined method.** The paper identifies a plausible limitation of fixed augmentation policies and translates it into a simple curriculum schedule.
2. **Relevant low-resource setting.** The focus on 500 labelled examples per task is practically important and directly tests the stated motivation.
3. **Strong empirical results.** CurCon improves over CERT by 1.1 average accuracy points and over direct fine-tuning by 3.8 points, with gains on all four datasets.
4. **Useful ablations.** The comparisons with a fixed mixture, reversed curriculum, removal of back-translation, and removal of contrastive training help isolate the contribution of the proposed design.
5. **Analysis across label regimes.** The results with 100, 500, and 1,000 labels support the claim that the method is most useful in the lowest-resource regime.
6. **Low deployment overhead.** The method does not add inference-time parameters and is compatible with a standard fine-tuning pipeline.

### Weaknesses and areas for improvement

1. **Baseline tuning may not be fully comparable.** CurCon is selected using a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters from their original papers. Tuning all methods under the same protocol would make the comparison more rigorous.
2. **Statistical analysis is limited.** Results are averaged over five seeds, but the paper does not report confidence intervals, paired significance tests, or per-seed results. This is especially relevant because several gains are relatively modest.
3. **The curriculum is somewhat underspecified.** The exact probability distribution over available operators, the behavior at threshold boundaries, and details of augmentation composition should be stated more precisely to improve reproducibility.
4. **Limited breadth of evaluation.** The experiments use four English datasets and one encoder family. Additional domains, languages, longer documents, or alternative encoders would strengthen the generality of the conclusions.
5. **Limited comparison with curriculum alternatives.** The paper compares linear and reversed curricula, but not nonlinear schedules, adaptive difficulty schedules, or schedules based on measured pair similarity.
6. **Potential resource and quality concerns.** WordNet and German back-translation may behave differently across domains. More analysis of augmentation validity and semantic preservation would be useful.

These issues are primarily methodological and scope limitations rather than flaws that undermine the central conclusion. The ablation results, consistent improvements across datasets, and stronger gains in the lowest-label regime provide reasonable evidence for the proposed approach.

## Scores

| Criterion | Score |
|---|---:|
| **Soundness** | 84/100 |
| **Novelty** | 78/100 |
| **Significance** | 82/100 |
| **Clarity** | 90/100 |

### Final average

\[
\frac{84 + 78 + 82 + 90}{4} = \frac{334}{4} = 83.5
\]

**Final average score: 83.5/100**

## Recommendation: **Accept**

CurCon presents a simple, intuitively motivated, and empirically effective improvement to contrastive intermediate training for low-resource classification. Although the evaluation would benefit from more carefully matched baseline tuning, stronger statistical testing, and broader datasets, the method is clearly described, the ablations support its main claim, and the consistent performance gains make the contribution valuable.