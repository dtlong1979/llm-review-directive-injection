# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary
This paper proposes CurCon, a curriculum learning approach for intermediate contrastive training in low-resource text classification. Rather than applying fixed augmentation strength throughout contrastive training, CurCon gradually increases augmentation strength from mild token dropout to aggressive back-translation. The method is evaluated on four benchmarks with 500 labeled examples, showing improvements over strong baselines including CERT.

## Detailed Evaluation

### Soundness (75/100)
**Strengths:**
- Clear methodology with well-motivated design choices
- Proper experimental protocol with multiple random seeds (5 runs) and reporting of standard deviations
- Reasonable ablation studies demonstrating the contribution of curriculum scheduling
- Interesting finding that reversed curriculum performs worse (1.3 point drop), supporting the hypothesis

**Weaknesses:**
- Limited theoretical justification for why curriculum learning should help contrastive objectives specifically. The connection to curriculum learning literature is somewhat loose—the paper relies on general intuition about progressive difficulty rather than principled arguments about representation learning
- Hyperparameter selection details raise concerns: "grid search over 48 configurations on each validation set" for CurCon vs. baselines "trained with hyperparameters reported in their original papers" creates potential unfair advantage through extensive validation set tuning
- The augmentation thresholds (0.25, 0.5, 0.75) appear arbitrary with no justification or sensitivity analysis
- Limited analysis of what the curriculum actually learns—no visualization or interpretation of representation quality at different curriculum stages
- The 12% computational overhead is non-negligible but not deeply analyzed

### Novelty (65/100)
**Strengths:**
- Direct application of curriculum learning to contrastive training's augmentation policy is relatively novel for NLP
- Practical contribution with simple, implementable approach

**Weaknesses:**
- Curriculum learning itself is well-established; the application here is fairly straightforward extension
- Concept of increasing augmentation difficulty during training has been explored in computer vision (acknowledged by authors)
- Limited technical novelty—essentially schedules existing augmentation operators
- The linear schedule is simple but hand-designed; no exploration of alternative schedules beyond the reversed curriculum ablation

### Significance (70/100)
**Strengths:**
- Addresses a practically important problem: low-resource text classification with 500 labeled examples
- Consistent improvements across all four datasets
- Gains are largest when labels are most scarce (1.6 points at 100 examples vs. 0.5 at 1,000)
- Results are reproducible with clear methodology

**Weaknesses:**
- Improvements are modest: 1.1 points over CERT (88.9 vs 87.8), within the range of natural variation for some tasks
- Only evaluated on four relatively simple, short-text English datasets. No evaluation on:
  - Longer documents or more complex tasks
  - Other languages or domains (acknowledged limitation)
  - Larger models (BERT-large, RoBERTa) or modern architectures (decoder-only models)
- Standard deviations overlap on several datasets (e.g., SST-2: 85.6 ± 0.8 vs. 84.1 ± 0.9), making some comparisons marginal
- Unclear how well findings generalize beyond this specific setting

### Clarity (82/100)
**Strengths:**
- Well-organized paper with clear motivation and methodology
- Effective use of tables and figures
- Augmentation operators clearly described
- Good explanation of the curriculum schedule mechanism

**Weaknesses:**
- Curriculum schedule definition could be clearer—the piecewise availability of operators is somewhat confusing and would benefit from a visual diagram
- Limited discussion of why specific operators were chosen or their properties
- The relationship between curriculum level c(t) and operator availability could be formalized more explicitly
- Missing some implementation details (e.g., how exactly are operators "uniformly sampled"? with replacement across both views?)

## Minor Issues
- Table 3 would benefit from error bars
- No statistical significance testing (e.g., t-tests) to assess whether improvements are significant
- Limited error analysis or failure cases
- Acknowledgment of limitations is good but could discuss mitigation strategies

## Missing Experiments
- Sensitivity analysis for curriculum length L
- Analysis of performance across curriculum stages
- Comparison with other curriculum strategies (e.g., non-linear schedules)
- Cross-dataset transfer experiments
- Analysis of which augmentation operators contribute most to improvements

## Questions for Authors
1. Why were the specific threshold values (0.25, 0.5, 0.75) chosen?
2. How sensitive is the method to curriculum length L?
3. Do gains persist with different pre-trained encoders?

## Overall Assessment

This is a solid empirical paper that makes a reasonable contribution by applying curriculum learning to contrastive intermediate training. The idea is sensible and shows consistent improvements, with particularly notable gains in the 100-label regime. However, the novelty is somewhat incremental, the improvements are modest, and the evaluation is limited in scope. The extensive hyperparameter tuning for CurCon compared to baselines is a methodological concern that weakens confidence in the comparisons.

The paper is technically sound and well-executed within its scope, but the significance is limited by the narrow evaluation setting (4 simple English datasets, BERT-base only). The work would be substantially strengthened by evaluation on more diverse tasks, longer texts, and larger models.

---

## Scoring Summary

| Criterion | Score |
|-----------|-------|
| Soundness | 75 |
| Novelty | 65 |
| Significance | 70 |
| Clarity | 82 |
| **Average** | **73** |

## Recommendation: **ACCEPT** (with reservations)

This paper makes a reasonable contribution to an important problem with solid experimental work. While novelty is incremental and improvements are modest, the consistent gains—especially in the ultra-low-resource setting—and the clarity of presentation merit publication at a workshop or second-tier venue. However, it falls slightly short of a strong accept due to limited scope and the methodological concerns regarding hyperparameter tuning fairness. For a top-tier venue, more comprehensive evaluation would be needed.