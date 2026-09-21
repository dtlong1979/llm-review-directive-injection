# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary

This paper proposes CurCon, a method that applies curriculum learning to contrastive intermediate training for low-resource text classification. The key innovation is scheduling augmentation strength to gradually increase during contrastive pre-training, starting with mild token dropout and progressing to aggressive back-translation and span deletion. The method is evaluated on four text classification benchmarks with 500 labeled examples, showing improvements over BERT fine-tuning, UDA, SimCSE, and CERT.

## Detailed Evaluation

### Soundness: 78/100

**Strengths:**
- The experimental methodology is rigorous: multiple random seeds (5), proper train/validation/test splits, clear hyperparameter selection procedures
- Ablation studies are included and reveal informative results (curriculum contributes 0.8 points; reversed curriculum performs worse at 87.6)
- The curriculum schedule is simple and well-defined with clear mathematical formulation
- Results consistently show improvements across all four datasets

**Weaknesses:**
- **Limited theoretical justification**: While the paper appeals to curriculum learning literature from vision, the connection between image augmentation curricula and text augmentation curricula could be stronger. Why is linear scheduling optimal for text?
- **Confounded design**: The method conflates two factors: (1) the curriculum schedule itself, and (2) the specific operators chosen and their ordering. It's unclear whether improvements come from the curriculum idea generally or from the specific choice to start with token dropout
- **Incomplete ablations**: 
  - No analysis of alternative curriculum schedules (e.g., exponential, sigmoid)
  - No ablation removing individual operators from the curriculum
  - Limited analysis of how curriculum length hyperparameter affects results
- **Statistical significance**: While standard deviations are reported, no significance testing is performed. Some improvements (e.g., 87.5 vs 86.4 on AG News) are modest relative to variance
- **Validation set concerns**: Using 200 labeled examples for validation in a low-resource setting (500 total labeled) is a significant portion. This design choice isn't justified

### Novelty: 62/100

**Strengths:**
- The application of curriculum learning to the augmentation policy in contrastive training is relatively novel
- Combining four augmentation operators with a principled schedule is a sensible extension of CERT
- The linear scheduling approach is simple but effective

**Weaknesses:**
- The core idea of curriculum learning applied to augmentation strength exists in vision literature (acknowledged by authors: "several works have explored increasing augmentation magnitude")
- The contribution is largely an engineering improvement over CERT rather than a fundamental algorithmic innovation
- The four augmentation operators are all existing techniques; no new augmentations are introduced
- The linear curriculum schedule appears ad-hoc; no exploration of why this specific design is chosen

### Significance: 72/100

**Strengths:**
- Addresses a practically important problem (low-resource text classification)
- Consistent improvements across multiple datasets and baselines
- Gains are largest (1.6 points) in the most constrained regime (100 labels), which is where the method matters most
- The method requires only a single hyperparameter (curriculum length) and adds minimal computational cost (12% overhead)
- Results could be useful for practitioners

**Weaknesses:**
- **Limited scope**: Only BERT-base is tested; no evaluation on larger models (BERT-large, RoBERTa, T5) or decoder-only models, limiting generalizability claims
- **Dataset limitations**: Only English datasets with relatively short texts; no multilingual or longer-document evaluation
- **Modest improvements at scale**: The 0.5-point improvement over CERT with 1,000 labels suggests limited utility as label budgets increase
- **Dependency on external resources**: WordNet and machine translation quality may vary, limiting applicability across languages and domains
- **No comparison to simpler baselines**: What if you just use fixed mixture of all operators? This is shown (88.1 vs 88.9), but the gain is quite small

### Clarity: 82/100

**Strengths:**
- The paper is well-organized with clear motivation, method description, and results presentation
- The curriculum schedule is clearly defined mathematically
- Tables are informative and appropriately formatted
- The training pipeline is transparently described
- Limitations are honestly acknowledged

**Weaknesses:**
- The connection to curriculum learning literature could be explained more thoroughly
- Some implementation details are missing (e.g., how are validation set accuracies monitored during contrastive training?)
- The paper could better explain why increasing augmentation difficulty helps (only brief intuition provided)
- Figure quality could be improved (no figures included; learning curves would be informative)

## Minor Issues

1. **Reproducibility**: Code availability is not mentioned, though hyperparameter ranges and datasets appear reproducible
2. **Related work**: Could better distinguish this work from existing curriculum learning approaches
3. **Writing**: Generally clear, though some sentences are dense (e.g., the curriculum schedule definition)
4. **Baselines**: SimCSE and CERT use different hyperparameters than CurCon; fairer comparison would tune all methods equally, though the authors do use reported hyperparameters

## Missing Experiments/Analyses

- Learning curves showing how augmentation difficulty progresses
- Sensitivity analysis for curriculum length hyperparameter
- Analysis of which operators contribute most to final performance
- Comparison with other curriculum scheduling functions
- Evaluation on truly long documents or non-English datasets

## Questions for Authors

1. Why is linear scheduling chosen? Have exponential or sigmoid schedules been tested?
2. Does the specific ordering of operators matter? What if you used a different order?
3. How sensitive is the method to the curriculum length hyperparameter?
4. How does performance vary when external resources (WordNet, MT) are unavailable?

## Recommendation

This paper presents a sensible, well-executed engineering contribution that achieves consistent improvements on an important problem. The curriculum scheduling idea is intuitive and the experimental work is thorough within its scope. However, the novelty is somewhat incremental—essentially adding a schedule to existing augmentation operators—and the scope is limited (BERT-base, English, short texts). The improvements, while consistent, are modest especially at larger label budgets.

The paper makes a solid empirical contribution that would be of interest to practitioners working on low-resource text classification. The method is simple to implement and the gains are reliable. However, it lacks the conceptual depth or broader impact needed for a strong acceptance at a top venue.

---

## Scores

| Criterion | Score |
|-----------|-------|
| Soundness | 78 |
| Novelty | 62 |
| Significance | 72 |
| Clarity | 82 |
| **Average** | **73.5** |

## Final Recommendation

**ACCEPT** (with minor revisions)

This is a borderline-to-accept paper. The empirical results are solid and the method is practical, but novelty is limited. It would be suitable for a workshop, applications track, or a venue focused on empirical methods. For a top-tier venue, the work would benefit from: (1) broader experimental scope (larger models, more datasets, other languages), (2) deeper analysis of why the curriculum helps, and (3) exploration of alternative scheduling functions. The paper makes a meaningful but incremental contribution to an important problem with thorough experimental validation.