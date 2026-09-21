## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually increases the strength of text augmentations during contrastive pretraining, moving from token dropout toward synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show improvements over fine-tuning, UDA, SimCSE, and CERT. The reported gains are supported by ablations and by experiments varying the number of labelled examples.

### Strengths

1. **Clear motivation.** The paper identifies a plausible limitation of fixed augmentation policies: strong augmentations may be difficult early in training, while weak augmentations may provide insufficient learning signal later.
2. **Simple and practical method.** CurCon requires no architectural changes or inference-time overhead and can be incorporated into an existing CERT-style pipeline.
3. **Relevant low-resource setting.** The focus on 500 or fewer labelled examples is practically meaningful and appropriate for studying intermediate representation learning.
4. **Consistent empirical gains.** CurCon improves over CERT on all four datasets and reports gains across multiple label budgets.
5. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that the schedule, rather than merely the use of augmentations, contributes to performance.
6. **Good presentation.** The method, experimental pipeline, results, limitations, and computational cost are described clearly.

### Soundness

The experimental design is generally appropriate, and the reported results support the central claim that a curriculum can improve contrastive intermediate training. Reporting mean and standard deviation over five seeds is useful, and the ablations provide a reasonable initial test of the proposed mechanism.

Several details would benefit from clarification or stronger controls:

- The probability distribution over available augmentation operators is not fully specified. The text states that operators are “determined by” the curriculum level and that available operators are sampled uniformly, but it is unclear whether the operator set changes discretely at the thresholds or whether augmentation magnitudes also scale continuously with \(c(t)\).
- CurCon receives a grid search over 48 configurations per dataset, whereas baselines use hyperparameters from their original papers. A controlled comparison would ideally tune all methods under the same validation protocol.
- Statistical significance tests or paired seed-level comparisons would strengthen the claim that the improvements are reliable, particularly for the smaller gains on TREC and the 1,000-label setting.
- The treatment of unlabelled data and any preprocessing overlap between labelled, validation, and contrastive examples should be described more explicitly.
- Since the study uses relatively short English benchmark texts, it is not yet clear how robust the approach is to longer documents, domain shift, or languages without WordNet-quality resources.

These are mostly issues of experimental completeness and reproducibility rather than fundamental flaws. The core method is technically coherent, and the evidence is sufficient for the main claims at the current scope.

### Novelty

The central idea—scheduling augmentation difficulty in contrastive intermediate training—is intuitive but worthwhile. Curriculum learning, contrastive learning, and augmentation scheduling are individually established, so the novelty lies primarily in their integration for low-resource text classification and in the systematic comparison of an increasing-strength schedule against fixed and reversed schedules.

The contribution is therefore incremental rather than highly novel. Nevertheless, the method addresses a relevant gap and is sufficiently distinct from standard CERT and SimCSE-style pipelines to constitute a useful contribution.

### Significance

The reported average improvement of 1.1 points over CERT and 3.8 points over direct fine-tuning is meaningful in the low-resource regime. The stronger gain with only 100 labelled examples is particularly relevant to the paper’s motivation. The method is also computationally and architecturally lightweight, which increases its practical value.

The significance would be further improved by evaluations on more varied domains, larger datasets, additional encoder families, or more competitive tuning of the baselines. Still, within the paper’s stated scope, the contribution is useful and likely to interest researchers working on low-resource adaptation and semi-supervised representation learning.

### Clarity

The paper is well organized and easy to follow. The motivation, method, experimental setup, and limitations are clearly stated. Tables are concise and directly support the claims. The paper would be even clearer if it included:

- pseudocode or a diagram of the curriculum schedule;
- the exact augmentation probabilities and implementation details;
- the selected curriculum lengths for each dataset;
- confidence intervals or seed-level results;
- a more explicit discussion of how CurCon differs from simply applying a time-varying mixture of augmentation policies.

These are modest presentation and reproducibility improvements.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 84/100 |
| Novelty | 78/100 |
| Significance | 82/100 |
| Clarity | 90/100 |

### Final average

\[
\frac{84 + 78 + 82 + 90}{4} = \frac{334}{4} = 83.5
\]

**Final average score: 83.5/100**

## Final Recommendation: **Accept**

The paper presents a clear, practically motivated, and empirically supported improvement to contrastive intermediate training for low-resource text classification. Although the novelty is moderate and the experimental comparisons could be made more rigorous through uniform hyperparameter tuning and stronger statistical analysis, the method is simple, the gains are consistent, and the contribution is appropriate for acceptance. Minor revisions should clarify the scheduling probabilities, improve reproducibility, and strengthen the discussion of baseline tuning and statistical reliability.