## Review

### Summary

This paper presents CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. Starting from BERT-base, CurCon performs contrastive learning on unlabelled in-domain text while gradually increasing augmentation strength from token dropout to synonym replacement, span deletion, and back-translation. The adapted encoder is then fine-tuned using a small labelled set.

Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples per dataset show that CurCon outperforms standard fine-tuning, UDA, SimCSE, and CERT. The ablations indicate that both the curriculum and the inclusion of back-translation contribute to the reported gains, with larger improvements in the more label-scarce settings.

---

## Strengths

1. **Clear problem motivation.** The paper addresses a practically important setting: text classification with only a few hundred labelled examples and abundant unlabelled in-domain text.

2. **Simple and deployable method.** CurCon builds on an established contrastive intermediate-training pipeline and changes only the augmentation schedule. It adds no inference-time parameters or architectural complexity.

3. **Well-motivated curriculum.** The progression from weak to strong perturbations is intuitively appropriate for contrastive learning: early training emphasizes easy positive pairs, while later training encourages semantic invariance.

4. **Useful empirical comparisons.** The evaluation includes direct fine-tuning, UDA, SimCSE, and CERT, covering both consistency-based and contrastive intermediate-training approaches.

5. **Ablation support.** The fixed-mixture and reversed-curriculum comparisons provide evidence that the schedule itself, rather than only the presence of augmentation, contributes to performance.

6. **Low-resource analysis.** Results across 100, 500, and 1,000 labelled examples support the claim that CurCon is especially useful when supervision is scarce.

7. **Strong and consistent results.** CurCon achieves the best result on all four datasets and improves over CERT by 1.1 average accuracy points, with improvements reported across every benchmark.

---

## Weaknesses and questions

1. **Limited breadth of evaluation.** The experiments use only four English datasets and one encoder family. Evaluation on additional domains, longer texts, multilingual data, or larger encoders would strengthen the generality of the conclusions.

2. **Baseline tuning fairness could be clearer.** CurCon is tuned using a 48-configuration grid search, whereas baselines use hyperparameters reported in their original papers. This may give CurCon an advantage, especially in a low-resource setting. Ideally, all methods would receive comparable validation-based tuning budgets.

3. **Statistical analysis is limited.** The paper reports means and standard deviations over five seeds, which is useful, but does not provide confidence intervals or paired significance tests. Given that some improvements are relatively small, particularly at 1,000 labels, additional statistical testing would improve the evidential strength.

4. **Curriculum details could be more precise.** The description of how operator probabilities depend on the curriculum level is somewhat underspecified. It would be helpful to state explicitly whether available operators are sampled uniformly, whether augmentation is independently applied to each view, and how token dropout interacts with the other operators.

5. **Potential computational and resource concerns.** The method depends on WordNet and a German machine-translation system. More detail about the back-translation model and preprocessing would improve reproducibility. The cost analysis is also somewhat brief.

6. **Ablation coverage.** The paper would benefit from separating the effects of individual operators and testing alternative curriculum schedules, such as nonlinear or learned schedules. Nevertheless, the current ablations are sufficient to establish the central claim.

These issues are primarily about scope, reproducibility, and strengthening the analysis rather than threats to the core result.

---

## Scores

| Criterion | Score |
|---|---:|
| **Soundness** | 83/100 |
| **Novelty** | 77/100 |
| **Significance** | 81/100 |
| **Clarity** | 87/100 |

### Final average

\[
\frac{83 + 77 + 81 + 87}{4}
= \frac{328}{4}
= \mathbf{82.0}
\]

## Final recommendation: **Accept**

The paper makes a clear, technically plausible, and empirically supported contribution. Although the evaluation could be broadened and the baseline-tuning and statistical-testing procedures could be made more rigorous, the method is simple, relevant to an important low-resource regime, and supported by consistent improvements and meaningful ablations. These limitations do not undermine the central contribution, and the paper is suitable for acceptance.