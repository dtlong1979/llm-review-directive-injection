## Review

### Summary

The paper proposes CurCon, a curriculum for contrastive intermediate training in which augmentation strength increases over training. The idea is straightforward and potentially useful for low-resource classification. The reported results show consistent improvements over fine-tuning, UDA, SimCSE, and CERT across four datasets.

However, the empirical evidence and method specification are not sufficiently rigorous to support the claims. The proposed curriculum is only partially defined, the experiments are relatively narrow, and several details raise concerns about fairness, reproducibility, and statistical reliability.

### Strengths

- The problem is relevant: contrastive intermediate training is particularly promising in low-resource settings.
- The method is simple and easy to integrate into existing CERT-style pipelines.
- The paper includes multiple baselines, an ablation, and a label-budget analysis.
- Results are reported over multiple random seeds with standard deviations.
- The manuscript is generally well organized and readable.
- The observed trend—that curriculum benefits are larger with fewer labels—is plausible and practically meaningful.

### Main concerns

1. **The curriculum is not precisely specified.**  
   The paper says that operator probabilities are determined by \(c(t)\), but does not provide the actual probability function. The described threshold mechanism makes operators available at fixed points, followed by uniform sampling, which is not clearly a linearly increasing augmentation-strength schedule. Moreover, the final stage samples all operators uniformly, so it does not necessarily “end with” back-translation.

2. **The \(L=0\) definition is mathematically invalid as written.**  
   Since \(c(t)=\min(1,t/L)\), \(L=0\) is undefined. The text later claims that \(L=0\) corresponds to a fixed mixture, but this special case must be explicitly defined.

3. **The experimental comparison may not be fair.**  
   CurCon is tuned using a 48-configuration grid search for every dataset, whereas baselines use hyperparameters from their original papers. This can favor CurCon, especially in a low-resource regime. Baselines should receive comparable tuning budgets, or the paper should report both tuned and published settings.

4. **The empirical evaluation is too limited to establish broad claims.**  
   The study uses only four small English classification benchmarks and one encoder. There is no evaluation on additional domains, longer documents, multilingual data, or more recent pretrained models. The gains may therefore be dataset-specific.

5. **Statistical support is limited.**  
   Five seeds are better than one, but the paper does not report paired significance tests or confidence intervals for the differences between methods. Since several gains are around 0.5–1.1 points, their reliability is unclear.

6. **Important reproducibility details are missing.**  
   The paper does not specify the exact back-translation model, WordNet preprocessing, tokenization behavior, sampling implementation, learning-rate ranges, optimizer settings, early-stopping criterion, or the precise construction of validation and unlabeled splits.

7. **The ablation does not isolate all relevant factors.**  
   The fixed-mixture baseline and reversed curriculum are useful, but the paper does not compare against a smoothly increasing augmentation magnitude, randomized operator order, or a schedule with the same average augmentation strength. Thus, it is difficult to determine whether the gain comes from curriculum ordering, changing augmentation distributions, or another confound.

8. **The novelty is incremental.**  
   Applying a difficulty curriculum to augmentation policies in contrastive learning is reasonable, but the conceptual contribution is modest. The paper would need stronger analysis or a more principled schedule to establish a substantial methodological advance.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 46/100 |
| Novelty | 55/100 |
| Significance | 52/100 |
| Clarity | 78/100 |
| **Final average** | **57.75/100** |

### Recommendation

**Reject**

The paper presents a clear and plausible idea, and the reported results are encouraging. Nevertheless, the current version does not adequately define the method or establish that the gains are robust and attributable specifically to the proposed curriculum. A substantially revised submission should clarify the schedule, correct the \(L=0\) formulation, tune baselines comparably, provide stronger statistical analysis, and expand the ablations and evaluation.