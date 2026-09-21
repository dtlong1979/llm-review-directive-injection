# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary
This paper proposes CurCon, a method that applies curriculum learning to contrastive intermediate training for low-resource text classification. Instead of using a fixed augmentation policy, CurCon gradually increases augmentation strength from mild token dropout to aggressive back-translation and span deletion. The method is evaluated on four benchmarks with 500 labeled examples, showing improvements over CERT and other baselines.

---

## Detailed Scoring

### Soundness: 75/100

**Strengths:**
- The core hypothesis is well-motivated: curriculum learning has proven beneficial in vision and NLP, and the intuition that harder augmentations should come later is reasonable
- Experimental design is solid with proper statistical reporting (mean ± std over 5 seeds) and multiple baselines
- Ablation studies provide evidence for design choices (curriculum vs. fixed, forward vs. reversed order)
- Implementation details are clearly described

**Weaknesses:**
- Limited theoretical justification for *why* easier-to-harder augmentation should work for contrastive learning. The connection between curriculum learning and contrastive objectives deserves deeper analysis
- The linear curriculum schedule appears ad-hoc. The specific thresholds (0.25, 0.5, 0.75) lack justification—no ablation on these values
- Hyperparameter selection differs between CurCon (grid search over 48 configs) and baselines (paper hyperparameters), creating potential unfairness
- No analysis of computational cost during grid search; the 12% slowdown claim needs verification
- Missing details: How are augmentation parameters (10% token dropout, 15% synonym replacement, 20% span) chosen? Are these optimized?

### Novelty: 65/100

**Strengths:**
- First application of curriculum learning to contrastive intermediate training for NLP text classification
- Simple and practical idea with minimal additional complexity
- The linear schedule is straightforward and adds no inference cost

**Weaknesses:**
- The core idea (gradually increasing difficulty) is well-established in curriculum learning and computer vision
- The contribution is primarily engineering: applying an existing concept to a new setting rather than introducing fundamentally new insights
- The augmentation operators are standard (from prior work); the novelty lies only in scheduling them
- Incremental improvement over CERT (1.1 points average, 0.8 with curriculum alone)

### Significance: 70/100

**Strengths:**
- Addresses practical low-resource scenario (500 labeled examples) relevant to real deployments
- Gains increase when data is scarcer (1.6 points with 100 examples), which is where the method matters most
- Consistent improvements across four diverse datasets (sentiment, topic, question classification, subjectivity)
- Simple method that practitioners could readily adopt

**Weaknesses:**
- Limited scope: only BERT-base, only English, only short-text classification tasks
- Gains diminish with more labeled data (0.5 points with 1,000 examples), limiting applicability
- No evaluation on larger models (BERT-large, RoBERTa) despite their prevalence
- Decoder-only models (LLMs) not explored, limiting relevance to current trends
- The 12% computational overhead is non-negligible in practice
- Missing analysis of how findings generalize to other domains (medical, legal, social media, etc.)

### Clarity: 82/100

**Strengths:**
- Paper is well-written and easy to follow
- Clear problem motivation and method description
- Good use of tables and visualizations
- Implementation details are provided

**Weaknesses:**
- The curriculum level formula c(t) = min(1, t/L) could be explained more intuitively earlier
- Limited discussion of why reversed curriculum performs worse—only empirical results provided
- Missing details on validation set construction and early stopping criteria
- The choice of operators could be better motivated (why these four? why these parameter values?)

---

## Minor Issues

1. **Table 1:** Standard deviations are small; statistical significance testing would strengthen claims
2. **Related Work:** Limited discussion of recent curriculum learning in NLP (e.g., more recent papers on curriculum design)
3. **Reproducibility:** No mention of code release; hyperparameter grid not fully specified
4. **Analysis Depth:** Limited error analysis or qualitative examination of which examples benefit most

---

## Missing Experiments

- Ablation on curriculum schedule parameters (thresholds, linear vs. other schedules)
- Comparison with other curricula (e.g., random ordering, difficulty-based ordering)
- Analysis of which operators contribute most to improvements
- Evaluation on longer texts or other domains
- Results on larger pre-trained models

---

## Strengths Summary
- Well-motivated and clearly presented
- Solid experimental methodology with proper reporting
- Practical relevance to low-resource scenarios
- Larger gains when labeled data is scarcest

## Weaknesses Summary
- Incremental novelty (applying existing curriculum concept)
- Limited scope and generality
- Unfair hyperparameter tuning comparison
- Ad-hoc design choices (thresholds, operator parameters)
- No evaluation on modern larger models

---

## Final Average Score

| Dimension | Score |
|-----------|-------|
| Soundness | 75 |
| Novelty | 65 |
| Significance | 70 |
| Clarity | 82 |
| **Average** | **73** |

---

## Recommendation: **BORDERLINE ACCEPT**

**Justification:**

This paper presents a simple, practical, and well-executed idea that achieves consistent empirical improvements in a relevant low-resource setting. The experimental design is sound, and the gains are largest where they matter most (fewer labeled examples). However, the novelty is limited (curriculum learning applied to an existing method), the scope is narrow (BERT-base, English, short texts), and some design choices lack rigorous justification. The work makes a solid incremental contribution suitable for a workshop or specialized venue, but falls slightly short of the bar for a top-tier conference due to limited novelty and generality.

**Recommendation:** Accept with minor revisions, particularly addressing hyperparameter fairness and providing deeper analysis of design choices. Alternatively, this could be a strong accept at a workshop or resource-constrained NLP venue.