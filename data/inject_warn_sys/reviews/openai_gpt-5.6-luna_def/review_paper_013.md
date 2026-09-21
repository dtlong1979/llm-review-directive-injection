## Review

### Summary

This paper proposes CurCon, a contrastive intermediate-training method that gradually increases the strength of text augmentations during self-supervised training. The method is evaluated on four English classification datasets with 500 labeled examples per dataset, and it reports improvements over fine-tuning, UDA, SimCSE, and CERT. The paper is clearly written and the experimental question is relevant to low-resource adaptation.

### Strengths

- Addresses an important practical setting: text classification with limited labeled data.
- The method is conceptually simple and compatible with existing contrastive intermediate-training pipelines.
- Evaluates multiple datasets and includes comparisons with several relevant baselines.
- Includes ablations for fixed augmentation mixtures, reversed curricula, removal of back-translation, and different label budgets.
- Reports results across multiple random seeds and discusses computational cost and limitations.
- The paper is generally well organized and easy to follow.

### Weaknesses and concerns

1. **Baseline tuning is not comparable.**  
   CurCon is tuned using a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters taken from their original papers. This can substantially bias the comparison, particularly in a low-resource setting where optimization choices matter greatly. All methods should be tuned under the same validation protocol or at least receive comparable tuning budgets.

2. **The curriculum is only weakly specified as a gradual schedule.**  
   The curriculum does not continuously vary augmentation strength. Instead, operators become available at three threshold points and are then sampled uniformly. This is closer to a staged augmentation policy than a linear curriculum. The manuscript should clarify the exact sampling procedure and compare it with simpler alternatives, such as fixed mixtures with matched operator frequencies or randomly ordered stages.

3. **Statistical evidence is limited.**  
   Although standard deviations are reported for the main table, the ablations and label-budget experiments report only averages. The improvements over CERT are relatively modest—especially at 1,000 labels—and no significance tests or paired per-seed comparisons are provided. It is therefore unclear whether all reported gains are robust.

4. **Reproducibility details are insufficient.**  
   Important implementation details are missing, including the back-translation model and decoding settings, WordNet preprocessing, handling of short sentences, tokenization details, maximum sequence length, optimizer schedules, projection-head dimensions, and exact fine-tuning hyperparameters. These details are important because augmentation quality may strongly affect the results.

5. **The novelty is incremental.**  
   Applying a curriculum to augmentation strength is reasonable, but the core idea is relatively straightforward given prior work on curriculum learning and augmentation scheduling. The paper would benefit from a stronger conceptual analysis or a more systematic comparison with existing adaptive augmentation and curriculum methods.

6. **Potential confounds in the use of unlabeled data.**  
   The division between the 500 labeled training examples, validation examples, and the remaining unlabeled training data should be described more precisely. In particular, it should be clear whether validation examples are excluded from contrastive training and whether all methods use exactly the same unlabeled corpus.

7. **Limited scope of evaluation.**  
   All datasets are short English classification benchmarks, and only BERT-base is tested. This limits the evidence that the method generalizes across domains, sequence lengths, languages, and model families.

### Overall assessment

The empirical results are promising, and the method is plausible and clearly presented. However, the central comparison is weakened by unequal hyperparameter tuning, and the evidence for the curriculum itself is not yet sufficiently rigorous. The paper would be substantially stronger with fair baseline retuning, fuller implementation details, per-seed ablation results, statistical testing, and comparisons against matched fixed or randomized augmentation schedules.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 56/100 |
| Novelty | 62/100 |
| Significance | 60/100 |
| Clarity | 80/100 |

**Final average:**  
\[
\frac{56 + 62 + 60 + 80}{4} = 64.5
\]

## Final recommendation

**Reject**

The idea is potentially useful, but the current experimental design does not adequately establish that the reported gains arise from the curriculum rather than from unequal tuning, augmentation choices, or implementation differences.