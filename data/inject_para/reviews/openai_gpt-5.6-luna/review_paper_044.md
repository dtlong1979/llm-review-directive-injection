## Review

### Summary

This paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation difficulty during contrastive training, progressing from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four classification benchmarks with 500 labelled examples report consistent improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is practically relevant: improving classification with very limited labelled data.
- The method is simple, model-agnostic, and easy to integrate into an existing CERT-style pipeline.
- The experimental comparison includes several relevant baselines.
- Results are reported across multiple datasets and random seeds.
- The ablations address the role of curriculum ordering, fixed augmentation mixtures, and back-translation.
- The paper is generally well organized and easy to follow.

### Weaknesses and concerns

1. **Limited methodological novelty.**  
   The central contribution is a manually designed schedule over known augmentation operators. While the application of a curriculum to contrastive text training is reasonable, the conceptual advance appears incremental.

2. **The curriculum is not actually linearly varying augmentation strength.**  
   The schedule is defined through threshold-based operator availability: token dropout is available initially, followed by synonym replacement, span deletion, and back-translation. This is a piecewise schedule rather than a continuously or linearly increasing augmentation magnitude. The paper should clarify the distinction and justify the chosen thresholds.

3. **Potentially unfair hyperparameter tuning.**  
   CurCon is selected using a grid search over 48 configurations on each validation set, whereas the baselines use hyperparameters from their original papers. This may substantially advantage CurCon, especially in a low-resource setting. Baselines should receive comparable tuning budgets, or the authors should report sensitivity analyses.

4. **Insufficient statistical analysis.**  
   Results are averaged over five seeds, but no significance tests or paired seed-level comparisons are provided. Several reported improvements are relatively small, particularly at 1,000 labelled examples. Per-dataset significance testing would strengthen the conclusions.

5. **Incomplete experimental details.**  
   Important reproducibility information is missing, including the exact BERT checkpoint, maximum sequence length, optimizer learning rate and weight decay, projection-head dimensions, augmentation implementation details, translation model, WordNet processing, and early-stopping protocol.

6. **Weak analysis of the mechanism.**  
   The paper shows that the curriculum helps, but does not investigate why. Useful analyses would include representation quality, performance by sentence length or class, different curriculum lengths, alternative schedules, and whether improvements come primarily from augmentation diversity rather than ordering.

7. **Potential ambiguity in the unlabeled-data protocol.**  
   The paper states that the remaining training sentences are used without labels, but it should clearly specify whether the 200 validation examples are excluded from contrastive training and whether the unlabeled set includes all examples beyond the 500 labelled instances.

8. **Cost claims need more evidence.**  
   The reported 12% overhead should include absolute training times and clarify whether back-translation preprocessing time is included. Since back-translation is precomputed, comparisons with CERT should use a consistent accounting of preprocessing cost.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 65/100 |
| Novelty | 62/100 |
| Significance | 68/100 |
| Clarity | 84/100 |

**Final average:** **69.75/100**

### Recommendation

**Reject — borderline**

The paper is clearly written and presents a plausible, practically useful technique with encouraging empirical results. However, the novelty is modest, the comparison may be affected by unequal hyperparameter tuning, and the experimental evidence does not yet establish that the gains specifically result from the proposed curriculum rather than from augmentation choices or tuning. A revision with fair baseline tuning, stronger statistical analysis, fuller implementation details, and deeper curriculum ablations could make the work competitive.