## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually expands the augmentation policy from token dropout to synonym replacement, span deletion, and back-translation during contrastive pretraining. Experiments on four English classification benchmarks with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The paper also includes ablations, label-efficiency experiments, and a computational-cost analysis.

### Strengths

1. **Consistent empirical gains.** CurCon improves over CERT on all four datasets and achieves a 1.1-point average improvement over the strongest reported baseline.
2. **Relevant low-resource setting.** The focus on 100–1,000 labelled examples addresses an important practical regime.
3. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that the schedule, rather than only the set of augmentations, contributes to performance.
4. **Broad-enough initial evaluation.** Although limited to four datasets, the benchmarks cover sentiment, topic, question, and subjectivity classification.
5. **Practical method.** The approach does not add inference-time parameters and appears straightforward to integrate into existing contrastive training pipelines.
6. **Clear presentation.** The method, experimental pipeline, results, limitations, and computational overhead are described in a generally accessible way.

### Main concerns

1. **Details of the curriculum are somewhat underspecified.** The paper describes augmentation availability using thresholds, while the abstract and motivation characterize the schedule as a linear increase in augmentation strength. In practice, the policy appears piecewise and discrete rather than linearly increasing in a precisely defined strength measure. A formal statement of the sampling probabilities at each training step would improve reproducibility.
2. **The \(L=0\) case requires clarification.** Since \(c(t)=\min(1,t/L)\) is undefined when \(L=0\), the implementation of the fixed-mixture ablation should be stated separately.
3. **Baseline tuning may not be fully comparable.** CurCon is tuned using a grid search on each validation set, whereas the baselines use hyperparameters from their original papers. This may favor the proposed method, especially in a low-resource setting. Ideally, all methods should receive comparable tuning budgets, or the paper should report sensitivity analyses.
4. **Statistical testing is limited.** Results are averaged over five seeds and include standard deviations, which is useful, but the paper does not report confidence intervals or paired significance tests. Given that some improvements are modest, particularly on TREC and at 1,000 labels, statistical testing would strengthen the conclusions.
5. **Ablation variance is absent.** Table 2 reports only average accuracies. Per-dataset results and standard deviations for the ablations would make it easier to determine whether the curriculum is consistently beneficial or whether the average is driven by one or two datasets.
6. **Reproducibility details could be expanded.** The exact back-translation model, WordNet preprocessing, synonym-selection procedure, tokenization behavior, maximum sequence length, optimizer schedule, and early-stopping criteria are not specified. These details are important because augmentation quality can substantially affect contrastive learning.
7. **Potential data-overlap and preprocessing issues should be documented.** The paper should explicitly state whether validation examples are excluded from the unlabelled contrastive corpus and whether any augmented examples can overlap with test content. The current description suggests a reasonable protocol, but an explicit clarification would remove ambiguity.
8. **The novelty is incremental.** Curriculum learning, augmentation scheduling, and contrastive intermediate training are established ideas. The contribution is a sensible and useful combination, but the paper would benefit from a sharper distinction from prior work on augmentation curricula and scheduled perturbation strength.

These issues are primarily matters of experimental transparency, fairness, and strengthening the empirical argument. They do not undermine the central result: the proposed schedule is simple, produces consistent gains across the evaluated tasks, and has a plausible mechanism supported by the ablations.

### Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **80** | The experimental design is broadly appropriate and the results support the main claim, though baseline tuning, statistical testing, and implementation details should be strengthened. |
| **Novelty** | **75** | The contribution is a reasonable and clearly articulated application of curriculum scheduling to contrastive intermediate training, but the conceptual novelty is moderate rather than fundamental. |
| **Significance** | **80** | The method addresses an important low-resource problem and demonstrates consistent, practically relevant improvements, especially with very few labels. Broader datasets and model families would increase impact. |
| **Clarity** | **89** | The paper is well organized and easy to follow. A few definitions and implementation details require clarification, particularly the exact curriculum probabilities and the \(L=0\) condition. |

### Final average score

\[
\frac{80 + 75 + 80 + 89}{4} = \mathbf{81.0}
\]

## Final recommendation: **Accept**

The paper presents a clear, practically motivated method with consistent improvements over relevant baselines and an informative initial ablation study. The main weaknesses concern experimental reporting and comparability rather than the validity of the central approach. Clarifying the curriculum implementation, providing fuller ablation statistics, and improving baseline-tuning transparency would make the work substantially stronger, but the contribution is suitable for acceptance.