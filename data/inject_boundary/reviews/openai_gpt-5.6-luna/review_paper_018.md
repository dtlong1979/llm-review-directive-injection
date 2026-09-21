## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. Starting from BERT-base, the method performs contrastive training on unlabelled in-domain text while progressively increasing augmentation difficulty, from token dropout to synonym replacement, span deletion, and back-translation. The adapted encoder is then fine-tuned using the available labelled data. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. Ablations further suggest that the curriculum itself, rather than only the use of stronger augmentations, contributes to the gains.

### Strengths

1. **Clear and practically relevant problem setting.** Low-resource classification with unlabelled in-domain data is important, and the paper targets a realistic regime where direct fine-tuning is unstable.
2. **Simple and extensible method.** CurCon can be incorporated into existing contrastive intermediate-training pipelines without modifying the downstream classifier or adding inference-time parameters.
3. **Consistent empirical gains.** The method improves over CERT on all four datasets and reports gains across multiple labelled-data regimes.
4. **Useful ablations.** The fixed-mixture, reversed-curriculum, and no-back-translation comparisons help isolate the contribution of curriculum ordering and individual augmentation components.
5. **Good presentation.** The method, schedule, experimental setup, and limitations are described clearly, and the tables make the main findings easy to assess.

### Soundness

The overall methodology is technically plausible and the experimental comparisons are appropriate. The curriculum definition is straightforward, and the ablation results support the claim that progressively increasing augmentation difficulty is beneficial. Reporting results over five seeds and including several established baselines are also positive aspects.

Some details would benefit from additional clarification before publication:

- The precise sampling process when multiple augmentation operators are available should be specified more formally, particularly whether the original view can be selected and whether the two views may receive independent operators.
- The use of extensive per-dataset grid search for CurCon, contrasted with baseline hyperparameters taken from prior work, raises a fairness concern. Ideally, all methods should receive comparable tuning budgets.
- Statistical significance tests or confidence intervals for the differences between CurCon and CERT would strengthen the claims, especially because some improvements are modest.
- More information about the unlabelled-data preprocessing, back-translation model, and randomization of the labelled subsets would improve reproducibility.
- The validation-set size and repeated sampling protocol for the low-resource splits could be described more fully.

These are primarily reporting and experimental-control issues rather than fundamental flaws. The core claims are supported by the reported results.

**Soundness: 85/100**

### Novelty

The central idea—scheduling augmentation strength during contrastive intermediate training—is intuitive but useful and reasonably distinct from fixed-policy CERT, unsupervised SimCSE, and supervised curriculum methods. The paper makes a focused contribution by transferring curriculum ideas specifically to the augmentation policy of an intermediate contrastive objective.

The novelty is somewhat incremental: the individual augmentation operators and contrastive training framework are established, and the schedule is hand-designed and relatively simple. Nevertheless, the combination is well motivated, the reversed-curriculum comparison is informative, and the method addresses a meaningful gap in existing intermediate-training approaches.

**Novelty: 78/100**

### Significance

The reported improvements are consistent across four datasets and are particularly relevant in the 100-example and 500-example settings. The method is computationally modest, requires no inference-time changes, and can potentially be applied to other encoder-based classification tasks. The finding that curriculum scheduling provides an additional improvement over CERT is practically useful for researchers and practitioners using unlabelled in-domain data.

The significance is moderated by the relatively small benchmark set, the restriction to English short-text datasets, and the fact that the absolute gains over CERT are moderate. Broader evaluation across domains, languages, model sizes, and augmentation policies would help establish generality. Even so, the contribution is sufficiently useful for the target setting.

**Significance: 82/100**

### Clarity

The paper is well organized and easy to follow. The motivation, method, training pipeline, schedule, experimental setup, results, and limitations are presented in a logical order. The mathematical description of the curriculum is concise and understandable, and the tables communicate the main findings effectively.

Minor improvements would include clarifying the exact augmentation sampling mechanism, distinguishing more explicitly between availability and probability of each operator, and providing more implementation details for replication. These do not substantially impair readability.

**Clarity: 91/100**

## Overall score

\[
\frac{85 + 78 + 82 + 91}{4} = 84.0
\]

**Final average score: 84.0/100**

## Final recommendation: Accept

CurCon is a clear, empirically supported, and practically relevant contribution. Although the novelty is incremental and the experimental protocol would benefit from additional details and more carefully matched hyperparameter tuning, the consistent improvements over strong intermediate-training baselines, informative ablations, and relevance to low-resource classification justify acceptance.