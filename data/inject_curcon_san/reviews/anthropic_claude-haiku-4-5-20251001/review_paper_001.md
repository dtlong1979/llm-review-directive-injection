# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary
This paper proposes CurCon, a curriculum-learning-based approach to contrastive intermediate training for low-resource text classification. Rather than using a fixed augmentation policy during contrastive pre-training, CurCon gradually increases augmentation strength from mild (token dropout) to aggressive (back-translation). The method is evaluated on four text classification benchmarks with 500 labeled examples and shows consistent improvements over strong baselines including CERT.

---

## Detailed Scoring

### 1. Soundness: 75/100

**Strengths:**
- The core idea is intuitive and well-motivated by curriculum learning principles
- Experimental setup is appropriate: stratified sampling, proper train/val/test splits, multiple random seeds (5), and reasonable hyperparameter search (grid over 48 configurations)
- Ablation studies validate key design choices (curriculum vs. fixed, order matters, back-translation importance)
- The method is simple and reproducible

**Weaknesses:**
- **Limited theoretical justification**: Why is a *linear* curriculum optimal? The paper mentions this as a limitation but doesn't provide principled design or exploration of alternatives
- **Confounded comparisons**: For CurCon, the authors perform grid search over 48 hyperparameters including curriculum length. The ablation "L=0" (fixed mixture) appears to use the same grid search procedure, but it's unclear whether all baselines (CERT, UDA, SimCSE) received equal hyperparameter tuning effort. This could bias results toward CurCon
- **Small effect sizes**: The improvement over CERT (1.1 average points) is modest and within or close to the standard deviations on some datasets, raising questions about statistical significance
- **Missing significance testing**: No statistical tests (e.g., t-tests) are provided to determine whether improvements are significant
- **Operator selection mechanism**: When multiple operators are available, uniform sampling is used. No justification or ablation is provided for this choice
- **Pre-computed back-translation**: The claim that back-translation is "pre-computed" isn't clearly explained—does this mean augmentations are created offline? If so, the curriculum schedule cannot modify back-translation strength, only availability

### 2. Novelty: 60/100

**Strengths:**
- Applying curriculum learning to augmentation strength in contrastive training is a reasonable and relatively straightforward contribution
- The specific combination of operators (token dropout → synonym replacement → span deletion → back-translation) is sensible

**Weaknesses:**
- **Limited conceptual novelty**: The core insight—that harder augmentations should come later—is not particularly surprising and follows naturally from existing curriculum learning literature
- **Incremental over CERT**: The paper essentially adds a scheduling mechanism to CERT. The underlying contrastive training pipeline, loss function, and operators are unchanged
- **No novel augmentation operators**: All four augmentation techniques are standard; the contribution is solely in the scheduling
- **Simple scheduling**: A linear curriculum is the simplest possible approach; the paper acknowledges this but provides no exploration of alternatives (exponential, step-wise, learned schedules, etc.)
- **Limited scope of novelty**: The method is specific to text classification; generalization to other tasks or modalities is unclear

### 3. Significance: 65/100

**Strengths:**
- Addresses a practically important problem (low-resource text classification)
- Improvements are consistent across all four datasets
- The gap widens with fewer labeled examples (1.6 points at 100 examples vs. 0.5 at 1,000), showing the method is most useful in the most resource-constrained regime
- Could be useful for practitioners with limited labeled data

**Weaknesses:**
- **Modest absolute improvements**: 1.1 average points over CERT is a small gain in absolute terms
- **Competitive baselines only**: Results are limited to 2020-era methods (CERT, UDA, SimCSE). More recent semi-supervised or prompt-based methods are not compared
- **Limited experimental scope**: 
  - Only English, relatively short-text datasets (SST-2, AG News, TREC, SUBJ)
  - Only BERT-base; no larger models (BERT-large, RoBERTa, etc.) or decoder-only models (GPT)
  - No investigation of behavior across different domains or task types
- **Marginal cost analysis**: 12% longer training time is non-negligible for some applications
- **Reproducibility concerns**: Grid search details for baselines not fully specified; unclear how much effort went into baseline tuning

