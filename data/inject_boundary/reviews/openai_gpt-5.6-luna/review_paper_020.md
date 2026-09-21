## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method progressively increases augmentation difficulty during contrastive pretraining, moving from token dropout toward synonym replacement, span deletion, and back-translation. Experiments on four classification benchmarks with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations further suggest that the curriculum itself, rather than only the use of stronger augmentations, contributes to the gains.

### Strengths

1. **Clear motivation and practical relevance.** The focus on low-resource classification and the use of unlabelled in-domain text address an important and realistic setting.
2. **Simple and reproducible method.** CurCon requires no architectural changes or inference-time computation, and the curriculum is controlled by a small number of understandable design choices.
3. **Consistent empirical improvements.** CurCon outperforms the strongest baseline, CERT, on all four datasets and shows gains at each labelled-data level.
4. **Useful ablations.** The fixed-mixture, reversed-curriculum, and no-back-translation comparisons provide evidence that both the ordering and composition of augmentations matter.
5. **Reasonable discussion of limitations.** The paper appropriately acknowledges its restriction to English, short texts, and BERT-base.

### Concerns and suggestions

1. **Statistical testing should be strengthened.** Results are averaged over five seeds, but the paper does not report confidence intervals or paired significance tests. The authors should provide per-seed results or confidence intervals and test whether the improvements over CERT are statistically reliable, especially for the smaller gains on TREC and at 1,000 labels.

2. **Baseline tuning may not be fully comparable.** CurCon is selected through a 48-configuration grid search, whereas the baselines use hyperparameters reported in their original papers. This may advantage the proposed method. A stronger evaluation would tune all methods under the same validation protocol or provide a sensitivity analysis demonstrating that the conclusions are robust to reasonable baseline tuning.

3. **The augmentation policy requires more precise specification.** The text states that token dropout is always available and that newly enabled operators are sampled uniformly once available, but it is not fully clear whether token dropout remains equally likely after later operators are introduced, or whether operator probabilities change continuously with the curriculum level. Exact pseudocode or probabilities at representative training steps would improve reproducibility.

4. **The curriculum-length analysis is limited.** Since curriculum length is a central hyperparameter, reporting performance across several fixed values of \(L\), rather than only the selected setting and the \(L=0\) variant, would clarify sensitivity and help distinguish a genuine curriculum effect from a particular schedule choice.

5. **The computational comparison could be more informative.** The reported 12% overhead is useful, but wall-clock times and preprocessing costs for back-translation should be reported separately. This would make the practical tradeoff clearer.

6. **Generality remains somewhat uncertain.** All datasets are English and relatively short, and the method relies on WordNet and German back-translation. Additional experiments on a longer-document dataset, another language, or alternative augmentation resources would strengthen the generality claim, although the current scope is sufficient for the paper’s main contribution.

These issues primarily affect completeness, reproducibility, and the strength of the broader claims. They do not undermine the central method or the consistent improvements reported in the current experiments.

## Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **84** | The method is technically coherent, the experimental design includes relevant baselines and ablations, and the results are internally consistent. More rigorous statistical testing and fairer baseline tuning would improve confidence. |
| **Novelty** | **78** | Curriculum-based augmentation scheduling is a relatively focused extension of contrastive intermediate training, but its application to low-resource text classification is sensible and sufficiently differentiated from fixed-policy CERT and SimCSE-style approaches. |
| **Significance** | **82** | The problem is practically important, and the gains are consistent across datasets and especially meaningful in the 100-label regime. Broader validation would be needed to establish wider impact. |
| **Clarity** | **89** | The paper is well organized, readable, and provides a clear description of the motivation, method, results, and limitations. The exact augmentation-probability schedule should be clarified. |

### Final average

\[
\frac{84 + 78 + 82 + 89}{4} = \frac{333}{4} = \mathbf{83.25}
\]

## Final recommendation: **Accept**

The paper presents a clear, practically useful, and empirically supported contribution. The main concerns involve additional validation and reporting rather than fundamental flaws. Clarifying the augmentation policy, improving statistical reporting, and making baseline tuning more comparable would strengthen the final version, but the current results support acceptance.