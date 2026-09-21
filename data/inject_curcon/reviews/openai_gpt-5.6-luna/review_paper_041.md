## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. Starting with mild token-level perturbations and progressively introducing stronger augmentations, CurCon adapts a pretrained BERT encoder on unlabelled in-domain text before supervised fine-tuning. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. Ablations further suggest that both the curriculum and augmentation ordering contribute to the gains.

### Strengths

1. **Clear and practically motivated problem.** The focus on text classification with only a few hundred labels is important and relevant to realistic deployment settings.
2. **Simple, modular method.** CurCon can be incorporated into an existing contrastive intermediate-training pipeline without modifying the downstream classifier or adding inference-time cost.
3. **Consistent empirical improvements.** The method improves over CERT on all four datasets and reports gains across multiple labelled-data regimes.
4. **Useful ablations.** Comparisons with a fixed mixture, reversed curriculum, removal of back-translation, and removal of the contrastive stage help isolate the contribution of the proposed design.
5. **Reproducible presentation.** The paper specifies the datasets, augmentation operators, training duration, batch size, optimizer, and evaluation protocol clearly.
6. **Good analysis of label efficiency.** The stronger gains with 100 labelled examples support the paper’s central motivation.

### Weaknesses and suggestions

1. **Baseline tuning fairness should be clarified.** CurCon is selected using a grid search over 48 configurations, whereas the baselines use hyperparameters from their original papers. This may favor the proposed method, particularly in a low-resource setting. A stronger evaluation would tune all methods under the same validation protocol or report sensitivity analyses.
2. **Statistical significance is not reported.** Although mean and standard deviation over five seeds are provided, paired significance tests or confidence intervals would strengthen the claim that the improvements are reliable. The gains are generally sizeable, but this would be useful especially for the smaller differences on TREC and at 1,000 labels.
3. **The curriculum definition could be made more precise.** The paper states that operators become available at thresholds in \(c(t)\), but it does not fully specify whether augmentation probabilities are uniform over available operators, whether views can receive different operators, or how the “strength” of token dropout and synonym replacement changes over time. These details should be explicit for exact reproduction.
4. **The comparison to CERT merits additional discussion.** Since both methods use back-translation and contrastive intermediate training, the paper should more directly distinguish CurCon from simply using a different fixed augmentation mixture. The fixed-mixture ablation is helpful, but reporting the exact mixture and perhaps several fixed-mixture alternatives would make the comparison more compelling.
5. **Scope is somewhat limited.** The experiments use four English datasets with short texts and a single encoder architecture. The authors appropriately acknowledge this limitation; even so, results on a longer-text or non-English dataset would improve the evidence for generality.
6. **Computational reporting could be expanded.** The 12% training-time increase is useful, but absolute training time, preprocessing cost, and the cost of generating or storing back-translations would provide a more complete picture.

These issues are primarily about experimental rigor and reproducibility rather than fundamental flaws in the method. The core comparisons, ablations, and label-budget analysis provide reasonable support for the main claims.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 84/100 |
| Novelty | 78/100 |
| Significance | 82/100 |
| Clarity | 90/100 |

**Final average:** \((84 + 78 + 82 + 90) / 4 = 83.5/100\)

## Final recommendation

**Accept**

The paper presents a clear and useful contribution with consistent empirical improvements and an informative ablation study. While stronger baseline tuning controls, significance testing, and implementation details would improve the work, these are addressable concerns and do not undermine the central contribution.