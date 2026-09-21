# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Soundness: 82/100

**Strengths:**
- The experimental methodology is solid: proper stratified sampling, reporting of means and standard deviations over 5 seeds, appropriate validation set usage with early stopping
- The curriculum design is theoretically motivated by curriculum learning principles and empirically validated through ablations
- The reversed curriculum ablation (Table 2) provides good evidence that the specific ordering matters rather than just increased diversity
- Hyperparameter selection via grid search on validation sets is appropriate

**Weaknesses:**
- Limited baseline coverage: no comparison with more recent approaches (paper appears to be from 2021-2022 era, but even contemporary semi-supervised methods could strengthen claims)
- The curriculum schedule is entirely linear and hand-designed without justification for why linear interpolation is optimal
- The ablation on augmentation operators is incomplete—we don't see individual contributions of each operator or their interactions
- Pre-computation of back-translation is mentioned but not analyzed: unclear if this affects the contrastive training dynamics compared to dynamic computation
- No analysis of hyperparameter sensitivity, particularly for the curriculum length L across different datasets

## Novelty: 72/100

**Strengths:**
- The application of curriculum learning to augmentation strength in contrastive intermediate training is straightforward and intuitive, filling a clear gap
- While not deeply novel, the idea is sensible and previously unexplored in this specific context
- The paper clearly positions itself as building on CERT with a targeted improvement rather than claiming broader novelty

**Weaknesses:**
- The core contribution is relatively incremental—applying existing curriculum learning ideas to an existing method (CERT) with a linear schedule
- The augmentation operators themselves are standard (token dropout, synonym replacement, span deletion, back-translation are all from prior work)
- The curriculum design lacks sophistication: a fixed linear schedule is elementary compared to recent curriculum learning work in other domains
- Limited exploration of the design space (why these four operators? why these thresholds at 0.25, 0.5, 0.75?)

## Significance: 78/100

**Strengths:**
- Addresses a practically important problem: low-resource text classification with only 500 labelled examples is highly relevant
- Improvements are consistent across all four datasets, suggesting robustness
- The observation that gains are largest when labels are scarce (Table 3: 1.6 points at 100 examples) is valuable and well-demonstrated
- The simplicity of the method makes it easily adoptable by practitioners
- 12% training time overhead is acceptable for the accuracy gains

**Weaknesses:**
- Improvements, while consistent, are modest (0.8-1.5 points over CERT depending on dataset)
- Evaluation is limited to four English datasets with relatively short texts, reducing generalizability claims
- No evaluation on truly challenging scenarios (extremely low-resource regimes like 50 examples, or highly specialized domains)
- Impact limited to text classification; broader applicability to other NLP tasks is unexplored
- Only evaluated on BERT-base; unclear if the curriculum approach works with larger models or different architectures

## Clarity: 88/100

**Strengths:**
- Well-written with clear motivation and problem statement
- The method description is concise and precise (Section 3)
- Experimental setup is clearly documented with reproducible details
- Tables are informative and results clearly presented
- The curriculum formulation (c(t) = min(1, t/L)) is simple and easy to understand

**Weaknesses:**
- Limited discussion of *why* curriculum learning should help contrastive learning beyond general intuition
- The relationship between contrastive temperature and curriculum schedule could be better explained
- Missing some implementation details: how are the four operators weighted when all are available? How sensitive is the method to the specific threshold values (0.25, 0.5, 0.75)?

## Minor Issues

1. The claim that representation learning "benefits from progressively harder training signals" in the abstract needs more empirical support beyond this paper
2. Table 3 would benefit from error bars to indicate statistical significance of differences at different data scales
3. The related work section could better position the work relative to other curriculum learning applications in NLP
4. No discussion of failure cases or datasets where CurCon underperforms

## Missing Experiments

- Per-operator contribution analysis
- Sensitivity analysis for curriculum thresholds (0.25, 0.5, 0.75)
- Comparison with non-linear curriculum schedules
- Evaluation on datasets with longer texts or specialized domains
- Results on BERT-large or other model families

## Questions for Authors

1. Why these specific threshold values (0.25, 0.5, 0.75)? Were other values explored?
2. What is the curriculum length L typically set to relative to T?
3. How does performance vary with different orderings of operators?

---

## Summary Assessment

This is a competent paper that makes a modest but solid contribution to low-resource text classification. The core idea—applying curriculum learning to augmentation strength in contrastive intermediate training—is intuitive and well-executed. The experimental work is careful, with proper reporting of uncertainty and ablations that validate the approach. The writing is clear and the method is practical.

However, the novelty is limited (applying existing curriculum learning to an existing method with a linear schedule), the improvements are incremental (0.8-1.1 points), and the evaluation scope is narrow (four English datasets, short texts, BERT-base only). The lack of sophisticated curriculum design and incomplete ablations on operator contributions are minor weaknesses.

The paper makes a valuable incremental contribution to an important practical problem with a simple, reproducible method. While not groundbreaking, it represents solid scientific work with clear relevance to practitioners working in low-resource settings.

---

## Final Scores

| Dimension | Score |
|-----------|-------|
| Soundness | 82 |
| Novelty | 72 |
| Significance | 78 |
| Clarity | 88 |
| **Average** | **80** |

## Recommendation: **ACCEPT**

This paper merits acceptance as a solid, well-executed contribution to low-resource text classification. While the novelty is incremental and improvements modest, the work is technically sound, addresses a practical problem, and provides consistent empirical validation. The simplicity and reproducibility of the method, combined with its consistent gains across datasets and particularly strong results in extremely low-resource settings (100 examples), make it a valuable addition to the literature. The limitations are appropriately acknowledged, and the work would benefit the community interested in practical NLP applications with limited labeling budgets.