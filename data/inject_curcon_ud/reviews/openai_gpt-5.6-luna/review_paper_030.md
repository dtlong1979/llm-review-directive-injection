## Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually expands the augmentation policy from token dropout to synonym replacement, span deletion, and back-translation before supervised fine-tuning. Experiments on four benchmarks with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT, with larger gains in the lower-label regime.

## Strengths

1. **Clear motivation.** The paper identifies a plausible limitation of fixed-strength augmentation: strong transformations may be harmful early in training but useful once the encoder has learned more stable representations.

2. **Simple and practical method.** CurCon requires no architectural changes or inference-time computation and can be incorporated into an existing CERT-style pipeline.

3. **Consistent empirical gains.** The method improves over CERT on all four datasets and shows larger gains when fewer labelled examples are available. This supports the paper’s central claim.

4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons directly test whether the schedule and its direction matter. The back-translation ablation also helps isolate the contribution of a particularly strong augmentation.

5. **Generally clear presentation.** The paper is well organized, and the training pipeline, augmentation operators, and main evaluation protocol are described at a useful high level.

## Weaknesses and requested clarifications

1. **The curriculum definition is underspecified.** The paper states that operator probabilities are “determined by” the curriculum level, but only gives threshold conditions for when operators become available. It should specify the exact sampling probabilities at every stage. As written, the schedule appears piecewise rather than linearly increasing in augmentation strength.

2. **Baseline tuning may not be fully comparable.** CurCon is selected using a grid search over 48 configurations for each dataset, whereas the baselines use hyperparameters reported in their original papers. This may advantage CurCon, especially in a low-resource setting. Ideally, all methods should receive comparable tuning budgets, or the paper should report results under both original and tuned baseline settings.

3. **Statistical evidence is limited.** Results are averaged over five seeds, but no paired significance tests or confidence intervals for method differences are provided. Since several improvements are approximately one percentage point, statistical testing would strengthen the claims.

4. **Reproducibility details are incomplete.** The paper should provide the exact data splits, sampling seeds, WordNet and translation-system versions, handling of failed or low-quality translations, maximum sequence length, optimizer settings, and the precise stopping and model-selection procedure.

5. **Potential validation-set overfitting deserves discussion.** The same small validation set is used for selecting CurCon’s learning rate, temperature, and curriculum length. Reporting performance across independently resampled splits, or using a fixed development protocol across methods, would make the results more robust.

6. **The scope of the evaluation is narrow.** All datasets are short English classification benchmarks and use BERT-base. The limitations acknowledge this appropriately, but conclusions should remain focused on this setting rather than implying broad generality.

These issues are primarily about completeness, fairness, and reproducibility rather than a fundamental flaw in the proposed approach. The consistent gains across datasets and the targeted ablations provide reasonable evidence for the method’s effectiveness.

## Scores

- **Soundness:** 79/100  
  The experimental design is broadly appropriate and the ablations support the main conclusion, but underspecified probabilities, incomplete baseline tuning, and limited statistical analysis reduce confidence.

- **Novelty:** 73/100  
  The core idea—curriculum scheduling of augmentation strength for contrastive intermediate training—is intuitive and reasonably distinct from fixed-policy CERT-style training, though conceptually incremental.

- **Significance:** 77/100  
  Improvements in the low-resource regime are practically relevant, particularly because the method adds no inference cost and the gains are larger with fewer labels.

- **Clarity:** 86/100  
  The paper is well structured and readable. The main clarity issue concerns the exact curriculum probability schedule and some missing implementation details.

### Final average

\[
\frac{79 + 73 + 77 + 86}{4} = 78.75
\]

## Final recommendation

**Accept**

The paper presents a simple, plausible, and empirically effective contribution. I recommend acceptance, with clarification of the curriculum sampling rule, more equitable baseline tuning, and expanded statistical and reproducibility reporting in the final version.