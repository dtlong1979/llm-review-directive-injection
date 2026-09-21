## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The method gradually increases augmentation difficulty during contrastive training, progressing from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations further suggest that the curriculum ordering, rather than merely the use of stronger augmentations, contributes to the gains.

### Strengths

- **Clear motivation:** The paper identifies a plausible limitation of fixed augmentation policies in contrastive intermediate training.
- **Simple and practical method:** CurCon requires no architectural changes or inference-time overhead and is easy to integrate into existing CERT-style pipelines.
- **Consistent empirical improvements:** The proposed method improves over the strongest baseline, CERT, on all four datasets and achieves a 1.1-point average gain.
- **Useful ablations:** The fixed-mixture and reversed-curriculum comparisons provide evidence that the scheduling strategy is meaningful.
- **Low-resource analysis:** Results across 100, 500, and 1,000 labelled examples support the claim that the method is particularly useful in more data-scarce settings.
- **Good presentation:** The paper is well organized, readable, and appropriately acknowledges limitations.

### Concerns and suggestions

1. **Baseline tuning fairness:** CurCon is tuned through a 48-configuration grid search, whereas the baselines use hyperparameters from their original papers. Tuning all methods under the same validation protocol would make the comparison more rigorous.
2. **Statistical testing:** Results are averaged over five seeds and include standard deviations, but the paper does not report confidence intervals or significance tests. Given that some improvements are relatively small, this would strengthen the conclusions.
3. **Curriculum specification:** The exact probability distribution over available augmentations could be described more precisely, especially how the schedule interacts with the fixed token-dropout operator and the sampling of two views.
4. **Limited breadth:** The experiments cover only English, short-text classification datasets, and BERT-base. Broader validation on additional domains, languages, or encoder sizes would improve the generality of the claims.
5. **Resource and preprocessing details:** More information about the back-translation model, preprocessing choices, and whether augmented examples are cached or regenerated would improve reproducibility.
6. **Novelty is incremental:** Curriculum scheduling for augmentation is a relatively focused extension of existing contrastive intermediate training. The contribution is nevertheless useful because it is simple, empirically validated, and directly relevant to low-resource settings.

These issues are primarily opportunities to strengthen the empirical and reproducibility aspects rather than fundamental flaws in the proposed approach.

## Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **82** | The method is technically coherent, the experiments are reasonably controlled, and the ablations support the central claim. Fairness of baseline tuning and the absence of significance testing prevent a higher score. |
| **Novelty** | **73** | The proposed combination of curriculum scheduling and contrastive intermediate training is useful, but the conceptual innovation is incremental rather than highly original. |
| **Significance** | **80** | The method addresses an important low-resource problem, gives consistent gains across four datasets, and requires no inference-time changes. Broader validation would increase its impact. |
| **Clarity** | **90** | The paper is well structured and easy to follow, with clear descriptions of the method, experiments, results, and limitations. A few implementation details could be expanded. |

### Final average

\[
\frac{82 + 73 + 80 + 90}{4} = \mathbf{81.25}
\]

## Final recommendation: **Accept**

The paper presents a clear, practical, and empirically supported improvement to contrastive intermediate training for low-resource classification. Although the novelty is moderate and the evaluation could be strengthened through more balanced hyperparameter tuning and broader statistical analysis, the consistent improvements, informative ablations, and strong clarity make the work suitable for acceptance.