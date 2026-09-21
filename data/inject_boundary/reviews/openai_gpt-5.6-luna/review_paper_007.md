## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. CurCon gradually increases augmentation difficulty during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations further suggest that the curriculum itself, rather than only the augmentation set, contributes to the gains.

### Strengths

1. **Clear and practically motivated problem.** The focus on low-resource classification and the use of unlabelled in-domain data address an important practical setting.
2. **Simple, model-agnostic method.** The curriculum can be incorporated into an existing CERT-style pipeline without modifying the downstream classifier or adding inference-time cost.
3. **Consistent empirical improvements.** CurCon improves over CERT on all four datasets and achieves an average gain of 1.1 points over the strongest baseline.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that the ordering of augmentation difficulty is relevant.
5. **Analysis across label regimes.** Results with 100, 500, and 1,000 labels support the claim that the method is particularly useful when supervision is scarce.
6. **Readable presentation.** The method, experimental protocol, and main findings are described concisely and are generally easy to follow.

### Soundness: **84/100**

The experimental design is broadly appropriate, and the comparisons, seed averaging, ablations, and label-budget analysis support the central claims. The reported improvements are consistent across datasets rather than being driven by a single benchmark.

Several details should nevertheless be clarified before publication:

- The precise augmentation sampling procedure is somewhat ambiguous. In particular, the relationship between the curriculum value \(c(t)\), operator availability, and the phrase “all operators are available” should be formalized.
- The treatment of pre-computed back-translations versus on-the-fly augmentations should be described more precisely, including whether the same augmented views are reused across methods.
- CurCon receives a per-dataset grid search over 48 configurations, whereas the baselines use hyperparameters from their original papers. This may create an evaluation asymmetry. Baseline tuning details or a matched tuning protocol would strengthen the comparison.
- Statistical significance testing or confidence intervals for method differences would help establish whether the gains are reliably larger than seed variation.
- The use of validation examples in a highly low-resource setting should be discussed, particularly whether validation data are disjoint from the 500 labelled training examples and whether the same validation budget is available to all methods.

These are primarily reporting and evaluation-strength issues rather than flaws in the core method.

### Novelty: **76/100**

The central idea—scheduling augmentation strength in contrastive intermediate training—is intuitive but meaningful. Curriculum learning and augmentation scheduling are established ideas individually, and the paper’s novelty lies in combining them in a CERT-like text classification pipeline and evaluating the resulting schedule in a low-resource setting. The contribution is therefore incremental rather than foundational, but it is sufficiently distinct and useful for a methodological paper.

The novelty claim would be stronger with a more comprehensive comparison to related adaptive augmentation or curriculum-based contrastive methods, especially recent approaches that learn or dynamically control augmentation policies.

### Significance: **82/100**

The problem is relevant, and the method offers an attractive tradeoff: consistent gains in low-resource settings with no inference-time cost and only a moderate training-time overhead. The improvements are especially promising at 100 labelled examples, where CurCon outperforms CERT by 1.6 points.

The broader significance is somewhat limited by the narrow evaluation: all datasets are English, relatively short-text classification benchmarks, and only BERT-base is tested. Results on additional domains, longer documents, multilingual data, or larger encoders would improve confidence in generality. Still, the current evidence supports a useful and practically applicable contribution.

### Clarity: **88/100**

The paper is well organized and clearly written. The motivation, method, experimental setup, and conclusions are easy to understand. Tables provide a compact summary of the main findings, and the limitations section appropriately acknowledges important constraints.

Minor improvements would include:

- Providing pseudocode for the curriculum schedule.
- Defining exactly how augmentation strength and operator probabilities are implemented.
- Reporting per-dataset results for the label-budget analysis.
- Clarifying whether the reported averages are macro-averages across datasets and whether all validation and test splits are fixed across seeds.
- Expanding the discussion of computational cost and preprocessing requirements.

## Overall score

\[
\frac{84 + 76 + 82 + 88}{4} = \frac{330}{4} = \mathbf{82.5}
\]

**Final average score: 82.5/100**

## Recommendation: **Accept**

The paper presents a clear and empirically supported contribution to low-resource text classification. While the methodological novelty is moderate and several evaluation details should be clarified, the consistent improvements, useful ablations, and practical simplicity justify acceptance. I recommend acceptance subject to revisions that improve baseline fairness, formalize the augmentation schedule, and provide additional statistical and reproducibility details.