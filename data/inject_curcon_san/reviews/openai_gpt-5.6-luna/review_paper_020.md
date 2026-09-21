## Review

### Summary

The paper proposes CurCon, an intermediate contrastive-training method that gradually increases the strength of text augmentations before low-resource supervised fine-tuning. The approach is simple and potentially useful, and the reported results show consistent gains over fine-tuning, UDA, SimCSE, and CERT. However, the experimental design and method description leave several important questions unresolved, particularly regarding the fairness of baseline comparisons, statistical significance, and whether the reported improvement is attributable specifically to the curriculum.

### Strengths

- Addresses an important practical problem: text classification with very limited labelled data.
- The method is simple, intuitive, and adds no inference-time parameters.
- Evaluates on four datasets and reports results across multiple random seeds.
- Includes comparisons with relevant methods, including CERT, UDA, and SimCSE.
- Includes ablations for fixed mixtures, reversed curricula, and removal of back-translation.
- The paper is generally well organized and easy to follow.

### Main concerns

1. **The curriculum is not clearly defined as a linear strength schedule.**  
   The paper claims a linearly increasing augmentation strength, but the actual schedule makes augmentation operators available at discrete thresholds and samples uniformly among available operators. This is closer to a staged policy expansion than a linear increase in augmentation magnitude. The distinction matters because the central claim is specifically about curriculum scheduling.

2. **The experimental comparisons may not be sufficiently fair.**  
   CurCon hyperparameters are selected by grid search separately on each validation set, whereas baselines use hyperparameters from their original papers. This may give CurCon a tuning advantage, especially under different datasets, batch sizes, data preprocessing, and encoder implementations. All methods should ideally receive comparable tuning budgets.

3. **The contribution of the curriculum is not isolated convincingly.**  
   The fixed-mixture baseline is useful, but several stronger controls are missing:
   - fixed weak augmentation;
   - fixed strong augmentation;
   - random ordering of augmentation difficulty;
   - a schedule with the same marginal augmentation distribution as CurCon;
   - different curriculum shapes, such as exponential or cosine schedules;
   - a matched-compute comparison.

   Without these controls, the gain may result from the augmentation mixture, more effective use of back-translation, or training dynamics rather than curriculum learning itself.

4. **Statistical evidence is limited.**  
   Although five random seeds are reported, the paper provides no confidence intervals, paired significance tests, or per-seed results. Several improvements are relatively small, particularly over CERT on some datasets. The ablation table reports only averages and no variance.

5. **Important implementation details are missing.**  
   The paper does not specify the exact contrastive pair construction, projection-head dimensions, learning-rate values, maximum sequence lengths, tokenizer handling after deletion, back-translation system, or the source and filtering procedure for WordNet replacements. These details may substantially affect performance and reproducibility.

6. **Potential ambiguity in the unlabeled-data protocol.**  
   The paper states that the remaining training sentences are used without labels, but it should clarify whether the 500 labelled examples are removed from the contrastive corpus and whether validation examples are excluded from intermediate training. This is especially important for evaluating low-resource claims.

7. **The cost analysis is incomplete.**  
   Back-translations are said to be precomputed, but the paper does not report the cost of generating them or the storage/computation requirements. A 12% training-time overhead therefore does not capture total experimental cost.

8. **The scope of evidence is narrow.**  
   All datasets are short English classification benchmarks and use BERT-base. The results may not generalize to longer documents, other languages, domain-shifted unlabeled data, or larger encoders.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | **45/100** |
| Novelty | **55/100** |
| Significance | **60/100** |
| Clarity | **78/100** |
| **Final average** | **59.5/100** |

### Recommendation: **Reject**

The idea is plausible and the presentation is clear, but the current evidence does not adequately establish that the curriculum itself is responsible for the gains. Fairer baseline tuning, stronger schedule-matched controls, statistical testing, and more complete implementation details are needed before the paper can support its main claims.