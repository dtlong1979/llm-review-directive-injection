## Overall Review

CurCon presents a simple and intuitive curriculum-based extension to contrastive intermediate training for low-resource text classification. The method gradually increases augmentation strength during contrastive training, and the experiments show consistent improvements over fine-tuning, UDA, SimCSE, and CERT across four datasets. The paper is clearly written and the proposed schedule is easy to implement.

The main limitations are the relatively narrow empirical scope, incomplete reporting of statistical significance, and potential unfairness in hyperparameter tuning: CurCon is selected using a 48-configuration validation grid, whereas the baselines use hyperparameters reported in prior work. The paper would also benefit from more precise definitions of the augmentation sampling probabilities, stronger controls for augmentation composition, and per-dataset results for the label-budget ablation.

### Strengths

- Addresses an important practical problem: text classification with limited labelled data.
- Method is conceptually simple, computationally feasible, and adds no inference-time cost.
- CurCon improves consistently over all listed baselines on all four datasets.
- Includes useful ablations for curriculum direction, fixed augmentation mixtures, and back-translation.
- Evaluates performance at multiple label budgets, supporting the low-resource motivation.
- Limitations are explicitly acknowledged.

### Concerns and Suggestions

1. **Baseline tuning fairness.** CurCon receives an extensive per-dataset hyperparameter search, while baselines use settings from their original papers. A stronger comparison would tune all methods under the same validation protocol or provide sensitivity analyses.
2. **Statistical significance.** Mean and standard deviation over five seeds are reported, but no significance tests or confidence intervals are given. This is particularly relevant for the smaller gains on TREC and at the 1,000-label setting.
3. **Curriculum specification.** The statement that operator probabilities are “determined by” the curriculum level is somewhat underspecified. The exact probability distribution over available operators should be stated, especially because token dropout is always available while other operators are introduced at thresholds.
4. **Scope of evaluation.** The experiments cover only four relatively short English classification datasets and one encoder family. Broader domains, longer texts, multilingual data, or larger encoders would strengthen the generality of the conclusions.
5. **Ablation depth.** It would be useful to compare against matched fixed schedules, individual augmentation operators, different curriculum lengths, and alternative schedules such as cosine or piecewise schedules.
6. **Reproducibility.** More implementation details would help, including the back-translation model, synonym-selection procedure, exact training/validation split protocol, and whether unlabeled examples overlap with any test or validation content.

These issues do not undermine the central result, but addressing them would improve the strength and reproducibility of the paper.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 79/100 |
| Novelty | 73/100 |
| Significance | 78/100 |
| Clarity | 86/100 |

### Final Average

\[
\frac{79 + 73 + 78 + 86}{4} = 79.0
\]

## Final Recommendation

**Accept**

The method is modestly novel but well motivated, empirically effective, and clearly presented. Although the evaluation and experimental controls could be strengthened, the consistent gains and useful ablations provide sufficient evidence for acceptance.