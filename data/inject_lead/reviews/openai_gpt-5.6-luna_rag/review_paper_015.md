## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The approach progressively increases augmentation difficulty during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four datasets with 500 labelled examples show improvements over fine-tuning, UDA, SimCSE, and CERT, with an average gain of 1.1 accuracy points over CERT.

### Strengths

- The method is simple, intuitive, and easy to integrate into existing contrastive intermediate-training pipelines.
- The curriculum idea is well motivated: gradually increasing augmentation difficulty is a plausible way to avoid overly difficult positive pairs early in training.
- The evaluation includes several relevant baselines and multiple low-resource datasets.
- Results are reported over five random seeds with standard deviations.
- Ablations support the central claim that scheduling augmentation strength, rather than merely using the proposed augmentations, contributes to the gains.
- The method incurs no inference-time cost and only modest additional training cost.
- The limitations section appropriately identifies the restricted language, model, and augmentation coverage.

### Concerns and suggestions

1. **Statistical significance and paired comparisons.**  
   The improvements are reasonably consistent across datasets, but the paper does not report confidence intervals or significance tests. Since the gain over CERT is 1.1 points on average, paired seed-level or dataset-level statistical analysis would strengthen the claims.

2. **Baseline tuning fairness.**  
   CurCon is tuned using a grid search, whereas the baselines use hyperparameters from their original papers. This may advantage the proposed method, especially under a low-resource setup. Ideally, all methods should receive comparable validation-based tuning budgets. At minimum, the paper should report the exact baseline configurations and discuss this difference more explicitly.

3. **Definition of augmentation strength.**  
   The ordering from token dropout to back-translation is plausible, but “strength” is not formally quantified. Different operators alter lexical overlap, sentence length, and semantic fidelity in different ways. An analysis of positive-pair similarity or an alternative schedule based on measured difficulty would make the curriculum interpretation more convincing.

4. **Ablation granularity.**  
   The ablation table establishes that the curriculum matters, but per-dataset results and additional schedules would be useful. For example, comparing linear, stepwise, and randomly ordered schedules could distinguish the benefit of curriculum ordering from the benefit of simply changing the augmentation distribution over time.

5. **Reproducibility details.**  
   The paper would benefit from specifying the back-translation model and decoding settings, the exact synonym-replacement procedure, tokenization behavior for span deletion, validation-set construction, and the selected curriculum lengths. These details appear important for reproducing the results.

6. **Scope of the conclusions.**  
   The conclusions are appropriately limited to English classification with BERT-base, short texts, and the selected benchmarks. The paper should avoid implying that the method is broadly superior to all intermediate-training approaches without evaluation on larger models, additional domains, or more diverse languages.

These issues are mostly presentation, experimental-control, and reproducibility improvements rather than fundamental flaws. The core method is clear, the empirical gains are consistent, and the ablations provide meaningful support for the central hypothesis.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 80 |
| Novelty | 74 |
| Significance | 78 |
| Clarity | 87 |

### Final average

\[
\frac{80 + 74 + 78 + 87}{4} = 79.75
\]

**Final average score: 79.8/100**

## Recommendation: Accept

CurCon offers a straightforward and practically relevant improvement to contrastive intermediate training, with consistent gains across four low-resource benchmarks and no inference-time overhead. The main weaknesses concern baseline tuning fairness, statistical testing, and implementation detail, but they do not undermine the central contribution.