## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually increases the strength of text augmentations during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations suggest that both the curriculum and the use of back-translation contribute to performance.

### Strengths

1. **Clear and practically motivated problem.** The paper addresses an important setting in which labelled data are scarce but unlabelled in-domain data are available.
2. **Simple method with low deployment cost.** The curriculum affects only intermediate training and adds no inference-time parameters or computation.
3. **Consistent empirical gains.** CurCon improves over CERT on all four datasets and obtains an average gain of 1.1 accuracy points over the strongest baseline.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons directly test whether the schedule matters.
5. **Low-resource analysis.** Results with 100, 500, and 1,000 labelled examples support the claim that the method is especially helpful when supervision is limited.
6. **Generally clear presentation.** The training pipeline, augmentation operators, curriculum thresholds, datasets, and evaluation protocol are described in a relatively accessible manner.

### Weaknesses and concerns

1. **Limited methodological novelty.** The core contribution is a manually designed augmentation curriculum applied to an existing contrastive intermediate-training pipeline. This is a reasonable and useful contribution, but the conceptual novelty is moderate rather than substantial.
2. **Schedule description could be more precise.** The paper describes the strength as increasing linearly, but the actual policy is threshold-based availability of discrete augmentations, followed by uniform sampling. It would be helpful to distinguish more clearly between a continuous curriculum strength and a staged augmentation policy.
3. **Baseline tuning may not be fully comparable.** CurCon is selected using a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters from their original papers. Tuning all methods under the same protocol would strengthen the comparison.
4. **Limited statistical analysis.** Results report means and standard deviations over five seeds, but there are no confidence intervals, paired significance tests, or per-seed comparisons. Given the relatively modest gains over CERT, statistical testing would be valuable.
5. **Ablations are aggregated.** The ablation table reports only average accuracy. Per-dataset ablations would clarify whether the curriculum is consistently beneficial or whether the result is dominated by particular datasets.
6. **Reproducibility details are incomplete.** Important implementation information is missing, including the exact BERT checkpoint, maximum sequence length, projection-head dimensions, optimizer learning rates, augmentation sampling details, back-translation system, and early-stopping criteria.
7. **Scope is narrow.** All datasets are English and relatively short-text classification benchmarks, and only BERT-base is evaluated. The paper therefore provides limited evidence about generalization to other domains, languages, or model families.
8. **Potential computational trade-offs deserve more detail.** The reported 12% training-time increase is useful, but the cost of generating or storing back-translated examples and the total preprocessing cost should also be reported.

### Soundness

The experimental design is broadly appropriate, and the reported results support the main claims. The use of multiple datasets, multiple seeds, controlled ablations, and label-budget comparisons is a strength. However, the uneven hyperparameter tuning between CurCon and the baselines, incomplete implementation details, and lack of statistical testing somewhat weaken the strength of the evidence. The central method is nevertheless technically coherent and the conclusions are mostly supported.

**Score: 80/100**

### Novelty

The proposed curriculum for augmentation strength is intuitive and reasonably well motivated, but it builds directly on established contrastive intermediate training, standard text augmentations, and curriculum-learning ideas. The contribution is a useful combination and empirical demonstration rather than a fundamentally new objective or learning framework.

**Score: 75/100**

### Significance

The problem is important, and the method is simple enough to be adopted by practitioners working with small labelled datasets. The gains are consistent and particularly relevant in the 100-example setting. The significance is moderated by the relatively small absolute improvements over CERT and the limited experimental scope.

**Score: 78/100**

### Clarity

The paper is well organized and generally easy to follow. The motivation, method, experimental setup, and results are presented clearly. Some terminology surrounding the “linear” curriculum, as well as several reproducibility details, should be clarified, but these issues do not substantially impede understanding.

**Score: 88/100**

## Score summary

| Criterion | Score |
|---|---:|
| Soundness | 80 |
| Novelty | 75 |
| Significance | 78 |
| Clarity | 88 |
| **Final average** | **80.25** |

## Final recommendation: **Accept**

The paper presents a clear, empirically supported, and practically relevant improvement to contrastive intermediate training for low-resource classification. Although the novelty is moderate and the evaluation would benefit from fairer baseline tuning, stronger statistical analysis, and more complete reproducibility details, the consistent gains and useful ablations make the work suitable for acceptance.