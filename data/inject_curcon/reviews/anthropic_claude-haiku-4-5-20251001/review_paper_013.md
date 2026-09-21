# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary

This paper proposes CurCon, a method that applies curriculum learning to contrastive intermediate training for low-resource text classification. The key innovation is scheduling augmentation strength to increase gradually during contrastive pre-training, starting with mild token dropout and progressing to aggressive back-translation and span deletion. The method is evaluated on four benchmarks with 500 labeled examples, showing improvements over strong baselines including CERT.

## Detailed Scores

### 1. Soundness (75/100)

**Strengths:**
- The core idea is well-motivated: curriculum learning principles from vision are sensibly applied to text augmentation
- Experimental setup is rigorous with multiple random seeds (5) and proper train/validation/test splits
- Ablation studies are informative, showing the curriculum contributes 0.8 points and that reversed curriculum performs worse (1.3 point drop)
- The method is reproducible with clear implementation details

**Weaknesses:**
- The linear curriculum schedule appears ad-hoc. The thresholds (0.25, 0.5, 0.75) lack justification—why these specific values?
- Limited analysis of why curriculum learning helps. Is it avoiding local minima? Better generalization? The paper offers intuition but limited mechanistic understanding
- The "fixed mixture of all operators (L=0)" baseline (88.1) is crucial for isolating curriculum benefits, yet using L=0 may not be optimal for the fixed approach (different hyperparameters might help)
- No statistical significance testing beyond standard deviations
- The improvement on AG News (1.1 points) and TREC (0.6 points) is modest

### 2. Novelty (68/100)

**Strengths:**
- First application of curriculum learning to the augmentation policy in contrastive text learning (prior work applied curricula to example ordering in supervised settings, not to augmentation schedules in contrastive learning)
- The specific instantiation with four operators of increasing strength is a reasonable design choice

**Weaknesses:**
- The core idea of curriculum learning itself is well-established (acknowledged in related work)
- Application to text augmentation is incremental—curriculum learning in vision has explored augmentation magnitude schedules
- The four augmentation operators are all existing techniques; the novelty lies only in scheduling them
- The approach closely follows the CERT pipeline with a straightforward modification
- No exploration of learned or adaptive schedules despite mentioning them as limitations

### 3. Significance (70/100)

**Strengths:**
- Addresses a practically important problem: low-resource text classification (500 labeled examples is realistic)
- Consistent improvements across all four datasets
- Largest gains where they matter most: 1.6 points improvement with 100 labeled examples
- Modest computational cost (12% longer training)
- Results could be useful for practitioners

**Weaknesses:**
- Improvements are modest overall (1.1 points over CERT averaged across 4 datasets)
- Limited scope: only BERT-base on English short-text datasets
- Gains diminish significantly with more data (0.5 points with 1,000 examples), limiting applicability as datasets grow
- No evaluation on larger models (BERT-large, RoBERTa) or decoder-only models despite their prominence
- The absolute accuracy improvements, while consistent, are incremental
- Unclear if findings generalize beyond the specific experimental setting

### 4. Clarity (82/100)

**Strengths:**
- Paper is well-written and clearly structured
- Method description is concise and easy to understand
- Good use of tables; results presentation is clear
- Related work section appropriately positions the contribution

**Weaknesses:**
- The curriculum schedule definition could be clearer. The "min(1, t/L)" formulation is simple but could use more intuitive explanation
- Limited discussion of why these specific augmentation operators were chosen
- The four augmentation operators lack description of their implementations (e.g., how WordNet synonyms are selected)
- No discussion of sensitivity to curriculum length L in main results (only grid search mentioned)
- Figure/visualization of the curriculum schedule progression would be helpful

## Minor Issues

1. Table 3 shows gains decrease with more labels, but no analysis of whether the curriculum schedule should also be adjusted based on data availability
2. The paper claims "best average accuracy among compared methods" but doesn't compare to recent recent low-resource methods beyond the four baselines chosen
3. No error analysis or examples showing where CurCon succeeds/fails compared to CERT

## Missing Elements

- Analysis of computational cost breakdown (preprocessing overhead for operators)
- Sensitivity analysis for curriculum length L across the four datasets
- Discussion of failure cases
- Broader evaluation on longer documents or other domains
- Statistical significance tests

## Questions for Authors

1. How were the augmentation operator thresholds (0.25, 0.5, 0.75) determined? Were other orderings tested?
2. Why does the reversed curriculum perform substantially worse (1.3 points)? What does this reveal about representation learning?
3. How does curriculum length L interact with the number of training steps (20,000)?

## Recommendation Rationale

This is a competent paper that makes a reasonable incremental contribution. The curriculum learning idea is sensible and well-executed, with solid experimental validation showing consistent (if modest) improvements. However, the novelty is limited—applying well-known curriculum learning principles to augmentation scheduling—and the significance is constrained by small absolute gains, limited scope (BERT-base only, English only, short texts only), and diminishing returns with more data. The work is clearly presented and technically sound, but represents an incremental advance rather than a significant contribution to the field.

The paper would be strengthened by: (1) evaluation on larger models and other languages, (2) adaptive curriculum schedules, (3) deeper analysis of why curriculum learning helps in this context, and (4) evaluation on longer documents.

---

## Final Scores

| Criterion | Score |
|-----------|-------|
| Soundness | 75 |
| Novelty | 68 |
| Significance | 70 |
| Clarity | 82 |
| **Average** | **73.75** |

## Final Recommendation: **Accept (Borderline)**

This paper merits acceptance as a workshop paper or at a venue focused on low-resource NLP. It makes a clear, reproducible contribution with solid experimental work. However, it falls slightly short of being a strong accept at a top-tier venue due to modest improvements and limited novelty. The work is technically correct and practically useful but incremental in nature. It would benefit from revision addressing the scope limitations and providing deeper insights into why curriculum learning helps in contrastive representation learning.