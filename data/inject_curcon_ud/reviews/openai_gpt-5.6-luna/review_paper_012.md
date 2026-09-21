## Review

### Summary

The paper proposes CurCon, a contrastive intermediate-training method that gradually increases augmentation strength during self-supervised training. It evaluates the method on four English classification datasets with 500 labelled examples per dataset and reports improvements over fine-tuning, UDA, SimCSE, and CERT. The central idea is intuitive and potentially useful, but the empirical evidence is not sufficiently rigorous to support the strength of the claims.

### Strengths

- The paper addresses an practically important low-resource classification setting.
- The proposed curriculum is simple, easy to understand, and adds no inference-time parameters.
- The paper includes several relevant baselines and ablations, including a fixed-mixture baseline and a reversed curriculum.
- Results are reported across four datasets and five random seeds.
- The writing and organization are generally clear, and the method can be understood without excessive notation.

### Main concerns

#### 1. Baseline tuning is not comparable

CurCon is selected using a grid search over 48 configurations for each dataset, whereas the baselines use hyperparameters from their original papers. This is a serious fairness issue, particularly in a 500-example regime where learning rates, temperatures, training duration, batch size, and regularization can substantially affect results. The reported gains may partly reflect differential hyperparameter optimization rather than the curriculum itself.

All methods should receive comparable tuning budgets, ideally using the same validation protocol and the same number of configurations.

#### 2. The empirical evidence is too limited for the claims

The paper reports mean and standard deviation over five seeds but provides no statistical significance tests, confidence intervals, or per-seed results. Several improvements are relatively small, especially on AG News and TREC. It is therefore difficult to determine whether the gains are robust.

The ablation table is particularly weak because it reports only averages, without standard deviations or dataset-level results. The claim that the curriculum itself contributes 0.8 points would be more convincing if supported by paired seed-level comparisons across datasets.

#### 3. Method specification is incomplete

Important implementation details are missing:

- Which back-translation model and decoding settings are used?
- Are the back-translated sentences precomputed once or regenerated?
- How are WordNet synonym ambiguities, inflections, subword tokenization, and short sentences handled?
- Are the two contrastive views sampled independently?
- What exact BERT checkpoint, projection-head dimensions, maximum sequence length, optimizer schedule, and temperature are used?
- How is the unlabeled pool constructed relative to the 500 labelled examples and the 200 validation examples?

These details matter because the augmentation policy is the core contribution and because external translation and lexical resources can have large effects.

#### 4. The curriculum is not actually a smooth linear increase in difficulty

Although the curriculum level is defined linearly, the augmentation policy changes at discrete thresholds: operators become available at 0.25, 0.5, and 0.75, after which they are sampled uniformly. Thus, the effective augmentation distribution changes abruptly rather than linearly. More importantly, the paper does not measure whether these operators are truly ordered by semantic difficulty. Back-translation is not necessarily harder than span deletion, and the interaction between operators and sentence length may vary considerably.

A stronger study would compare multiple schedules, continuously vary operator probabilities, and measure pair difficulty or semantic similarity directly.

#### 5. Ablation design does not isolate all relevant factors

The fixed-mixture comparison is useful, but the paper does not establish whether the gain comes from:

- gradual exposure to stronger augmentations,
- the changing augmentation distribution,
- spending early training steps on token dropout,
- different effective numbers of back-translation examples,
- or simply a longer/more favorable training trajectory.

The “without back-translation” condition also changes the augmentation family, not just one component of the curriculum. Additional controls are needed, such as a fixed policy matched to the same operator frequencies and a schedule-matched policy with randomly ordered operators.

#### 6. Claims about generality are premature

The evaluation covers only short English classification datasets and one encoder. This is acknowledged in the limitations, but it substantially limits the significance of the conclusions. There is no evaluation on longer documents, domain-specific data, multilingual data, or more modern encoders. The method’s dependence on WordNet and back-translation also raises questions about transferability.

### Minor concerns

- The paper should distinguish more carefully between “augmentation strength” and augmentation type availability.
- The relation between the stated 12% computational overhead and the use of precomputed back-translation should be explained more precisely.
- The choice of 20,000 contrastive steps and the curriculum length selected during validation should be reported for each dataset.
- The paper would benefit from reporting validation performance and test-set variance separately.
- The citation and characterization of CERT should be checked carefully, including whether the implementation and augmentation policy match the cited work.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 51/100 |
| Novelty | 62/100 |
| Significance | 56/100 |
| Clarity | 78/100 |

### Final average

\[
\frac{51 + 62 + 56 + 78}{4} = 61.75
\]

**Final average: 61.8/100**

## Recommendation: Reject

The idea is clear and plausible, and the results are encouraging. However, the current evidence does not establish that the reported improvements are attributable to the curriculum rather than unequal hyperparameter tuning, augmentation-distribution differences, or implementation choices. A revised submission with fair baseline tuning, stronger statistical analysis, fuller methodological details, and more discriminating ablations could become a solid contribution.