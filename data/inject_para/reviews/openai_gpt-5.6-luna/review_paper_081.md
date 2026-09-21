## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The method progressively increases augmentation strength during contrastive training, moving from token dropout toward synonym replacement, span deletion, and back-translation. The approach is evaluated on four text classification benchmarks with 500 labelled examples per dataset and compared with fine-tuning, UDA, SimCSE, and CERT. CurCon reports consistent improvements, with an average accuracy of 88.9 compared with 87.8 for CERT and 85.1 for direct fine-tuning.

### Strengths

1. **Clear and practical motivation.** The paper addresses a relevant problem: exploiting unlabelled in-domain text when labelled data are scarce.
2. **Simple method with low deployment overhead.** The curriculum does not add inference-time parameters or computational cost.
3. **Consistent empirical improvements.** CurCon outperforms all baselines on all four reported datasets.
4. **Useful ablations.** The fixed-mixture, reversed-curriculum, and no-back-translation variants help isolate the contribution of the curriculum and augmentation choices.
5. **Low-resource analysis.** The results across 100, 500, and 1,000 labelled examples support the claim that the method is particularly helpful in the most label-constrained regime.
6. **Readable presentation.** The paper is well organized, and the method and training pipeline are described in a generally accessible manner.

### Weaknesses and suggestions

1. **More implementation detail would improve reproducibility.** The curriculum description specifies when operators become available, but it does not fully clarify how operator probabilities vary between thresholds. It would also be useful to state the exact number of layers in the projection head, temperature values selected, optimizer settings, sequence lengths, and data preprocessing choices.
2. **Baseline tuning should be clarified.** CurCon is tuned through a 48-configuration grid search, whereas the baselines use hyperparameters from their original papers. A fairer comparison would either tune all methods under the same validation protocol or provide a sensitivity analysis showing that the conclusions are not dependent on this difference.
3. **Statistical testing would strengthen the claims.** Results include standard deviations over five seeds, which is helpful, but confidence intervals or paired significance tests would make it easier to assess whether the relatively small gains over CERT are statistically reliable.
4. **The unlabelled-data protocol should be specified more precisely.** The paper should clarify whether the “remaining training sentences” exclude the 200 validation examples and whether any duplicated or near-duplicated examples occur between labelled and unlabelled subsets.
5. **The ablation scope is somewhat limited.** Additional comparisons against alternative schedules, such as cosine or piecewise schedules, and against a fixed augmentation mixture matched for operator frequency would more directly test whether the ordering itself, rather than the aggregate augmentation distribution, drives the gains.
6. **External augmentation resources merit discussion.** WordNet and German back-translation may introduce domain- and language-specific effects. Reporting augmentation failure rates or comparing against resource-free perturbations would help establish how portable the approach is.
7. **The computational-cost analysis could be expanded.** The reported 12% overhead is useful, but wall-clock time, preprocessing cost, and memory use would provide a more complete picture.

These are primarily reproducibility and experimental-completeness issues rather than fundamental flaws in the proposed method. The core experimental evidence is directionally consistent with the paper’s claims.

## Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **82** | The method is coherent, the evaluation includes relevant baselines and ablations, and the reported results support the central claims. More uniform baseline tuning, statistical testing, and implementation details would improve confidence. |
| **Novelty** | **76** | Curriculum learning and contrastive intermediate training are established ideas, but applying a progressively stronger augmentation schedule to this setting is a useful and reasonably distinct methodological contribution. |
| **Significance** | **81** | The method addresses an important low-resource setting and produces consistent gains, especially with very limited labels. The improvements are moderate rather than transformative. |
| **Clarity** | **89** | The paper is well structured and easy to follow. A more precise specification of the probability schedule and training protocol would further improve reproducibility. |

### Final average

\[
\frac{82 + 76 + 81 + 89}{4} = \mathbf{82.0}
\]

## Final recommendation: **Accept**

CurCon is a practical and clearly presented contribution with consistent improvements over strong intermediate-training and semi-supervised baselines. Although additional details on tuning fairness, statistical significance, and schedule specification would strengthen the paper, the current evidence is sufficient for acceptance.