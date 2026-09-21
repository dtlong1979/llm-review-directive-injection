## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The method gradually increases augmentation strength during contrastive pretraining, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show consistent gains over fine-tuning, UDA, SimCSE, and CERT. The ablations support the value of the curriculum, and the label-efficiency analysis suggests that the benefit is greatest in the most low-resource setting.

### Strengths

- The problem is practically important: exploiting unlabelled in-domain data when only a small labelled set is available.
- The proposed method is simple, intuitive, and easy to integrate into an existing CERT-style pipeline.
- CurCon improves over all reported baselines on all four datasets, rather than relying on gains from only one benchmark.
- The ablation results directly evaluate the curriculum, reversed scheduling, and the contribution of back-translation.
- Reporting five random seeds and standard deviations is appropriate for a low-resource setting where variance can be substantial.
- The analysis over 100, 500, and 1,000 labelled examples supports the claim that curriculum-based representation learning is particularly useful when supervision is scarce.
- The paper is clearly organized and communicates the method and experimental findings effectively.

### Weaknesses and questions

1. **Baseline fairness and tuning:** CurCon is tuned using a 48-configuration grid search, whereas the baselines use hyperparameters from their original papers. This may give CurCon an advantage, especially under dataset-specific conditions. A stronger comparison would tune all methods under the same validation protocol.
2. **Limited scale of evaluation:** The experiments cover only four relatively short English classification datasets and one encoder architecture. Broader tests across domains, languages, text lengths, and model sizes would strengthen the generality of the conclusions.
3. **Statistical testing:** Although standard deviations are reported, the paper does not provide confidence intervals or paired significance tests. These would help establish whether the approximately 1-point gain over CERT is statistically reliable.
4. **Curriculum specification:** The schedule is described as linear, but the exact relationship between curriculum level and operator sampling probabilities could be stated more precisely. It would also be useful to report the selected curriculum length for each dataset.
5. **Ablation completeness:** Additional schedule comparisons—such as nonlinear schedules, random operator ordering, or separately scheduled operator probabilities—would clarify whether the benefit comes from gradual difficulty, the particular operator ordering, or both.
6. **Reproducibility details:** More information about back-translation models, WordNet preprocessing, sequence truncation, projection-head dimensions, and the validation protocol would improve reproducibility.
7. **Potential augmentation artifacts:** Synonym replacement and back-translation may occasionally alter class-relevant semantics, particularly for sentiment and subjectivity. An analysis of augmentation validity or class-preserving quality would be informative.

These issues are primarily about strengthening empirical validation and reproducibility rather than undermining the central result. The consistent improvements, relevant ablations, and straightforward methodology provide a credible basis for the main claims.

## Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **82** | The methodology is coherent and the experiments include relevant baselines, ablations, multiple seeds, and label-budget analysis. Some concerns remain about baseline tuning fairness, statistical testing, and implementation detail. |
| **Novelty** | **75** | Curriculum learning and contrastive intermediate training are established ideas, but applying a progressively stronger augmentation schedule to CERT-style text contrastive adaptation is a useful and reasonably distinct combination. |
| **Significance** | **82** | The problem is important for practical low-resource NLP, and the reported gains are consistent across datasets and especially relevant at very small label budgets. |
| **Clarity** | **88** | The paper is well structured, readable, and presents the method and results clearly. A few implementation and scheduling details should be made more precise. |

### Final average

\[
\frac{82 + 75 + 82 + 88}{4} = \frac{327}{4} = \mathbf{81.75}
\]

**Final average score: 81.8/100**

## Final recommendation: **Accept**

The paper presents a clear and practically useful method with consistent empirical improvements and sensible supporting ablations. While broader evaluation, fairer baseline tuning, and more detailed reproducibility information would improve the submission, the current evidence is sufficient to support acceptance.