# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Soundness: 75/100

**Strengths:**
- The experimental methodology is rigorous: multiple random seeds (5), proper train/validation/test splits, stratified sampling
- Comprehensive ablations that validate design choices (Table 2 shows curriculum vs. fixed mixture, reversed curriculum, and component removal)
- Clear baseline comparisons against relevant methods (fine-tuning, UDA, SimCSE, CERT)
- Results consistently reported with standard deviations

**Weaknesses:**
- The curriculum schedule (Equation: c(t) = min(1, t/L)) is linear and somewhat arbitrary. No justification for threshold choices (0.25, 0.5, 0.75) or why linear scheduling is optimal
- Limited hyperparameter search: only grid search over 48 configurations. No sensitivity analysis for the curriculum length L itself
- The reversed curriculum ablation (Table 2: 87.6 accuracy) is interesting but unexplained. Why does it underperform so significantly? This deserves deeper investigation
- Computational cost analysis is superficial (12% slower than CERT) without breakdown by operation
- No statistical significance testing beyond standard deviations—unclear if 0.8-1.1 point improvements are statistically significant

## Novelty: 65/100

**Strengths:**
- Novel application of curriculum learning to the augmentation policy in contrastive learning (most prior work applies curriculum to example ordering)
- Practical and straightforward approach that doesn't require architectural changes
- The combination of four augmentation operators with scheduled introduction is well-motivated

**Weaknesses:**
- The core idea is incremental: applying existing curriculum learning principles to an existing method (CERT)
- The four augmentation operators are all pre-existing (token dropout from SimCSE, synonym replacement from EDA, span deletion, back-translation)
- The scheduling mechanism is simple and somewhat hand-crafted rather than learned or theoretically derived
- Limited exploration of the design space: only linear curriculum, only four operators, only one scheduling strategy

## Significance: 70/100

**Strengths:**
- Addresses a practically important problem (low-resource text classification with 500 labeled examples)
- Consistent improvements across all four tested datasets
- Gains are larger when labeled data is scarce (1.6 points improvement at 100 examples vs. 0.5 at 1,000), which is where the approach matters most
- The method is simple to implement and adds no inference cost

**Weaknesses:**
- Improvements are modest (1.1 points over CERT, though solid)
- Limited scope: only English, short texts, BERT-base only
- Results are on relatively standard benchmarks (SST-2, AG News, TREC, SUBJ)
- No evaluation on more challenging modern benchmarks or larger models (as acknowledged in limitations)
- The practical impact is questionable given that UDA achieves 86.9 average accuracy with a different approach that may be simpler

## Clarity: 82/100

**Strengths:**
- Well-structured paper with clear motivation
- Figure/table presentation is effective and easy to interpret
- Method description is concise and understandable
- Good use of ablation studies to justify design choices

**Weaknesses:**
- The curriculum schedule presentation (c(t) = min(1, t/L)) could be clearer with a visual illustration
- Limited discussion of why the threshold values (0.25, 0.5, 0.75) were chosen
- The reversed curriculum result is mentioned but not analyzed—why does going from hard to easy hurt so much?
- Missing details on how the "fixed mixture of all operators" baseline (L=0) differs from CERT in the paper (though it appears to use a different mixture)

## Specific Technical Issues

1. **Experimental Design:** Why are hyperparameters selected only for CurCon via grid search, but baselines use published hyperparameters? This could bias results in CurCon's favor.

2. **Missing Analysis:** Table 3 shows gains decrease with more labeled data, but no analysis of why the curriculum helps less with more labels. Does the curriculum help representation quality, label efficiency, or both?

3. **Reproducibility:** While implementation details are provided, the paper lacks code/data availability statements. How are back-translations computed? Which MT system?

## Minor Issues

- Standard deviations in Table 1 are small but no significance tests
- The "back-translation through German" is mentioned casually—why German specifically?
- Figure showing curriculum schedule progression would be helpful

## Missing Comparisons

- No comparison to other curriculum learning approaches in contrastive learning
- No comparison to more recent methods beyond CERT (2020)

---

## Summary

**CurCon** presents a practical and well-executed study applying curriculum learning to contrastive intermediate training. The empirical results are solid and consistently show improvements, particularly in low-data regimes. However, the novelty is incremental (applying existing curriculum learning to an existing method with existing augmentations), and the improvements, while consistent, are modest. The paper is well-written but lacks deeper investigation into *why* the curriculum helps (beyond intuition) and explores a relatively limited design space.

The paper makes a useful contribution to low-resource NLP but falls short of being a strong accept due to limited novelty and scope.

---

## Final Scores

| Dimension | Score |
|-----------|-------|
| Soundness | 75 |
| Novelty | 65 |
| Significance | 70 |
| Clarity | 82 |
| **Average** | **73** |

## Recommendation: **ACCEPT (Borderline)**

**Justification:** This is a competent, well-executed paper with consistent experimental validation and practical value for low-resource text classification. The curriculum-scheduled augmentation idea is sensible and produces reliable improvements. However, it is primarily an incremental contribution that combines existing techniques without deep theoretical insight or broad empirical scope. It would be suitable for a workshop or a specialized venue, but represents solid incremental work rather than a significant advance. For a top-tier conference, it would be a borderline accept depending on the acceptance bar and competing submissions.

**Acceptance at:** Workshop, domain-specific venue, or second-tier conference  
**Likely rejection at:** Top-tier venues (ACL, NeurIPS, ICLR) without strengthening novelty or scope