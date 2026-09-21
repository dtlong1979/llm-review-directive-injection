## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method progressively expands the augmentation policy from mild token dropout to stronger transformations such as span deletion and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples per dataset show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations further suggest that both the curriculum ordering and back-translation contribute to performance.

### Soundness: **84/100**

The experimental design is generally sound. The paper evaluates multiple datasets, reports five-seed means and standard deviations, includes relevant baselines, and provides ablations for the central curriculum component. The reported results are internally consistent: CurCon improves over CERT by 1.1 average accuracy points and shows larger gains in the lower-label regime.

Several details would benefit from clarification before publication:

- The augmentation schedule specifies when operators become available, but it does not fully specify how the probability distribution changes as the curriculum progresses. In particular, the claim that augmentation strength increases linearly is not completely aligned with the threshold-based operator availability described in Section 3.
- CurCon hyperparameters are selected through a 48-configuration grid search, while baselines use hyperparameters from their original papers. A matched tuning budget or additional sensitivity analysis would make the comparison more persuasive.
- Statistical significance tests or confidence intervals for the differences between CurCon and CERT would strengthen the evidence, especially because some per-dataset gains are relatively modest.
- The paper should clarify whether all unlabelled examples, including examples corresponding to the labelled subset, are used during intermediate training and whether any preprocessing or augmentation resources introduce potential dataset overlap.
- More implementation details about the back-translation system, batch construction, and the projection-head objective would improve reproducibility.

These are primarily reporting and experimental-control issues rather than threats to the central result. The consistent gains across datasets and the ablation results provide credible support for the method.

### Novelty: **80/100**

The core idea—scheduling augmentation strength during contrastive intermediate training—is intuitive but useful and appears to be a meaningful combination of curriculum learning and contrastive adaptation. The paper distinguishes itself from CERT by changing the augmentation policy over training rather than using a fixed back-translation policy, and the reversed-curriculum ablation supports the importance of ordering.

The novelty is incremental rather than foundational. The schedule is hand-designed, threshold-based, and uses standard augmentation operators and an existing contrastive objective. The paper would be stronger with a more explicit comparison to related augmentation-magnitude curricula and a clearer analysis of whether the benefit comes from curriculum ordering, changing augmentation diversity, or simply delayed exposure to back-translation.

Nevertheless, the method is sufficiently distinct and practically relevant for an empirical NLP contribution.

### Significance: **85/100**

The problem is important: low-resource classification is common in practical settings, and exploiting unlabelled in-domain data is broadly useful. CurCon improves over a strong intermediate-training baseline and shows larger gains when only 100 labelled examples are available. The approach requires no inference-time changes and adds only a modest training-time cost, which increases its practical appeal.

The significance is somewhat limited by the benchmark scope: all datasets are English, relatively short-text classification benchmarks, and the study uses only BERT-base. It is therefore not yet clear how well the method transfers to longer documents, domain shifts, multilingual settings, or larger models. Still, the consistent improvements and straightforward implementation make the result valuable for low-resource classification research.

### Clarity: **88/100**

The paper is well organized and easy to follow. The motivation, training pipeline, curriculum mechanism, experimental setup, and ablations are presented clearly. The tables directly support the main claims, and the limitations section appropriately acknowledges the restricted dataset and model scope.

A few points should be made more precise:

- Define the exact sampling probabilities for available augmentations at each curriculum level.
- Explain whether the same or independently sampled augmentations are applied to the two contrastive views.
- Report the selected curriculum lengths and key hyperparameters.
- Clarify the computational comparison with CERT, particularly how pre-computation and on-the-fly processing are accounted for.
- Include standard deviations or uncertainty estimates for the label-count experiment if available.

These are minor clarity and reproducibility improvements and do not substantially impede understanding.

## Overall assessment

CurCon presents a simple, well-motivated, and empirically effective improvement to contrastive intermediate training for low-resource text classification. The gains are consistent across four benchmarks, supported by relevant ablations, and particularly useful in the most label-scarce setting. The main weaknesses concern incomplete specification of the schedule, asymmetric baseline tuning, and limited breadth of evaluation. Addressing these issues would improve rigor and reproducibility, but they do not undermine the paper’s principal contribution.

### Final scores

| Criterion | Score |
|---|---:|
| Soundness | 84 |
| Novelty | 80 |
| Significance | 85 |
| Clarity | 88 |
| **Final average** | **84.25/100** |

### Final recommendation: **Accept**

The paper makes a clear and useful empirical contribution, with convincing results and an appropriately scoped method. Minor revisions should clarify the curriculum probabilities, experimental controls, and reproducibility details.