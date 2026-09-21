## Review

### Summary

This paper introduces CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method progressively increases augmentation strength during contrastive pre-adaptation, beginning with token dropout and gradually introducing synonym replacement, span deletion, and back-translation. The adapted encoder is then fine-tuned on a small labelled set.

The empirical evaluation covers four standard text-classification benchmarks with 500 labelled examples per dataset and compares CurCon with direct fine-tuning, UDA, SimCSE, and CERT. CurCon reports consistent improvements over all baselines, as well as ablations showing that the curriculum itself contributes beyond using a fixed mixture of augmentations. The paper is well organized, easy to follow, and addresses a practically relevant low-resource setting.

---

## Scores

| Criterion | Score |
|---|---:|
| **Soundness** | **85/100** |
| **Novelty** | **80/100** |
| **Significance** | **85/100** |
| **Clarity** | **92/100** |

### Final average

\[
\frac{85 + 80 + 85 + 92}{4} = \mathbf{85.5}
\]

**Final average score: 85.5/100**

## Recommendation: **Accept**

---

## Detailed assessment

### 1. Soundness — 85/100

The central experimental design is generally sound. The paper compares CurCon against relevant baselines, uses multiple datasets, reports results across five random seeds, and includes ablations for the curriculum, curriculum direction, and back-translation. The reported improvements are consistent across all four datasets rather than being driven by one isolated benchmark. The label-budget analysis also supports the paper’s main motivation: curriculum-based contrastive adaptation appears most useful in the most label-scarce setting.

The method is sufficiently specified at a high level: the augmentation operators, contrastive objective, curriculum thresholds, training duration, and downstream fine-tuning procedure are described. The ablation comparing the full method with a fixed augmentation mixture is particularly important because it isolates the contribution of scheduling rather than merely showing the benefit of additional augmentation.

There are, however, several issues that should be clarified or strengthened:

- The paper reports means and standard deviations but does not provide significance tests or per-seed results. Given that some gains over CERT are relatively modest, especially at 1,000 labelled examples, confidence intervals or paired statistical tests would make the conclusions more robust.
- The baseline hyperparameter treatment is potentially asymmetric. CurCon is selected using a grid search on each validation set, whereas baselines use hyperparameters from their original papers. A fairer comparison would either tune all methods under the same budget or report an additional comparison with carefully re-tuned baselines.
- The curriculum definition is somewhat underspecified. The text says that the probability of applying each operator is determined by the curriculum level, but then describes hard thresholds and uniform sampling among available operators. It should explicitly state whether the schedule changes the operator set only, or also changes individual operator probabilities and perturbation magnitudes.
- The special case \(L=0\) is described informally. Since \(c(t)=\min(1,t/L)\) is undefined at \(L=0\), the fixed-mixture behavior should be stated separately in the formal definition.
- The use of external resources—WordNet and German back-translation—deserves more implementation detail, including the translation model or service, handling of failed translations, and whether all augmented examples are generated with a fixed or stochastic process.
- The validation protocol and the exact construction of the 500-example labelled subsets could be described more fully. In particular, it would be useful to clarify whether the same sampled labelled subsets are used across methods and seeds, and whether validation examples are excluded from contrastive pretraining.

These are mostly reproducibility and evaluation-strength concerns rather than fundamental flaws. The ablations and consistent dataset-level improvements provide reasonable support for the main claim.

### 2. Novelty — 80/100

The paper’s novelty is meaningful but incremental. Curriculum learning, contrastive intermediate training, and text augmentation are all established ideas. The contribution lies in combining them in a simple and targeted way: scheduling augmentation difficulty during contrastive intermediate training for low-resource classification.

The strongest aspect of the novelty is that the schedule is applied specifically to the intermediate contrastive adaptation stage, rather than to supervised example ordering or only to downstream consistency training. The comparison between an easy-to-hard schedule, a fixed mixture, and a reversed schedule gives the proposed design a useful empirical rationale.

