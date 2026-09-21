# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary

This paper proposes CurCon, a curriculum learning approach that schedules augmentation strength during contrastive intermediate training for low-resource text classification. Rather than using a fixed set of augmentations throughout training, CurCon gradually progresses from mild token dropout to aggressive back-translation and span deletion. Experiments on four benchmarks with 500 labelled examples show consistent improvements over strong baselines including CERT.

## Detailed Scores

### Soundness: 78/100

**Strengths:**
- The experimental design is rigorous: multiple datasets, five random seeds, proper train/validation/test splits with stratified sampling
- Statistical reporting includes standard deviations, enabling assessment of significance
- The ablation studies effectively validate design choices, particularly demonstrating that curriculum order matters (reversed curriculum hurts performance)
- The curriculum formulation is simple and interpretable: a single hyperparameter (L) controls progression through operators

**Weaknesses:**
- The hyperparameter search space (48 configurations) is relatively large for a curriculum method that claims to simplify training. No analysis of sensitivity to curriculum length or other hyperparameters is provided
- The claim about "progressively harder training signals" lacks theoretical justification or empirical analysis of what makes operators "harder." Token dropout may not be strictly easier than WordNet-based synonym replacement
- The pre-computation of back-translations is mentioned but not detailed. It's unclear whether this affects the fairness of comparison with CERT
- Missing analysis: no investigation of what the model actually learns at different curriculum stages, or validation that the learned representations indeed benefit from the schedule
- The 12% computational overhead is mentioned but not deeply analyzed—impact on practical applicability is unclear

### Novelty: 72/100

**Strengths:**
- The application of curriculum learning to augmentation scheduling in contrastive intermediate training is novel and well-motivated
- The specific combination of four operators (token dropout → synonym replacement → span deletion → back-translation) appears original
- The method is simple enough to be broadly applicable, yet addresses a real limitation of CERT

**Weaknesses:**
- Curriculum learning itself is well-established; the contribution is primarily engineering one curriculum schedule
- The operators are largely drawn from existing work (EDA, back-translation, SimCSE)
- The linear curriculum schedule is acknowledged as "hand-designed" without exploration of alternatives
- Limited conceptual depth: the paper is incremental over CERT rather than introducing fundamentally new ideas about representation learning or curriculum design

### Significance: 75/100

**Strengths:**
- Addresses a practically important problem: text classification with very limited labels (500 examples) is common in industry
- Improvements are consistent across all four benchmarks (+1.1 over CERT average)
- The method is model-agnostic and adds no inference cost
- Demonstrates that gains are largest in the most resource-constrained regime (1.6 points at 100 examples vs. 0.5 at 1,000)

**Weaknesses:**
- Absolute improvements, while consistent, are modest: +1.1 points over CERT and +3.8 over naive fine-tuning
- Limited scope: only four English benchmarks with relatively short texts; no exploration of longer documents or non-English datasets
- Restricted to BERT-base; unclear whether findings generalize to larger models (RoBERTa, ELECTRA) or decoder-only architectures (GPT-2/3)
- The practical impact is somewhat limited given the 12% computational overhead and complexity of hyperparameter selection
- Incremental improvement: CERT already substantially closes the gap between fine-tuning (85.1) and CurCon (88.9)

### Clarity: 82/100

**Strengths:**
- Clear, well-organized presentation with appropriate use of figures and tables
- The curriculum schedule is explained with precise mathematical formulation
- Related work section properly contextualizes the contribution
- Experimental setup is thoroughly documented

**Weaknesses:**
- The motivation for why curriculum learning should help contrastive learning could be more developed
- Limited intuitive explanation of why this particular progression of augmentations works well
- The connection between augmentation strength and training difficulty could be made more explicit
- Would benefit from visualizations or analysis of learned representations at different curriculum stages

## Detailed Comments

1. **Method Design**: The choice of four specific operators and the curriculum thresholds (0.25, 0.5, 0.75) appear somewhat arbitrary. Were these selected empirically, or is there principled reasoning? A sensitivity analysis would strengthen the contribution.

2. **Experimental Design**: The grid search over 48 configurations specifically for CurCon while baselines use published hyperparameters may introduce bias. Did you attempt to tune baselines similarly?

3. **Statistical Significance**: While standard deviations are reported, formal significance tests (e.g., paired t-tests) between CurCon and CERT would clarify whether improvements are statistically reliable, particularly on TREC where the difference is small.

4. **Missing Ablations**: 
   - What if you use a different operator order? 
   - How sensitive is performance to the specific thresholds (0.25, 0.5, 0.75)?
   - How does curriculum length L affect results across datasets?

5. **Generalization**: The acknowledgment that experiments are limited to BERT-base and English datasets is appropriate but concerning. Brief experiments with one additional encoder (e.g., RoBERTa) would strengthen claims.

6. **Computational Cost**: The 12% overhead is mentioned but not contextualized. For a method advocating curriculum learning's simplicity, this is notable.

## Minor Issues

- Table 3 shows diminishing returns with more labels, which is intuitive but worth emphasizing in the narrative
- The related work section could better position curriculum learning for contrastive objectives specifically
- Some notation could be clearer (e.g., explicitly defining how operators are sampled when multiple are available)

## Questions for Authors

1. Did you investigate learned curricula or only fixed schedules?
2. How do results change if you vary the thresholds (0.25, 0.5, 0.75)?
3. Can you provide visualizations of representation changes across curriculum stages?
4. How do results differ with other pre-trained encoders?

## Overall Assessment

This paper makes a solid, well-executed contribution to low-resource text classification. The core idea—scheduling augmentation strength during contrastive training—is intuitive and empirically validated. The experiments are rigorous with appropriate statistical reporting, and the improvements are consistent if modest. The method's simplicity and model-agnostic nature are valuable.

However, the novelty is primarily engineering-focused rather than conceptual, and the scope is somewhat limited (English, BERT-base, short texts only). The improvements, while consistent, are incremental rather than transformative. The paper would be strengthened by deeper analysis of why the curriculum helps, broader experimental validation, and exploration of adaptive scheduling.

Despite these limitations, the paper represents competent research addressing a practical problem with a simple, effective method. The ablations validate design choices, and the writing is clear. The work would be a reasonable addition to a venue's program, particularly given the strong empirical results across multiple datasets.

---

## Scores Summary

| Dimension | Score |
|-----------|-------|
| Soundness | 78 |
| Novelty | 72 |
| Significance | 75 |
| Clarity | 82 |
| **Average** | **76.75** |

## Recommendation: **ACCEPT**

This paper merits acceptance. It presents a straightforward but effective method with rigorous experimental validation, consistent improvements over strong baselines, and practical value for the low-resource setting. While not groundbreaking, it makes a solid contribution that advances the field incrementally. The ablations convincingly support the proposed approach, and the writing is clear. The limitations are acknowledged honestly, and the scope, while not exhaustive, is appropriate for the contribution level. This work represents the kind of focused, well-executed research that conferences should publish.