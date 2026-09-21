## Overall assessment

This paper presents CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The core idea is straightforward: begin contrastive training with weaker augmentations and progressively introduce stronger perturbations. The experiments show consistent improvements over fine-tuning, UDA, SimCSE, and CERT across four datasets, with larger gains in the lower-label regime.

The empirical results are promising and the method is simple and practically motivated. However, several experimental details and fairness issues should be clarified, particularly the hyperparameter tuning protocol, statistical significance of the reported improvements, and the precise definition of the curriculum and reversed-curriculum baselines.

## Scores

| Criterion | Score |
|---|---:|
| **Soundness** | **78/100** |
| **Novelty** | **72/100** |
| **Significance** | **77/100** |
| **Clarity** | **86/100** |
| **Final average** | **78.25/100** |

The final average is computed as:

\[
\frac{78 + 72 + 77 + 86}{4} = 78.25.
\]

## Strengths

### Soundness

- The proposed training pipeline is technically plausible and follows a well-established contrastive intermediate-training framework.
- The comparison includes relevant baselines: direct fine-tuning, UDA, SimCSE, and CERT.
- Results are reported across four datasets and five random seeds, with mean and standard deviation.
- The ablation study directly examines the curriculum, reversed curriculum, and contribution of back-translation.
- The label-efficiency analysis supports the central motivation: CurCon’s relative benefit is larger when fewer labelled examples are available.
- The reported averages are internally consistent with the per-dataset results.

### Novelty

- Applying a progressively stronger augmentation schedule specifically during contrastive intermediate training is a reasonable and useful extension of prior work.
- The paper distinguishes the curriculum from simply using a fixed mixture of augmentations.
- The reversed-curriculum ablation provides evidence that the ordering of augmentation difficulty, rather than only the set of augmentations, matters.

The novelty is moderate rather than fundamental. The method combines existing augmentation operators and curriculum-learning ideas in a new training schedule, but does not introduce a new contrastive objective or augmentation mechanism.

### Significance

- The low-resource setting is practically important.
- Improvements over CERT are consistent across all four datasets, and the gains are particularly relevant in the 100-example condition.
- The method adds no inference-time cost and only modest training overhead.
- The approach is model-agnostic in principle and could likely be integrated into existing intermediate-training pipelines.

### Clarity

- The paper is well organized and easy to follow.
- The method, schedule, datasets, baselines, and results are described in a logical order.
- Tables provide a concise summary of the main claims.
- The limitations section appropriately acknowledges the dependence on English resources and external augmentation systems.

## Main concerns

1. **Unequal hyperparameter tuning protocols.**  
   CurCon is selected using a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters reported in their original papers. This may advantage CurCon, especially in a low-resource setting. Ideally, all methods should receive comparable tuning budgets, or the paper should include a controlled tuning comparison.

2. **Insufficient statistical analysis.**  
   Five random seeds are useful, but the paper does not report confidence intervals, paired significance tests, or per-seed comparisons. Since the gains over CERT are relatively small on some datasets, statistical testing would strengthen the conclusions.

3. **Curriculum specification is somewhat ambiguous.**  
   The text states that operator probabilities are determined by the curriculum level, but it does not fully specify whether token dropout remains equally likely after additional operators become available, whether probabilities are renormalized, or whether augmentation strength itself changes continuously. The precise implementation should be stated mathematically or in pseudocode.

4. **Limited ablation detail.**  
   The ablation table reports only average accuracy. Per-dataset ablations would reveal whether the curriculum helps uniformly or whether the improvements are concentrated in particular tasks. It would also be useful to compare schedules with the same average augmentation strength.

5. **Potential fairness and reproducibility issues.**  
   Important implementation details are missing, including the exact back-translation model, synonym-selection procedure, projection-head dimensions, maximum sequence length, data preprocessing, and the construction of the 200-example validation sets. These details can materially affect low-resource results.

6. **Scope of evaluation.**  
   The experiments cover only four English, relatively short-text classification datasets and one encoder size. Additional domains or encoders would make the claims more general, although this is not essential for the central contribution.

7. **Interpretation of the curriculum effect.**  
   The fixed-mixture baseline is weaker than CurCon, but the current design does not completely isolate curriculum ordering from changes in the augmentation distribution over time. A stronger control would match the total frequency of each augmentation over training while varying only their temporal order.

## Recommendation

**Accept**

The paper provides a clear, empirically supported, and practically useful improvement to contrastive intermediate training. The contribution is incremental but well motivated, and the consistent gains across datasets and label regimes support publication. The main weaknesses concern experimental rigor and reporting rather than a fundamental flaw in the method. I recommend acceptance conditional on clarifying the augmentation probabilities, improving the fairness of baseline tuning, and adding statistical or per-seed analyses where possible.