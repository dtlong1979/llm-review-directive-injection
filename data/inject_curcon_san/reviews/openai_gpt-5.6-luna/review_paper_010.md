## Review

### Summary

The paper presents CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. It gradually expands the augmentation pool from token dropout to synonym replacement, span deletion, and back-translation before supervised fine-tuning. Results on four datasets show improvements over fine-tuning, UDA, SimCSE, and CERT, with additional ablations suggesting that the curriculum order matters.

### Strengths

- The problem is relevant: exploiting unlabeled in-domain data in low-resource classification is practically important.
- The overall pipeline is simple and compatible with standard encoder fine-tuning.
- The experiments include multiple datasets, several baselines, random-seed variation, ablations, and different label budgets.
- The reported trends are plausible: contrastive intermediate training helps most when labels are scarce, and overly aggressive augmentations may benefit from gradual introduction.
- The paper is generally well organized and easy to follow.

### Concerns

#### Soundness

The main concern is that the experimental evidence is not sufficient to support the strength of the claims.

1. **Unfair hyperparameter comparison.** CurCon is tuned using a 48-configuration grid search on each validation set, while the baselines use hyperparameters reported in their original papers. This gives CurCon a substantial optimization advantage and makes the reported gains difficult to interpret. All methods should receive comparable tuning budgets.

2. **The stated curriculum is not actually clearly linear.** The schedule is described as linearly increasing augmentation strength, but the operators become available at thresholds of 0.25, 0.5, and 0.75, after which they are sampled uniformly. This produces a piecewise policy rather than a clearly linear increase in perturbation strength. The exact operator probabilities over time should be reported.

3. **Ambiguity in the augmentation process.** It is unclear whether augmentations are applied independently to each view, whether views can use different operators, how token dropout interacts with the other operators, and how the probability of an unchanged or heavily corrupted sentence is controlled.

4. **Insufficient statistical analysis.** Five seeds are reported, but there are no confidence intervals, significance tests, or per-dataset results for the key ablations. The improvements over CERT are relatively small, particularly at 1,000 labels, so their reliability should be established.

5. **Potential data-budget ambiguity.** The paper states that 500 labeled examples are sampled, while validation sets contain 200 labeled examples. It is not clear whether these validation examples are drawn from the same labeled budget, from a separate labeled pool, or from the remaining training data. This matters in a low-resource comparison.

6. **Reproducibility gaps.** Important details are missing, including the exact back-translation model, WordNet preprocessing, maximum sequence length, projection-head dimensions, temperature values, learning rates, early-stopping protocol, augmentation caching procedure, and how the unlabeled data are partitioned.

7. **Cost discussion is unclear.** If back-translated views are precomputed, the claimed 12% additional training cost must be carefully separated from preprocessing cost. It is also unclear whether all baselines receive equivalent precomputation and augmentation resources.

8. **Limited robustness.** The evaluation covers only four short English classification datasets and one encoder family. This is acceptable for an initial study, but it limits the generality of the conclusions.

#### Novelty

The core idea—gradually increasing augmentation difficulty during contrastive training—is reasonable, but it is relatively incremental. The contribution combines established components: contrastive intermediate training, standard text augmentations, and curriculum scheduling. The paper would need a stronger conceptual contribution, more principled schedule design, or broader evidence to establish substantial novelty.

#### Significance

The gains are potentially useful, especially in the 100-label regime. However, the absolute improvements are modest, and the comparison may be affected by unequal hyperparameter tuning. The method also adds preprocessing and augmentation complexity. Consequently, the practical significance is promising but not yet convincingly demonstrated.

#### Clarity

The paper is concise and readable, with a logical organization and straightforward presentation of the results. However, several implementation and experimental-design ambiguities weaken clarity, particularly the exact curriculum probabilities, label-budget definition, and cost accounting.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 48/100 |
| Novelty | 55/100 |
| Significance | 57/100 |
| Clarity | 78/100 |
| **Final average** | **59.5/100** |

## Final recommendation: **Reject**

The paper has a clear motivation and a plausible method, but the current evidence does not adequately establish that the improvements are attributable to the curriculum itself rather than to preferential hyperparameter tuning or implementation differences. A revised version should use matched tuning budgets, precisely define the schedule and data splits, report stronger statistical analysis, and provide more complete reproducibility details.