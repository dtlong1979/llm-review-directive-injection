## Review

### Summary

The paper proposes CurCon, a contrastive intermediate-training method that progressively increases text augmentation difficulty before low-resource supervised fine-tuning. The idea is intuitive and experimentally promising: CurCon improves over the reported CERT baseline by 1.1 average accuracy points across four datasets. However, the empirical evidence is not yet sufficiently rigorous to establish that the gains are attributable specifically to the curriculum rather than to augmentation choice, hyperparameter tuning, or implementation differences.

### Scores

| Criterion | Score | Assessment |
|---|---:|---|
| **Soundness** | **58/100** | The overall training pipeline is plausible, and the ablation results support some benefit from scheduling. However, several methodological details are underspecified, and the comparison is potentially unfair because CurCon is tuned by an extensive per-dataset grid search while baselines use hyperparameters from their original papers. The curriculum definition is also internally ambiguous: the paper describes a linear schedule, but the actual policy changes at discrete thresholds, and the \(L=0\) formulation is mathematically undefined without an additional convention. No statistical significance tests or per-seed ablation results are reported. |
| **Novelty** | **57/100** | Applying an easy-to-hard augmentation curriculum to contrastive intermediate training is a reasonable and potentially useful combination. Nevertheless, the conceptual novelty is moderate: curriculum learning, augmentation scheduling, and contrastive intermediate training are all established ideas. The method appears to be a relatively simple hand-designed schedule rather than a substantially new contrastive objective or adaptive curriculum mechanism. |
| **Significance** | **63/100** | The low-resource setting is practically relevant, and the reported gains are largest with only 100 labels, which is encouraging. Still, the evaluation is limited to four small English classification datasets and BERT-base. The average improvement over CERT is modest, and the absence of significance testing makes it difficult to determine whether the gains are robust. Stronger comparisons, broader datasets, and better-controlled experiments would be needed to establish wider impact. |
| **Clarity** | **76/100** | The paper is well organized and generally easy to follow. The motivation, method, and experimental results are presented clearly. Reproducibility is weakened by missing details about the exact augmentation probabilities, synonym-selection procedure, back-translation system, optimization settings, preprocessing, dataset sampling, and baseline implementations. |

### Final average

\[
\frac{58 + 57 + 63 + 76}{4} = \mathbf{63.5/100}
\]

## Recommendation: **Reject**

The paper presents a clear and plausible idea with encouraging preliminary results, but the current evidence is insufficient for acceptance. The main concerns are experimental fairness and incomplete specification of the curriculum. In particular:

1. **Unequal hyperparameter tuning:** CurCon receives a 48-configuration per-dataset grid search, whereas the baselines use settings from prior publications. All methods should be tuned under the same validation protocol.
2. **Ambiguous curriculum formulation:** The schedule is described as linear, but augmentation availability changes discretely at thresholds. The relationship between \(c(t)\) and operator probabilities is not explicitly defined.
3. **Undefined \(L=0\) case:** The formula \(c(t)=\min(1,t/L)\) is undefined when \(L=0\), despite the ablation treating this as a valid setting.
4. **Insufficient statistical analysis:** Five seeds are reported for the main results, but no confidence intervals, paired tests, or significance tests are provided. The relatively small improvements may not be statistically reliable.
5. **Weakly controlled ablations:** The fixed-mixture and reversed-curriculum variants should be matched for augmentation frequency, compute, and possibly random augmentation choices. Additional ablations isolating each operator and schedule shape would help establish causality.
6. **Limited evaluation:** Only four English datasets and one encoder are used, limiting evidence for generality.

A revised version with matched tuning for all baselines, a precise schedule definition, stronger statistical testing, and more comprehensive ablations could become a solid empirical contribution.