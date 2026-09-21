## Review

### Summary

The paper proposes CurCon, a contrastive intermediate-training method that gradually increases the availability of text augmentations during self-supervised training. The method is evaluated on four English classification datasets in a 500-label setting and reports improvements over fine-tuning, UDA, SimCSE, and CERT. The central idea is intuitive and the experimental results are promising, but several methodological and reporting issues limit confidence in the conclusions.

### Strengths

- Addresses an important practical problem: classification with very limited labeled data.
- The proposed method is simple and adds no inference-time parameters.
- Evaluation includes multiple datasets and several relevant baselines.
- Results are reported over multiple random seeds.
- The paper includes ablations, label-budget analysis, and a computational-cost discussion.
- The presentation is generally well organized and easy to follow.

### Main concerns

1. **The curriculum is not actually linear in augmentation strength.**  
   The schedule \(c(t)=\min(1,t/L)\) is linear, but augmentation availability changes in discrete thresholds at 0.25, 0.5, and 0.75. Moreover, each operator has a fixed magnitude, and available operators are sampled uniformly. Thus, the effective augmentation distribution is staircase-shaped rather than linearly increasing. The paper should define the exact sampling probabilities and distinguish curriculum progress from augmentation severity.

2. **The ablation does not fully isolate the curriculum effect.**  
   The fixed-mixture baseline is useful, but the curriculum changes the temporal distribution of augmentations and the frequency with which each operator is used during training. A stronger control would preserve the same marginal augmentation frequencies while randomizing their order, or compare against multiple fixed mixtures with matched compute and operator usage.

3. **Baseline tuning is potentially unfair.**  
   CurCon is selected using a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters from their original papers. This can substantially favor the proposed method, particularly in low-resource settings. All methods should receive comparable tuning budgets.

4. **Statistical evidence is incomplete.**  
   Standard deviations are provided for the main results, but not for the ablations or label-budget experiments. No significance tests or per-seed results are reported. Given the relatively small improvements over CERT, especially at 1,000 labels, it is difficult to assess whether the gains are robust.

5. **Important implementation details are missing.**  
   The paper does not fully specify the sentence representation, projection-head architecture, exact InfoNCE formulation, augmentation sampling for the two views, back-translation system, truncation behavior, or the precise curriculum-length search space. These omissions affect reproducibility.

6. **The interpretation of the gains is somewhat overstated.**  
   The experiments support an improvement for the tested English datasets and settings, but they do not establish that progressive augmentation is generally superior. The method also combines several augmentation operators and external resources, so the gains may partly reflect the augmentation set rather than the curriculum itself.

7. **Novelty is moderate rather than substantial.**  
   Applying a difficulty schedule to augmentation strength in contrastive learning is a reasonable contribution, but it is a relatively direct extension of curriculum learning and existing contrastive intermediate-training methods. The paper would benefit from stronger positioning against prior augmentation-scheduling methods and more careful novelty claims.

### Scores

| Criterion | Score (0–100) |
|---|---:|
| Soundness | 52 |
| Novelty | 58 |
| Significance | 60 |
| Clarity | 82 |

### Final average

\[
\frac{52 + 58 + 60 + 82}{4} = 63.0
\]

### Final recommendation: **Reject**

The paper is clearly written and presents a plausible, potentially useful method, but the current evidence does not adequately establish that the curriculum itself—rather than tuning differences, augmentation composition, or other confounds—is responsible for the reported improvements. Stronger controlled experiments, fair baseline tuning, complete implementation details, and statistical analysis would be needed for acceptance.