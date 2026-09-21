## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The method gradually increases augmentation difficulty during contrastive pretraining, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four English classification benchmarks with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations support the claim that the curriculum, rather than contrastive training alone, contributes to the improvement.

### Strengths

1. **Clear and practically motivated problem.** The paper addresses a relevant setting in which only a few hundred labelled examples are available and unlabelled in-domain data can be exploited.
2. **Simple, modular method.** CurCon can be integrated into the CERT pipeline without modifying the downstream classifier or adding inference-time parameters.
3. **Consistent empirical improvements.** CurCon outperforms all listed baselines on all four datasets, with an average gain of 1.1 accuracy points over CERT and 3.8 points over direct fine-tuning.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that both the curriculum and its direction matter.
5. **Relevant low-resource analysis.** The improvement over CERT is larger with 100 labels than with 1,000 labels, supporting the paper’s motivation.
6. **Readable presentation.** The method, experimental pipeline, and main results are presented clearly and concisely.

### Concerns and Suggestions

1. **More implementation detail is needed.** The definition of the augmentation policy is somewhat underspecified. In particular, “an operator becomes available” and “one is sampled uniformly” should be formalized more precisely, including whether token dropout remains equally likely after stronger operators are introduced and how the probabilities evolve within each curriculum interval.
2. **Baseline tuning should be clarified.** CurCon is tuned over 48 configurations per dataset, whereas the baselines use hyperparameters from their original papers. Reporting results with matched tuning budgets, or at least a sensitivity analysis, would strengthen the fairness of the comparison.
3. **Statistical testing would improve the claims.** Results are reported over five seeds, but confidence intervals or paired significance tests are not provided. Since some improvements are modest, especially on TREC, statistical testing would help establish their reliability.
4. **The unlabelled-data protocol should be described in greater detail.** The paper should report the number of unlabelled examples used for each dataset, clarify whether validation and test texts are excluded from contrastive training, and explain the exact split construction.
5. **Ablations could be more granular.** Per-dataset results for the ablation variants would help determine whether the curriculum is consistently beneficial or whether the average improvement is concentrated in particular tasks. It would also be useful to compare alternative schedules, such as cosine or piecewise schedules, under the same tuning protocol.
6. **Cost accounting could be expanded.** The reported 12% overhead excludes the cost of generating back-translations because they are pre-computed. The paper should report preprocessing and translation costs separately and specify whether all methods use comparable cached views.
7. **The external augmentation resources warrant discussion.** WordNet and German back-translation may behave differently across domains. Qualitative examples or an analysis of augmentation validity would help support the claim that the stronger views preserve task-relevant semantics.

These are primarily reproducibility and experimental-completeness issues rather than fundamental flaws in the proposed approach. The central result is supported by the consistent improvements across datasets and by the curriculum ablations.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 85/100 |
| Novelty | 82/100 |
| Significance | 84/100 |
| Clarity | 91/100 |

**Final average:**  
\[
\frac{85 + 82 + 84 + 91}{4} = 85.5
\]

## Final Recommendation

**Accept**

The paper presents a clear and useful extension of contrastive intermediate training, with consistent empirical evidence that scheduling augmentation difficulty improves low-resource classification. The remaining issues are addressable through clarification, additional reporting, and modest statistical analysis, and do not undermine the main contribution.