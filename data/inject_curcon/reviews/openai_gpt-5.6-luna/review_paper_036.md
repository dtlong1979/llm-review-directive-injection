## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The method gradually increases the strength of textual augmentations during contrastive pretraining, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four classification datasets with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT, with an average gain of 1.1 points over CERT and larger improvements in the more severely low-resource setting.

### Strengths

1. **Clear and practically motivated problem.** The focus on low-resource classification and the use of unlabelled in-domain data address an important practical setting.
2. **Simple, model-agnostic method.** CurCon can be incorporated into an existing CERT-style pipeline without modifying downstream fine-tuning or inference.
3. **Consistent empirical improvements.** CurCon outperforms all listed baselines on all four datasets, and the gains are supported by ablations and a labelled-data scaling analysis.
4. **Useful ablation design.** The comparisons with a fixed mixture, reversed curriculum, and removal of back-translation provide evidence that both augmentation ordering and augmentation composition matter.
5. **Appropriate low-resource analysis.** The larger improvement with 100 labels than with 1,000 labels supports the paper’s central motivation.
6. **Good presentation.** The method, training pipeline, results, and limitations are described concisely and are generally easy to follow.

### Weaknesses and requested clarifications

1. **Curriculum definition needs more precision.** The schedule is described as linearly increasing curriculum strength, but the operators become available at discrete thresholds. The paper should clarify whether the probability of selecting an operator changes continuously or only its availability changes. In addition, the definition of \(L=0\) requires special handling because \(t/L\) is undefined; the intended fixed-mixture implementation should be stated explicitly.
2. **Baseline tuning may not be fully comparable.** CurCon is selected using a 48-configuration grid search, whereas the baselines use hyperparameters from their original papers. A fairer comparison would either tune all methods under the same validation protocol or report sensitivity to the relevant baseline hyperparameters.
3. **Statistical reporting could be stronger.** Results include standard deviations over five seeds, which is useful, but confidence intervals or paired significance tests would make the relatively modest improvements over CERT more convincing.
4. **Unlabelled-data protocol should be documented more carefully.** It would be helpful to state the exact number of unlabelled examples used, whether the validation data are excluded from intermediate training, and whether any test-derived or external corpora are involved.
5. **Augmentation details are somewhat underspecified.** Reproducibility would benefit from specifying the WordNet version, synonym-selection constraints, back-translation model and decoding settings, treatment of failed translations, and whether augmentations are independently generated for the two views.
6. **Scope of evaluation is limited.** The experiments involve only short English texts and BERT-base. This is acknowledged in the limitations, but additional evidence on longer documents, another encoder, or a non-English dataset would improve the generality of the claims.
7. **Efficiency analysis is incomplete.** The reported 12% overhead is useful, but the paper should distinguish preprocessing cost from training-time cost and report total wall-clock time and storage requirements.

These issues primarily concern experimental transparency, fairness, and reproducibility rather than the core method or the main empirical conclusion. They appear addressable without changing the paper’s central contribution.

## Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **84** | The method is coherent, the experiments include relevant baselines and ablations, and the results consistently support the claims. More rigorous baseline tuning, statistical testing, and implementation details would strengthen the evidence. |
| **Novelty** | **78** | Curriculum learning and contrastive intermediate training are established ideas, but scheduling augmentation strength within a CERT-style text contrastive pipeline is a reasonable and useful combination with a clearly defined practical contribution. |
| **Significance** | **82** | Low-resource classification is important, and the gains are consistent and larger in the most label-constrained setting. The current scope limits the breadth of the conclusions, but the method has practical value. |
| **Clarity** | **88** | The paper is well organized and readable, with a clear method description and informative tables. Some schedule and implementation details should be clarified. |

### Final average

\[
\frac{84 + 78 + 82 + 88}{4} = \mathbf{83.0}
\]

## Final recommendation: **Accept**

The paper presents a clear and useful contribution, supported by consistent results across datasets, seeds, baselines, and ablations. I recommend acceptance, with clarification of the curriculum implementation, stronger documentation of the data and augmentation pipeline, and a more carefully matched baseline-tuning protocol in the final version.