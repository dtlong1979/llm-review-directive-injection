## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The method gradually increases the strength of text augmentations during contrastive pretraining, moving from token dropout to synonym replacement, span deletion, and back-translation. The approach is evaluated on SST-2, AG News, TREC, and SUBJ using 500 labelled examples per dataset, with comparisons against standard fine-tuning, UDA, SimCSE, and CERT.

CurCon achieves the best performance on all four datasets, improving average accuracy from 87.8% for CERT to 88.9%. The ablations further suggest that both the curriculum ordering and the inclusion of back-translation contribute to the gains.

### Strengths

1. **Clear and practically relevant problem.** Low-resource classification is important, and exploiting unlabelled in-domain data is a well-motivated approach.
2. **Simple, modular method.** CurCon can be incorporated into an existing contrastive intermediate training pipeline without inference-time changes or architectural modifications.
3. **Strong empirical results.** The proposed method improves over all reported baselines on each of the four datasets, with an average gain of 1.1 points over CERT and 3.8 points over direct fine-tuning.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum variants provide evidence that the training schedule, rather than augmentation alone, is responsible for part of the improvement.
5. **Low-resource analysis.** The results across 100, 500, and 1,000 labelled examples support the claim that the method is most useful when supervision is limited.
6. **Good presentation.** The paper is well organized, concise, and explains the training pipeline and curriculum schedule clearly.

### Weaknesses and questions

1. **Baseline tuning and fairness.** The paper states that CurCon hyperparameters are selected by grid search, whereas baselines use hyperparameters from their original papers. For a fully fair comparison, the baselines should ideally receive comparable tuning effort, especially in the low-resource setting.
2. **Limited experimental breadth.** The evaluation uses four relatively short English classification datasets and only BERT-base. Results on additional domains, longer documents, multilingual data, or different encoders would strengthen the generality of the conclusions.
3. **Statistical analysis.** Results are averaged over five seeds, but the paper does not report significance tests or confidence intervals for the aggregate improvements. Given that some gains are modest, this would be useful.
4. **Curriculum mechanism could be analyzed more deeply.** The paper uses hand-designed thresholds and a linear schedule. More detailed sensitivity analyses over curriculum length and threshold choices would clarify how robust the method is.
5. **Some implementation details are underspecified.** For example, the exact treatment of multiple operators, the back-translation system, and the construction of the unlabelled pools could be described in more detail to improve reproducibility.

These issues are mostly empirical completeness and reproducibility concerns rather than fundamental flaws. The central comparison is coherent, and the reported ablations are directionally consistent with the main claim.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 86/100 |
| Novelty | 78/100 |
| Significance | 82/100 |
| Clarity | 90/100 |

### Final average

\[
\frac{86 + 78 + 82 + 90}{4} = \frac{336}{4} = 84.0
\]

**Final average score: 84.0/100**

## Recommendation: Accept

The paper presents a clear and effective improvement to contrastive intermediate training for low-resource text classification. Although the novelty is incremental and the evaluation could be broadened, the method is well motivated, easy to implement, and supported by consistent gains across datasets and ablations. The limitations are appropriate for discussion in the paper and do not outweigh the empirical contribution.