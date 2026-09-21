## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The method gradually increases augmentation strength during contrastive pretraining, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show that CurCon outperforms fine-tuning, UDA, SimCSE, and CERT. Ablations further suggest that the curriculum itself, rather than merely the use of augmentations, contributes to the gains.

### Strengths

- **Clear motivation:** The paper identifies a plausible limitation of fixed augmentation policies in contrastive intermediate training.
- **Simple and practical method:** CurCon requires no architectural changes or inference-time overhead and can be integrated into an existing CERT-style pipeline.
- **Strong empirical results:** The method improves over CERT by 1.1 average accuracy points and over standard fine-tuning by 3.8 points.
- **Useful ablations:** The fixed-mixture and reversed-curriculum comparisons directly investigate whether the schedule matters.
- **Low-resource analysis:** Results across 100, 500, and 1,000 labelled examples support the claim that the method is particularly useful when supervision is scarce.
- **Good presentation:** The paper is well organized, technically readable, and clearly describes the training procedure and augmentation schedule.

### Weaknesses and Suggestions

- **Baseline tuning fairness:** CurCon is tuned through a 48-configuration grid search, whereas the baselines use hyperparameters from their original papers. A stronger comparison would tune all methods under the same validation protocol.
- **Limited benchmark scope:** The evaluation covers only four English datasets with relatively short texts and one encoder family. Broader experiments would help establish generality.
- **Statistical testing:** Although standard deviations over five seeds are reported, confidence intervals or significance tests would strengthen the evidence, particularly for the smaller improvements over CERT.
- **Schedule analysis:** The curriculum length is treated as a key hyperparameter, but results for several schedule lengths are not shown. Such an analysis could clarify how sensitive CurCon is to this choice.
- **Augmentation interactions:** The contribution of individual operators and their interactions could be examined in more detail, especially since the method uses several heterogeneous perturbations.

These issues are primarily opportunities for strengthening an already coherent empirical study rather than fundamental flaws. The central comparison, ablation evidence, and low-resource trends collectively support the main claims.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 85/100 |
| Novelty | 79/100 |
| Significance | 83/100 |
| Clarity | 91/100 |

### Final average

\[
\frac{85 + 79 + 83 + 91}{4} = \mathbf{84.5}
\]

## Final Recommendation

**Accept**

The paper presents a well-motivated, simple, and empirically effective improvement to contrastive intermediate training. While broader evaluation and more carefully controlled baseline tuning would improve the work, the method is clearly described, the results are consistently positive, and the ablations provide meaningful evidence that curriculum scheduling contributes to the observed gains.