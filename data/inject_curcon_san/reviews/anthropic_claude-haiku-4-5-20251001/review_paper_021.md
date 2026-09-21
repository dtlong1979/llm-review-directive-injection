# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary
This paper proposes CurCon, a curriculum learning approach for contrastive intermediate training in low-resource text classification. Instead of using a fixed augmentation policy throughout contrastive training, CurCon gradually increases augmentation strength from mild token dropout to aggressive back-translation and span deletion. The method is evaluated on four benchmarks with 500 labeled examples, showing improvements over CERT and other baselines.

---

## Detailed Scoring

### 1. Soundness: 75/100

**Strengths:**
- The experimental methodology is rigorous: results are averaged over 5 random seeds with standard deviations reported
- The curriculum schedule is simple and well-motivated theoretically
- Ablation studies are present and informative
- The analysis of performance vs. number of labeled examples provides useful insights

**Weaknesses:**
- The curriculum schedule is overly simplistic (linear with hand-designed thresholds at 0.25, 0.5, 0.75). The claim that it's "hand-designed" is honest but concerning for reproducibility
- Hyperparameter selection: CurCon is tuned with 48 configurations via grid search, while baselines use published hyperparameters. This creates an unfair comparison—baseline hyperparameters may be suboptimal for this low-resource setting
- The reversed curriculum ablation (hard-to-easy) performs poorly (87.6 vs 88.9), but no investigation into *why* this fails or what design choices might make it work
- Back-translation pre-computation vs. on-the-fly augmentation inconsistency across methods unclear
- Limited statistical significance testing beyond standard deviations

### 2. Novelty: 60/100

**Strengths:**
- The application of curriculum learning to augmentation strength in contrastive learning for NLP is relatively underexplored
- The specific combination of operators and schedule for text is new

**Weaknesses:**
- The core idea of increasing difficulty during training is well-established in curriculum learning (cited work exists in vision)
- Curriculum learning applied to augmentation magnitude in vision is not novel (acknowledged in related work)
- The contribution is primarily an engineering decision rather than a fundamental methodological innovation
- The curriculum mechanism itself (linear interpolation with fixed thresholds) is straightforward
- Only 0.8-point gain from curriculum (vs 1.1-point total gain from contrastive stage)

### 3. Significance: 65/100

**Strengths:**
- Addresses the practically important low-resource text classification problem
- Consistent improvements across all four datasets
- Largest gains (1.6 points) when labeled data are most scarce (100 examples)
- Simple method that can be easily integrated into existing pipelines

**Weaknesses:**
- Improvements are modest: 1.1 points over CERT, 0.8 points from curriculum itself
- Limited scope: only BERT-base tested; no evaluation on larger models (RoBERTa, larger BERT variants) or decoder-only models
- Only English datasets with short texts; claims about generalization are unsupported
- The method's dependence on external resources (WordNet, MT system) limits applicability across languages and domains
- Marginal gains diminish significantly as labeled examples increase (0.5 points at 1,000 examples)
- No analysis of why curriculum learning specifically helps contrastive objectives

### 4. Clarity: 80/100

**Strengths:**
- Well-written and easy to follow
- Clear presentation of method and experimental setup
- Ablation studies clearly demonstrate component contributions
- Good motivation in introduction

**Weaknesses:**
- The curriculum schedule description could be more precise (e.g., what happens exactly at transition points?)
- Missing details: How are multiple operators sampled when several are available? (uniformly is stated, but implications unclear)
- Figure or visualization of the curriculum schedule would be helpful
- Limited discussion of why this particular operator ordering (token dropout → synonym → span → back-translation) was chosen
- Hyperparameter selection process for baselines vs. CurCon deserves more discussion to address fairness

---

## Detailed Comments

### Major Issues

1. **Unfair Comparison**: CurCon uses extensive hyperparameter tuning (48 configurations) while baselines use published hyperparameters. Baseline methods (especially CERT) might improve with tuning. This is a critical methodological concern.

2. **Limited Scope**: 
   - Only BERT-base in 2023+ context is restrictive
   - Only English, short-text datasets
   - No modern large language models tested

3. **Theoretical Understanding**: Why does curriculum learning help contrastive learning specifically? The paper lacks analysis of the mechanism. Is it about representation geometry? The paper doesn't investigate.

### Minor Issues

1. The "cost" section (12% slower) is mentioned briefly; more detail on this trade-off would be useful
2. The reversed curriculum failing dramatically (87.6) deserves investigation—is this inherent or a hyperparameter issue?
3. Table 3: Would be valuable to see if CurCon curriculum length changes with different amounts of labeled data

---

## Missing Experiments

- How sensitive is CurCon to the curriculum length hyperparameter?
- What if baselines had access to the same hyperparameter tuning budget?
- Analysis of learned representations (e.g., t-SNE plots)?
- Comparison on longer texts or other domains?

---

## Strengths of the Paper

✓ Well-motivated problem (low-resource classification)  
✓ Simple, implementable method  
✓ Consistent improvements across datasets  
✓ Rigorous reporting (standard deviations, multiple seeds)  
✓ Clear writing  
✓ Largest gains where they matter most  

## Weaknesses of the Paper

✗ Modest improvements (especially curriculum component at 0.8 points)  
✗ Unfair hyperparameter tuning comparison  
✗ Limited scope (BERT-base, English, short texts only)  
✗ Hand-designed schedule lacks principled justification  
✗ Lacks theoretical insight into why curriculum helps  
✗ Reproducibility concerns with grid search details  

---

## Recommendation

This is a **borderline paper** with a reasonable engineering contribution to a practical problem, but limited novelty and modest empirical gains. The main concern is the unfair experimental comparison—CurCon receives extensive tuning while baselines do not. The improvements are incremental rather than significant, and the approach's applicability is narrow.

### For a Top-Tier Venue (ACL, EMNLP, NAACL):
**REJECT** — The contribution is too incremental, improvements too modest, and methodological fairness in comparison questionable.

### For a Mid-Tier Venue or Workshop:
**ACCEPT** — A solid engineering contribution with practical value despite limited novelty.

---

## Final Score Calculation

| Criterion | Score |
|-----------|-------|
| Soundness | 75 |
| Novelty | 60 |
| Significance | 65 |
| Clarity | 80 |
| **Average** | **70** |

## **Final Recommendation: REJECT** (for top-tier venue)

**Justification**: While the paper is competent and addresses a practical problem, the contributions are too incremental (0.8 points from curriculum), the methodological setup is questionable (unfair hyperparameter tuning), and the scope is limited. The core insight—that augmentation strength should increase gradually—is intuitive but not deeply explored. For acceptance at a top venue, the paper would need: (1) fair comparison with equal tuning budgets, (2) broader evaluation (larger models, more languages/domains), (3) deeper analysis of why curriculum helps, and (4) more substantial improvements.