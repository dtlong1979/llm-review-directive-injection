## Review

### Summary

This paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The approach progressively expands the augmentation pool from token dropout to synonym replacement, span deletion, and back-translation during contrastive training. It is evaluated on four English classification datasets with 500 labelled examples per dataset and compared against fine-tuning, UDA, SimCSE, and CERT. CurCon improves average accuracy from 87.8 with CERT to 88.9, with larger gains in the more severely low-resource setting.

### Strengths

1. **Clear practical motivation.** Improving text classification with only a few hundred labelled examples is important and well motivated.
2. **Simple and implementable method.** CurCon requires no architectural changes or inference-time overhead and can be incorporated into an existing CERT-style pipeline.
3. **Relevant comparisons.** The paper includes strong and appropriate baselines, including direct fine-tuning, UDA, SimCSE, and CERT.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that the schedule, rather than only the augmentation set, contributes to performance.
5. **Low-resource analysis.** Results at 100, 500, and 1,000 labelled examples support the claim that the method is most useful when labels are scarce.
6. **Good presentation.** The paper is generally well organized, readable, and clear about the training pipeline and experimental setting.

### Concerns

1. **The curriculum definition is underspecified.** The text describes a linearly increasing curriculum level, but operators become available at discrete thresholds and are then sampled uniformly. Thus, the implemented schedule is mostly stepwise rather than a fully linear increase in augmentation strength. The exact operator-selection probabilities should be stated mathematically.
2. **The \(L=0\) case is formally undefined.** Since \(c(t)=\min(1,t/L)\), the fixed-mixture condition requires a separate definition rather than division by zero.
3. **Baseline fairness needs clarification.** CurCon hyperparameters are selected through a 48-configuration grid search, while baselines use hyperparameters from their original papers. This may advantage CurCon, particularly under dataset and implementation changes. Ideally, all methods should receive comparable tuning budgets.
4. **Statistical evidence is limited.** Results report standard deviations over five seeds, but there are no significance tests or confidence intervals for the claimed improvements. The ablation table also reports only aggregate means, making it difficult to assess variability.
5. **Limited scale of evaluation.** The experiments cover only four relatively short English classification datasets and one encoder architecture. The conclusions should be framed as evidence for this setting rather than as broadly established improvements.
6. **Reproducibility details are incomplete.** Important details such as the exact back-translation model, WordNet preprocessing, maximum sequence length, augmentation composition, data filtering, and sampling procedure should be reported.
7. **Potential data-split ambiguity.** The paper should clarify whether the 200 validation examples are taken from the original training set before constructing the unlabelled pool, and ensure that no validation or test text is used during intermediate training.
8. **Cost comparison is somewhat unclear.** If back-translated views are precomputed for both CERT and CurCon, the stated 12% overhead should distinguish preprocessing cost from optimization-time cost.

These issues are primarily related to experimental control, specification, and reproducibility rather than to a fatal flaw in the central idea.

### Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **78** | The method is plausible and supported by consistent results and ablations, but baseline tuning fairness, statistical testing, and implementation details need improvement. |
| **Novelty** | **72** | Scheduling augmentation difficulty in contrastive intermediate training is a reasonable and useful contribution, although the conceptual advance over curriculum learning and existing augmentation scheduling is incremental. |
| **Significance** | **78** | The gains are practically relevant in low-resource settings, especially with 100 labelled examples, though the absolute improvements are moderate and the evaluation scope is narrow. |
| **Clarity** | **86** | The paper is well structured and easy to follow, with only some ambiguity in the formal curriculum and data-processing descriptions. |

### Final average

\[
\frac{78 + 72 + 78 + 86}{4} = \mathbf{78.5}
\]

## Final recommendation: **Accept**

The paper presents a clear, practically useful, and reasonably well-supported method. Although the novelty is moderate and several experimental details should be strengthened, the consistent improvements over strong baselines, the low-resource analysis, and the informative ablations justify acceptance. The authors should clarify the curriculum implementation, improve baseline tuning comparability, and provide fuller reproducibility and statistical details in the final version.