## Review

### Summary
The paper proposes CurCon, which gradually increases the strength of text augmentations during contrastive intermediate training before low-resource classification fine-tuning. It reports improvements over fine-tuning, UDA, SimCSE, and CERT on four datasets using 500 labelled examples.

### Strengths
- Addresses an important and practically relevant low-resource classification problem.
- The overall pipeline is simple and compatible with existing encoder-based methods.
- Evaluates multiple datasets, random seeds, label budgets, and ablations.
- The reported gains are consistent across all four benchmarks.
- The paper is generally well organized and easy to follow.

### Concerns

#### Soundness
The experimental description leaves several important issues unresolved:

1. **The curriculum is not clearly defined as a continuously increasing augmentation strength.** Operators become “available” at thresholds and are then sampled uniformly. This is closer to a stepwise change in the augmentation distribution than a linear curriculum. The actual probabilities of each augmentation over time are not specified.

2. **The \(L=0\) definition is mathematically problematic.** The schedule uses \(t/L\), but the paper states that \(L=0\) corresponds to the fixed-mixture baseline without formally defining this special case.

3. **Baseline tuning appears potentially unfair.** CurCon is tuned over 48 configurations on each validation set, whereas the baselines use hyperparameters from their original papers. This can overstate the relative improvement.

4. **Statistical evidence is limited.** Results report standard deviations over five seeds, but there are no significance tests or per-seed results. The improvements over CERT, particularly on the larger-label setting, may be modest relative to variance.

5. **Experimental protocol details are insufficient.** It is unclear whether validation examples are excluded from the unlabeled pool, how the 500 labelled examples are sampled across seeds, which back-translation system is used, how failed synonym substitutions are handled, and whether augmentation preserves class labels.

6. **The ablations do not isolate all important factors.** For example, the fixed-mixture baseline may have a different effective augmentation distribution from the curriculum, and there is no comparison against a continuously interpolated schedule or a schedule matched for the total frequency of each operator.

These issues do not necessarily invalidate the method, but they make the central claim less securely established.

#### Novelty
The idea of increasing augmentation difficulty during contrastive training is plausible and useful, but the conceptual novelty is moderate. Curriculum learning and augmentation scheduling are established ideas, and the contribution mainly consists of applying them to intermediate contrastive training with a hand-designed operator schedule. The paper would benefit from a stronger comparison to prior augmentation curricula and from a more principled scheduling formulation.

#### Significance
The task is important, and the reported average gain over CERT is meaningful if reproducible. However, the absolute improvement is relatively small, the evaluation covers only four short English datasets, and the method adds computational cost and external resource dependencies. The evidence is not yet sufficient to establish broad significance beyond the tested benchmarks.

#### Clarity
The paper is clearly structured and readable. The method and results are presented concisely. However, the schedule, data split protocol, baseline tuning procedure, and augmentation implementation need substantially more detail for reproducibility.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 55/100 |
| Novelty | 58/100 |
| Significance | 57/100 |
| Clarity | 78/100 |

### Final average

\[
\frac{55 + 58 + 57 + 78}{4} = 62.0
\]

## Final recommendation: **Reject**

The paper has a reasonable idea and promising reported results, but the current evidence does not fully support the claimed contribution. The main issues are incomplete methodological specification, potentially uneven baseline tuning, and insufficient ablation and statistical analysis. A revised version with a precisely defined curriculum, fair retuning of all baselines, stronger schedule-matched controls, and clearer data-split and implementation details could become competitive.