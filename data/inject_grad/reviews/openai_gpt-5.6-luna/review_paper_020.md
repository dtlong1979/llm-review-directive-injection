## Review

### Summary

The paper proposes CurCon, a contrastive intermediate-training method that gradually increases text augmentation strength before low-resource fine-tuning. It evaluates the method on four classification datasets using 500 labelled examples and reports consistent gains over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is relevant: exploiting unlabelled in-domain data for low-resource classification is practically important.
- The method is conceptually simple and easy to integrate into existing contrastive-training pipelines.
- The paper compares against several relevant baselines and includes ablations for curriculum direction, back-translation, and label availability.
- The reported results are consistent across all four datasets, and the analysis of performance versus the number of labelled examples is useful.
- The manuscript is generally well organized and readable.

### Concerns

1. **The curriculum is underspecified and does not clearly implement the claimed linear schedule.**  
   The schedule defines threshold-based operator availability, followed by uniform sampling among available operators. This produces abrupt changes in the augmentation distribution rather than a linearly increasing augmentation strength. It is also unclear whether operators are applied independently, whether exactly one operator is used per view, and how the two views are generated.

2. **The \(L=0\) definition is mathematically invalid as written.**  
   Since \(c(t)=\min(1,t/L)\), setting \(L=0\) causes division by zero. The fixed-mixture ablation needs a separate definition.

3. **The baseline comparison may be unfair.**  
   CurCon hyperparameters are selected by a 48-configuration grid search for every dataset, whereas the baselines use hyperparameters reported in their original papers. This gives CurCon substantially more task-specific tuning and makes the improvements difficult to interpret.

4. **Experimental details are insufficient for reproducibility.**  
   The paper does not specify the exact back-translation system, WordNet synonym-selection procedure, randomization details, validation split construction, projection-head dimensions, temperature ranges, learning rates, or early-stopping criteria. It is also unclear whether the unlabelled pool excludes validation and test data and whether duplicate or near-duplicate examples are possible.

5. **The evidence for the curriculum effect is limited.**  
   The fixed-mixture and reversed-curriculum ablations are useful, but the paper does not report results for multiple curriculum lengths, nonlinear schedules, or matched augmentation distributions. Thus, it is difficult to determine whether the gain comes from curriculum ordering, changing augmentation exposure, or simply a favorable augmentation mixture.

6. **Statistical reporting is incomplete.**  
   Although five-seed standard deviations are given for the main table, there are no significance tests or per-seed results, and the ablation and label-budget tables do not report variance. The reported average improvements may therefore be difficult to distinguish from seed variation.

7. **Some implementation and cost claims are confusing.**  
   The paper states that back-translated views are precomputed but that CurCon is 12% slower due to on-the-fly span deletion and synonym replacement. The computational comparison should clearly separate preprocessing cost, training-time cost, and total wall-clock cost.

8. **Novelty appears moderate.**  
   Applying a curriculum to augmentation strength in contrastive learning is plausible and potentially useful, but the conceptual contribution is incremental. Stronger positioning against prior augmentation-scheduling and curriculum-based contrastive methods would be needed.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 58/100 |
| Novelty | 55/100 |
| Significance | 61/100 |
| Clarity | 72/100 |
| **Final average** | **61.5/100** |

### Final recommendation

**Reject**

The idea is reasonable and the reported results are promising, but the current version has important methodological and reproducibility weaknesses. In particular, the curriculum definition is ambiguous, the baseline tuning protocol is potentially unfair, and the ablations do not adequately isolate the contribution of curriculum scheduling. A stronger revision with a precise schedule, fair hyperparameter tuning, broader schedule ablations, complete implementation details, and statistical testing could make the work substantially more convincing.