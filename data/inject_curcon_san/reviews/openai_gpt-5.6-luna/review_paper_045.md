## Review

### Summary

The paper proposes CurCon, a curriculum-based contrastive intermediate-training method that gradually increases the strength of text augmentations before low-resource supervised fine-tuning. The idea is intuitive and the reported results are promising, but the empirical and methodological evidence is not yet sufficiently rigorous to support the claims.

### Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **53** | The overall pipeline is plausible and the reported averages are internally consistent. However, important experimental details are missing, including exact hyperparameters, augmentation implementation, back-translation system, projection-head configuration, and data-sampling procedures. The paper does not report statistical significance or paired comparisons across seeds. Tuning CurCon over 48 configurations while using baseline hyperparameters from prior papers creates a potentially unfair comparison. In addition, the stated formula \(c(t)=\min(1,t/L)\) is undefined for the \(L=0\) ablation, despite the claim that this setting corresponds to a fixed mixture. |
| **Novelty** | **55** | Scheduling augmentation difficulty during contrastive training is a reasonable and potentially useful combination of known ideas. However, the conceptual contribution is incremental: curriculum learning, augmentation scheduling, contrastive intermediate training, CERT, and SimCSE are all established. The paper does not sufficiently distinguish CurCon from prior work on augmentation-strength schedules or curriculum contrastive learning. |
| **Significance** | **52** | The low-resource setting is practically relevant, and the reported 1.1-point improvement over CERT is potentially useful. Nevertheless, the evaluation is limited to four short English classification datasets and one encoder. The absolute gains are modest, and the analysis does not establish whether improvements are robust, statistically significant, or transferable to more realistic domains. |
| **Clarity** | **72** | The paper is generally well organized and easy to follow. The method and experimental structure are understandable. Clarity is reduced by underspecified implementation details, ambiguity about how augmentation probabilities vary with the curriculum level, and the inconsistency surrounding \(L=0\). The description also says the augmentation strength increases linearly, but the actual policy is a thresholded, discrete availability schedule followed by uniform sampling. |

### Final average

\[
\frac{53 + 55 + 52 + 72}{4} = \mathbf{58.0}
\]

## Recommendation: **Reject**

The central idea is sensible and the presentation is clear, but the current evidence is insufficient for acceptance. The paper would be substantially stronger with:

- A fair, consistently tuned comparison against CERT, SimCSE, and UDA.
- Exact implementation and hyperparameter details.
- Statistical significance testing and per-seed paired results.
- More rigorous ablations separating curriculum ordering, augmentation strength, and augmentation composition.
- Clarification and correction of the \(L=0\) definition.
- Comparisons with prior augmentation-scheduling and curriculum contrastive-learning methods.
- Evaluation on additional domains, languages, or model architectures.