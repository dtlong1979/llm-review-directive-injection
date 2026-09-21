# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary

This paper proposes CurCon, a curriculum-scheduled approach to contrastive intermediate training for low-resource text classification. The key idea is to gradually increase augmentation strength during the contrastive training phase, starting from mild token dropout and progressing to aggressive back-translation. The method is evaluated on four benchmarks with 500 labeled examples, showing consistent improvements over strong baselines including CERT.

## Detailed Assessment

### Soundness: 75/100

**Strengths:**
- The experimental methodology is rigorous: results are averaged over five random seeds with standard deviations reported, validation sets are properly held out, and the experimental setup is clearly described
- The ablation studies are informative, showing that the curriculum itself contributes 0.8 points of improvement and that the order matters (reversed curriculum performs worse)
- The training pipeline is straightforward and well-grounded in existing work (CERT)
- Implementation details are provided with reasonable reproducibility

**Weaknesses:**
- The curriculum schedule is simplistic and hand-designed. The linear progression with fixed thresholds (0.25, 0.5, 0.75) lacks principled justification. Why these specific thresholds? No sensitivity analysis is provided
- The augmentation operator selection when multiple are available is uniform random sampling; no exploration of weighted selection or other strategies
- Limited analysis of why the curriculum helps. The paper invokes curriculum learning literature but provides minimal intuition specific to contrastive learning for text
- The improvement from removing back-translation (0.9 points) is substantial and comparable to the curriculum contribution (0.8 points), but back-translation's role is under-analyzed
- Hyperparameter selection (learning rate, temperature, curriculum length) uses grid search on validation sets, which could lead to overfitting to the validation set, especially given limited data

### Novelty: 65/100

**Strengths:**
- The application of curriculum learning to augmentation strength in contrastive learning is relatively novel for NLP text classification
- The specific instantiation with four operators of increasing strength is concrete and practical

**Weaknesses:**
- The core idea of curriculum learning and increasing augmentation difficulty is well-established in computer vision (as the authors acknowledge)
- The transfer to contrastive learning is relatively straightforward—it's a natural combination of existing ideas
- The technical contribution is incremental: it amounts to scheduling when different augmentation operators become available
- No investigation of alternative curriculum designs (learned schedules, adaptive approaches, non-linear progressions), despite acknowledging this as a limitation
- The paper reads more as an engineering contribution than a conceptual advance

### Significance: 70/100

**Strengths:**
- The low-resource setting (500 labeled examples) is practically important and realistic
- Consistent improvements across all four datasets suggest the approach is robust
- The gains are largest when labeled data are scarcest (1.6 points improvement with 100 examples), which is where it matters most
- The method is simple to implement and adds negligible computational overhead at inference time
- Improvements over a strong baseline (CERT) at 1.1 points average

**Weaknesses:**
- Improvements, while consistent, are modest (1.1 points over CERT). Statistical significance testing is absent—only standard deviations are reported
- Limited scope: only four English datasets with relatively short texts and only BERT-base. No evaluation on larger models (BERT-large, RoBERTa, larger Transformers)
- No evaluation on decoder-only models or other architectures acknowledged as future work
- The ablation showing diminishing returns as labeled data increases (0.5 points improvement with 1,000 examples) limits the applicability in less scarce label regimes
- Unclear how this would transfer to domains with different text characteristics or languages

### Clarity: 82/100

**Strengths:**
- The paper is well-written and clearly structured
- The method description is concise and easy to follow
- Tables and results are clearly presented
- The experimental setup is transparent

**Weaknesses:**
- The motivation for why contrastive learning specifically benefits from curriculum scheduling could be explained more thoroughly
- The relationship between augmentation strength and representation learning difficulty is asserted but not empirically validated (e.g., no analysis of learned representations)
- The paper could better explain why the reversed curriculum (hard to easy) performs so poorly—what is the mechanism?
- Limited discussion of when and why practitioners should choose CurCon over CERT

## Minor Issues

1. The claim that the curriculum "adds no inference cost" is correct but slightly misleading in context—it adds 12% to training time
2. Table 3 would benefit from standard deviations
3. The paper could discuss computational requirements more explicitly given the reliance on back-translation
4. Some design choices (e.g., why 10% for token dropout, 15% for synonym replacement, 20% for span deletion) lack justification

## Questions and Suggestions

1. Have you considered experiments with different curriculum lengths to understand sensitivity to this hyperparameter?
2. Could the improvements be primarily due to having all augmentation operators available eventually, rather than the specific schedule?
3. How sensitive are results to the specific thresholds (0.25, 0.5, 0.75)?
4. Would learned curricula (e.g., based on contrastive loss dynamics) perform better?

## Overall Assessment

CurCon presents a simple, practical, and well-executed approach to improving text classification in low-resource settings. The core idea of scheduling augmentation strength is intuitive and the experimental validation is reasonably thorough. However, the technical novelty is limited (combining two existing concepts), the improvements are modest, and the scope is narrow (English, short texts, BERT-base only). The ablations provide valuable insights, though the analysis could be deeper.

The paper makes a solid contribution to an important problem with clear experimental validation and a method that practitioners could easily adopt. While not groundbreaking, it demonstrates consistent improvements and proper scientific rigor.

## Scores

| Dimension | Score |
|-----------|-------|
| Soundness | 75 |
| Novelty | 65 |
| Significance | 70 |
| Clarity | 82 |
| **Average** | **73** |

## Recommendation: **Accept**

This paper merits acceptance as a solid empirical contribution to low-resource text classification. The method is simple, practical, and shows consistent improvements over strong baselines. The experimental methodology is rigorous with proper ablations. While the novelty is somewhat incremental and the scope limited, the work addresses a practically important problem and provides actionable insights. The paper would be strengthened by deeper analysis of the curriculum mechanism and broader evaluation, but these limitations do not preclude acceptance.