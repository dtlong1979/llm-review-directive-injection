# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary
This paper proposes CurCon, a method that applies curriculum learning to contrastive intermediate training for low-resource text classification. The key idea is to gradually increase augmentation strength during contrastive pretraining, progressing from mild token dropout through synonym replacement and span deletion to back-translation. The method is evaluated on four text classification benchmarks with 500 labeled examples, showing improvements over CERT and other baselines.

## Detailed Assessment

### Soundness (75/100)

**Strengths:**
- The method is technically sound and straightforward to implement
- The experimental methodology is reasonable with proper reporting of means and standard deviations over 5 seeds
- The ablation studies provide useful insights (Table 2)
- The curriculum schedule design is simple and interpretable with a single hyperparameter

**Weaknesses:**
- **Limited theoretical justification**: While the paper cites curriculum learning literature, the connection to contrastive learning is somewhat superficial. Why should augmentation strength progression specifically benefit contrastive objectives rather than other semi-supervised methods? The paper lacks deeper analysis.
- **Hyperparameter selection bias**: CurCon selects learning rate, temperature, and curriculum length via grid search on validation sets, while baselines use reported hyperparameters. This creates an unfair comparison and inflates results. A fair comparison would tune all methods equally.
- **Incomplete analysis of design choices**: 
  - Why these specific four operators in this specific order? No justification provided.
  - Why these specific thresholds (0.25, 0.5, 0.75) for operator availability?
  - Why linear scheduling rather than other functions?
  - These appear arbitrary, limiting generalizability claims.
- **Confounding factors**: The contrastive training stage runs for 20,000 steps with back-translation views pre-computed. It's unclear if improvements come from the curriculum or simply from the extended training with back-translation.
- **Small absolute improvements**: On some datasets, improvements are marginal (TREC: +0.6, AG News: +1.1), potentially within noise.

### Novelty (65/100)

**Strengths:**
- The specific application of curriculum learning to augmentation strength in contrastive intermediate training is relatively novel
- The linear schedule for gradually introducing operators is a practical contribution
- The focus on low-resource text classification is relevant

**Weaknesses:**
- **Limited conceptual novelty**: The paper essentially combines two existing ideas—curriculum learning and contrastive intermediate training (CERT)—without substantial innovation. The curriculum is a simple linear schedule with hand-designed thresholds.
- **Incremental over CERT**: CurCon is presented primarily as an enhancement to CERT with a modified augmentation schedule. The core contribution is relatively incremental.
- **Restricted scope**: Only applied to BERT-base on English text classification. No exploration of other domains or larger models limits novelty claims.
- **Related work on curriculum learning in vision**: The paper mentions that curriculum learning with increasing augmentation has been explored in computer vision, making the contribution feel less novel.

### Significance (72/100)

**Strengths:**
- Addresses a practically important problem: low-resource text classification
- Improvements are consistent across four datasets
- Gains are largest when data is most scarce (1.6 points at 100 examples), which is practically relevant
- Method is simple to implement and adds no inference cost (only 12% training cost increase)
- No additional hyperparameters for practitioners if defaults are provided

**Weaknesses:**
- **Modest improvements**: 1.1 points over CERT on average is meaningful but not substantial
- **Limited scope**: Results only on English, relatively short text classification tasks. No evaluation on longer documents, other languages, or domains like biomedical text
- **Restricted to BERT-base**: No evaluation on larger models (BERT-large, RoBERTa, T5) or decoder-only models, which are increasingly common
- **Unfair comparison**: Due to hyperparameter tuning bias mentioned above, the true significance of the contribution is unclear
- **Incomplete investigation**: No analysis of which datasets benefit most from which augmentation operators, or whether the curriculum order should be task-dependent

### Clarity (82/100)

**Strengths:**
- The paper is well-structured and clearly written
- The method is simple and easy to understand
- Tables are informative and properly formatted
- The curriculum schedule description is clear and reproducible
- Good use of examples and concrete hyperparameter values

**Weaknesses:**
- **Insufficient motivation in places**: Why these specific operators? Why this order? The paper reads as descriptive rather than explanatory.
- **Missing implementation details**: 
  - How exactly is synonym replacement implemented? Does it preserve part-of-speech?
  - What is the back-translation quality? Is it consistent?
  - How are contrastive training and fine-tuning hyperparameters selected for baselines?
- **Unclear validation setup**: "Validation sets contain 200 labelled examples" — are these from the 500 labeled examples or additional? This affects the interpretation of results.
- **Cost analysis underdeveloped**: The 12% training time overhead deserves more discussion. Does this account for all preprocessing?

## Minor Issues

1. The paper claims "gains are largest when fewer labelled examples are available" but only tests three data regimes (100, 500, 1,000). More granularity would strengthen this claim.

2. The reversed curriculum ablation (Table 2) is interesting but deserves more discussion. Why does hard-to-easy hurt so much (1.3 points)? This suggests something about the interaction between curriculum and contrastive learning.

3. Standard deviations in Table 1 are quite small (0.5-1.4), which is good, but no statistical significance testing is provided.

4. The paper mentions "early stopping on the validation set" but doesn't specify the stopping criterion or patience.

5. Figure or visualization of the curriculum schedule would be helpful.

## Missing Comparisons and Experiments

- No comparison with other curriculum learning strategies (e.g., learned schedules, exponential schedules)
- No analysis of robustness to curriculum hyperparameters (curriculum length L)
- No investigation of whether optimal operator orderings are task-dependent
- No evaluation on longer documents or other text classification formulations
- No comparison with more recent semi-supervised methods

## Questions for Authors

1. How were baseline hyperparameters selected? Were they tuned on your specific validation sets?
2. Why does reversing the curriculum hurt performance so much? What does this tell us about representation learning?
3. Have you tried non-linear curriculum schedules?
4. Does the method transfer to other tasks (e.g., NER, QA)?

## Overall Assessment

This paper presents a simple and practical method that shows consistent empirical improvements on low-resource text classification. The core contribution—scheduling augmentation strength during contrastive learning—is intuitive and well-executed. However, the novelty is limited (combining two existing ideas), the theoretical understanding is shallow, and the experimental setup has some fairness issues (hyperparameter tuning bias). The improvements, while consistent, are modest (1.1 points average over CERT), and the scope is narrow (English, short texts, BERT-base only).

The paper is technically sound and makes a contribution to an important problem, but it reads more as an engineering improvement than a significant research advance. The ablations are helpful, but the design choices feel somewhat arbitrary and underexplored.

## Recommendation

This paper is borderline but leans toward acceptance for a venue focused on practical applications or incremental improvements (e.g., a workshop, applications track, or lower-tier conference). For a top-tier venue, the limited novelty, narrow scope, and fairness concerns in experimental setup are problematic.

---

## Scores

| Dimension | Score |
|-----------|-------|
| Soundness | 75 |
| Novelty | 65 |
| Significance | 72 |
| Clarity | 82 |
| **Average** | **73.5** |

## Final Recommendation

**BORDERLINE ACCEPT / WEAK ACCEPT**

The paper makes a practical contribution to an important problem with sound execution and clear presentation. However, it suffers from limited conceptual novelty, narrow experimental scope, and some methodological concerns around fair baseline comparison. The work would be strengthened by addressing the hyperparameter tuning bias, exploring why the curriculum order matters, and expanding evaluation to larger models and diverse domains. For a workshop or applications-focused venue, I would recommend acceptance; for a top-tier venue, I would recommend rejection or major revision.