Scores (0–100)
- Soundness: 80
- Novelty: 70
- Significance: 75
- Clarity: 87

Final average score: 78.0

Recommendation: Accept

Review
Strengths
- Clear and well-motivated idea: progressively increasing augmentation strength during contrastive intermediate training is intuitive, aligns with curriculum learning principles, and is easy to adopt.
- Solid empirical results in a relevant low-resource regime: consistent gains over strong baselines (CERT, UDA, SimCSE) across four datasets, with the largest benefits when labels are scarcest.
- Careful ablations: fixed-mixture vs. curriculum, reversed curriculum, and removal of back-translation all help isolate where gains come from; showing the reversed curriculum hurts strengthens the claim that the order matters.
- Practicality: minimal engineering overhead, no inference-time cost, and implementation details provided at a useful level.

Weaknesses and concerns
- Modest absolute gains: average +1.1 over CERT and +0.8 attributable to the curriculum are meaningful but not large; significance testing is not reported despite small standard deviations.
- Fairness of comparison: CurCon uses per-dataset grid search over 48 configurations, while baselines appear to use hyperparameters from their papers; stronger tuning of baselines (or at least a shared tuning protocol) would strengthen claims.
- Scope: results are limited to English, relatively short-text datasets, and BERT-base; it is unclear how well the approach scales to larger encoders, long documents, or other languages.
- Curriculum design: the schedule is hand-crafted with step thresholds and a linear ramp; comparisons to alternative schedules (e.g., smooth probability annealing, adaptive curricula) would add depth.
- Augmentation choices: reliance on WordNet and German back-translation may limit portability; analysis of augmentation quality/noise across domains is limited.

Questions and suggestions
- Report statistical significance for main improvements over CERT across seeds.
- Provide a shared hyperparameter tuning protocol for all methods, or at least a sensitivity analysis showing CurCon’s robustness to learning rate, temperature, and curriculum length.
- Evaluate on an additional domain with longer documents or a non-English dataset to test generality.
- Explore learned/adaptive curricula and alternative mixing strategies (e.g., gradually increasing probabilities rather than hard thresholds; combining multiple operators per view).
- Include calibration or robustness assessments (e.g., performance under heavy noise) to support the representation-quality claim.
- Release code and augmentation configurations to improve reproducibility.

Overall assessment
This paper offers a simple, well-justified enhancement to contrastive intermediate training that yields consistent improvements in low-resource text classification. While the novelty is incremental and the gains modest, the method’s clarity, practicality, and reproducible design make it a valuable contribution. With stronger baseline tuning and significance tests, the empirical case would be even more compelling. I recommend acceptance.