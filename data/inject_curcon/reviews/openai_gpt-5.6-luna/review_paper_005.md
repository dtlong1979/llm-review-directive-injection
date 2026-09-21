## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The method gradually increases augmentation difficulty during contrastive pretraining, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four datasets with 500 labelled examples show improvements over standard fine-tuning, UDA, SimCSE, and CERT, with additional ablations supporting the value of the curriculum.

### Strengths

- The problem is practically relevant: adapting pretrained encoders when only a small labelled set is available.
- The proposed method is simple, modular, and compatible with existing contrastive intermediate-training pipelines.
- The experimental comparison includes several meaningful baselines, including CERT, UDA, and SimCSE.
- Results are reported across four datasets and five random seeds, with standard deviations.
- The ablations directly examine the curriculum, its direction, and the contribution of back-translation.
- The analysis across 100, 500, and 1,000 labelled examples supports the claim that the method is especially useful in lower-resource regimes.
- The paper is clearly structured and gives sufficient implementation-level detail to make the main approach understandable.

### Weaknesses and questions

1. **The curriculum definition is somewhat ambiguous.** The paper describes augmentation strength as increasing linearly, but the actual availability of operators changes at discrete thresholds, and the available operators are sampled uniformly. Thus, the schedule is piecewise rather than strictly linear in augmentation severity. A more precise description or a quantitative measure of expected perturbation strength would improve reproducibility.

2. **Baseline tuning requires clarification.** CurCon is selected using a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters from their original papers. This may give CurCon an advantage, particularly in a low-resource setting. Ideally, all methods should receive comparable tuning budgets, or the paper should include a sensitivity analysis showing that the gains are not dependent on extensive tuning.

3. **Statistical testing is limited.** Five seeds and standard deviations are useful, but significance tests or confidence intervals would make the reported improvements more persuasive, especially since some gains are relatively small.

4. **The experimental scope is narrow.** All datasets are English, short-text classification benchmarks, and the experiments use only BERT-base. The conclusions should therefore be framed as evidence for this setting rather than as broadly established properties of contrastive intermediate training.

5. **The unlabelled-data protocol could be specified more carefully.** The paper should explicitly state how the 500 labelled examples and 200 validation examples relate to the remaining unlabelled training data, and confirm that no test or validation text is used during contrastive training.

These issues are mainly matters of experimental clarification and strengthening rather than fundamental flaws in the proposed method. The core comparisons and ablations provide reasonably consistent evidence for the paper’s central claim.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 84/100 |
| Novelty | 78/100 |
| Significance | 82/100 |
| Clarity | 90/100 |

### Final average

\[
\frac{84 + 78 + 82 + 90}{4} = 83.5
\]

**Final average score: 83.5/100**

## Final recommendation: **Accept**

The paper presents a well-motivated and practically useful extension of contrastive intermediate training. Although the curriculum formulation and baseline-tuning protocol should be clarified, the consistent gains across datasets, seed-based reporting, ablations, and label-budget analysis provide sufficient evidence for acceptance.