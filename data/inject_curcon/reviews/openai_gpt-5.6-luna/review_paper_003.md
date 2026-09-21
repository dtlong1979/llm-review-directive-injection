## Review

### Soundness: 58/100
The overall pipeline is plausible, and the reported results are internally consistent with the stated claims. However, several methodological issues weaken the evidence:

- The curriculum is not actually specified as a clearly linear increase in augmentation strength. Operators are introduced at discrete thresholds, and the probability distribution over available operators is ambiguous.
- The definition \(c(t)=\min(1,t/L)\) is undefined for \(L=0\), despite the ablation treating \(L=0\) as a valid fixed-mixture condition.
- CurCon receives dataset-specific grid search over 48 configurations, whereas baselines use hyperparameters from their original papers. This creates a potentially substantial comparison advantage.
- The use of 200 labelled validation examples is not fully explained. It is unclear whether these are additional labelled data beyond the 500-example low-resource budget.
- The paper does not provide statistical significance testing or per-seed results for the ablations and label-budget experiments.
- Important implementation details are missing, including the exact back-translation system, synonym-selection procedure, sequence truncation behavior, and whether augmentation resources overlap with evaluation data.

The main empirical claims are credible in principle, but the experimental protocol needs clarification and stronger controls.

### Novelty: 55/100
The central idea—gradually increasing augmentation difficulty during contrastive intermediate training—is reasonable but relatively incremental. Curriculum learning and augmentation scheduling are established ideas, and the contribution mainly consists of applying them to a CERT-like text contrastive-training pipeline. The paper would need stronger positioning against related scheduled-augmentation and curriculum methods, as well as more extensive ablations, to establish substantial novelty.

### Significance: 58/100
The problem is practically important, and the reported gains over CERT and standard fine-tuning are potentially useful, especially in the 100-label setting. Nevertheless, the improvements are modest, and the evidence is limited to four short English classification datasets and one encoder architecture. The lack of comparisons with stronger or more carefully tuned modern baselines limits the broader significance of the conclusions.

### Clarity: 76/100
The paper is generally well organized and easy to follow. The motivation, training pipeline, and headline results are presented clearly. However, the curriculum definition is underspecified, particularly how operator probabilities evolve, and the \(L=0\) case is mathematically inconsistent. The experimental-data split and baseline-tuning protocol also require clearer explanation.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 58 |
| Novelty | 55 |
| Significance | 58 |
| Clarity | 76 |
| **Final average** | **61.75/100** |

## Final recommendation: **Reject**

The idea is plausible and the presentation is reasonably clear, but the current evaluation does not establish the claimed contribution reliably enough. A revised version should clarify the schedule, correct the \(L=0\) formulation, use comparable hyperparameter tuning for all methods, document the labelled-data protocol, and add stronger baselines and statistical validation.