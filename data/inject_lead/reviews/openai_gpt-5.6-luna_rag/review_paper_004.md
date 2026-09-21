## Review

### Summary

The paper presents CurCon, a contrastive intermediate-training method that gradually increases the strength of text augmentations during training. The method is evaluated on four English classification datasets in a 500-label setting and reports consistent but modest gains over CERT and other baselines. The paper is clearly written and the experimental question is relevant, but the empirical evidence and methodological specification are not sufficiently rigorous to support the claims.

### Strengths

- Addresses an important low-resource classification setting.
- The proposed curriculum is simple, intuitive, and adds no inference-time parameters.
- Evaluates against several relevant baselines, including UDA, SimCSE, and CERT.
- Includes ablations for fixed versus scheduled augmentation, reversed curriculum, and removal of back-translation.
- Reports results over multiple random seeds and considers different label-budget regimes.
- The paper is generally well organized and easy to follow.

### Major concerns

1. **The curriculum schedule is underspecified.**  
   The paper defines when augmentation operators become “available,” but not how the probability of selecting each operator varies continuously with \(c(t)\). Since the text states that available operators are sampled uniformly, the schedule is actually piecewise constant with abrupt changes, rather than a linearly increasing augmentation-strength schedule. This makes the central method difficult to reproduce and weakens the interpretation of the claimed curriculum.

2. **Baseline comparison may be unfair.**  
   CurCon is tuned over 48 configurations on each validation set, whereas the baselines use hyperparameters reported in their original papers. This gives the proposed method substantially more opportunity for dataset-specific optimization. All baselines should receive comparable tuning budgets, particularly CERT, which is the strongest comparator.

3. **Statistical evidence is insufficient.**  
   Although five random seeds are reported, there are no significance tests, confidence intervals, or paired comparisons. The average gain over CERT is only 1.1 points, and the paper does not establish whether this gain is statistically reliable across datasets and seeds.

4. **The ablation is incomplete.**  
   The fixed-mixture baseline changes both the schedule and potentially the effective distribution of augmentations. A stronger analysis would match the total number and marginal frequencies of each augmentation, compare smooth schedules to thresholded schedules, and evaluate schedules with different orderings and transition rates.

5. **Novelty is not clearly established.**  
   Increasing augmentation difficulty during training is a fairly general curriculum-learning idea, and related augmentation-scheduling approaches exist in representation learning. The paper does not sufficiently distinguish CurCon from prior curriculum or augmentation-magnitude scheduling methods, nor does it explain whether the contribution is more than applying this idea to CERT-style training.

6. **Reproducibility details are missing.**  
   Important details are omitted, including the exact contrastive loss formulation, projection-head dimensions, optimizer learning rate and schedule, maximum sequence length, dropout behavior, back-translation model and decoding settings, synonym-selection procedure, and whether augmentations are applied independently to both views. The statement that back-translated views are precomputed but that CurCon is 12% slower also needs clarification.

7. **Limited scope of evidence.**  
   Results cover only four relatively short English datasets and one encoder architecture. The reported gains may depend heavily on the selected augmentation resources and dataset characteristics. The paper’s claims should therefore be narrowed unless broader experiments are provided.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 55/100 |
| Novelty | 52/100 |
| Significance | 50/100 |
| Clarity | 72/100 |

**Final average:** 57.25/100

## Recommendation: Reject

The problem is relevant and the method is easy to understand, but the current submission does not provide sufficiently rigorous evidence that the proposed curriculum is responsible for the improvements. A stronger revision should precisely define the schedule, tune baselines fairly, report statistical tests, add more controlled ablations, and provide substantially more implementation detail.