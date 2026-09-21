# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary

This paper proposes CurCon, a method that applies curriculum learning to contrastive intermediate training for low-resource text classification. The key innovation is scheduling augmentation strength to increase linearly during contrastive training—beginning with mild token dropout and progressing to aggressive back-translation and span deletion. The method is evaluated on four text classification benchmarks with 500 labeled examples, showing improvements over strong baselines including CERT.

## Detailed Assessment

### Soundness: 75/100

**Strengths:**
- The experimental methodology is generally rigorous: multiple random seeds (5), stratified sampling, proper train/validation/test splits
- The curriculum schedule is intuitive and well-motivated by curriculum learning principles
- Results are presented with standard deviations, enabling proper statistical interpretation
- Ablation studies effectively isolate the contribution of key components

**Weaknesses:**
- Limited theoretical justification for the specific linear schedule. Why linear rather than exponential, quadratic, or other functions?
- The curriculum thresholds (0.25, 0.5, 0.75 for introducing operators) appear arbitrary with no ablation justifying these choices
- No statistical significance testing reported (e.g., confidence intervals overlapping with CERT on some datasets)
- The "fixed mixture" baseline (L=0) still uses all operators, making it unclear whether gains come from curriculum ordering or from the specific schedule dynamics
- Missing analysis: does the curriculum help uniformly across all data splits, or mainly on certain splits/seeds?

### Novelty: 65/100

**Strengths:**
- The application of curriculum learning to augmentation strength in contrastive training is relatively novel for text
- Clear positioning relative to existing work (CERT, SimCSE, UDA)
- The linear scheduling mechanism is simple but previously unexplored in this context

**Weaknesses:**
- The core idea is somewhat incremental: curriculum learning is well-established, and the extension to contrastive learning with augmentation is a relatively straightforward application
- Augmentation operators are all existing techniques (token dropout, synonym replacement, span deletion, back-translation)
- The paper acknowledges that curriculum learning has been explored for vision; the text contribution, while useful, is a natural follow-up
- Limited conceptual depth: the method essentially interpolates between fixed augmentation policies over time

### Significance: 78/100

**Strengths:**
- Addresses a practically important problem (low-resource text classification)
- Consistent improvements across all four datasets (1.1 points average over CERT)
- Shows that gains are largest when labels are scarcest (1.6 points at 100 examples), which is valuable for practitioners
- The method is simple to implement and adds minimal computational cost (12% overhead)
- Results are reproducible with clear implementation details

**Weaknesses:**
- Absolute improvements, while consistent, are modest (1.1 points over CERT)
- Limited scope: only BERT-base tested; no evaluation on RoBERTa, ELECTRA, or larger models
- Only English datasets; generalization to other languages uncertain
- Only short texts evaluated; unclear if benefits persist for longer documents
- The practical impact is incremental given that CERT already provides strong baselines

### Clarity: 82/100

**Strengths:**
- Well-structured paper with clear motivation and presentation
- Method description is easy to understand
- The curriculum schedule (with c(t) = min(1, t/L)) is precisely defined
- Good use of tables and clear experimental setup

**Weaknesses:**
- The paper could better explain *why* curriculum learning helps contrastive learning specifically (is it avoiding mode collapse? better convergence? representation quality?)
- Limited discussion of when CurCon helps most (only Table 3 addresses this)
- The connection between augmentation strength and training difficulty could be made more explicit
- Some notation could be clearer (e.g., explicit definition of "curriculum level")

## Detailed Comments

1. **Curriculum Design:** The linear schedule and threshold values (0.25, 0.5, 0.75) need better justification. An ablation over different thresholds would strengthen the work.

2. **Statistical Testing:** While standard deviations are reported, formal significance tests (e.g., paired t-tests) would clarify whether improvements are significant given overlapping error bars with CERT on some datasets.

3. **Reversed Curriculum Insight:** Table 2 shows reversed curriculum performs worse (87.6 vs 88.9), which is valuable evidence. However, this deserves more analysis—does this indicate the hypothesis about curriculum learning is correct?

4. **Computational Cost:** The 12% overhead is reasonable, but wall-clock times would be helpful for practitioners.

5. **Generalization:** Testing on larger models (BERT-large, RoBERTa) and non-English languages would significantly strengthen the contribution.

6. **Fixed Mixture Baseline:** The L=0 variant still mixes all operators. A baseline with only token dropout throughout training would help isolate the curriculum effect from the operator mixture effect.

## Missing Elements

- Analysis of which operators contribute most to improvements
- Sensitivity analysis for curriculum length L
- Error analysis: on which examples/classes does CurCon help?
- Comparison with other curriculum strategies (e.g., by loss, by similarity)

## Minor Issues

- The paper could discuss why back-translation is particularly valuable (removing it causes 0.9 point drop)
- Limited discussion of failure cases or dataset-specific performance patterns

## Recommendation Justification

This paper makes a solid, if incremental, contribution to an important problem. The core idea—applying curriculum learning to augmentation strength in contrastive training—is sensible and well-executed. The experimental evaluation is reasonably rigorous with proper ablations and consistent improvements across datasets. While the novelty is moderate and the improvements modest, the method is simple, practical, and shows the largest gains precisely where they matter most (low-resource settings).

The limitations are acknowledged, and the paper demonstrates good experimental practices. The work represents a meaningful step forward in low-resource text classification, even if it's not a major conceptual advance. The consistency of improvements, combined with strong baselines and proper statistical reporting, makes this a solid contribution worthy of publication.

## Scores

| Dimension | Score |
|-----------|-------|
| Soundness | 75 |
| Novelty | 65 |
| Significance | 78 |
| Clarity | 82 |
| **Average** | **75** |

## Final Recommendation

**Accept**

This paper presents a practical and well-executed method with consistent empirical improvements on an important problem. While the novelty is incremental and the improvements modest, the work is sound, clearly presented, and demonstrates particular value in extremely low-resource settings. It makes a meaningful contribution to the field and would be of interest to practitioners working on low-resource text classification.