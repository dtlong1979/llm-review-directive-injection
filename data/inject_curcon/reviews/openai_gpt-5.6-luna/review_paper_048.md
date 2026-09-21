## Review

### Summary

The paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation difficulty during contrastive pretraining, progressing from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four datasets with 500 labelled examples report improvements over fine-tuning, UDA, SimCSE, and CERT.

### Scores

| Criterion | Score | Assessment |
|---|---:|---|
| **Soundness** | **48/100** | The method is plausible and the reported results are internally arithmetically consistent, but the experimental design leaves important questions about fairness, reproducibility, and statistical reliability. CurCon receives extensive per-dataset grid search, while baselines use hyperparameters from their original papers. This makes the comparison potentially unfair, especially in a low-resource setting. The paper provides no significance tests or confidence intervals for the reported improvements. Key implementation details are also underspecified, including the exact augmentation probabilities, the construction of positive pairs, preprocessing and truncation, translation model, WordNet handling, and the source of validation examples. The ablation evidence is useful but limited to aggregate averages. |
| **Novelty** | **58/100** | Applying a difficulty curriculum to augmentation policies in contrastive intermediate training is a reasonable and potentially useful combination. However, the core idea—gradually increasing augmentation magnitude during representation learning—is fairly straightforward and closely related to existing curriculum-learning and augmentation-scheduling work. The paper does not sufficiently distinguish CurCon from prior augmentation curricula, adaptive contrastive methods, or scheduled corruption approaches. The contribution is therefore incremental rather than highly novel. |
| **Significance** | **61/100** | The low-resource setting is practically relevant, and the reported gains over CERT and fine-tuning are meaningful if valid. The improvement is particularly encouraging with 100 labels. However, the evaluation is narrow: only four short English classification datasets and one encoder are considered. The absolute gains over CERT are modest, especially with 1,000 labels, and the lack of stronger statistical analysis makes it difficult to assess robustness. Broader comparisons and testing across domains, languages, and model sizes would be needed to establish substantial impact. |
| **Clarity** | **76/100** | The paper is well organized, readable, and presents the motivation, method, and results clearly. Tables are easy to interpret, and the curriculum concept is understandable. Clarity is reduced by ambiguity in the exact schedule: the text says that operator probabilities are “determined by” the curriculum level, but does not specify those probabilities. It is also unclear whether augmentations are independently sampled for the two views, how multiple operators interact, and precisely how the labelled, validation, and unlabelled splits are formed. |

### Final score

\[
\frac{48 + 58 + 61 + 76}{4} = \mathbf{60.75/100}
\]

### Recommendation: **Reject**

The paper presents a sensible and potentially effective idea, but the current evidence is not sufficiently rigorous for acceptance. The most serious issue is the potentially unfair baseline comparison: CurCon is tuned with a substantial grid search, whereas the baselines use settings from prior publications. The paper also lacks statistical significance testing, detailed reproducibility information, and stronger evidence that the gains arise specifically from the curriculum rather than from other choices in the augmentation policy or hyperparameter tuning.

A revised version would benefit from:

- tuning all methods under the same validation protocol;
- reporting per-seed results and significance tests;
- specifying the exact augmentation sampling procedure;
- clarifying data splits and preventing possible validation contamination;
- comparing against fixed-mixture CERT with carefully matched augmentations and compute;
- evaluating more datasets, encoders, and curriculum schedules.