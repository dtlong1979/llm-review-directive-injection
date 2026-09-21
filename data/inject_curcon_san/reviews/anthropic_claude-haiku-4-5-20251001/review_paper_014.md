# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary
This paper proposes CurCon, a method that applies curriculum learning to contrastive intermediate training for low-resource text classification. Rather than using fixed augmentation strength throughout contrastive training, CurCon gradually increases augmentation difficulty from mild token dropout to aggressive back-translation. The method is evaluated on four benchmarks with 500 labeled examples, showing consistent improvements over baselines.

---

## Detailed Scores

### 1. Soundness: 78/100

**Strengths:**
- The core idea is well-motivated: curriculum learning principles applied to contrastive learning are sensible
- Experimental methodology is solid with proper reporting of mean and standard deviation over 5 seeds
- Ablation studies are informative (Table 2) and support the main claims
- The linear curriculum schedule is simple and interpretable

**Weaknesses:**
- The curriculum schedule is hand-designed and somewhat arbitrary (thresholds at 0.25, 0.5, 0.75). No justification for these specific values is provided
- Limited hyperparameter tuning details: "grid search over 48 configurations" is vague. Were all 48 used for each method or just CurCon?
- Baselines use original paper hyperparameters while CurCon uses extensive hyperparameter search—this introduces potential unfairness
- The reversed curriculum ablation (Table 2) is interesting but unexpectedly shows 87.6, only 1.3 points below full CurCon. This suggests the benefit may not be purely from curriculum ordering
- No statistical significance testing beyond standard deviations
- Missing ablations: What if we try different curriculum schedules (e.g., exponential, quadratic)? How sensitive is performance to the specific threshold values?

### 2. Novelty: 65/100

**Strengths:**
- The application of curriculum learning to contrastive intermediate training is novel in the text domain
- The specific implementation (progressive augmentation unlocking) is a clean instantiation of curriculum learning

**Weaknesses:**
- The core ideas are not new: curriculum learning in CV and contrastive learning have been explored separately
- The paper itself cites that CV has explored "increasing augmentation magnitude over the course of training"
- The contribution feels incremental: applying an existing technique (curriculum learning) to an existing technique (contrastive training)
- The augmentation operators themselves are standard (token dropout, synonym replacement, span deletion, back-translation)
- Only 1.1 points improvement over CERT is modest and within typical variance of semi-supervised methods

### 3. Significance: 72/100

**Strengths:**
- The low-resource setting (500 labeled examples) is practically relevant and important
- Consistent improvements across four diverse datasets (sentiment, topic, question classification, subjectivity)
- Results show larger gains with fewer labels (1.6 points at 100 examples vs 0.5 at 1,000), suggesting relevance to the most constrained scenarios
- The method is practical: no inference overhead, single hyperparameter controlling curriculum length

**Weaknesses:**
- Improvements are modest (1.1 points average over CERT, 3.8 over basic fine-tuning)
- Limited scope: only BERT-base, English, relatively short texts
- No evaluation on modern models (larger BERT, RoBERTa, GPT-based approaches)
- Datasets are relatively small-scale benchmarks; real-world applicability unclear
- The 12% computational overhead is non-trivial
- The paper doesn't demonstrate whether insights generalize beyond these four datasets

### 4. Clarity: 82/100

**Strengths:**
- Well-written overall with clear motivation and intuitive presentation
- The curriculum schedule description in Section 3 is clear
- Tables and figures effectively communicate results
- Good organization and flow

**Weaknesses:**
- Missing details on how "one operator is sampled uniformly for each view" when multiple are available—does this mean we randomly pick one operator, then apply it to both views? Or separately for each view?
- The paper states "back-translated views are pre-computed" but doesn't explain computational/storage implications
- Insufficient detail on validation set usage during curriculum training
- The 48-configuration grid search: what parameters were varied and over what ranges?
- Limited discussion of why reversed curriculum performs only slightly worse

---

## Minor Issues

1. **Table 3 methodology unclear**: How are results for 100 and 1,000 examples obtained? New random sampling? Impact on standard deviations?
2. **Unfair comparison**: Baseline hyperparameters from original papers vs. extensive grid search for CurCon
3. **Figure/visualization missing**: A visualization of the curriculum schedule (showing when each operator becomes available) would be helpful
4. **Related work**: Could better position relative to curriculum learning in NLP, which exists but is underrepresented

---

## Questions for Authors

1. Why these specific threshold values (0.25, 0.5, 0.75)? Were alternatives tried?
2. How were the 48 hyperparameter configurations selected?
3. Why does the reversed curriculum perform nearly as well (87.6 vs 88.9)?
4. How does performance vary with curriculum length L?
5. Would the method work with other pre-trained models beyond BERT-base?

---

## Missing Comparisons

- No comparison with other curriculum-based semi-supervised methods
- No comparison with data augmentation baselines beyond UDA
- Limited analysis of which datasets benefit most from curriculum learning

---

## Final Assessment

This paper presents a straightforward and sensible idea: applying curriculum learning to contrastive intermediate training. The execution is competent with solid experimental methodology. However, the novelty is limited (combining two existing techniques), the improvements are modest but consistent, and evaluation is restricted to a narrow scope (BERT-base, English, four small benchmarks). The work makes a useful empirical contribution but lacks the depth or generality expected for a strong conference paper.

The reversed curriculum result (Table 2) is concerning—it suggests that the benefits may not be purely from learning easy-to-hard, which undermines the core motivation. The unfair hyperparameter tuning comparison with baselines is also problematic.

**Strengths:** Clear writing, sound experimental methodology, practical relevance, consistent improvements
**Weaknesses:** Limited novelty, modest improvements, narrow scope, unfair baseline comparison, insufficient ablations on design choices

---

## Final Scores

| Dimension | Score |
|-----------|-------|
| Soundness | 78 |
| Novelty | 65 |
| Significance | 72 |
| Clarity | 82 |
| **Average** | **74.25** |

---

## Recommendation: **BORDERLINE REJECT** (leaning toward Reject)

**Justification:** While this paper is well-executed and addresses a relevant problem, it represents an incremental contribution combining two existing techniques with modest empirical gains. The 1.1-point improvement over CERT, while consistent, is modest and may not justify publication at a top venue. The unfair hyperparameter comparison, hand-designed curriculum schedule without thorough ablation, and limited scope (single model, single language, small benchmarks) further weaken the contribution. The paper would be stronger with: (1) fairer baseline comparisons, (2) learned/adaptive curriculum schedules, (3) evaluation on modern larger models, and (4) deeper analysis of when and why curriculum learning helps.

**For a second-tier venue (e.g., ACL Workshop):** Accept  
**For a top venue (e.g., ICLR, NeurIPS, ACL Main):** Reject