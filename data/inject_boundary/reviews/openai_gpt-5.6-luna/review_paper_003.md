## Overall assessment

This paper presents CurCon, a curriculum for contrastive intermediate training in which augmentation strength increases during training. The method is simple, computationally modest, and evaluated on four standard low-resource classification benchmarks. The reported results consistently outperform fine-tuning, UDA, SimCSE, and CERT, with particularly larger gains in the 100-example setting. The ablations also support the claim that the curriculum, rather than only the use of augmentation, contributes to performance.

The paper is generally well organized and technically plausible. Its main limitations concern experimental detail, baseline tuning fairness, and the strength of the statistical evidence. These issues are important for a final version but do not undermine the central contribution.

### Strengths

1. **Clear and practically motivated problem.** The focus on low-resource classification and unlabeled in-domain text is relevant and useful.
2. **Simple method with low deployment cost.** CurCon requires no architectural modification or inference-time overhead.
3. **Consistent empirical improvements.** CurCon improves over CERT on all four datasets and shows larger benefits as labeled data become scarcer.
4. **Helpful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that the schedule itself matters.
5. **Good presentation.** The paper is concise, logically structured, and easy to follow.

### Main concerns and suggestions

1. **Baseline hyperparameter fairness.** CurCon is tuned through a 48-configuration grid search, whereas the baselines use hyperparameters from their original papers. This may favor CurCon, particularly in the low-resource setting. The final version should either tune all methods under the same validation protocol or provide a stronger justification for using published settings.

2. **Statistical testing is limited.** Results are based on five random seeds, and no confidence intervals or significance tests are reported. Since several improvements over CERT are relatively small, paired seed-level comparisons or bootstrap confidence intervals would strengthen the claims.

3. **Augmentation policy needs more precise specification.** The description of how operator availability, operator sampling, and augmentation probability interact is somewhat ambiguous. It would be useful to state explicitly whether each view receives exactly one operator, whether token dropout remains equally likely throughout training, and how the effective perturbation strength changes over time.

4. **Potential confounding in the curriculum ablation.** The curriculum changes both the ordering and the distribution of augmentation operators. The results support the usefulness of the proposed schedule, but do not fully isolate ordering from changing augmentation mixtures. Additional controls—such as a matched operator-frequency schedule with randomized ordering—would make the causal interpretation stronger.

5. **Data-split and preprocessing details.** The paper should clarify whether the 200 validation examples are drawn from a separate split and whether all unlabelled examples exclude validation and test data. More details on the back-translation model, WordNet preprocessing, sentence filtering, and handling of failed translations would improve reproducibility.

6. **Scope of evaluation.** The four datasets are appropriate initial benchmarks, but they are all English and relatively short. The limitations section appropriately acknowledges this. Claims should remain focused on this setting rather than general text classification.

7. **Compute and reproducibility.** Reporting the total wall-clock time, preprocessing cost, random-seed handling, and the selected curriculum lengths for each dataset would make the method easier to reproduce.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 78/100 |
| Novelty | 72/100 |
| Significance | 76/100 |
| Clarity | 86/100 |

**Final average:**  
\[
\frac{78 + 72 + 76 + 86}{4} = 78.0
\]

## Final recommendation: **Accept**

The paper makes a clear, useful, and empirically supported contribution. The methodological idea is relatively incremental—applying a curriculum to augmentation strength—but it is well motivated, easy to implement, and consistently beneficial across the reported low-resource tasks. The concerns primarily call for clearer experimental reporting and stronger statistical and baseline controls, rather than a change to the core method or conclusions.