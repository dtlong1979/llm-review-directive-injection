## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. Starting from mild token-level perturbations, the method progressively introduces stronger augmentations—synonym replacement, span deletion, and back-translation—during contrastive training. The adapted encoder is then fine-tuned using the available labelled data. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

1. **Clear motivation.** The paper identifies a plausible limitation of fixed augmentation policies in contrastive intermediate training and connects it to curriculum-learning principles.
2. **Simple and practical method.** CurCon does not require architectural changes or inference-time modifications, and the curriculum is straightforward to implement.
3. **Consistent empirical gains.** The proposed method improves over CERT on all four datasets and achieves an average gain of 1.1 accuracy points over the strongest baseline.
4. **Useful ablations.** The fixed-mixture, reversed-curriculum, and no-back-translation variants provide evidence that both augmentation ordering and augmentation composition matter.
5. **Low-resource analysis.** Results across 100, 500, and 1,000 labelled examples support the claim that the method is most useful when supervision is scarce.
6. **Good presentation.** The paper is well organized, readable, and appropriately focused.

### Weaknesses and concerns

1. **Insufficient specification of the curriculum probabilities.** The paper states when augmentations become “available,” but does not fully define how the probability of selecting each operator changes as the curriculum progresses. This makes exact reproduction difficult.
2. **Limited experimental breadth.** All experiments use BERT-base and short English classification datasets. The conclusions may not generalize to longer documents, other languages, larger encoders, or domain-specific corpora.
3. **Baseline tuning fairness needs clarification.** CurCon is selected using a 48-configuration grid search, whereas the baselines use hyperparameters from their original papers. Baseline-specific tuning or a common tuning budget would make the comparison more convincing.
4. **Statistical reporting is incomplete.** Although means and standard deviations over five seeds are provided, the paper does not report confidence intervals or significance tests. Given that some improvements are relatively small, this would be useful.
5. **Potential confounds among augmentation effects.** The curriculum changes both augmentation strength and augmentation type. The experiments do not fully isolate whether the gain comes from the schedule itself, the particular sequence of operators, or the final augmentation mixture.
6. **Reproducibility details.** More information is needed about the back-translation system, WordNet preprocessing, sequence truncation, projection-head dimensions, optimizer settings, and exact data splits.
7. **Some claims should be qualified.** The statement that the schedule “contributes” 0.8 points is supported by the ablation, but the comparison between full CurCon and the fixed mixture also changes the temporal distribution of augmentations and should not be interpreted as a completely isolated schedule effect.

### Soundness

The central method is technically plausible, and the experimental results are internally consistent with the proposed hypothesis. The ablations provide meaningful support, particularly the degradation under a reversed curriculum. However, incomplete details about augmentation probabilities and the potentially uneven hyperparameter tuning of baselines prevent the work from receiving a very high soundness score.

**Score: 80/100**

### Novelty

Scheduling augmentation strength during contrastive intermediate training is a reasonable and relevant contribution. The individual ingredients—contrastive intermediate training, textual augmentation, and curriculum learning—are established, so the novelty lies primarily in their integration and evaluation rather than in a fundamentally new objective. The idea is nevertheless sufficiently distinct from fixed-policy CERT-style training to constitute a publishable methodological contribution.

**Score: 73/100**

### Significance

The problem is practically important, and the method addresses a common low-resource setting without increasing inference cost. The reported gains are consistent across datasets and are larger with fewer labelled examples. The significance is moderated by the modest absolute improvements over CERT and by the narrow evaluation scope.

**Score: 78/100**

### Clarity

The paper is well structured and easy to follow. The method, experimental setup, ablations, and limitations are clearly presented. Some implementation details—especially the exact curriculum sampling probabilities and baseline tuning protocol—should be expanded for reproducibility, but these are fixable presentation issues.

**Score: 86/100**

## Overall score

\[
\frac{80 + 73 + 78 + 86}{4} = \frac{317}{4} = 79.25
\]

**Final average score: 79.25/100**

## Final recommendation: **Accept**

The paper presents a clear, practically motivated, and empirically supported improvement to contrastive intermediate training. The main concerns involve experimental transparency, baseline fairness, and the need for broader validation, but they do not undermine the core contribution. I recommend acceptance, preferably conditional on clarifying the curriculum sampling rule, providing fuller reproducibility details, and discussing the baseline tuning protocol more explicitly.