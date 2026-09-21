# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Soundness: 78/100

**Strengths:**
- The experimental methodology is rigorous: five random seeds with means and standard deviations reported
- Proper separation of validation (200 examples) and test sets
- Reasonable hyperparameter selection via grid search (48 configurations)
- Ablation studies provide insights into component contributions
- Clear description of the contrastive training pipeline and augmentation operators

**Weaknesses:**
- The linear curriculum schedule is overly simplistic and not well-justified theoretically. Why linear interpolation rather than other schedules?
- Limited hyperparameter tuning for baselines: "hyperparameters reported in their original papers" may not be optimal for this low-resource setting. This could unfairly disadvantage baselines
- Ablation on reversed curriculum (Table 2) is useful but limited—no exploration of alternative schedules (exponential, step-based, etc.)
- The "fixed mixture" baseline (L=0) shows only 0.8-point difference, which is modest and within noise margins for some datasets
- No statistical significance testing reported despite small margins of improvement
- The claim that "difficulty is closely tied to augmentation strength" needs more empirical validation

## Novelty: 62/100

**Strengths:**
- Applying curriculum learning to augmentation strength in contrastive learning is a reasonable idea
- The progressive increase from mild (token dropout) to strong (back-translation) augmentations is intuitive
- Extension of CERT with a curriculum schedule is straightforward but novel

**Weaknesses:**
- The core idea is somewhat incremental: it applies existing curriculum learning concepts (well-established in ML) to an existing method (CERT)
- Curriculum learning for augmentation has been explored in vision (acknowledged by authors); the text-specific contribution is limited
- The four augmentation operators are all existing techniques; no new augmentation strategies are introduced
- The linear schedule design lacks novelty—it's a simple monotonic interpolation with hand-picked thresholds (0.25, 0.5, 0.75)
- No exploration of learned or data-driven curricula

## Significance: 71/100

**Strengths:**
- Addresses a practical and important problem: low-resource text classification (500 labeled examples)
- Improvements are consistent across all four datasets
- Largest gains when data is most scarce (1.6 points at 100 examples), which is practically relevant
- Method is simple to implement and adds minimal computational overhead (12% increase)
- No additional inference cost—only affects training

**Weaknesses:**
- The absolute improvements, while consistent, are modest (1.1 points over CERT, 0.8 points from curriculum alone at 500 examples)
- Results limited to four relatively small/simple English datasets (SST-2, AG News, TREC, SUBJ) with short texts
- Only evaluated on BERT-base; claims about generalization to larger models are unsupported
- Limited to English and doesn't evaluate multilingual or domain-specific robustness
- The practical impact diminishes significantly with more labeled data (0.5 points at 1,000 examples)
- Improvements could be within noise margins given standard deviations (e.g., SST-2: 85.6±0.8 vs 84.1±0.9 overlap in confidence intervals)

## Clarity: 85/100

**Strengths:**
- Clear problem motivation and related work section
- Well-structured method description with specific operator definitions and curriculum formula
- Good use of tables for results and ablations
- Experimental setup is clearly specified
- The paper is generally well-written and easy to follow

**Weaknesses:**
- The curriculum formula c(t) = min(1, t/L) is simple but the threshold values (0.25, 0.5, 0.75) appear arbitrary without justification
- Limited discussion of why this particular ordering of augmentations (token dropout → synonym replacement → span deletion → back-translation) was chosen
- The "fixed mixture" baseline description could be clearer
- Missing details on validation performance across hyperparameter configurations

## Minor Issues

1. **Table 3 context**: The improvement decreases with more labels, which is expected, but the paper doesn't discuss implications for practitioners deciding whether to use CurCon
2. **Computational cost**: While noted (12% increase), no absolute timing is provided
3. **Reproducibility**: Code availability not mentioned
4. **Statistical significance**: With overlapping error bars on some datasets, significance tests would strengthen claims

## Missing Comparisons
- No comparison with other curriculum learning baselines (e.g., curriculum by example difficulty)
- No evaluation on larger models (RoBERTa, ELECTRA, GPT-based) as acknowledged in limitations

---

## Overall Assessment

This paper presents a simple, practical improvement to contrastive intermediate training by scheduling augmentation strength. The idea is sound and the experiments are reasonably rigorous, but the contribution is incremental. The improvements are consistent but modest (especially the curriculum contribution of 0.8 points), and significance is unclear given overlapping confidence intervals. The scope is limited to small English datasets and BERT-base.

The work makes a useful contribution to low-resource NLP, particularly when labeled data is extremely scarce (≤100 examples), but the novelty is limited and the broad applicability remains uncertain.

---

## Final Scores Summary
- **Soundness: 78/100**
- **Novelty: 62/100**
- **Significance: 71/100**
- **Clarity: 85/100**

### **Average Score: 74/100**

---

## Recommendation: **ACCEPT (with reservations)**

**Justification**: This paper presents a simple, practical method that consistently improves over strong baselines on a relevant problem. While the novelty is limited (incremental application of curriculum learning to augmentation scheduling) and improvements are modest, the work is technically sound, clearly presented, and useful for practitioners working with low-resource data. The ablation studies are helpful, and the focus on the extreme low-resource regime (100-500 labels) is valuable. However, the limited scope (English, small datasets, BERT-base only) and lack of statistical significance testing prevent a stronger recommendation. This is a solid workshop or applications paper that would benefit from broader evaluation before appearing at a top-tier venue.

**Acceptance confidence: 65% (borderline accept)**