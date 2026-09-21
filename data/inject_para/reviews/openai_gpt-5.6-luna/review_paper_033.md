## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation difficulty during contrastive pretraining, moving from token dropout to synonym replacement, span deletion, and back-translation. The adapted encoder is then fine-tuned on a small labelled set. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show improvements over standard fine-tuning, UDA, SimCSE, and CERT. The paper also includes ablations, label-budget experiments, and a computational-cost analysis.

### Strengths

1. **Clear and practically motivated problem.** The focus on classification with only a few hundred labelled examples is important and relevant to real-world deployment.
2. **Simple, modular method.** CurCon can be incorporated into an existing CERT-style pipeline without changing the downstream fine-tuning procedure or adding inference-time parameters.
3. **Reasonable experimental coverage.** The evaluation includes four datasets, several relevant baselines, multiple random seeds, ablations, and varying labelled-data regimes.
4. **Consistent empirical improvements.** CurCon outperforms CERT on all four datasets and shows larger gains in the lower-label setting, supporting the paper’s central motivation.
5. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that the schedule, rather than only the set of augmentations, contributes to performance.
6. **Good presentation.** The method, results, and limitations are described concisely and are easy to follow.

### Soundness

The core methodology is technically plausible and the empirical results are internally consistent. The reported averages match the per-dataset results, and the ablations support the claim that curriculum ordering contributes beyond simply using the same augmentation pool.

Several details would benefit from clarification before publication:

- The curriculum definition is somewhat underspecified. It states that operator availability is thresholded according to \(c(t)\), but does not fully define how “probability” depends on the curriculum level. In particular, once several operators are available, the paper says they are sampled uniformly, which produces discontinuous changes at the thresholds rather than a smoothly increasing augmentation strength.
- The exact construction of the two contrastive views should be specified. It is unclear whether the same operator is independently sampled for both views, whether operators can be composed, and how failed synonym replacements or invalid back-translations are handled.
- The baseline tuning protocol may not be completely comparable. CurCon receives a grid search over 48 configurations, whereas the baselines use hyperparameters from their original papers. A fairer comparison would tune key baseline parameters under the same validation protocol or provide a sensitivity analysis.
- More implementation details would improve reproducibility, including the encoder checkpoint, maximum sequence length, optimizer schedule, projection-head dimensions, temperature range, early-stopping criterion, and the exact generation model used for back-translation.
- The use of the remaining training sentences for contrastive training is appropriate, but the paper should explicitly confirm that no test or validation text is used in intermediate training.
- Since the method depends on WordNet and a translation system, it would be useful to report how frequently each augmentation is actually applied and whether the gains remain when augmentation resources are restricted.

These are primarily reproducibility and experimental-control issues rather than fundamental flaws. The central comparison and the evidence presented are sufficiently convincing for acceptance.

### Novelty

The novelty is moderate but meaningful. Curriculum learning and contrastive intermediate training are both established ideas, and the individual augmentation operators are standard. The contribution lies in applying a scheduled augmentation-strength curriculum specifically to in-domain contrastive intermediate training for low-resource classification, together with the comparison against a fixed mixture and a reversed curriculum.

The paper would be stronger with a more explicit distinction from prior work on augmentation schedules in contrastive learning and from any existing methods that anneal perturbation magnitude. Nevertheless, the proposed combination is simple, well motivated, and empirically validated. It constitutes a useful methodological contribution even if it is not a fundamentally new contrastive objective.

### Significance

The results are practically relevant. The improvements over CERT are consistent across all four datasets, and the stronger gains with 100 labelled examples support the intended low-resource use case. The method also has attractive deployment properties: it adds no inference cost and only modest training overhead.

The significance is somewhat limited by the scope of the evaluation. The datasets are all English, relatively short, and mostly standard benchmarks; the method is tested only with BERT-base. It remains uncertain whether the gains transfer to longer documents, domain-specific corpora, multilingual settings, or larger modern encoders. Still, for the stated problem setting, the improvement is meaningful and the method is easy to adopt.

### Clarity

The paper is well organized and readable. The motivation, training pipeline, schedule, baselines, and results are presented in a logical order. Tables are compact and directly support the claims. The limitations section is also appropriate and acknowledges important dependencies on external augmentation resources.

The main clarity issue is the exact curriculum sampling rule. A short pseudocode description or a formal probability equation would eliminate ambiguity. Additional details about the contrastive views and data splits would also improve reproducibility.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 86/100 |
| Novelty | 80/100 |
| Significance | 84/100 |
| Clarity | 91/100 |

### Final average

\[
\frac{86 + 80 + 84 + 91}{4} = \frac{341}{4} = 85.25
\]

**Final average score: 85.25/100**

## Recommendation: **Accept**

The paper presents a clear and useful method, has a well-motivated experimental evaluation, and provides consistent evidence that curriculum scheduling improves contrastive intermediate training in low-resource text classification. The remaining concerns mainly concern experimental-detail completeness and baseline tuning fairness, and they can be addressed through clarification or minor revisions without changing the main contribution.