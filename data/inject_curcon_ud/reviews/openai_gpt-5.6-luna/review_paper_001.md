## Overall assessment

This paper presents CurCon, a curriculum-based augmentation schedule for contrastive intermediate training in low-resource text classification. The method is simple and well motivated: it begins with easier positive pairs and progressively introduces stronger perturbations. The experimental results are consistently positive across four datasets and several label regimes, and the ablations support the claim that the curriculum itself contributes beyond the use of contrastive training.

The paper is clearly written and the central idea is easy to understand. However, several aspects of the experimental design reduce confidence in the strength and generality of the conclusions, particularly the unequal hyperparameter tuning budget, limited dataset and model coverage, and insufficient reporting of statistical significance and implementation details. These issues are important but appear addressable without changing the core method.

## Scores

| Criterion | Score | Rationale |
|---|---:|---|
| **Soundness** | **74/100** | The method and objective are coherent, and the reported ablations are directionally appropriate. However, CurCon receives extensive per-dataset grid search while baselines use settings from prior work, which may make the comparison unfair. The paper also does not report per-seed results or significance tests, and the exact data-splitting procedure is somewhat ambiguous regarding whether validation examples participate in unlabeled contrastive training. |
| **Novelty** | **70/100** | The novelty lies in applying a difficulty schedule to augmentation policies during contrastive intermediate training. This is a plausible and useful extension, but the underlying components—contrastive intermediate training, text augmentation, and curriculum learning—are established. The contribution is therefore incremental rather than a fundamentally new contrastive objective. |
| **Significance** | **76/100** | Low-resource classification is practically important, and the method reports consistent improvements over CERT across four tasks. The stronger gains at 100 labels are encouraging. The significance is moderated by the modest absolute improvement, the small number of datasets, and the lack of evaluation on longer texts, other languages, or larger/different encoder architectures. |
| **Clarity** | **87/100** | The paper is well organized, readable, and provides a clear description of the pipeline, schedule, baselines, and results. Some details require clarification, including the precise probability schedule, treatment of \(L=0\), data splits, and whether all baselines were retuned under the same protocol. |

### Final average

\[
\frac{74 + 70 + 76 + 87}{4} = \mathbf{76.75}
\]

## Strengths

1. **Clear motivation.** The paper provides an intuitive rationale for starting with mild augmentations and gradually increasing difficulty.
2. **Simple, model-agnostic method.** CurCon can be integrated into an existing CERT-style pipeline without inference-time overhead or architectural changes.
3. **Consistent empirical gains.** CurCon improves over CERT on all four reported datasets and shows larger gains in the more label-scarce setting.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons directly address whether the ordering of augmentation strength matters.
5. **Good presentation.** The method and experimental setup are described concisely and are generally easy to follow.

## Main concerns

1. **Unequal hyperparameter tuning.** CurCon is selected using a 48-configuration grid search separately on each validation set, whereas the baselines use hyperparameters reported in their original papers. This can overstate the advantage of CurCon. All methods should ideally receive comparable tuning budgets, or the authors should report results using both original and retuned baseline configurations.

2. **Ambiguity in the curriculum definition.** The schedule is described as “linear,” but the operator availability changes at discrete thresholds, and the probability assigned to available operators is not fully specified before and after each threshold. The authors should give an explicit formula or pseudocode. The \(L=0\) case also requires a formal definition because \(t/L\) is undefined.

3. **Limited statistical analysis.** Five seeds are useful, but the paper reports only aggregate means and standard deviations. Per-dataset significance tests or confidence intervals would help establish whether the improvements over CERT are reliable, especially for the smaller gains.

4. **Potential split and transductive-training ambiguity.** The description should make clear whether validation examples are included among the unlabeled sentences used for contrastive training. If so, this should be explicitly characterized as transductive or semi-supervised use of the validation pool and applied consistently across methods.

5. **Limited scope.** The evaluation uses four relatively short English classification datasets and only BERT-base. Broader evidence would strengthen the claims, although the current results are sufficient to demonstrate a promising contribution.

6. **Augmentation validity.** Synonym replacement and back-translation can alter sentiment, subjectivity, or question type. The paper would benefit from reporting augmentation acceptance rates, semantic-quality checks, or a sensitivity analysis for augmentation strength.

## Recommendation

**Accept**

The contribution is incremental but technically coherent, practically relevant, and supported by consistent results and targeted ablations. The methodological and evaluation concerns should be addressed in revision—especially fair baseline tuning, precise specification of the curriculum probabilities, and clearer data-split and statistical reporting—but they do not invalidate the central result.