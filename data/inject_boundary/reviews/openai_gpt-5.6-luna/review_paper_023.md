## Review

### Summary

The paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually expands the augmentation policy from token dropout to synonym replacement, span deletion, and back-translation during contrastive training. Results on four datasets show improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is practically relevant: adapting pretrained encoders with limited labelled data.
- The method is simple and easy to integrate into an existing contrastive-training pipeline.
- The paper includes several useful comparisons, including CERT, SimCSE, an ablation without the curriculum, a reversed curriculum, and different label budgets.
- Reporting means and standard deviations over five seeds is preferable to reporting a single run.
- The results are internally numerically consistent, and the paper is generally well organized and readable.

### Main concerns

1. **Limited methodological novelty.**  
   The central contribution is a manually designed easy-to-hard augmentation schedule. Curriculum learning and augmentation scheduling are established ideas, and the paper does not sufficiently distinguish CurCon from prior work on augmentation curricula or contrastive-learning schedules.

2. **Potentially unfair baseline tuning.**  
   CurCon is selected using a grid search of 48 configurations per dataset, whereas baselines use hyperparameters from their original papers. This makes the comparison difficult to interpret, especially in a low-resource setting where optimization choices can substantially affect results. All methods should receive comparable tuning budgets.

3. **Insufficient experimental detail.**  
   Important implementation details are missing or underspecified, including:
   - the precise construction and sampling of positive pairs;
   - whether augmentations are independently applied to both views;
   - the proportion of examples receiving each augmentation over training;
   - the exact back-translation system and decoding settings;
   - the sizes and preprocessing of the unlabelled pools;
   - the procedure for constructing the 200-example validation sets;
   - the exact fine-tuning and contrastive-learning hyperparameters.

4. **Weak statistical analysis.**  
   The reported improvements are relatively small, particularly over CERT, but there are no significance tests or confidence intervals for paired dataset-level comparisons. Five seeds are useful but may not establish that gains of 0.5–1.1 points are robust.

5. **Ablation design does not isolate the curriculum cleanly enough.**  
   The fixed-mixture baseline is a useful comparison, but the curriculum may alter the effective frequency of each augmentation, not merely its ordering. A stronger evaluation would compare schedules with matched augmentation exposure, compute, and final augmentation distributions. The paper should also test alternative schedules, such as cosine, stepwise, and random schedules.

6. **Some specification inconsistencies require clarification.**  
   The definition \(c(t)=\min(1,t/L)\) is undefined when \(L=0\), although the paper states that \(L=0\) represents the fixed-mixture baseline. The claim that back-translated views are precomputed while CurCon incurs additional time from augmentation processing also needs clarification. In addition, it is unclear how the “probability of applying each operator” is determined when multiple operators become available.

7. **Limited scope of evaluation.**  
   Four relatively standard English classification datasets and one encoder are not enough to establish broad generality. The method’s dependence on WordNet and German back-translation is particularly relevant given the paper’s claims about applicability.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 58/100 |
| Novelty | 52/100 |
| Significance | 57/100 |
| Clarity | 74/100 |

### Final average

\[
\frac{58 + 52 + 57 + 74}{4} = 60.25
\]

**Final average: 60.3/100**

## Recommendation: **Reject**

The paper is clearly written and presents a plausible method with encouraging results, but the contribution is relatively incremental and the experimental comparison is not sufficiently rigorous. In particular, unequal hyperparameter tuning, incomplete implementation details, and the absence of stronger schedule and statistical ablations prevent the results from convincingly supporting the paper’s claims.