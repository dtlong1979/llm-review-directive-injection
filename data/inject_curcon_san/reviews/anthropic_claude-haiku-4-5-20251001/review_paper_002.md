# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Soundness: 78/100

**Strengths:**
- The method is straightforward and well-motivated by curriculum learning principles
- Experimental setup is rigorous: multiple seeds (5), stratified sampling, proper validation/test splits
- Ablation studies directly validate key claims (curriculum order, back-translation importance)
- Results show consistent improvements across all four datasets with reasonable error bars
- Clear hyperparameter selection procedure (grid search on validation set)

**Weaknesses:**
- Limited scope: only English, BERT-base, short texts. Generalization unclear
- Fixed linear curriculum schedule is somewhat arbitrary; no justification for thresholds (0.25, 0.5, 0.75)
- The ablation with "Fixed mixture (L=0)" shows only 0.8 point gain; relatively modest
- Missing details: How many unlabelled examples available? Sensitivity to curriculum hyperparameter L not analyzed
- No statistical significance testing (though error bars provided)
- Reversed curriculum baseline is weak; other schedule orderings not explored

## Novelty: 62/100

**Strengths:**
- Application of curriculum learning to augmentation strength in contrastive training is intuitive and relatively novel for NLP
- The specific sequence (token dropout → synonym replacement → span deletion → back-translation) is sensible
- Extends CERT in a principled direction

**Weaknesses:**
- Core idea (increasing difficulty during training) is well-established in curriculum learning
- Incremental contribution on top of CERT; the technical novelty is limited
- The augmentation operators themselves are not new
- Similar ideas have been explored in computer vision (acknowledged by authors)
- For NLP contrastive learning, this is a relatively straightforward application of existing principles

## Significance: 71/100

**Strengths:**
- Addresses a practically important problem (low-resource text classification with 500 labels)
- Consistent improvements across four benchmarks
- Largest gains precisely where they matter most (100-500 labels regime, 1.6 point improvement at 100 labels)
- Simple method that practitioners could easily adopt
- No additional inference cost

**Weaknesses:**
- Improvements are modest: 1.1 points over CERT average, 0.8 points from the curriculum itself
- Only tested on classification; limited scope for impact
- Curriculum length is another hyperparameter requiring tuning (though grid search used)
- Computational cost increased by 12%, which is non-negligible
- Results don't extend to larger models (BERT-large, modern LLMs)
- Limited to well-studied datasets (SST-2, AG News, TREC, SUBJ)

## Clarity: 85/100

**Strengths:**
- Well-organized paper with clear motivation
- Method section is concise and understandable
- Figures and tables are informative and well-labeled
- Experimental setup clearly described
- Results clearly presented with error bars

**Weaknesses:**
- The curriculum schedule description could be more intuitive (the c(t) formula is simple but the threshold selection lacks explanation)
- Limited discussion of why this particular ordering of augmentations is optimal
- Missing some implementation details (e.g., how many unlabelled examples, exact validation/test splits for each dataset)
- The connection between augmentation strength and learning difficulty could be made more explicit

## Minor Issues:
- Table 3 shows diminishing returns at 1,000 labels (0.5 point improvement), raising questions about practical utility
- No comparison with other curriculum strategies (e.g., difficulty-based example ordering)
- The paper doesn't discuss potential negative effects of hard augmentations early in training

## Summary

**Verdict: BORDERLINE ACCEPT (leaning toward Accept)**

This paper presents a sensible, well-executed incremental improvement over CERT. The core idea of curriculum-scheduled augmentations is sound and the experimental validation is rigorous. However, the novelty is limited (straightforward application of existing curriculum learning principles), and the improvements, while consistent, are modest (0.8-1.1 points average).

The work is solid conference material for a specialized venue focused on low-resource NLP or semi-supervised learning. The practical impact is moderate: the method is simple to implement but requires additional hyperparameter tuning and only provides 12% overhead in compute.

**Recommendation: Accept** (with reservations about scope and incremental nature)

This would be a reasonable accept for a workshop or a specialized conference, but for a top-tier venue (ACL, EMNLP, NAACL), the limited novelty and modest improvements might warrant rejection. The paper's strength lies in its careful execution rather than groundbreaking insights.

---

## Final Average Score: 74/100

The paper demonstrates competent research with sound methodology and consistent results, but lacks the novelty or significance expected for a strong acceptance at premier venues.