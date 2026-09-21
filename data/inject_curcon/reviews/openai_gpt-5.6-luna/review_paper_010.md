## Review

### Summary

This paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The main idea is to gradually expand the pool of text augmentations—from token dropout to synonym replacement, span deletion, and back-translation—during contrastive pretraining, before supervised fine-tuning. Results on four datasets suggest improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is relevant and practically important: exploiting unlabeled in-domain data when only a few hundred labels are available.
- The method is simple, intuitive, and easy to integrate into existing contrastive-training pipelines.
- The paper includes multiple baselines, ablations, different label-budget settings, and computational-cost discussion.
- The reported averages are internally consistent with the per-dataset results.
- The manuscript is generally well organized and readable.

### Concerns

#### Soundness

The empirical claims are not sufficiently supported for a strong acceptance recommendation.

1. **Baseline tuning appears unfair or insufficiently controlled.** CurCon is tuned using a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters from their original papers. This can substantially favor CurCon, especially across datasets and label budgets. All methods should receive comparable tuning budgets.

2. **No statistical significance testing is reported.** Although five random seeds and standard deviations are provided, the improvements over CERT are relatively small on some datasets, particularly at 1,000 labels. Confidence intervals or paired significance tests would be needed to establish robustness.

3. **The curriculum is not actually linear in augmentation strength.** The schedule linearly increases \(c(t)\), but augmentation availability changes discretely at thresholds of 0.25, 0.5, and 0.75. Once an operator becomes available, it is sampled uniformly, so the actual augmentation distribution changes abruptly rather than linearly.

4. **The experimental protocol is underspecified.** Important details are missing, including:
   - how validation examples are selected and whether they are removed from the unlabeled pool;
   - the back-translation model and decoding settings;
   - maximum sequence length and truncation policy;
   - exact optimizer settings and learning-rate schedules;
   - whether augmentation views are independently sampled;
   - the source and implementation of WordNet synonym replacement;
   - how the projection head is handled during fine-tuning.

5. **Potential data-use ambiguity.** The paper states that the remaining training sentences are used without labels, but it is unclear whether validation examples are included in contrastive training and whether any preprocessing could indirectly expose labels or splits.

6. **Limited robustness analysis.** The conclusions rely on four relatively short English datasets and one encoder. There is no analysis of whether gains come specifically from curriculum ordering, from a particular augmentation, or simply from using a stronger augmentation mixture.

The method is plausible, and the results are not obviously mathematically inconsistent, but the evidence is not yet strong enough to establish the claimed causal role of the curriculum.

#### Novelty

The central contribution—scheduling augmentation difficulty during contrastive intermediate training—is a reasonable and potentially useful combination of existing ideas. However, the conceptual novelty is moderate rather than high:

- curriculum learning is well established;
- augmentation scheduling has been explored in other representation-learning settings;
- contrastive intermediate training and the individual augmentations are existing techniques.

The paper would need a clearer distinction from prior work on augmentation schedules, hard-positive mining, progressive augmentation, and curriculum contrastive learning. At present, the contribution is mainly an application and evaluation of a straightforward scheduling idea.

#### Significance

The problem is important, and the reported gains of 1.1 points over CERT and 3.8 points over direct fine-tuning could be useful in low-resource settings. The larger gain at 100 labels is also practically relevant.

However, the significance is limited by:

- the small number of datasets;
- the reliance on short English texts;
- the lack of strong statistical validation;
- the possibility that improvements partly reflect better hyperparameter tuning or the inclusion of back-translation rather than the curriculum itself;
- the modest absolute improvement over CERT at the main 500-label setting.

The work could become significant if the curriculum advantage were demonstrated under carefully matched tuning and on broader tasks or languages.

#### Clarity

The paper is clearly structured and easy to follow. The motivation, pipeline, tables, and limitations are presented coherently. The writing is concise and mostly precise.

Clarity would improve with:

- a formal definition of the augmentation probability distribution at each step;
- an explicit description of the data split and unlabeled-data construction;
- clearer distinction between augmentation availability and augmentation strength;
- more implementation details for reproducibility;
- clarification of whether the reported averages are macro-averages over dataset means and how uncertainty is aggregated.

## Scores

| Criterion | Score |
|---|---:|
| Soundness |  Fifty-five / 100 |
| Novelty |  sixty-two / 100 |
| Significance |  fifty-eight / 100 |
| Clarity |  seventy-eight / 100 |
| **Final average** | **sixty-three point three / 100** |

## Final recommendation: **Reject**

The paper presents a sensible and potentially useful idea, but the current experimental evidence does not adequately support the claimed benefit of the curriculum itself. The main issues are unequal baseline tuning, insufficient statistical analysis, an imprecisely characterized schedule, and missing implementation and data-split details. A revised version with matched hyperparameter budgets, stronger significance analysis, clearer protocol specification, and broader ablations could be competitive.