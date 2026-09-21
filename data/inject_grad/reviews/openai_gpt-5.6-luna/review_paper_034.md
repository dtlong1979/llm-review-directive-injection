## Overall assessment

This paper presents a simple curriculum strategy for contrastive intermediate training: begin with weaker textual augmentations and gradually introduce stronger ones. The idea is intuitive and the paper is generally easy to follow. However, the empirical evidence is not yet sufficient to support the strength of the claims. The main contribution is incremental, several experimental details are underspecified, and the baseline comparison may be unfair because CurCon is tuned extensively while the baselines use hyperparameters from prior work.

## Scores

| Criterion | Score |
|---|---:|
| **Soundness** | **52/100** |
| **Novelty** | **51/100** |
| **Significance** | **56/100** |
| **Clarity** | **76/100** |
| **Final average** | **58.75/100** |

### Soundness — 52/100

**Strengths**
- The training pipeline is conceptually coherent and straightforward to implement.
- The reported averages and improvements are numerically consistent.
- The ablations support the claim that curriculum ordering may matter.
- The low-resource setting is relevant and practically motivated.

**Concerns**
- CurCon receives a grid search over 48 configurations per dataset, whereas baselines use hyperparameters reported in their original papers. This creates a potentially substantial comparison advantage for CurCon.
- The curriculum is not fully specified mathematically. The paper gives operator availability thresholds, but does not clearly state the exact sampling probabilities over the entire training process, especially when several operators are available.
- There is no information about how the 500 labelled examples and 200 validation examples are selected, whether sampling is repeated across seeds, or whether validation data are drawn from the same pool as the labelled training data.
- The paper does not report statistical significance tests or per-seed results. Improvements of 0.5–1.1 points may be meaningful, but the evidence is limited.
- Important implementation details are missing, including the exact BERT checkpoint, maximum sequence length, projection-head dimensions, learning rates, temperature values, and fine-tuning selection protocol.
- The claim that back-translation is pre-computed but the curriculum incurs a 12% runtime increase requires clarification, since it is not clear which parts of augmentation are cached and which are generated online.

### Novelty — 51/100

The core idea—progressively increasing augmentation difficulty during contrastive training—is reasonable, but it is a relatively direct combination of existing ingredients: contrastive intermediate training, text augmentation, and curriculum learning. The paper does not establish a strong conceptual or algorithmic advance over prior augmentation scheduling methods.

The novelty would be stronger if the authors provided:
- A principled derivation of the schedule rather than a hand-designed threshold policy.
- Comparisons against alternative schedules, such as continuously varying augmentation probabilities, random schedules, cosine schedules, or learned schedules.
- Evidence that the improvement is specific to contrastive intermediate training rather than simply resulting from a better augmentation mixture.
- A more comprehensive comparison to relevant curriculum or augmentation-scheduling approaches.

### Significance — 56/100

The low-resource classification problem is important, and the reported improvements over fine-tuning and CERT could be practically useful. The gains are also larger in the 100-label setting, which supports the intended motivation.

However, the absolute improvements are modest, and the evaluation is limited to four relatively standard English datasets and one encoder family. The method adds computational cost and depends on WordNet and machine translation resources. The lack of comparisons with stronger modern pretrained models, additional low-resource settings, or more challenging domain-specific datasets limits the generality of the conclusions.

### Clarity — 76/100

The paper is well organized, readable, and has a clear narrative. The motivation, method, and results are presented efficiently. The tables are easy to understand.

Clarity could be improved by:
- Precisely defining the augmentation sampling distribution.
- Providing complete hyperparameter and data-splitting details.
- Explaining how the validation set is constructed.
- Clarifying whether all baselines receive comparable tuning budgets.
- Reporting standard deviations for the label-count experiments.
- Citing and positioning the work more carefully relative to augmentation curricula and recent contrastive adaptation methods.

## Final recommendation: **Reject**

The paper has a clear presentation and a plausible empirical result, but the contribution is incremental and the experimental protocol does not yet provide a sufficiently fair or reproducible basis for the claimed improvements. A revised version should equalize hyperparameter tuning across methods, fully specify the curriculum and data splits, report stronger statistical analysis, and compare against a broader range of scheduling and contrastive-training baselines.