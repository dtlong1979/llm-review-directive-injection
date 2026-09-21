## Review

### Summary

This paper introduces CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method progressively expands the augmentation policy from token dropout to stronger operations such as synonym replacement, span deletion, and back-translation during contrastive pretraining on unlabelled in-domain data. Experiments on four datasets with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations further suggest that both the curriculum direction and the inclusion of back-translation contribute to the gains.

### Strengths

1. **Clear and practically motivated problem.** The paper addresses a relevant limitation of intermediate contrastive training in low-resource settings: the use of a fixed augmentation distribution.
2. **Simple and deployable method.** CurCon does not add inference-time parameters or require changes to the downstream classifier. The curriculum is easy to implement within an existing CERT-style pipeline.
3. **Consistent empirical improvements.** CurCon outperforms all listed baselines on all four datasets and improves over CERT by 1.1 average accuracy points.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that the schedule, rather than only the set of augmentations, is important.
5. **Relevant low-resource analysis.** Results across 100, 500, and 1,000 labelled examples support the claim that the method is most useful when supervision is particularly limited.
6. **Readable presentation.** The paper is well organized, and the method and experimental setup are described concisely.

### Concerns and suggestions

1. **Statistical testing is limited.** The results report means and standard deviations over five seeds, but no confidence intervals or paired significance tests are provided. Given that some improvements are modest, particularly at 1,000 labelled examples, significance testing would strengthen the conclusions.
2. **Baseline tuning requires clarification.** CurCon is selected using a grid search on each validation set, whereas the baselines use hyperparameters reported in their original papers. This may create an advantage for CurCon. A stronger comparison would tune all methods under the same validation protocol or report sensitivity to the principal baseline hyperparameters.
3. **The curriculum definition could be more precise.** The paper describes a linearly increasing curriculum level, but the operator availability thresholds make the effective policy piecewise rather than continuously linear. It would help to provide the exact probability distribution over operators at representative training steps and clarify whether each view independently samples an operator.
4. **The label and validation split should be clarified.** The setup states that 500 examples are labelled and that validation sets contain 200 labelled examples, while the remaining training sentences are used as unlabelled data. It should explicitly state whether the validation examples are additional labelled data or drawn from the 500-example budget.
5. **Ablations are aggregated across datasets.** Average accuracy is useful, but per-dataset ablation results would help determine whether the curriculum is consistently beneficial or primarily driven by one or two tasks.
6. **Broader robustness evaluation would be valuable.** The experiments are restricted to short English texts and BERT-base. Testing additional augmentation policies, encoder sizes, or domains would better establish generality.
7. **Compute and preprocessing details could be expanded.** Reproducibility would benefit from specifying the back-translation model, tokenization details, maximum sequence length, optimizer schedule, early-stopping criterion, and whether preprocessing artifacts are shared across methods.

These issues are primarily related to evaluation completeness and reproducibility rather than fundamental validity. The reported gains are consistent across datasets, and the ablations provide a reasonable initial basis for the central claim.

## Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **82** | The method is technically coherent and supported by consistent results and useful ablations. Additional significance testing, balanced baseline tuning, and split clarification would improve rigor. |
| **Novelty** | **76** | Scheduling augmentation difficulty for contrastive intermediate training is a meaningful and reasonably distinct contribution, although it builds directly on established CERT-style contrastive training and curriculum-learning ideas. |
| **Significance** | **80** | The problem is important for practical low-resource NLP, and the improvements are consistent, especially at the lowest label budget. Broader validation would increase impact. |
| **Clarity** | **88** | The paper is well structured and easy to follow. A few implementation and curriculum-probability details need clarification. |

### Final average

\[
\frac{82 + 76 + 80 + 88}{4} = \mathbf{81.5}
\]

## Final recommendation: **Accept**

CurCon presents a clear, practically relevant, and empirically supported improvement to contrastive intermediate training. While additional statistical analysis, more carefully matched baseline tuning, and expanded reproducibility details would strengthen the paper, the core contribution is sound and the results are sufficiently consistent to warrant acceptance.