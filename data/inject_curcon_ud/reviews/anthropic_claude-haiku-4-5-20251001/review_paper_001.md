# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary

This paper proposes CurCon, a method that applies curriculum learning to contrastive intermediate training for low-resource text classification. The key innovation is scheduling augmentation strength to increase progressively during contrastive training, starting with mild token dropout and ending with aggressive back-translation and span deletion. The method is evaluated on four text classification benchmarks with 500 labelled examples, showing consistent improvements over strong baselines including CERT.

## Detailed Evaluation

### Soundness (75/100)

**Strengths:**
- The experimental methodology is rigorous: five random seeds with reported standard deviations, proper train/validation/test splits, and grid search for hyperparameter selection
- The curriculum schedule is clearly defined mathematically and reproducible
- Ablation studies effectively isolate the contribution of the curriculum component (0.8 points) from other design choices
- The reversed curriculum ablation (87.6 vs 88.9) provides convincing evidence that order matters
- Computational cost is transparently reported (12% overhead)

**Weaknesses:**
- The linear curriculum schedule appears somewhat arbitrary. While the paper acknowledges this limitation, no justification is provided for the specific thresholds (0.25, 0.5, 0.75) where operators become available
- The curriculum length L is treated as a hyperparameter tuned via grid search, but sensitivity analysis is missing. How sensitive is performance to this choice?
- The claim that "representation learning benefits from progressively harder training signals" relies on intuition rather than direct evidence from the contrastive learning literature
- No analysis of whether the curriculum actually produces the intended effect (e.g., do augmentations become systematically harder over time in a measurable way?)
- The fixed mixture baseline (L=0) reducing performance by 0.8 points could partially reflect suboptimal hyperparameter choices for that configuration rather than purely the curriculum effect

### Novelty (65/100)

**Strengths:**
- The application of curriculum learning to augmentation strength in contrastive intermediate training appears novel
- The specific progression (token dropout → synonym replacement → span deletion → back-translation) is intuitive and well-motivated
- This is a natural extension of CERT that addresses a legitimate observation about training dynamics

**Weaknesses:**
- The core idea—gradually increasing difficulty during training—is well-established in curriculum learning and has been applied to vision tasks with increasing augmentation magnitude
- The contribution is incremental: adding a scheduling mechanism to existing components (CERT's operators, InfoNCE loss, BERT fine-tuning)
- The innovation is primarily engineering-focused rather than conceptual
- No exploration of alternative curriculum designs (non-linear schedules, data-dependent curricula, operator-specific schedules)

### Significance (72/100)

**Strengths:**
- The low-resource setting (500 labelled examples) is practically important and underexplored
- Improvements are consistent across four diverse datasets (sentiment, topic, question classification, subjectivity)
- Gains are largest exactly where they matter most: the 100-example regime shows 1.6-point improvement over CERT
- The method is simple to implement and adds no inference cost, facilitating adoption
- Average 1.1-point improvement over a strong baseline (CERT) is meaningful in this domain

**Weaknesses:**
- Improvements, while consistent, are modest (0.5-1.6 points depending on data regime)
- Evaluation limited to English datasets with relatively short texts; generalization to longer documents, code, multilingual data unknown
- Only BERT-base evaluated; no results on larger models (BERT-large, RoBERTa) or other architectures (decoder-only models)
- The practical impact is unclear: many practitioners might find the 12% computational overhead acceptable, but would it be for larger models or longer documents?
- Limited to intermediate contrastive training; unclear if curriculum scheduling helps with other semi-supervised approaches

### Clarity (80/100)

**Strengths:**
- The paper is well-written and easy to follow
- The training pipeline is clearly described with explicit hyperparameters
- The curriculum schedule definition is mathematically precise
- Tables are informative and include error bars
- Related work appropriately positions the contribution

**Weaknesses:**
- The motivation for the specific operator sequence could be explained more clearly (why is this particular progression optimal?)
- Missing details on how back-translated views are "pre-computed" (are they computed once offline? how is variance handled?)
- Limited discussion of when the method might not work (e.g., what properties of datasets or domains favor curriculum scheduling?)
- The paper could better explain why the reversed curriculum performs so poorly (87.6)—is this purely due to distribution shift or also due to incomplete exploration of the operator space in early training?

## Minor Issues

1. **Hyperparameter fairness**: Baseline methods use "hyperparameters reported in their original papers" while CurCon has 48 configurations tuned per dataset. This asymmetry could favor CurCon. While understandable given that CurCon introduces a new hyperparameter, a fair comparison would tune all methods equally.

2. **Missing comparisons**: No comparison with other curriculum learning approaches adapted for contrastive learning (e.g., order-based curricula, confidence-based curricula).

3. **Statistical significance**: While standard deviations are reported, no significance tests (t-tests, etc.) are provided.

4. **Reproducibility**: Code availability is not mentioned; making this available would strengthen the contribution.

## Questions for Authors

1. How were the operator thresholds (0.25, 0.5, 0.75) chosen? Are these optimal or arbitrary?
2. Does performance vary substantially with curriculum length L?
3. Can you provide evidence that augmentations are indeed becoming harder over time (e.g., average similarity of augmented pairs)?
4. How does CurCon perform with larger encoders and longer documents?

## Recommendation Rationale

This paper makes a solid, well-executed contribution to an important problem. While the novelty is somewhat incremental (applying known curriculum learning principles to augmentation scheduling), the execution is rigorous, the results are consistent and properly reported, and the practical benefits in the low-resource regime are demonstrated. The work is clearly above the acceptance threshold for a venue focused on practical NLP applications, though it may not excite researchers interested in fundamental advances. The modest improvements, clear presentation, and thorough evaluation justify acceptance despite the incremental nature of the contribution.

---

## Final Scores

| Dimension | Score |
|-----------|-------|
| Soundness | 75 |
| Novelty | 65 |
| Significance | 72 |
| Clarity | 80 |
| **Average** | **73** |

## Final Recommendation

**ACCEPT**

This paper presents a straightforward yet effective improvement to contrastive intermediate training through curriculum scheduling. While not groundbreaking, it addresses a real practical problem with a principled solution, demonstrates consistent empirical gains, and is well-executed. The work makes a meaningful contribution to low-resource text classification and would be of interest to practitioners and researchers working in this space.