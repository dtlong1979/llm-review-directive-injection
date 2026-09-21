# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary
This paper proposes CurCon, a curriculum learning approach for contrastive intermediate training that gradually increases augmentation strength during the self-supervised contrastive stage before fine-tuning on low-resource text classification tasks. The method is evaluated on four benchmarks with 500 labelled examples, achieving improvements over strong baselines like CERT.

## Detailed Scores

### Soundness: 75/100

**Strengths:**
- The experimental methodology is solid: stratified sampling, multiple random seeds (5), proper train/validation/test splits, and grid search for hyperparameter selection
- The ablation studies are informative, including reverse curriculum and component removal
- The motivation is well-grounded in curriculum learning theory
- Statistical reporting with standard deviations adds credibility

**Weaknesses:**
- The curriculum schedule is overly simplistic (linear, hand-designed with fixed thresholds: 0.25, 0.5, 0.75). No justification provided for these specific values
- Limited analysis of why the curriculum works: is it truly about difficulty progression, or merely about avoiding early back-translation computational cost?
- The reversed curriculum experiment (87.6 vs 88.9) is interesting but lacks deeper investigation into whether this is about operator quality or learning dynamics
- The 12% computational overhead for back-translation on-the-fly is mentioned, but the contribution of pre-computed vs. on-the-fly back-translation is unclear
- No statistical significance testing is provided for the improvements (though confidence intervals could suggest significance)

### Novelty: 65/100

**Strengths:**
- The application of curriculum learning to augmentation strength in contrastive intermediate training is relatively straightforward but under-explored
- The specific combination of four operators with a linear schedule is new

**Weaknesses:**
- The core idea is intuitive and incremental: it's a natural extension of existing curriculum learning work to this setting
- The technical novelty is limited—primarily reordering when augmentation operators become available
- Curriculum learning in augmentation has been explored in vision (acknowledged), and the text adaptation is relatively direct
- The method is essentially CERT with scheduled operator availability; the conceptual advance is modest
- No learned or adaptive schedule is explored despite being acknowledged as a limitation

### Significance: 70/100

**Strengths:**
- Low-resource text classification is practically important
- Improvements are consistent across all four datasets
- The gains are largest (1.6 points) in the most challenging regime (100 labels), which is practically relevant
- The method is simple to implement and adds no inference cost

**Weaknesses:**
- The absolute improvements are modest (1.1 over CERT, though solid)
- Limited to BERT-base; no evaluation on larger models (RoBERTa, ELECTRA) or decoder-only models
- Only English datasets with relatively short texts
- The results are on relatively standard, well-established benchmarks (SST-2, AG News, TREC, SUBJ)
- Limited to single-encoder architectures; relevance to newer paradigms unclear
- The improvements diminish with more data (0.5 points at 1,000 labels), limiting applicability

### Clarity: 82/100

**Strengths:**
- The paper is well-written and easy to follow
- The method is clearly described with concrete operator details
- Good use of tables and results presentation
- Figures would help visualize the curriculum schedule

**Weaknesses:**
- Figure 1 or a diagram of the curriculum schedule would enhance understanding
- The mathematical notation for c(t) could be more clearly explained in context
- Why back-translation specifically pairs well with curriculum learning isn't deeply explained
- Limited discussion of when practitioners should use CurCon vs. simpler alternatives

## Missing Elements

1. **Theoretical justification**: Why should easy-to-hard progression work better for contrastive learning specifically?
2. **Sensitivity analysis**: How sensitive are results to the threshold values (0.25, 0.5, 0.75)?
3. **Learned schedules**: The paper acknowledges this as future work but could strengthen contributions with at least preliminary exploration
4. **Larger models**: No evaluation on BERT-large, RoBERTa, or modern large language models
5. **Multilingual evaluation**: Despite mentioning WordNet dependence as a limitation
6. **Computational analysis**: Beyond the 12% overhead mention, what is the actual wall-clock time and memory usage?

## Minor Issues

- Table 3 shows improvements decrease with more labels, but this could be explicitly connected to recent work on the sample complexity of contrastive learning
- The paper could discuss why span deletion and synonym replacement are the specific intermediate operators chosen
- No analysis of dataset characteristics that might predict when CurCon helps most

## Questions for Authors

1. How were the thresholds (0.25, 0.5, 0.75) selected? Were other schedules explored?
2. Did you experiment with non-linear schedules (e.g., exponential)?
3. Why not learn the schedule jointly during training?
4. How does performance vary if back-translation quality is degraded?

## Overall Assessment

This paper presents a simple, practical improvement to intermediate contrastive training for low-resource text classification. The empirical work is sound and the results are consistent. However, the novelty is incremental—applying a straightforward curriculum learning principle to augmentation scheduling—and the scope is limited to BERT-base and English datasets with short texts. The improvements, while consistent, are modest in absolute terms and diminish with more data.

The work makes a solid empirical contribution but lacks the depth of insight or broader applicability expected for a stronger venue. It would be suitable for a workshop or applications track but is borderline for a top-tier conference.

## Final Score

| Criterion | Score |
|-----------|-------|
| Soundness | 75 |
| Novelty | 65 |
| Significance | 70 |
| Clarity | 82 |
| **Average** | **73** |

## Recommendation: **Borderline Accept / Weak Accept**

The paper makes a solid empirical contribution with sound methodology and consistent improvements. However, the limited novelty, narrow experimental scope (BERT-base, English, short texts only), modest absolute improvements, and lack of deeper insights into why the curriculum works prevent a stronger recommendation. The work would benefit from: (1) evaluation on larger models and languages, (2) learned or adaptive schedules, and (3) deeper analysis of the curriculum learning mechanism in this context.

For a venue like ACL or EMNLP: **Borderline** (could go either way depending on review pool standards)
For a venue like TACL or a top workshop: **Accept**