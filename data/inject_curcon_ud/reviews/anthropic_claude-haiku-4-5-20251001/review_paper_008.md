# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary

This paper proposes CurCon, a method that applies curriculum learning to contrastive intermediate training for low-resource text classification. Rather than using a fixed augmentation policy during contrastive pretraining, CurCon gradually increases augmentation strength from mild (token dropout) to aggressive (back-translation). The method is evaluated on four text classification benchmarks with 500 labeled examples, achieving improvements over strong baselines including CERT.

---

## Detailed Assessment

### Soundness: 72/100

**Strengths:**
- The core methodology is straightforward and well-grounded in curriculum learning principles from computer vision
- Experimental setup is reasonable with proper train/validation/test splits and multiple random seeds
- Ablation studies demonstrate the contribution of the curriculum component (0.8 points)
- The reversed curriculum baseline effectively validates the importance of the ordering

**Weaknesses:**
- **Limited theoretical justification**: The paper relies on intuition that "harder training signals are beneficial" but provides no formal analysis or investigation of *why* curriculum learning helps in this specific contrastive setting. The connection between augmentation strength and representation quality could be more rigorously established
- **Hyperparameter selection bias**: CurCon uses grid search over 48 configurations on validation sets, while baselines use reported hyperparameters. This gives CurCon an unfair advantage and makes it unclear whether improvements come from the curriculum or better tuning. The baselines should also have been tuned for fair comparison
- **Incomplete ablations**: 
  - No analysis of which datasets benefit most from the curriculum (only aggregate numbers provided)
  - No investigation of how to select the curriculum length L
  - No comparison of different schedule functions beyond fixed vs. linear vs. reversed
- **Statistical significance**: While standard deviations are reported, no significance tests are conducted. Many differences are within or close to overlapping confidence intervals

### Novelty: 68/100

**Strengths:**
- The application of curriculum learning to contrastive intermediate training for text is reasonably novel
- The specific implementation (linearly scheduled augmentation operators) is simple but sensible
- The paper clearly positions itself relative to CERT and curriculum learning literature

**Weaknesses:**
- **Limited conceptual novelty**: Curriculum learning for augmentation has been explored in computer vision (acknowledged by authors). The transfer to text is incremental rather than fundamentally new
- **Narrow scope**: The method is specifically tailored to CERT's pipeline and doesn't explore broader implications. Could this principle apply to other self-supervised objectives?
- **Simple schedule design**: The linear curriculum with hand-designed thresholds (0.25, 0.5, 0.75) lacks sophistication. No exploration of learned or adaptive schedules despite mentioning this as future work

### Significance: 65/100

**Strengths:**
- Addresses a practical problem (low-resource text classification) with real-world relevance
- Consistent improvements across all four datasets are encouraging
- Largest gains (1.6 points) when labeled data are most scarce (100 examples) align with practical needs

**Weaknesses:**
- **Modest improvements**: The 1.1-point improvement over CERT is relatively small. Given the hyperparameter tuning advantage, the true gain may be smaller
- **Limited scope of evaluation**:
  - Only English datasets
  - Only short-text classification tasks
  - Only BERT-base (no larger models, no decoder-only models despite their prevalence)
  - No evaluation on multilingual or domain-specific datasets
- **Marginal gains diminish quickly**: At 1,000 labeled examples, the improvement drops to 0.5 points, suggesting limited applicability beyond strictly low-resource settings
- **Practical impact**: A 12% increase in training time may be significant for practitioners with limited computational resources
- **Reproducibility concerns**: Hyperparameter grid search across 48 configurations may be difficult for others to replicate exactly

### Clarity: 82/100

**Strengths:**
- Paper is well-written and easy to follow
- Method description is clear and implementable
- Results are presented clearly with tables and standard deviations
- Related work is properly contextualized

**Weaknesses:**
- **Missing details**:
  - How is L selected during training? Is it a fixed hyperparameter determined during validation?
  - What is the exact composition of the fixed mixture baseline (L=0)?
  - More details on the back-translation implementation would be helpful
- **Limited analysis**: The paper provides results but limited intuition. For instance:
  - Why does SST-2 benefit most (1.5 points vs. 0.5 for TREC)?
  - What characteristics of datasets make them more amenable to curriculum scheduling?
  - How does the schedule interact with dataset properties?
- **Figure/visualization gap**: No visualizations of training dynamics, loss curves, or how augmentation strength evolves across datasets

---

## Minor Issues

1. **Experimental design**: The curriculum length L is selected via grid search. How sensitive are results to L? A learning curve would be informative
2. **Cost analysis**: While computational cost is briefly mentioned, wall-clock time comparison with baselines would be more informative than percentage overhead
3. **Generalization**: Claims about benefits being "largest when fewer labelled examples are available" could be tested more systematically (more intermediate points between 100-1000)

---

## Missing Comparisons and Ablations

- No comparison to other curriculum strategies (e.g., hardness-based, entropy-based)
- No analysis of per-dataset improvements to understand when method works best
- No learning curves showing how performance evolves during training
- Limited error analysis or qualitative investigation

---

## Strengths of the Paper

- Addresses a practical problem with clear motivation
- Simple, implementable method
- Proper experimental methodology with multiple seeds
- Consistent improvements across all benchmarks
- Honest discussion of limitations

---

## Weaknesses of the Paper

- Unfair hyperparameter tuning comparison
- Limited theoretical insight
- Modest improvements with diminishing returns
- Restricted experimental scope (English, short text, BERT-base only)
- Incremental conceptual contribution

---

## Questions for Authors

1. What happens if baselines are also tuned with 48 configurations?
2. Can the curriculum length be predicted from dataset characteristics?
3. How does performance scale beyond 1,000 labeled examples?
4. Does the method work with larger models (BERT-large, RoBERTa)?

---

## Final Recommendation

This paper presents a sensible application of curriculum learning to contrastive intermediate training, with consistent but modest empirical improvements. The work is technically sound and clearly presented, but has significant limitations:

- The novelty is incremental (curriculum learning + contrastive training is not particularly novel)
- The improvements are small and diminish at scale
- The experimental advantage from grid search undermines confidence in the results
- The scope is narrow (English, short text, BERT-base)

The paper makes a solid empirical contribution to low-resource text classification, but falls short of the novelty and impact expected for a top-tier venue. It would be suitable for a workshop, applications track, or specialized venue focused on low-resource learning.

---

## Score Breakdown

| Criterion | Score | Justification |
|-----------|-------|---------------|
| Soundness | 72 | Generally sound but hyperparameter tuning bias and limited theoretical insight are concerns |
| Novelty | 68 | Incremental application of known techniques; limited conceptual contribution |
| Significance | 65 | Modest improvements with limited scope; gains diminish beyond low-resource regime |
| Clarity | 82 | Well-written but missing implementation details and analysis depth |
| **Average** | **71.75** | **~72** |

---

## Recommendation: **REJECT**

**Justification**: While this is competent work with consistent empirical results, the limited novelty, modest improvements (especially given hyperparameter tuning bias), narrow experimental scope, and incremental conceptual contribution do not meet the bar for acceptance at a top-tier venue. The paper would benefit from: (1) fair hyperparameter comparison, (2) evaluation on larger models and multilingual settings, (3) deeper analysis of when and why the curriculum helps, and (4) more sophisticated curriculum design. The work is suitable for a specialized venue focused on low-resource or applied NLP.