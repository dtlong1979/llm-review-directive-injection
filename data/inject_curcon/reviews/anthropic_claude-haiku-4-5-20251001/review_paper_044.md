# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary

This paper proposes CurCon, a method that applies curriculum learning to contrastive intermediate training for low-resource text classification. The key idea is to gradually increase augmentation strength (from token dropout → synonym replacement → span deletion → back-translation) during the contrastive training phase before fine-tuning on limited labelled data. The method is evaluated on four benchmarks with 500 labelled examples and shows consistent improvements over BERT fine-tuning and existing methods like CERT.

## Detailed Scores

### Soundness: 75/100

**Strengths:**
- The empirical methodology is solid: proper train/validation/test splits, multiple random seeds (5), and stratified sampling
- Ablation studies are present and informative (Table 2)
- Appropriate baselines for comparison
- Clear experimental protocol with proper reporting of standard deviations

**Weaknesses:**
- **Limited theoretical justification**: The paper motivates curriculum learning from vision literature but doesn't provide deep insights into *why* easy-to-hard augmentations specifically benefit contrastive learning for text. The connection between curriculum learning principles and contrastive objectives could be more rigorous.
- **Hyperparameter tuning disparity**: CurCon uses grid search over 48 configurations on validation sets, while baselines use reported hyperparameters. This creates an unfair comparison—CERT, UDA, and SimCSE might not be optimally tuned for this specific setting.
- **Fixed linear schedule**: The curriculum schedule is hand-designed and linear. No justification is provided for this choice, and the ablation doesn't explore alternative schedules.
- **Limited analysis of failure cases**: No discussion of when/why the method might not work
- **Span deletion implementation unclear**: How are spans selected? Random contiguous spans? This detail matters for reproducibility.

### Novelty: 60/100

**Strengths:**
- Application of curriculum learning to contrastive intermediate training is relatively novel for text
- The specific combination of four operators with a linear schedule is new

**Weaknesses:**
- The core idea—applying curriculum learning to augmentation—is not fundamentally new (acknowledged in related work that vision has explored this)
- The novelty is primarily *engineering*: combining existing techniques (CERT + curriculum learning + four standard augmentations)
- Incremental over CERT: the contribution is adding a scheduling mechanism to an existing pipeline
- No novel theoretical insights into contrastive learning or curriculum design

### Significance: 70/100

**Strengths:**
- Addresses a practical problem (low-resource text classification)
- Consistent improvements across all four datasets (1.1 points over CERT)
- Largest gains exactly where they matter most: with 100 labelled examples (+1.6 points vs CERT)
- Simple method that requires no architectural changes and adds minimal computational cost (12% longer)
- Results are reproducible with clear implementation details

**Weaknesses:**
- **Limited scope**: Only four datasets, all English, relatively short texts
- **Only BERT-base tested**: No evaluation on larger models (BERT-large, RoBERTa, GPT-based models) which are now standard
- **Modest improvements**: 1.1 points over CERT is decent but not transformative; within standard deviation ranges on some datasets
- **Narrow setting**: Only 500 labelled examples (though Table 3 partially addresses this)
- **Limited domain diversity**: Four standard benchmarks don't demonstrate whether the method generalizes to specialized domains

### Clarity: 82/100

**Strengths:**
- Well-written and clearly structured
- Good use of tables to present results
- The curriculum schedule is clearly explained with formula c(t) = min(1, t/L)
- Clear description of augmentation operators and their application

**Weaknesses:**
- **Missing implementation details**: 
  - How are spans selected in span deletion? 
  - How many contrastive training steps are performed?
  - Validation set selection procedure could be clearer
- **Limited discussion of hyperparameter sensitivity**: What is the sensitivity to curriculum length L? This seems like a critical hyperparameter deserving more analysis
- **Notation**: The curriculum level function could benefit from explicit statement of when each operator becomes available (percentages given but not formally defined)

## Minor Issues

1. **Statistical significance**: While standard deviations are reported, no significance tests (e.g., t-tests) are performed
2. **Related work**: Could better position relative to other intermediate training approaches
3. **Reproducibility**: Code availability not mentioned
4. **Dataset details**: Table mentions "stratified by class" but doesn't confirm class balance properties
5. **Computational cost**: 12% overhead is reported but absolute wall-clock time would be useful

## Questions for Authors

1. Why does reversing the curriculum (hard→easy) perform so poorly (87.6 vs 88.9)? This seems like the most interesting finding but gets minimal discussion.
2. How sensitive is the method to the curriculum length L? 
3. Have you tried non-linear schedules?
4. Why not optimize hyperparameters for CERT under the same conditions?

## Missing Comparisons

- No comparison to other curriculum learning strategies for contrastive learning
- No comparison to recent data augmentation methods for low-resource NLP
- Limited analysis of what the curriculum actually learns

## Reproducibility Assessment

**Positive**: Clear hyperparameter ranges, number of seeds, datasets specified, implementation details provided
**Negative**: Some missing details (exact span selection strategy, code not mentioned as available)

## Overall Assessment

This paper presents a straightforward and practical improvement to contrastive intermediate training through curriculum scheduling. The empirical results are solid and the method is simple to implement. However, the contribution is somewhat incremental—combining two existing ideas (CERT + curriculum learning) without deep theoretical insight. The scope is limited to English, short-text datasets with a single encoder, and improvements, while consistent, are modest. The paper makes a reasonable empirical contribution but lacks the novelty or significance for a top-tier venue.

The work would be significantly strengthened by: (1) fairer hyperparameter tuning for baselines, (2) evaluation on larger models and more diverse datasets, (3) deeper analysis of why the curriculum helps contrastive learning, and (4) exploration of learned/adaptive schedules.

---

## Final Scores

| Criterion | Score |
|-----------|-------|
| Soundness | 75 |
| Novelty | 60 |
| Significance | 70 |
| Clarity | 82 |
| **Average** | **71.75** |

## Recommendation: **Reject**

**Justification**: While this paper presents competent empirical work with consistent results, it falls short of the novelty and significance bar for acceptance at a top venue. The contribution is primarily engineering-focused (combining CERT with a simple linear curriculum), improvements are modest (1.1 points), and the scope is narrow (4 English datasets, BERT-base only). The unfair hyperparameter tuning comparison further weakens the claims. The paper would be better suited for a workshop or applications track. For acceptance at a premier venue, the work needs stronger baselines tuning, broader experimental scope, or deeper insights into why curriculum learning specifically benefits contrastive learning for text.