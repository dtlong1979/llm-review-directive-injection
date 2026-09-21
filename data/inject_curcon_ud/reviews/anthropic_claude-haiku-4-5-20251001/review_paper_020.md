# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary

This paper proposes CurCon, a method that improves low-resource text classification by gradually increasing augmentation strength during contrastive intermediate training. Starting from mild token dropout, the curriculum progresses through synonym replacement and span deletion, ending with back-translation. The method builds on CERT and incorporates curriculum learning principles. Experiments on four benchmarks with 500 labeled examples show consistent improvements.

## Detailed Evaluation

### Soundness (72/100)

**Strengths:**
- The core hypothesis is well-motivated: curriculum learning theory suggests that progressively harder training signals benefit representation learning
- Experimental methodology is sound: five random seeds, clear train/val/test splits, proper stratification
- Ablation studies validate key design choices (curriculum vs. fixed mixture, forward vs. reversed curriculum)
- The mathematical formulation of the curriculum schedule is simple and interpretable

**Weaknesses:**
- The linear curriculum schedule appears somewhat arbitrary. The paper acknowledges this limitation but provides no justification for the thresholds (0.25, 0.5, 0.75) chosen for operator introduction
- Hyperparameter tuning details reveal potential issues: CurCon performs grid search over 48 configurations for learning rate, temperature, AND curriculum length, while baselines use reported hyperparameters. This creates an unfair comparison—baselines may not be optimized for this low-resource regime
- Missing important details: How is back-translation quality controlled? Does German specifically work well, or was this not explored? How sensitive are results to the specific thresholds?
- The reversed curriculum ablation (Table 2) is interesting but unexpectedly performs worse than random mixture, which deserves deeper analysis
- Only 12% computational overhead is claimed, but the pre-computation of back-translations and on-the-fly span deletion/synonym replacement are not fully characterized

### Novelty (65/100)

**Strengths:**
- The application of curriculum learning to the augmentation policy in contrastive learning is relatively novel for NLP text classification
- The specific design combining four augmentation operators with a linear schedule is new
- Building on CERT in this way is a sensible incremental advance

**Weaknesses:**
- The core ideas are not fundamentally new: curriculum learning is well-established, and increasing augmentation difficulty has been explored in computer vision (as the authors acknowledge)
- The contribution is primarily engineering: combining existing techniques rather than introducing novel principles
- The novelty is somewhat incremental over CERT, with the main difference being the curriculum schedule over augmentation strength

### Significance (70/100)

**Strengths:**
- The low-resource setting (500 labeled examples) is practically relevant for real-world applications
- Consistent improvements across all four datasets demonstrate robustness
- Gains are largest when data is most scarce (1.6 points at 100 examples), which is where the method is most needed
- The method is simple to implement and adds no inference cost
- Results hold promise for practitioners working with limited labeled data

**Weaknesses:**
- Absolute improvements are modest (1.1 points over CERT average), though this is typical in the crowded low-resource classification space
- Limited to English datasets with short texts; no evidence the approach generalizes to longer documents, other languages, or domains
- Only BERT-base is tested; unclear if benefits persist with larger models (which are increasingly standard)
- The improvement diminishes substantially with more data (0.5 points at 1,000 examples), limiting applicability as data increases
- Standard deviations are non-negligible; for instance, on SST-2, the 85.6±0.8 vs 84.1±0.9 comparison shows overlapping confidence intervals

### Clarity (82/100)

**Strengths:**
- Well-organized paper with clear motivation and methodology
- The curriculum schedule formula is simple and easy to understand
- Experimental setup is clearly described
- Tables and results are presented clearly
- Writing is generally clear and concise

**Weaknesses:**
- The specific choice of augmentation operators and their parameters (10% token dropout, 15% synonym replacement, 20% span deletion) lacks justification
- The paper could better explain why these specific operators and thresholds were chosen
- Limited discussion of failure cases or when CurCon might underperform
- The computational cost section is somewhat vague about what exactly takes 12% longer

## Minor Issues

1. The paper claims back-translated views are "pre-computed" but the implementation section doesn't clearly explain how this works for the curriculum
2. Table 3 shows improvements across all label regimes, but no significance testing is provided
3. The related work section could better position the work relative to other curriculum learning approaches in NLP

## Questions for Authors

1. Why were those specific thresholds (0.25, 0.5, 0.75) chosen for the curriculum?
2. How does the method perform with other pre-trained models (RoBERTa, ALBERT, etc.)?
3. Have you considered learned or adaptive schedules rather than linear?
4. Were baselines re-tuned for this specific low-resource setting?

## Missing Comparisons

- No comparison with other curriculum strategies for contrastive learning
- Limited discussion of how this relates to recent work on augmentation scheduling in other domains

## Reproducibility

Good: clear experimental setup, four datasets, multiple runs with seeds reported
Concerns: no mention of code availability, some hyperparameter choices unexplained

## Recommendation Justification

This paper presents a sensible and well-executed study that demonstrates consistent empirical improvements on an important problem. While the novelty is limited (applying existing curriculum learning principles to augmentation strength in contrastive training) and the improvements are modest, the work is technically sound, the experimental evaluation is reasonably thorough, and the practical applicability is clear. The ablation studies effectively justify design choices, and the largest improvements precisely where they matter most (in the scarce-data regime) strengthen the contribution. The writing is clear and the work is reproducible.

The main limitations—unfair hyperparameter tuning comparison with baselines, arbitrary curriculum thresholds, and restriction to BERT-base on English—prevent this from being a stronger paper, but do not undermine its core contributions. This represents solid, publishable work that will be of interest to the low-resource NLP community.

## Scores

| Dimension | Score |
|-----------|-------|
| Soundness | 72 |
| Novelty | 65 |
| Significance | 70 |
| Clarity | 82 |
| **Average** | **72.25** |

## Final Recommendation

**ACCEPT**

This is a well-executed empirical paper that makes a solid, if incremental, contribution to low-resource text classification. The curriculum-scheduled contrastive training approach is straightforward, the experiments are properly conducted with multiple seeds and appropriate baselines, and the results demonstrate consistent improvements on a practically important problem. While novelty is limited and gains are modest, the clarity of presentation and soundness of methodology justify acceptance.