# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary
This paper proposes CurCon, a method that applies curriculum learning to contrastive intermediate training for low-resource text classification. The key idea is to gradually increase augmentation strength during contrastive pretraining, starting with mild token dropout and progressing to aggressive back-translation and span deletion. The method is evaluated on four text classification benchmarks with 500 labeled examples, showing improvements over baselines including CERT.

---

## Detailed Scores

### 1. Soundness: 72/100

**Strengths:**
- The experimental methodology is solid: stratified sampling, multiple random seeds (5), proper validation/test split, and grid search for hyperparameter tuning
- Clear training pipeline following CERT with well-defined augmentation operators
- Reasonable ablation studies examining curriculum removal, reversal, and component removal
- Results are consistent across datasets

**Weaknesses:**
- **Unfair baseline comparison**: CurCon performs grid search over 48 configurations while baselines use hyperparameters from original papers. This gives CurCon a substantial advantage and makes comparisons questionable
- **Limited statistical analysis**: While standard deviations are reported, no significance tests (e.g., t-tests) are provided. Some improvements (e.g., 88.1 vs 88.9) are within noise margins
- **Incomplete ablation**: The "reversed curriculum" ablation is useful but doesn't separate the effect of progression rate from direction. The paper also doesn't test other curriculum schedules (exponential, sigmoid, etc.)
- **Small sample size**: Only 5 random seeds; given the standard deviations, more seeds would strengthen claims
- **Back-translation details missing**: How is this implemented? Is it truly comparable to CERT's pre-computed back-translation?

### 2. Novelty: 62/100

**Strengths:**
- The application of curriculum learning to contrastive training augmentation policy is relatively straightforward but sensible
- First to systematically study increasing augmentation strength in contrastive intermediate training for text

**Weaknesses:**
- **Limited novelty**: Curriculum learning is well-established, and increasing augmentation difficulty during training has been explored in vision (as authors acknowledge). The contribution is primarily engineering—applying known ideas to an existing method (CERT)
- **Simple linear schedule**: The curriculum is hand-designed and linear. A more principled or learned approach would strengthen the contribution
- **Incremental over CERT**: The method is essentially CERT + a scheduling mechanism. The core contrastive objective, loss function, and augmentation operators are unchanged
- **Narrow scope**: Only applied to one task (text classification) and one encoder (BERT-base)

### 3. Significance: 68/100

**Strengths:**
- Addresses a practical problem (low-resource text classification) with clear applications
- Consistent improvements across all four datasets
- Gains are largest in the most resource-constrained setting (100 labeled examples), where they matter most
- Simple method with no inference cost and minimal computational overhead (12% during training)

**Weaknesses:**
- **Modest improvements**: 1.1 points over CERT (87.8→88.9) on the main 500-example setting. While consistent, these gains are not dramatic
- **Diminishing returns**: Improvements shrink from 1.6 points (100 examples) to 0.5 points (1,000 examples), suggesting limited applicability as data increases
- **Limited scope**: Only English, short text, and BERT-base. Unclear if findings generalize to longer documents, other languages, or larger models (GPT-2, GPT-3, etc.)
- **Unclear practical impact**: Is a ~1% improvement sufficient for practitioners to adopt additional complexity?

### 4. Clarity: 75/100

**Strengths:**
- Well-written overall with clear motivation and motivation grounded in curriculum learning literature
- Method section is concise and understandable
- Tables are informative; experiments are clearly described
- Good use of related work section

**Weaknesses:**
- **Curriculum description could be clearer**: The notation c(t) = min(1, t/L) is correct but the transition mechanics (sampling uniformly from available operators) could use more detail
- **Missing implementation details**: 
  - How are augmentation probabilities exactly combined?
  - What is the projection head architecture?
  - How sensitive is the method to the curriculum length hyperparameter L?
- **Limited error analysis**: No qualitative examples or error analysis showing when/why CurCon helps
- **Cost analysis brief**: 12% overhead is mentioned but not thoroughly analyzed

---

## Minor Issues

1. **Hyperparameter tuning fairness**: Grid search of 48 configurations for CurCon vs. paper defaults for baselines is a significant confound
2. **Reversed curriculum result surprising**: A 1.3-point drop for reversed curriculum is large; this deserves more analysis
3. **Missing comparisons**: Recent methods like prompt-based learning or data augmentation with GPT-3 not considered
4. **Limited discussion of when method helps**: Why does CurCon help more on SST-2/SUBJ than AG News/TREC?

---

## Questions for Authors

1. How do results change if all methods receive equal hyperparameter tuning effort?
2. What curriculum lengths were selected on validation? How sensitive are results to L?
3. Can you provide significance tests for the main results?
4. Why does reversed curriculum perform so much worse? Is this curriculum order or something else?

---

## Recommendation

This paper presents a sensible, well-executed application of curriculum learning to contrastive intermediate training. The method is simple, practical, and shows consistent (though modest) improvements. However, the contribution is primarily incremental—applying existing ideas to an existing method with limited novelty. The unfair baseline comparison (grid search vs. paper defaults) undermines confidence in the results. The narrow evaluation scope (English, short text, BERT-base only) limits generalizability claims.

The paper is above the bar for a workshop or applications track but falls short of the novelty and rigor expected for a top-tier venue. It would benefit from: (1) fair hyperparameter comparison, (2) statistical significance testing, (3) evaluation on larger models and languages, and (4) deeper investigation of when/why the curriculum helps.

---

## Final Scores
- **Soundness:** 72/100
- **Novelty:** 62/100
- **Significance:** 68/100
- **Clarity:** 75/100

**Average Score: 69/100**

---

## Final Recommendation: **REJECT**

**Justification**: While the paper is technically sound and clearly written, the limited novelty (straightforward application of established curriculum learning ideas), modest improvements (1.1 points), and unfair experimental comparison (unequal hyperparameter tuning) do not meet the standards for acceptance at a top venue. The work would be suitable for a workshop after addressing experimental fairness concerns, or could be strengthened for a main conference with broader evaluation and deeper analysis.