## Review

### Summary

This paper proposes CurCon, an intermediate contrastive-training method that gradually increases the strength of text augmentations before low-resource fine-tuning. The idea is simple and potentially useful: begin with token dropout, then introduce synonym replacement, span deletion, and back-translation according to a curriculum. Experiments on four classification benchmarks with 500 labelled examples report consistent improvements over fine-tuning, UDA, SimCSE, and CERT.

The paper is clearly written and the empirical results are encouraging. However, several aspects of the experimental design and methodological description limit confidence in the conclusions, particularly the fairness of baseline comparisons, the absence of statistical testing for the main gains, and insufficient detail about data splits and augmentation implementation.

### Strengths

1. **Relevant problem setting.** Low-resource classification with unlabelled in-domain data is practically important.
2. **Simple and implementable method.** The curriculum can be added to an existing contrastive-training pipeline without inference-time cost or architectural changes.
3. **Consistent reported improvements.** CurCon outperforms CERT on all four datasets, with the largest gains in the lower-label setting.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that the schedule, rather than only the augmentation set, may be beneficial.
5. **Clear presentation.** The paper is well organized, and the central method is easy to understand.

### Main concerns

#### 1. Baseline tuning is not sufficiently fair

CurCon is selected using a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters reported in their original papers. This gives the proposed method a potentially substantial tuning advantage, especially in a low-resource setting where learning-rate, temperature, batch-size, and training-duration choices can materially affect performance.

All methods should receive comparable tuning budgets, or the paper should report both published-default and independently tuned baselines. In particular, CERT is the closest comparator and should be reimplemented and tuned under the same data and compute conditions.

#### 2. The statistical evidence is incomplete

The main table reports standard deviations over five seeds, but no confidence intervals or paired significance tests are provided. Several improvements are modest relative to the variability, especially on AG News and TREC. The paper should report per-seed results and use paired tests across identical seeds and splits. The ablation table reports only means, making it difficult to determine whether the claimed 0.8-point curriculum contribution is robust.

The label-count experiment also needs uncertainty estimates and clarification about whether the same sampled splits are used across methods.

#### 3. The protocol and data construction require more detail

The phrase “remaining training sentences without labels” is ambiguous. The paper should specify:

- whether all original training examples, including the 500 labelled examples, are available during contrastive training;
- whether validation examples are excluded from intermediate training;
- how the 200-example validation sets are sampled;
- whether each seed uses a different labelled subset;
- whether test data or test-derived resources enter augmentation or hyperparameter selection.

These details are essential for reproducibility and for ruling out inadvertent leakage.

#### 4. The curriculum is only partially characterized

The schedule changes operator availability at thresholds, but the actual augmentation distribution over time is not fully specified. Since available operators are sampled uniformly, adding a new operator changes the probability of token dropout and all previously available operators. Thus, the method changes both difficulty and the augmentation mixture. A stronger analysis would separately test:

- a schedule that increases augmentation magnitude while holding operator probabilities fixed;
- a schedule that changes operator probabilities but not strength;
- a curriculum with smoothly varying probabilities rather than abrupt thresholds.

This would better establish that progressive difficulty, rather than a particular mixture of augmentations, is responsible for the gains.

#### 5. Reproducibility details are missing

Important implementation choices are underspecified, including the exact BERT checkpoint, tokenizer and maximum sequence length, projection-head dimensions, temperature range, optimizer settings, number of epochs or stopping criteria for contrastive training, back-translation model, treatment of failed or unchanged WordNet replacements, and whether two views independently sample operators. These choices may have a meaningful effect on the results.

#### 6. Novelty is incremental

The core contribution is a curriculum over augmentation strength in contrastive intermediate training. This is a reasonable and potentially effective extension, but it is conceptually close to existing curriculum-learning and augmentation-scheduling ideas. The paper would benefit from a more comprehensive comparison to related augmentation-scheduling methods and from a clearer distinction between CurCon and simply using a time-varying augmentation mixture.

### Minor comments

- The paper should report dataset sizes and class distributions after sampling.
- The motivation would be stronger with an analysis of representation quality or alignment/uniformity, rather than classification accuracy alone.
- The claim that CurCon adds no inference cost is correct, but training cost should be reported for all baselines under the same hardware and preprocessing assumptions.
- The discussion should acknowledge that back-translation and WordNet introduce resource-dependent language and domain biases.
- It would be useful to report results for more than one curriculum length and to show sensitivity curves rather than only selecting the best value.

## Scores

| Criterion | Score (0–100) |
|---|---:|
| Soundness | 58 |
| Novelty | 62 |
| Significance | 60 |
| Clarity | 78 |

**Final average:** \((58 + 62 + 60 + 78) / 4 = 64.5\)

## Final recommendation: Reject

The paper presents a clear and plausible method with encouraging results, but the current evidence is not sufficiently rigorous to support the main claims. In particular, unequal baseline tuning, limited statistical analysis, incomplete protocol details, and confounding between curriculum difficulty and augmentation-mixture changes substantially weaken the evaluation. A revised version addressing these issues could become a useful contribution.