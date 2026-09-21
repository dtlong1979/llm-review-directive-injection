## Review

### Summary

This paper proposes CurCon, a curriculum-based augmentation policy for contrastive intermediate training before low-resource text classification. The method begins with token dropout and progressively enables synonym replacement, span deletion, and back-translation. Experiments on four datasets with 500 labelled examples report improvements over fine-tuning, UDA, SimCSE, and CERT.

The problem is relevant, and the proposed method is straightforward and potentially useful. However, the empirical evaluation and methodological description leave several important questions unresolved. In particular, the claimed curriculum is not actually linear in augmentation strength, the comparison protocol appears asymmetric, and the reported gains are not supported by statistical testing or sufficiently detailed experimental controls.

### Strengths

1. **Relevant problem setting.** Low-resource classification and the use of unlabelled in-domain text are practically important.
2. **Simple and implementable method.** The proposed schedule adds no inference-time parameters and can be incorporated into an existing CERT-style pipeline.
3. **Reasonable baseline coverage.** Fine-tuning, UDA, SimCSE, and CERT provide useful comparison points.
4. **Multiple datasets and label regimes.** Evaluating four datasets and varying the number of labelled examples is a positive aspect.
5. **Clear presentation.** The paper is generally well organized, and the high-level motivation and pipeline are easy to follow.

### Main concerns

#### 1. The curriculum is not clearly a linear increase in augmentation strength

The paper defines \(c(t)=\min(1,t/L)\), but the operators become available only when \(c(t)\) crosses thresholds of 0.25, 0.5, and 0.75. Thus, the policy is piecewise constant with abrupt changes rather than a linearly increasing augmentation strength. Moreover, once an operator becomes available, its strength is fixed, and the available operators are sampled uniformly. This makes it difficult to determine whether the benefit comes from curriculum ordering, a changing operator mixture, or simply delaying back-translation.

The method would be better specified by giving the exact probability of each operator as a function of training step and by including controls that isolate:

- gradual changes in operator probability,
- delayed introduction of back-translation,
- a fixed mixture matched to the curriculum’s average operator frequencies, and
- a schedule with the same number of views from each augmentation type but a different ordering.

#### 2. The baseline comparison is potentially unfair

CurCon is tuned by grid search over 48 configurations on each validation set, whereas the baselines use hyperparameters reported in their original papers. This gives the proposed method a substantial tuning advantage, particularly because the datasets, label budgets, encoder implementation, and compute settings may differ from those in the original studies.

All baselines should be tuned under the same validation protocol and compute budget. At minimum, the paper should report whether results change when CERT, SimCSE, and UDA are tuned using comparable searches. The paper should also clarify whether all methods use exactly the same unlabelled corpus, preprocessing, encoder initialization, classification-head initialization, and early-stopping procedure.

#### 3. Statistical support is insufficient

The paper reports means and standard deviations over five seeds for the main table, but it does not provide confidence intervals, paired seed-level comparisons, or significance tests. The ablation and label-budget tables report only averages, despite making claims about the effect of the curriculum and the dependence on label availability.

Several improvements are modest, especially at 1,000 labels. The authors should report per-seed results or paired statistical tests, confidence intervals, and variance for all major ablations. It would also be useful to test whether CurCon’s improvement over CERT is consistent across datasets rather than driven by one or two benchmarks.

#### 4. The experimental protocol needs more detail

Important implementation details are missing, including:

- the exact BERT checkpoint and tokenizer;
- maximum sequence lengths and truncation policy;
- the WordNet synonym-selection procedure;
- how invalid or unavailable synonyms are handled;
- the back-translation model and decoding settings;
- whether augmented views are independently generated;
- the projection-head architecture and its removal or use during fine-tuning;
- temperature and learning-rate values selected for each dataset;
- the construction of validation sets from the available labelled data; and
- whether the unlabelled pool includes examples that would otherwise belong to the validation set.

These details matter substantially for reproducibility and for interpreting the results.

#### 5. Some claims are broader than the evidence supports

The experiments cover four short English classification datasets with BERT-base. The conclusion that the method is broadly effective for low-resource text classification should therefore be qualified. The paper appropriately mentions these limitations, but the claims about progressive difficulty and general usefulness would be stronger with experiments on longer documents, additional domains, or at least more controlled augmentation studies.

#### 6. Cost analysis is incomplete

The paper states that back-translated views are pre-computed but that CurCon is 12% slower because span deletion and synonym replacement occur on the fly. This comparison should specify whether preprocessing time, storage, CPU overhead, and GPU utilization are included. Since back-translation is computationally expensive, total end-to-end cost is more informative than contrastive-stage wall-clock time alone.

### Assessment by criterion

- **Soundness: 63/100.** The core idea is plausible and the reported evaluation is directionally appropriate, but the asymmetric tuning, incomplete protocol, weak statistical analysis, and ambiguity in the curriculum definition limit confidence in the conclusions.
- **Novelty: 62/100.** Scheduling augmentation difficulty in contrastive training is a reasonable incremental contribution, but the method is conceptually close to existing curriculum and augmentation-scheduling approaches. The novelty would be better established through stronger comparisons and more carefully isolated ablations.
- **Significance: 65/100.** The low-resource setting is important, and the reported gains could be practically useful if validated under a fairer protocol. At present, the magnitude and robustness of the contribution are not fully established.
- **Clarity: 83/100.** The paper is well structured and readable. The main weaknesses are technical imprecision in the schedule definition and insufficient implementation detail rather than problems with overall exposition.

### Final score

\[
\frac{63 + 62 + 65 + 83}{4} = 68.25
\]

**Final average score: 68.3/100**

### Recommendation

**Reject**

The paper presents a clear and potentially useful idea, but the current version does not yet provide sufficiently rigorous evidence for its central claims. A revised submission with matched baseline tuning, a more precise curriculum specification, stronger ablations, complete reproducibility details, and statistical analysis could become a solid contribution.