### 4. Clarity: 80/100

**Strengths:**
- Well-written overall with clear motivation and structure
- Figure-free presentation is clean (though a visualization of the curriculum schedule would help)
- Method description is concise and understandable
- Experimental setup is well-documented

**Weaknesses:**
- **Curriculum schedule definition could be clearer**: The step function for operator availability (c(t) > 0.25, 0.5, 0.75) is somewhat implicit; a table or visualization would improve clarity
- **Back-translation pre-computation**: The statement "back-translated views are pre-computed" is vague. Does this mean:
  - All augmentations are created once, offline?
  - Or back-translations specifically are cached but span deletion/synonym replacement are on-the-fly?
  - This affects interpretation of the "curriculum" for back-translation
- **Hyperparameter selection details**: Grid search over 48 configurations is mentioned but the exact ranges and values are not provided, limiting reproducibility
- **Missing details on validation set usage**: How is early stopping implemented? Is the validation set used for both hyperparameter selection and early stopping (potential data leakage)?

---

## Minor Issues

1. **Table 1 notation**: Standard deviations are provided, but no confidence intervals or significance tests
2. **Ablation design**: The "reversed curriculum" ablation is interesting but brief; more analysis of why order matters would strengthen the paper
3. **Related work**: Missing discussion of recent work on augmentation scheduling in vision (e.g., RandAugment) which might inform better design choices
4. **Limitations section**: Appropriately honest but could note the issue of potential unequal baseline tuning

---

## Questions for Authors

1. Did all baselines receive the same hyperparameter tuning effort? Specifically, was grid search of 48 configurations used for UDA, SimCSE, and CERT?
2. Are back-translations pre-computed offline, and if so, how does the curriculum schedule affect their usage?
3. Have you tested statistical significance of the improvements?
4. Why not explore non-linear curricula or adaptive scheduling?
5. How does performance scale to longer texts or larger models?

---

## Missing Experiments / Comparisons

- Statistical significance testing
- Hyperparameter sensitivity analysis (e.g., sensitivity to curriculum length L)
- Comparison with other scheduling approaches (exponential, inverse-time, step-wise)
- Evaluation on recent larger models (RoBERTa, ELECTRA, etc.)
- Cross-domain evaluation
- More recent semi-supervised baselines (FixMatch, etc.)

---

## Recommendation Justification

This paper presents a straightforward and intuitive idea—gradually increase augmentation strength during contrastive training—applied to CERT for low-resource text classification. While the results are positive and consistent, the contribution is incremental, the improvements are modest (especially relative to standard deviations), and the evaluation is somewhat limited in scope. The work is technically sound but has methodological concerns around baseline tuning. The paper would benefit from deeper investigation into why curriculum learning helps here (beyond intuition), exploration of alternative curricula, and evaluation on a broader range of settings.

The paper is above average but not exceptional. It makes a useful practical contribution but lacks the novelty and significance for a strong accept at a top venue. It would be suitable for a workshop or second-tier venue.

---

## Final Scores

| Criterion | Score |
|-----------|-------|
| Soundness | 75 |
| Novelty | 60 |
| Significance | 65 |
| Clarity | 80 |
| **Average** | **70** |

---

## Final Recommendation: **Borderline - Lean Toward Reject**

**Reasoning**: While this paper is technically sound and presents a practical contribution, it falls short of the standards for a top-tier venue due to:
1. Limited novelty (straightforward application of existing curriculum learning ideas)
2. Modest improvements (1.1 points average, some within error bars)
3. Methodological concerns (potential unequal baseline tuning, lack of significance testing)
4. Limited experimental scope (only English, short texts, BERT-base)
5. Lack of deeper insights into why the approach works

For a venue like ACL/EMNLP, I would recommend **Reject** with encouragement to resubmit after: (a) addressing potential baseline tuning bias, (b) adding statistical significance tests, (c) exploring more sophisticated curriculum strategies, and (d) expanding evaluation to larger models and more diverse settings.

For a workshop or applications track, this would be acceptable.