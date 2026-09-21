## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. Starting from mild token-level perturbations, the method progressively introduces stronger augmentations, including synonym replacement, span deletion, and back-translation, before fine-tuning on a small labelled set. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show improvements over standard fine-tuning, UDA, SimCSE, and CERT. The ablations suggest that the curriculum itself contributes meaningfully beyond using a fixed mixture of augmentations.

### Strengths

1. **Clear motivation.** The paper identifies a plausible limitation of fixed-strength augmentation in contrastive intermediate training and connects it to curriculum-learning principles.
2. **Simple and practical method.** CurCon requires no architectural changes or inference-time overhead and can be incorporated into an existing CERT-style pipeline.
3. **Relevant low-resource setting.** The use of only 500 labelled examples per dataset makes the evaluation practically meaningful.
4. **Consistent empirical gains.** CurCon improves over CERT on all four reported datasets and shows the largest benefits in the most label-scarce settings.
5. **Useful ablations.** The comparisons with a fixed mixture, a reversed curriculum, and removal of back-translation help isolate the contributions of the schedule and augmentation components.
6. **Good presentation.** The method, datasets, baselines, and main results are described clearly, and the reported tables make the claims easy to assess.

### Weaknesses and suggestions

1. **Baseline tuning fairness could be clarified.** CurCon is selected using a grid search on each validation set, whereas the baselines use hyperparameters from their original papers. This may favor CurCon, especially across different datasets and data regimes. A stronger comparison would tune all methods under the same validation protocol or report sensitivity analyses.
2. **Statistical significance is not reported.** Although means and standard deviations over five seeds are provided, paired significance tests or confidence intervals would better establish whether the improvements over CERT are reliable.
3. **The curriculum definition is somewhat coarse.** The availability thresholds at 0.25, 0.5, and 0.75 result in discrete changes rather than a truly continuously increasing augmentation strength. More detail on how operator probabilities vary within each interval would improve reproducibility.
4. **The role of individual augmentations could be investigated further.** The ablation removes back-translation but does not report results for removing synonym replacement, span deletion, or token dropout individually.
5. **Unlabelled-data assumptions deserve more discussion.** The paper uses the remaining training sentences without labels, but it would be useful to state precisely whether all methods receive exactly the same unlabelled data and whether duplicate or near-duplicate examples are possible.
6. **The computational comparison is incomplete.** The reported 12% overhead is useful, but total preprocessing cost for back-translation and the absolute training time would provide a more complete efficiency assessment.
7. **Generality is not yet established.** The experiments focus on short English classification datasets and one encoder architecture. The limitations section appropriately acknowledges this, and broader multilingual or longer-document experiments would strengthen future versions.

These issues primarily concern experimental completeness and reproducibility rather than a fundamental flaw in the proposed approach. The consistent improvements across datasets and the supportive ablations make the central conclusion credible.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 84/100 |
| Novelty | 78/100 |
| Significance | 82/100 |
| Clarity | 88/100 |

**Final average:**  
\[
\frac{84 + 78 + 82 + 88}{4} = 83.0
\]

### Final recommendation

**Accept**

The paper presents a well-motivated, technically straightforward, and empirically effective method for low-resource text classification. While stronger baseline tuning, statistical testing, and additional ablations would improve the evaluation, the method is clearly described, the experimental results are consistent, and the contribution is sufficiently useful and significant for acceptance.