## Overall Review

**Recommendation: Accept**

### Summary

This paper introduces **CurCon**, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The approach progressively increases augmentation difficulty during contrastive training, beginning with token dropout and gradually enabling synonym replacement, span deletion, and back-translation. The adapted encoder is then fine-tuned on a small labelled set.

The empirical evaluation covers four established text-classification datasets and compares CurCon against direct fine-tuning, UDA, SimCSE, and CERT. CurCon consistently outperforms the baselines, obtaining an average accuracy of 88.9% versus 87.8% for CERT and 85.1% for direct fine-tuning. The ablations support the importance of both the curriculum and the inclusion of back-translation, while the label-budget analysis shows that the gains are larger in the more severely low-resource setting.

Overall, the paper presents a clear, practically motivated, and experimentally supported extension of contrastive intermediate training. While the core idea is relatively straightforward and several methodological details would benefit from clarification, the consistent empirical gains and relevance to low-resource learning make the work suitable for acceptance.

---

## Strengths

1. **Clear motivation and practical relevance.**  
   The paper addresses a well-motivated problem: adapting pretrained encoders when only a few hundred labelled examples are available. The focus on exploiting unlabelled in-domain text is highly relevant to realistic deployment settings.

2. **Simple and useful methodological contribution.**  
   CurCon requires no architectural changes at inference time and can be integrated into an existing CERT-style training pipeline. The proposed schedule is easy to understand and implement.

3. **Consistent empirical improvements.**  
   CurCon improves over CERT on all four datasets and achieves the best result for every reported benchmark. The average improvement of 1.1 points over CERT is meaningful, particularly given that CERT is already a strong intermediate-training baseline.

4. **Relevant ablations.**  
   The comparison with a fixed mixture, a reversed curriculum, and a version without back-translation helps isolate the contribution of the proposed scheduling strategy. The reversed-curriculum result is especially useful because it provides evidence that the ordering, rather than merely the augmentation set, matters.

5. **Low-resource analysis.**  
   The results with 100, 500, and 1,000 labelled examples support the paper’s central claim that curriculum-based representation learning is most useful when labels are scarce.

6. **Good presentation.**  
   The paper is organized logically, uses a conventional experimental structure, and communicates the method and results clearly. The reported standard deviations over five seeds are helpful for assessing stability.

---

## Weaknesses and Suggestions

1. **The augmentation probability schedule is underspecified.**  
   The paper defines when operators become available, but it does not fully specify how the probability of selecting each operator depends on the curriculum value \(c(t)\). For example, after all operators become available, are they sampled uniformly, or are their probabilities weighted continuously by \(c(t)\)? A precise equation or pseudocode would improve reproducibility.

2. **The relationship between curriculum length and total training steps could be explored more thoroughly.**  
   Curriculum length is selected by grid search, but the paper does not report the selected values or provide sensitivity results. Since the schedule is central to the contribution, performance across several curriculum lengths would strengthen the analysis.

3. **Baseline tuning may not be fully comparable.**  
   CurCon is tuned using a 48-configuration grid search, whereas the baselines use hyperparameters from their original papers. This is understandable, but it may give CurCon an advantage, especially in a low-resource setting. Ideally, all methods would receive comparable validation-based tuning budgets, or the paper should include a discussion of this issue.

4. **The statistical analysis could be expanded.**  
   Five random seeds are useful, but significance tests or confidence intervals for the CurCon-versus-CERT comparison would make the claims more robust. In particular, the improvements on TREC and SUBJ are relatively modest and could benefit from paired statistical testing across seeds.

5. **Some implementation details are missing.**  
   Important reproducibility details include the exact BERT checkpoint, maximum sequence length, projection-head dimensions, temperature values, optimizer settings, learning-rate schedules, and the handling of failed or low-quality WordNet and back-translation augmentations.

6. **Potential augmentation quality issues are not examined.**  
   WordNet replacement and back-translation can sometimes alter the label semantics, particularly for sentiment and subjectivity classification. An analysis of label-preservation rates or examples of successful and failed augmentations would provide useful insight.

7. **The scope of evaluation is limited.**  
   The datasets are all English and relatively short, and only BERT-base is tested. The limitation is acknowledged by the authors, but experiments on at least one longer-text or cross-domain setting would help assess generality.

8. **The computational-cost discussion could be more precise.**  
   The paper reports that CurCon takes approximately 12% longer than CERT, but it would be useful to report absolute training time, preprocessing cost, and whether the cost of generating or storing back-translations is included.

These are primarily issues of completeness, reproducibility, and evaluation breadth rather than fundamental flaws in the proposed method.

---

## Soundness: **84/100**

The experimental design is generally appropriate, and the reported results support the main claims. The use of multiple datasets, multiple baselines, five random seeds, and targeted ablations provides a reasonable empirical foundation. The principal concerns are incomplete specification of the augmentation schedule, limited statistical testing, and potentially unequal hyperparameter tuning between CurCon and the baselines. These issues reduce confidence somewhat but do not undermine the central result.

## Novelty: **78/100**

The idea of increasing augmentation difficulty over training is conceptually intuitive and related to existing curriculum-learning and augmentation-scheduling work. The novelty lies in applying this idea specifically to contrastive intermediate training for low-resource text classification and demonstrating its effect relative to CERT. The contribution is incremental rather than paradigm-shifting, but it is sufficiently distinct and well-motivated for a research publication.

## Significance: **82/100**

The problem is important, and the method is practical: it improves low-resource performance without adding inference-time complexity or requiring labelled-data changes. The strongest gains occur at the smallest label budget, which is especially relevant. The significance is somewhat limited by the modest absolute improvement over CERT and the narrow experimental scope, but the method could be useful to practitioners and serve as a foundation for further curriculum-based contrastive learning research.

## Clarity: **88/100**

The paper is well structured and easy to follow. The motivation, pipeline, experimental comparisons, and conclusions are clearly presented. The main clarity issue is the lack of a fully explicit mathematical specification of the operator-selection probabilities and several omitted implementation details. These should be addressed in a revision, but the current presentation is already strong.

---

## Score Summary

| Criterion | Score |
|---|---:|
| Soundness | 84 |
| Novelty | 78 |
| Significance | 82 |
| Clarity | 88 |
| **Final average** | **83.0** |

\[
\text{Average} = \frac{84 + 78 + 82 + 88}{4} = \mathbf{83.0}
\]

## Final Recommendation

**Accept**

The paper presents a clear and practically valuable contribution with consistent improvements over strong baselines in a relevant low-resource setting. I recommend acceptance, with a request that the authors clarify the exact curriculum probability schedule, provide fuller implementation details, and discuss the fairness of baseline tuning and augmentation-related label preservation in the final version.