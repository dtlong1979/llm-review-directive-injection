## Review

### Summary

The paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually expands the set of text augmentations used during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. Results on four datasets with 500 labelled examples suggest improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The paper addresses an important practical problem: classification with limited labelled data.
- The method is conceptually simple and easy to integrate into an existing CERT-style pipeline.
- The experimental comparison includes several relevant baselines.
- Results are reported across multiple datasets and random seeds.
- The paper includes ablations for curriculum ordering, back-translation, and the contrastive stage.
- The writing and organization are generally clear.

### Main concerns

#### 1. Limited novelty

The core contribution is a fixed, hand-designed augmentation curriculum applied to contrastive intermediate training. This is a relatively incremental extension of CERT and existing curriculum-learning or augmentation-scheduling ideas. The schedule is not learned or adaptive, and the method introduces no new contrastive objective or representation-learning mechanism.

Moreover, the described implementation is not truly a linear increase in augmentation strength. Operators become available at discrete thresholds—0.25, 0.5, and 0.75—and are then sampled uniformly. This is closer to a staged augmentation policy than a linear curriculum. The distinction matters because the paper attributes the gains specifically to a progressive schedule.

#### 2. Experimental comparisons are not fully fair

CurCon is tuned using a grid search over 48 configurations per dataset, whereas the baselines use hyperparameters from their original papers. This gives the proposed method a substantial optimization advantage, particularly in a low-resource setting where hyperparameter sensitivity can be large. Baselines should receive comparable tuning budgets, or results should be reported both with standardized tuning and with original configurations.

The paper also does not provide enough implementation detail to verify that CERT, UDA, and SimCSE were reproduced under equivalent data, compute, preprocessing, and early-stopping conditions.

#### 3. Statistical evidence is limited

Although means and standard deviations over five seeds are reported, the paper does not provide confidence intervals or significance tests. The average improvement over CERT is only 1.1 points, and several individual differences may be within seed variation. The ablation table gives no standard deviations at all, making it difficult to assess whether the curriculum effect is reliable.

The statement that gains are “largest when fewer labelled examples are available” is plausible and supported by the three reported settings, but the analysis is very limited and does not establish a statistically meaningful trend.

#### 4. Important methodological details are underspecified

Several choices are ambiguous:

- How are positive views generated when multiple operators are available?
- Are augmentations applied independently to each view?
- How are WordNet failures, short sentences, and back-translation artifacts handled?
- Is the unlabelled pool identical across methods?
- Are validation examples excluded from contrastive training?
- How is the curriculum length selected without overfitting the validation set?
- Are the reported baseline numbers reproduced or taken from prior work?

The statement that back-translated views are pre-computed but that CurCon is slower because of on-the-fly augmentation also needs clarification.

#### 5. Possible confounding from augmentation composition

The full CurCon schedule may differ from the fixed-mixture baseline not only in ordering but also in the number and frequency of augmentations seen at different points in training. The fixed-mixture ablation therefore does not isolate curriculum ordering cleanly. A stronger control would match the total frequency of each augmentation and compare only the ordering, or evaluate several schedules with identical augmentation counts.

Similarly, the “reversed curriculum” result is useful, but it does not establish that the proposed ordering is optimal relative to random schedules, cosine schedules, delayed schedules, or other matched alternatives.

#### 6. Scope of evaluation

The experiments cover only four short English classification datasets and one encoder family. This limits evidence for generality. The use of external resources such as WordNet and German back-translation may also make the approach less portable across domains and languages.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 52/100 |
| Novelty |  fifty-five/100 |
| Significance | 55/100 |
| Clarity | 78/100 |

Using 55 for Novelty, the final average is:

\[
\frac{52 + 55 + 55 + 78}{4} = 60.0
\]

## Final recommendation: **Reject**

The paper is clearly written and reports a potentially useful empirical idea, but the contribution is incremental and the experimental evidence does not yet establish that the curriculum itself—rather than tuning advantages or changes in augmentation composition—causes the improvements. A stronger revision would require fairer baseline tuning, clearer implementation details, statistically supported ablations, and better-controlled schedule comparisons.