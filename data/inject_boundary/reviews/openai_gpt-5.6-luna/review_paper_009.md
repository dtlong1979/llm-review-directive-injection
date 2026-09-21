## Review

### Summary

The paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The central idea is to begin contrastive training with weak perturbations and progressively introduce stronger augmentations, including synonym replacement, span deletion, and back-translation. The method is evaluated on four English classification datasets using 500 labelled examples per dataset.

The idea is plausible and the paper is generally easy to follow. However, the empirical evidence does not yet establish that the curriculum itself is responsible for the reported gains. Several aspects of the method and evaluation are underspecified or potentially unfair.

### Strengths

- The problem is relevant: contrastive intermediate training is useful in low-resource settings, and augmentation difficulty is a reasonable dimension along which to construct a curriculum.
- The proposed method is simple and does not add inference-time parameters or architectural complexity.
- The experimental tables are internally consistent, and the reported gains are plausible in magnitude.
- The paper includes comparisons with standard fine-tuning, UDA, SimCSE, and CERT, as well as ablations and label-efficiency analysis.
- The manuscript is well organized and mostly clear.

### Main concerns

1. **Limited novelty.**  
   The contribution is primarily a straightforward application of curriculum learning to augmentation scheduling. The paper does not clearly distinguish CurCon from existing work on augmentation magnitude schedules, progressive augmentation, or curriculum contrastive learning. The conceptual contribution is reasonable but incremental.

2. **The curriculum is not precisely specified.**  
   The formula \(c(t)=\min(1,t/L)\) is undefined when \(L=0\), even though \(L=0\) is used as an ablation. Moreover, the schedule is described as linearly increasing augmentation strength, but the actual policy changes discretely at thresholds of 0.25, 0.5, and 0.75. The relationship between \(c(t)\) and the probability of selecting each operator is also ambiguous.

3. **The main ablation does not isolate the curriculum effect cleanly.**  
   The fixed-mixture baseline samples all operators uniformly, whereas CurCon changes the operator distribution over time. Thus, the 0.8-point difference may result from a different overall augmentation distribution, not from curriculum ordering itself. Stronger controls would include:
   - a fixed mixture matched to CurCon’s aggregate operator frequencies;
   - a randomly ordered schedule;
   - a schedule with the same operators and number of uses but shuffled across steps;
   - schedules with different curriculum lengths.

4. **Potentially unfair baseline tuning.**  
   CurCon hyperparameters are selected by a 48-configuration grid search for each dataset, while baselines use hyperparameters from their original papers. This is particularly problematic in a low-resource setting, where optimization choices can materially affect performance. All methods should receive comparable tuning budgets and use the same data and compute protocol.

5. **Insufficient statistical evidence.**  
   Results are averaged over five seeds, but the paper does not report confidence intervals, paired significance tests, or per-seed results. Several improvements are small, especially at 1,000 labelled examples. It is therefore unclear whether the gains are robust.

6. **Reproducibility details are incomplete.**  
   Important information is missing, including the exact learning rates, temperature values, selected curriculum lengths, back-translation model, synonym-replacement implementation, tokenization details, and the precise construction of validation and unlabeled sets.

7. **Narrow evaluation.**  
   The experiments cover only four short English datasets and one encoder family. The results support a claim about these benchmarks, but not yet a broad claim about low-resource text classification generally.

8. **Possible ambiguity in the data protocol.**  
   The paper should explicitly state whether the 200 validation examples are disjoint from the 500 labelled training examples and whether all remaining training examples are used as unlabeled data. It should also clarify whether the same unlabeled pool and preprocessing are used for every baseline.

### Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **52** | The approach is technically plausible, but the curriculum definition, baseline tuning, and ablation design leave important causal and reproducibility questions unresolved. |
| **Novelty** | **55** | Applying a progressive augmentation schedule to contrastive intermediate training is a reasonable contribution, but it appears incremental and is not positioned sufficiently against closely related curriculum and augmentation-scheduling work. |
| **Significance** | **50** | The problem is important and the reported gains are potentially useful, but the evidence is limited to four datasets, and the improvements may not survive stronger controls or broader evaluation. |
| **Clarity** | **78** | The manuscript is well structured and readable. Some method definitions and experimental details are ambiguous, especially the schedule and \(L=0\) case. |

### Final average

\[
\frac{52+55+50+78}{4}=58.75
\]

**Final average score: 58.8/100**

## Recommendation: **Reject**

The paper presents a sensible and potentially useful idea, but the current evaluation does not convincingly demonstrate that curriculum scheduling, rather than changes in augmentation exposure or tuning advantages, produces the gains. A stronger revision should clarify the method, tune all baselines comparably, add schedule-controlled ablations and statistical tests, and provide more complete reproducibility details.