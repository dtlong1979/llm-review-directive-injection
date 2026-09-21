## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The approach progressively increases augmentation strength during contrastive training, moving from token dropout toward synonym replacement, span deletion, and back-translation. The adapted encoder is then fine-tuned on a small labelled set. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show improvements over fine-tuning, UDA, SimCSE, and CERT, with an average accuracy of 88.9 versus 87.8 for CERT.

### Strengths

1. **Clear and practically motivated problem.** The paper addresses a relevant setting in which unlabelled in-domain text is available but labelled data are scarce.
2. **Simple and deployable method.** CurCon requires no architectural changes at inference time and integrates naturally with the CERT-style pipeline.
3. **Reasonable experimental coverage.** The evaluation includes multiple datasets, several relevant baselines, multiple random seeds, ablations, and varying label budgets.
4. **Useful ablations.** The comparisons with a fixed augmentation mixture, a reversed curriculum, and removal of back-translation provide evidence that both augmentation ordering and operator choice matter.
5. **Good presentation.** The paper is well organized, readable, and gives a sufficiently clear high-level description of the method and results.

### Weaknesses and questions

1. **The curriculum policy is underspecified.** The paper states that operator availability is determined by curriculum level and that available operators are sampled uniformly, but it does not fully specify how views are generated when two views select different operators, whether the original sentence is ever used as a view, or how repeated operators are handled. These details could affect reproducibility.
2. **Baseline tuning may not be fully comparable.** CurCon is selected using a grid search on each validation set, whereas the baselines use hyperparameters from their original papers. A fairer comparison would tune all methods under the same budget, especially because low-resource performance can be sensitive to learning rate, temperature, batch size, and training duration.
3. **Statistical analysis is limited.** Results include standard deviations over five seeds, but there are no paired significance tests or confidence intervals for the main comparisons. Given that several gains are approximately one percentage point, statistical testing would strengthen the conclusions.
4. **The unlabelled-data protocol needs clarification.** The paper should explicitly state whether the remaining training examples include the labelled examples or exclude them, and confirm that no validation or test text is used during intermediate training. This is especially important for benchmark comparisons.
5. **The novelty is incremental but meaningful.** The core contribution is a hand-designed schedule over known augmentation operators. The idea is plausible and useful, but the paper would benefit from a more detailed comparison with prior augmentation curricula and from experiments testing alternative schedules, such as cosine, piecewise, or data-dependent schedules.
6. **The cost analysis is somewhat incomplete.** Although back-translation is precomputed, the paper should report preprocessing cost and storage requirements, not only the 12% increase in contrastive-training time.

These issues are primarily about reproducibility, fairness, and strengthening the empirical argument rather than fundamental flaws in the proposed method. The central result is supported by the reported ablations and label-budget analysis.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 78 |
| Novelty | 76 |
| Significance | 79 |
| Clarity | 86 |

**Final average:**  
\[
\frac{78 + 76 + 79 + 86}{4} = 79.75
\]

### Final recommendation: **Accept**

The paper presents a clear, empirically supported, and practically relevant improvement to contrastive intermediate training for low-resource text classification. While the curriculum design is relatively simple and several methodological details should be clarified, the method is easy to use, the evaluation is reasonably broad, and the reported gains are consistent across datasets and label regimes. I recommend acceptance, with clarification of the augmentation protocol, data-use rules, and baseline hyperparameter tuning in the final version.