## Review

### Summary

This paper proposes CurCon, a curriculum for contrastive intermediate training in which text augmentations become progressively stronger during adaptation on unlabelled in-domain data. The method is simple: it begins with token dropout and progressively enables synonym replacement, span deletion, and back-translation. Experiments on four standard text-classification datasets in a 500-label regime show consistent improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- **Clear and practically motivated problem.** The paper addresses an important issue in low-resource classification: how to make effective use of unlabelled in-domain text.
- **Simple, model-agnostic method.** The proposed curriculum can be incorporated into existing contrastive intermediate-training pipelines without inference-time changes or additional model parameters.
- **Consistent empirical gains.** CurCon outperforms CERT on all four reported datasets, with improvements ranging from 0.6 to 1.5 accuracy points.
- **Relevant ablations.** The fixed-mixture and reversed-curriculum comparisons support the claim that the schedule, rather than only the augmentation set, contributes to the result.
- **Useful label-efficiency analysis.** The larger gain at 100 labelled examples is consistent with the stated motivation.
- **Generally clear presentation.** The method and experimental pipeline are described in a reasonably accessible way.

### Concerns

1. **Limited experimental breadth.** The evaluation uses only four English datasets, all with relatively short texts, and only BERT-base. The conclusions should therefore be framed as evidence for this setting rather than as broadly established across low-resource classification.

2. **Baseline tuning is potentially imbalanced.** CurCon is selected using a 48-configuration validation grid on each dataset, whereas the baselines use hyperparameters from their original papers. For a fair comparison, the baselines should receive comparable tuning budgets, or the paper should report sensitivity analyses and clearly distinguish transferred from re-tuned configurations.

3. **Insufficient protocol detail.** The sampling procedure for the 500 labelled examples, construction of the 200-example validation sets, treatment of the remaining training data, and prevention of overlap between labelled, validation, and unlabelled subsets should be specified more precisely. Results would be more convincing if the same sampled splits were used across methods and multiple label-sampling repetitions were reported.

4. **The curriculum definition is somewhat coarse.** The schedule is described as linearly increasing curriculum strength, but operators are actually introduced at discrete thresholds. This is a staged availability schedule rather than a fully continuous linear increase in augmentation magnitude. The paper should clarify this distinction and compare thresholded, smoothly weighted, and perhaps randomly ordered schedules.

5. **Ablation reporting is incomplete.** The ablation table reports only averages. Per-dataset results and standard deviations would help determine whether the effect is robust or driven primarily by one or two datasets. It would also be useful to isolate the effects of individual operators and their ordering.

6. **Statistical analysis could be stronger.** Five random seeds are helpful but limited, especially in a 100- or 500-label regime. Confidence intervals or paired significance tests across identical splits would better support claims of consistent improvement.

7. **Some implementation details are underspecified.** Important reproducibility information includes the exact back-translation system, WordNet processing rules, tokenization and truncation behavior, projection-head dimensions, optimizer schedules, maximum sequence length, and the precise handling of multiple augmentations per view.

8. **Cost analysis is narrow.** The reported 12% overhead excludes the cost of generating or obtaining back-translations because they are pre-computed. The paper should distinguish preprocessing cost, storage cost, and training-time cost, and report absolute runtimes where possible.

These issues mainly affect the strength and generality of the conclusions rather than the core plausibility of the method. The central comparison and ablations provide reasonable initial evidence that scheduling augmentation difficulty can improve contrastive intermediate training.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 75 |
| Novelty | 70 |
| Significance | 76 |
| Clarity | 84 |

**Final average:** \((75 + 70 + 76 + 84)/4 = 76.25\)

### Final recommendation

**Accept**

The contribution is incremental but useful, and the method is simple, clearly motivated, and supported by consistent results and relevant ablations. Acceptance is appropriate provided the final version strengthens the experimental-protocol description, balances baseline tuning, reports uncertainty and per-dataset ablations, and clarifies the computational-cost accounting.