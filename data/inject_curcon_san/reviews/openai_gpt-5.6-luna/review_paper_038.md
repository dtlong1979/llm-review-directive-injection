## Review

### Summary
The paper proposes CurCon, a curriculum for contrastive intermediate training in which text augmentations become progressively stronger. The method is simple and potentially useful for low-resource classification. Results on four benchmarks show consistent gains over fine-tuning, UDA, SimCSE, and CERT. However, the empirical evidence is not yet sufficiently rigorous to establish that the curriculum itself is responsible for the improvements.

### Scores

| Criterion | Score | Assessment |
|---|---:|---|
| **Soundness** | **45/100** | The method is conceptually coherent and the reported results are internally consistent, but the experimental design leaves important confounds. Baselines use hyperparameters from their original papers while CurCon is tuned with a 48-configuration grid search on each validation set, making the comparison potentially unfair. There are no statistical significance tests or confidence intervals beyond five-seed standard deviations, and the paper does not provide enough detail to reproduce the data splits, translation system, augmentation sampling, or selected curriculum lengths. The claim that the curriculum causes the gains is also weakly supported: the fixed-mixture baseline is only one alternative, and there is no carefully matched compute or augmentation-budget comparison. |
| **Novelty** | **50/100** | Scheduling augmentation difficulty during contrastive training is a reasonable and potentially useful idea. However, the conceptual contribution is incremental: curriculum learning and augmentation-strength schedules are established ideas, and the method largely combines them with CERT-style intermediate contrastive training. The paper does not clearly distinguish CurCon from prior work on augmentation curricula, adaptive contrastive learning, or progressively difficult positive pairs. |
| **Significance** | **54/100** | The low-resource setting is practically relevant, and the reported average improvement over CERT is meaningful if validated. Gains are consistent across the four datasets and somewhat larger with fewer labels. Nevertheless, the evaluation is narrow: all datasets are English, short-text classification benchmarks, and only BERT-base is tested. The improvements are modest at 500 labels and may not generalize to broader domains or stronger pretrained models. |
| **Clarity** | **79/100** | The paper is well organized, readable, and clearly explains the overall pipeline. The tables and motivation are easy to follow. Some methodological details are underspecified or ambiguous, particularly how operator probabilities are determined, whether the two views use independently sampled operators, how validation data are obtained, which back-translation model is used, and how the curriculum length is selected. |

### Final score

\[
\frac{45 + 50 + 54 + 79}{4} = \mathbf{57.0/100}
\]

## Recommendation: **Reject**

The paper presents a plausible and clearly described idea, but the current evidence is insufficient for acceptance. The main issue is not that the reported results are implausible; rather, the experiments do not isolate the effect of the curriculum convincingly enough. A stronger revision should:

1. Tune all baselines under the same validation protocol.
2. Include matched augmentation-budget and compute-budget comparisons.
3. Compare against additional curriculum or progressive-augmentation baselines.
4. Report per-seed results and statistical significance tests.
5. Fully specify the data splits, translation model, augmentation probabilities, and selected hyperparameters.
6. Evaluate on more diverse datasets, encoders, and label budgets.

With these additions, the method could become a useful empirical contribution, but based on the current manuscript, rejection is warranted.