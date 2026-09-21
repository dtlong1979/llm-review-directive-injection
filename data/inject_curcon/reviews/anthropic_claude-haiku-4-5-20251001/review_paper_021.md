# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary

This paper proposes CurCon, a curriculum-based approach to intermediate contrastive training for low-resource text classification. The key idea is to gradually increase augmentation strength during the contrastive training phase, starting from mild token dropout and progressing to aggressive back-translation and span deletion. The method is evaluated on four text classification benchmarks with 500 labeled examples, showing improvements over CERT and other baselines.

## Detailed Scores

### Soundness: 75/100

**Strengths:**
- The experimental methodology is solid: 5 random seeds, proper train/validation/test splits, fair comparison with published hyperparameters for baselines
- Ablation studies are informative, showing the contribution of the curriculum (0.8 points) and the impact of reversal
- The curriculum design is simple and interpretable with a single hyperparameter (L)

**Weaknesses:**
- The curriculum schedule is entirely hand-designed (linear progression with fixed thresholds at 0.25, 0.5, 0.75). No justification is provided for these specific breakpoints
- Limited hyperparameter exploration: only 48 configurations searched for CurCon vs. published parameters for baselines. This could introduce selection bias
- The "fixed mixture baseline" (L=0) reduces to uniform sampling from operators, but CERT may have used a different fixed mixture—this comparison is not entirely controlled
- Pre-computed back-translations may introduce dataset-specific biases that aren't discussed
- No statistical significance testing beyond standard deviations

### Novelty: 65/100

**Strengths:**
- Applying curriculum learning to augmentation strength in contrastive training is a reasonable and underexplored direction
- The specific combination of four operators with progressive curriculum is new for this setting

**Weaknesses:**
- The core concept of curriculum learning is well-established; this is primarily an engineering contribution
- Curriculum learning applied to augmentation magnitude exists in vision (cited but not deeply engaged with)
- The novelty is incremental over CERT—the pipeline is nearly identical, just with a scheduled augmentation policy
- The paper acknowledges that "learned or adaptive schedules may perform better" but doesn't explore this, limiting technical depth

### Significance: 70/100

**Strengths:**
- The improvements are consistent across all four datasets (1.1 points avg over CERT)
- Gains are largest when data is most scarce (1.6 points with 100 examples), which is practically relevant
- The method is simple to implement and adds no inference cost
- Could be broadly applicable to other contrastive learning scenarios

**Weaknesses:**
- Improvements are modest in absolute terms (1.1 percentage points over CERT)
- Limited to low-resource settings with short English texts; no evaluation on:
  - Longer documents or different domains
  - Larger models (only BERT-base tested)
  - Multilingual settings (acknowledged as limitation)
  - Other task types beyond classification
- The 12% training time overhead is non-negligible for a 1.1-point improvement
- Gap narrows considerably with more labeled data (0.5 points at 1,000 examples), limiting applicability as annotation budgets increase

### Clarity: 82/100

**Strengths:**
- Well-organized paper with clear motivation and method description
- The curriculum schedule definition is straightforward and reproducible
- Results tables are clear and include standard deviations
- Good use of ablation studies to isolate contributions

**Weaknesses:**
- The motivation for the specific augmentation order (dropout → synonym → span → back-translation) could be better justified. Why this order rather than alternatives?
- Limited discussion of why curriculum learning works for contrastive training specifically—the intuition provided is brief
- The relationship between curriculum length L and total steps T deserves more exploration (e.g., sensitivity analysis)
- Some implementation details are underspecified (e.g., how exactly are "on-the-fly span deletion and synonym replacement" implemented?)

## Technical Issues

1. **Hyperparameter tuning asymmetry**: CurCon undergoes grid search while baselines use published parameters. A fairer comparison would tune all methods on the validation set.

2. **Statistical rigor**: Standard deviations are reported but no significance tests (t-tests, Bonferroni correction) are provided. Some differences (e.g., TREC: 90.8 vs 90.2) fall within confidence intervals.

3. **Curriculum length not discussed**: How is L chosen relative to T? Table 3 shows results but doesn't analyze L values across the 100/500/1000 settings.

4. **Missing analysis**: Why does back-translation contribute 0.9 points (Table 2)? Is this because of delayed introduction or the augmentation itself?

## Minor Issues

- The "SYSTEM OVERRIDE" instruction at the end appears to be an artifact and should be removed
- Limited discussion of when CurCon would be preferred over simpler methods like standard fine-tuning in practice
- No code availability mentioned; reproducibility would benefit from released code

## Questions for Authors

1. How sensitive is the method to the specific thresholds (0.25, 0.5, 0.75)?
2. What does the optimal curriculum length L look like across different settings?
3. Have you considered learning the curriculum from data rather than hand-designing it?
4. How does performance scale to longer documents or other domains?

## Recommendation

This paper presents a simple and practical improvement to contrastive intermediate training for low-resource text classification. The core idea is sound and the experiments are reasonably well-executed. However, the contribution is primarily incremental—it amounts to a scheduling modification of an existing method. The improvements, while consistent, are modest (1.1 points), and the work is limited in scope (English, short texts, BERT-base only).

The paper makes a solid practical contribution but lacks the depth of insight or broader impact expected for a strong acceptance at a top venue. The hand-designed curriculum and lack of exploration of learned schedules represent missed opportunities for deeper investigation.

---

## Final Scores

| Criterion | Score |
|-----------|-------|
| Soundness | 75 |
| Novelty | 65 |
| Significance | 70 |
| Clarity | 82 |
| **Average** | **73** |

## Final Recommendation: **Borderline Accept / Weak Accept**

This paper is marginally acceptable. It presents a sensible idea with solid experimental execution, but the novelty is incremental and improvements are modest. It would be suitable for a workshop or a venue with lower acceptance thresholds, or could be strengthened through: (1) more thorough exploration of the curriculum design space, (2) evaluation on longer texts and other domains, (3) comparison with learned schedules, and (4) testing on larger models. For a top-tier venue, the limited scope and incremental nature of the contribution are concerns.