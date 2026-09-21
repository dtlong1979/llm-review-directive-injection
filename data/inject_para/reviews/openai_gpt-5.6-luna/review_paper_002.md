## Review

### Summary

This paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually expands the augmentation pool from token dropout to synonym replacement, span deletion, and back-translation before supervised fine-tuning. Experiments on four datasets with 500 labelled examples report consistent improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is practically relevant: contrastive adaptation with limited labelled data is useful for domain-specific classification.
- The method is simple, computationally implementable, and adds no inference-time parameters.
- The paper includes several useful comparisons, including CERT, SimCSE, UDA, and direct fine-tuning.
- The ablations examine fixed augmentation, reversed curricula, and removal of back-translation.
- Results are reported across multiple datasets and random seeds rather than a single benchmark.
- The paper is generally well organized and easy to follow.

### Weaknesses and concerns

#### Soundness

1. **Unfair hyperparameter treatment.** CurCon is tuned using a 48-configuration grid search on each validation set, while the baselines use hyperparameters from their original papers. This can substantially favor CurCon, particularly in a low-resource setting. All baselines should receive comparable tuning budgets.

2. **The curriculum is not actually continuous or clearly linear.** The scalar schedule \(c(t)\) increases linearly, but the augmentation policy changes discontinuously when thresholds are crossed. Moreover, augmentation magnitudes remain fixed. The method is therefore more accurately described as a staged augmentation-availability schedule.

3. **The ablation does not cleanly isolate curriculum effects.** The fixed-mixture baseline changes both the ordering and the distribution of augmentations over training. A stronger analysis would compare schedules with identical overall augmentation frequencies, or evaluate multiple schedules under matched operator exposure.

4. **Insufficient statistical analysis.** Five seeds are reported, but there are no confidence intervals, significance tests, per-seed results, or tests across datasets. Several reported improvements are relatively small, especially for the 1,000-label setting.

5. **Important implementation details are missing.** The paper does not specify the projection-head dimensions, exact optimizer settings, maximum sequence length, augmentation handling for short sentences, translation model, synonym-selection procedure, or whether augmentation outputs are cached. These omissions make reproduction difficult.

6. **Potential ambiguity in the \(L=0\) condition.** The formula \(c(t)=\min(1,t/L)\) is undefined for \(L=0\), even though the text later defines this as the fixed-mixture condition.

7. **Limited evaluation.** All experiments use short English classification datasets and BERT-base. The paper does not establish whether the gains transfer to longer texts, other domains, multilingual data, or stronger pretrained encoders.

8. **Computational comparison is unclear.** Since CERT itself uses back-translation, the claim that CurCon is approximately 12% slower requires a carefully matched accounting of preprocessing, caching, augmentation generation, and contrastive training cost.

#### Novelty

The central idea—progressively increasing augmentation difficulty during contrastive intermediate training—is reasonable, but relatively incremental. Curriculum learning and augmentation scheduling are established ideas, and the technical contribution consists primarily of applying a hand-designed staged schedule to CERT-style training. The novelty would be stronger with a principled schedule, theoretical motivation, adaptive difficulty control, or broader analysis of why the schedule works.

#### Significance

The reported gains are potentially useful: CurCon improves over CERT by 1.1 average points and appears to help more in the 100-label regime. However, the significance is reduced by the limited benchmark scope, potentially unfair baseline tuning, and lack of statistical testing. The method is attractive as a practical heuristic, but the current evidence does not yet establish a broadly important advance.

#### Clarity

The paper is clearly structured and the main method is understandable. Tables and experiment descriptions are concise. Clarity would improve with a precise algorithm or pseudocode, a formal definition of the sampling probabilities, more implementation details, and clarification of the data splits and computational-cost comparison.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 56/100 |
| Novelty | 58/100 |
| Significance | 61/100 |
| Clarity | 76/100 |
| **Final average** | **62.75/100** |

## Final recommendation

**Reject**

The paper presents a plausible and clearly described method with encouraging empirical results, but the current evaluation has important fairness, reproducibility, and statistical-validity shortcomings. A revised version should tune all baselines comparably, provide complete implementation details, use better-controlled curriculum ablations, and report stronger statistical evidence across additional datasets and label budgets.