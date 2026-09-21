## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The approach gradually increases augmentation difficulty during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show that CurCon outperforms fine-tuning, UDA, SimCSE, and CERT. The ablations further suggest that both the curriculum direction and the inclusion of back-translation contribute to performance.

### Strengths

- **Clear and practical motivation.** The paper addresses a meaningful problem: adapting pretrained encoders when only a small labelled set is available.
- **Simple methodological contribution.** The curriculum is easy to understand and implement, adds no inference-time cost, and can be integrated into an existing CERT-style pipeline.
- **Strong empirical results.** CurCon improves average accuracy over CERT by 1.1 points and over standard fine-tuning by 3.8 points. Improvements are reported consistently across all four datasets.
- **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons directly test whether the schedule itself matters.
- **Low-resource analysis.** Results across 100, 500, and 1,000 labelled examples support the claim that the method is especially helpful when supervision is scarce.
- **Good presentation.** The method, experimental protocol, tables, limitations, and computational cost are described concisely and coherently.

### Weaknesses and suggestions

1. **Baseline tuning may not be fully comparable.** CurCon hyperparameters are selected by grid search, whereas baselines use hyperparameters reported in their original papers. For a fair comparison, all methods should ideally receive comparable tuning budgets on the same validation splits.
2. **Statistical analysis is limited.** Results include standard deviations over five seeds, but the paper does not report confidence intervals or significance tests. Given that some gains are modest, especially at 1,000 labels, paired significance testing would strengthen the conclusions.
3. **The curriculum specification could be more precise.** The description says that operator availability depends on curriculum thresholds and that available operators are sampled uniformly, but it does not fully clarify how the strength schedule translates into probabilities or whether the individual augmentation magnitudes also change continuously.
4. **Generality is not yet established.** The experiments are restricted to four English classification benchmarks, relatively short inputs, and BERT-base. Testing on additional domains, longer documents, or other encoder families would help establish broader applicability.
5. **The source and handling of unlabelled data merit clarification.** The paper should explicitly state whether all unlabelled training sentences are disjoint from the labelled subset and whether any preprocessing or augmentation resource introduces possible test-set contamination.
6. **Compute reporting could be expanded.** The reported 12% overhead is useful, but wall-clock training times, preprocessing costs for back-translation, and total resource consumption would make the cost analysis more reproducible.

These are mostly issues of experimental completeness and reproducibility rather than fundamental flaws. The central comparison is logically aligned with the proposed contribution, and the ablations provide reasonable evidence that the curriculum—not merely contrastive training or back-translation—is responsible for part of the gain.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 84/100 |
| Novelty | 78/100 |
| Significance | 81/100 |
| Clarity | 88/100 |

### Final average

\[
\frac{84 + 78 + 81 + 88}{4} = \mathbf{82.75}
\]

**Final average score: 82.8/100**

## Recommendation: Accept

CurCon presents a clear, practically motivated, and empirically supported improvement to contrastive intermediate training for low-resource text classification. Although broader evaluation, stronger baseline tuning controls, and more detailed statistical analysis would improve the paper, the method is simple, the ablations are relevant, and the reported gains are consistent across datasets and label regimes. These limitations do not undermine the main contribution, so I recommend **Accept**.