Here is my review of the paper “CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification.”

Summary
- The paper proposes CurCon, a curriculum over augmentation strength during contrastive intermediate training on unlabeled in-domain text prior to fine-tuning. The curriculum progresses from mild perturbations (token dropout) to stronger ones (synonym replacement, span deletion, back-translation).
- On four classification benchmarks with 500 labeled examples, CurCon improves average accuracy to 88.9 vs. 87.8 (CERT) and 85.1 (standard fine-tuning). Ablations indicate the curriculum accounts for ~0.8 average accuracy points, with larger gains when labeled data are scarcer.

Strengths
- Clear, simple idea that is easy to implement and adds no inference cost.
- Careful experimental protocol for the targeted low-resource regime: four datasets, five seeds, and ablations (fixed mixture, reversed curriculum, removing back-translation).
- Empirical gains are consistent across datasets and larger when labels are very limited, supporting the intended use case.
- The paper is well written and provides sufficient training details to facilitate reproduction.

Weaknesses and concerns
- Fairness of tuning: CurCon hyperparameters (including learning rate and temperature) are tuned via grid search per dataset, while baselines use hyperparameters from their original papers. This can disadvantage baselines in the low-resource regime; a matched tuning budget for baselines would strengthen the claims.
- Scope is limited: only English, short-text datasets, and BERT-base. No results on larger or decoder-only models, or on longer documents/domains.
- Statistical significance is not reported; while mean ± std is shown, formal tests would better support the small but consistent gains over CERT.
- The curriculum manipulates operator availability in stages but not operator magnitudes (e.g., span length, replacement rates). It would be informative to compare against a magnitude-only schedule or mixed schedules.
- Related work on curriculum over augmentation magnitude in vision is mentioned, but closer NLP comparisons (e.g., curricula or schedules over data difficulty/augmentation strength) are not empirically examined.

Suggestions for improvement
- Re-tune baselines under the same validation/tuning protocol or include a matched tuning budget analysis.
- Report statistical significance (e.g., paired tests over seeds).
- Evaluate on at least one longer-text dataset and one non-English dataset to probe generality.
- Explore schedules over augmentation magnitudes and/or adaptive curricula driven by performance signals.
- Provide sensitivity analysis for curriculum length and the thresholds at which operators become available.

Scores (0–100)
- Soundness: 80
- Novelty: 68
- Significance: 74
- Clarity: 88

Final average score: 77.5

Recommendation: Accept

Rationale: While the contribution is incremental, it is well-motivated, methodologically sound, and yields consistent improvements in a practically important setting with a straightforward approach. With stronger fairness controls in tuning and broader evaluation, this work could have solid impact for practitioners tackling low-resource text classification.