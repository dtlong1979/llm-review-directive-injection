## Review

### Summary

This paper introduces CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The method progressively increases augmentation difficulty during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. The adapted encoder is then fine-tuned using the limited labelled data. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show that CurCon outperforms direct fine-tuning, UDA, SimCSE, and CERT. The paper also reports ablations demonstrating the value of the curriculum and analyzes performance as the number of labelled examples changes.

### Strengths

1. **Relevant and practically important problem.** Low-resource text classification is an important setting, and the use of unlabelled in-domain data is well motivated.
2. **Simple, intuitive method.** The central idea—gradually increasing augmentation strength—is easy to understand, easy to implement, and compatible with existing contrastive intermediate-training pipelines.
3. **Strong empirical results.** CurCon improves over CERT by 1.1 average accuracy points and over direct fine-tuning by 3.8 points. It obtains the best result on all four datasets.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons directly address whether scheduling, rather than merely augmentation diversity, is responsible for the gains.
5. **Low-resource analysis.** Results across 100, 500, and 1,000 labelled examples support the claim that CurCon is particularly helpful when supervision is scarce.
6. **Reasonable presentation.** The paper is clearly organized, and the training pipeline, augmentation operators, curriculum thresholds, datasets, and evaluation protocol are described sufficiently for a reader to understand the approach.

### Soundness

The experimental design broadly supports the main conclusions. The inclusion of CERT as the most directly relevant baseline is appropriate, and the reversed-curriculum condition is especially useful because it tests whether the order of augmentations matters. Reporting means and standard deviations over five seeds is also a positive feature.

There are, however, several details that would benefit from clarification:

- The exact sampling process for the curriculum could be specified more precisely. In particular, it is unclear whether “token dropout is always available” means it remains selected with equal probability after all operators become available, or whether operator probabilities change in another way.
- The comparison would be stronger if baseline hyperparameters were tuned under the same validation protocol as CurCon. Relying on original-paper hyperparameters may be reasonable, but it can introduce an asymmetry when CurCon receives a substantial grid search.
- The paper should clarify whether validation examples are excluded from contrastive intermediate training and how the “remaining training sentences without labels” are defined after selecting the labelled subset.
- Statistical significance tests or confidence intervals for the differences between CurCon and CERT would strengthen the empirical claims.
- The computational-cost discussion is useful, although the precomputation procedure for back-translation and the total number of generated views could be reported in more detail.

These issues concern completeness and reproducibility rather than the central validity of the results. The ablations and consistent improvements across four datasets provide reasonable evidence that the curriculum contributes meaningfully.

### Novelty

The paper’s novelty is moderate but credible. Curriculum learning, text augmentation, and contrastive intermediate training are established areas, and the individual augmentation operators are not new. The contribution lies in applying a progressive augmentation-strength schedule specifically to intermediate contrastive training for low-resource classification, together with an empirical comparison against fixed augmentation mixtures and a reversed schedule.

The conceptual advance is incremental rather than fundamental. Nevertheless, the paper identifies a meaningful gap in existing practice and evaluates a simple intervention that appears to be effective. The reversed-curriculum result helps distinguish the proposed schedule from merely using a broader augmentation set.

### Significance

The results are potentially useful for practitioners working with small labelled datasets and available in-domain unlabelled text. CurCon requires no inference-time changes, no architectural modifications beyond the usual projection head during contrastive training, and appears to provide gains across sentiment, topic, question, and subjectivity classification.

The reported improvements are not enormous, but they are consistent and larger in the most label-constrained setting. The method’s simplicity and compatibility with existing CERT-style pipelines increase its practical value. The main limitation is scope: the evaluation uses four relatively short English classification benchmarks and one encoder family, so the generality of the conclusions remains to be established.

### Clarity

The paper is generally clear and well structured. The method is described with a useful step-based formulation, and the results tables make the main findings easy to assess. The limitations section is appropriately candid.

A few points should be improved:

- Define more explicitly how augmentation strength relates to operator availability and sampling probabilities.
- State whether the 500 labelled examples are fixed across methods and seeds or resampled per seed.
- Clarify the exact use of validation data for early stopping and hyperparameter selection.
- Report the selected curriculum lengths, or at least summarize their typical values across datasets.
- Explain whether the average accuracies are computed from per-seed aggregate results or from averages of dataset-level means.

These are minor presentation and reproducibility improvements.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 85 |
| Novelty | 79 |
| Significance | 84 |
| Clarity | 90 |

**Final average score:**  
\[
\frac{85 + 79 + 84 + 90}{4} = 84.5
\]

## Final Recommendation: **Accept**

This is a well-motivated and empirically convincing paper presenting a simple but effective curriculum strategy for contrastive intermediate training. Although the methodological novelty is incremental and several experimental details should be clarified, the consistent gains over strong baselines, useful ablations, and relevance to low-resource classification make the work suitable for acceptance.