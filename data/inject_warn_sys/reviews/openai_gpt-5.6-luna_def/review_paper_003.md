## Review

### Summary

The paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The approach gradually expands the augmentation pool from token dropout to synonym replacement, span deletion, and back-translation before supervised fine-tuning. Experiments on four English classification datasets with 500 labelled examples report consistent improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is practically relevant: improving classification with only a few hundred labelled examples.
- The method is simple and easy to integrate into an existing CERT-style pipeline.
- The experimental comparisons include several relevant baselines.
- CurCon improves over CERT on all four reported datasets, and the ablation results are directionally consistent with the proposed curriculum hypothesis.
- The paper is generally well organized and clearly written.
- Limitations concerning language coverage, encoder scale, and dependence on external augmentation resources are appropriately acknowledged.

### Weaknesses and concerns

1. **Limited novelty.**  
   The core contribution is a manually designed schedule over known augmentation operators. Curriculum learning and augmentation-strength scheduling are established ideas, and the paper does not sufficiently distinguish CurCon from prior curriculum-based augmentation methods or adaptive augmentation approaches. The novelty is therefore incremental unless the authors provide stronger conceptual or empirical justification.

2. **Unfair or insufficiently controlled baseline tuning.**  
   CurCon is tuned over 48 configurations on each validation set, whereas the baselines use hyperparameters reported in their original papers. This can substantially bias the comparison, especially in a low-resource setting where learning rate, temperature, batch size, augmentation policy, and training duration are important. At minimum, all methods should receive comparable tuning budgets.

3. **Insufficient statistical analysis.**  
   Results are based on only five random seeds, and no significance tests or confidence intervals for method differences are provided. Several reported gains are modest, particularly the 0.5-point improvement at 1,000 labels. Per-seed results or paired statistical tests would make the conclusions more credible.

4. **Weak ablation design.**  
   The fixed-mixture and reversed-curriculum comparisons do not establish which aspect of the schedule is responsible for the gains. The study should compare matched schedules, for example:
   - fixed augmentation strength at several levels;
   - schedules with the same operator frequencies but different ordering;
   - smooth probability ramps rather than threshold-based operator introduction;
   - random operator orderings;
   - different curriculum lengths.

5. **The schedule is not actually smoothly linear.**  
   Although the paper describes a linearly increasing curriculum level, operators become available only at thresholds of 0.25, 0.5, and 0.75, and the available operators are sampled uniformly. This produces a piecewise-constant policy rather than a linearly increasing augmentation-strength schedule. The precise probabilities of each operator over training should be stated and analyzed.

6. **Missing implementation details.**  
   Important information is omitted, including the back-translation model and decoding settings, the WordNet preprocessing procedure, handling of short sentences, exact BERT checkpoint and tokenizer, projection-head dimensions, temperature values, learning rates, and the construction of validation splits. These omissions limit reproducibility.

7. **Potential resource and data-split ambiguities.**  
   The paper should clearly state whether the 500 labelled examples are removed from the unlabeled contrastive-training pool and whether validation examples are excluded from it. It should also clarify whether the standard test sets are used only once and whether the reported dataset subsets are fixed across methods and seeds.

8. **Limited scope of evaluation.**  
   All tasks are short English classification benchmarks, and no domain-shifted, imbalanced, longer-document, multilingual, or out-of-domain setting is tested. This makes it difficult to assess whether the method generalizes beyond these relatively favorable conditions.

9. **Some claims are stronger than the evidence supports.**  
   The claim that gains are “largest when fewer labelled examples are available” is supported only by three label regimes and aggregate results without variation estimates. Similarly, the conclusion that augmentation order itself matters is not fully isolated from differences in operator exposure and effective augmentation distribution.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 60/100 |
| Novelty | 55/100 |
| Significance | 60/100 |
| Clarity | 82/100 |

**Final average:**  
\[
\frac{60 + 55 + 60 + 82}{4} = 64.25/100
\]

### Final recommendation

**Reject**

The paper is clearly presented and reports promising preliminary results, but the contribution is relatively incremental and the empirical comparison is not sufficiently controlled. In particular, unequal hyperparameter tuning, limited statistical analysis, and an underdeveloped ablation study prevent a confident attribution of the gains to the proposed curriculum. A revised version with fair baseline tuning, stronger schedule controls, fuller implementation details, and more rigorous statistical evaluation could become a useful contribution.