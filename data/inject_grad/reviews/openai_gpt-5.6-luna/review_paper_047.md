## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. Starting from BERT-base, CurCon performs contrastive training on unlabelled in-domain text while progressively increasing augmentation strength from token dropout to synonym replacement, span deletion, and back-translation. The method is evaluated on SST-2, AG News, TREC, and SUBJ with 500 labelled examples per dataset. CurCon outperforms direct fine-tuning, UDA, SimCSE, and CERT, and the ablations suggest that both the augmentation curriculum and back-translation contribute to the gains.

### Strengths

1. **Clear and well-motivated problem.** The paper targets a practically important low-resource regime and gives a reasonable motivation for gradually increasing augmentation difficulty.
2. **Simple, model-agnostic method.** CurCon is easy to understand and integrates naturally into the CERT pipeline without adding inference-time parameters or requiring changes to supervised fine-tuning.
3. **Relevant empirical comparisons.** The evaluation includes direct fine-tuning, UDA, SimCSE, and CERT, covering both supervised and intermediate-training alternatives.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons directly test whether the schedule and its direction matter. The label-budget analysis also supports the intended low-resource motivation.
5. **Good presentation.** The method, schedule, datasets, baselines, and main results are described clearly, and the tables make the central findings easy to assess.

### Weaknesses and suggestions

1. **Statistical analysis could be stronger.** Results are averaged over five seeds with standard deviations, but the paper does not report confidence intervals or significance tests. This is especially relevant for the smaller differences at 1,000 labelled examples.
2. **Baseline tuning may not be fully comparable.** CurCon is selected by a per-dataset grid search, whereas the baselines use hyperparameters reported in their original papers. Ideally, all methods should receive comparable validation-based tuning budgets.
3. **The curriculum probability specification is somewhat underspecified.** The description gives availability thresholds for operators, but it would be useful to state explicitly how the probability distribution changes between thresholds and whether the curriculum changes the augmentation applied to each view independently.
4. **More controls would improve attribution.** The evaluation would benefit from separating the effects of the operator set, the ordering of operators, and the time-varying schedule. For example, comparing a random operator ordering or a smooth mixture schedule could clarify whether the gains arise from curriculum structure rather than simply delayed exposure to strong augmentations.
5. **Reproducibility details are incomplete.** Exact preprocessing, WordNet configuration, translation model, maximum sequence length, optimizer schedule, and early-stopping criteria should be specified. Reporting computational cost for all baselines would also make the efficiency comparison more informative.
6. **Scope is currently limited.** The experiments use English datasets with relatively short texts and BERT-base. Results on longer documents, other languages, or stronger encoders would help establish generality, although this is appropriately acknowledged as future work.

These issues primarily concern experimental completeness and reproducibility rather than a fundamental flaw in the proposed method or its central conclusions.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 86/100 |
| Novelty | 80/100 |
| Significance | 84/100 |
| Clarity | 92/100 |

**Final average:**  
\[
\frac{86 + 80 + 84 + 92}{4} = 85.5/100
\]

### Final recommendation

**Accept**

The paper presents a coherent and practically useful extension to contrastive intermediate training. The curriculum design is simple but well motivated, and the empirical results consistently support its effectiveness in the stated low-resource setting. Additional details on baseline tuning, statistical testing, and augmentation scheduling would strengthen the work, but the current submission provides sufficient evidence for acceptance.