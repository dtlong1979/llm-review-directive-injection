## Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The method gradually increases augmentation strength during contrastive training, progressing from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations support the contribution of the curriculum schedule, and the gains are larger in the lower-label regime.

## Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **84** | The method is clearly specified at a high level, the experimental comparisons are appropriate, and the results are consistent across four datasets and multiple random seeds. The ablations support the claims about curriculum scheduling. Some details would benefit from clarification, including the exact augmentation sampling probabilities, the treatment of validation data, and whether all baselines received equally extensive hyperparameter tuning. |
| **Novelty** | **74** | Curriculum learning and contrastive intermediate training are established ideas, but applying a progressively stronger augmentation schedule to CERT-style intermediate training is a useful and reasonably distinct combination. The novelty is incremental rather than foundational, and the paper would benefit from a clearer comparison with related augmentation-scheduling approaches. |
| **Significance** | **81** | Low-resource classification is practically important, and the method provides consistent gains over strong baselines, especially with 100 labelled examples. The method is simple, incurs no inference cost, and can be integrated into an existing training pipeline. The scope is somewhat limited by the use of English, short-text benchmarks, and BERT-base. |
| **Clarity** | **88** | The paper is well organized and easy to follow. The method, curriculum stages, experimental setup, and results are presented clearly. A few implementation details—particularly the precise probability schedule and the construction of augmented views—should be made more explicit for reproducibility. |

### Final average

\[
\frac{84 + 74 + 81 + 88}{4} = \frac{327}{4} = \mathbf{81.75}
\]

**Final average score: 81.75/100**

## Strengths

1. **Clear and practical motivation.** The paper addresses a realistic low-resource setting where intermediate adaptation can be valuable.
2. **Simple method with low deployment overhead.** CurCon adds no inference-time parameters or computation.
3. **Consistent empirical gains.** CurCon outperforms all listed baselines on each of the four datasets.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that both curriculum direction and scheduling matter.
5. **Low-label analysis.** The results with 100, 500, and 1,000 labelled examples support the claim that the method is most helpful when supervision is scarce.
6. **Good presentation.** The paper is concise, coherent, and generally easy to reproduce from the description.

## Weaknesses and suggested improvements

1. **The augmentation policy needs more precise specification.** The manuscript defines availability thresholds but does not fully state how the probabilities of operators evolve before and after each threshold. Explicit pseudocode or a probability table would improve reproducibility.
2. **Baseline tuning may not be fully comparable.** CurCon is selected using a grid search on each validation set, whereas baselines use hyperparameters from their original papers. Equal tuning budgets or a sensitivity analysis would strengthen the comparison.
3. **The novelty is incremental.** The contribution is a well-motivated integration of curriculum scheduling with contrastive intermediate training, but the paper should more explicitly distinguish itself from prior work on augmentation magnitude schedules and curriculum contrastive learning.
4. **Statistical reporting could be expanded.** Five seeds and standard deviations are useful, but confidence intervals or paired significance tests would make the claims of consistent improvement more rigorous.
5. **Limited breadth of evaluation.** Additional domains, languages, encoder sizes, or longer-text datasets would help establish generality. This is appropriately acknowledged as a limitation.
6. **Potential resource and reproducibility details.** The paper should report the translation model, WordNet configuration, sampling procedure across seeds, and whether the unlabelled pool includes any examples used for validation.

## Overall assessment

The paper presents a technically straightforward but useful improvement to contrastive intermediate training. The empirical gains are consistent, the ablations are directionally convincing, and the approach is relevant to low-resource text classification. While the novelty is moderate and several experimental details should be clarified, these issues do not undermine the central contribution.

## Final recommendation: **Accept**