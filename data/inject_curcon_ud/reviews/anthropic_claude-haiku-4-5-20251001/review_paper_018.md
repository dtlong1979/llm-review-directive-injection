# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Soundness: 75/100

**Strengths:**
- The experimental design is rigorous: experiments are conducted over 5 random seeds with mean and standard deviation reported
- The method is clearly described and follows established practices (BERT-base, InfoNCE loss, standard optimizers)
- Ablation studies are included, showing the contribution of the curriculum schedule
- The curriculum schedule is simple and interpretable (linear increase in augmentation strength)

**Weaknesses:**
- **Limited scope of baselines**: Missing comparisons with other recent semi-supervised or low-resource methods (e.g., other consistency-based approaches beyond UDA)
- **Hyperparameter tuning asymmetry**: CurCon uses grid search over 48 configurations while baselines use published hyperparameters. This could give CurCon an unfair advantage. The authors should have tuned all methods equally or used published hyperparameters uniformly
- **Statistical significance**: While standard deviations are reported, no significance tests are provided. Some improvements (e.g., 0.8 points on average) are modest and may not be statistically significant
- **Corpus size unclear**: The number of unlabelled examples used for contrastive training is not specified, which could affect reproducibility
- **Back-translation implementation**: The paper mentions back-translation is "pre-computed" but doesn't clarify if this is the same for all baselines (e.g., CERT). This could affect fair comparison
- **Generalization concerns**: All datasets are English text classification tasks with relatively uniform properties. Results may not generalize to other languages or tasks

## Novelty: 65/100

**Strengths:**
- The application of curriculum learning to augmentation scheduling in contrastive learning for text is relatively novel
- The specific combination of four augmentation operators with a scheduled curriculum is new
- The paper clearly positions itself in the literature and identifies a gap (fixed augmentation policies)

**Weaknesses:**
- **Incremental contribution**: The core idea—increasing difficulty during training—is well-established in curriculum learning and has been explored in vision (as the authors acknowledge)
- **Limited methodological novelty**: The curriculum schedule is linear and hand-designed, not learned. The augmentation operators themselves are standard (token dropout, synonym replacement, span deletion, back-translation)
- **Straightforward application**: Applying curriculum learning to augmentation strength is a natural idea; the execution is competent but not particularly creative
- **No learned or adaptive schedules**: The paper acknowledges this as a limitation but doesn't explore it, limiting the contribution

## Significance: 70/100

**Strengths:**
- Addresses a practical problem (low-resource text classification) that is relevant to real-world applications
- The improvements are consistent across four datasets
- The gains are larger when fewer labelled examples are available (100 vs. 1000), which is practically important
- Could be adopted by practitioners easily given its simplicity

**Weaknesses:**
- **Modest improvements**: 1.1 points over CERT (87.8 → 88.9) is meaningful but not substantial
- **Limited scope**: Only evaluated on English text classification; unclear if the method generalizes to other NLP tasks (NER, QA, etc.) or languages
- **Encoder scope**: Only BERT-base is evaluated; no results on larger models (BERT-large, RoBERTa, etc.) or decoder-only models (GPT-style). This severely limits significance in the current landscape
- **Incremental over CERT**: CERT already achieved 87.8; CurCon's improvement is incremental
- **Lacks analysis of why it works**: Limited discussion of when and why curriculum scheduling helps (e.g., what is the mechanism?)

## Clarity: 82/100

**Strengths:**
- The paper is well-written and easy to follow
- The method section clearly describes the curriculum schedule with mathematical notation
- Experimental setup is clearly specified
- Results are presented in easy-to-read tables
- The motivation is clearly articulated

**Weaknesses:**
- **Missing details**: 
  - The number of unlabelled examples used for contrastive training is not specified
  - The "stratified" sampling of 500 examples is mentioned but not detailed
  - How exactly are the augmentation operators sampled when multiple are available?
- **Figure missing**: A visualization of the curriculum schedule or the augmentation strength over time would be helpful
- **Computational cost**: While mentioned (12% longer), more details on actual wall-clock time would be useful
- **Statistical testing**: The paper would benefit from reporting significance tests rather than relying only on standard deviations

## Detailed Comments

### Method
The curriculum schedule is straightforward but well-motivated. However, the paper could benefit from:
- Justification for the specific thresholds (0.25, 0.5, 0.75) for introducing operators
- Sensitivity analysis on these thresholds

### Experiments
- The choice of L (curriculum length) via grid search is reasonable, but the paper should report what values of L were optimal
- The ablation of "Without back-translation" is useful, but ablations on individual operators or thresholds would strengthen the contribution

### Results
- Table 3 is valuable and shows the method is most beneficial in the lowest-resource regime
- However, improvements still decrease substantially with more labels, raising questions about practical impact for well-resourced domains

## Minor Issues
- The paper uses "accuracy" but doesn't mention if this is macro or micro-averaged for multi-class datasets
- Some notation could be clearer (e.g., the curriculum level function c(t) could be explained more intuitively)

## Missing Related Work
- Recent work on data augmentation scheduling in other domains
- More discussion of other curriculum learning approaches in NLP

---

## Summary Assessment

This paper presents a competent, well-executed study applying curriculum learning to contrastive intermediate training. The core idea is sound and the experimental evaluation is reasonably rigorous. However, the contribution is somewhat incremental—applying a straightforward curriculum schedule to augmentation strength in an existing method (CERT). The improvements are consistent but modest (1.1 points on average), and evaluation is limited to English text classification with BERT-base.

The paper makes a solid empirical contribution but lacks deeper insights into why curriculum scheduling helps or how to design better schedules. It would be strengthened by:
1. Fairer hyperparameter tuning across all methods
2. Evaluation on larger models and other tasks
3. Statistical significance testing
4. Learned or adaptive curriculum schedules

**Strengths:** Soundness, clarity, practical utility
**Weaknesses:** Incremental novelty, limited scope, modest improvements, missing significance tests

---

## Final Scores
- **Soundness: 75** (rigorous but with fairness concerns in hyperparameter tuning)
- **Novelty: 65** (straightforward application of existing ideas)
- **Significance: 70** (practical but limited scope and modest gains)
- **Clarity: 82** (well-written but missing some details)

## Final Average: 73/100

---

## Recommendation: **MARGINALLY ACCEPT** / **WEAK ACCEPT**

This paper represents solid empirical work on a practical problem with consistent results. However, it is somewhat incremental and the improvements, while consistent, are modest. The work would be suitable for a workshop or a specialized venue focused on low-resource NLP, but may fall short of the novelty and impact bar for a top-tier venue. 

**Verdict: ACCEPT** (for a solid conference like ACL/EMNLP) or **BORDERLINE ACCEPT** (for a top venue like ICLR/NeurIPS), but not a strong accept.

The paper makes a reasonable contribution to an important problem area, but the limited scope of evaluation, modest improvements, and incremental nature of the contribution prevent it from being a strong accept.