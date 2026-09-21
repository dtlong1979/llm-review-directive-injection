## Review

### Summary

The paper proposes CurCon, a contrastive intermediate-training method for low-resource text classification that increases augmentation difficulty during training. It evaluates the method on four English classification datasets with 500 labeled examples each and reports improvements over fine-tuning, UDA, SimCSE, and CERT.

The topic is relevant, and the proposed method is straightforward and potentially useful. However, the empirical evidence and methodological specification are not sufficiently rigorous to support the claims. In particular, the curriculum is not actually defined as a smooth linear increase in augmentation strength, the comparison with baselines is potentially unfair, and the paper lacks statistical significance analysis and important implementation details.

### Strengths

- Addresses a practically important low-resource classification setting.
- Uses a simple method that could be easy to implement.
- Includes several relevant baselines and multiple datasets.
- Reports results over five random seeds and includes ablations.
- The reported improvements are consistent across all four datasets.
- The paper is generally well organized and readable.

### Major concerns

1. **The curriculum is underspecified and does not match the stated formulation.**  
   The paper describes a linearly increasing augmentation strength, but the actual policy uses thresholded operator availability at 0.25, 0.5, and 0.75. Once an operator becomes available, the operators are sampled uniformly. Thus, the augmentation policy changes discontinuously rather than linearly, and the effective strength is not clearly defined. The phrase “probability of applying each operator is determined by \(c(t)\)” is not accompanied by an explicit probability formula.

2. **The \(L=0\) formulation is mathematically undefined.**  
   Since \(c(t)=\min(1,t/L)\), setting \(L=0\) produces division by zero. The text informally states that this case corresponds to a fixed mixture, but the method should define this separately and precisely.

3. **Baseline tuning is potentially unfair.**  
   CurCon is selected using a 48-configuration grid search for each dataset, while the baselines use hyperparameters from their original papers. This gives the proposed method substantially more opportunity for dataset-specific optimization. At minimum, all methods should receive comparable tuning budgets, or the authors should report results under matched tuning protocols.

4. **Statistical evidence is incomplete.**  
   Although means and standard deviations over five seeds are reported, there are no significance tests, confidence intervals, or paired seed-level comparisons. Given that the improvements over CERT are between 0.5 and 1.5 points, it is important to establish whether these gains are statistically reliable.

5. **The ablation evidence is limited.**  
   The ablation table reports only average accuracy, without per-dataset results or variability. Consequently, it is difficult to determine whether the curriculum consistently helps or whether the average gain is driven by one dataset. The comparison also does not isolate the effect of the schedule from the effect of the specific operator mixture.

6. **Important reproducibility details are missing.**  
   The paper does not specify the exact BERT checkpoint, projection-head architecture and dimensionality, optimizer settings, temperature values, early-stopping procedure, data preprocessing, back-translation system, or the precise sampling policy for views. These details are particularly important because the claimed gains are modest.

7. **The novelty is incremental.**  
   Applying a difficulty curriculum to augmentation policies in contrastive learning is reasonable, but the technical contribution is relatively narrow. The method consists mainly of ordering standard augmentations by presumed strength. Stronger analysis or comparison with adaptive schedules, continuous strength schedules, or other curriculum baselines would better establish novelty.

### Minor concerns

- “Back-translation at full strength” is somewhat misleading because back-translation is merely one of the uniformly sampled available operators after the final stage.
- The paper should report computational cost for all methods, not only the relative overhead over CERT.
- It would be useful to include results for more label counts and confidence intervals, especially given the claim that gains are largest in the lowest-resource regime.
- The use of WordNet synonym replacement may be problematic for domain-specific or polysemous language; the paper does not analyze the quality of the generated views.
- The claim that CurCon has no inference cost is true in the narrow architectural sense, but the practical training-time overhead is nontrivial and should be emphasized more clearly.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 55/100 |
| Novelty | 58/100 |
| Significance | 57/100 |
| Clarity | 79/100 |

### Final average

\[
\frac{55 + 58 + 57 + 79}{4} = 62.25
\]

**Final average score: 62.3/100**

## Recommendation: **Reject**

The paper presents a plausible and clearly described high-level idea, but the current empirical methodology is not sufficiently rigorous for acceptance. The main issues are the mismatch between the claimed and implemented curriculum, unfair baseline tuning, insufficient statistical analysis, and limited ablation and reproducibility details. A revised version with a formally specified schedule, matched hyperparameter tuning, stronger statistical validation, and more comprehensive ablations could become a viable contribution.