That said, the method is relatively straightforward. The schedule is manually designed, linear, and threshold-based, and the paper does not introduce a new contrastive objective or a theoretically novel curriculum formulation. The contribution would be more distinctive if the authors offered a deeper analysis of why the schedule helps—for example, by measuring representation uniformity, alignment, augmentation difficulty, or training dynamics over time—or compared against more alternatives such as continuous probability interpolation, learned schedules, or randomized operator orderings.

Thus, the work represents a solid methodological contribution with practical originality, though not a major conceptual breakthrough.

### 3. Significance — 85/100

The problem is important and realistic. Text classification with only a few hundred labelled examples is common in domain adaptation and specialized applications, and the method is compatible with standard pretrained encoders and downstream fine-tuning procedures. The reported gains are consistent and practically relevant:

- 1.1 points over CERT at 500 labels,
- 3.8 points over direct fine-tuning,
- and 1.6 points over CERT at 100 labels.

The method also adds no inference-time cost and only a moderate reported training-time overhead. These properties improve its practical appeal.

The significance is somewhat limited by the scope of the evaluation. All datasets are English, relatively short-text classification benchmarks, and the experiments use only BERT-base. It is therefore not yet clear whether the conclusions generalize to longer documents, domain-specific corpora, multilingual settings, larger encoders, or substantially different label distributions. In addition, the reported absolute gains, while consistent, are moderate on some datasets.

Nevertheless, the method addresses a clear practical bottleneck, is simple to implement, and produces improvements under a challenging low-resource regime. The contribution is significant enough for acceptance, particularly as a useful empirical method and a basis for further work on adaptive augmentation curricula.

### 4. Clarity — 92/100

The paper is clearly structured and communicates the motivation, method, evaluation, and conclusions effectively. The tables are concise and directly support the claims. The curriculum intuition is easy to understand, and the limitations section appropriately acknowledges the dependence on language resources and the hand-designed schedule.

A few details should be improved for complete reproducibility:

- Define the exact operator sampling probabilities at each curriculum stage.
- State the contrastive batch construction and whether both views are used symmetrically.
- Specify the back-translation system and preprocessing choices.
- Clarify whether the validation examples participate in unsupervised contrastive training.
- Report the actual selected curriculum lengths and other best hyperparameters, or provide sufficient supplementary details to reproduce the grid search.
- Clarify whether “remaining training sentences without labels” includes the held-out validation data.

These are minor presentation and reproducibility improvements. The overall exposition is strong.

---

## Strengths

1. **Clear practical motivation:** The work targets a realistic low-resource regime where direct fine-tuning is unstable.
2. **Simple and deployable method:** CurCon requires no architectural changes and adds no inference cost.
3. **Relevant baselines:** UDA, SimCSE, CERT, and direct fine-tuning provide meaningful comparisons.
4. **Consistent results:** CurCon improves over the baselines on all four datasets.
5. **Useful ablations:** The fixed-mixture and reversed-curriculum comparisons support the claim that the schedule—not only the augmentation set—matters.
6. **Label-budget analysis:** Results at 100, 500, and 1,000 examples align with the proposed motivation.
7. **Appropriate limitations:** The paper candidly discusses language, model-size, and augmentation-resource limitations.

## Main concerns

1. Baseline hyperparameters should ideally be tuned under a comparable budget.
2. The curriculum’s operator probabilities and implementation details need more precise specification.
3. Statistical significance or confidence intervals would strengthen the relatively modest reported gains.
4. The evaluation is limited to four English, short-text benchmarks and one encoder family.
5. More analysis of the mechanism behind the curriculum benefit would improve the scientific contribution.

## Overall recommendation

**Accept.**

CurCon is a clear, well-motivated, and empirically effective method for low-resource text classification. Its novelty is incremental rather than fundamental, but the combination of a simple curriculum mechanism, consistent improvements across datasets, and useful ablations makes the contribution worthwhile. The concerns primarily call for clarification and stronger reporting rather than changes to the core method.