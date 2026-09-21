## Review

### Summary

The paper proposes CurCon, a contrastive intermediate-training method that gradually increases the strength of text augmentations during training. The idea is straightforward: begin with token dropout, progressively introduce synonym replacement and span deletion, and eventually use back-translation. Experiments on four English classification datasets with 500 labelled examples report improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The paper addresses a relevant problem: text classification with very limited labelled data.
- The proposed method is conceptually simple and potentially easy to integrate into existing contrastive-training pipelines.
- The experimental comparison includes several reasonable baselines.
- The paper reports results across multiple datasets and random seeds.
- The manuscript is generally well organized and easy to follow.
- The ablation comparing forward, fixed, and reversed curricula is useful in principle.

### Weaknesses

1. **Insufficient experimental rigor**

   The central claims are based on only four datasets, one encoder, one low-resource sampling regime, and five seeds. The paper does not report statistical significance tests or confidence intervals for the differences between CurCon and CERT. Given that several improvements are around one percentage point, it is unclear whether the gains are robust.

   The ablation table reports only averages and no standard deviations or per-dataset results. This makes it impossible to assess whether the curriculum consistently helps or whether the average is driven by one dataset.

2. **Unfair or under-specified baseline tuning**

   CurCon receives a grid search over 48 configurations on each validation set, whereas the baselines use hyperparameters “reported in their original papers.” This is not a fair comparison, particularly in a low-resource setting where learning rate, temperature, training duration, augmentation strength, and early stopping can substantially affect performance. All baselines should receive comparable tuning budgets.

3. **Methodological ambiguity**

   The augmentation schedule is not specified precisely enough for reproduction. In particular:

   - The relationship between curriculum level and operator probabilities is unclear.
   - It is not stated whether augmentation is independently sampled for each view.
   - The exact synonym-replacement and span-deletion procedures are unspecified.
   - The back-translation model, decoding settings, and language direction are not given.
   - The meaning of “token dropout” is unclear because removing tokens may require special handling of subword pieces.
   - The projection-head architecture and contrastive temperature search range are omitted.

   The statement that the schedule is controlled by a single hyperparameter is also somewhat misleading, since the operator thresholds and augmentation magnitudes are additional hand-designed choices.

4. **Limited analysis of what causes the gains**

   The fixed-mixture baseline is helpful but does not fully isolate the curriculum effect. A stronger analysis would compare:

   - The same augmentations with independently tuned fixed probabilities.
   - A schedule matched for the total number of examples seen under each augmentation.
   - Schedules with different ordering but equal augmentation distributions.
   - Different curriculum lengths and nonlinear schedules.
   - A no-back-translation curriculum with a comparable total augmentation budget.

   Without these controls, the observed improvement may result from the particular augmentation mixture or training exposure rather than curriculum learning itself.

5. **Potential validation and selection concerns**

   The validation set is used for early stopping and hyperparameter selection, but the paper does not explain whether the same validation examples are reused across all five seeds and all configurations. In a 200-example validation set, extensive per-dataset grid search could produce substantial selection variance. The paper should clarify the selection protocol and ideally include repeated data splits or nested validation.

6. **Novelty is modest**

   The main contribution is a simple schedule over known augmentation operators. The paper does not sufficiently distinguish CurCon from existing work on scheduled augmentation, curriculum learning, or contrastive learning with varying augmentation strengths. The related-work discussion is brief and does not establish that this particular scheduling strategy has not already been explored in closely related settings.

7. **Cost and reproducibility claims need clarification**

   The paper states that back-translated views are precomputed, yet CurCon is approximately 12% slower because of on-the-fly operations. It should report preprocessing costs separately, including translation generation time and storage requirements. Training details such as sequence length, hardware precision, optimizer settings, warmup, weight decay, and the number and size of the unlabeled examples are also missing.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 56/100 |
| Novelty | 61/100 |
| Significance | 58/100 |
| Clarity | 78/100 |

**Final average:**  
\[
(56 + 61 + 58 + 78)/4 = \mathbf{63.25}
\]

### Final recommendation

**Reject**

The paper presents a plausible and clearly described high-level idea, but the current evidence is not sufficiently rigorous to support the claimed contribution. The main issues are asymmetric baseline tuning, limited statistical analysis, incomplete implementation details, and insufficient controls isolating the curriculum effect. A stronger revision with fair hyperparameter tuning, fuller reporting, significance testing, and more comprehensive schedule ablations could make the work substantially more convincing.