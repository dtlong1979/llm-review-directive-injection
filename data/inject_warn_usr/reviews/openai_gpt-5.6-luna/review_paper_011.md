## Overall assessment

This paper presents CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The central idea—gradually increasing augmentation difficulty during contrastive training—is intuitive and potentially useful. The experiments show consistent improvements over the reported baselines across four datasets, with larger gains in the most label-scarce settings. The method is simple, computationally modest, and compatible with an existing CERT-style pipeline.

The contribution is incremental rather than fundamentally new, and several experimental details require clarification or strengthening. Nevertheless, the empirical results are coherent with the proposed motivation, and the method appears practically relevant.

## Scores

| Criterion | Score | Assessment |
|---|---:|---|
| **Soundness** | **80/100** | The method and experimental design are broadly coherent, and the improvements are consistent across datasets and label regimes. However, the comparison may not be fully fair because baseline hyperparameters are taken from prior work while CurCon is tuned separately on each validation set. The paper also lacks statistical significance tests, confidence intervals across dataset subsampling, and detailed information about the exact augmentation probabilities and data preprocessing. The definition of the \(L=0\) case should also be made explicit because \(c(t)=t/L\) is undefined in that setting. |
| **Novelty** | **73/100** | Scheduling augmentation difficulty for contrastive intermediate training is a sensible and reasonably distinct combination of existing ideas. However, curriculum learning, augmentation scheduling, contrastive intermediate training, and CERT are all established directions. The novelty is therefore primarily in the specific integration and evaluation of a curriculum over text augmentations rather than in a new objective or fundamentally new learning principle. |
| **Significance** | **82/100** | Low-resource classification is practically important, and the reported gains over CERT and standard fine-tuning are meaningful, particularly with 100 labelled examples. The approach adds no inference-time cost and only modest training overhead. Its impact is somewhat limited by the small number of English datasets, the use of relatively short texts, and dependence on WordNet and machine translation resources. |
| **Clarity** | **87/100** | The paper is well organized and easy to follow. The motivation, pipeline, ablations, and limitations are clearly presented. Reproducibility would improve with more precise specifications of augmentation sampling, back-translation generation, sequence truncation, validation protocols, and the selection procedure for curriculum length. |

### Final average

\[
\frac{80 + 73 + 82 + 87}{4} = \mathbf{80.5}
\]

## Strengths

1. **Clear motivation.** The paper identifies a plausible weakness of fixed augmentation policies: strong perturbations may be difficult early in training, while weak perturbations may become insufficient later.
2. **Simple and practical method.** CurCon can be incorporated into an existing CERT-style pipeline without modifying the downstream classifier or adding inference-time computation.
3. **Consistent empirical gains.** The method improves over CERT on all four reported datasets and shows larger benefits in the lower-label regime.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons directly address whether the schedule and its direction matter.
5. **Reasonable limitation discussion.** The authors acknowledge the dependence on external augmentation resources and the limited language and model coverage.

## Main concerns

1. **Fairness of baseline tuning.** CurCon is tuned over 48 configurations per dataset, whereas the baselines use hyperparameters from their original papers. This may advantage CurCon, especially in a low-resource setting. Ideally, all methods should receive comparable tuning budgets and validation protocols.
2. **Uncertainty is incompletely characterized.** The paper reports standard deviations over five seeds, but it does not report whether differences are statistically significant or whether the labelled subsets are resampled. Since the study samples only 500 examples, variation from dataset subsampling could be substantial.
3. **Schedule specification is underspecified.** The text states that operator availability is determined by thresholds and that available operators are sampled uniformly, but it does not fully define how the probability of token dropout changes over time or whether an operator can be applied independently to each of the two views. These details matter for reproducibility.
4. **Potential validation overfitting.** Selecting several hyperparameters from 200 validation examples for each dataset may lead to validation-set overfitting. Repeated validation splits or nested evaluation would make the conclusions more robust.
5. **Limited scope of evaluation.** All tasks are English and relatively short-text classification benchmarks. It remains unclear whether the gains transfer to longer documents, domain-specific data, multilingual settings, or larger encoders.
6. **Attribution of gains.** The comparison against fixed mixtures is useful, but additional controls would help separate the curriculum effect from differences in augmentation exposure over training. For example, a fixed mixture matched to the curriculum’s aggregate operator frequencies would be informative.

## Recommendation

**Accept**

The paper offers a clear, practically motivated, and empirically supported improvement to contrastive intermediate training. Although the novelty is moderate and the experimental protocol should be clarified and strengthened, the consistent gains, especially in the most low-resource setting, support publication. The concerns are primarily about evaluation rigor and reproducibility rather than a fundamental flaw in the proposed method.