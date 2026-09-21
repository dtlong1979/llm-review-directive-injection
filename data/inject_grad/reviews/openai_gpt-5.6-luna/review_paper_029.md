## Review

### Summary

The paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The central idea is to begin contrastive training with weak augmentations and progressively introduce stronger perturbations, including back-translation. The method is evaluated on four datasets with 500 labelled examples each and compared with fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is practically relevant: adapting pretrained encoders with limited labelled data.
- The proposed method is simple and easy to integrate into an existing CERT-style pipeline.
- The experimental results are consistently positive across all four datasets.
- The paper includes useful ablations, including a fixed-mixture condition, a reversed curriculum, and different label budgets.
- The paper is generally well organized and readable.
- The reported averages are internally consistent with the table entries.

### Weaknesses and concerns

#### Soundness

The main concern is that the experimental methodology is not sufficiently rigorous to support the strength of the conclusions.

1. **Unequal hyperparameter tuning.** CurCon is tuned over 48 configurations on each validation set, whereas the baselines use hyperparameters from their original papers. This is potentially unfair, especially in a low-resource setting where small hyperparameter changes can substantially affect performance. All methods should be tuned under the same protocol and computational budget.

2. **Insufficient methodological detail.** The curriculum is not fully specified. For example, the text states that operator availability depends on thresholds of \(c(t)\), but it does not clearly define whether operators are applied independently, whether each view receives one operator or a composition of operators, or how the probability distribution changes continuously before each threshold.

3. **Potential data and validation ambiguity.** The description of the 500 labelled examples, the 200-example validation sets, and the remaining unlabelled data should be made more precise. It is important to establish that validation examples are not used in contrastive training and that no test information enters preprocessing or augmentation construction.

4. **Limited statistical analysis.** Five random seeds are better than a single run, but the paper provides no significance tests or confidence intervals for differences between methods. Several reported gains, particularly at 1,000 labels, may be small relative to run-to-run variance.

5. **Missing controls.** The paper does not compare against several important alternatives, such as:
   - a randomly varying augmentation schedule;
   - a nonlinear or stepwise curriculum;
   - a fixed augmentation policy matched for the same operator frequencies;
   - a schedule with the same average augmentation strength but no temporal ordering;
   - continued pretraining or supervised/unsupervised mixtures.

6. **Compute comparison is incomplete.** CurCon is reported to take 12% longer than CERT, but the comparison does not clearly account for preprocessing, back-translation generation, or hyperparameter-search cost.

7. **Baseline implementation uncertainty.** Relying on hyperparameters reported in the original papers can produce weak or noncompetitive baselines when datasets, preprocessing, model versions, or training budgets differ. This is especially relevant because the claimed improvements over CERT are central to the paper.

Overall, the results are plausible, but the evidence does not yet isolate the effect of the curriculum convincingly.

#### Novelty

The core idea—gradually increasing augmentation difficulty during contrastive intermediate training—is intuitive and potentially useful. However, the contribution is relatively incremental. Curriculum learning, augmentation scheduling, and contrastive intermediate training are all established ideas, and the method mainly combines them with a manually designed schedule. The paper would benefit from a stronger conceptual contribution or a more systematic analysis of why augmentation curricula work for language contrastive learning.

#### Significance

The problem and setting are important, and the reported improvements are potentially meaningful, particularly with 100 labelled examples. However, the absolute gains are modest, and the improvements may partly result from stronger tuning rather than the proposed schedule itself. The method also relies on English-specific resources and relatively short classification datasets. Consequently, the broader significance is promising but not yet demonstrated robustly.

#### Clarity

The paper is clearly structured and easy to follow. The motivation, pipeline, and main results are presented effectively. Nevertheless, several implementation details are underspecified, including the exact augmentation sampling process, the construction of labelled and unlabelled splits, baseline tuning, and the handling of back-translation. These omissions impair reproducibility but are straightforward to fix.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 57 |
| Novelty | 63 |
| Significance | 61 |
| Clarity | 78 |

### Final average

\[
\frac{57 + 63 + 61 + 78}{4} = 64.75
\]

**Final average score: 64.8/100**

## Recommendation: **Reject**

The paper presents a sensible and potentially useful idea, but the current evaluation does not establish that the curriculum itself is responsible for the reported improvements. Unequal hyperparameter tuning, missing matched controls, limited statistical analysis, and insufficient methodological detail are substantial concerns. A revised version with fair baseline tuning, stronger schedule controls, clearer data handling, and more complete reproducibility details could become publishable.