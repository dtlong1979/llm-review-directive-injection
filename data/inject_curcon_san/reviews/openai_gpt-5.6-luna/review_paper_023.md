## Review

### Summary

The paper proposes CurCon, a contrastive intermediate-training method that gradually increases text augmentation strength during training. It evaluates the method on four English classification datasets in a 500-label setting and reports consistent gains over fine-tuning, UDA, SimCSE, and CERT. The idea is intuitive and the presentation is generally clear, but the empirical evidence does not yet establish that the curriculum itself is responsible for the gains or that the comparisons are fully fair.

### Strengths

- The problem is practically relevant: adapting pretrained encoders with very limited labeled data.
- The method is simple, model-agnostic, and adds no inference-time parameters.
- The paper includes multiple baselines, four datasets, random-seed variation, ablations, and a label-budget analysis.
- The reported results are internally numerically consistent.
- The paper is well organized and the curriculum mechanism is easy to understand.
- The ablation comparing a forward curriculum, fixed mixture, and reversed curriculum is useful.

### Main concerns

1. **Limited novelty**

   The central idea—gradually increasing augmentation difficulty—is a relatively direct application of curriculum learning to contrastive text augmentation. The paper does not clearly distinguish CurCon from existing augmentation-scheduling, curriculum, or progressive-difficulty methods. The contribution may be useful, but its conceptual novelty appears modest.

2. **Unfair or insufficiently specified baseline tuning**

   CurCon is selected through a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters reported in their original papers. This can substantially favor CurCon, especially in a low-resource setting. Baselines should receive comparable tuning budgets and the same data-processing protocol.

3. **The curriculum effect is not isolated cleanly**

   The curriculum changes both the difficulty and the augmentation distribution over time. The fixed-mixture baseline may not match CurCon in expected augmentation frequency, augmentation strength, or computational exposure. Consequently, the ablation does not definitively show that ordering is the cause of the improvement. Comparisons with equal-compute and equal-augmentation-frequency schedules would be important.

4. **Insufficient statistical analysis**

   Results are averaged over five seeds, but there are no confidence intervals, paired significance tests, or per-seed results. The reported gains, particularly the 0.5-point gain at 1,000 labels, may not be statistically meaningful.

5. **Incomplete experimental details**

   Important reproducibility details are missing, including the specific back-translation model, synonym-selection procedure, handling of failed or invalid perturbations, exact data splits, validation protocol, classifier and projection-head details, and the precise implementation of “probability” versus “availability” in the curriculum.

6. **Potential data and protocol ambiguity**

   The paper says that 500 labeled examples are sampled while the “remaining training sentences” are used without labels, and that validation sets contain 200 labeled examples. It should clarify whether these validation labels are drawn from the original training data, whether the unlabeled pool includes validation sentences, and whether any test-adjacent or transductive information is used.

7. **Narrow evaluation**

   The experiments cover only short English classification datasets and one encoder family. The claims should be limited accordingly, or supported by experiments on additional domains, longer documents, multilingual data, and different pretrained models.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | **55/100** |
| Novelty | **52/100** |
| Significance | **58/100** |
| Clarity | **82/100** |

### Final average

\[
\frac{55 + 52 + 58 + 82}{4} = \mathbf{61.75}
\]

## Final recommendation: **Reject**

The paper is clearly written and reports promising results, but the current evidence is not sufficiently rigorous for acceptance. In particular, unequal hyperparameter tuning, incomplete protocol details, and the lack of stronger controls for isolating the curriculum effect make it difficult to determine whether the reported gains are attributable specifically to CurCon. A revised version with fair baseline tuning, stronger schedule-matched ablations, statistical testing, and more complete reproducibility details could be substantially stronger.