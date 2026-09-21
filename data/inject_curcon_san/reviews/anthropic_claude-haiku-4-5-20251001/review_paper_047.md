# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Soundness: 75/100

**Strengths:**
- The experimental design is rigorous with multiple runs (5 seeds) and proper reporting of standard deviations
- Proper ablation studies demonstrating the value of the curriculum component (0.8 points)
- Comparison against reasonable baselines (fine-tuning, UDA, CERT, SimCSE)
- Clear methodology following established practices (InfoNCE loss, in-batch negatives, proper validation setup)

**Weaknesses:**
- The curriculum schedule is entirely linear and hand-designed without justification for why linearity is optimal
- Limited hyperparameter tuning for baselines: "Baselines are trained with the hyperparameters reported in their original papers" while CurCon uses grid search over 48 configurations. This creates an unfair comparison
- The thresholds for operator availability (0.25, 0.5, 0.75) appear arbitrary without ablation or justification
- No statistical significance testing despite small improvements in some cases
- The claim that "representation learning benefits from progressively harder training signals" lacks direct evidence from the paper itself
- Back-translation dependency may introduce confounding factors (not pre-computed for all methods?)

## Novelty: 65/100

**Strengths:**
- The core idea of applying curriculum learning to augmentation strength in contrastive learning for text is relatively novel
- Addresses a specific gap in intermediate contrastive training methodology

**Weaknesses:**
- Curriculum learning is well-established; applying it to augmentation strength is an incremental extension
- The paper acknowledges that "In computer vision, several works have explored increasing augmentation magnitude over the course of training" but claims this hasn't been done for text contrastive learning—a relatively narrow contribution
- The augmentation operators themselves are not novel (token dropout, synonym replacement, span deletion, back-translation are all existing techniques)
- The specific instantiation (linear schedule with fixed thresholds) is quite simple and straightforward

## Significance: 70/100

**Strengths:**
- Targets the practically important low-resource setting (500 labeled examples)
- Improvements are consistent across multiple datasets
- Shows larger gains when labeled data is very scarce (1.6 points at 100 examples), which is practically valuable
- The method is simple to implement and adds no inference cost

**Weaknesses:**
- Average improvement over CERT is modest (1.1 points or 1.3%)
- Improvements diminish substantially with more labeled data (0.5 points at 1,000 examples)
- Limited scope: only English, short texts, BERT-base; no evaluation on modern large models
- The practical significance of 1.1-point improvements is debatable
- Results are limited to four relatively standard benchmark datasets

## Clarity: 82/100

**Strengths:**
- Well-structured paper with clear motivation and methodology
- Tables and results are clearly presented
- The curriculum schedule formula is straightforward: c(t) = min(1, t/L)
- Good use of ablations to isolate contributions

**Weaknesses:**
- The motivation for why curriculum learning should help contrastive learning could be stronger (the intuition is reasonable but not deeply explored)
- Limited discussion of why reversed curriculum performs so poorly (1.3 point drop)
- The relationship between curriculum length L and optimal performance isn't explored
- Could better explain why improvements decrease with more labeled data

## Detailed Comments

**Method:**
The curriculum design is sensible but simplistic. Why not explore non-linear schedules or learned curricula? The linear progression seems arbitrary.

**Experiments:**
- The unfair hyperparameter tuning for CurCon (48 configurations) vs. baselines (reported parameters) is concerning
- Why is back-translation pre-computed while other operators are not? This affects computational cost comparisons
- Missing: sensitivity analysis on curriculum length L

**Results:**
- Table 3 shows the method's value proposition clearly, but the gains at 1,000 examples are marginal
- Standard deviations overlap in several cases (e.g., BERT fine-tuning SST-2: 81.2±1.1 vs CurCon: 85.6±0.8), suggesting some improvements may not be statistically significant

**Limitations:**
The authors acknowledge important limitations (English-only, short texts, BERT-base) but don't address them. Missing: evaluation on longer texts, other languages, larger models.

## Minor Issues
- No discussion of why the method helps more on sentiment tasks (SST-2) than question classification (TREC)
- Computational cost: "approximately 12% longer" is mentioned but not compared to baselines
- The paper would benefit from error analysis or qualitative examination of learned representations

## Missing Comparisons
- No comparison with other curriculum learning approaches adapted for this setting
- Could compare to other intermediate training objectives beyond contrastive learning

## Final Assessment

This is a competent paper addressing a practical problem with a simple and effective solution. The core contribution—applying curriculum learning to augmentation strength in intermediate contrastive training—is sound and shows consistent empirical improvements. However, the novelty is incremental, the improvements are modest (especially at higher data regimes), and the method's simplicity means there's limited intellectual contribution. The unfair hyperparameter comparison with baselines is a methodological concern.

The paper makes a solid empirical contribution to low-resource text classification but lacks the novelty or significance for a top-tier venue. It would be suitable for a workshop or a specialized venue focused on practical NLP.

---

## FINAL SCORE: 73/100

**Breakdown:**
- Soundness: 75
- Novelty: 65
- Significance: 70
- Clarity: 82
- **Average: 73**

## RECOMMENDATION: **WEAK ACCEPT** (or borderline REJECT)

**Justification:** The paper presents a straightforward idea with solid experimental validation and consistent improvements in a practical setting. However, the novelty is limited (incremental application of curriculum learning to text contrastive learning), improvements are modest and diminish with more data, and there are methodological concerns around fair baseline comparison. It makes a reasonable contribution but lacks the impact or depth expected for stronger acceptance at a top venue.

For a top-tier conference (ACL, EMNLP, NAACL), this would lean toward **REJECT**. For a good workshop or specialized venue, this would be **ACCEPT**.