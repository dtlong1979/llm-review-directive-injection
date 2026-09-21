## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The approach gradually increases augmentation difficulty during contrastive pretraining, moving from token dropout to synonym replacement, span deletion, and back-translation. The encoder is then fine-tuned on a small labelled set. Experiments on SST-2, AG News, TREC, and SUBJ using 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations further suggest that the curriculum itself, rather than contrastive training alone, contributes to the gains.

### Strengths

1. **Clear motivation and practical setting.** The paper targets a realistic low-resource regime and uses unlabelled in-domain text effectively.
2. **Simple and plausible method.** The curriculum is easy to understand and implement, adds no inference-time parameters, and can be incorporated into existing CERT-style pipelines.
3. **Consistent empirical improvements.** CurCon improves over CERT on all four datasets and reports gains across multiple label budgets.
4. **Useful ablations.** Comparisons with a fixed mixture, reversed curriculum, and removal of back-translation help isolate the role of the proposed scheduling strategy.
5. **Good presentation.** The paper is well organized, readable, and provides sufficient high-level detail to understand the training procedure and experimental protocol.

### Weaknesses and concerns

1. **Limited breadth of evaluation.** The experiments cover only four relatively short English classification datasets and a single encoder architecture. Testing on additional domains, longer documents, multilingual data, or larger encoders would strengthen the generality of the conclusions.
2. **Baseline tuning may be asymmetric.** CurCon is selected using a grid search on each validation set, whereas the baselines use hyperparameters reported in their original papers. For a fair comparison, all methods should ideally receive comparable tuning budgets under the same low-resource protocol.
3. **Some methodological details are underspecified.** The exact probability distribution over augmentation operators, the number and type of views, the source and quality of the back-translation system, and the construction of validation splits should be described more precisely.
4. **Statistical analysis is limited.** Results are averaged over five seeds, but the paper does not report confidence intervals or significance tests. Given the relatively modest improvements over CERT, this analysis would help establish robustness.
5. **Potential confounding from augmentation resources.** The gains may partly reflect the use of several strong augmentation operators, particularly back-translation, rather than the curriculum alone. The fixed-mixture ablation addresses this issue to some extent, but matched-compute and operator-specific comparisons would make the attribution stronger.
6. **Compute and reproducibility reporting could be improved.** The paper reports approximate relative cost but does not provide total training time, memory use, or details of the translation model and WordNet preprocessing.

### Soundness

The central method is technically coherent, and the experimental results are consistent with the stated hypothesis. The fixed-mixture and reversed-curriculum ablations provide meaningful evidence that scheduling matters. However, the asymmetric hyperparameter tuning and incomplete implementation details reduce confidence in the strength of the empirical conclusions. The work appears fundamentally sound, but additional controls would improve its rigor.

**Score: 80/100**

### Novelty

The individual ingredients—contrastive intermediate training, text augmentation, and curriculum learning—are established. The main novelty lies in applying a progressively stronger augmentation schedule specifically to contrastive intermediate training for low-resource classification. This is a relatively modest but clear methodological contribution, and the paper distinguishes itself through a simple, interpretable scheduling mechanism and relevant ablations.

**Score: 73/100**

### Significance

The problem is practically important, and the reported improvements are consistent across all four datasets and multiple label budgets. The method is inexpensive to deploy at inference time and could be useful in settings where unlabelled domain text is available. The significance is somewhat limited by the narrow evaluation scope and moderate absolute gains, but the approach is potentially valuable as a general training recipe.

**Score: 78/100**

### Clarity

The paper is well structured and communicates the motivation, method, experiments, and conclusions clearly. Tables are easy to interpret, and the limitations are appropriately acknowledged. Some implementation and evaluation details require clarification, particularly the augmentation sampling probabilities and fairness of baseline tuning, but these issues do not substantially impair readability.

**Score: 88/100**

## Final score

\[
\frac{80 + 73 + 78 + 88}{4} = 79.75
\]

**Final average score: 79.8/100**

## Recommendation: Accept

CurCon presents a clear and practically motivated contribution with consistent empirical improvements and useful ablations. Although the novelty is incremental and the evaluation would benefit from broader coverage and more carefully matched baseline tuning, the method is simple, plausible, and sufficiently supported by the reported results. I recommend **Accept**, ideally contingent on clarifying the augmentation policy, providing stronger statistical analysis, and documenting the experimental setup in greater detail.