## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation difficulty during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations further suggest that both the curriculum ordering and back-translation contribute to performance.

### Strengths

- **Clear and practically motivated problem.** The focus on low-resource classification and the use of unlabelled in-domain data are highly relevant.
- **Simple, model-agnostic method.** CurCon can be incorporated into an existing CERT-style pipeline without modifying inference or downstream fine-tuning.
- **Consistent empirical gains.** CurCon outperforms all reported baselines on all four datasets, with an average improvement of 1.1 points over CERT and larger gains in the 100-label regime.
- **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that the schedule, rather than only the augmentation set, is important.
- **Reasonable analysis of label efficiency and cost.** The results indicate that the method is most useful when supervision is especially scarce, while the reported computational overhead is moderate.
- **Well organized presentation.** The method, experimental protocol, and main findings are easy to follow.

### Weaknesses and questions

1. **Baseline tuning and fairness.** CurCon hyperparameters are selected through a 48-configuration grid search, whereas the baselines use hyperparameters from their original papers. This may advantage CurCon, especially in a low-resource setting. A stronger comparison would tune all methods under the same validation protocol.
2. **Limited dataset and model coverage.** The evaluation is restricted to four English datasets with short texts and BERT-base. This limits evidence for generalization to longer documents, other languages, or larger and newer encoders.
3. **Statistical testing is incomplete.** Means and standard deviations over five seeds are reported, but no significance tests or per-seed results are provided. Given that some gains over CERT are relatively small, confidence intervals or paired significance tests would strengthen the claims.
4. **Curriculum specification could be more precise.** The interaction between “curriculum level,” operator availability, and uniform sampling should be stated more formally. In particular, the \(L=0\) case requires a special definition because \(t/L\) is otherwise undefined.
5. **Augmentation implementation details are insufficient.** The paper should specify the WordNet synonym-selection procedure, handling of invalid or semantically inappropriate replacements, the back-translation model, and whether augmentations are applied independently to each view.
6. **Potential confounds in the ablation.** The fixed-mixture baseline may have a different effective augmentation distribution from the curriculum at intermediate stages. Matching the total frequency of each operator would provide a cleaner test of curriculum ordering.
7. **Cost statement needs clarification.** The paper says that back-translated views are pre-computed but also attributes the overhead to on-the-fly operations. The preprocessing and training-time costs should be reported separately.

These issues are mostly about experimental completeness and reproducibility rather than fundamental flaws in the proposed approach. The consistent gains across tasks, the label-efficiency analysis, and the curriculum ablations provide a credible empirical basis for the central claim.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 84/100 |
| Novelty | 78/100 |
| Significance | 82/100 |
| Clarity | 88/100 |

**Final average:** \((84 + 78 + 82 + 88) / 4 = \mathbf{83.0/100}\)

### Final recommendation

**Accept**

The paper presents a clear and useful extension of contrastive intermediate training, supported by consistent results and relevant ablations. Addressing the baseline-tuning fairness, augmentation details, statistical testing, and cost accounting would improve the work, but the current evidence is sufficient for acceptance.