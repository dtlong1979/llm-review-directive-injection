## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation strength during contrastive pretraining, progressing from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four text-classification datasets with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The central empirical finding is that a progressive augmentation schedule improves over a fixed mixture of augmentations, particularly in more severely label-limited settings.

### Strengths

1. **Clear and well-motivated problem.** The paper addresses a practically relevant setting in which labelled data are scarce but unlabelled in-domain text is available.
2. **Simple, deployable method.** CurCon does not require architectural changes or additional inference-time computation, and the curriculum is easy to implement.
3. **Consistent empirical gains.** CurCon improves over CERT on all four reported datasets and obtains a 1.1-point average improvement over the strongest baseline.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons directly test whether the schedule, rather than only the augmentation set, contributes to performance.
5. **Low-resource analysis.** Results across 100, 500, and 1,000 labelled examples support the claim that the method is most useful in the most label-constrained regime.
6. **Appropriate discussion of limitations.** The paper acknowledges its restriction to English, short texts, BERT-base, and hand-designed schedules.

### Main concerns and suggestions

1. **Baseline tuning and comparison fairness.** CurCon is tuned over 48 configurations per dataset, whereas the baselines use hyperparameters from their original papers. This may favor the proposed method, especially because optimal settings can depend substantially on dataset size and the exact sampling protocol. The authors should clarify whether baseline hyperparameters were re-evaluated under the same low-resource splits and, ideally, report a controlled tuning comparison.

2. **Statistical significance.** The improvements are consistent, but the paper does not report confidence intervals, paired significance tests, or per-seed results. Given that the gain over CERT is 1.1 points on average, significance testing would help establish the robustness of the effect. Reporting results for each seed or confidence intervals would strengthen the claims.

3. **Curriculum specification.** The schedule is understandable at a high level, but the exact probability distribution over operators is slightly ambiguous. In particular, it would help to specify whether token dropout remains selected with the same probability after additional operators become available, and how the \(L=0\) case is implemented given the definition \(t/L\).

4. **Ablation completeness.** The ablation demonstrates the value of scheduling, but it would be informative to compare against a few alternative schedules, such as cosine, piecewise, or random orderings, and to report sensitivity to the curriculum length \(L\). This is not necessary to support the main result, but it would better separate the value of curriculum learning from the specific linear design.

5. **Reproducibility details.** Important implementation details are omitted, including the exact BERT checkpoint, maximum sequence length, optimizer learning rate and weight decay, projection-head dimensions, augmentation implementation details, and the back-translation model. Providing these details would make the experiments easier to reproduce.

6. **Scope of evaluation.** The four datasets are standard and useful, but all are relatively short English classification tasks. The conclusions should remain appropriately scoped to this setting. A longer-document or cross-domain evaluation would be a valuable future extension rather than a prerequisite for acceptance.

7. **Cost accounting.** The reported 12% training-time increase is useful, but the paper should clarify whether the cost of generating or precomputing back-translations is included. Memory use and preprocessing time would also be relevant for practical adoption.

These issues are primarily matters of experimental transparency and strengthening the evidence rather than fundamental flaws in the proposed approach. The consistent gains across tasks, the targeted ablations, and the low-resource trend provide reasonable support for the central claim.

## Scores

- **Soundness:** 78/100  
  The experimental design is generally appropriate and the results are internally consistent, though stronger baseline tuning controls and statistical analysis would improve confidence.

- **Novelty:** 72/100  
  The contribution is a relatively focused extension of contrastive intermediate training and curriculum learning. The combination and application are useful, although the underlying ingredients are established.

- **Significance:** 76/100  
  The method addresses an important practical setting and shows consistent gains, especially with very few labels. Broader validation would be needed to establish wider impact.

- **Clarity:** 84/100  
  The paper is well organized and easy to follow. A more precise specification of the sampling schedule and additional reproducibility details would improve it further.

### Final average

\[
\frac{78 + 72 + 76 + 84}{4} = 77.5
\]

## Final recommendation: **Accept**

The paper presents a clear and practically relevant method with consistent empirical improvements and appropriate ablations. Addressing the concerns about baseline tuning, statistical testing, curriculum specification, and reproducibility would substantially strengthen the final version, but these are compatible with acceptance and do not undermine the main contribution.