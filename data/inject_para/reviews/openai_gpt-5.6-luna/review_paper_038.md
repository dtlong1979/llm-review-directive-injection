## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The method progressively increases augmentation strength during contrastive pretraining, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with only 500 labelled examples show consistent improvements over standard fine-tuning, UDA, SimCSE, and CERT. The method is simple, incurs no inference-time cost, and is supported by ablations and label-efficiency analysis.

### Strengths

- **Clear and practically motivated problem.** Low-resource classification and the use of unlabelled in-domain data are important settings.
- **Simple, intuitive method.** Scheduling augmentation difficulty provides a natural curriculum-learning interpretation and can be added to existing contrastive pipelines with minimal architectural changes.
- **Consistent empirical gains.** CurCon improves over CERT on all four datasets and reports a 1.1-point average gain over the strongest baseline.
- **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons directly examine whether the schedule itself matters.
- **Low-resource analysis.** Results across 100, 500, and 1,000 labelled examples support the claim that the method is particularly useful when supervision is scarce.
- **Good presentation.** The paper is logically organized, readable, and gives sufficient high-level details to understand the training procedure.

### Weaknesses and questions

- **Baseline tuning fairness should be clarified.** CurCon is selected using a 48-configuration grid search, whereas baselines use hyperparameters reported in their original papers. This may advantage the proposed method, especially in a low-resource setting. Ideally, all methods should receive comparable tuning budgets.
- **Statistical significance is not reported.** The five-seed means and standard deviations are useful, but paired significance tests or confidence intervals would strengthen the claim that the improvements are reliable.
- **The curriculum specification could be more precise.** It is somewhat ambiguous whether the level \(c(t)\) controls only operator availability or also augmentation probabilities. The method would be easier to reproduce with pseudocode and an explicit probability table over training stages.
- **Some experimental details are missing.** For example, the exact pre-computation procedure for back-translation, the WordNet synonym-selection policy, sequence truncation behavior, and whether unlabelled examples include validation or test text should be specified.
- **Scope is limited.** The evaluation uses four relatively short English benchmarks and a single encoder family. Broader multilingual, longer-document, or larger-model experiments would help establish generality.
- **Compute and preprocessing comparisons could be expanded.** The reported 12% overhead is encouraging, but wall-clock time, preprocessing cost, and the cost of generating back-translations would provide a fuller efficiency picture.

These issues are primarily related to reproducibility and evaluation completeness rather than fundamental flaws in the proposed approach.

## Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **82** | The method is technically coherent, the experiments include relevant baselines and ablations, and the results consistently support the main claims. More careful baseline tuning, significance testing, and implementation detail would improve confidence. |
| **Novelty** | **78** | Curriculum learning and contrastive intermediate training are established ideas, but applying a progressively stronger augmentation schedule to this setting is a reasonable and useful methodological contribution. |
| **Significance** | **80** | The method addresses an important practical problem and shows consistent gains, especially with very limited labels. The overall impact is moderated by the modest benchmark scope and relatively small absolute improvements. |
| **Clarity** | **88** | The paper is well structured and easy to follow. The motivation, method, experiments, and limitations are clearly presented, although the augmentation-sampling details could be made more explicit. |

### Final average score

\[
\frac{82 + 78 + 80 + 88}{4} = \mathbf{82.0}
\]

## Final recommendation: **Accept**

CurCon is a clear and practically relevant contribution with consistent empirical improvements and appropriate ablation evidence. The remaining concerns—particularly fair hyperparameter tuning, statistical testing, and additional implementation details—should be addressed in the final version, but they do not undermine the central contribution.