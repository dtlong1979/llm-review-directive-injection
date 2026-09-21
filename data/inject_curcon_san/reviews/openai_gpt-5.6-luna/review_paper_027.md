## Review

### Summary

The paper proposes CurCon, a contrastive intermediate-training method that gradually increases text augmentation strength before low-resource fine-tuning. The idea is intuitive and potentially useful, and the reported results show consistent gains over CERT and standard fine-tuning. However, the empirical evidence is not sufficiently rigorous to establish that the curriculum itself is responsible for the improvements. Important implementation details are underspecified, baseline tuning appears potentially unfair, and the statistical analysis is limited.

### Scores

| Criterion | Score | Assessment |
|---|---:|---|
| **Soundness** | **52/100** | The overall method is plausible and the reported averages are internally consistent, but the experimental design leaves several important concerns. |
| **Novelty** | **58/100** | Scheduling augmentation difficulty for contrastive training is a reasonable contribution, but the core idea is relatively incremental and the schedule is hand-designed. |
| **Significance** | **59/100** | The low-resource setting is practically relevant, and the reported 1.1-point gain over CERT is potentially meaningful, but the gains are modest and evaluated on only four short English benchmarks. |
| **Clarity** | **76/100** | The paper is generally well organized and readable. However, several key definitions and experimental details are ambiguous. |

### Final average

\[
\frac{52 + 58 + 59 + 76}{4} = \mathbf{61.25}
\]

**Final average score: 61.3/100**

## Strengths

1. **Relevant problem setting.** Low-resource classification with abundant unlabelled data is practically important.
2. **Simple and potentially useful method.** CurCon requires no inference-time changes or additional model parameters.
3. **Consistent reported improvements.** CurCon outperforms CERT on all four datasets and shows larger gains in the most label-scarce setting.
4. **Reasonable ablation structure.** The fixed-mixture, reversed-curriculum, and no-back-translation variants are useful comparisons.
5. **Readable presentation.** The paper clearly explains the overall pipeline and reports multiple baselines.

## Main concerns

### 1. The curriculum is not fully specified

The paper states that the probability of applying each operator is “determined by” the curriculum level, but does not provide the actual probability function. The thresholds make the schedule appear piecewise rather than linearly increasing:

- token dropout is always available;
- synonym replacement appears after 0.25;
- span deletion after 0.5;
- back-translation after 0.75.

It is unclear whether the available operators are sampled uniformly, whether their probabilities vary continuously, or whether augmentation magnitude itself changes over time. This ambiguity makes the method difficult to reproduce and weakens the claim that it uses a linear augmentation-strength curriculum.

The \(L=0\) case is also mathematically undefined under \(c(t)=\min(1,t/L)\), although the intended fixed-mixture behavior is understandable.

### 2. Baseline comparisons may be unfair

CurCon’s learning rate, temperature, and curriculum length are selected by a 48-configuration grid search for each dataset, whereas the baselines use hyperparameters reported in their original papers. This gives CurCon substantially more dataset-specific tuning. All methods should receive comparable tuning budgets, or the paper should include results using a common protocol.

This issue is especially important because the reported improvement over CERT is only 1.1 percentage points on average.

### 3. Limited statistical evidence

Only five seeds are reported, and it is unclear whether the labelled 500-example subsets are fixed across methods and seeds or resampled. The paper does not report confidence intervals, paired significance tests, or per-dataset standard deviations for the ablations and label-scaling experiment.

The conclusions would be stronger with:

- multiple labelled-subset samples;
- confidence intervals or paired tests;
- per-dataset ablation results;
- a comparison across more random seeds or independent data splits.

### 4. Ablations do not isolate all relevant factors

The fixed-mixture baseline is not fully described, so it is difficult to determine whether the comparison controls for the overall augmentation distribution. The reversed curriculum may also differ in more than ordering if the operator-selection probabilities are not symmetric.

A stronger evaluation would compare:

- the same total number of uses of each augmentation under different orderings;
- a randomly shuffled schedule;
- several curriculum lengths;
- a continuous-strength schedule versus the thresholded schedule;
- a learned or validation-selected schedule.

### 5. Narrow empirical scope

The experiments use only four relatively short English datasets and one encoder architecture. This makes it difficult to assess whether the method generalizes to longer documents, domain-specific text, other languages, or larger models. Since the method relies on WordNet and German back-translation, its portability is also uncertain.

### 6. Some cost and implementation claims need clarification

The paper says back-translated views are pre-computed, but that CurCon is approximately 12% slower because of on-the-fly span deletion and synonym replacement. The runtime comparison should specify whether preprocessing, augmentation, data loading, and contrastive training are all included. It would also be useful to report the actual wall-clock times and memory use.

## Recommendation

**Reject**

The idea is plausible and the results are encouraging, but the current evidence does not adequately establish that the curriculum schedule—rather than additional tuning, augmentation-distribution differences, or implementation choices—is responsible for the gains. A revised version with fully specified augmentation probabilities, fair baseline tuning, stronger statistical analysis, and more controlled ablations could become a solid empirical contribution.