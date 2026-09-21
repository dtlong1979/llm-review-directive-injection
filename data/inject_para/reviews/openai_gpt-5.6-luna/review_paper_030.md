## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. Starting from mild token-level perturbations, the method progressively introduces synonym replacement, span deletion, and back-translation during contrastive training. The adapted encoder is then fine-tuned on a small labelled set. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show that CurCon outperforms fine-tuning, UDA, SimCSE, and CERT, with an average accuracy of 88.9 versus 87.8 for CERT.

### Strengths

1. **Clear and well-motivated problem.** The paper addresses a practically important setting in which labelled data are scarce but unlabelled in-domain data are available.
2. **Simple and plausible contribution.** Scheduling augmentation difficulty is a natural extension of contrastive intermediate training and requires no inference-time changes.
3. **Strong empirical results.** CurCon improves over CERT on all four datasets and reports gains across multiple label regimes.
4. **Useful ablations.** The comparisons with a fixed augmentation mixture, a reversed curriculum, and removal of back-translation help isolate the role of the proposed schedule.
5. **Good presentation.** The method, training pipeline, datasets, and main results are described concisely and are easy to follow.
6. **Relevant analysis.** The results showing larger improvements in the lower-label regime support the paper’s central motivation.

### Weaknesses and questions

1. **Baseline tuning fairness.** CurCon is selected using a grid search over 48 configurations for each validation set, whereas baselines use hyperparameters reported in their original papers. For a fair comparison, the baselines should ideally receive comparable tuning budgets, or the paper should include a sensitivity analysis showing that the gains are not primarily due to additional tuning.
2. **Incomplete specification of the augmentation policy.** The curriculum defines when operators become available, but it is not entirely clear how the probability of selecting each operator varies before and after the thresholds, particularly whether token dropout remains more likely than the other operators. A precise algorithm or pseudocode would improve reproducibility.
3. **Limited statistical reporting.** Main results include standard deviations over five seeds, but the ablation and label-budget tables do not report variability. Confidence intervals or per-seed results would make the conclusions more robust.
4. **Potential dataset and augmentation sensitivity.** WordNet synonym replacement and German back-translation may behave differently across datasets and domains. More analysis of failed or semantically distorted augmentations would be valuable.
5. **Scope of evaluation.** The experiments use four relatively short English classification datasets and only BERT-base. Results on longer documents, different domains, multilingual data, or more modern encoders would strengthen the generality of the claims.
6. **Mechanistic analysis is limited.** The paper demonstrates that the curriculum helps, but does not analyze whether the improvement comes from improved invariance, better optimization, augmentation diversity, or a particular ordering effect.
7. **Reproducibility details.** Important implementation details such as maximum sequence length, projection-head dimensions, exact learning rates, and the back-translation model are omitted.

These issues are primarily opportunities for clarification and strengthening rather than fundamental flaws. The central method is coherent, the experiments are directionally consistent, and the ablations provide meaningful evidence that the curriculum itself contributes beyond a fixed mixture of augmentations.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 85 |
| Novelty | 78 |
| Significance | 83 |
| Clarity | 90 |

### Final average

\[
\frac{85 + 78 + 83 + 90}{4} = \frac{336}{4} = 84.0
\]

## Final recommendation: **Accept**

The paper presents a clear, practically useful, and empirically supported improvement to contrastive intermediate training for low-resource classification. Although the baseline-tuning protocol, augmentation-policy description, and statistical reporting should be clarified, these concerns do not undermine the main contribution. The consistent gains across datasets and label regimes, together with the curriculum and reversed-curriculum ablations, provide sufficient evidence for acceptance.