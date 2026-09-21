## Overall assessment

This paper presents a simple curriculum for contrastive intermediate training in low-resource text classification. The empirical results are promising, and the paper is generally easy to follow. However, the experimental methodology is not sufficiently rigorous to support the strength of the claims. In particular, the baseline tuning procedure is potentially unfair, the curriculum is not actually clearly linear in augmentation strength, and important implementation and statistical details are missing.

### Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **62** | The method is plausible and the reported trends are internally consistent, but the experimental comparison has important weaknesses. CurCon is tuned with a 48-configuration grid on each validation set, whereas baselines use hyperparameters from their original papers. This may substantially advantage CurCon in the low-resource setting. The paper does not report per-seed results, confidence intervals, significance tests, or whether all baselines were reimplemented and tuned under identical conditions. The curriculum is described as linear, but the actual operator availability changes abruptly at thresholds and the expected augmentation strength is not shown to increase linearly. |
| **Novelty** | **66** | Scheduling augmentation difficulty during contrastive training is a reasonable and potentially useful idea. However, the method is a relatively straightforward combination of existing contrastive intermediate training, standard text augmentations, and curriculum learning. The conceptual advance over prior augmentation-scheduling work is modest, and the paper does not sufficiently establish how CurCon differs from existing adaptive or scheduled augmentation methods. |
| **Significance** | **68** | Low-resource text classification is important, and the reported average improvement over CERT is potentially meaningful. The gains are larger with fewer labels, which supports the motivation. Nevertheless, the evaluation is limited to four short English classification datasets and one encoder family. The practical significance is difficult to assess without stronger baselines, broader domains, and more robust statistical analysis. |
| **Clarity** | **78** | The paper is well organized and generally readable. The training pipeline, datasets, and main results are easy to understand. Some methodological details are underspecified, including the exact sampling procedure for two views, augmentation composition, back-translation implementation, preprocessing, optimizer settings, early-stopping protocol, and the treatment of random seeds. The description of the schedule also conflicts somewhat with the claim of a linear increase in augmentation strength. |

### Final average

\[
\frac{62 + 66 + 68 + 78}{4} = \mathbf{68.5}
\]

## Recommendation: **Reject**

The paper has a promising idea and encouraging preliminary results, but the current evidence is not strong enough for acceptance. The most important revision would be to rerun all baselines with comparable hyperparameter tuning and compute budgets, report complete per-seed statistics and significance tests, clarify the exact curriculum mechanism, and expand the ablation and robustness analysis.