# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Soundness: 75/100

**Strengths:**
- The experimental methodology is rigorous: results are averaged over 5 random seeds with standard deviations reported
- The ablation study (Table 2) effectively validates key design choices
- The curriculum design is intuitive and well-motivated from curriculum learning literature
- Hyperparameter selection via grid search is appropriate

**Weaknesses:**
- The improvement of 0.8 points from the curriculum (Table 2) is modest in absolute terms and within typical variance ranges for NLP
- The reversed curriculum experiment (1.3 point drop) is encouraging but limited to a single reverse order—more curriculum variants could strengthen the claims
- The linear curriculum schedule is presented as fixed; no justification for this particular design is provided beyond intuition
- Potential confound: the ablation uses L=0 which mixes all operators uniformly, but doesn't test a non-curriculum version with operators added gradually in a non-curriculum manner
- The cost analysis (12% slowdown) is mentioned but not thoroughly analyzed

## Novelty: 65/100

**Strengths:**
- Applying curriculum learning to augmentation strength in contrastive learning for text is a reasonable extension
- The progressive operator scheduling (token dropout → synonym replacement → span deletion → back-translation) is a sensible design
- This specific combination hasn't been explored before in this setting

**Weaknesses:**
- The core idea of curriculum learning is well-established (acknowledged in Section 2)
- Applying it to augmentation in vision has been explored (mentioned in Related Work)
- The contribution is essentially adapting an existing paradigm to text contrastive learning—incremental rather than fundamental
- The method is straightforward: a linear schedule controlling when different operators become available
- Limited novelty in the actual augmentation operators used (all standard techniques)

## Significance: 70/100

**Strengths:**
- Low-resource text classification is practically important
- Results show consistent improvements across all four datasets
- The improvement is largest when data is scarcest (1.6 points at 100 examples, Table 3), which is the most relevant regime
- The method is simple and broadly applicable
- No additional inference cost makes deployment practical

**Weaknesses:**
- Absolute improvements are modest (1.1 points over CERT, 3.8 over baseline fine-tuning)
- Gains diminish substantially with more labels (0.5 points at 1,000 examples)
- Limited to 500 labelled examples as the primary focus; most realistic low-resource scenarios have even fewer labels or fewer datasets evaluated
- Evaluation is restricted to 4 relatively simple, well-studied English datasets
- No evaluation on other languages or significantly different domains
- Improvements over CERT (the closest competitor) are not dramatic

## Clarity: 82/100

**Strengths:**
- Well-structured paper with clear motivation and methodology
- The curriculum schedule is formally defined (c(t) = min(1, t/L)) and easy to understand
- Tables are informative and well-presented
- The writing is generally clear and accessible
- Good use of comparisons to related work

**Weaknesses:**
- The "curriculum length L" hyperparameter is introduced but its selection process (grid search) feels disconnected from the curriculum concept itself
- Limited discussion of why specific operator thresholds (0.25, 0.5, 0.75) were chosen
- The projection head architecture is mentioned briefly but not detailed
- Some experimental details relegated to brief mentions (e.g., "early stopping on validation set")
- No visualization of what happens at different curriculum stages

## Detailed Comments

### Positive Aspects:
1. **Solid empirical validation**: Multiple datasets, multiple baselines, proper statistical reporting
2. **Practical method**: Simple to implement, no inference overhead
3. **Well-motivated**: Curriculum learning is a reasonable principle to apply here
4. **Reproducibility**: Clear description of hyperparameters and training procedure

### Concerns:
1. **Modest improvements**: The curriculum contributes ~0.8 points; while consistent, this is not substantial
2. **Limited scope**: English, short texts, BERT-base only; generalization unclear
3. **Hyperparameter sensitivity**: The method introduces curriculum length as a new hyperparameter requiring tuning
4. **Baseline concerns**: CERT is the main comparison, but even the improvement over it is modest
5. **Theoretical justification**: Why should *linear* scheduling be optimal? No adaptive methods explored

## Missing Experiments/Analysis:
- Analysis of what curriculum length values are selected (does it vary by dataset?)
- Sensitivity analysis on curriculum length
- Comparison of different schedule shapes (linear vs. exponential vs. sigmoid)
- Analysis of which augmentations contribute most
- Experiments with other encoders (RoBERTa, ALBERT, etc.)

## Overall Assessment

This paper presents a straightforward and practical approach to improving low-resource text classification by applying curriculum learning principles to contrastive intermediate training. The work is technically sound and empirically validated, with consistent improvements across datasets. However, the novelty is limited (curriculum learning applied to augmentation in text), the absolute improvements are modest (0.8 points from curriculum, 1.1 over CERT), and the evaluation is restricted in scope.

The paper makes a reasonable contribution to an important problem, but the incremental nature of the work and modest empirical gains limit its impact. It represents solid empirical work rather than a significant methodological advance.

---

## Final Scores:
- **Soundness: 75**
- **Novelty: 65**
- **Significance: 70**
- **Clarity: 82**

## Average Score: **(75 + 65 + 70 + 82) / 4 = 73/100**

## Recommendation: **Weak Accept**

This paper makes a reasonable contribution with solid empirical validation, but the novelty is limited and improvements are modest. It would be suitable for a workshop or second-tier venue, but is borderline for a top-tier conference. The consistency of results and practical applicability push it slightly toward acceptance, though the limited scope and incremental nature are concerns. The work would be strengthened by broader evaluation, deeper analysis of the curriculum design choices, and investigation of adaptive scheduling approaches.