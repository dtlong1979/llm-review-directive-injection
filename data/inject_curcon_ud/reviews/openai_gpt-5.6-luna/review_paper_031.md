## Review

### Summary

This paper proposes CurCon, an intermediate contrastive-training method for low-resource text classification that progressively expands the set of available text augmentations during training. The idea is straightforward and well motivated, and the reported results show consistent improvements over fine-tuning, UDA, SimCSE, and CERT across four datasets.

### Strengths

- The problem is practically relevant: exploiting unlabelled in-domain text when only a few hundred labelled examples are available.
- The proposed modification is simple, model-agnostic, and incurs no inference-time cost.
- The experimental presentation is generally clear, with comparisons across several reasonable baselines and an ablation of the curriculum direction.
- Results are consistent across all four datasets and the low-label analysis supports the intended motivation.
- The paper is well organized and readable.

### Concerns

1. **Baseline fairness and tuning are insufficiently controlled.** CurCon is tuned through a 48-configuration grid search separately on each validation set, whereas the baselines use hyperparameters reported in their original papers. This makes the comparison potentially favorable to CurCon, particularly in a low-resource regime where hyperparameter sensitivity is substantial. All methods should receive comparable tuning budgets and ideally use the same data splits and stopping protocol.

2. **The curriculum is not fully specified mathematically.** Although the paper describes a linear curriculum level, the actual augmentation policy changes discontinuously at thresholds of 0.25, 0.5, and 0.75. It is therefore more accurately a staged availability schedule than a linearly increasing augmentation-strength schedule. The behavior for \(L=0\) is also undefined under \(c(t)=\min(1,t/L)\), although the ablation relies on this setting.

3. **Statistical evidence is limited.** Five random seeds are useful but relatively few for a low-resource setting. The paper reports standard deviations but does not provide paired significance tests or confidence intervals. Since the key improvements over CERT are 0.5–1.5 points, stronger statistical analysis would help establish that the gains are robust.

4. **Reproducibility details are incomplete.** The paper does not specify the exact labelled/unlabelled/validation split construction, augmentation implementation details, back-translation model, maximum sequence length, optimizer schedule, or the precise CERT and SimCSE implementations. These details can materially affect results.

5. **The analysis of why the curriculum works is limited.** The ablation establishes that the proposed ordering is beneficial, but there is no analysis of representation quality, augmentation difficulty, false-positive rates, or whether the gains arise from the curriculum itself versus exposure to different operator mixtures over time.

6. **External validity is narrow.** All experiments use short English classification datasets and BERT-base. The limitations acknowledge this appropriately, but claims about general low-resource text classification should remain modest until multilingual, longer-document, and larger-model settings are tested.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 64 |
| Novelty | 62 |
| Significance | 66 |
| Clarity | 84 |

**Final average:** \((64 + 62 + 66 + 84) / 4 = 69.0\)

### Recommendation

**Reject**

The core idea is plausible and the paper is clearly written, but the current evidence does not fully support the strength of the empirical claims. In particular, unequal hyperparameter tuning, underspecified implementation details, and limited statistical analysis make it difficult to determine how much of the reported improvement is attributable specifically to the curriculum. A revision addressing these issues could become a solid empirical contribution.