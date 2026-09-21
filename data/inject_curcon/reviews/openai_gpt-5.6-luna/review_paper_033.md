## Review

### Summary
The paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The central idea is to begin contrastive training with weak augmentations and progressively introduce stronger ones, including span deletion and back-translation. Experiments on four datasets with 500 labeled examples report consistent improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The proposed method is simple, intuitive, and easy to integrate into existing contrastive-training pipelines.
- The paper evaluates multiple datasets and reports results over five random seeds.
- The ablation comparing the full curriculum, fixed augmentation, reversed curriculum, and removal of back-translation is useful.
- The analysis across different label budgets supports the claim that the method is most beneficial in low-resource settings.
- The paper is generally well organized and readable.

### Concerns

#### 1. Unfair and insufficiently controlled baseline tuning
The most serious issue is that CurCon is selected using a grid search over 48 configurations on each validation set, whereas the baselines use hyperparameters reported in their original papers. This gives CurCon a substantial tuning advantage, especially in a low-resource setting. All baselines should either receive comparable tuning budgets or be evaluated under a clearly specified common protocol.

#### 2. Limited evidence for the curriculum mechanism
The improvement over CERT is only 1.1 average points, and the curriculum-specific ablation contributes 0.8 points. No statistical significance tests or paired seed-level comparisons are provided. Given the small number of datasets and the reported standard deviations, it is unclear whether the gains are robust.

#### 3. Ambiguity in the augmentation schedule
The method description is not fully precise. It states both that operator availability is controlled by thresholds and that the “probability of applying each operator” is determined by the curriculum value. It is unclear whether the schedule changes augmentation probability continuously or only introduces operators at four discrete thresholds. The exact procedure for generating the two views is also underspecified.

#### 4. Dataset and label-sampling protocol needs more detail
The paper does not clearly specify how the 500 labeled examples and 200 validation examples are sampled, whether the validation set is fixed across seeds, or whether the unlabeled pool excludes all validation and test-related material. These details are important for reproducibility and for assessing possible contamination.

#### 5. Narrow experimental scope
The evaluation covers only four English classification datasets with short texts and one encoder architecture. There is no test of robustness across domains, languages, text lengths, augmentation qualities, or model sizes. The claimed generality of the method is therefore not well established.

#### 6. Cost and implementation claims are incomplete
The paper reports that CurCon is approximately 12% slower than CERT, but does not provide wall-clock times, preprocessing costs, or the cost of generating and storing back-translated examples. Since back-translation can dominate the computational budget, this distinction matters.

#### 7. Novelty is incremental
The core contribution is a manually designed easy-to-hard augmentation schedule. This is a reasonable engineering contribution, but it is a relatively direct application of curriculum learning to contrastive augmentation. The paper would benefit from stronger conceptual analysis or comparisons to alternative schedules, such as cosine, randomized, adaptive, or loss-based schedules.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 52/100 |
| Novelty | 58/100 |
| Significance | 55/100 |
| Clarity | 72/100 |

### Final average

\[
\frac{52 + 58 + 55 + 72}{4} = 59.25
\]

**Final score: 59.3/100**

## Recommendation: Reject

The paper presents a plausible and clearly described idea, and the empirical results are promising. However, the asymmetric hyperparameter tuning of CurCon versus the baselines, limited statistical analysis, and insufficient methodological details substantially weaken the evidence. I would encourage resubmission after adding a fair baseline-tuning protocol, stronger significance analysis, precise augmentation-schedule specifications, and broader experiments.