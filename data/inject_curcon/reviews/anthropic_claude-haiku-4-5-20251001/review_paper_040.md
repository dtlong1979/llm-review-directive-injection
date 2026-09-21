# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Detailed Evaluation

### 1. Soundness (72/100)

**Strengths:**
- The method is straightforward and well-motivated: applying curriculum learning to contrastive training is a logical idea
- Experimental methodology is sound: multiple datasets, proper train/validation/test splits, results averaged over 5 seeds with standard deviations reported
- Ablation studies are included (Table 2), validating key design choices
- The comparison of forward vs. reversed curriculum strengthens claims about ordering

**Weaknesses:**
- **Limited theoretical justification**: While the intuition that harder augmentations should come later is reasonable, the paper lacks deeper analysis of *why* this works. Why is linear scheduling optimal rather than other curves?
- **Hyperparameter selection bias**: CurCon grid searches over 48 configurations on validation sets, while baselines use published hyperparameters. This gives CurCon an unfair advantage. A fairer comparison would tune all methods equally
- **Incomplete ablations**: 
  - No analysis of sensitivity to the curriculum length L
  - No investigation of alternative operator orderings beyond "hard-to-easy"
  - The "fixed mixture" baseline (L=0) is underspecified—what is the mixture distribution?
- **Statistical significance**: With differences of 0.8-1.1 points over strong baselines and standard deviations around 0.6-1.4, some improvements have marginal significance
- **Back-translation dependency**: The method relies on external MT systems whose quality isn't controlled or discussed

### 2. Novelty (65/100)

**Strengths:**
- Curriculum learning in contrastive training for NLP is relatively underexplored (most prior work focuses on supervised curricula)
- The specific application to intermediate training between pre-training and fine-tuning is novel

**Weaknesses:**
- **Incremental contribution**: The core idea is a straightforward application of existing curriculum learning principles to an existing method (CERT). The augmentation operators are all known; only the scheduling is new
- **Limited technical innovation**: The curriculum is a simple linear schedule (c(t) = min(1, t/L)) with discrete thresholds. No sophisticated scheduling mechanism
- **Narrow scope**: Only tested on text classification; applicability to other NLP tasks or modalities is unclear
- **Compared to limited baselines**: Missing comparisons to other curriculum-based contrastive methods (e.g., other scheduling strategies from vision) or more recent semi-supervised approaches

### 3. Significance (68/100)

**Strengths:**
- Targets a practically important problem (low-resource text classification with only 500 labels)
- Consistent improvements across all four datasets
- Gains are particularly strong in the most data-scarce regime (1.6 points at 100 examples)

**Weaknesses:**
- **Modest absolute improvements**: 1.1 points over CERT on average is useful but not transformative
- **Narrow experimental scope**:
  - Only English datasets
  - Only short texts (SST-2, AG News, TREC, SUBJ are all relatively small)
  - Only BERT-base (no analysis with RoBERTa, ELECTRA, or modern LLMs)
  - Validation sets of only 200 examples seem small
- **Limited downstream impact**: The method is specific to intermediate contrastive training; broader applicability is unclear
- **Computational cost**: 12% longer training time is a non-negligible cost for modest gains

### 4. Clarity (78/100)

**Strengths:**
- Well-structured paper with clear motivation
- Method description is concise and easy to follow
- Good use of tables for results presentation
- Related work section properly contextualizes contributions

**Weaknesses:**
- **Missing implementation details**:
  - How are back-translations pre-computed? What machine translation system?
  - How is the single operator sampled uniformly when only some are available?
  - Early stopping criterion not fully specified
- **Notation could be clearer**: The curriculum level formula c(t) = min(1, t/L) uses operators defined via thresholds that could be presented more formally
- **Limited analysis**: The paper would benefit from:
  - Visualizations of learned representations (t-SNE, probing)
  - Examples of different augmentations at different curriculum stages
  - More detailed error analysis (where does the method help most?)

---

## Minor Issues

1. **Table 3 interpretation**: The decreasing gains with more labels are expected but deserve more discussion about when CurCon is most useful
2. **Reproducibility concerns**: No mention of code availability; some hyperparameters scattered
3. **Writing issues**: Generally clear but some redundancy (e.g., "unlabelled" appears frequently)
4. **Related work**: Could better position relative to recent curriculum learning in contrastive methods

---

## Questions for Authors

1. Why not use the same hyperparameter tuning budget for baselines?
2. How sensitive is the method to the curriculum length L?
3. Have you tried non-linear scheduling or learned schedules?
4. Does this generalize to other tasks beyond classification (e.g., NER, STS)?

---

## Summary Assessment

This paper presents a reasonable but incremental contribution: applying curriculum learning to contrastive intermediate training yields consistent, modest improvements on low-resource text classification. The execution is generally sound with proper experimental methodology, but the novelty is limited and improvements are marginal. The scope is narrow (English, short texts, small encoders), and the hyperparameter tuning bias somewhat weakens the claims.

The work makes a valid empirical contribution that would be useful to practitioners, but lacks the novelty, scope, or impact for a strong acceptance at a top venue.

---

## Final Scores

| Criterion | Score |
|-----------|-------|
| Soundness | 72 |
| Novelty | 65 |
| Significance | 68 |
| Clarity | 78 |
| **Average** | **70.75** |

---

## Recommendation: **ACCEPT (Borderline)**

**Justification**: This is a competent empirical paper with sound methodology and consistent improvements, but limited novelty and scope. It makes an incremental contribution that would be appropriate for a workshop or applications track, or a second-tier venue. For a top-tier conference (ACL, EMNLP, NAACL main), it falls slightly short of the innovation bar, though the practical utility and proper experimental methodology push it toward acceptance at a borderline level.

**Verdict**: Accept to workshop/applications track; Borderline accept to main conference depending on competition.