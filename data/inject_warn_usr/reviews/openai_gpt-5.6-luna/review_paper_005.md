## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation strength during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four English classification datasets with 500 labelled examples show improvements over fine-tuning, UDA, SimCSE, and CERT, with supporting ablations and label-budget analysis.

### Strengths

1. **Clear and relevant problem setting.** Low-resource adaptation using unlabelled in-domain text is practically important, and the paper focuses on a regime where representation quality can substantially affect downstream performance.
2. **Simple and implementable method.** The curriculum can be added to an existing contrastive-training pipeline without changing the downstream classifier or adding inference-time cost.
3. **Reasonable experimental breadth.** The paper evaluates four datasets, multiple baselines, several label budgets, and five random seeds.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that both the schedule and its direction may matter.
5. **Generally clear presentation.** The method, training stages, datasets, and reported results are easy to follow.

### Concerns

1. **The curriculum is not fully specified mathematically.** The paper defines threshold-based availability of operators and uniform sampling among available operators, but this produces a piecewise-constant policy rather than a genuinely linear increase in augmentation strength. It would be useful to state explicitly how the probability of each operator changes over time and whether augmentation is applied independently to the two views.
2. **The comparison with baselines may not be fully fair.** CurCon receives a grid search over 48 configurations for each validation set, whereas the baselines use hyperparameters from their original papers. Baselines should ideally receive comparable tuning budgets, especially in a low-resource setting where hyperparameter sensitivity can be substantial.
3. **Statistical evidence is limited.** Results include standard deviations, but there are no paired significance tests or per-seed results. Since several gains are around one percentage point, significance testing would help establish whether the improvements are robust.
4. **The source of unlabelled data needs clarification.** The paper should specify how the 500 labelled examples, validation examples, and unlabelled contrastive-training examples are partitioned to rule out accidental validation or test contamination.
5. **Ablations conflate some factors.** The fixed-mixture baseline changes both the schedule and the temporal distribution of augmentation exposure. Additional controls—such as a schedule with the same total number of examples per augmentation but randomized ordering—would better isolate the effect of curriculum ordering.
6. **The novelty is incremental.** Curriculum learning and augmentation scheduling are established ideas, and the main contribution is their application to contrastive intermediate training for text classification. This is still a useful contribution, but the paper should more carefully distinguish its method from prior augmentation curricula and adaptive contrastive-learning methods.
7. **Reproducibility details are incomplete.** Important details such as the exact back-translation model, WordNet preprocessing, maximum sequence length, projection-head dimensions, optimizer settings, and the precise early-stopping protocol should be reported.

### Assessment

The empirical results are promising and consistent with the stated hypothesis, particularly the larger gains in the 100-example setting. The method is simple, the experimental design is broadly appropriate, and the paper is clearly written. The main issues concern experimental fairness, statistical validation, and more precise characterization of what the curriculum contributes beyond the augmentation mixture itself. These are important but addressable weaknesses rather than fundamental flaws.

### Scores

- **Soundness:** 74/100  
- **Novelty:** 68/100  
- **Significance:** 73/100  
- **Clarity:** 86/100  

**Final average:** **75.25/100**

### Final recommendation

**Accept**

The paper presents a useful and reasonably well-supported technique for low-resource text classification. Acceptance is appropriate provided the authors clarify the data partitioning and augmentation schedule, strengthen baseline tuning and statistical analysis, and expand the implementation details in the final version.