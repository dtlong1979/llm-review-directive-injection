## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The method gradually increases the strength of text augmentations during contrastive pretraining, moving from token dropout to synonym replacement, span deletion, and back-translation. On four datasets with 500 labelled examples, CurCon outperforms fine-tuning, UDA, SimCSE, and CERT, with additional ablations suggesting that the curriculum itself contributes to the gains.

### Strengths

- **Clear and practical problem setting.** Low-resource classification with in-domain unlabelled data is important and well motivated.
- **Simple, modular method.** CurCon can be incorporated into an existing CERT-style pipeline without architectural changes or inference-time overhead.
- **Strong empirical results.** CurCon improves over CERT by 1.1 average accuracy points and over direct fine-tuning by 3.8 points.
- **Useful ablations.** The comparisons with a fixed mixture, reversed curriculum, and removal of back-translation help isolate the contribution of the proposed schedule.
- **Low-resource analysis.** The experiments varying the number of labelled examples support the claim that the method is particularly beneficial when supervision is scarce.
- **Readable presentation.** The paper is clearly structured, and the mathematical description of the schedule is concise and understandable.

### Weaknesses and requested clarifications

1. **Baseline tuning and fairness.** CurCon receives a per-dataset grid search over learning rate, temperature, and curriculum length, whereas the baselines use hyperparameters reported in their original papers. This may disadvantage the baselines. Ideally, all methods should receive comparable validation-based tuning, or the paper should report a sensitivity analysis showing that the conclusions are robust to reasonable baseline tuning.

2. **Statistical significance.** Results are averaged over five seeds, but no paired significance tests or confidence intervals for the differences are reported. Given that some gains are relatively small, especially at 1,000 labels, significance testing would strengthen the claims.

3. **Curriculum definition could be more precise.** The schedule specifies when operators become available, but it is not fully clear whether the probability distribution over available operators is uniform at every stage or whether the availability probabilities themselves vary continuously with \(c(t)\). The implementation should state this explicitly.

4. **Comparison to alternative schedules.** The reversed curriculum and fixed-mixture ablations are useful, but comparisons with a nonlinear schedule, a random schedule, or a schedule matched for the same expected augmentation strength would provide a stronger test that ordering—not merely augmentation exposure—causes the improvement.

5. **Reproducibility details.** The paper would benefit from reporting exact dataset split procedures, preprocessing, maximum sequence length, augmentation failure handling, translation model details, and the number of examples used for contrastive training. Releasing code and fixed sampled splits would further improve reproducibility.

6. **Scope of evaluation.** The experiments cover only English, relatively short texts, and BERT-base. The limitations acknowledge this appropriately, but claims should remain scoped to this setting.

These issues are primarily about strengthening experimental validation and reproducibility rather than undermining the central result. The reported ablations and low-resource trends provide credible evidence that the curriculum schedule is useful.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 84/100 |
| Novelty | 78/100 |
| Significance | 82/100 |
| Clarity | 88/100 |

### Final average

\[
\frac{84 + 78 + 82 + 88}{4} = 83.0
\]

## Final recommendation: **Accept**

The paper presents a clear and empirically effective method for low-resource text classification. Although stronger baseline tuning, statistical testing, and implementation details would improve the work, the method is simple, well motivated, and supported by consistent results and informative ablations. These are addressable weaknesses, and the paper merits acceptance.