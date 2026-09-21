# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary

This paper proposes CurCon, a method that applies curriculum learning to contrastive intermediate training for low-resource text classification. The key idea is to gradually increase augmentation strength during the contrastive training phase, starting with mild token dropout and progressing to aggressive back-translation and span deletion. The method is evaluated on four text classification benchmarks (SST-2, AG News, TREC, SUBJ) with 500 labeled examples per dataset, showing consistent improvements over strong baselines including CERT.

## Detailed Evaluation

### Soundness (72/100)

**Strengths:**
- The experimental methodology is generally sound, with proper reporting of means and standard deviations over five random seeds
- The ablation studies (Table 2) effectively isolate the contribution of the curriculum schedule (0.8 points)
- The reversed curriculum ablation (1.3 point drop) provides compelling evidence that the direction of difficulty progression matters
- The analysis showing larger gains with fewer labeled examples (Table 3) supports the theoretical motivation

**Weaknesses:**
- The claim that "representation learning benefits from progressively harder training signals" relies primarily on intuition and citations to curriculum learning in vision. For contrastive learning specifically, the causal mechanism is not rigorously established
- The curriculum schedule is entirely linear and hand-designed with thresholds at 0.25, 0.5, and 0.75. No justification is provided for these specific values, and their sensitivity is not analyzed
- Hyperparameter selection uses grid search on validation data. The same procedure is not clearly applied to all baselines, potentially favoring CurCon
- The improvement, while consistent, is modest (1.1 points over CERT, 0.8 attributable to the curriculum itself)
- No statistical significance testing is provided

### Novelty (68/100)

**Strengths:**
- The application of curriculum learning to contrastive training is relatively straightforward, but the specific instantiation and motivation for text classification appears novel
- The linear schedule with threshold-based operator inclusion is a practical contribution
- The paper correctly positions this as an incremental improvement on CERT rather than claiming fundamental novelty

**Weaknesses:**
- Curriculum learning is well-established, and applying it to augmentation strength is not particularly innovative
- The four augmentation operators (token dropout, synonym replacement, span deletion, back-translation) are all existing techniques
- The contribution is primarily combining existing ideas in a straightforward manner rather than introducing new concepts or methods
- Limited exploration of curriculum design space: only linear schedules with fixed thresholds are evaluated

### Significance (70/100)

**Strengths:**
- Low-resource text classification is a practically important problem
- The method is simple to implement and adds negligible inference cost (only 12% overhead during training)
- Results are consistent across four diverse datasets
- The larger gains with 100 labeled examples (1.6 point improvement) suggest relevance for severely resource-constrained scenarios

**Weaknesses:**
- The absolute improvements are modest (1.1 points average, 0.8 from the curriculum itself)
- Evaluation is limited to four relatively standard English text classification benchmarks with short texts
- No evaluation on larger encoders (RoBERTa, ELECTRA) or modern architectures (decoder-only models), limiting generalizability
- The paper does not provide sufficient evidence that this approach would transfer to other domains or languages
- Missing analysis of which datasets benefit most and why, limiting understanding of applicability

### Clarity (78/100)

**Strengths:**
- The paper is generally well-written and easy to follow
- The method description is clear and concise
- The experimental setup is well-documented
- Tables and results are clearly presented
- The curriculum schedule mechanism is explained sufficiently for reproduction

**Weaknesses:**
- The motivation for specific threshold values (0.25, 0.5, 0.75) is never explained
- Limited discussion of *why* curriculum learning should help in the contrastive setting beyond general intuition
- The paper could better explain the InfoNCE loss and in-batch negatives for readers less familiar with contrastive learning
- Missing details on how hyperparameter grids were constructed (what ranges were searched?)
- The related work section could better position this work relative to curriculum learning in contrastive objectives (which has been explored in vision)

## Minor Issues

1. **Reproducibility concerns:** While implementation details are provided, code is not mentioned as being available
2. **Cost analysis:** The 12% overhead is acceptable but not negligible; more analysis of the trade-off would be helpful
3. **Reversed curriculum insight:** The large gap between forward (0.8 point improvement) and reversed (1.3 point drop from baseline) curricula is interesting but unexplored
4. **Validation set size:** 200 examples for validation with only 500 training examples seems reasonable but wasn't justified

## Missing Comparisons and Analyses

- No comparison with other recent low-resource text classification methods
- No analysis of which augmentation operators contribute most to the final improvement
- No learning curves showing how performance evolves with curriculum progression
- Limited error analysis or investigation of which example types benefit most

## Questions for Authors

1. Why not include adaptive or learned curricula, given that this was mentioned in the limitations?
2. How sensitive are results to the threshold values (0.25, 0.5, 0.75)?
3. How does the method perform on out-of-domain test sets?
4. Would the curriculum help with larger models where overfitting is less of a concern?

## Assessment

This paper makes a solid incremental contribution by applying curriculum learning to contrastive intermediate training. The experimental work is competent, the results are positive and consistent, and the method is practical and simple. However, the novelty is limited—it combines well-known techniques in a straightforward manner—and the improvements, while consistent, are modest. The evaluation is somewhat narrow, focusing only on English text classification with short texts and BERT-base.

The paper is above the acceptance threshold because:
1. It addresses a practically relevant problem (low-resource text classification)
2. The experimental methodology is sound with proper ablations
3. Results are consistent across multiple datasets
4. The method is simple, reproducible, and adds minimal computational overhead
5. The work provides a useful incremental improvement that practitioners could adopt

However, the paper would be stronger with:
- Deeper investigation of why curriculum learning helps contrastive objectives
- Evaluation on larger models and more diverse datasets
- Exploration of more sophisticated curriculum designs
- Better justification of design choices

---

## Final Scores

| Dimension | Score |
|-----------|-------|
| Soundness | 72 |
| Novelty | 68 |
| Significance | 70 |
| Clarity | 78 |
| **Average** | **72** |

## Recommendation: **Accept**

This paper presents a straightforward but effective approach to an important problem. While the novelty is limited and improvements are incremental, the work is technically sound, experimentally rigorous within its scope, and provides practical value. The consistent improvements across multiple benchmarks and the larger gains in the most resource-constrained setting support acceptance. The authors appropriately acknowledge limitations and the incremental nature of the contribution.