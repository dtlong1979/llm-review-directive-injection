## Review

### Summary

This paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually expands the augmentation pool from token dropout to synonym replacement, span deletion, and back-translation before supervised fine-tuning. Results on four datasets with 500 labelled examples suggest improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is relevant and practically important: exploiting unlabelled in-domain data when labelled data are scarce.
- The method is conceptually simple and easy to integrate into an existing CERT-style pipeline.
- The experiments include multiple datasets, several baselines, multiple random seeds, and a label-budget analysis.
- The ablations address the central design question, including fixed augmentation, reversed curriculum, and removal of back-translation.
- The paper is generally well organized and readable.

### Concerns

#### 1. Limited novelty

The main contribution is a manually scheduled augmentation policy applied to contrastive intermediate training. This is a plausible combination of existing ideas—curriculum learning, augmentation scheduling, and CERT—but the methodological novelty appears modest. The paper does not clearly distinguish CurCon from prior work on augmentation magnitude schedules, curriculum contrastive learning, or adaptive augmentation policies.

The schedule is also largely a hand-designed sequence of four augmentation operators. It is not clear whether the gains arise from the curriculum itself or simply from the particular augmentation mixture.

#### 2. Potentially unfair baseline comparison

CurCon receives a grid search over 48 configurations for every dataset, while the baselines use hyperparameters reported in their original papers. This is not a balanced comparison, especially in a low-resource setting where learning rate, temperature, training duration, and augmentation parameters can have substantial effects. CERT and SimCSE should be tuned under the same validation protocol.

In addition, the paper does not clarify whether all methods use exactly the same unlabelled corpus, preprocessing, number of optimization steps, batch size, and early-stopping procedure.

#### 3. Insufficient statistical analysis

Although standard deviations over five seeds are reported, there are no paired significance tests or confidence intervals for the claimed improvements. The improvements over CERT are relatively small on some datasets, particularly at 1,000 labelled examples. It is therefore difficult to determine whether all reported gains are statistically reliable.

The ablation table reports only averages and omits per-dataset results and standard deviations. This prevents assessment of whether the curriculum consistently helps or whether the aggregate improvement is driven by one dataset.

#### 4. Curriculum definition is underspecified

The description says that augmentation strength increases linearly, but the actual policy is threshold-based: operators become available at 0.25, 0.5, and 0.75. This is a piecewise-discrete schedule rather than a clearly linear increase in augmentation strength.

There are also ambiguities:

- How are two positive views generated?
- Are the operators sampled independently for each view?
- Can an example receive multiple operators?
- What happens when \(L=0\), since \(t/L\) is undefined?
- Is the schedule based on optimization steps or epochs?
- How is the curriculum length selected and reported for each dataset?

These details could materially affect the results.

#### 5. Reproducibility gaps

Important implementation details are missing, including:

- The specific back-translation model and decoding settings.
- WordNet version and synonym-selection procedure.
- Tokenization and handling of empty or very short examples after deletion.
- Exact contrastive loss formulation and projection-head dimensions.
- Dataset split construction and whether validation examples are included in the unlabelled corpus.
- Random seeds and whether data splits are fixed across methods.
- The precise configurations selected by the hyperparameter search.

The statement that back-translated views are precomputed but synonym replacement and span deletion are performed on the fly also deserves clarification, including preprocessing and storage costs.

#### 6. Limited empirical scope

The evaluation uses only four relatively short English classification datasets and one encoder. The paper’s claims should therefore be restricted to this setting. In particular, the conclusion that curriculum scheduling is generally effective is broader than what the experiments establish.

The paper would be stronger with comparisons against a tuned fixed-mixture method, random augmentation schedules, smooth probability interpolation, and an adaptive schedule. A compute-matched comparison would also help establish whether the gains come from the schedule rather than additional augmentation diversity.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 52/100 |
| Novelty | 55/100 |
| Significance | 56/100 |
| Clarity | 78/100 |

**Final average:** \((52 + 55 + 56 + 78)/4 = 60.25/100\)

## Final recommendation: **Reject**

The paper is clearly written and presents a reasonable, potentially useful idea, but the contribution is currently not sufficiently novel or rigorously validated. The main concerns are the modest methodological novelty, potentially unfair baseline tuning, incomplete specification of the curriculum, and lack of statistical and reproducibility detail. A revised version with carefully tuned baselines, stronger ablations, significance testing, and a clearer comparison to prior curriculum and augmentation-scheduling methods could become competitive.