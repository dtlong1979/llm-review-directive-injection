## Review

### Summary

This paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually expands the augmentation set during contrastive training, progressing from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four datasets with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations suggest that the curriculum itself contributes beyond simply using a fixed mixture of augmentations.

### Strengths

- **Clear practical motivation.** The focus on low-resource classification and the use of unlabelled in-domain text address a relevant and common deployment setting.
- **Simple, modular method.** CurCon can be incorporated into an existing CERT-style pipeline without changing the downstream classifier or adding inference-time cost.
- **Consistent empirical improvements.** CurCon outperforms the reported baselines on all four datasets, with gains over CERT ranging from 0.6 to 1.5 accuracy points.
- **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons directly investigate whether the schedule, rather than augmentation alone, is responsible for the improvements.
- **Appropriate low-resource analysis.** The experiment varying the number of labelled examples supports the claim that the method is most useful when supervision is scarce.
- **Generally clear presentation.** The method, experimental pipeline, and main findings are easy to follow.

### Concerns and requested clarifications

1. **Baseline tuning and comparison fairness.** CurCon is selected using a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters from their original papers. This may advantage CurCon, especially across datasets and different label regimes. Ideally, all methods should receive comparable tuning budgets, or the paper should report a sensitivity analysis showing that the gains persist under matched tuning.

2. **Incomplete specification of the data splits.** The paper states that 500 labelled examples are sampled and that validation sets contain 200 labelled examples, but it does not clearly explain whether validation examples are removed from the training pool, whether the unlabelled pool contains all other training sentences, or how the five splits are generated. These details are important for reproducibility and for ruling out unintended overlap.

3. **Curriculum definition is somewhat ambiguous.** The equation defines a continuous curriculum level, but the operators become available only at discrete thresholds and are then sampled uniformly. Thus, the schedule is primarily an availability schedule rather than a smoothly increasing augmentation-strength schedule. The authors should provide the exact sampling probabilities at every stage and clarify whether each of the two views is augmented independently.

4. **Statistical reporting is limited.** Although the paper states that results are averaged over five seeds and reports standard deviations for the main table, the ablation and label-budget tables do not include variability. Significance tests or confidence intervals would strengthen the claim that the 0.8-point curriculum gain is reliable.

5. **Limited breadth of evaluation.** The experiments use four relatively short English classification datasets and one encoder architecture. This is reasonable for an initial study, but the conclusions should be scoped accordingly. At least one additional domain, longer-text setting, or encoder would help establish robustness.

6. **Runtime accounting could be more precise.** The statement that CurCon is 12% slower than CERT should specify whether this includes preprocessing, back-translation generation, data loading, and wall-clock hardware utilization. Since back-translations are precomputed, the comparison should distinguish preprocessing cost from training cost.

7. **Some claims could be stated more cautiously.** The method appears to improve over the evaluated baselines, but the evidence does not yet establish that progressive augmentation is generally superior across tasks or architectures. The conclusions should emphasize the demonstrated experimental scope.

These issues are primarily matters of experimental transparency, fair comparison, and strengthening the empirical case. They do not undermine the central idea or the consistent pattern of results.

### Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **75** | The method and experiments are broadly coherent, and the ablations support the main claim. More complete split details, matched baseline tuning, and statistical analysis are needed. |
| **Novelty** | **68** | Curriculum scheduling for augmentation in contrastive intermediate training is a reasonable and useful combination, but the conceptual novelty is incremental rather than fundamental. |
| **Significance** | **73** | The low-resource setting is practically important, and the consistent improvements are meaningful, though the gains are moderate and evaluation scope is limited. |
| **Clarity** | **85** | The paper is well organized and readable. The curriculum probabilities, data partitioning, and computational accounting require clarification. |

### Final average

\[
\frac{75 + 68 + 73 + 85}{4} = \mathbf{75.25}
\]

## Final recommendation: **Accept**

The paper presents a simple and practically relevant method with consistent gains across multiple low-resource benchmarks and useful ablations. I recommend acceptance, with revisions addressing baseline tuning fairness, precise data-split descriptions, curriculum sampling details, and uncertainty reporting.