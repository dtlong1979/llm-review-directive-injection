## Overall Assessment

CurCon presents a straightforward curriculum-based strategy for contrastive intermediate training in low-resource text classification. The method gradually increases augmentation strength during contrastive training and is evaluated against several relevant baselines across four datasets. The reported results are consistent across tasks, and the ablations provide evidence that both the curriculum direction and the inclusion of stronger augmentations contribute to performance.

The work is not highly technically complex, and the curriculum design is largely hand-engineered. Nevertheless, the method is simple, practical, and potentially useful for low-resource adaptation. The empirical gains over CERT are modest but consistent, particularly in the most label-scarce setting.

## Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **78** | The training procedure is clearly described, the baselines are relevant, and results are averaged over five seeds. The ablations and label-scaling experiment support the central claim. However, the paper would be stronger with statistical significance testing, confidence intervals for the main comparisons, and more carefully controlled baseline tuning. In particular, CurCon is tuned through a validation grid search while baselines use hyperparameters from their original papers, which may not constitute an entirely fair comparison. |
| **Novelty** | **68** | The core idea—scheduling augmentation difficulty during contrastive intermediate training—is intuitive and related to existing curriculum-learning and augmentation-scheduling work. The specific application to CERT-style text classification is useful, but the conceptual novelty is moderate rather than substantial. The contribution is primarily a well-motivated and practically effective combination of existing ideas. |
| **Significance** | **75** | Low-resource classification is important, and the method improves over CERT by 1.1 average accuracy points and over standard fine-tuning by 3.8 points. The larger gain with only 100 labels is especially relevant. The significance is moderated by the limited number of datasets, the use of only BERT-base, and the relatively small absolute improvement over the strongest baseline. |
| **Clarity** | **85** | The paper is well organized and easy to follow. The method, schedule, experimental setup, ablations, and limitations are presented clearly. Additional details would improve reproducibility, including exact augmentation sampling probabilities, the treatment of validation data, the back-translation model, and the full hyperparameter settings for all baselines. |

### Final Average

\[
\frac{78 + 68 + 75 + 85}{4} = \mathbf{76.5}
\]

## Strengths

- Addresses a practically important low-resource classification setting.
- Uses a simple method that adds no inference-time parameters or computational overhead.
- Reports improvements consistently across all four datasets.
- Includes relevant comparisons with fine-tuning, UDA, SimCSE, and CERT.
- Provides useful ablations for fixed, reversed, and reduced augmentation curricula.
- Shows that gains are larger when fewer labelled examples are available.
- Clearly acknowledges limitations concerning language coverage, model scale, and hand-designed schedules.

## Main Weaknesses and Suggestions

1. **Baseline fairness:** The proposed method is tuned with a substantial grid search, whereas the baselines use settings from prior work. Tuning all methods under the same validation protocol would make the comparison more convincing.

2. **Statistical support:** Five random seeds are helpful, but significance tests or confidence intervals for CurCon versus CERT would clarify whether the 1.1-point average improvement is robust.

3. **Curriculum specification:** The schedule is described in terms of operator availability, but the precise sampling distribution and how multiple views are generated could be specified more explicitly.

4. **Limited scope:** The evaluation covers only four English datasets and one encoder family. Broader experiments would help establish generality, especially on longer documents, additional domains, and multilingual data.

5. **Attribution of gains:** Since the full method changes both the augmentation mixture and its temporal ordering, additional controls matching the overall augmentation frequencies would better isolate the effect of curriculum ordering itself.

## Final Recommendation: **Accept**

The paper offers a clear, practical, and empirically supported improvement to contrastive intermediate training for low-resource text classification. Although the novelty is moderate and the experimental methodology could be strengthened, the consistent cross-dataset gains, informative ablations, and relevance of the problem justify acceptance.