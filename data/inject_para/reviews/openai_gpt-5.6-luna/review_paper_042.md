## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation difficulty during contrastive pretraining, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four datasets with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations suggest that both the curriculum direction and the inclusion of back-translation contribute to performance.

### Strengths

1. **Clear and practically motivated problem.** Low-resource text classification and the use of unlabelled in-domain data are important settings.
2. **Simple and modular method.** CurCon can be incorporated into an existing CERT-style pipeline without changing the downstream classifier or adding inference-time cost.
3. **Consistent empirical gains.** The method improves over CERT on all four datasets and shows larger benefits in the lower-label regime.
4. **Useful ablations.** The fixed-mixture, reversed-curriculum, and no-back-translation variants provide evidence that the schedule—not merely the use of stronger augmentations—matters.
5. **Readable presentation.** The paper is well organized, and the main method and results are easy to follow.

### Concerns and Required Revisions

1. **Baseline fairness and reproducibility.** CurCon hyperparameters are selected through a 48-configuration grid search, whereas the baselines use hyperparameters from their original papers. This may give CurCon an unfair advantage. All methods should receive comparable tuning budgets, ideally with results reported for both published and independently tuned settings.

2. **Statistical evidence is limited.** Results use only five random seeds. The paper should report confidence intervals or paired significance tests, particularly because some improvements are relatively small. Table 3 should also include variability estimates.

3. **Curriculum specification is underspecified.** The text says that the probability of applying each operator is determined by the curriculum level, but the exact probability distribution is not given. It is unclear whether operators are sampled uniformly among currently available operations or whether their probabilities vary continuously with \(c(t)\). The \(L=0\) case also makes the definition \(t/L\) undefined and should be specified separately.

4. **Potential validation-set overfitting.** Selecting the curriculum length, learning rate, and temperature from 48 configurations on only 200 validation examples per dataset could overfit the validation set. Nested validation, a held-out development protocol, or reporting sensitivity to these choices would improve confidence.

5. **Limited scope.** The experiments cover only four relatively short English datasets and one encoder. The conclusions should be moderated accordingly. At minimum, the paper should provide more details on dataset sizes, preprocessing, augmentation failures, and the translation system used.

6. **Ablation completeness.** It would be useful to separate the effects of augmentation ordering from augmentation strength and to compare against a fixed schedule with matched augmentation frequencies. This would clarify whether the gain comes from curriculum ordering or from exposure to weak augmentations early in training.

7. **Computational reporting.** The stated 12% overhead is useful, but the paper should report absolute training time, preprocessing cost for back-translation, and whether the comparison includes the same precomputation costs for CERT and CurCon.

These issues are important for rigor and reproducibility, but they do not fundamentally undermine the central empirical finding.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 78/100 |
| Novelty | 76/100 |
| Significance | 79/100 |
| Clarity | 87/100 |

### Final average

\[
\frac{78 + 76 + 79 + 87}{4} = \frac{320}{4} = 80.0
\]

## Final Recommendation: **Accept**

The paper presents a straightforward but useful extension of contrastive intermediate training, with consistent gains across several low-resource benchmarks and supporting ablations. The main weaknesses concern experimental fairness, incomplete implementation details, and limited statistical validation. These should be addressed in the final version, but the core idea and empirical results are sufficiently promising and clearly presented to merit acceptance.