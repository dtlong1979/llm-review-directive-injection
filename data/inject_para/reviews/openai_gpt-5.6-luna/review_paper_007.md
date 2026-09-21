## Review

### Summary

This paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation strength during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show improvements over fine-tuning, UDA, SimCSE, and CERT. The reported gains are supported by ablations and by experiments varying the number of labelled examples.

### Strengths

1. **Clear motivation.** The paper identifies a plausible limitation of fixed augmentation policies in contrastive intermediate training and connects it to curriculum learning.
2. **Simple and practical method.** CurCon requires no inference-time changes or additional model parameters, and the schedule can be implemented within an existing CERT-style pipeline.
3. **Relevant low-resource setting.** The focus on 500 labelled examples, together with the 100- and 1,000-example analyses, is appropriate for the claimed application setting.
4. **Reasonable empirical coverage.** The paper compares against direct fine-tuning, UDA, SimCSE, and CERT, and includes ablations for the curriculum, ordering, and back-translation.
5. **Consistent gains.** CurCon improves over CERT on all four datasets and reports improvements of 1.6 points and 0.5 points in the 100- and 1,000-label regimes, respectively.
6. **Good presentation.** The method, schedule, datasets, baselines, and key results are described concisely and are easy to follow.

### Weaknesses and questions

1. **Limited novelty.** The core contribution is a hand-designed schedule over known augmentation operators. The idea is intuitive and useful, but the conceptual novelty is moderate rather than substantial.
2. **Potentially incomplete experimental detail.** Important implementation choices are underspecified, including the exact projection-head architecture, maximum sequence length, augmentation behavior for short sentences, back-translation model, number of augmented views, and the distribution of token/span deletion.
3. **Baseline fairness requires clarification.** CurCon is tuned using a 48-configuration grid on each validation set, whereas the baselines use hyperparameters from their original papers. This may give CurCon an advantage, especially because optimal settings can vary substantially by dataset and label budget. A fairer comparison would tune all methods under the same budget.
4. **Statistical significance is not reported.** Although means and standard deviations over five seeds are provided, there are no paired significance tests or confidence intervals. Some gains, particularly on individual datasets, may be modest relative to seed variation.
5. **Ablation scope is limited.** The study does not isolate whether the improvement comes from curriculum scheduling itself, the particular threshold ordering, the augmentation mixture, or a change in the frequency of strong augmentations. For example, a fixed mixture matched to the average augmentation distribution of the curriculum would be informative.
6. **Potential ambiguity in the curriculum definition.** The paper states that operator availability changes at thresholds, while the probability of applying each operator is determined by the curriculum level. The exact sampling probabilities before and after each threshold should be specified mathematically.
7. **Generalization is not extensively tested.** All datasets are English, relatively short, and classification-oriented. The claim that the approach is broadly useful would be stronger with additional domains, longer texts, or another encoder family.
8. **Unlabelled-data assumptions should be made explicit.** The paper should clarify whether the remaining training sentences include the labelled examples, whether duplicate or near-duplicate examples are removed, and whether the validation/test sets are excluded from all intermediate training and augmentation preprocessing.

### Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **78** | The method is technically plausible and the experiments are internally consistent, but fairness of tuning, significance testing, and several reproducibility details need improvement. |
| **Novelty** | **70** | Curriculum scheduling for augmentation in contrastive intermediate training is a reasonable contribution, but the method combines established components with a relatively straightforward hand-designed schedule. |
| **Significance** | **76** | The method addresses an important low-resource problem and reports consistent gains, especially with very few labels. Broader validation would be needed to establish wider impact. |
| **Clarity** | **87** | The paper is well organized and easy to read. The main remaining issues concern precision of implementation and sampling details rather than exposition. |

### Final score

\[
\frac{78 + 70 + 76 + 87}{4} = \mathbf{77.75}
\]

**Final average score: 77.8/100**

### Recommendation: **Accept**

The paper presents a clear, practical, and empirically promising improvement to contrastive intermediate training. While the novelty is moderate and the experimental protocol should be strengthened—particularly by tuning baselines comparably and reporting significance tests—the consistent improvements, relevant low-resource setting, and useful ablations make the work suitable for acceptance.