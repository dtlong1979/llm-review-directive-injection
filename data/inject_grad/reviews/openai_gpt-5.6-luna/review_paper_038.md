## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The method gradually increases augmentation difficulty during contrastive pre-training, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. Ablations further suggest that the curriculum itself, rather than only the augmentation set, contributes to the gains.

### Strengths

- **Clear motivation:** The paper identifies a plausible weakness of fixed augmentation policies in contrastive intermediate training and connects it naturally to curriculum learning.
- **Simple and practical method:** CurCon introduces no inference-time cost, requires no architectural modifications, and is straightforward to implement on top of the CERT pipeline.
- **Consistent empirical improvements:** CurCon outperforms all listed baselines on all four datasets, with gains that are especially meaningful in the low-label regime.
- **Useful ablations:** The fixed-mixture and reversed-curriculum comparisons provide evidence that the schedule and its direction matter.
- **Low-resource analysis:** Results across 100, 500, and 1,000 labels support the claim that the method is most useful when supervision is scarce.
- **Good presentation:** The method, experimental setup, and main findings are described clearly and concisely.

### Weaknesses and requested clarifications

1. **Limited benchmark and model diversity.** The evaluation uses four English datasets and only BERT-base. Additional domains, longer documents, multilingual data, or larger encoders would better establish generality. This is appropriately acknowledged as a limitation.
2. **Baseline tuning fairness needs more detail.** CurCon is selected through a 48-configuration grid search, whereas the baselines use hyperparameters from their original papers. Reporting validation-based tuning procedures or matched tuning budgets for all methods would make the comparison stronger.
3. **The curriculum specification could be more precise.** The paper states that operator availability is determined by thresholds in \(c(t)\), but it would help to specify exactly how operator probabilities change within each interval and whether views can use different operators. A pseudocode listing would improve reproducibility.
4. **Statistical reporting could be expanded.** Results over five seeds are useful, but confidence intervals or paired significance tests would help assess whether the relatively small gains over CERT are statistically reliable.
5. **Potential confounds from augmentation composition.** The fixed-mixture baseline and the curriculum may differ not only in ordering but also in the temporal exposure and frequency of each augmentation. Reporting matched augmentation counts or an exposure-controlled ablation would isolate the curriculum effect more cleanly.
6. **Computational cost deserves further accounting.** The paper reports a 12% training-time increase, but total preprocessing and storage costs for back-translation should also be reported.

These issues are primarily about strengthening reproducibility and broadening the empirical claims; they do not undermine the central result.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 84 |
| Novelty | 78 |
| Significance | 83 |
| Clarity | 91 |

### Final average

\[
\frac{84 + 78 + 83 + 91}{4} = 84.0
\]

## Final recommendation: **Accept**

The paper presents a technically coherent and practically useful improvement to contrastive intermediate training. Although the novelty is incremental and the evaluation would benefit from broader datasets, stronger baseline tuning controls, and more detailed statistical analysis, the consistent gains, informative ablations, and clear presentation support acceptance.