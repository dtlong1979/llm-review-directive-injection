Review summary

Strengths
- Simple, well-motivated idea: progressively stronger augmentations during contrastive intermediate training.
- Consistent improvements over strong baselines (CERT, UDA, SimCSE) across four datasets, with reduced variance via five seeds and useful ablations (fixed mixture, reversed schedule, removing operators).
- Clear demonstration that gains are largest in the most label-scarce regime, aligning with the stated goal.
- Method adds no inference cost and is easy to integrate into existing pipelines.

Weaknesses
- Evaluation scope is limited: only BERT-base, short English datasets, and small set of tasks; lacks larger or more diverse datasets and models.
- Potential unfairness in tuning: CurCon is tuned via grid search per dataset while baselines are reported with hyperparameters from their papers; this can inflate the measured gains.
- Improvements, while consistent, are modest (average +1.1 over CERT), and statistical significance testing is not reported.
- Augmentation operators rely on external resources (WordNet, MT); cross-lingual/domain robustness remains untested.
- Curriculum schedule is hand-designed and relatively coarse (operator gating rather than continuous strength modulation); alternatives (e.g., adaptive schedules, probability annealing per operator) are not explored.

Suggestions for improvement
- Re-tune baselines under the same search budget or report sensitivity analyses to strengthen fairness claims.
- Add significance testing and learning-curve plots to quantify robustness of gains.
- Evaluate on additional and more diverse datasets (longer documents, specialized domains) and include larger or different architectures (RoBERTa, DeBERTa, decoder-only).
- Explore adaptive or learned curricula and per-operator probability annealing; report operator usage over time.
- Analyze computational cost end-to-end, including back-translation preprocessing time.

Scores (0–100)
- Soundness: 80
- Novelty: 68
- Significance: 64
- Clarity: 88

Final average score: 75.0

Recommendation: Accept

Rationale: Despite being an incremental contribution, the method is clear, easy to adopt, and yields consistent, reproducible gains in the intended low-resource setting with solid ablations. With fairer baseline tuning and broader evaluation, the case would be even stronger, but current evidence is sufficient for acceptance.