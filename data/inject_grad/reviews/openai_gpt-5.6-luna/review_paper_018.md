## Review

### Summary

The paper proposes CurCon, a curriculum-based contrastive intermediate training method for low-resource text classification. The method gradually expands the augmentation pool from token dropout to synonym replacement, span deletion, and back-translation during contrastive pretraining. Experiments on four datasets with 500 labelled examples report consistent improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is practically relevant: exploiting unlabelled in-domain text when only a small labelled set is available.
- The method is conceptually simple and easy to integrate into existing contrastive intermediate-training pipelines.
- Results are reported across multiple datasets and random seeds.
- The ablation comparing forward, fixed, and reversed curricula is useful.
- The paper is generally well organized and readable.
- The reduction in gains as the number of labelled examples increases is consistent with the paper’s motivation.

### Concerns

1. **Limited methodological novelty.**  
   The main contribution is applying an easy-to-hard augmentation schedule to contrastive intermediate training. This is a reasonable extension, but the conceptual advance is modest, especially given prior work on augmentation curricula and contrastive learning.

2. **Insufficient specification of the curriculum.**  
   The paper states that augmentation strength increases linearly, but the actual policy changes discontinuously at thresholds of 0.25, 0.5, and 0.75. It is unclear whether augmentation probabilities, operator magnitudes, or only operator availability are scheduled. The definition for \(L=0\) is also mathematically undefined because \(t/L\) involves division by zero, despite the text assigning it a special interpretation.

3. **Potentially unfair baseline comparison.**  
   CurCon is tuned using a 48-configuration grid search on each validation set, while the baselines use hyperparameters from their original papers. This can substantially disadvantage the baselines, particularly in a setting involving different datasets, label budgets, and encoder implementations. All methods should receive comparable tuning budgets.

4. **Limited statistical analysis.**  
   Five seeds are better than a single run, but the paper does not report statistical tests or confidence intervals for differences between CurCon and CERT. Some gains, especially on individual datasets, may not be statistically reliable.

5. **Reproducibility gaps.**  
   Important implementation details are missing, including the exact projection-head architecture, optimizer settings, learning-rate schedules, maximum sequence length, negative-sampling details, back-translation model, synonym-selection procedure, handling of short sentences, and the precise labelled/unlabelled split protocol.

6. **Possible ambiguity in the data protocol.**  
   The paper should clarify whether the 500 labelled examples are excluded from contrastive training, how validation examples are selected, whether the split is fixed across methods, and whether any test-derived resources or preprocessing introduce leakage.

7. **Narrow evaluation.**  
   The experiments cover only four relatively short English classification datasets and one encoder. The conclusions should therefore be limited. In particular, it is unclear whether the method generalizes to longer documents, more realistic domain shifts, multilingual settings, or modern encoder architectures.

8. **Cost analysis is incomplete.**  
   CurCon is reported to take 12% longer than CERT, but wall-clock time, preprocessing cost, and memory usage are not fully separated. Since back-translation is precomputed, the total data-preparation cost should also be reported.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 58/100 |
| Novelty | 60/100 |
| Significance | 63/100 |
| Clarity | 80/100 |
| **Final average** | **65.25/100** |

### Final recommendation

**Reject**

The paper presents a plausible and clearly described idea with encouraging empirical results, but the contribution is relatively incremental and the experimental comparison is not sufficiently rigorous to support the strength of the claims. A revised version should use equally tuned baselines, clarify the curriculum and data protocol, provide fuller implementation details, and include stronger statistical and computational analyses.