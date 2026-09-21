# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary

This paper proposes CurCon, a method that incorporates curriculum learning into contrastive intermediate training for low-resource text classification. The key idea is to gradually increase augmentation strength during the contrastive pretraining phase, starting with mild perturbations (token dropout) and progressing to aggressive transformations (back-translation, span deletion). The method is evaluated on four text classification benchmarks with 500 labeled examples, showing consistent improvements over strong baselines including CERT.

## Soundness (78/100)

**Strengths:**
- The experimental methodology is solid with proper controls: five random seeds reported with standard deviations, stratified sampling, appropriate train/validation/test splits
- The ablation studies are well-designed and provide useful insights (curriculum vs. fixed mixture, reversed curriculum, removal of individual components)
- The comparison against reasonable baselines (fine-tuning, UDA, SimCSE, CERT) is appropriate
- Implementation details are sufficiently clear for reproducibility

**Weaknesses:**
- The curriculum schedule is simple and hand-designed (linear with fixed thresholds: 0.25, 0.5, 0.75). While the paper acknowledges this limitation, no justification is provided for these specific values. Sensitivity analysis would strengthen claims
- The choice of augmentation operators and their ordering appears somewhat arbitrary. Why is token dropout->synonym replacement->span deletion->back-translation the right progression? Alternative orderings are not explored beyond the "reversed curriculum" ablation
- Hyperparameter selection via grid search on each validation set is reasonable but raises questions about generalization. The curriculum length L appears to be tuned per dataset, which limits the method's practical applicability
- The modest improvements (1.1 points over CERT) may not account for potential variance in hyperparameter selection across methods. While standard deviations are reported, comparative fairness could be questioned

**Minor concerns:**
- Back-translation requires external resources (German MT system), introducing potential dependencies and language-specificity
- The paper doesn't discuss computational cost comparisons with baselines, only relative cost to CERT (12% slower)

## Novelty (72/100)

**Strengths:**
- The application of curriculum learning to augmentation strength in contrastive learning for NLP is relatively novel
- The specific instantiation for text classification with intermediate training is reasonably new
- The paper clearly positions itself relative to prior work in curriculum learning, contrastive learning, and low-resource classification

**Weaknesses:**
- Curriculum learning is well-established; the contribution is primarily an engineering application rather than a fundamental insight
- The idea of increasing augmentation difficulty during training has been explored in computer vision (as acknowledged). The adaptation to NLP is somewhat incremental
- The augmentation operators themselves are not novel—they are taken from prior work (EDA, back-translation)
- The method closely follows the CERT pipeline with a single modification (curriculum scheduling). The novelty is somewhat limited in scope

## Significance (74/100)

**Strengths:**
- Low-resource text classification is practically important
- Consistent improvements across four diverse datasets (sentiment, topic, question classification, subjectivity) suggest some generality
- The insight that gains are largest with fewer labeled examples (Table 3: 1.6 points at 100 examples vs. 0.5 at 1,000) is valuable
- The method is practical: minimal hyperparameters, no additional inference cost, works with existing fine-tuning procedures

**Weaknesses:**
- Limited evaluation scope: only 500 labeled examples as primary setting; only English; only BERT-base encoder
- Improvements are modest in absolute terms (1.1 points average over CERT), which limits practical impact
- The paper doesn't establish whether improvements translate to other domains, languages, or model sizes
- No analysis of what representations are learned differently with curriculum vs. fixed augmentation (e.g., visualization or probing tasks)
- The limitation to "relatively short texts" is concerning given the increasing prevalence of longer document classification

## Clarity (85/100)

**Strengths:**
- The paper is generally well-written and easy to follow
- The method description is clear and concise
- Figures and tables are informative (particularly Table 3's analysis by labeled data quantity)
- The experimental setup is transparent
- Related work is well-organized and positions the contribution clearly

**Weaknesses:**
- The curriculum schedule definition (equation: c(t) = min(1, t/L)) could be presented more formally upfront
- Limited discussion of *why* curriculum learning should help contrastive learning—the intuition is briefly mentioned but not deeply explored
- The paper could better explain why back-translation at the end is particularly beneficial
- Missing details on validation set construction for hyperparameter selection (how are 200 examples reserved for validation from the labeled set in the 500-example setting?)

## Detailed Comments

1. **Curriculum design rationale**: The progression from token dropout → synonym replacement → span deletion → back-translation is presented as obvious, but alternatives deserve exploration. Why not try different orderings systematically?

2. **Generalization**: The claim of improvements would be stronger with evaluation on at least one dataset in a different language or domain, or with different model sizes (BERT-large, RoBERTa, etc.)

3. **Statistical significance**: While standard deviations are reported, no significance tests are provided. Given the relatively small differences and moderate variance, confidence intervals would be helpful.

4. **Analysis depth**: The paper would benefit from analysis of what the curriculum learns differently. Do learned representations differ in interpretable ways?

## Minor Issues

- The statement "adds no inference cost" is correct but could be emphasized earlier
- Table 1: The improvements are consistent but modest; confidence in ranking across datasets given overlapping error bars would be useful
- The 12% slowdown during training is non-negligible and deserves more discussion

## Recommendation Justification

This paper presents a straightforward but effective modification to existing contrastive intermediate training. While the novelty is limited (applying established curriculum learning principles to augmentation strength), the work is sound, the experiments are reasonably comprehensive for the scope, and the results are consistent. The practical utility for low-resource scenarios is clear, and the insights about diminishing returns with more labeled data are valuable. The limitations are acknowledged appropriately, and the writing is clear.

The work makes a solid incremental contribution to an important problem. The experimental methodology is rigorous, the baselines are strong, and the improvements are demonstrated across multiple datasets. However, the modest absolute improvements, limited scope of evaluation (English only, BERT-base only, short texts), and incremental nature of the contribution prevent this from being a strong accept.

---

## Scores

| Dimension | Score |
|-----------|-------|
| Soundness | 78 |
| Novelty | 72 |
| Significance | 74 |
| Clarity | 85 |
| **Average** | **77** |

## Final Recommendation

**ACCEPT**

This paper merits acceptance as a solid contribution to low-resource text classification. It demonstrates rigorous experimental work with consistent improvements on multiple benchmarks. While the novelty is incremental and improvements are modest, the simplicity, practicality, and consistent empirical gains across datasets make it a worthwhile addition to the literature. The work will be of interest to practitioners working with limited labeled data and researchers in semi-supervised and contrastive learning. The limitations are appropriately acknowledged and provide clear directions for future work.