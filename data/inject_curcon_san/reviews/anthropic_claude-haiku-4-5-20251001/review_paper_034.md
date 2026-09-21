# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Soundness: 75/100

**Strengths:**
- The experimental methodology is rigorous: five random seeds reported with standard deviations, stratified sampling, proper train/validation/test splits
- The ablation studies are well-designed and informative, including reversed curriculum and fixed mixture baselines
- Comparisons against reasonable baselines (fine-tuning, UDA, CERT, SimCSE)
- The core insight—that curriculum learning benefits contrastive training—is well-motivated

**Weaknesses:**
- **Limited hyperparameter comparison**: Baselines use reported hyperparameters while CurCon uses grid search over 48 configurations. This introduces potential bias. A fairer comparison would involve grid-searching all methods.
- **Confounding factors**: The curriculum length L is selected on the validation set via grid search. It's unclear whether improvements come from the curriculum concept or simply from better hyperparameter tuning.
- **Statistical significance**: While standard deviations are reported, no significance tests are provided. The improvements, while consistent, are sometimes modest (0.8-1.5 points).
- **Limited analysis of design choices**: Why these specific thresholds (0.25, 0.5, 0.75)? Why linear scheduling? These choices appear arbitrary and are acknowledged but not investigated.
- **Operator details unclear**: The exact sampling procedure when multiple operators are available needs clarification. Is it truly uniform? What about deterministic behavior during validation?

## Novelty: 65/100

**Strengths:**
- Applying curriculum learning specifically to augmentation strength in contrastive learning is a natural but under-explored idea
- The application to text classification with intermediate training represents a concrete contribution
- Simple, interpretable approach requiring no architectural changes

**Weaknesses:**
- **Limited novelty**: The core idea is straightforward application of known curriculum learning principles to an existing method (CERT). Curriculum learning and progressive augmentation have been explored in vision.
- **Incremental over CERT**: The paper essentially adds one design component (curriculum scheduling) to CERT. The novelty is more engineering-oriented than conceptual.
- **Design choices not novel**: The four augmentation operators are existing techniques; the curriculum itself is linear and hand-designed (acknowledged by authors)
- **No new theoretical insights**: The paper is purely empirical without providing deeper understanding of why curriculum scheduling helps contrastive learning

## Significance: 70/100

**Strengths:**
- Addresses a practically important problem (low-resource text classification with 500 labeled examples)
- Consistent improvements across four diverse datasets
- Gains are largest when labeled data is scarce (Table 3), making this practically relevant
- Simple method that practitioners can easily adopt
- Average improvement of 1.1 points over CERT is meaningful in low-resource settings

**Weaknesses:**
- **Limited scope**: Only English, relatively short texts, BERT-base only. No evaluation on longer documents, other languages, or larger models (acknowledged limitation).
- **Modest absolute gains**: While 88.9 vs 87.8 is consistent, it's not transformative
- **Pre-computed back-translation limits applicability**: The method requires precomputing augmentations, which limits flexibility
- **Restricted to text classification**: Unclear whether findings generalize to other NLP tasks
- **No downstream impact analysis**: How do these improvements translate to real-world applications?

## Clarity: 82/100

**Strengths:**
- Well-structured paper with clear motivation
- Method is easy to understand and implement
- Figures and tables are informative
- Implementation details are provided (batch size, optimizer, early stopping)
- The curriculum schedule formula is clearly specified

**Weaknesses:**
- **Augmentation operator probabilities** are explained somewhat ambiguously. The description "available when c(t) exceeds X" could be clearer about exact sampling probabilities
- **Missing details**: How is the curriculum length L selected? Is validation set accuracy monitored during training? How sensitive are results to the grid search range?
- **Limited discussion of failure cases**: No analysis of when/why CurCon doesn't improve over CERT
- **Computational cost**: "approximately 12% longer" is vague—actual wall-clock times would be helpful

## Detailed Comments

1. **Hyperparameter fairness (Critical)**: The paper's main concern is that CurCon undergoes grid search while baselines don't. The authors should either (a) grid-search all methods or (b) show results are robust to curriculum length choices.

2. **Curriculum design**: Why linear? Table 2 shows reversed curriculum performs worse (-1.3 points), but this could simply reflect "easy-to-hard is better than hard-to-easy" rather than validating linearity specifically.

3. **Statistical testing**: With standard deviations, confidence intervals or significance tests would strengthen claims.

4. **Reproducibility**: Code availability is not mentioned. Given modest margins, reproducibility is important.

5. **Table 3 analysis**: The 1.6→0.5 point improvement trend is interesting and well-explained, but deserves deeper investigation.

## Minor Issues
- Some redundancy between abstract and introduction
- "Content words" in augmentation section needs clearer definition
- Related work could better position this work relative to recent curriculum learning in NLP

## Missing Experiments
- Sensitivity analysis on curriculum hyperparameters (threshold values 0.25, 0.5, 0.75)
- Different curriculum schedules (exponential, step-based)
- Larger models (RoBERTa, ALBERT)
- Cross-domain evaluation (train on one domain, apply to another)

## Recommendation Justification

This is a competent empirical paper that combines existing ideas (curriculum learning + contrastive intermediate training) in a straightforward manner. The experiments are reasonably rigorous, and improvements are consistent across datasets. However:

- **Novelty is limited**: The contribution is primarily engineering-oriented
- **Significance is moderate**: Improvements are consistent but modest (1.1 points on average)
- **Soundness concerns**: Hyperparameter fairness is questionable
- **Scope is narrow**: Limited to English, short texts, BERT-base

The paper would be suitable for a workshop or application-focused venue, but falls slightly short of the bar for a top-tier venue due to limited novelty and incremental nature of the contribution.

---

## Final Scores:
- **Soundness**: 75
- **Novelty**: 65
- **Significance**: 70
- **Clarity**: 82

**Average Score: 73/100**

## Final Recommendation: **BORDERLINE REJECT** (or Weak Accept depending on venue)

**Rationale**: This is a well-executed empirical paper with consistent results, but the contribution is primarily an engineering optimization of an existing method. The modest improvements (1.1 points average), limited scope (English, short texts, BERT-base), and potential hyperparameter fairness issues prevent a strong acceptance. The paper would benefit from: (1) fairer hyperparameter comparison, (2) evaluation on larger/different models, (3) deeper investigation of why curriculum scheduling helps, and (4) multilingual experiments.

For a specialized venue (e.g., low-resource NLP workshop), this could be accepted. For a general conference, it falls short of the novelty/significance bar.