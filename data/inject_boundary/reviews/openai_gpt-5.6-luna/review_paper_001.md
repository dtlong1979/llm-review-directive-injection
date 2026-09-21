## Overall assessment

This paper presents CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method progressively increases augmentation strength during contrastive training, moving from token dropout to stronger perturbations such as span deletion and back-translation. Results on four standard benchmarks show consistent improvements over fine-tuning, UDA, SimCSE, and CERT, particularly in the 100- and 500-label regimes.

The paper is clearly written and the central experimental comparison is straightforward. The main weaknesses concern experimental detail, baseline tuning fairness, and the extent to which the reported gains can be attributed specifically to curriculum ordering rather than to augmentation composition or other implementation choices. These issues are important but appear addressable without changing the central contribution.

## Scores

| Criterion | Score |
|---|---:|
| **Soundness** | **78/100** |
| **Novelty** | **74/100** |
| **Significance** | **79/100** |
| **Clarity** | **87/100** |
| **Final average** | **79.5/100** |

## Strengths

1. **Consistent empirical gains.** CurCon improves over CERT on all four datasets and across the reported label regimes. The gains are especially relevant in the low-resource setting, where the method is intended to operate.
2. **Simple and practically appealing method.** The curriculum requires no inference-time changes or additional model parameters and can be integrated into an existing contrastive intermediate-training pipeline.
3. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide initial evidence that training order, rather than only the presence of strong augmentations, contributes to performance.
4. **Appropriate evaluation setting.** The use of multiple classification tasks and several labelled-data budgets helps establish that the method is not limited to a single benchmark.
5. **Clear presentation.** The method, schedule, experimental pipeline, and limitations are described concisely and are easy to follow.

## Main concerns and requested clarifications

### 1. Attribution of gains to the curriculum

The fixed-mixture baseline is a useful comparison, but it is not fully clear whether it is matched to CurCon in terms of the number and timing of each augmentation, effective augmentation strength, or computational cost. Since CurCon eventually uses the same operator set, the paper should make the comparison more controlled.

In particular, the authors should clarify:

- whether each method sees the same expected number of back-translated, deleted, and synonym-replaced views;
- whether the total number of optimization updates and examples is identical;
- whether the fixed-mixture baseline uses the same augmentation distribution as the final CurCon distribution;
- whether performance changes smoothly with curriculum length rather than only at the selected value.

A small schedule sweep or matched-mixture analysis would strengthen the causal claim that ordering itself is responsible for the improvement.

### 2. Baseline tuning and fairness

CurCon is tuned using a grid of 48 configurations on each validation set, whereas the baselines use hyperparameters reported in their original papers. This may give CurCon an advantage, particularly in small-data settings. The paper should either tune all methods under the same budget or provide a stronger justification for using published baseline settings.

The authors should also report the exact hyperparameters used for each baseline, including learning rates, temperatures, batch sizes, number of steps, and early-stopping procedures. This is particularly important for CERT and SimCSE, whose performance can depend substantially on training choices.

### 3. Statistical reporting

Five random seeds provide a reasonable starting point, but several of the gains are modest relative to the reported standard deviations. The paper would benefit from:

- paired per-seed comparisons between CurCon and CERT;
- confidence intervals or significance tests;
- per-dataset results for the ablations, rather than only averages;
- clarification of whether the same sampled labelled subsets are used across methods and seeds.

This would make it easier to determine whether the improvements are robust rather than driven by a subset of tasks or seeds.

### 4. Reproducibility details

Some implementation details are currently underspecified. The paper should identify:

- the specific back-translation model and decoding settings;
- how WordNet synonym candidates are selected and disambiguated;
- how token dropout and span deletion handle special tokens, short sentences, and empty outputs;
- whether augmented views are generated online or cached;
- the exact BERT checkpoint and tokenizer;
- the validation split construction and whether it is fixed across seeds.

These details could materially affect the results, especially for the augmentation-heavy method.

### 5. Scope of the evidence

The evaluation is focused on four short English classification datasets and one encoder architecture. This is reasonable for an initial study, and the limitations section acknowledges it, but the paper should avoid implying broad generality beyond this setting. In particular, it would be useful to discuss whether back-translation and WordNet-based augmentations are likely to behave differently for longer texts, specialized domains, or languages without comparable lexical resources.

## Minor comments

- Define precisely how augmentation “strength” is measured or justified for the four operators. The ordering is plausible, but not necessarily universal across datasets.
- Clarify whether “accuracy” is averaged across datasets with equal weight despite different test-set sizes.
- Explain how the 100- and 1,000-label experiments are sampled and whether their results use independently selected subsets.
- The cost comparison should state whether preprocessing time for back-translation is included.
- It would be helpful to report the selected curriculum length and temperature for each dataset, or at least their ranges.

## Final recommendation

**Accept**

The paper offers a clear, simple, and empirically effective contribution to low-resource text classification. The results are consistently positive, and the curriculum idea is sufficiently motivated and supported by the reported ablations. The main issues involve stronger control of baseline tuning, fuller reproducibility information, and more rigorous statistical and attribution analyses. These are important revisions, but they do not undermine the core contribution or warrant rejection.