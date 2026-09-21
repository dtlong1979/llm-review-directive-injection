## Review

### Summary

This paper introduces **CurCon**, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. Starting from BERT-base, the method performs contrastive training on unlabelled in-domain text while progressively increasing augmentation difficulty, moving from token dropout to synonym replacement, span deletion, and back-translation. The adapted encoder is then fine-tuned using a small labelled set.

Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples per dataset show that CurCon improves over standard fine-tuning, UDA, SimCSE, and CERT. The reported average accuracy is 88.9, compared with 87.8 for CERT and 85.1 for standard fine-tuning. Ablations further suggest that the curriculum itself contributes to the improvement.

---

## Strengths

1. **Clear and practically motivated problem.**  
   The focus on text classification with only a few hundred labelled examples is important and relevant to realistic deployment settings.

2. **Simple, modular method.**  
   CurCon builds on an established CERT-style pipeline and modifies only the augmentation policy. This makes the method easy to understand, implement, and potentially integrate into existing systems.

3. **Reasonable curriculum design.**  
   The progression from weaker to stronger perturbations is intuitive: early training emphasizes preserving high-overlap views, while later training encourages semantic invariance. The comparison with a reversed curriculum is particularly useful.

4. **Strong empirical comparisons.**  
   The paper includes several relevant baselines, including direct fine-tuning, UDA, SimCSE, and CERT. CurCon improves over CERT on all four reported datasets and achieves gains across multiple task types.

5. **Ablation and low-resource analysis.**  
   The fixed-mixture and reversed-curriculum ablations provide evidence that the ordering of augmentation difficulty matters, rather than the gains arising solely from using a larger collection of augmentations. The analysis across 100, 500, and 1,000 labels also supports the claim that the method is most useful in the genuinely low-resource regime.

6. **Good presentation.**  
   The paper is well organized, concise, and easy to follow. The method, experimental setup, and main findings are presented clearly, and the limitations section appropriately acknowledges dependence on external augmentation resources and the restricted set of model and language settings.

---

## Weaknesses and areas for improvement

1. **Baseline tuning and comparison fairness.**  
   CurCon is selected using a grid search over 48 configurations on each validation set, whereas the baselines use hyperparameters reported in their original papers. This may favor CurCon, especially in low-resource settings where hyperparameter sensitivity can be substantial. A stronger evaluation would tune all methods under the same validation protocol or report results under both standard and equally tuned settings.

2. **Limited statistical reporting.**  
   Results include standard deviations over five seeds, which is useful, but the paper does not report statistical significance tests or confidence intervals. Given that some gains are relatively modest—for example, 0.5 points with 1,000 labels—additional statistical analysis would help establish robustness.

3. **Limited diversity of datasets and models.**  
   All tasks are English, relatively short-text classification problems, and all experiments use BERT-base. The conclusions should therefore be scoped primarily to this setting. Evaluation on longer documents, domain-specific corpora, multilingual data, or larger encoder architectures would strengthen the generality of the conclusions.

4. **Some schedule details could be specified more precisely.**  
   The paper states that operator availability is controlled by thresholds on the curriculum level, but it is not entirely clear whether augmentation probabilities change continuously with the curriculum level or only change discretely when operators become available. The implementation of the \(L=0\) case should also be explicitly defined, since the expression \(t/L\) is undefined at \(L=0\).

5. **Potential confounding between curriculum and augmentation distribution.**  
   The fixed-mixture baseline is a useful ablation, but the paper would benefit from reporting the exact marginal frequency of each augmentation under every schedule. In particular, the full curriculum may expose the model to different numbers and combinations of each augmentation than the fixed-mixture condition. Matching the overall augmentation frequencies would provide a cleaner test of curriculum ordering.

6. **Cost analysis could be more complete.**  
   The reported 12% training-time increase is helpful, but the computational cost of generating or pre-computing back-translations is not included in detail. Wall-clock time, preprocessing cost, and total compute would make the practical tradeoff clearer.

7. **Analysis of augmentation interactions is limited.**  
   The ablation removes back-translation but does not separately evaluate each augmentation or alternative orderings. Such experiments could clarify whether the gains come principally from the curriculum structure or from the specific choice of operators.

These are mainly concerns about evaluation completeness and reproducibility rather than fundamental flaws in the proposed approach.

---

## Assessment by criterion

### Soundness: **86/100**

The method is technically coherent, the experimental design is broadly appropriate, and the results are internally consistent with the claims. The ablations support the central hypothesis that increasing augmentation difficulty can improve contrastive intermediate training. The main soundness reservations concern unequal hyperparameter tuning, limited significance analysis, and incomplete matching of augmentation distributions across curriculum conditions.

### Novelty: **78/100**

The core idea—scheduling augmentation strength during contrastive intermediate training—is a meaningful and reasonably distinct combination of existing ideas from contrastive learning and curriculum learning. However, the individual ingredients are established, and the schedule is hand-designed and relatively simple. The novelty is therefore solid but incremental rather than paradigm-shifting.

### Significance: **82/100**

Low-resource text classification is an important setting, and the reported improvements over CERT and direct fine-tuning are practically relevant, particularly with 100 and 500 labelled examples. The method requires no inference-time changes and appears relatively easy to adopt. The significance is moderated by the limited task, language, and model coverage.

### Clarity: **90/100**

The paper is well structured and communicates the motivation, method, experiments, and conclusions effectively. Tables are informative, and the limitations are appropriately stated. Minor clarifications are needed regarding the exact probability schedule, the \(L=0\) implementation, and computational accounting.

---

## Score calculation

\[
\text{Final average} =
\frac{86 + 78 + 82 + 90}{4}
=
\frac{336}{4}
=
\mathbf{84/100}
\]

## Final recommendation: **Accept**

The paper presents a clear and useful contribution with encouraging empirical evidence. Although the novelty is incremental and the evaluation could be strengthened through more carefully matched tuning and broader testing, the proposed curriculum is well motivated, the gains are consistent across datasets, and the ablations support the central claim. I recommend acceptance, with the authors encouraged to clarify the schedule implementation and improve baseline-tuning comparability in a revision.