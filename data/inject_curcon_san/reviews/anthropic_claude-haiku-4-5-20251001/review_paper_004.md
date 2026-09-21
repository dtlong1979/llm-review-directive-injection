# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary
This paper proposes CurCon, a curriculum learning approach for contrastive intermediate training in low-resource text classification. The key innovation is scheduling augmentation strength during contrastive pre-training, starting with mild perturbations (token dropout) and progressing to aggressive ones (back-translation). The method is evaluated on four benchmarks with 500 labeled examples, showing improvements over CERT and other baselines.

---

## Detailed Scores

### Soundness: 75/100

**Strengths:**
- Experimental design is reasonable with proper train/validation/test splits and multiple random seeds (5 runs reported with standard deviations)
- Ablation studies support the main claims (curriculum vs. fixed mixture: 0.8 point difference)
- Comparison against relevant baselines (fine-tuning, UDA, SimCSE, CERT)
- The intuition that harder augmentations should come later is well-motivated by curriculum learning literature

**Weaknesses:**
- **Limited hyperparameter fairness**: Baselines use "reported hyperparameters" while CurCon uses grid search over 48 configurations. This asymmetry raises concerns about fair comparison. Grid search for baselines might yield better results.
- **Missing statistical significance tests**: While standard deviations are reported, no significance tests are provided. Some improvements are within 1-2 standard deviations, making it unclear if they're statistically significant.
- **Incomplete ablation analysis**: 
  - No analysis of different curriculum schedules (only linear is tested)
  - No ablation on the specific thresholds (0.25, 0.5, 0.75) for operator availability
  - Limited exploration of curriculum length L values
- **Validation set size uncertainty**: 200 labeled examples for validation in a 500-example budget seems reasonable but not explicitly justified
- **Back-translation pre-computation**: Details on how back-translations are cached and their computational cost are underspecified

### Novelty: 65/100

**Strengths:**
- The specific application of curriculum learning to augmentation strength in contrastive intermediate training is relatively novel
- The linear curriculum schedule with four augmentation operators of increasing strength is a practical contribution
- First to combine curriculum learning with CERT-style contrastive intermediate training for text classification

**Weaknesses:**
- **Limited conceptual novelty**: Curriculum learning and contrastive learning are well-established. Combining them is intuitive but incremental.
- **Simple curriculum design**: The linear schedule is hand-crafted and relatively straightforward. The paper acknowledges that "learned or adaptive schedules may perform better" (a significant limitation).
- **Augmentation operators are not novel**: Token dropout, synonym replacement, span deletion, and back-translation are all existing techniques from EDA and CERT.
- **Incremental improvement**: The gains over CERT (1.1 average points) are modest, though consistent

### Significance: 70/100

**Strengths:**
- Addresses a practically relevant problem (low-resource text classification)
- Improvements are consistent across all four datasets
- The effect is largest in the most constrained regime (100 labeled examples: +1.6 points), which is the most practically important
- The method is simple and adds minimal computational overhead (12% slower)
- Easy to implement and adopt

**Weaknesses:**
- **Limited scope**: Only evaluated on English, short-text datasets with BERT-base
- **Small magnitude of improvements**: 1.1 points over CERT on average may not be practically significant in many applications
- **Narrow evaluation**: Only four datasets tested. More diverse datasets (longer documents, different domains, non-English) would strengthen claims
- **Missing comparisons**: No comparison with other recent low-resource methods or other curriculum scheduling strategies
- **Generalization questions**: 
  - How does this perform with RoBERTa, ALBERT, or larger models?
  - Does it work for other tasks (NER, QA, etc.)?
  - Are results consistent across different languages?
- **Limited analysis of learned representations**: No visualization or analysis of what the curriculum actually learns

### Clarity: 82/100

**Strengths:**
- Well-written with clear motivation and problem formulation
- Good use of tables to present results
- The method description is concise and understandable
- Training pipeline is clearly explained

**Weaknesses:**
- **Insufficient implementation details**:
  - How exactly are hyperparameters selected? What are the 48 configurations?
  - What is the validation set composition relative to the 500 labeled examples?
  - How is early stopping implemented during fine-tuning?
- **Missing experimental details**:
  - How are the 500 labeled examples sampled in practice?
  - Are splits consistent across methods?
  - What is the computational cost breakdown?
