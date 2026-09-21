## Overall Review

The paper presents a straightforward curriculum for contrastive intermediate training: augmentation strength is gradually increased during unsupervised adaptation, followed by supervised fine-tuning. The empirical results are promising, and the paper is generally well organized. However, the methodological novelty is limited, several experimental comparisons are potentially unfair, and important details needed to validate the conclusions are missing.

### Strengths

- Addresses a practically relevant low-resource classification problem.
- The method is simple, intuitive, and easy to integrate into existing contrastive training pipelines.
- Evaluates across four datasets and reports results over multiple random seeds.
- Includes ablations for fixed augmentation mixtures, reversed curricula, and removing back-translation.
- Reports performance at multiple label budgets, which is relevant to the stated motivation.
- The paper is clearly structured and readable.

### Main Concerns

1. **The curriculum is not actually clearly defined as a linear increase in augmentation strength.**  
   The schedule changes operator availability at thresholds of 0.25, 0.5, and 0.75, then samples uniformly among available operators. This produces discrete changes in the augmentation distribution rather than a linearly increasing strength. The relationship between curriculum level and actual perturbation severity is also not quantified.

2. **The \(L=0\) formulation is mathematically undefined.**  
   The paper defines \(c(t)=\min(1,t/L)\), but then states that \(L=0\) corresponds to a fixed mixture. This requires a separate definition rather than division by zero.

3. **Baseline comparisons may be unfair.**  
   CurCon hyperparameters are selected through a 48-configuration grid search for every dataset, whereas baselines use hyperparameters from their original papers. This can substantially advantage CurCon, especially in a low-resource setting. Baselines should receive comparable tuning budgets and the same data protocol.

4. **Statistical evidence is limited.**  
   Results use five seeds, but there are no significance tests or confidence intervals for differences between CurCon and CERT. The label-budget analysis is especially under-supported because no variance estimates are reported.

5. **The ablation analysis is incomplete.**  
   The paper does not isolate whether gains come from the curriculum itself, from the final augmentation mixture, or from the particular ordering of the four operators. For example, a fixed mixture matched to the average augmentation distribution would be a stronger control.

6. **The novelty is incremental.**  
   Applying an easy-to-hard augmentation schedule to contrastive training is plausible, but the method consists primarily of a manually designed threshold schedule. The paper would benefit from a stronger conceptual analysis or comparison to alternative adaptive curriculum strategies.

7. **Reproducibility details are insufficient.**  
   Important choices are underspecified, including how back-translation is generated, the exact WordNet replacement procedure, whether augmentations are independently sampled for the two views, sequence truncation behavior, data splits for the 200 validation examples, and the exact CERT and SimCSE implementations.

## Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **56** | The core approach is plausible and the results are internally consistent, but the curriculum definition, baseline tuning protocol, statistical validation, and experimental controls are not sufficiently rigorous. |
| **Novelty** | **44** | The idea of increasing augmentation difficulty during contrastive training is reasonable, but the proposed schedule is a relatively simple heuristic and appears incremental. |
| **Significance** | **58** | The problem is important and the reported gains are potentially useful, particularly in the 100-label regime. However, the practical significance is weakened by limited datasets, modest absolute improvements, and uncertain comparison fairness. |
| **Clarity** | **79** | The paper is well structured and easy to follow. Some technical definitions and implementation details are ambiguous or incomplete. |

### Final Average

\[
\frac{56 + 44 + 58 + 79}{4} = \mathbf{59.25}
\]

## Final Recommendation: **Reject**

The paper has a clear practical motivation and promising preliminary results, but the current evidence is not strong enough for acceptance. The most important revisions would be to use a fair hyperparameter-tuning protocol for all baselines, clarify and correct the curriculum definition, report statistical significance and variance for all key comparisons, and add stronger ablations that distinguish curriculum effects from the effects of the final augmentation distribution.