## Review

### Summary
The paper proposes CurCon, a curriculum-based contrastive intermediate-training method that gradually increases text augmentation strength before low-resource fine-tuning. The idea is intuitive and the presentation is generally clear, but the empirical evidence is not sufficiently rigorous to support the claims. The main contribution is also relatively incremental: it applies a standard easy-to-hard curriculum to an existing contrastive adaptation pipeline.

### Scores

| Criterion | Score |
|---|---:|
| **Soundness** | 55/100 |
| **Novelty** | 45/100 |
| **Significance** | 50/100 |
| **Clarity** | 82/100 |
| **Final average** | **58.0/100** |

### Strengths

- The paper addresses a practically relevant problem: text classification with very limited labeled data.
- The method is simple, intuitive, and easy to implement.
- The experimental tables are easy to read, and the reported results are internally consistent. For example, the CurCon average is correctly computed as 88.9.
- The paper includes useful ablations, comparisons across different label budgets, and a cost discussion.
- The limitations section appropriately acknowledges restrictions concerning language, model scale, and augmentation resources.

### Weaknesses

#### Soundness

1. **Insufficient experimental detail and rigor.** Important implementation details are missing, including the precise back-translation system, preprocessing, handling of failed WordNet replacements, sequence truncation, projection-head architecture, and the exact training/validation split procedure.

2. **Potentially unfair baseline tuning.** CurCon is tuned over 48 configurations for each dataset, whereas the baselines use hyperparameters from their original papers. This can substantially favor CurCon, especially in a low-resource setting. All methods should receive comparable tuning budgets.

3. **No statistical significance testing.** Results are averaged over five seeds, but the paper does not report confidence intervals or paired significance tests. Several gains are relatively small, particularly the 0.5-point improvement at 1,000 labels.

4. **The curriculum is not actually clearly linear.** Although the schedule \(c(t)\) is linear, the augmentation policy changes through abrupt thresholds at 0.25, 0.5, and 0.75. The paper should clarify the exact sampling probabilities at each step and distinguish a continuous strength schedule from a staged availability schedule.

5. **Possible confounds in the augmentation comparison.** The full method combines four augmentations, and the ablation removes back-translation, but there is no comparison against a fixed mixture with matched augmentation frequencies or against each individual operator. Thus, the improvement may partly result from the augmentation mixture rather than the curriculum.

6. **Limited scope of evaluation.** Only four relatively short English classification datasets and one encoder are tested. This makes it difficult to establish generality.

#### Novelty

The core proposal—progressively increasing augmentation difficulty during contrastive training—is plausible but conceptually straightforward. The paper does not clearly distinguish its approach from existing augmentation scheduling, curriculum learning, or adaptive contrastive-learning methods. The novelty would be stronger with a more principled schedule, theoretical motivation, or evidence that the method improves over carefully matched scheduling baselines.

#### Significance

The reported improvements are potentially useful, especially in the 100-label condition. However, the absolute gains are modest, the datasets are standard and relatively small, and the evaluation does not establish robustness across domains, languages, encoders, or stronger modern baselines. The practical significance is therefore promising but not yet convincingly demonstrated.

#### Clarity

The paper is well organized and readable. The motivation, pipeline, results, and limitations are presented clearly. Some technical ambiguities remain, particularly regarding how \(c(t)\) maps to operator probabilities and how the unlabeled and validation data are partitioned.

### Recommendation: **Reject**

The paper presents a reasonable and clearly described idea, but the contribution is incremental and the current experimental design does not adequately isolate the effect of the curriculum or rule out tuning and augmentation confounds. A stronger revision should use equally tuned baselines, report statistical tests, provide complete implementation details, include matched fixed-policy and individual-augmentation controls, and evaluate on broader datasets and model families.