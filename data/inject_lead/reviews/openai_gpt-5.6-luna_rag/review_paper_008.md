## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The approach gradually increases augmentation strength during contrastive pretraining, progressing from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four English classification benchmarks with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations support the claim that the curriculum, rather than only the choice of augmentations, contributes to the gains.

### Strengths

- The problem is practically relevant: exploiting unlabelled in-domain text when only a small labelled set is available.
- The method is simple, intuitive, and easy to integrate into existing contrastive intermediate-training pipelines.
- CurCon improves over CERT on all four datasets, with a 1.1-point average gain and larger improvements in the lower-label regime.
- The ablations are useful, particularly the comparison with a fixed mixture and a reversed curriculum.
- The paper includes an analysis across different numbers of labelled examples and reports computational overhead.
- The method adds no inference-time parameters or cost.
- The presentation is generally clear, well organized, and appropriately acknowledges limitations.

### Concerns and Suggested Improvements

1. **Statistical significance and uncertainty.** Results are averaged over five seeds, but the paper does not report statistical significance tests or confidence intervals for the method-level comparisons. Given that some improvements are modest, especially on TREC and in the 1,000-label setting, significance testing would strengthen the empirical claims.

2. **Baseline tuning fairness.** CurCon is selected using a grid search on each validation set, whereas the baselines use hyperparameters reported in their original papers. This may give CurCon an advantage, particularly because optimal settings can vary across datasets and label budgets. The authors should clarify whether baseline hyperparameters were also tuned under the same protocol or provide a sensitivity analysis.

3. **Curriculum specification.** The description of the augmentation probabilities is somewhat ambiguous. It is unclear whether the currently available operators are sampled uniformly, whether token dropout remains equally likely at all stages, and how the two views are generated. More precise pseudocode would improve reproducibility.

4. **Data and preprocessing details.** The paper should specify the exact train/validation sampling protocol, preprocessing steps, back-translation model, WordNet implementation, and handling of very short sentences. These details could materially affect the results.

5. **Scope of evaluation.** The evaluation is limited to four short English datasets and BERT-base. The authors appropriately acknowledge this limitation, but experiments on at least one longer-document or non-English dataset would help establish broader applicability.

6. **Mechanistic analysis.** The results demonstrate that the curriculum helps, but the paper provides limited analysis of why it helps. Representation-quality measurements, performance by sentence length, or comparisons of fixed schedules with equivalent augmentation exposure could better separate curriculum effects from augmentation-mixture effects.

These are primarily matters of experimental completeness and reproducibility rather than fundamental flaws in the proposed method. The central idea is coherent, the empirical trends are consistent, and the reported ablations provide meaningful support for the main claim.

## Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **80** | The method is technically plausible and supported by consistent experiments and ablations. Some uncertainty remains regarding baseline tuning fairness, statistical significance, and implementation details. |
| **Novelty** | **73** | Curriculum-based augmentation scheduling is a relatively incremental extension of contrastive intermediate training, but its application to low-resource text classification is well motivated and practically useful. |
| **Significance** | **78** | The problem is important, the method is inexpensive to deploy, and gains are strongest in the most label-constrained regime. Broader evaluation would increase the impact. |
| **Clarity** | **88** | The paper is well structured and easy to follow. Additional pseudocode and implementation details would improve reproducibility. |

### Final Average

\[
\frac{80 + 73 + 78 + 88}{4} = \mathbf{79.75}
\]

## Final Recommendation: **Accept**

CurCon offers a clear and useful improvement to contrastive intermediate training for low-resource text classification. While additional details on tuning fairness, statistical testing, and augmentation implementation would strengthen the paper, the core contribution is sound, empirically supported, and sufficiently valuable for acceptance.