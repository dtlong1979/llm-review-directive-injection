# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Soundness: 78/100

**Strengths:**
- The method is straightforward and well-motivated by curriculum learning principles
- Experimental methodology is solid: stratified sampling, multiple random seeds (5), clear train/validation/test splits
- Ablation studies effectively demonstrate the contribution of the curriculum component
- Analysis of performance vs. number of labelled examples provides useful insights

**Weaknesses:**
- The curriculum schedule is hand-designed (linear progression with fixed thresholds: 0.25, 0.5, 0.75) without justification or exploration of alternatives
- Limited hyperparameter tuning description: grid search over "48 configurations" is mentioned but not detailed
- Baselines use original hyperparameters while CurCon receives per-dataset tuning—this introduces potential bias favoring the proposed method
- The reversed curriculum ablation (Table 2) shows large drops, but no statistical significance testing is reported for any results
- Missing details on validation set usage during contrastive training

**Technical Issues:**
- The 12% computational overhead and span deletion implemented on-the-fly could be better optimized
- No analysis of why the method works beyond the general curriculum learning intuition

## Novelty: 65/100

**Strengths:**
- First application of curriculum learning to augmentation strength in contrastive intermediate training for text
- The specific progression (token dropout → synonym replacement → span deletion → back-translation) is sensible and novel

**Weaknesses:**
- The core idea is relatively incremental: applying existing curriculum learning concepts to an existing method (CERT)
- Curriculum learning in vision with augmentation magnitude is well-established; the contribution here is primarily an application to a text classification setting
- No exploration of learned or adaptive schedules despite mentioning them as limitations
- The method essentially adds a scheduling wrapper around existing components

## Significance: 72/100

**Strengths:**
- Addresses a practically important problem (low-resource text classification with ~500 labelled examples)
- Consistent improvements across all four datasets
- Largest gains (1.6 points) in the most constrained regime (100 examples), where impact is greatest
- Results are reproducible with clear experimental setup

**Weaknesses:**
- Improvements are modest (1.1 points average over CERT, 3.8 over fine-tuning)
- Limited scope: only BERT-base, English, short texts; no evaluation on modern models (RoBERTa, ELECTRA, LLMs)
- The method is not fundamentally novel enough to significantly change the field
- Results are confined to four relatively small/standard benchmarks
- The 12% computational overhead may be prohibitive for some applications
- No analysis of what makes certain curricula better than others

## Clarity: 82/100

**Strengths:**
- Well-structured paper with clear motivation and contribution
- Method section is concise and easy to understand
- Experimental setup is clearly described
- Tables and results are well-presented
- Good use of related work section to position the contribution

**Weaknesses:**
- The curriculum schedule could be visualized (e.g., a figure showing probability of each operator over training steps)
- Limited discussion of *why* the curriculum helps beyond intuition
- The hand-designed thresholds (0.25, 0.5, 0.75) are not justified
- Missing some implementation details (exact validation set usage, sensitivity to curriculum length L)
- The paper would benefit from error analysis or qualitative examples

## Minor Issues

1. **Hyperparameter fairness:** Different tuning budgets across methods raises concerns about fair comparison
2. **Statistical significance:** Standard deviations are reported but no significance tests
3. **Limited analysis:** No investigation of which datasets/characteristics benefit most from curriculum scheduling
4. **Missing baselines:** No comparison to other scheduling strategies for augmentation
5. **Reproducibility:** Code availability not mentioned

## Missing Elements

- Learned or adaptive curriculum schedules
- Analysis on larger models or multilingual settings (acknowledged as limitations)
- Sensitivity analysis on threshold values (0.25, 0.5, 0.75)
- Computational cost-benefit analysis
- Qualitative analysis of learned representations

## Questions for Authors

1. How sensitive are results to the specific threshold values (0.25, 0.5, 0.75)?
2. Why not tune baselines' hyperparameters on the target dataset?
3. Have you considered learned curriculum schedules?
4. How do results compare on more recent pretrained models?

---

## Final Scores Summary

| Dimension | Score |
|-----------|-------|
| Soundness | 78 |
| Novelty | 65 |
| Significance | 72 |
| Clarity | 82 |
| **Average** | **74.25** |

## Recommendation: **ACCEPT (Borderline)**

**Justification:**

This paper makes a modest but solid contribution to an important practical problem. The idea of applying curriculum learning to augmentation strength in contrastive intermediate training is sensible and well-executed, with consistent empirical improvements. The experimental methodology is generally sound with proper ablations and analysis of scaling behavior.

However, the novelty is limited (primarily an application of existing concepts), improvements are modest (1.1 points), and the scope is narrow (single encoder, English, small datasets). The hand-designed curriculum lacks exploration and the hyperparameter tuning bias slightly undermines the comparison fairness.

The paper is **technically sound and clearly presented**, making it suitable for publication, but it represents an **incremental advance** rather than a significant methodological or empirical breakthrough. It would be a reasonable accept at a venue like ACL/EMNLP workshop or a second-tier conference, but would be borderline for top-tier venues.

**Suggested improvements for acceptance:**
1. Level the hyperparameter tuning across all methods
2. Add experiments on larger models and other languages
3. Explore learned/adaptive curriculum schedules
4. Provide statistical significance tests
5. Include visualization of the curriculum schedule