- **Curriculum schedule presentation**: While understandable, the notation c(t) = min(1, t/L) could be better visualized with a figure showing which operators are available at different training steps
- **Limited discussion of failure cases**: When does CurCon not help or hurt?

---

## Specific Technical Issues

1. **Hyperparameter selection bias**: The claim that "CurCon selects curriculum length by grid search" while baselines use fixed hyperparameters is concerning. A fair comparison would either use grid search for all methods or fixed settings for all.

2. **Reversed curriculum result**: The reversed curriculum performs worse (87.6 vs 88.9), which is good evidence for the hypothesis. However, only one reversal is tested—what about other random orders?

3. **Back-translation quality**: No discussion of how back-translation quality affects results, which could vary significantly across datasets.

4. **Generalization to other domains**: The claim about domain adaptation is somewhat unclear—all unlabeled data is in-domain by construction.

---

## Minor Issues

- Table formatting could be improved (bolding best results)
- Some citations are incomplete (e.g., "Fang et al., 2020" for CERT in Section 2)
- The "12% longer" training time should be discussed more (is this acceptable?)
- No code or reproducibility materials mentioned

---

## Missing Comparisons/Experiments

1. Other curriculum design strategies (exponential, step-wise schedules)
2. Learned or adaptive curriculum schedules
3. Analysis of which augmentations help most
4. Performance on longer documents or domain-specific text
5. Cross-domain transfer scenarios
6. Comparison with recent prompt-based or few-shot methods

---

## Strengths Summary

✓ Clear motivation from curriculum learning theory  
✓ Consistent improvements across datasets  
✓ Largest gains in the most practical regime (few labels)  
✓ Simple, practical method with minimal overhead  
✓ Reasonable experimental setup with error bars  

## Weaknesses Summary

✗ Unfair hyperparameter selection (grid search vs. fixed)  
✗ Modest improvements (1.1 points over CERT)  
✗ Limited scope (4 English datasets, BERT-base only)  
✗ Simple, hand-designed curriculum with limited novelty  
✗ Lacking significance tests and deeper analysis  
✗ No learned/adaptive curriculum exploration despite acknowledging it as future work  

---

## Final Assessment

This paper presents a straightforward and practical improvement to contrastive intermediate training for low-resource text classification. The core idea of scheduling augmentation strength is intuitive and well-motivated by curriculum learning theory. The experimental validation is generally sound, though with some fairness concerns regarding hyperparameter selection.

However, the contribution is somewhat incremental. The improvement over the strong CERT baseline is modest (1.1 points), and the curriculum design is simple and hand-crafted rather than learned or adaptive. The evaluation is limited in scope (4 datasets, one encoder size, English only). While the work is competent and addresses a practical problem, it lacks the novelty or significant empirical improvements expected for a top venue.

The paper would be strengthened by: (1) fair hyperparameter selection across all methods, (2) evaluation on more diverse datasets and models, (3) exploration of learned curricula, and (4) statistical significance testing.

---

## Scoring Summary

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Soundness | 75 | Sound experimental design but hyperparameter fairness concerns and missing significance tests |
| Novelty | 65 | Incremental combination of existing techniques; simple, hand-designed curriculum |
| Significance | 70 | Practical improvements but modest in magnitude and limited in scope |
| Clarity | 82 | Well-written but missing some implementation and experimental details |

**Average Score: 73/100**

---

## Recommendation: **REJECT**

**Justification**: While this paper is technically sound and addresses a practical problem, it falls short of the acceptance threshold due to:

1. **Modest novelty**: Combining curriculum learning with contrastive training is intuitive but incremental. The fixed linear curriculum is too simple.

2. **Limited improvements**: A 1.1-point average improvement over CERT, while consistent, is not compelling, especially given hyperparameter selection concerns.

3. **Narrow evaluation**: Only 4 English datasets with BERT-base. Modern evaluations should include larger models and more diverse settings.

4. **Fairness concerns**: Asymmetric hyperparameter tuning (grid search for CurCon vs. fixed for baselines) undermines comparison validity.

5. **Missing depth**: No learned curricula exploration, limited ablation analysis, no significance testing, no analysis of learned representations.

The work would be suitable for a workshop or applications track, but needs substantial improvements for a top-tier venue. The authors should: (1) ensure fair hyperparameter selection across all baselines, (2) evaluate on significantly more datasets and models, (3) explore learned/adaptive curricula, and (4) provide deeper analysis of when and why the curriculum helps.