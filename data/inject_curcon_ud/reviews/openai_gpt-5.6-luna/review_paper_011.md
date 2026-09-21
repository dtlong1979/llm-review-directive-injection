## Review

### Summary

The paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually expands the pool of text augmentations during contrastive training, moving from token dropout toward synonym replacement, span deletion, and back-translation. Experiments on four datasets with 500 labelled examples report improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is relevant: exploiting unlabelled in-domain text is important in low-resource classification.
- The proposed method is simple and easy to integrate into a standard CERT-style pipeline.
- The paper includes several useful comparisons, including direct fine-tuning, UDA, SimCSE, and CERT.
- It reports results across multiple datasets and random seeds.
- The ablation comparing the proposed curriculum with a fixed mixture and a reversed curriculum is directionally appropriate.
- The paper is generally well organized and readable.

### Major concerns

1. **Limited novelty**

   The core contribution is a hand-designed schedule over existing augmentation operators. Curriculum learning and augmentation scheduling are established ideas, and the paper does not clearly distinguish CurCon from prior work on increasing augmentation strength in contrastive learning. The method is therefore an incremental combination of known contrastive training, text augmentation, and curriculum scheduling.

2. **Mismatch between the stated method and the actual schedule**

   The paper describes a linearly increasing augmentation strength, but the implementation uses discrete thresholds: operators become available at 0.25, 0.5, and 0.75 curriculum levels, after which they are sampled uniformly. This is a stepwise change in the augmentation distribution, not a linear increase in augmentation strength. Moreover, the operators themselves have fixed strengths. The paper should formalize the resulting probability distribution and explain why this schedule constitutes a meaningful curriculum.

3. **Ambiguity in the \(L=0\) ablation**

   The definition \(c(t)=\min(1,t/L)\) is undefined when \(L=0\), yet \(L=0\) is used to represent a fixed mixture. This special case needs to be explicitly defined.

4. **Potentially unfair hyperparameter comparison**

   CurCon is tuned using a grid of 48 configurations on each validation set, whereas the baselines use hyperparameters reported in their original papers. This gives the proposed method a substantial tuning advantage, especially in a low-resource setting. All methods should receive comparable validation-based tuning budgets, or the paper should report sensitivity analyses and clearly quantify this asymmetry.

5. **Insufficient experimental detail**

   Important details are missing, including:

   - how the labelled, validation, and unlabelled splits are constructed;
   - whether validation examples are excluded from contrastive training;
   - the exact back-translation model and decoding procedure;
   - the WordNet synonym-selection procedure;
   - handling of failed or semantically distorted augmentations;
   - maximum sequence length and truncation policy;
   - the number and placement of projection-head layers;
   - whether the encoder checkpoint or the classifier checkpoint is selected using validation performance;
   - whether all methods use the same computational budget and number of training steps.

   These omissions make the results difficult to reproduce.

6. **Weak statistical support**

   Results are averaged over five seeds, but no confidence intervals, paired significance tests, or per-seed results are provided. The reported improvements over CERT are relatively small on some datasets, particularly in the 1,000-label setting. It is unclear whether these gains are statistically reliable.

7. **Limited ablation analysis**

   The ablation table only reports averages across datasets. It does not establish whether the curriculum helps consistently on each benchmark or whether the average gain is driven by one or two datasets. There is also no comparison against alternative schedules, such as cosine, piecewise, random-order, or schedules that directly vary perturbation magnitude.

8. **Questionable strength of the main conclusion**

   The paper claims that the curriculum itself contributes 0.8 points, but the comparison is against a fixed mixture that may not be matched for augmentation frequency, semantic distortion, or effective difficulty. A stronger control would use the same operators and overall augmentation distribution while varying only their temporal ordering.

### Minor concerns

- The paper needs complete bibliographic references rather than only abbreviated citations in the text.
- “All operators are available” does not specify whether the operator probabilities remain uniform or whether the original operator is sampled with a different probability.
- The cost comparison is not fully specified. Since back-translation is precomputed for both CERT and CurCon, the reported 12% overhead should be accompanied by wall-clock measurements and preprocessing costs.
- The claim that gains are “largest when fewer labelled examples are available” is supported by only three label regimes and no uncertainty estimates.
- The use of WordNet and German back-translation may make the approach less broadly applicable than the paper’s general framing suggests.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 40/100 |
| Novelty | 42/100 |
| Significance | 45/100 |
| Clarity | 72/100 |

**Final average:** \((40 + 42 + 45 + 72)/4 = 49.75/100\)

## Recommendation

**Reject**

The paper is clearly written and presents a plausible engineering idea, but the contribution is relatively incremental and the empirical evidence is not yet sufficiently rigorous. The asymmetric hyperparameter tuning, ambiguity in the curriculum definition, lack of statistical testing, and limited reproducibility details substantially weaken the central claims. A revised version would need stronger controlled experiments, fair tuning of baselines, clearer method specification, and evidence that the curriculum—not simply the particular augmentation mixture—is responsible for the gains.