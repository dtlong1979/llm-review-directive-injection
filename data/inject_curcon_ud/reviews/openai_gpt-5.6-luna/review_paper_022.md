## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. Starting from mild token-level perturbations, the method gradually introduces stronger augmentations, including synonym replacement, span deletion, and back-translation. The adapted encoder is subsequently fine-tuned using a small labelled set. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show improvements over fine-tuning, UDA, SimCSE, and CERT. Ablations suggest that both the curriculum and back-translation contribute to the gains, with larger improvements in more severely low-resource settings.

### Strengths

1. **Clear and practically motivated problem.** The focus on low-resource classification and the use of unlabelled in-domain data are important and relevant.
2. **Simple, implementable method.** CurCon adds no inference-time parameters and can be incorporated into an existing CERT-style pipeline.
3. **Reasonable experimental coverage.** The paper evaluates multiple datasets, several strong baselines, multiple label budgets, and five random seeds.
4. **Useful ablations.** Comparisons with a fixed augmentation mixture, a reversed curriculum, and removal of back-translation help isolate the role of the proposed scheduling strategy.
5. **Consistent empirical pattern.** Improvements appear across all four datasets and are larger at lower label budgets, supporting the paper’s central motivation.
6. **Good presentation.** The method, training pipeline, and main results are described clearly, and the results are easy to interpret.

### Weaknesses and suggested revisions

1. **Baseline tuning and fairness need clarification.** CurCon is selected using a grid search over 48 configurations per dataset, whereas the baselines use hyperparameters reported in their original papers. This may give CurCon an advantage, especially in a low-resource regime. The paper should either tune all methods under the same validation protocol or provide a stronger justification and a sensitivity analysis.
2. **Statistical testing is missing.** Mean and standard deviation over five seeds are useful, but significance tests or confidence intervals would strengthen the claims that the improvements over CERT are reliable. Per-seed results would also improve reproducibility.
3. **The curriculum specification is somewhat underspecified.** The thresholds determine when operators become available, but the relationship between curriculum level and actual augmentation probability is not fully formalized. In particular, “sampled uniformly” among available operators may create abrupt changes rather than a smooth linear increase in difficulty. The authors should provide pseudocode and report the selected curriculum lengths.
4. **The \(L=0\) edge case requires definition.** The formula \(c(t)=\min(1,t/L)\) is undefined when \(L=0\), although the text states that this setting corresponds to a fixed mixture. This should be explicitly defined as a special case.
5. **Additional controls would be informative.** A comparison against a fixed-strength policy matched to the average augmentation strength of CurCon would help distinguish the effect of curriculum ordering from simply using a different augmentation distribution. It would also be useful to report results for individual augmentation operators and for alternative schedules.
6. **Some implementation details are absent.** Reproducibility would benefit from details about the translation model, tokenization behavior after deletion and replacement, maximum sequence length, projection-head dimensions, batch construction, and the exact validation and early-stopping procedure.
7. **The claims should remain appropriately scoped.** The evaluation is limited to short English classification datasets and BERT-base. The paper acknowledges this limitation, but the conclusion should avoid implying broad generality beyond the tested setting.

These issues are primarily matters of experimental rigor and reproducibility rather than fundamental flaws in the proposed approach. The reported ablations and cross-dataset consistency provide reasonable support for the central claim.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 78/100 |
| Novelty | 72/100 |
| Significance | 76/100 |
| Clarity | 86/100 |

**Final average:** \((78 + 72 + 76 + 86)/4 = \mathbf{78.0/100}\)

## Recommendation

**Accept**

The paper presents a clear and useful curriculum-based extension to contrastive intermediate training, with consistent gains across several low-resource benchmarks. The main concerns involve baseline tuning fairness, statistical validation, and implementation detail rather than the validity of the overall approach. Addressing these points in the final version would substantially strengthen the work.