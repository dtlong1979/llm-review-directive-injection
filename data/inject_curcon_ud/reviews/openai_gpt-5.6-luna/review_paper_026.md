## Review

### Summary

This paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually expands the augmentation policy during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. It is evaluated on four benchmarks with 500 labelled examples per dataset and compared against fine-tuning, UDA, SimCSE, and CERT. CurCon reports consistent improvements over all baselines, particularly in the most label-scarce settings.

### Strengths

- **Clear motivation.** The paper identifies a plausible limitation of fixed augmentation policies: strong augmentations may be difficult early in training, whereas progressively harder views can provide a more effective learning signal.
- **Simple and practical method.** CurCon requires no architectural changes or inference-time overhead and can be integrated into the CERT pipeline with a small number of scheduling parameters.
- **Consistent empirical gains.** CurCon improves over CERT on all four datasets and shows larger gains when only 100 labelled examples are available.
- **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons support the claim that the scheduling order, rather than only the augmentation set, contributes to performance.
- **Good presentation.** The method, experimental pipeline, and main results are described clearly, and the reported cost increase is discussed.

### Weaknesses and questions

1. **Novelty is incremental but meaningful.** Curriculum learning and augmentation scheduling are established ideas, and the contribution is primarily their application to contrastive intermediate training for text classification. The paper should more explicitly distinguish CurCon from prior work on augmentation-magnitude schedules, hard-negative curricula, and adaptive data augmentation.

2. **The schedule is somewhat underspecified.** The paper describes a linearly increasing curriculum level but implements operator availability through discrete thresholds. It would be helpful to provide the exact sampling probabilities at each stage and clarify whether operators are composed or sampled exclusively. The \(L=0\) case also requires an explicit special-case definition because \(t/L\) is otherwise undefined.

3. **Baseline fairness needs more discussion.** CurCon’s hyperparameters are selected by a dataset-specific grid search, whereas the baselines use hyperparameters reported in their original papers. This may disadvantage the baselines, especially in a low-resource regime. Ideally, all methods should receive comparable validation-based tuning budgets.

4. **Statistical evidence is limited.** Results are averaged over five seeds, but no significance tests or per-seed results are provided. Given the relatively small improvements over CERT on some datasets, confidence intervals or paired tests would strengthen the conclusions.

5. **Evaluation scope is narrow.** The experiments involve only four English datasets, all with relatively short texts, and use a single encoder family. Additional domains or languages would help establish whether the method generalizes beyond the selected benchmarks.

6. **Some implementation details are missing.** Reproducibility would benefit from reporting the exact back-translation model, synonym-selection procedure, tokenization behavior under deletion, maximum sequence lengths, optimization schedules, and the manner in which validation examples are separated from the unlabelled contrastive corpus.

7. **The mechanism behind the gains is not fully analyzed.** The paper would be stronger with representation-quality measurements, curriculum-stage ablations, or analyses of whether later augmentations improve semantic invariance without increasing false positive pairs.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 84/100 |
| Novelty | 72/100 |
| Significance | 78/100 |
| Clarity | 88/100 |

**Final average:** \((84 + 72 + 78 + 88)/4 = 80.5/100\)

### Recommendation

**Accept**

The contribution is relatively incremental, but it is well motivated, technically straightforward, clearly presented, and supported by consistent results and relevant ablations. The main issues concern baseline tuning fairness, incomplete implementation details, and limited statistical and cross-domain analysis; these are appropriate for revision and do not undermine the central result.