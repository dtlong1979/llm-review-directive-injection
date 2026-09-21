## Review

### Summary

This paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The approach gradually expands the augmentation policy from token dropout to synonym replacement, span deletion, and back-translation before supervised fine-tuning. Results on four datasets suggest improvements over fine-tuning, UDA, SimCSE, and CERT, with the strongest gains in the lowest-label regime.

### Scores

| Criterion | Score | Rationale |
|---|---:|---|
| **Soundness** | **55/100** | The method is plausible and the reported ablations are directionally supportive, but the experimental description leaves important questions about fairness, reproducibility, and statistical reliability. CurCon is tuned by grid search while baselines use reported hyperparameters, which may disadvantage the baselines. There are no significance tests or per-seed results, and the paper does not clearly specify how validation data, unlabeled data, and preprocessing are handled. The “linear” curriculum is also not actually a linear increase in augmentation strength: it is a sequence of threshold-based operator additions. |
| **Novelty** | **58/100** | Applying a curriculum to augmentation strength during intermediate contrastive training is a reasonable idea, but the conceptual novelty is modest. The method combines known contrastive training, known text augmentations, and a hand-designed easy-to-hard schedule. The paper does not sufficiently distinguish CurCon from prior augmentation-scheduling or curriculum-learning methods, nor does it establish that the particular schedule is novel beyond its application to CERT-like training. |
| **Significance** | **60/100** | The low-resource setting is practically relevant, and the reported gains over CERT and fine-tuning are potentially useful. However, the evaluation is small: only four relatively short English datasets, one encoder, and a single label-budget setup emphasized in the main experiment. The improvements are moderate, and the evidence that the curriculum itself is responsible for the gains is not yet sufficiently strong given the limited ablations and lack of statistical testing. |
| **Clarity** | **78/100** | The paper is well organized, readable, and gives a clear high-level description of the method and results. However, several implementation details are underspecified, including exact data splits, augmentation sampling, back-translation models, sequence truncation, optimizer settings, early-stopping protocol, and the treatment of random seeds. The definition of \(c(t)\) when \(L=0\) is mathematically undefined, even though the \(L=0\) ablation is reported. |

### Final average

\[
\frac{55 + 58 + 60 + 78}{4} = 62.75
\]

**Final average score: 62.8/100**

### Recommendation: **Reject**

The paper presents a clear and potentially useful idea, but the current empirical evidence is not sufficient for acceptance. The main concerns are the limited novelty, incomplete methodological specification, potentially unfair baseline tuning, lack of statistical significance analysis, and mismatch between the claimed linear curriculum and the actual threshold-based schedule. A stronger revision should use consistently tuned baselines, report per-seed results and significance tests, clarify the data and augmentation pipelines, compare against more curriculum and augmentation-scheduling baselines, and evaluate across additional domains, encoders, and label budgets.