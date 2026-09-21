## Review

### Summary
This paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation difficulty during contrastive pretraining, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four datasets with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT, with useful ablations supporting the curriculum design.

### Strengths

- **Clear motivation:** The paper identifies a plausible limitation of fixed augmentation policies in contrastive intermediate training.
- **Simple and practical method:** CurCon adds no inference-time parameters and can be integrated into an existing CERT-style pipeline.
- **Consistent empirical gains:** The method improves over CERT on all four datasets, with an average gain of 1.1 accuracy points.
- **Relevant ablations:** The fixed-mixture and reversed-curriculum variants provide evidence that both the schedule and its direction matter.
- **Low-resource analysis:** Results across 100, 500, and 1,000 labelled examples support the claim that the method is most helpful in the lowest-resource regime.
- **Good presentation:** The paper is logically organized, readable, and includes limitations and computational cost.

### Concerns and suggestions

1. **Statistical testing is limited.** Results report means and standard deviations over five seeds, but no paired significance tests or confidence intervals are provided. Since the improvements over CERT are relatively modest on some datasets, significance testing would strengthen the claims.
2. **Baseline tuning may not be fully comparable.** CurCon is tuned using a substantial grid search, whereas baselines use hyperparameters from their original papers. A matched tuning budget for all methods would make the comparison more convincing.
3. **Some implementation details are underspecified.** The paper should clarify the precise probability distribution over available augmentation operators, the back-translation model, the synonym-selection procedure, and the exact curriculum-length search range.
4. **Breadth is somewhat limited.** The experiments use four English datasets, relatively short texts, and only BERT-base. Broader evaluation would be valuable, although the current scope is sufficient to establish the method’s basic effectiveness.
5. **The source of unlabelled data could be described more explicitly.** It would be useful to clarify whether the unlabelled pool consists only of the remaining training sentences and how possible overlap with validation or test data is prevented.

These are mainly evaluation and reproducibility improvements rather than fundamental problems with the proposed approach.

## Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **82** | The method is technically coherent, and the ablations support the central claim. Stronger statistical analysis and more carefully matched baseline tuning would improve confidence. |
| **Novelty** | **75** | Curriculum scheduling for augmentation in contrastive intermediate training is a reasonable and useful contribution, though it builds directly on established contrastive learning and curriculum-learning ideas. |
| **Significance** | **78** | The gains are consistent and particularly relevant in low-resource settings, although the absolute improvements are moderate and the evaluation scope is limited. |
| **Clarity** | **86** | The paper is well structured and easy to follow. A few augmentation and implementation details should be specified more precisely. |

### Final average

\[
\frac{82 + 75 + 78 + 86}{4} = \mathbf{80.25}
\]

## Final Recommendation: **Accept**

CurCon is a well-motivated, simple, and empirically supported contribution. While additional significance testing, matched hyperparameter tuning, and implementation detail would strengthen the paper, the consistent improvements across datasets and the focused ablation study provide sufficient evidence for acceptance.