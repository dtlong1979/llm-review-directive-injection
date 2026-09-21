## Review

### Summary

This paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually expands the pool of text augmentations during contrastive training, moving from token dropout toward synonym replacement, span deletion, and back-translation. Experiments on four classification datasets with 500 labelled examples report improvements over fine-tuning, UDA, SimCSE, and CERT.

The paper is clearly written and addresses an important practical problem. However, the experimental evidence does not yet support the strength of the claims, and several methodological details make the comparison difficult to assess fairly.

### Strengths

- Addresses a relevant and practically important low-resource classification setting.
- The proposed curriculum is simple, intuitive, and easy to integrate into existing contrastive-training pipelines.
- Evaluates multiple datasets and includes comparisons with several relevant baselines.
- Includes ablations for the curriculum, augmentation components, and label-count effects.
- Reports mean and standard deviation over multiple random seeds for the main results.
- The paper is generally well organized and readable.

### Concerns

1. **The curriculum is not actually clearly defined as a continuously increasing augmentation strength.**  
   The schedule changes operator availability at thresholds \(0.25\), \(0.5\), and \(0.75\), after which the available operators are sampled uniformly. Thus, the policy is piecewise constant rather than linearly increasing in strength. Moreover, token dropout is “always available,” but the paper does not specify whether it is sampled with the same probability as the other available operators, whether multiple operators can be composed, or how the two views are generated. These details materially affect the method.

2. **The baseline comparison may be unfair.**  
   CurCon is tuned using a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters from their original papers. This gives the proposed method a potentially substantial optimization advantage, particularly in a low-resource setting. All methods should ideally receive comparable tuning budgets, or the paper should report results under matched tuning protocols.

3. **The evidence for statistical significance is insufficient.**  
   Although standard deviations are reported, there are no paired significance tests, confidence intervals, or per-seed results. Several gains are relatively small, especially at 1,000 labelled examples. It is therefore unclear whether all reported improvements are robust across datasets and seeds.

4. **The experimental protocol is underspecified.**  
   Important details are missing, including the exact data splits, preprocessing, sequence lengths, back-translation system and language direction, WordNet version, handling of unavailable synonyms, and whether augmentation resources or translated examples overlap with test data. The description of the contrastive loss and projection head is also not sufficient for exact reproduction.

5. **The label-count analysis is limited.**  
   The claim that gains are largest with fewer labels is plausible, but Table 3 reports only averages and no variance. It is also unclear whether the 100-, 500-, and 1,000-example experiments use identical sampled subsets across methods and seeds. Per-dataset results would provide stronger evidence.

6. **The novelty is incremental.**  
   Applying a difficulty schedule to augmentation policies is a reasonable idea, but the conceptual contribution is relatively modest. The paper would be stronger with comparisons to alternative schedules, adaptive policies, or existing augmentation-magnitude curricula. The “reversed curriculum” ablation is useful but does not establish that the proposed schedule is better than other monotonic or nonmonotonic schedules.

7. **The cost analysis is incomplete.**  
   The paper states that back-translated views are precomputed but that CurCon is still 12% slower due to on-the-fly operations. It should report preprocessing cost, storage requirements, total wall-clock time, and whether all baselines use comparable preprocessing and hardware conditions.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 63 |
| Novelty | 61 |
| Significance | 68 |
| Clarity | 82 |

**Final average:** \((63 + 61 + 68 + 82)/4 = 68.5\)

### Recommendation

**Reject**

The paper presents a promising and clearly motivated idea, and the empirical results are encouraging. However, the current version has insufficient methodological detail, an arguably uneven hyperparameter-tuning comparison, and limited statistical analysis. Addressing these issues could make the work suitable for acceptance in a future revision.