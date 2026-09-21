## Review

### Summary

The paper proposes CurCon, which gradually increases the strength of text augmentations during contrastive intermediate training. The method is simple and potentially useful for low-resource classification, and the reported results show consistent gains over fine-tuning, UDA, SimCSE, and CERT. However, the empirical evidence and methodological description are not yet sufficiently rigorous to support the paper’s claims.

### Strengths

- Addresses an important practical problem: classification with very limited labelled data.
- The proposed curriculum is simple, intuitive, and adds no inference-time parameters.
- CurCon improves over CERT on all four reported datasets.
- Includes ablations for fixed augmentation mixtures, reversed curricula, and removal of back-translation.
- The paper is generally well organized and easy to follow.

### Concerns

#### Soundness

The main weakness is the experimental methodology.

1. **Unequal hyperparameter tuning.** CurCon is selected using a 48-configuration grid search on each validation set, whereas baselines use hyperparameters from their original papers. This may give CurCon an unfair advantage, particularly in a low-resource setting where hyperparameter sensitivity is substantial. All methods should receive comparable tuning budgets.

2. **Insufficient statistical analysis.** Results are averaged over only five seeds, and no confidence intervals, paired tests, or per-seed results are provided. The reported gains, especially the 0.5-point improvement with 1,000 labels, may not be statistically meaningful.

3. **Ambiguous curriculum definition.** The paper says augmentation strength increases linearly, but the actual policy is threshold-based: operators become available at 0.25, 0.5, and 0.75, and then are sampled uniformly. This is not clearly a linear increase in strength. The behavior at \(L=0\) is also mathematically undefined under \(c(t)=\min(1,t/L)\), although the intended special case is stated informally.

4. **Ablations are not fully controlled.** The fixed-mixture baseline may have a different augmentation distribution and optimization trajectory from CurCon. It is unclear whether the comparison controls for the number and type of views, augmentation frequency, and computational cost.

5. **Limited methodological detail.** Important information is missing, including the exact back-translation model, synonym replacement procedure, handling of failed or shortened augmentations, sequence truncation, projection-head dimensions, temperature ranges, learning rates, and whether unlabeled data include validation examples.

6. **Potential data-split ambiguity.** The paper should clearly specify whether the 500 labelled examples, validation set, and contrastive unlabeled pool are disjoint and whether any standard test or validation sentences enter intermediate training.

The results are plausible, but the current description does not establish that the curriculum itself, rather than tuning or augmentation differences, produces the reported gains.

#### Novelty

The central idea—progressively increasing augmentation difficulty in contrastive training—is reasonable but incremental. Curriculum learning and augmentation scheduling are established ideas, and the paper does not clearly distinguish CurCon from prior work on augmentation schedules, curriculum contrastive learning, or adaptive augmentation policies. The contribution would be more compelling with stronger comparisons to closely related scheduled-augmentation methods and a more principled analysis of why the proposed schedule works.

#### Significance

The problem is relevant, and a consistent 1.1-point gain over CERT could be useful in low-resource settings. However, the evaluation is limited to four small English classification datasets and one encoder family. The gains are moderate, and the paper does not establish robustness across domains, languages, encoder sizes, or substantially different label budgets. The 12% training-time overhead is acceptable, but the practical benefit should be weighed against the additional complexity and reliance on external resources.

#### Clarity

The paper is clearly structured and readable overall. The method and experimental pipeline are easy to understand at a high level. Clarity is reduced by the ambiguity in the curriculum formulation, incomplete implementation details, and imprecise description of the baseline tuning protocol. The claim of a “linear” schedule should be revised or the schedule should actually be made continuous.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 54/100 |
| Novelty | 46/100 |
| Significance | 56/100 |
| Clarity | 82/100 |
| **Final average** | **59.5/100** |

The average is:

\[
\frac{54 + 46 + 56 + 82}{4} = 59.5
\]

## Final recommendation: **Reject**

The paper presents a clear and potentially useful idea, but the current evidence is not sufficiently rigorous for acceptance. A stronger revision should use equally tuned baselines, report statistical significance and per-seed results, clarify the data splits and augmentation implementation, control the ablations more carefully, and compare against closer curriculum or scheduled-augmentation approaches.