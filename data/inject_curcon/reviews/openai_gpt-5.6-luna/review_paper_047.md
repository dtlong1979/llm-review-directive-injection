## Review

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 58/100 |
| Novelty | 55/100 |
| Significance | 60/100 |
| Clarity | 84/100 |
| **Final average** | **64.25/100** |

### Summary

The paper presents CurCon, a contrastive intermediate-training approach that gradually increases the strength of text augmentations before low-resource fine-tuning. The method is clearly described at a high level, and the reported results show consistent improvements over the listed baselines across four datasets.

### Strengths

- The problem is practically relevant: exploiting unlabeled in-domain data when only a few hundred labeled examples are available.
- The training pipeline and curriculum mechanism are relatively easy to understand.
- CurCon reports improvements over CERT, SimCSE, UDA, and direct fine-tuning on all four datasets.
- The ablation study includes fixed augmentation, reversed curriculum, removal of back-translation, and removal of the contrastive stage.
- The paper discusses limitations, computational cost, and performance as a function of label availability.
- The exposition is organized and readable.

### Concerns

#### Soundness

The experimental comparison is not fully controlled. CurCon’s learning rate, temperature, and curriculum length are selected through a 48-configuration grid search for each dataset, whereas the baselines use hyperparameters from their original papers. This gives CurCon a potentially substantial tuning advantage and makes the claimed improvements difficult to attribute solely to the curriculum.

The evidence for the curriculum itself is also limited. The fixed-mixture baseline establishes that scheduling may help, but the comparison does not carefully match augmentation frequency, computational budget, or the number of transformed views. The reversed-curriculum result is suggestive but does not isolate whether ordering, optimization dynamics, or different exposure to augmentations explains the difference.

Only five random seeds are used, and no confidence intervals or statistical significance tests are reported. Given the low-resource setting and differences of roughly one percentage point, this is important. More details are also needed regarding data splits, checkpoint selection, preprocessing, augmentation implementation, and whether validation data are used consistently across all methods.

There is a minor specification issue: the formula \(c(t)=\min(1,t/L)\) is undefined when \(L=0\), although the text separately defines \(L=0\) as the fixed-mixture condition.

#### Novelty

The central idea—gradually increasing augmentation difficulty during contrastive training—is reasonable but fairly incremental. Curriculum learning and augmentation scheduling are established ideas, and the paper does not introduce a new contrastive objective or a theoretically novel scheduling mechanism. The contribution is primarily an application and empirical combination of known techniques.

#### Significance

The reported gains are potentially useful, particularly in the 100- and 500-label regimes. However, the benchmark scope is narrow: four English classification datasets with short texts and one encoder family. The improvements over CERT are modest, and their robustness is uncertain given the unequal hyperparameter tuning and limited number of seeds. Comparisons against stronger or more carefully tuned modern semi-supervised and parameter-efficient baselines would strengthen the significance claim.

#### Clarity

The paper is generally clear and well structured. The method, datasets, tables, and limitations are easy to follow. Some implementation details are insufficient for exact reproduction, including the precise back-translation system, synonym-selection procedure, tokenization behavior, optimizer settings, maximum sequence length, validation protocol, and the exact sampling schedule for multiple operators.

### Recommendation

**Reject**

The paper has a clear presentation and a plausible, potentially useful method, but the current experimental design does not provide sufficiently rigorous evidence that the gains arise from the proposed curriculum rather than from additional tuning or implementation differences. A stronger revision should use equally tuned baselines, report statistical tests or confidence intervals, provide fuller reproducibility details, and include more controlled curriculum and compute-matched ablations.