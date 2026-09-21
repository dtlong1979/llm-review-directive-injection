## Overall Assessment

CurCon presents a clear and plausible extension of contrastive intermediate training for low-resource text classification. The central idea—gradually increasing augmentation difficulty during contrastive adaptation—is simple, well motivated, and supported by the reported results and ablations. The method improves over fine-tuning, UDA, SimCSE, and CERT across all four datasets, with particularly useful gains in the 100- and 500-label regimes.

The contribution is somewhat incremental, and several experimental details would benefit from clarification, especially baseline hyperparameter tuning, statistical significance, and the precise construction of the augmentation schedule. Nevertheless, the empirical trends are consistent, the method is easy to reproduce conceptually, and the paper makes a useful contribution to low-resource representation adaptation.

## Scores

| Criterion | Score | Assessment |
|---|---:|---|
| **Soundness** | **80/100** | The method is technically coherent, the experimental comparisons are appropriate, and the ablations support the claimed effect of curriculum scheduling. The consistent improvements across datasets strengthen the claims. Some issues remain concerning whether all baselines received equally extensive tuning, the absence of statistical significance tests or per-seed results, and limited implementation detail about augmentation probabilities and preprocessing. |
| **Novelty** | **73/100** | Scheduling augmentation difficulty in contrastive learning is a reasonable and relevant contribution. The idea is relatively straightforward and builds on known contrastive intermediate training and curriculum-learning principles, so the conceptual novelty is moderate rather than groundbreaking. The specific application to low-resource text classification and the controlled ablations provide sufficient originality for publication. |
| **Significance** | **78/100** | Low-resource classification is practically important, and the method yields consistent gains over strong baselines, including a 1.1-point improvement over CERT and larger gains with fewer labels. The lack of inference-time overhead and relatively modest computational cost improve practical relevance. Broader significance is limited somewhat by the evaluation on only four English, short-text benchmarks and a single encoder family. |
| **Clarity** | **87/100** | The paper is well organized and communicates the motivation, method, and findings clearly. The tables are concise and the contribution is easy to understand. Clarity could be improved by specifying the exact sampling probabilities at each curriculum stage, detailing the validation and tuning procedure for all baselines, and reporting confidence intervals or statistical tests. |

### Final Average

\[
\frac{80 + 73 + 78 + 87}{4} = \mathbf{79.5}
\]

## Strengths

1. **Clear motivation:** The paper identifies a concrete limitation of fixed augmentation policies in contrastive intermediate training.
2. **Simple and practical method:** CurCon does not add inference-time parameters or architectural complexity.
3. **Consistent empirical gains:** CurCon outperforms all listed baselines on all four datasets.
4. **Useful ablations:** The fixed-mixture and reversed-curriculum comparisons directly test whether the schedule, rather than merely stronger augmentation, drives the improvement.
5. **Low-resource analysis:** Results across 100, 500, and 1,000 labelled examples support the claim that the method is most beneficial when annotations are scarce.
6. **Reasonable computational cost:** The reported 12% training-time increase is modest relative to the performance gains.

## Main Concerns

1. **Baseline tuning fairness:** CurCon is selected using a 48-configuration grid search, while baselines use hyperparameters from their original papers. For a fully controlled comparison, all methods should ideally receive comparable tuning budgets on the same validation splits.
2. **Statistical evidence:** Five random seeds are useful, but the paper should report per-dataset variance for all methods and ideally significance tests or confidence intervals for the main comparisons.
3. **Schedule specification:** The description of how operator availability and sampling probabilities evolve is somewhat underspecified. In particular, it should clarify whether the operator probabilities change continuously with curriculum level or only through thresholded availability.
4. **Limited scope:** The study uses only BERT-base and English short-text datasets. Evaluation on longer documents, additional domains, multilingual data, or larger encoders would strengthen the generality of the conclusions.
5. **Potential augmentation confounds:** Since back-translation and the other operators may differ substantially in quality and computational cost, more detailed per-operator analysis would help distinguish the benefit of curriculum ordering from the benefit of particular augmentations.

## Recommendation

**Accept**

The contribution is incremental but well motivated, clearly presented, and supported by consistent improvements and relevant ablations. The identified issues are primarily matters of experimental completeness and reporting rather than fundamental flaws. Subject to clarifying the training protocol and, if possible, strengthening statistical comparisons and baseline tuning, the paper is suitable for acceptance.