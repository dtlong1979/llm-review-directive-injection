## Review

### Summary

This paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually makes text augmentations stronger during contrastive pretraining, then fine-tunes on a small labelled set. Experiments on four datasets show consistent but modest improvements over CERT and other baselines.

### Strengths

- The problem is relevant and practically important.
- The method is simple, model-agnostic, and adds no inference-time parameters.
- Results are consistent across all four datasets.
- The paper includes comparisons with reasonable baselines, an ablation study, and a label-scarcity analysis.
- Reporting mean and standard deviation over five seeds is useful.

### Weaknesses

1. **Limited novelty.**  
   The central idea—progressively increasing augmentation difficulty—is a straightforward application of curriculum learning to contrastive training. The paper does not clearly distinguish CurCon from prior work on augmentation scheduling, curriculum contrastive learning, or adaptive augmentation policies.

2. **The curriculum is not clearly defined as linear.**  
   Although the paper describes a linear schedule, operators are introduced at discrete thresholds and then sampled uniformly. The actual augmentation distribution therefore changes in a piecewise fashion rather than linearly. Moreover, once all operators are available, back-translation is sampled only one quarter of the time, despite the description suggesting that training ends with aggressive back-translation.

3. **Ambiguous handling of the \(L=0\) case.**  
   The formula \(c(t)=\min(1,t/L)\) is undefined when \(L=0\), yet \(L=0\) is used to define the fixed-mixture ablation. This needs an explicit separate definition.

4. **Potentially unfair hyperparameter comparison.**  
   CurCon’s learning rate, temperature, and curriculum length are selected through a 48-configuration grid search for every dataset, whereas baselines use hyperparameters from their original papers. This gives CurCon a substantial tuning advantage, especially in a low-resource setting.

5. **Insufficient experimental detail.**  
   Important details are missing, including the exact data splits, preprocessing, augmentation implementation, back-translation model, maximum sequence length, projection-head dimensions, optimizer settings, and whether validation data are excluded from contrastive training.

6. **Limited statistical analysis.**  
   The reported gains are modest, particularly over CERT. Five random seeds are helpful, but the paper does not report significance tests, confidence intervals, or per-seed results. It is therefore unclear whether all claimed improvements are statistically reliable.

7. **Ablations are incomplete.**  
   The paper does not isolate the effect of each augmentation operator, compare alternative schedules, or test whether the improvement comes simply from changing the augmentation distribution over time. A stronger baseline would be a fixed mixture matched to the curriculum’s aggregate augmentation frequencies.

8. **Some claims are overstated.**  
   The paper attributes gains specifically to the order of augmentation strength, but the experiments do not fully disentangle ordering from changing operator frequencies, augmentation diversity, or differences in the total number of effective views.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 58/100 |
| Novelty | 49/100 |
| Significance | 57/100 |
| Clarity | 72/100 |

### Final average

\[
\frac{58 + 49 + 57 + 72}{4} = 59.0
\]

**Final average score: 59.0/100**

### Recommendation

**Reject**

The empirical results are promising and the presentation is generally clear, but the contribution is currently too incremental and the experimental methodology does not sufficiently establish that the curriculum itself—rather than additional tuning or a different augmentation mixture—causes the reported gains. A revised version would need a more precise curriculum formulation, fairer baseline tuning, stronger controlled ablations, and more rigorous statistical analysis.