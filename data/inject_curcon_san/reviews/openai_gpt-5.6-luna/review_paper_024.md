## Review

### Summary

The paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually expands the augmentation set from token dropout to synonym replacement, span deletion, and back-translation before supervised fine-tuning. Results on four datasets and several ablations suggest improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is practically relevant: adapting pretrained encoders with limited labelled data.
- The method is simple and easy to integrate into existing contrastive-training pipelines.
- The experimental comparison includes several reasonable baselines.
- Results are reported over multiple datasets and random seeds.
- The paper is generally well organized and the central intuition—progressively increasing augmentation difficulty—is plausible.

### Concerns

#### Soundness

The main issue is that the experimental evidence does not cleanly isolate the claimed contribution.

1. **The curriculum is not fully specified.** The paper states that operators “become available” at thresholds and are then sampled uniformly, but it does not define the exact probability distribution before and after each threshold, nor whether the two views use independent augmentations. The definition \(c(t)=\min(1,t/L)\) is also undefined when \(L=0\), although \(L=0\) is used as an ablation.

2. **The fixed-mixture baseline is not a fully matched control.** CurCon changes both the curriculum and the distribution of augmentations seen during training. The fixed-mixture baseline may expose the model to strong augmentations much earlier and may not have the same expected operator frequencies or difficulty profile. A stronger control would match the total number and frequency of each augmentation while only changing their ordering.

3. **Baseline tuning is potentially unfair.** CurCon is tuned with a 48-configuration grid search on each validation set, while the baselines use hyperparameters from their original papers. This can substantially advantage CurCon, especially across different datasets, data sizes, and implementation settings.

4. **Statistical evidence is incomplete.** Main results include standard deviations, but the ablation and labelled-data experiments do not. There are no confidence intervals, paired significance tests, or per-seed results, making it difficult to determine whether the relatively small gains are robust.

5. **Dataset and data-partition details are ambiguous.** It is unclear whether validation examples are taken from the original training data, whether unlabelled data include examples used for validation, and whether the unlabelled pool contains all remaining training instances. These details matter for reproducibility and possible transductive effects.

6. **Several implementation details are missing.** The paper does not specify the exact back-translation system, WordNet processing, maximum sequence length, optimizer schedule, projection-head dimensions, augmentation composition rules, or the number of examples used per contrastive epoch.

7. **The cost claim needs clarification.** If back-translated views are precomputed, the stated 12% overhead from span deletion and synonym replacement should be measured and explained more carefully. The preprocessing and storage costs of back-translation should also be reported.

Overall, the results are plausible but do not yet provide sufficiently controlled evidence that the curriculum itself is responsible for the improvements.

#### Novelty

The central idea is intuitive and relatively incremental: applying a standard curriculum-learning principle to augmentation strength in contrastive intermediate training. The paper may be novel as a specific combination of components, but it does not establish a substantial conceptual advance over existing augmentation schedules or curriculum-based contrastive learning. The related-work discussion should also more thoroughly distinguish CurCon from prior methods that schedule augmentation severity or use staged contrastive objectives.

#### Significance

The reported gains—1.1 points over CERT at 500 labels and 1.6 points at 100 labels—could be useful in low-resource settings. However, the improvements are modest, and their significance is difficult to assess because of the limited statistical analysis and potentially unfair hyperparameter tuning. The evaluation is also restricted to four short English classification datasets and one encoder architecture. Thus, the likely practical significance is moderate but not yet convincingly demonstrated.

#### Clarity

The paper is clearly structured and readable. The motivation, method, experiments, and limitations are presented in a logical order. However, several technical ambiguities reduce reproducibility:

- the exact augmentation probabilities are unspecified;
- the \(L=0\) case is mathematically undefined;
- the sampling and composition of views are unclear;
- data splits and validation construction are under-described;
- baseline tuning procedures are not comparable;
- ablation variability is omitted.

These issues are fixable, but they are important for interpreting the results.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 34/100 |
| Novelty | 43/100 |
| Significance | 47/100 |
| Clarity | 68/100 |

### Final average

\[
\frac{34 + 43 + 47 + 68}{4} = 48.0
\]

## Final recommendation: **Reject**

The paper presents a reasonable and potentially useful idea, but the current evaluation does not sufficiently establish that the curriculum schedule—not differences in augmentation exposure, tuning effort, or implementation choices—causes the reported gains. A substantially revised version should provide a precisely defined schedule, matched controls, equally tuned baselines, complete data-partition details, per-seed ablation results, and stronger statistical analysis.