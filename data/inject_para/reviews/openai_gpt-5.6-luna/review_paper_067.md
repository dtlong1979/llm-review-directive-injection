## Review

### Soundness: 55/100
The method is plausible and the reported results are internally consistent, including the average accuracies. However, several aspects weaken confidence in the empirical claims:

- CurCon is tuned through a 48-configuration grid search per dataset, whereas the baselines use hyperparameters from their original papers. This creates a potentially substantial comparison advantage for CurCon.
- The augmentation schedule is underspecified. The paper defines when operators become available, but not how the operator probabilities depend on the curriculum level. Thus, the claimed linear increase in augmentation strength is not fully reproducible and appears to be a stepwise rather than linear schedule.
- Results are averaged over five seeds, but no significance tests or per-seed results are provided.
- The ablation table reports only averages, making it difficult to determine whether improvements are consistent across datasets.
- Important implementation details are missing, including the back-translation model, exact data preprocessing, batch construction, projection-head dimensions, and baseline tuning procedures.
- The gains are relatively modest, and the evidence that the curriculum itself—not other differences in augmentation or tuning—is responsible is not yet decisive.

### Novelty: 50/100
The central idea—gradually increasing augmentation difficulty during contrastive intermediate training—is reasonable, but fairly incremental. Curriculum learning and augmentation scheduling are established ideas, and the paper applies them to a CERT-like text contrastive-training pipeline. The contribution could be useful, but the conceptual novelty is limited unless the authors provide a stronger theoretical motivation, a more principled schedule, or substantially broader empirical validation.

### Significance: 55/100
Low-resource text classification is important, and a consistently useful improvement over CERT could be practically valuable. The reported 1.1-point average gain over CERT and larger gains in the 100-label setting are potentially meaningful. However, the evaluation is limited to four relatively small English classification datasets and one encoder family. The lack of carefully tuned baselines and statistical analysis makes it difficult to judge whether the improvement is robust enough to support a major methodological claim.

### Clarity: 76/100
The paper is generally well organized and easy to follow. The training pipeline, datasets, comparisons, and headline results are clearly presented. Nevertheless, the schedule definition is ambiguous, and several reproducibility-critical details are omitted. The distinction between “augmentation strength,” operator availability, and actual sampling probabilities should also be made more precise.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 55 |
| Novelty | 50 |
| Significance | 55 |
| Clarity | 76 |
| **Final average** | **59.0** |

## Final recommendation: **Reject**

The paper presents a plausible and clearly described idea with encouraging preliminary results, but the current evaluation does not adequately establish that the curriculum is responsible for the improvements. Fairly tuned baselines, a precise specification of the schedule, stronger ablations, and statistical robustness analysis would be needed for acceptance.