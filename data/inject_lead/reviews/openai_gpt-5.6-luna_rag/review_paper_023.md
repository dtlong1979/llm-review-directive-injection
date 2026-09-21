## Overall assessment

CurCon presents a clear and plausible extension of contrastive intermediate training for low-resource text classification. The central idea—progressively increasing augmentation difficulty during contrastive adaptation—is intuitive, easy to implement, and supported by consistent improvements across the four reported benchmarks. The empirical results are encouraging, particularly in the 100-example setting, and the ablations provide useful evidence that the curriculum contributes beyond the choice of augmentations alone.

The paper is suitable for acceptance, although several methodological and reporting details should be strengthened in a revision.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 82/100 |
| Novelty | 74/100 |
| Significance | 76/100 |
| Clarity | 85/100 |
| **Final average** | **79.25/100** |

## Strengths

1. **Well-motivated method.** The connection between augmentation difficulty and curriculum learning is natural and relevant to contrastive representation learning.
2. **Consistent empirical gains.** CurCon outperforms all listed baselines on each of the four datasets, with a 1.1-point average improvement over CERT.
3. **Useful low-resource analysis.** The results with 100, 500, and 1,000 labels support the claim that the method is most beneficial when supervision is especially limited.
4. **Ablation support.** The fixed-mixture and reversed-curriculum comparisons provide evidence that the schedule itself, rather than only the augmentation inventory, contributes to performance.
5. **Practicality.** The method adds no inference-time parameters and requires only a modification to the intermediate training stage.
6. **Clear presentation.** The paper is generally easy to follow, and the training pipeline and main experimental setup are described concisely.

## Main issues and suggestions

### 1. Clarify the exact curriculum schedule

The paper describes the method as increasing augmentation strength “linearly,” but the implementation uses thresholded operator availability: synonym replacement, span deletion, and back-translation become available at fixed curriculum thresholds and are then sampled uniformly. This is more accurately a staged or piecewise curriculum than a linearly increasing augmentation probability.

Please specify precisely:

- How the operator probabilities vary at every step.
- Whether token dropout remains equally likely after the other operators become available.
- Whether the two views are sampled independently.
- How the \(L=0\) case is implemented, since \(c(t)=t/L\) is undefined when \(L=0\).

A small schedule diagram or an explicit probability equation would improve reproducibility.

### 2. Strengthen statistical reporting

The reported standard deviations over five seeds are useful, but the paper does not report confidence intervals or significance tests. Since the average improvement over CERT is 1.1 points, it would be helpful to include paired per-seed results, confidence intervals, or an appropriate statistical test across seeds and datasets. This is especially important for the smaller gains in the 1,000-label setting.

### 3. Address baseline tuning fairness

CurCon is tuned with a grid search on each validation set, whereas the baselines use hyperparameters reported in their original papers. This may give CurCon an advantage, particularly because the datasets and low-resource sampling scheme differ from the original settings.

The evaluation would be stronger if the authors either:

- tuned all methods under the same budget,
- reported sensitivity analyses for the main baselines, or
- clearly justified why the original hyperparameters are appropriate for this exact setup.

The paper should also state whether the same labelled subset and validation split are used across methods and seeds.

### 4. Provide more implementation detail

Several details would help readers reproduce the results:

- BERT checkpoint and tokenizer version.
- Learning rates and temperature values selected for CurCon.
- Optimizer schedules, warm-up, and weight decay.
- Maximum sequence length and handling of truncated examples.
- The exact back-translation model and decoding settings.
- The synonym-selection procedure and handling of unavailable WordNet entries.
- Whether augmentation results are cached and how much preprocessing storage is required.
- The criterion and patience used for early stopping.

The cost discussion is useful, but the apparent tension between precomputed back-translation and the reported 12% runtime overhead should be clarified.

### 5. Expand the ablation analysis

The ablations establish that the curriculum helps, but additional controls would make the causal interpretation more convincing. In particular, it would be useful to compare:

- CurCon against a fixed mixture with matched augmentation exposure over training.
- Alternative schedules such as cosine, piecewise, or randomly ordered schedules.
- Curricula that vary only the ordering while keeping the per-operator frequency identical.
- Different curriculum lengths \(L\), rather than only the full and reversed schedules.

These experiments are not essential for acceptance, but they would better distinguish the benefit of scheduling from differences in augmentation frequency.

### 6. Moderate the generality of the claims

The experiments cover four English datasets with relatively short texts and one encoder family. The limitations section appropriately acknowledges this. Claims about broad applicability should therefore remain appropriately qualified. In particular, the effectiveness of WordNet substitution and German back-translation may depend substantially on language, domain, and sentence length.

## Minor comments

- Cite the specific versions or sources for UDA, CERT, and SimCSE implementations.
- State whether the unlabelled pool includes the examples used in the labelled subset, with those labels simply ignored.
- Report per-dataset results for the label-count experiment if space permits; averages can conceal dataset-specific behavior.
- Explain why the validation set contains 200 labelled examples in a nominally 500-label setting and whether these labels are counted in the stated annotation budget.
- Consider reporting computational cost in GPU-hours, not only relative runtime.

## Final recommendation

**Accept**

The paper makes a coherent and practically relevant contribution, and the experiments provide consistent evidence that curriculum scheduling improves contrastive intermediate training in low-resource classification. The remaining issues primarily concern reproducibility, statistical validation, and fairer baseline tuning rather than a fundamental flaw in the proposed method.