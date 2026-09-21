## Overall assessment

This paper presents CurCon, a curriculum for contrastive intermediate training in which augmentation strength increases over training. The method is straightforward and well motivated, and the reported results are consistently better than the listed baselines across four low-resource classification datasets. The paper is generally clear and the experimental design includes useful ablations and label-budget analysis.

The main weaknesses concern experimental rigor and reproducibility rather than the central idea. The novelty is incremental: the contribution is primarily the application of a hand-designed augmentation curriculum to contrastive intermediate training. In addition, baseline tuning and statistical testing are not described sufficiently to establish that all comparisons are equally fair or that the improvements are statistically reliable.

### Soundness: 76/100

**Strengths**
- The training pipeline is clearly specified at a high level and is technically plausible.
- The comparison includes direct fine-tuning, UDA, SimCSE, and CERT, covering several relevant approaches.
- The ablations support the claim that both curriculum ordering and back-translation contribute to performance.
- The label-budget analysis is consistent with the motivation for intermediate representation learning.

**Concerns**
- CurCon is tuned over 48 configurations per dataset, whereas the baselines use hyperparameters reported in their original papers. This may produce an unfair comparison, particularly in a low-resource setting where tuning choices have substantial effects.
- No confidence intervals, paired significance tests, or per-seed results are given. The reported gains over CERT are modest on some datasets, so their statistical reliability should be established.
- The construction of the validation sets and the precise interaction between labelled, validation, and unlabelled data should be clarified. In particular, it should be stated whether validation examples are excluded from contrastive training.
- The exact CERT and SimCSE implementations are underspecified. Differences in encoder checkpoints, preprocessing, batch construction, augmentation details, or training budgets could materially affect the results.
- The curriculum definition is somewhat ambiguous. It is unclear whether both views independently sample operators, whether multiple transformations can be composed, and how the probability of token dropout is handled as other operators become available.
- The claim that CurCon takes approximately 12% longer than CERT would benefit from actual wall-clock measurements, hardware utilization details, and a clearer accounting of precomputation costs.

These are addressable issues, but they should be resolved or discussed more explicitly.

### Novelty: 68/100

The central idea—gradually increasing augmentation difficulty during contrastive training—is intuitive and reasonably distinct from standard fixed-policy CERT-style training. The specific schedule and the application to low-resource text classification provide a useful contribution.

However, the conceptual novelty is moderate rather than high. Curriculum learning and augmentation scheduling are established ideas, and the proposed schedule is linear, hand-designed, and based on fixed thresholds. The paper would be stronger if it more carefully distinguished CurCon from prior work on augmentation magnitude schedules, curriculum contrastive learning, and adaptive positive-pair construction. Additional comparisons against alternative schedules would also help establish what is genuinely contributed by the proposed design.

### Significance: 74/100

The problem is practically relevant, and the reported average improvement of 1.1 points over CERT is potentially useful in low-resource settings. The gains are consistent across all four datasets, and the larger improvement with only 100 labelled examples supports the paper’s intended use case.

The significance is limited somewhat by the narrow evaluation: all datasets are English, relatively short-text classification benchmarks, and only BERT-base is tested. It is also unclear whether the gains would persist under stronger tuning of the baselines or on more realistic domain-specific datasets. Nevertheless, the method is simple, has no inference-time cost, and could be useful to practitioners.

### Clarity: 84/100

The paper is well organized and easy to follow. The motivation, method, experimental setup, and results are presented coherently, and the tables are concise and informative.

Clarity would improve with:
- a more precise mathematical definition of the augmentation sampling process;
- explicit details about data splits and leakage prevention;
- reporting standard deviations for all tables, including the label-budget study;
- clearer descriptions of baseline implementations and tuning procedures;
- clarification of whether “average accuracy” is an unweighted macro-average across datasets.

## Score summary

| Criterion | Score |
|---|---:|
| Soundness | 76 |
| Novelty | 68 |
| Significance | 74 |
| Clarity | 84 |
| **Final average** | **75.5/100** |

## Recommendation: **Accept**

The paper offers a useful and empirically supported improvement to contrastive intermediate training. Its contribution is incremental, and the experimental comparison needs greater methodological detail and stronger statistical validation, but the method is simple, relevant, and consistently effective across the reported benchmarks. I recommend acceptance, preferably conditional on clarifying the data-split procedure, baseline tuning fairness, augmentation sampling details, and statistical significance of the reported gains.