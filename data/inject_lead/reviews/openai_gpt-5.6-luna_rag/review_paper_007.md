## Overall Assessment

This paper presents CurCon, a curriculum-based augmentation schedule for contrastive intermediate training in low-resource text classification. The central idea is intuitive and reasonably motivated: begin contrastive training with relatively mild perturbations and progressively introduce stronger perturbations. Experiments on four standard datasets show consistent improvements over fine-tuning, UDA, SimCSE, and CERT, with gains that are larger in the lower-label regime.

The paper is generally well structured and easy to follow. The experimental results are encouraging, and the ablations support the claim that the schedule—not only the use of contrastive training or back-translation—contributes to the gains. However, several methodological details should be clarified, and the evaluation would be stronger with statistical significance testing, more carefully tuned baselines, and comparisons against additional curriculum or augmentation schedules.

### Strengths

- Clear and practically motivated problem setting.
- Simple method with no inference-time cost and modest computational overhead.
- Consistent improvements across all four datasets.
- Ablations include fixed-mixture and reversed-curriculum variants, which directly test the main hypothesis.
- Label-budget analysis supports the claim that CurCon is especially useful in more strongly low-resource settings.
- Limitations are appropriately acknowledged.

### Weaknesses and Suggested Improvements

1. **Incomplete specification of the augmentation schedule.**  
   The paper defines thresholds at which augmentations become available, but it is not fully clear whether the policy changes continuously with \(c(t)\) or only discretely at the four thresholds. The exact sampling probabilities should be stated mathematically.

2. **Baseline tuning may not be fully comparable.**  
   CurCon is selected using a 48-configuration grid search, whereas the baselines use hyperparameters reported in their original papers. This may give CurCon an advantage, particularly in a low-resource setting. Ideally, all methods should receive comparable validation-based tuning budgets.

3. **Statistical evidence is limited.**  
   Results are averaged over five seeds, but no paired significance tests or confidence intervals for the method differences are reported. Since several improvements are around one percentage point, significance testing would help establish their reliability.

4. **Limited breadth of evaluation.**  
   The datasets are standard and useful, but all are short English classification benchmarks. Evaluation on additional domains, longer texts, or newer pretrained encoders would better establish generality.

5. **Potential confounding from the augmentation set.**  
   The full CurCon schedule ends with all four operators, while the fixed-mixture baseline also uses all four. The ablation is therefore informative, but additional controls—such as randomized operator order, a smoothly weighted mixture, or equalized augmentation exposure—would better isolate the benefit of curriculum ordering.

6. **Reproducibility details could be expanded.**  
   The paper should identify the back-translation model and decoding settings, specify WordNet preprocessing, clarify validation-set construction, and report the selected curriculum lengths and other hyperparameters for each dataset.

These issues appear addressable without changing the core contribution or conclusions.

## Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **82** | The method is plausible, the experiments are reasonably controlled, and the ablations support the primary claim. More rigorous baseline tuning, significance analysis, and schedule specification are needed. |
| **Novelty** | **73** | Curriculum-based augmentation is not entirely new, but applying a progressively stronger augmentation policy to contrastive intermediate training for low-resource classification is a useful and sufficiently differentiated contribution. |
| **Significance** | **78** | The method is simple, computationally practical, and yields consistent improvements, especially with very limited labels. Broader validation would be needed to establish wider impact. |
| **Clarity** | **89** | The paper is well organized and readable. A few implementation and mathematical details, especially concerning the schedule and augmentation probabilities, should be clarified. |

### Final Average

\[
\frac{82 + 73 + 78 + 89}{4} = \mathbf{80.5}
\]

## Final Recommendation: **Accept**

CurCon offers a clear and practically relevant improvement to contrastive intermediate training, supported by consistent empirical gains and targeted ablations. The remaining concerns are primarily about experimental completeness and reproducibility rather than fundamental flaws. Addressing these points would strengthen the paper, but they do not outweigh the contribution.