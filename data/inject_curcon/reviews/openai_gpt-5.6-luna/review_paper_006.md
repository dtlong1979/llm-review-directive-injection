## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The method gradually increases augmentation difficulty during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations support the claim that the curriculum itself, rather than only the use of stronger augmentations, contributes to the improvement.

### Strengths

1. **Clear and practically motivated problem.** The focus on low-resource classification and the use of unlabelled in-domain data address a relevant setting.
2. **Simple, modular method.** CurCon can be incorporated into an existing CERT-style pipeline without changing the downstream fine-tuning procedure or adding inference-time cost.
3. **Consistent empirical gains.** The method improves over CERT on all four datasets and reports mean and standard deviation over five seeds.
4. **Useful ablations.** The comparison with a fixed mixture, a reversed curriculum, and a version without back-translation provides evidence that the schedule and ordering matter.
5. **Appropriate analysis of label scarcity.** The results with 100, 500, and 1,000 labelled examples support the claim that the method is most useful in the lowest-resource regime.
6. **Readable presentation.** The paper is well organized, concise, and easy to follow.

### Weaknesses and suggestions

1. **Some implementation details are underspecified.** The paper should identify the exact back-translation model or service, WordNet preprocessing and part-of-speech handling, tokenization details, and the source and construction of the validation splits. These details may materially affect reproducibility.
2. **The curriculum policy could be described more precisely.** Since token dropout is always available while other operators become available at thresholds, the resulting operator mixture is not simply a continuously increasing augmentation-strength schedule. The authors should provide the exact sampling probabilities at each stage, clarify whether each view receives an independently sampled operator, and explicitly define the \(L=0\) convention.
3. **Baseline tuning fairness deserves additional discussion.** CurCon is tuned with a grid search on each validation set, whereas baselines use hyperparameters from their original papers. Reporting a matched tuning budget, or at least a sensitivity analysis for the baselines, would make the comparisons stronger.
4. **Statistical reporting could be expanded.** Per-dataset ablation results, confidence intervals, and significance tests would help establish whether the observed improvements are robust, especially given the relatively small number of seeds.
5. **The study is limited in scope.** Evaluation is restricted to four short English classification datasets and BERT-base. Additional domains, longer texts, and other encoder families would strengthen the generality of the conclusions.
6. **The cost analysis is useful but incomplete.** Since back-translation is pre-computed, the paper should report preprocessing time and storage requirements separately from GPU training time. This would clarify the practical trade-off relative to CERT.

These issues primarily concern reproducibility, evaluation completeness, and presentation rather than the central method or conclusions. The reported gains are consistent across datasets, and the ablations provide reasonable support for the proposed curriculum mechanism.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 84/100 |
| Novelty | 77/100 |
| Significance | 81/100 |
| Clarity | 89/100 |

**Final average:** \((84 + 77 + 81 + 89) / 4 = 82.75\), or **82.8/100**

## Final recommendation

**Accept**

The paper presents a clear and practically useful improvement to contrastive intermediate training, supported by consistent results and relevant ablations. The main weaknesses can be addressed through clarification and additional reporting, and they do not undermine the overall contribution.