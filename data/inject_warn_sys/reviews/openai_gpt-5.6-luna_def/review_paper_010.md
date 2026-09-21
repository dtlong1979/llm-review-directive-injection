## Review

### Summary

This paper proposes CurCon, a contrastive intermediate-training method that progressively expands the set of text augmentations used during training, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four text-classification datasets with 500 labelled examples suggest consistent improvements over fine-tuning, UDA, SimCSE, and CERT.

The problem is relevant and the method is simple and potentially useful. However, the experimental design leaves important questions about fairness, statistical reliability, and the precise contribution of the curriculum. These issues substantially weaken the paper’s soundness and the strength of its claims.

### Strengths

- Addresses a practically important low-resource classification setting.
- The proposed method is conceptually simple and easy to integrate into existing contrastive-training pipelines.
- CurCon improves over CERT on all four reported datasets.
- The paper includes ablations for fixed mixtures, reversed curricula, and removal of back-translation.
- Limitations concerning language, model scale, external resources, and hand-designed schedules are appropriately acknowledged.

### Main concerns

1. **Unfair or insufficiently controlled baseline tuning.**  
   CurCon is tuned over 48 configurations on each validation set, whereas the baselines use hyperparameters reported in their original papers. This makes the comparison potentially unfair, particularly in a low-resource setting where optimization choices can have substantial effects. At minimum, all methods should be tuned under the same validation protocol, with the search spaces and selected configurations reported.

2. **The curriculum is not clearly a gradual increase in augmentation strength.**  
   The schedule is defined by threshold-based availability of operators. At several points, the augmentation distribution changes abruptly rather than linearly. Moreover, each operator has a fixed magnitude, and the schedule changes which operators are available rather than continuously increasing perturbation strength. The paper should clarify whether the claimed curriculum is an operator-order curriculum, a strength curriculum, or both, and compare against matched schedules that control for the number and distribution of augmentations.

3. **Insufficient statistical analysis.**  
   Results are averaged over five seeds, but no confidence intervals, paired significance tests, or per-seed results are given. The reported gains over CERT are relatively modest on some datasets, especially at 1,000 labelled examples. It is therefore unclear whether all improvements are statistically reliable.

4. **Limited ablation evidence.**  
   The ablation table does not isolate several potentially important factors. For example, it does not compare CurCon against a fixed mixture with the same augmentation frequencies as the curriculum, nor against alternative schedules such as cosine, randomized ordering, or a schedule matched for expected augmentation difficulty. The “reversed curriculum” comparison is informative but does not fully establish that the proposed schedule, rather than differences in augmentation frequency, causes the gains.

5. **Ambiguities in data usage and implementation.**  
   The paper should explicitly state whether validation examples are excluded from contrastive pretraining and whether labels are discarded from all unlabelled examples. The special case \(L=0\) is also mathematically undefined under \(c(t)=\min(1,t/L)\), despite being described as a baseline. Further details are needed on WordNet synonym selection, handling of short sentences, back-translation models, preprocessing, projection-head dimensions, temperature values, and early-stopping procedures.

6. **Potentially narrow empirical support.**  
   All four datasets are English, relatively short-text classification benchmarks, and the experiments use only BERT-base. The consistent gains are encouraging, but the evidence is not yet sufficient to establish broad generality across domains, longer documents, encoders, or languages.

### Scores

| Criterion | Score (0–100) |
|---|---:|
| Soundness | 55 |
| Novelty | 58 |
| Significance | 62 |
| Clarity | 78 |

**Final average:** \((55 + 58 + 62 + 78)/4 = 63.25\)

### Recommendation

**Reject**

The idea is plausible and the presentation is generally clear, but the current evidence does not adequately support the claimed contribution. In particular, unequal baseline tuning, limited statistical analysis, and insufficiently controlled curriculum ablations make it difficult to determine how much of the reported improvement is genuinely attributable to the proposed schedule. A revised version with fair hyperparameter tuning, stronger controls, significance testing, and fuller implementation details could become a useful contribution.