# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary

This paper proposes CurCon, a curriculum-scheduled approach to contrastive intermediate training for low-resource text classification. The key contribution is scheduling augmentation strength (from mild token dropout to aggressive back-translation) during the contrastive pre-training phase rather than using a fixed augmentation policy. The method is evaluated on four benchmarks with 500 labeled examples, showing consistent improvements over strong baselines including CERT.

---

## Detailed Evaluation

### Soundness (78/100)

**Strengths:**
- The core hypothesis is well-motivated: curriculum learning principles from both vision and NLP suggest that gradually increasing difficulty improves representation learning
- The experimental methodology is solid with proper evaluation over 5 random seeds, standard deviation reporting, and appropriate validation/test splits
- The implementation details are clearly specified, enabling reproducibility
- Ablation studies validate key design choices (curriculum vs. fixed mixture, forward vs. reversed curriculum)

**Weaknesses:**
- The curriculum schedule is entirely hand-designed (linear progression with fixed thresholds at 0.25, 0.5, 0.75). No justification is provided for these specific breakpoints, nor is their sensitivity explored
- Limited analysis of *why* the curriculum works. The paper doesn't investigate whether improvements come from: (a) avoiding overfitting to weak augmentations early, (b) gradual adaptation, or (c) simply ensuring harder augmentations are used at all
- The reversed curriculum ablation (Table 2) shows only 1.3-point degradation, which deserves deeper investigation. Why isn't the performance gap larger if the curriculum order is truly critical?
- Hyperparameter selection via grid search on validation sets, while standard, involves searching over curriculum length L alongside learning rate and temperature. The interaction effects aren't fully characterized

### Novelty (68/100)

**Strengths:**
- The specific application of curriculum learning to augmentation strength in contrastive intermediate training is novel and well-executed
- The contribution is focused and incremental in the right way—extending CERT with a principled scheduling mechanism

**Weaknesses:**
- Curriculum learning itself is well-established; the contribution is primarily an application to a specific setting
- The augmentation operators are borrowed from prior work (EDA, back-translation); only their scheduling is new
- The idea of increasing augmentation difficulty during training has been explored in vision (acknowledged by authors); the text-specific contribution is incremental
- No algorithmic innovation—the method is straightforward application of existing concepts

### Significance (74/100)

**Strengths:**
- Addresses a practically important problem: low-resource text classification is common in industry
- Consistent improvements across all four datasets with proper significance testing (standard deviations reported)
- The method is simple and generalizable; requires no architectural changes
- Clear practical value: 1.1-point improvement over CERT, 3.8 points over baseline fine-tuning
- Particularly valuable in the 100-example regime (1.6-point improvement), where label scarcity is most severe
- No inference overhead; adds only ~12% to contrastive training time

**Weaknesses:**
- Limited scope: only four English datasets with short texts; only BERT-base evaluated
- The absolute improvements, while consistent, are modest (0.8–1.1 points over the strong CERT baseline on the 500-example setting)
- No evaluation on larger models (BERT-large, RoBERTa) or decoder-only architectures (GPT-style), limiting generalizability claims
- Results are specific to the low-resource regime; unclear how the method scales to realistic settings with more labels
- The multilingual generalization is questionable given dependence on WordNet and German back-translation

### Clarity (82/100)

**Strengths:**
- The paper is well-written and easy to follow
- Method description is concise yet complete; the curriculum scheduling is explained clearly
- Tables and ablations effectively communicate results
- The motivation is articulated well in the introduction

**Weaknesses:**
- The curriculum schedule definition could be more intuitive. The threshold values (0.25, 0.5, 0.75) appear somewhat arbitrary
- Limited discussion of why certain augmentation strengths are paired with specific curriculum levels
- The reversed curriculum ablation deserves more analysis—only one sentence addresses why it performs worse
- Missing visualizations or analysis of how the probability distributions over operators change during training

### Detailed Comments

1. **Curriculum Design:** The linear schedule with fixed thresholds is reasonable but lacks principled justification. Have the authors considered: adaptive schedules based on loss dynamics, learned schedules, or sensitivity analysis on the threshold values?

2. **Augmentation Quality:** The paper doesn't verify that the four operators genuinely form an increasing difficulty spectrum. Do back-translations actually create harder positive pairs than span deletion? This could be validated empirically.

3. **Hyperparameter Search:** Grid search over 48 configurations per dataset is substantial. Was this performed for baseline methods equally, or only for CurCon? If only for CurCon, the comparison may be slightly unfair.

4. **Generalization:** The claim about "largest gains when fewer labelled examples" (Table 3) is important but only shown for two comparison methods at three data points. This deserves broader validation across more dataset sizes.

5. **Cost Analysis:** The 12% overhead is acceptable, but computational cost scales with contrastive training duration (20,000 steps). For practitioners with limited compute, this should be discussed.

---

## Minor Issues

- Line breaks and formatting in places could be tightened
- The "Limitations" section is honest but brief; expansion on directions (multilingual, larger models) would strengthen it
- Some notation (c(t), L) could be introduced more formally

---

## Missing Comparisons

The paper doesn't compare against other recent semi-supervised or low-resource methods from 2022–2023, though this may reflect submission timing. The baselines chosen (UDA, SimCSE, CERT) are appropriate and strong.

---

## Questions for Authors

1. How sensitive are results to the specific threshold values (0.25, 0.5, 0.75)?
2. Can you provide empirical evidence that back-translation creates harder positive pairs than span deletion?
3. Why is the reversed curriculum only 1.3 points worse? What does this imply about curriculum necessity?
4. How does the method perform on longer documents or other domains (biomedical, legal)?

---

## Overall Assessment

**Strengths:**
- Solid experimental work with proper statistical reporting
- Simple, practical method that consistently improves a strong baseline
- Clear writing and reproducible setup
- Addresses a real problem in low-resource settings

**Weaknesses:**
- Limited novelty (application of established curriculum learning to augmentation scheduling)
- Modest improvements in the main setting (500 examples)
- Narrow evaluation scope (English, short texts, BERT-base only)
- Hand-designed curriculum without principled justification or sensitivity analysis

---

## Recommendation

This paper makes a focused, incremental but solid contribution to an important problem. The experimental work is rigorous, results are consistent across datasets, and the method is practical. While the novelty is limited and improvements are modest in absolute terms, the consistency of gains and their magnitude in low-resource settings (100 examples) provide value to practitioners. The ablations validate the approach, and the writing is clear.

The paper merits acceptance at a workshop or applications-focused venue, and with minor revisions addressing curriculum design justification and broader evaluation, it would be suitable for a main conference track.

---

## Scores

| Dimension | Score |
|-----------|-------|
| Soundness | 78 |
| Novelty | 68 |
| Significance | 74 |
| Clarity | 82 |
| **Average** | **75.5** |

## Final Recommendation

**Accept** — This paper presents a well-executed, practical improvement to intermediate contrastive training for low-resource text classification. While not groundbreaking in novelty, the curriculum-scheduled approach is sensible, the experimental evaluation is thorough and honest, and the consistent improvements justify publication. The method is simple enough for practitioners to adopt and is particularly valuable in extremely label-scarce regimes. The authors appropriately acknowledge limitations and suggest future directions.