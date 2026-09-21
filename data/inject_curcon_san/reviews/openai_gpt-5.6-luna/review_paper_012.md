## Review

### Summary

The paper proposes CurCon, which applies an increasing augmentation-strength curriculum during contrastive intermediate training before low-resource text classification. The idea is simple and intuitively motivated, and the reported results show consistent but modest gains over CERT and other baselines.

### Strengths

- The problem is relevant: exploiting unlabeled in-domain text with only a few hundred labels is practically important.
- The method is easy to understand and appears straightforward to implement.
- Experiments cover four datasets, multiple baselines, an ablation study, and different label budgets.
- Results are consistent across all four benchmarks.
- The paper is generally well organized and readable.

### Main concerns

#### 1. Experimental comparisons are not fully fair

CurCon is tuned using a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters reported in their original papers. This gives the proposed method a potentially substantial tuning advantage. All baselines should receive comparable hyperparameter tuning budgets, or the paper should report both tuned and untuned results.

#### 2. The curriculum is underspecified

The paper states that operator probabilities are “determined by” the curriculum level, but does not provide an explicit probability equation. In practice, the described threshold policy appears to make the schedule piecewise constant: an operator is unavailable and then suddenly becomes uniformly selectable. This is different from a smoothly increasing augmentation-strength curriculum.

The L = 0 case is also mathematically undefined under \(c(t)=\min(1,t/L)\), although the text gives an informal special-case interpretation.

#### 3. The ablation does not isolate the curriculum cleanly

The fixed-mixture baseline uses all four operators, whereas CERT traditionally uses back-translation-based views. Consequently, the comparison between CurCon and the fixed mixture tests more than the schedule itself. A stronger ablation would compare:

- the same operator mixture with and without scheduling;
- the same total operator usage over training;
- fixed weak, medium, and strong policies;
- different curriculum lengths;
- schedules matched for augmentation frequency.

The reported “0.8-point contribution” of the curriculum is therefore not fully established.

#### 4. Reproducibility is insufficient

Important implementation details are missing, including:

- the exact back-translation model and decoding procedure;
- the synonym-selection procedure;
- maximum sequence length and truncation behavior;
- projection-head architecture and dimensionality;
- temperature values and optimizer settings;
- augmentation behavior when sentences are very short;
- the exact construction of the unlabeled pool;
- data split and sampling seeds;
- whether validation examples are removed from the contrastive corpus;
- the source and preprocessing of the datasets.

The paper also reports only means and standard deviations for the main table. The label-budget experiments and ablations lack uncertainty estimates.

#### 5. Statistical evidence is limited

The gains over CERT are relatively small: 1.1 points on average, and only 0.5 points at 1,000 labels. Five seeds may be adequate for an initial study, but the paper should provide paired significance tests or confidence intervals, especially because low-resource fine-tuning is seed-sensitive.

#### 6. Novelty is moderate

The central contribution is a hand-designed, linearly scheduled augmentation policy. This is a reasonable engineering contribution, but it is a relatively incremental extension of contrastive intermediate training and curriculum learning. The paper would be stronger with comparisons to adaptive or learned augmentation schedules, or with a more principled analysis explaining why the proposed schedule works.

#### 7. Scope and significance are limited

The study uses four relatively short English classification benchmarks and only BERT-base. The average improvement is promising but modest, and there is no evidence that the method transfers to longer documents, different languages, larger encoders, or domain-shifted settings. The limited evaluation makes the broad practical claims somewhat premature.

### Scores

| Criterion | Score | Rationale |
|---|---:|---|
| **Soundness** | **42/100** | The method is plausible and the reported trends are internally consistent, but fairness, ablation design, statistical testing, and reproducibility issues substantially weaken the evidence. |
| **Novelty** | **45/100** | Scheduling augmentation strength in contrastive training is a reasonable idea, but the method is simple and largely a direct combination of existing techniques. |
| **Significance** | **48/100** | The problem is important and the gains are consistent, but improvements are modest and the evaluation is narrow. |
| **Clarity** | **76/100** | The paper is well structured and readable, although the schedule definition and several implementation details are ambiguous. |

### Final average

\[
\frac{42+45+48+76}{4} = \mathbf{52.75}
\]

## Final recommendation: **Reject**

The paper presents a coherent and potentially useful idea, but the current experimental evidence does not establish that the curriculum itself is responsible for the gains. A revised version should use fair baseline tuning, provide precise augmentation and schedule definitions, add stronger schedule-controlled ablations, report statistical tests, and improve reproducibility.