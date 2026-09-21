## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The method gradually increases the strength of text augmentations during contrastive pre-training, progressing from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples per dataset show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The reported gains are particularly strong in the lowest-label regime.

### Strengths

1. **Well-motivated problem.** The paper addresses a practically important setting in which only a few hundred labelled examples are available but unlabelled in-domain data can be exploited.
2. **Simple and implementable method.** CurCon modifies the augmentation policy without changing the downstream fine-tuning procedure or adding inference-time parameters.
3. **Consistent empirical improvements.** The method improves over CERT on all four datasets and obtains an average gain of 1.1 accuracy points over the strongest baseline.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons support the claim that scheduling, rather than only the augmentation set, contributes to performance.
5. **Low-resource analysis.** The results with 100, 500, and 1,000 labelled examples are helpful and show that the method is most beneficial when supervision is scarcest.
6. **Clear presentation.** The method, experimental pipeline, limitations, and computational cost are described concisely and are generally easy to follow.

### Weaknesses and suggestions

1. **Statistical significance is not reported.** Although the paper reports means and standard deviations over five seeds, it does not provide confidence intervals or paired significance tests. Given that some improvements are modest, especially at 1,000 labels, statistical testing would strengthen the conclusions.
2. **Baseline tuning is not fully comparable.** CurCon is tuned using a grid search on each validation set, whereas the baselines use hyperparameters from their original papers. This may favor the proposed method. A stronger comparison would tune all methods under the same validation protocol or report both original and re-tuned baselines.
3. **The schedule description could be more precise.** The paper characterizes the schedule as linear, but the operators are introduced through discrete thresholds. In addition, the definition \(c(t)=\min(1,t/L)\) is undefined when \(L=0\), even though \(L=0\) is used for the fixed-mixture ablation. The implementation convention for this case should be stated explicitly.
4. **The augmentation policy is somewhat underspecified.** It would be useful to clarify whether operators are applied independently or whether exactly one operator is sampled per view, how synonym replacement handles unavailable WordNet entries, and whether the two views use independent augmentation draws.
5. **Limited breadth of evaluation.** The experiments cover only four English datasets and one encoder architecture. The limitations acknowledge this appropriately, but additional domains or encoders would help establish broader generality.
6. **Ablation reporting could be expanded.** The ablation table reports only averages. Per-dataset results would reveal whether the curriculum is consistently helpful or whether the aggregate gain is driven by particular tasks. It would also be informative to compare alternative curriculum lengths and schedules.
7. **Some cost details merit clarification.** The paper states that back-translation is pre-computed but does not specify the translation model or preprocessing pipeline. Since synonym replacement and span deletion are performed on the fly, reporting absolute training times would make the 12% overhead more interpretable.

These issues primarily affect reproducibility, fairness of comparison, and the strength of the empirical claims rather than the core validity of the proposed approach. The reported results are internally consistent, and the ablations provide reasonable evidence that the curriculum contributes beyond simply using a stronger augmentation mixture.

## Scores

- **Soundness:** 83/100  
  The method and experiments are coherent, with useful ablations, though significance testing and uniformly tuned baselines would improve methodological rigor.

- **Novelty:** 79/100  
  Curriculum learning and contrastive intermediate training are established ideas, but applying an augmentation-strength curriculum to this setting is a meaningful and reasonably distinct combination.

- **Significance:** 82/100  
  The problem is important, the method is inexpensive to deploy, and the gains are consistent, particularly in the most label-scarce setting. Broader evaluation would increase confidence in the impact.

- **Clarity:** 87/100  
  The paper is well organized and generally clear. A few implementation details and the precise definition of the schedule should be clarified.

### Final average score

\[
\frac{83 + 79 + 82 + 87}{4} = 82.75
\]

**Final average: 82.75/100**

## Final recommendation

**Accept**

The paper presents a clear, practically relevant, and empirically supported improvement to contrastive intermediate training. While additional statistical analysis, more carefully matched baseline tuning, and expanded reproducibility details would strengthen the work, the current results and ablations are sufficient to support acceptance.