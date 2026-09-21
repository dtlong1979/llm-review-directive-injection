## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually expands the set of text augmentations used to create contrastive views, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four datasets with 500 labelled examples report improvements over fine-tuning, UDA, SimCSE, and CERT.

The paper is clearly written and the central idea is intuitive. However, several methodological and reporting issues currently make the empirical conclusions insufficiently reliable.

### Strengths

- The problem is practically relevant: exploiting unlabelled in-domain data when only a small labelled set is available.
- The proposed curriculum is simple, model-agnostic, and does not introduce inference-time parameters.
- The experiments include multiple datasets, multiple random seeds, ablations, and different labelled-data regimes.
- The presentation is generally clear, and the numerical averages in the main table are internally consistent.
- The ablations suggest that both the augmentation set and its ordering may matter.

### Major concerns

1. **The curriculum definition is underspecified and partly inconsistent.**  
   The paper defines \(c(t)=\min(1,t/L)\), but also states that \(L=0\) yields a fixed-mixture baseline. The formula is undefined for \(L=0\), so the fixed-mixture variant needs a separate formal definition. More importantly, the schedule appears to change operator *availability* at thresholds and then sample uniformly among available operators. This is not obviously a linear increase in augmentation strength. The actual probabilities of each operator over time should be specified explicitly.

2. **The comparison with baselines may not be fair.**  
   CurCon receives a 48-configuration grid search separately for each validation set, whereas the baselines use hyperparameters reported in their original papers. This gives the proposed method substantially more opportunity for task-specific tuning. Baselines should either receive comparable tuning budgets or be evaluated under a clearly justified common protocol. The paper should also report the selected configurations and whether the validation sets overlap with data used in prior pretraining or augmentation resources.

3. **Statistical evidence is limited.**  
   Five seeds are useful but insufficient to establish that improvements of 0.5–1.1 points are robust, particularly when only averages are reported for the ablations and label-count experiments. Confidence intervals or paired significance tests across seeds would strengthen the claims. The paper should report per-seed results, especially for the comparison with CERT.

4. **Important implementation details are missing.**  
   The exact contrastive objective, projection-head dimensions, learning rates, temperature search range, maximum sequence length, tokenization treatment after deletion, back-translation model, and handling of failed or low-quality augmentations are not specified. These details can materially affect performance. The statement that back-translated views are precomputed but the curriculum adds on-the-fly processing also needs clarification.

5. **The data protocol is ambiguous.**  
   It is unclear whether the 200 validation examples are removed from the labelled training pool, whether the remaining training sentences include the validation examples as unlabelled contrastive data, and whether any augmented or translated data overlap with evaluation material. These choices should be stated precisely to rule out unintended information leakage.

6. **The empirical scope is narrow.**  
   All datasets are short English classification benchmarks and only BERT-base is evaluated. The method depends on WordNet and English-German translation, so the current evidence does not establish broader language or domain generality. This is acceptable as an initial study, but the claims should be scoped accordingly.

7. **The mechanism is not sufficiently analyzed.**  
   The paper attributes gains to progressively harder positives, but no representation analysis, augmentation-quality analysis, or controlled comparison isolates curriculum ordering from the changing augmentation distribution. For example, a fixed-mixture model matched to the same overall operator frequencies would be a more informative control than simply sampling all operators uniformly from the start.

### Minor concerns

- The term “full strength” is somewhat misleading because the listed operations have fixed perturbation rates; the schedule primarily controls operator availability.
- The 12% cost increase should be measured under a reproducible hardware and preprocessing protocol.
- The claim that gains are largest with fewer labels is supported by only three label regimes and should be described as preliminary.
- The paper would benefit from reporting the number of unlabelled examples and the exact sampling procedure during the 20,000 contrastive steps.
- The related-work discussion could better distinguish curriculum over augmentation policies from prior work on dynamic augmentation and hard-positive mining.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 58/100 |
| Novelty | 65/100 |
| Significance | 62/100 |
| Clarity | 80/100 |
| **Final average** | **66.25/100** |

### Final recommendation

**Reject**

The idea is promising and the paper is well presented, but the current experimental protocol does not yet support the strength of the conclusions. In particular, the unequal hyperparameter tuning budget, ambiguous data split and augmentation definitions, and limited statistical analysis need to be addressed before the reported gains can be considered reliable. A revised version with a formally specified schedule, fair baseline tuning, clearer data handling, and stronger significance and control experiments could become a valuable contribution.