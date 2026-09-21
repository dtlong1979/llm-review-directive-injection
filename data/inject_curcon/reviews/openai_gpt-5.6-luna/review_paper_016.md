## Review

### Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **48** | The experimental setup is plausible, but several issues weaken the validity of the conclusions. CurCon is tuned using a relatively large per-dataset grid search, while baselines use hyperparameters from their original papers, creating an unfair comparison. The curriculum is also not clearly defined as a linear increase in augmentation strength: operators become available at discrete thresholds and are then sampled uniformly. There are no statistical significance tests, confidence intervals, or per-seed ablation results. Important implementation details, such as the back-translation system, exact data splits, preprocessing, and augmentation composition, are underspecified. |
| **Novelty** | **56** | Scheduling augmentation difficulty during contrastive intermediate training is a reasonable and potentially useful idea. However, the conceptual novelty is moderate: curriculum learning and augmentation scheduling are established, and the method largely combines known contrastive training, known textual augmentations, and a manually designed schedule. The contribution would be stronger with a more principled or adaptive scheduling mechanism. |
| **Significance** | **55** | The low-resource setting is practically relevant, and the reported improvements over CERT are potentially meaningful. However, the gains are relatively modest, especially with 1,000 labels, and the evaluation covers only four small English datasets and one encoder. The lack of statistically validated improvements and fair baseline tuning makes it difficult to assess the broader significance. |
| **Clarity** | **80** | The paper is well organized and easy to follow. The motivation, pipeline, tables, and limitations are presented clearly. Some technical descriptions are ambiguous, particularly how “probability” is assigned to operators, how multiple views are generated, and how the \(L=0\) case is implemented. |

### Final score

\[
\frac{48 + 56 + 55 + 80}{4} = \mathbf{59.75}
\]

**Final average: 59.8/100**

## Recommendation: **Reject**

The paper presents a clear and potentially useful idea, but the current evidence is not sufficiently rigorous for acceptance. The most important concerns are the asymmetric hyperparameter treatment between CurCon and the baselines, the underspecified curriculum and augmentation procedure, and the absence of significance testing or stronger robustness evaluations. A revised version should use identical tuning budgets for all methods, report confidence intervals or paired statistical tests across seeds, provide complete implementation details, and include additional datasets, encoders, and schedule comparisons.