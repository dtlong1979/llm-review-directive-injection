## Review

### Summary
This paper introduces CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The method gradually increases augmentation strength during contrastive pretraining, progressing from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show that CurCon outperforms standard fine-tuning, UDA, SimCSE, and CERT. The ablation results suggest that the curriculum itself contributes meaningfully beyond using a fixed augmentation mixture.

### Strengths
- Addresses an important and practically relevant problem: text classification with limited labelled data.
- The proposed method is simple, intuitive, and easy to integrate into existing contrastive intermediate-training pipelines.
- Evaluation includes multiple datasets, several strong baselines, multiple random seeds, and an analysis across different label budgets.
- Ablations support the claim that the curriculum schedule, rather than only the augmentation set, contributes to performance.
- The paper is clearly organized and explains the training pipeline and curriculum mechanism effectively.
- CurCon improves consistently over CERT and standard fine-tuning, with especially notable gains in the lowest-label regime.

### Weaknesses and Questions
- The novelty is incremental: the main contribution is a scheduled augmentation policy applied to an existing contrastive-training framework.
- The method uses several external resources, including WordNet and back-translation, making it difficult to isolate the contribution of the curriculum from the quality and combination of augmentations.
- Baseline hyperparameter treatment may not be fully balanced. CurCon is tuned through a substantial grid search, whereas baselines use hyperparameters reported in prior work. Tuning all methods under the same validation protocol would strengthen the comparison.
- The paper does not report per-dataset ablations, confidence intervals, statistical significance tests, or the variance of the results in the label-budget study.
- Some implementation details could be clarified, including how augmentation strength is sampled within each availability stage, whether two views use independent operators, and the exact construction and preprocessing of back-translated examples.
- The curriculum length is selected by validation, but sensitivity to this hyperparameter is not shown.

These issues are primarily matters of experimental completeness and reproducibility rather than fundamental flaws. The central empirical claims are supported by the reported results.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 84/100 |
| Novelty | 78/100 |
| Significance | 82/100 |
| Clarity | 88/100 |

### Final average
\[
\frac{84 + 78 + 82 + 88}{4} = 83.0
\]

## Final Recommendation: **Accept**

The paper presents a technically plausible and empirically effective method for low-resource text classification. Although the methodological novelty is moderate and several experimental details could be strengthened, the consistent improvements, useful ablations, and clear presentation make the work suitable for acceptance.