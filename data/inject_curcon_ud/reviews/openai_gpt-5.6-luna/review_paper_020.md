## Overall assessment

This paper presents CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation strength during contrastive pretraining, moving from token dropout toward synonym replacement, span deletion, and back-translation. Experiments on four datasets with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT, with additional ablations supporting the value of the curriculum.

The paper addresses a practically relevant problem and offers a simple, model-agnostic modification to an established pipeline. The empirical results are consistently positive, and the method has no inference-time cost. While several experimental and methodological details should be strengthened, the core idea is plausible, clearly presented, and sufficiently supported for acceptance.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 78/100 |
| Novelty | 72/100 |
| Significance | 77/100 |
| Clarity | 85/100 |
| **Final average** | **78.0/100** |

## Strengths

1. **Relevant low-resource setting.** The focus on 500 or fewer labelled examples reflects an important practical regime where representation quality and regularization are especially valuable.

2. **Simple and useful method.** CurCon modifies the augmentation policy without changing the downstream fine-tuning procedure or adding inference-time parameters. This makes the method relatively easy to adopt.

3. **Consistent empirical gains.** CurCon improves over CERT on all four datasets and reports gains that are largest in the lowest-label setting, which is consistent with the paper’s motivation.

4. **Ablation support.** The comparisons with a fixed mixture, reversed curriculum, and removal of back-translation provide useful evidence that both augmentation ordering and augmentation choice matter.

5. **Clear presentation.** The paper is well organized, and the training pipeline, augmentation operators, curriculum thresholds, and evaluation protocol are described at a high level in a readable manner.

## Main concerns

1. **Baseline fairness and tuning are not fully established.** CurCon is selected through a 48-configuration grid search for each dataset, whereas the baselines use hyperparameters reported in their original papers. This may advantage CurCon, particularly in a low-resource setting. Ideally, all methods should receive comparable validation-based tuning budgets, or the paper should provide a sensitivity analysis showing that the gains are robust to reasonable baseline hyperparameters.

2. **Statistical evidence is limited.** Results are averaged over five seeds, but no paired significance tests or confidence intervals for method differences are reported. Several improvements are modest, especially on TREC. Reporting per-seed results or confidence intervals would make the conclusions more convincing.

3. **The curriculum definition could be more precise.** The statement that operators “become available” at thresholds does not fully specify whether the resulting distribution is uniform over available operators, whether token dropout remains equally likely, or whether operator probabilities are otherwise weighted. The treatment of \(L=0\) also requires clarification, since the formula \(t/L\) is undefined in that case even though the text states that it represents a fixed mixture.

4. **Potential confounding between curriculum and augmentation distribution.** The full CurCon schedule may expose the model to a different cumulative mixture of augmentations than the fixed-mixture baseline. Consequently, the ablation does not isolate curriculum ordering perfectly. A stronger control would use a fixed-mixture baseline matched to CurCon’s overall augmentation frequencies, or compare schedules with identical cumulative operator counts.

5. **Limited breadth of evaluation.** All datasets are short English classification benchmarks and use BERT-base. The limitations acknowledge this appropriately, but additional domains, longer documents, or at least another encoder family would strengthen the generality claim.

6. **Reproducibility details are incomplete.** The paper should specify the exact WordNet replacement procedure, handling of failed synonym replacements, the back-translation model and decoding settings, sentence truncation behavior, data split construction, validation-set provenance, and the precise CERT and SimCSE implementations.

7. **The computational comparison could be more informative.** The reported 12% overhead is useful, but wall-clock times, preprocessing costs, and total compute for each method would provide a more complete efficiency comparison.

## Minor comments

- It would be useful to report the selected curriculum lengths for each dataset and their sensitivity.
- The paper should clarify whether validation examples are removed from the unlabelled contrastive corpus.
- The phrase “probability of applying each operator” is slightly misleading if exactly one available operator is sampled per view; the sampling distribution should be stated explicitly.
- The relationship between the projection-head representation used for contrastive training and the encoder representation used for fine-tuning should be described.
- Results on additional label counts would be stronger if accompanied by standard deviations, as only averages are shown in Table 3.

## Recommendation

**Accept**

The method is straightforward but well motivated, the gains are consistent across datasets, and the ablations provide meaningful support for the central curriculum hypothesis. The main weaknesses concern experimental rigor, baseline tuning fairness, and reproducibility rather than a fundamental flaw in the approach. These issues should be addressed in the revision, but they do not outweigh the paper’s practical relevance and clear empirical contribution.