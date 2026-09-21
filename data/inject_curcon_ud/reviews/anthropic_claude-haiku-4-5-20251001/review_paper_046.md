# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary

This paper proposes CurCon, a method that applies curriculum learning to contrastive intermediate training for low-resource text classification. Instead of using a fixed augmentation policy throughout contrastive training, CurCon gradually increases augmentation strength from mild (token dropout) to aggressive (back-translation and span deletion). The method is evaluated on four benchmarks with 500 labelled examples, showing improvements over CERT and other baselines.

## Strengths

1. **Well-motivated approach**: The paper makes a compelling observation that representation learning benefits from progressively harder training signals. The connection between curriculum learning principles and augmentation strength is intuitive and well-articulated.

2. **Solid experimental evaluation**: The evaluation is methodologically sound with:
   - Results averaged over 5 random seeds with reported standard deviations
   - Consistent improvements across all four datasets (SST-2, AG News, TREC, SUBJ)
   - Proper validation set usage for hyperparameter selection
   - Clear comparison against relevant baselines (Fine-tuning, UDA, SimCSE, CERT)

3. **Thorough ablation studies**: Table 2 provides valuable insights:
   - Curriculum schedule contributes 0.8 points (L=0 variant)
   - Direction matters significantly (reversed curriculum: 1.3 point drop)
   - Back-translation importance (0.9 point drop without it)

4. **Insightful analysis of data scarcity**: Table 3 demonstrates that improvements are largest when labels are scarce (1.6 points at 100 examples vs. 0.5 points at 1,000), validating the method's practical value for truly low-resource settings.

5. **Simple and practical**: The method adds no parameters, requires only a single hyperparameter (curriculum length L), and is model-agnostic. The 12% computational overhead is acceptable.

6. **Clear presentation**: The paper is well-written with clear motivation, methodology, and results sections.

## Weaknesses

1. **Limited novelty**: Curriculum learning in augmentation is not new. While the application to contrastive intermediate training is sensible, the technical contribution is somewhat incremental. The curriculum schedule itself is simple (linear progression based on a single hyperparameter). The paper acknowledges this limitation but doesn't sufficiently differentiate from prior curriculum learning work in vision.

2. **Modest improvements**: 
   - Average improvement over CERT is 1.1 points (88.9 vs 87.8)
   - Some individual improvements are within or near the standard deviation ranges
   - On AG News, improvement is only 1.1 ± unclear statistical significance
   - The gains diminish substantially with more labelled data (0.5 points at 1,000 examples)

3. **Limited experimental scope**:
   - Only English datasets with short texts
   - Only BERT-base; no evaluation on larger models (BERT-large, RoBERTa, etc.) or decoder-only models
   - No evaluation on longer document classification tasks
   - Missing comparison with other recent low-resource methods
   - No multilingual evaluation despite text being a multilingual domain

4. **Hyperparameter tuning asymmetry**: CurCon uses grid search over 48 configurations on validation sets, while baselines use hyperparameters from original papers. This could introduce bias toward CurCon. While this follows common practice, a fair comparison would tune baselines similarly (or use defaults for all).

5. **Augmentation design choices lack justification**:
   - Why these specific four operators? 
   - Why these specific percentages (10% token dropout, 15% synonym replacement, 20% span deletion)?
   - Why linear curriculum rather than other schedules (exponential, sigmoid)?
   - The ablation doesn't isolate individual operator contributions

6. **Back-translation implementation details missing**:
   - Is this English↔German? Why German?
   - How sensitive is performance to translation quality?
   - Pre-computation of back-translations isn't clearly described

7. **Statistical significance**: While standard deviations are reported, no formal significance tests are provided. Some improvements appear marginal relative to variance.

8. **Limited analysis of when/why CurCon helps**:
   - Why are gains largest on SST-2 and SUBJ?
   - What properties of datasets make curricula more beneficial?
   - No error analysis or failure cases discussed

## Minor Issues

- Table 1 standard deviations could be better formatted for readability
- The claim that "curriculum schedule contributes 0.8 points" (Abstract) could be clearer—this is the difference between L=0 and full CurCon, not isolation of schedule alone
- Missing details on validation set selection (are these held-out from unlabelled data?)
- No discussion of computational cost during fine-tuning (does early stopping affect all methods equally?)

## Questions for Authors

1. Have you considered adaptive curriculum schedules (e.g., based on training dynamics)?
2. How sensitive is performance to the curriculum length hyperparameter?
3. Could you provide statistical significance tests?
4. How does performance scale to modern larger models?

## Verdict

This is a competent paper that makes a sensible contribution to low-resource text classification. The core idea—applying curriculum learning to augmentation strength in contrastive intermediate training—is intuitive and well-executed experimentally. The improvements are consistent across datasets and are particularly valuable in the extremely low-resource regime (100 examples). The method is simple, practical, and adds minimal computational overhead.

However, the technical novelty is limited (curriculum learning is well-established; the application is straightforward), and the empirical improvements, while consistent, are modest. The experimental scope is somewhat narrow (one language, one model size, short texts), and there are questions about fair baseline comparison through differential hyperparameter tuning.

The paper makes a solid incremental contribution with good experimental methodology. The work is above the acceptance threshold but not exceptional. It would be suitable for publication at a venue like ACL/EMNLP, representing a reliable, practical contribution that will be useful to practitioners working with limited labelled data.

## Scores

| Criterion | Score | Justification |
|-----------|-------|---------------|
| **Soundness** | 78 | Solid experimental design with proper averaging and ablations, but lacks statistical significance testing and has hyperparameter tuning asymmetry |
| **Novelty** | 62 | Sensible application of known curriculum learning principles; limited technical novelty; simple linear schedule |
| **Significance** | 72 | Consistent improvements with largest gains in truly low-resource regime; practical value but improvements diminish quickly with more labels |
| **Clarity** | 82 | Well-written and clear; some minor details missing but generally accessible |

## Final Score: **73.5/100**

## Recommendation: **ACCEPT**

This paper presents a simple, practical method with solid experimental validation. While not groundbreaking, it makes a reliable contribution to an important problem (low-resource text classification) with consistent empirical improvements. The work would benefit from broader evaluation and deeper analysis, but the current execution is sound and the results are meaningful for practitioners. The method's simplicity and efficiency make it practically appealing despite modest improvements.