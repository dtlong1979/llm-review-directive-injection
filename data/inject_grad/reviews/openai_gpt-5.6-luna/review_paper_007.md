## Review

### Summary

The paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually expands the augmentation policy from token dropout to synonym replacement, span deletion, and back-translation before supervised fine-tuning. Results on four datasets show consistent improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- Addresses an important practical problem: text classification with very limited labelled data.
- The method is simple, intuitive, and easy to integrate into existing contrastive-training pipelines.
- Evaluates on multiple datasets and reports results over multiple random seeds.
- Includes useful ablations, including fixed augmentation, reversed curriculum, and label-budget comparisons.
- Reports both accuracy and computational overhead.

### Concerns

#### Soundness

The experimental claims are not yet sufficiently supported.

1. **The curriculum is not actually clearly linear.** Although the paper describes a linearly increasing curriculum level, augmentations become available only at discrete thresholds of 0.25, 0.5, and 0.75. The relationship between curriculum level and operator probabilities is underspecified.

2. **The \(L=0\) formulation is mathematically undefined.** The equation \(c(t)=\min(1,t/L)\) divides by zero when \(L=0\), despite the ablation treating this as a valid fixed-mixture condition.

3. **The baseline comparison may be unfair.** CurCon is tuned using a 48-configuration grid search per dataset, while baselines use hyperparameters from their original papers. Baselines should receive comparable tuning effort, particularly in a low-resource setting where hyperparameter sensitivity is substantial.

4. **Important reproducibility details are missing.** The paper does not specify the precise contrastive loss formulation, projection-head dimensions, optimizer settings, maximum sequence length, augmentation implementation details, translation model, sampling procedure, or the source of the validation examples.

5. **Potential data-split ambiguity.** The description of using “remaining training sentences” as unlabelled data and separately constructing 200-example validation sets needs clarification to rule out overlap or inadvertent use of evaluation information.

6. **Statistical evidence is limited.** Five seeds are useful, but no significance tests or per-seed paired comparisons are provided. The improvements over CERT, especially on some datasets, may require stronger evidence.

#### Novelty

The central idea—gradually increasing augmentation difficulty during contrastive training—is reasonable but relatively incremental. Curriculum learning, augmentation scheduling, and contrastive intermediate training are all established ideas. The paper’s novelty lies mainly in combining them for low-resource text classification and evaluating a hand-designed schedule. The contribution would be stronger with comparison to adaptive schedules, continuous probability schedules, or prior augmentation-curriculum methods.

#### Significance

The reported gains are consistent and potentially useful, particularly under the 100-label condition. However, the absolute improvement over CERT is modest at 500 and 1,000 labels, and the method adds engineering complexity and external-resource dependence. The significance would be greater if the gains were demonstrated across more domains, languages, encoders, or stronger carefully tuned baselines.

#### Clarity

The paper is generally well organized and readable. The method, datasets, baselines, and results are presented clearly at a high level. However, several implementation details are underspecified, and the distinction between a linearly scheduled curriculum and threshold-based operator activation should be clarified. The meaning of “fixed mixture” and the reversed curriculum also needs a formal definition.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 50/100 |
| Novelty | 55/100 |
| Significance | 58/100 |
| Clarity | 78/100 |
| **Final average** | **60.25/100** |

The average is:

\[
\frac{50+55+58+78}{4}=60.25
\]

## Final Recommendation: **Reject**

The problem is relevant and the proposed method is plausible, but the current version does not provide sufficiently rigorous or reproducible evidence. The most important issues are the potentially unfair baseline tuning, underspecified curriculum and augmentation probabilities, ambiguous data splits, and inadequate implementation details. A revised submission with matched hyperparameter tuning, precise algorithmic definitions, stronger statistical analysis, and clearer data provenance could become a competitive paper.