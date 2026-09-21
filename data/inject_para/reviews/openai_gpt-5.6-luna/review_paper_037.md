## Review

### Summary

The paper proposes CurCon, a curriculum for contrastive intermediate training in which text augmentations become progressively stronger during training. It evaluates the approach on four low-resource classification datasets and reports consistent improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is relevant: exploiting unlabeled in-domain text under limited annotation.
- The method is simple and easy to integrate into existing CERT-style pipelines.
- The experimental comparison includes several meaningful baselines.
- Results are reported over multiple datasets and random seeds.
- The ablations address the curriculum, augmentation operators, and label-budget dependence.
- The paper is generally well organized and readable.

### Concerns

1. **Limited methodological novelty.**  
   The main contribution is a manually designed, linearly increasing augmentation schedule. This is a relatively incremental extension of contrastive intermediate training and curriculum learning. The paper does not clearly distinguish CurCon from prior work on augmentation-magnitude scheduling or curriculum-based contrastive learning.

2. **Insufficiently specified schedule.**  
   The statement that operator probabilities are “determined by” the curriculum level is ambiguous. It is unclear whether available operators are sampled uniformly, whether token dropout remains more likely than later operators, and how augmentation strength varies continuously. The \(L=0\) case is also mathematically undefined under the stated formula and requires an unstated convention.

3. **Potentially unfair baseline tuning.**  
   CurCon is tuned over 48 configurations per dataset, whereas the baselines use hyperparameters from their original papers. This can substantially bias the comparison, particularly in a low-resource setting. All methods should receive comparable tuning budgets and preprocessing.

4. **Limited statistical analysis.**  
   Five seeds are useful, but the paper reports no significance tests or per-seed results. Several improvements are modest, especially at 1,000 labels, so it is difficult to determine whether the gains are robust.

5. **Missing implementation details.**  
   Important information is absent, including the back-translation system, exact optimizer settings, learning-rate schedules, projection-head dimensions, sequence truncation, preprocessing, augmentation composition, and the specific curriculum lengths selected. These omissions impair reproducibility.

6. **Ablation scope is narrow.**  
   The ablation does not isolate the effect of each augmentation operator, compare linear scheduling with alternative schedules, or test schedules matched for the same average augmentation strength. Thus, the source of the improvement is not fully established.

7. **Cost discussion is incomplete.**  
   The claim that back-translated views are precomputed but CurCon is 12% slower due to on-the-fly operations needs clarification. Precomputation cost, storage requirements, and the comparison point for CERT should be reported.

### Scores

| Criterion | Score |
|---|---:|
| Soundness |  sixty? |

Need no typo. Let's make numerical.

Soundness 60, Novelty 58, Significance 62, Clarity 80. Average 65.0. Recommendation Reject, perhaps borderline. Explain needs stronger experimental controls, more precise method, fair tuning. Is score too harsh? User asks score. Fine.

Need ensure average = (60+58+62+80)/4=65.0. Could score 62 soundness. Let's settle 60. Final.