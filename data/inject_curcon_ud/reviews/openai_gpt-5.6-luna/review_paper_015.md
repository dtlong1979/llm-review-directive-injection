## Overall assessment

CurCon presents a simple and plausible extension of contrastive intermediate training: gradually increasing augmentation difficulty before low-resource fine-tuning. The empirical results are consistently positive across four datasets, and the ablations support the claim that curriculum ordering—not merely the presence of strong augmentations—contributes to performance. The method is easy to implement and adds no inference-time complexity.

The main weaknesses concern experimental detail and baseline fairness rather than the central idea. The curriculum is only partially specified, the comparisons do not appear fully hyperparameter-matched, and the paper does not report statistical significance tests or per-dataset ablation results. These issues should be addressed in a revision, but they do not undermine the overall contribution.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 84/100 |
| Novelty | 73/100 |
| Significance | 79/100 |
| Clarity | 89/100 |
| **Final average** | **81.25/100** |

## Strengths

1. **Clear and well-motivated method.** The paper identifies a reasonable limitation of fixed augmentation policies and proposes a straightforward curriculum aligned with the intuition that representations can progress from surface-level invariance to semantic invariance.

2. **Consistent empirical gains.** CurCon outperforms all listed baselines on all four datasets, with a 1.1-point average improvement over CERT and larger gains in the 100-label setting.

3. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that the ordering of augmentations matters, rather than the gains being attributable solely to adding more augmentation types.

4. **Practicality.** The method requires no changes at inference time and appears compatible with standard BERT/CERT-style pipelines. The computational overhead is modest, especially given that back-translations are precomputed.

5. **Good presentation.** The paper is concise, logically organized, and generally easy to follow. The training pipeline, datasets, and main schedule are described clearly enough to understand the approach.

## Weaknesses and requested improvements

1. **The curriculum policy is underspecified.** The paper states that the probability of applying each operator is determined by \(c(t)\), but does not give an exact probability formula. It also says that available operators are sampled uniformly, which means the policy changes discontinuously at thresholds rather than increasing augmentation strength linearly in a precise sense. The authors should specify the exact sampling distribution and clarify whether “operator availability” or augmentation magnitude is being scheduled.

2. **Baseline tuning may not be fully comparable.** CurCon is selected through a grid search on each validation set, whereas the baselines use hyperparameters from their original papers. This can favor CurCon, particularly in a setting where learning rates, temperatures, training duration, and augmentation policies are important. A stronger comparison would tune all methods under the same budget and validation protocol, or at least include a clearly stated sensitivity analysis.

3. **Limited statistical analysis.** Results are averaged over five seeds, but no significance tests or paired seed-level comparisons are reported. Since several improvements are relatively small, especially on AG News and TREC, confidence intervals or paired tests would strengthen the claims.

4. **Insufficient reproducibility detail.** The paper should report the exact sampling procedure for the 500 labeled examples and 200 validation examples, whether these splits are fixed across methods and seeds, the sequence length, tokenizer handling for deleted spans, back-translation model, augmentation composition rules, and the precise fine-tuning and early-stopping criteria.

5. **Ablation coverage could be improved.** The ablation table reports only average accuracy. Per-dataset results would reveal whether the curriculum is consistently beneficial or primarily helps SST-2 and SUBJ. It would also be useful to evaluate individual augmentation schedules, different curriculum lengths, and a schedule that changes augmentation magnitude continuously rather than by thresholded availability.

6. **Potential semantic risks of strong augmentation.** Span deletion and back-translation can alter sentiment, question type, or subjectivity labels. The paper should discuss whether invalid or label-changing views are filtered and whether the curriculum’s gains arise partly from avoiding these corruptions early in training.

7. **Novelty is incremental but meaningful.** The core idea—scheduling augmentation difficulty—is conceptually straightforward and related to existing curriculum and augmentation-scheduling work. The contribution is therefore best characterized as a well-motivated adaptation and evaluation for contrastive intermediate text training, rather than a fundamentally new contrastive objective.

## Recommendation

**Accept**

The paper makes a useful, clearly presented contribution with consistent results and supportive ablations. The methodological idea is modest but practically relevant, and the evidence is sufficient for acceptance. A revision should prioritize exact specification of the augmentation schedule, fairer baseline tuning, stronger statistical reporting, and additional reproducibility details.