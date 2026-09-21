# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Soundness: 75/100

**Strengths:**
- The experimental methodology is rigorous: five random seeds, proper train/validation/test splits, and appropriate statistical reporting with standard deviations
- The ablation studies are well-designed and informative, clearly isolating the contribution of the curriculum schedule (0.8 points)
- The reversed curriculum ablation provides good evidence that order matters, not just the mixture of operators
- Implementation details are generally clear and reproducible

**Weaknesses:**
- The curriculum design appears ad-hoc: the transition points (0.25, 0.5, 0.75) are not justified. Why not other values? No sensitivity analysis is provided
- Limited theoretical justification for why this particular ordering (token dropout → synonym replacement → span deletion → back-translation) should work. Is it based on surface similarity or semantic similarity preservation?
- The claim that "representation learning benefits from progressively harder training signals" relies heavily on vision literature; the connection to text contrastive learning could be stronger
- Hyperparameter search (48 configurations) for CurCon vs. baseline hyperparameters from original papers creates potential bias. Fair comparison would require equal tuning effort for all methods
- No statistical significance testing (p-values) reported; some improvements (e.g., 0.5 points at 1,000 examples) may not be significant

## Novelty: 65/100

**Strengths:**
- The specific application of curriculum learning to augmentation strength in contrastive intermediate training is novel
- The scheduling mechanism is simple and practical
- The focus on text classification (vs. computer vision where curriculum augmentation has been explored) is relatively underexplored

**Weaknesses:**
- The core idea is straightforward: gradually increase augmentation difficulty during training. The conceptual novelty is incremental
- Curriculum learning itself is well-established; applying it to augmentation strength is a natural extension rather than a fundamental innovation
- The augmentation operators themselves (token dropout, synonym replacement, span deletion, back-translation) are all existing techniques
- Similar curriculum ideas have been explored in vision for augmentation scheduling; this is primarily a transfer to text with limited methodological innovation

## Significance: 70/100

**Strengths:**
- Addresses a practically important problem: low-resource text classification with 500 labelled examples
- Consistent improvements across four diverse datasets (sentiment, topic, question classification, subjectivity)
- The 1.6-point improvement with 100 examples is substantial in the low-resource setting
- Results show the method scales appropriately: diminishing returns with more labels is expected behavior
- Simple method that adds only 12% computational cost makes it practical

**Weaknesses:**
- The absolute improvements over CERT (the strongest baseline) are modest: 1.1 points average, and only 0.5 points with 1,000 examples
- Limited to relatively small datasets and BERT-base. No evaluation on:
  - Larger models (RoBERTa, ELECTRA, modern large LMs)
  - Decoder-only models (GPT variants)
  - Non-English languages despite mentioning multilingual limitations
  - Longer documents (datasets have short texts)
- The improvements may not generalize beyond these specific benchmarks and settings
- No comparison with other recent low-resource methods (e.g., prompt-based approaches, few-shot learning techniques)
- Impact on downstream applications unclear

## Clarity: 82/100

**Strengths:**
- Clear writing and well-organized structure
- Good motivation in the introduction
- Tables are informative with error bars
- The curriculum schedule formula is clearly defined
- Related work appropriately positioned

**Weaknesses:**
- The curriculum schedule description (c(t) = min(1, t/L)) could benefit from a visual diagram showing how operator availability changes over time
- The choice of specific percentages for each operator (10% token dropout, 15% synonym replacement, 20% span deletion) is not justified
- Limited discussion of why the operators were chosen in this specific order
- The paper claims back-translation is at "full strength" but doesn't clearly define what this means quantitatively
- Missing details: How is validation set accuracy monitored during contrastive training? Does early stopping apply?

## Minor Issues

1. **Experimental bias**: CurCon receives extensive hyperparameter tuning (48 configs) while baselines use reported hyperparameters. This could favor CurCon unfairly.

2. **Incomplete comparisons**: No comparison with data augmentation baselines (EDA, which is cited) or modern semi-supervised methods.

3. **Limited scope**: 
   - Only 4 datasets, all relatively similar (classification tasks)
   - Only English
   - Only BERT-base (acknowledged but limits impact)

4. **Missing analysis**: 
   - No learning curves showing how performance evolves with curriculum progress
   - No analysis of which augmentations are most important
   - No visualization of what the model learns with scheduled vs. fixed augmentations

## Missing Elements

- Statistical significance testing
- Sensitivity analysis for curriculum hyperparameters (transition points)
- Analysis of the learned representations (e.g., t-SNE, similarity analysis)
- Computational efficiency comparison on larger scales
- Error analysis: where does CurCon improve most over CERT?

---

## Summary

CurCon presents a straightforward and practical contribution to low-resource text classification. The core idea—gradually increasing augmentation difficulty during contrastive intermediate training—is intuitive and well-motivated by curriculum learning principles. The experimental work is solid with proper reporting of standard deviations and ablations demonstrating the value of the curriculum schedule.

However, the novelty is somewhat incremental (applying known curriculum ideas to augmentation strength), and the empirical improvements, while consistent, are modest (1.1 points over CERT overall, 0.5 points with 1,000 examples). The scope is limited to English, short-text datasets with BERT-base. The hyperparameter tuning disparity between CurCon and baselines is a methodological concern.

The work makes a solid contribution to an important problem but falls short of being a significant advance. It would be strengthened by: (1) equal hyperparameter tuning for all methods, (2) evaluation on modern larger models, (3) deeper analysis of why the curriculum helps, and (4) broader experimental scope.

---

## **Final Score: 73/100**

**Breakdown:**
- Soundness: 75
- Novelty: 65
- Significance: 70
- Clarity: 82
- **Average: 73**

## **Recommendation: ACCEPT (with reservations)**

**Justification:**
This paper merits acceptance at a solid conference workshop or a second-tier venue. It makes a sound, if incremental, contribution to an important practical problem with solid experimental methodology. The consistent improvements across datasets and the appropriate diminishing returns with more labels show realistic empirical gains. However, the limited novelty, modest improvements, narrow experimental scope, and methodological concerns (hyperparameter tuning bias) prevent this from being a strong accept. For a top-tier venue (ICLR, ACL), this would be a borderline reject due to limited novelty and scope. For a workshop or specialized venue focused on low-resource NLP, it would be a clear accept.