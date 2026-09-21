# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary

This paper proposes CurCon, a method that applies curriculum learning to contrastive intermediate training for low-resource text classification. Rather than using a fixed augmentation policy throughout contrastive pretraining, CurCon gradually increases augmentation strength from mild token dropout to aggressive back-translation. The method is evaluated on four benchmarks with 500 labeled examples, showing improvements over strong baselines including CERT.

## Detailed Evaluation

### Soundness (72/100)

**Strengths:**
- The core idea is intuitive and well-motivated by curriculum learning principles
- The experimental setup is rigorous: five random seeds, stratified sampling, proper train/validation/test splits, and appropriate baselines
- The curriculum schedule design is simple and interpretable (linear progression with thresholds)
- Ablation studies directly validate the curriculum's contribution

**Weaknesses:**
- The improvement over CERT (1.1 points average) is modest and largely comes from hyperparameter tuning (grid search over 48 configurations for CurCon vs. reported hyperparameters for baselines). While standard practice, this creates an unfair comparison—baselines weren't optimized equally.
- Limited theoretical justification for why this specific curriculum order is optimal. The paper doesn't explain why token dropout→synonym replacement→span deletion→back-translation is the right progression, or whether other orderings were tested.
- The reversed curriculum experiment (Table 2) shows a 1.3-point drop, but this is a single alternative; more curriculum variants would strengthen claims about the importance of ordering.
- Back-translation quality depends on external tools (German MT), but no analysis of failure modes or sensitivity to translation errors is provided.
- The 12% computational overhead is non-trivial for intermediate training.

### Novelty (65/100)

**Strengths:**
- The application of curriculum learning specifically to the augmentation policy in contrastive training is relatively novel for text
- The concrete instantiation with four operators of increasing strength is practical

**Weaknesses:**
- Curriculum learning itself is well-established (acknowledged in Section 2)
- Using harder augmentations during training is intuitive; the conceptual contribution is incremental
- Similar ideas have been explored in vision (increasing augmentation magnitude)—the paper doesn't deeply engage with why text differs or why this approach wasn't previously standard
- The method is essentially a straightforward extension of CERT with a scheduled augmentation mixture; the technical novelty is limited

### Significance (70/100)

**Strengths:**
- Low-resource text classification is practically important
- Consistent improvements across all four datasets suggest robustness
- Larger gains with fewer labeled examples (1.6 points at 100 examples vs. 0.5 at 1,000) align with practical motivation
- The method is simple to implement and adds no inference cost

**Weaknesses:**
- The absolute improvements are modest (1.1 points over CERT, 3.8 over fine-tuning)
- Limited to four relatively simple English benchmarks with short texts; generalization is unclear
- No evaluation on modern larger models (only BERT-base) or decoder-only architectures, which are increasingly standard
- Scalability to other domains, languages, or data modalities is unexplored
- The paper is primarily an engineering contribution (scheduling existing augmentations) rather than a fundamental insight

### Clarity (82/100)

**Strengths:**
- Clear motivation and problem formulation
- Well-structured paper with effective use of tables
- The method description is concise and reproducible
- Good use of ablations to isolate contributions

**Weaknesses:**
- The augmentation operator parameters (10% token dropout, 15% synonym replacement, 20% span deletion) are mentioned but not justified. Were these tuned?
- Limited discussion of why curriculum learning helps (e.g., avoiding early collapse of contrastive learning, better basin of attraction?)
- The connection between representation learning difficulty and augmentation strength could be more formally developed
- Some implementation details are missing (e.g., how are multiple augmentation operators composed when sampled?)

## Minor Issues

1. **Hyperparameter fairness:** Grid search over 48 configurations for CurCon vs. reported hyperparameters for baselines is a significant concern. A fairer comparison would either tune all methods equally or show results with baseline-recommended hyperparameters.

2. **Statistical significance:** While standard deviations are reported, no significance tests (t-tests) are provided. Some improvements fall within error bars.

3. **Reproducibility:** Code availability is not mentioned; this would strengthen the contribution.

4. **Missing comparisons:** No comparison with other curriculum scheduling approaches (e.g., learned or adaptive schedules, as mentioned in limitations).

## Questions for Authors

1. How sensitive is performance to the threshold values (0.25, 0.5, 0.75) and operator parameters?
2. Was the reversed curriculum the only alternative tested?
3. What is the performance if baselines also had access to grid search over 48 configurations?
4. How does performance scale to modern larger models (BERT-large, RoBERTa)?

## Strengths of the Work

- Addresses a practically important problem
- Rigorous experimental methodology with multiple seeds and proper splits
- Consistent improvements across datasets
- Simple, interpretable method with clear ablations
- Particularly effective in the most data-scarce regime

## Weaknesses of the Work

- Modest improvements with potential hyperparameter tuning bias
- Limited novelty (straightforward application of known principles)
- Narrow experimental scope (English, short texts, BERT-base only)
- Incremental rather than transformative contribution
- Missing theoretical depth or broader insights

## Recommendation

This is a solid empirical paper that makes a reasonable contribution to low-resource text classification. The core idea is sensible, the experiments are well-executed with proper ablations, and the results are consistent. However, the novelty is incremental (scheduling existing augmentations), the improvements are modest, and the evaluation is limited in scope. The work would be strengthened by fairer baseline comparisons, evaluation on larger models, and deeper investigation of why curriculum learning helps in contrastive settings.

Despite these limitations, the paper presents a practical method with clear empirical benefits in a relevant setting, supported by careful experimental work. It merits publication as a solid empirical contribution, though it is not groundbreaking.

---

## Scores

| Dimension | Score |
|-----------|-------|
| Soundness | 72 |
| Novelty | 65 |
| Significance | 70 |
| Clarity | 82 |
| **Average** | **72.25** |

## Final Recommendation: **Accept**

This paper makes a reasonable empirical contribution to low-resource text classification with careful experimental validation. While the novelty is incremental and improvements are modest, the consistent gains across datasets, particularly in the extreme low-resource regime, and the simplicity of the approach justify publication. The work would benefit from addressing the hyperparameter tuning fairness issue and evaluation on larger models in future iterations.