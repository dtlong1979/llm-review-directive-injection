## Review

### Summary

This paper introduces CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The method gradually increases augmentation strength during contrastive pretraining, progressing from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four benchmarks with 500 labelled examples demonstrate consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations support the claim that the curriculum, rather than contrastive training alone, contributes to the gains.

### Strengths

- **Clear and practically motivated problem.** The focus on low-resource classification and the use of unlabelled in-domain text are highly relevant.
- **Simple, intuitive method.** Scheduling augmentation difficulty is easy to understand and can be incorporated into existing CERT-style pipelines without inference-time modifications.
- **Consistent empirical improvements.** CurCon outperforms all listed baselines on all four datasets and improves over CERT by 1.1 average accuracy points.
- **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons directly address whether the ordering of augmentation strength matters.
- **Low-resource analysis.** Results across 100, 500, and 1,000 labelled examples support the claim that the method is most useful when labels are scarce.
- **Clear presentation.** The paper is well organized, the method is specified concisely, and the tables make the central findings easy to assess.

### Concerns and suggested revisions

1. **Baseline tuning should be described more carefully.** CurCon is selected using a 48-configuration grid search, whereas the baselines use hyperparameters from their original papers. This may give CurCon an advantage, particularly in a low-resource setting. The paper would be stronger if the authors clarified whether baseline hyperparameters were also tuned on the same validation splits, or provided an additional comparison with uniformly tuned baselines.

2. **Statistical testing is limited.** Results are averaged over five seeds, but no confidence intervals or paired significance tests are reported. Since several differences are relatively small, especially at 1,000 labels, reporting confidence intervals or per-seed results would improve the reliability of the conclusions.

3. **The curriculum specification could be made more precise.** The paper states both that operator availability is thresholded by the curriculum level and that the probability of applying each operator is determined by that level. It would help to provide pseudocode or an explicit probability formula. The treatment of the two views should also be clarified: are operators sampled independently for each view, and can the same operator be selected twice?

4. **The role of the curriculum length deserves more analysis.** Since curriculum length is the principal method-specific hyperparameter, a plot or table showing performance across several values of \(L\) would help establish robustness and clarify whether the chosen schedule is broadly useful or highly dataset-dependent.

5. **Augmentation quality and reproducibility.** WordNet synonym replacement and back-translation can produce noisy or label-changing examples, especially for sentiment and subjectivity. More details about the translation model, filtering, random seeds, and handling of short sentences would improve reproducibility.

6. **Scope of evaluation.** The experiments use four relatively short English datasets and one encoder architecture. This is a reasonable initial evaluation, but the claims should remain appropriately scoped. Evaluation on at least one longer-text or multilingual dataset would strengthen the generality of the conclusions, though it is not essential for acceptance.

These issues are primarily about experimental transparency and robustness rather than fundamental flaws in the proposed method. The reported ablations and consistent gains make the central claim credible.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 87/100 |
| Novelty | 80/100 |
| Significance | 84/100 |
| Clarity | 91/100 |

### Final average

\[
\frac{87 + 80 + 84 + 91}{4} = 85.5
\]

**Final average score: 85.5/100**

## Final recommendation: **Accept**

The paper presents a clear and useful extension to contrastive intermediate training, with convincing initial empirical evidence and relevant ablations. The concerns about baseline tuning, statistical reporting, and schedule specification should be addressed in revision, but they do not undermine the core contribution.