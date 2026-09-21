## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation strength during contrastive training, moving from token dropout toward synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations suggest that both the curriculum and back-translation contribute to performance.

### Strengths

- **Clear and practically relevant motivation.** The focus on low-resource classification and the use of unlabelled in-domain data address an important and common setting.
- **Simple, model-agnostic method.** CurCon can be incorporated into an existing CERT-style pipeline without changing the downstream classifier or adding inference-time parameters.
- **Consistent empirical gains.** CurCon improves over CERT on all four datasets and reports gains across multiple label regimes.
- **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons directly test whether the schedule itself matters.
- **Appropriate analysis of label efficiency.** The larger improvements in the 100-example setting support the paper’s central low-resource motivation.
- **Generally clear presentation.** The method, datasets, baselines, and main results are described in an accessible and coherent manner.

### Weaknesses and requested clarifications

1. **Baseline tuning and fairness.** CurCon is selected using a grid search over 48 configurations per dataset, whereas the baselines use hyperparameters from their original papers. This may advantage CurCon, particularly in a low-resource setting. Ideally, all methods should receive comparable validation-based tuning budgets, or the paper should report a controlled sensitivity analysis.
2. **Schedule specification could be more precise.** The curriculum defines when operators become available, but it is not fully clear whether the operator probabilities are uniform over the available operators or whether the curriculum level also changes their probabilities continuously. Exact pseudocode would improve reproducibility.
3. **Statistical reporting.** Results are averaged over five seeds, which is useful, but significance testing or confidence intervals for the paired dataset-level comparisons would strengthen the conclusions.
4. **Scope of evaluation.** The datasets are all English and relatively short. The limitations acknowledge this appropriately, but broader domains, longer documents, or additional encoder families would help establish generality.
5. **Cost comparison.** The stated 12% overhead is informative, although the comparison would be more meaningful if preprocessing, translation, and cached-view generation costs were reported separately.
6. **Potential interaction among augmentations.** The ablations isolate back-translation but do not evaluate whether the benefit comes from the specific ordering, the changing augmentation diversity, or merely delaying the strongest augmentation. A few additional schedule controls would help disentangle these effects.

These issues primarily concern experimental completeness and reproducibility rather than the core validity of the approach. The reported results and ablations are consistent with the proposed mechanism, and the method is sufficiently specified to support the main claims.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 82/100 |
| Novelty | 76/100 |
| Significance | 78/100 |
| Clarity | 86/100 |

### Final average

\[
\frac{82 + 76 + 78 + 86}{4} = \frac{322}{4} = \mathbf{80.5}
\]

## Final recommendation: **Accept**

CurCon offers a simple and credible improvement to contrastive intermediate training for low-resource text classification. Although the experimental protocol would benefit from more carefully matched hyperparameter tuning and additional schedule controls, the consistent gains, relevant ablations, and clear presentation make the work suitable for acceptance.