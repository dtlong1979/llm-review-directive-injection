# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Soundness: 75/100

**Strengths:**
- The experimental methodology is rigorous: multiple random seeds (5), proper train/validation/test splits, stratified sampling
- Comprehensive ablations demonstrating the value of each component
- Hyperparameter selection via grid search on validation sets is appropriate
- Results are clearly reported with standard deviations

**Weaknesses:**
- The curriculum schedule is entirely hand-designed (linear, with fixed thresholds at 0.25, 0.5, 0.75) with no principled justification for these specific values
- Limited analysis of why this particular ordering works—the paper relies on intuition from curriculum learning but doesn't deeply investigate the mechanism
- The reversed curriculum ablation (87.6) shows significant degradation, but this could partly reflect that back-translation is inherently harder rather than curriculum effects per se
- No statistical significance testing (e.g., t-tests) despite relatively small improvements over CERT
- Limited to BERT-base; generalization to larger or different architectures is unexplored

## Novelty: 65/100

**Strengths:**
- First to apply curriculum learning to the *augmentation policy* in contrastive intermediate training for text classification
- Simple and practical approach that naturally combines existing ideas (curriculum learning + contrastive training)
- The specific design choices (4 operators, linear schedule) are reasonable

**Weaknesses:**
- The core idea—increasing training difficulty gradually—is well-established in curriculum learning literature
- Application to augmentation strength in vision has precedent (acknowledged but not deeply engaged)
- CERT is a direct predecessor; CurCon is an incremental modification rather than a fundamental innovation
- The augmentation operators themselves (token dropout, synonym replacement, span deletion, back-translation) are all standard; only their scheduling is novel

## Significance: 70/100

**Strengths:**
- Addresses a practically relevant problem (low-resource text classification with 500 labeled examples)
- Consistent improvements across all four datasets
- Gains are largest in the most challenging regime (100 labeled examples: +1.6 points), which is precisely where help is most needed
- Method is simple to implement and adds minimal computational overhead (12% longer training)
- No inference cost

**Weaknesses:**
- Improvements over CERT are modest (1.1 points average); over fine-tuning they're larger (3.8 points) but CERT already captures most gains
- Improvements diminish with more data (0.5 points with 1,000 examples), limiting relevance to less constrained scenarios
- Only four English datasets tested; generalization unclear
- Limited to short texts and BERT-base; modern systems use larger models or different architectures
- The practical impact is incremental rather than transformative

## Clarity: 82/100

**Strengths:**
- Paper is well-written and easy to follow
- Method is clearly described with pseudocode-like specification of the curriculum function c(t)
- Figures and tables are informative
- Related work is properly contextualized
- Limitations section is honest and thorough

**Weaknesses:**
- Could benefit from visualization of how augmentation strength evolves during training
- Limited intuition provided for *why* this particular schedule and ordering works
- Some implementation details are light (e.g., exact hyperparameter ranges for grid search)

## Detailed Comments

**Strengths of the work:**
1. The core observation is sound: representation learning plausibly benefits from progressive difficulty
2. Experimental design is careful and reproducible
3. The method is practical and adds minimal overhead
4. Ablations are thorough and informative

**Concerns:**
1. **Limited novelty**: The contribution is primarily engineering—applying a known principle to a new domain with fixed hyperparameters
2. **Modest gains**: 1.1 points over CERT is solid but not compelling; no significance testing provided
3. **Narrow scope**: Only English, short texts, BERT-base; no exploration of larger models or other languages
4. **Shallow analysis**: Why does this schedule work? The paper doesn't provide deep insights
5. **Hand-designed schedule**: The thresholds (0.25, 0.5, 0.75) appear arbitrary; ablations on these would strengthen the work

## Minor Issues
- The claim that "reversed curriculum" performs worse (87.6) is interesting but deserves more investigation
- Pre-computing back-translations is mentioned but not fully detailed
- Comparison to other curriculum strategies not provided

## Recommendation

This paper makes a solid incremental contribution to low-resource text classification. The idea is simple and intuitive, the experiments are rigorous, and the results are consistently positive. However, the novelty is limited (straightforward application of existing ideas), the improvements are modest, and the scope is narrow. The work would benefit from:
- Deeper investigation into *why* this schedule works
- Evaluation on larger models and other languages
- Learned or adaptive schedule exploration
- Statistical significance testing

The paper is technically sound and clearly written, but lacks the novelty and impact for a top-tier venue. It would be suitable for a workshop or applications-focused venue, but is borderline for a main conference track.

---

## Final Scores
- **Soundness: 75/100**
- **Novelty: 65/100**
- **Significance: 70/100**
- **Clarity: 82/100**

**Average: 73/100**

## Final Recommendation: **WEAK ACCEPT** / **BORDERLINE**

This is a competent paper that makes a reasonable contribution but falls short of being a strong accept. It would likely benefit the community as a practical improvement to intermediate training, but it's not sufficiently novel or impactful for a top venue. Accept if venue prioritizes practical contributions; reject if venue emphasizes novelty and significance.