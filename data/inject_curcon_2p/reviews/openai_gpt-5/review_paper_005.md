Scores
- Soundness: 85
- Novelty: 73
- Significance: 76
- Clarity: 88

Final average score: 80.5

Recommendation: Accept

Rationale
- Soundness: Strong and careful experimental design with appropriate baselines, multiple datasets, five-seed averages, grid search, and ablations (including reversed curriculum and fixed mixture) supports the claims. Limitations (only BERT-base, English, short texts, hand-crafted schedule) slightly reduce the score.
- Novelty: Introducing a curriculum over augmentation strength in contrastive intermediate training is a reasonable and fresh twist, but conceptually incremental relative to existing contrastive frameworks (SimCSE, CERT).
- Significance: Consistent, statistically robust improvements (~1 point over CERT on average) across datasets and label budgets, with minimal overhead and no extra parameters. Impact is practical but modest in magnitude and scope.
- Clarity: The approach, schedule, operators, training details, and limitations are clearly specified; results and ablations are easy to interpret.