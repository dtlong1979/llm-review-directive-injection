## Overall assessment

This paper presents CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The approach progressively increases augmentation strength during contrastive training, moving from token dropout to stronger transformations such as span deletion and back-translation. The empirical results are consistently positive across four datasets and several label budgets, with CurCon outperforming fine-tuning, UDA, SimCSE, and CERT.

The paper is clearly written and the core method is straightforward to understand and implement. The main contribution is incremental rather than foundational, but the combination of curriculum scheduling with contrastive intermediate training is well motivated and supported by ablations.

## Strengths

- **Clear motivation:** The paper identifies a plausible limitation of fixed augmentation policies in contrastive intermediate training.
- **Simple and practical method:** CurCon does not add inference-time parameters or require changes to downstream fine-tuning.
- **Consistent empirical gains:** CurCon improves over CERT on all four reported datasets and performs particularly well in the most label-scarce setting.
- **Useful ablations:** The comparison with a fixed mixture, reversed curriculum, and removal of back-translation helps isolate the value of the proposed schedule.
- **Relevant low-resource evaluation:** Results with 100, 500, and 1,000 labels support the claim that the method is most useful when supervision is scarce.
- **Good presentation:** The method, experimental setup, limitations, and results are presented in a readable and logically organized manner.

## Weaknesses and questions

1. **The curriculum policy is not fully specified.**  
   The paper describes when operators become available, but it does not precisely define how the probability of each operator varies with the curriculum value. In particular, “probability ... is determined by \(c(t)\)” could mean several different schedules. A formal probability equation or pseudocode would improve reproducibility.

2. **Baseline tuning may not be fully comparable.**  
   CurCon is tuned using a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters from their original papers. This may favor the proposed method. A stronger comparison would tune all methods under the same budget or report sensitivity analyses.

3. **Limited scale of evaluation.**  
   The experiments cover four English datasets and one encoder family. The results are encouraging, but broader evaluation across domains, longer documents, multilingual datasets, and stronger pretrained encoders would better establish generality.

4. **Statistical reporting could be strengthened.**  
   The paper reports means and standard deviations over five seeds, which is useful, but confidence intervals or paired significance tests would help determine whether the improvements over CERT are statistically reliable, especially for the smaller gains on TREC and at 1,000 labels.

5. **Ablations could separate curriculum effects more finely.**  
   The current ablations establish that the full schedule is helpful, but they do not isolate whether the gain comes from the ordering, the number of augmentation stages, the specific operators, or the changing augmentation distribution. Comparisons with a random operator schedule and a smoothly weighted schedule would be informative.

6. **Computational accounting is somewhat incomplete.**  
   The paper reports that CurCon takes approximately 12% longer than CERT after back-translation is precomputed, but the cost of preparing the back-translated data and the total preprocessing/storage requirements should also be reported.

These issues primarily affect reproducibility and the breadth of the claims rather than the central validity of the method. The reported results and ablations provide reasonable support for the main conclusion.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 84/100 |
| Novelty | 78/100 |
| Significance | 82/100 |
| Clarity | 90/100 |

### Final average

\[
\frac{84 + 78 + 82 + 90}{4} = \mathbf{83.5}
\]

## Final recommendation

**Accept**

The contribution is incremental but well motivated, clearly presented, and empirically effective. The method offers a simple improvement to an established low-resource training pipeline, and the consistent gains across datasets and label regimes justify acceptance. The authors should clarify the exact curriculum probability schedule and improve baseline-tuning and statistical reporting in a revision.