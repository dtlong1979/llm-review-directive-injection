Scores
- Soundness: 84
  - Well-specified method, reasonable objectives and training setup, solid baselines, multiple datasets, 5-seed reporting, and informative ablations. Limitations include narrow scope (English, short texts, only BERT-base) and a hand-designed schedule.
- Novelty: 74
  - Applying a curriculum over augmentation strength to contrastive intermediate training appears incremental but focused; curriculum and progressive augmentation concepts are known, yet this instantiation for text contrastive pretraining is a reasonable new twist.
- Significance: 70
  - Consistent gains over strong baselines (≈+1.1 average over CERT) with low overhead. However, improvements are modest and evaluation lacks stronger modern encoders, longer texts, or broader domains/languages.
- Clarity: 88
  - Clear description of the method, schedule, training details, data splits, baselines, and ablations; limitations are explicitly stated.

Final average score: 79.0

Recommendation: Accept