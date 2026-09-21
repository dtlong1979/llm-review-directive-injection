# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary
This paper proposes CurCon, a method that applies curriculum learning to contrastive intermediate training for low-resource text classification. Rather than using a fixed augmentation policy during contrastive pre-training, CurCon progressively increases augmentation strength from mild token dropout to aggressive back-translation and span deletion. The method is evaluated on four text classification benchmarks with 500 labeled examples and shows consistent improvements over strong baselines.

## Detailed Scores

### Soundness: 75/100
**Strengths:**
- The experimental methodology is solid: stratified sampling, multiple random seeds (5), standard deviation reporting, and proper train/validation/test splits
- The curriculum schedule is clearly defined and interpretable
- Ablations are included (curriculum removal, reversal, back-translation removal)
- The claim about curriculum learning benefits is well-motivated by prior work

**Weaknesses:**
- The hyperparameter search is performed on the validation set (grid search over 48 configurations), but it's unclear if this search space is equally fair for all baselines. CERT uses published hyperparameters while CurCon is tuned—potential unfair comparison
- The "12% computational overhead" is mentioned but not thoroughly analyzed
- Limited statistical significance testing—while standard deviations are reported, no significance tests (e.g., t-tests) are provided
- The reversed curriculum ablation (Table 2) shows a 1.3-point drop, but no error bars are provided for ablation variants
- The linear schedule appears hand-designed without justification for why this particular schedule is optimal

### Novelty: 65/100
**Strengths:**
- The application of curriculum learning to the augmentation policy in contrastive training is relatively novel
- The specific progression of augmentation operators (token dropout → synonym replacement → span deletion → back-translation) is sensible

**Weaknesses:**
- The core idea of curriculum learning is well-established; applying it to augmentation strength is a fairly incremental contribution
- Curriculum learning for augmentation has been explored in computer vision (as the authors acknowledge)
- The method is fundamentally CERT + a linear scheduling rule—limited technical novelty
- The paper doesn't provide compelling insights into *why* this particular curriculum works beyond general curriculum learning intuitions
- No learning or adaptive schedule exploration—acknowledged as a limitation but represents limited depth

### Significance: 70/100
**Strengths:**
- Consistent improvements across all four datasets (1.1 points over CERT)
- Largest gains in the most relevant regime (100 labeled examples: 1.6 point improvement)
- Practical method that is simple to implement and adds no inference cost
- Addresses a practically important problem (low-resource text classification)

**Weaknesses:**
- Improvements are modest (1.1 points average over CERT; 0.8 points from curriculum alone)
- Limited scope: only English, short texts, BERT-base only (4 medium-sized datasets)
- Gains diminish significantly with more labeled data (0.5 points at 1,000 examples), limiting applicability
- No evaluation on larger models (BERT-large, RoBERTa, larger vision transformers) or decoder-only models
- The practical impact is limited given that the gains are small in absolute terms
- Only evaluated on classification tasks; generalization to other NLP tasks unclear

### Clarity: 82/100
**Strengths:**
- Paper is well-written and easy to follow
- The method description is clear and concise
- Figure/table organization is logical
- The experimental setup is well-documented

**Weaknesses:**
- The curriculum schedule could be explained more intuitively (a figure showing how operator probabilities change over time would help)
- The choice of thresholds (0.25, 0.5, 0.75) and operator strengths (10% token dropout, 15% synonym replacement, etc.) lacks justification
- Limited discussion of why the reversed curriculum performs so poorly (1.3 points worse)—surprising enough to warrant investigation
- The limitations section is somewhat superficial; deeper discussion of when/why the method might fail would strengthen the paper

## Missing Elements
1. **Significance testing**: P-values or confidence intervals for main comparisons
2. **Fair baseline comparison**: Equal hyperparameter tuning for all methods
3. **Sensitivity analysis**: How sensitive is the method to curriculum schedule design (linear vs. exponential, threshold values)?
4. **Broader evaluation**: Larger models, other tasks, multilingual settings mentioned as limitations but would strengthen the work
5. **Analysis**: Deeper investigation into what the curriculum actually learns (e.g., representation analysis at different stages)

## Minor Issues
- Table 2 lacks error bars for ablation variants
- The mechanism by which easier augmentations help learning could be explained more deeply
- No discussion of variance across seeds in Table 3

## Questions for Authors
1. Why is the reversed curriculum so much worse (1.3 vs. 0.8 point drop)? 
2. How sensitive is performance to the specific threshold values (0.25, 0.5, 0.75)?
3. Did you try exponential or other non-linear schedules?

## Recommendation Justification
This is a solid empirical paper with a simple, practical idea and consistent experimental validation. The method is sound and addresses a relevant problem. However, the novelty is limited (straightforward application of curriculum learning), the improvements are modest (1.1 points, with 0.8 from the curriculum alone), and the evaluation scope is narrow. The work makes an incremental contribution suitable for a workshop or applications track, but falls short of the novelty and significance expected for a top-tier venue.

---

## Final Scores
| Criterion | Score |
|-----------|-------|
| Soundness | 75 |
| Novelty | 65 |
| Significance | 70 |
| Clarity | 82 |
| **Average** | **73** |

## Final Recommendation: **Borderline Accept / Weak Accept**

**Recommendation: ACCEPT** (with reservations)

This paper presents solid empirical work on a practical problem with consistent improvements over baselines. While the novelty is incremental and improvements modest, the method is simple, reproducible, and shows consistent gains, especially in the most relevant low-resource regime. It would be suitable for acceptance at a second-tier venue or a specialized workshop, though it represents an incremental rather than substantial advance.