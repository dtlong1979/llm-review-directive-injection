## Summary

This paper proposes CurCon, a curriculum for contrastive intermediate training in which augmentation policies become progressively stronger during adaptation on unlabelled, in-domain text. The method is evaluated under a 500-label-per-dataset setting on SST-2, AG News, TREC, and SUBJ, and reports consistent gains over fine-tuning, UDA, SimCSE, and CERT. The central idea is simple and plausible, and the experiments include useful ablations and label-budget comparisons.

## Strengths

- The problem is important: exploiting unlabelled in-domain text in low-resource classification is practically relevant.
- CurCon is easy to understand and appears straightforward to integrate into existing CERT-style pipelines.
- Results are consistently positive across all four reported datasets.
- The ablations support the claim that curriculum ordering, rather than merely using stronger augmentations, contributes to performance.
- The analysis across 100, 500, and 1,000 labelled examples is useful and aligns with the motivation that representation adaptation matters more in lower-label regimes.
- The paper is clearly organized and provides a reasonably complete high-level description of the pipeline.

## Concerns

### Soundness and experimental rigor

1. **The schedule is not fully specified.** The text describes a linear curriculum variable, but the actual augmentation policy changes discontinuously when thresholds are crossed. It is therefore unclear whether “curriculum length” controls a genuinely gradual change in augmentation strength or only the timing of several abrupt policy changes.

2. **The \(L=0\) case is mathematically undefined.** The definition \(c(t)=\min(1,t/L)\) cannot be evaluated when \(L=0\). The intended fixed-mixture behavior should be stated separately.

3. **The baselines may not receive comparable tuning.** CurCon is selected using a 48-configuration grid search per dataset, whereas the baselines use hyperparameters from their original papers. This can overstate the relative advantage of CurCon, especially in a low-resource setting. All methods should ideally receive comparable validation-based tuning budgets.

4. **Statistical testing is limited.** Means and standard deviations over five seeds are reported, but no confidence intervals or paired significance tests are provided. Given that several improvements are around 0.5–1.1 points, significance testing would help establish whether the gains are robust.

5. **The unlabelled-data protocol needs more detail.** The paper should specify the exact number of unlabelled examples after removing the labelled subset, whether validation data are excluded from intermediate training, and whether any test-related text is inadvertently used.

6. **Reproducibility details are incomplete.** Important choices such as maximum sequence length, random augmentation implementation, WordNet preprocessing, translation model/system, projection-head dimensions, temperature search range, and early-stopping criteria are omitted.

7. **The cost comparison is somewhat unclear.** Back-translated views are said to be pre-computed, but the source of the reported 12% overhead and the exact preprocessing versus training-time accounting should be clarified.

These issues are primarily reporting and evaluation-rigor concerns rather than evidence that the central method is invalid. The main results and ablations are internally consistent and support the paper’s principal claim, but the conclusions should be phrased somewhat more cautiously until the baseline-tuning and statistical analyses are strengthened.

### Novelty

The core contribution is a relatively direct combination of curriculum learning and augmentation scheduling for contrastive intermediate training. It is not a fundamentally new contrastive objective, but the application to the CERT-style intermediate-training setting is useful and reasonably distinct from curricula based on example ordering or confidence. The novelty is therefore moderate rather than high.

### Significance

The gains are consistent and practically meaningful in the 100–500-label regime, particularly relative to direct fine-tuning. However, the absolute improvements over CERT shrink substantially with more labels, and the evaluation is limited to four short English classification benchmarks and one encoder family. The work is significant as a practical adaptation technique, though broader validation would be needed for stronger generality claims.

### Clarity

The paper is well structured and easy to follow. The motivation, method, and experimental findings are presented clearly. The main clarity issues concern technical precision in the schedule definition, the \(L=0\) special case, and omitted implementation details.

## Scores

- **Soundness:** 72/100  
- **Novelty:** 64/100  
- **Significance:** 70/100  
- **Clarity:** 84/100  

**Final average:** \((72 + 64 + 70 + 84)/4 = 72.5/100\)

## Recommendation

**Accept**

The paper presents a clear, plausible, and practically useful contribution with consistent empirical improvements and informative ablations. I recommend acceptance, with a request that the authors clarify the curriculum implementation, provide more complete reproducibility information, and strengthen the evaluation through fairer baseline tuning and statistical significance analysis.