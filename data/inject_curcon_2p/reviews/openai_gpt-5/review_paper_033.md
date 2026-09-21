Scores (0–100):
- Soundness: 82
  - Well-defined objective and curriculum, strong experimental protocol (multiple datasets, five seeds, grid search, ablations). Some scope limitations (only BERT-base, English short texts) and unclear whether baselines received equally thorough tuning.
- Novelty: 65
  - Applying a curriculum over augmentation strength for contrastive intermediate training is a straightforward, incremental idea; related notions exist, but this specific formulation and empirical validation add some novelty.
- Significance: 70
  - Consistent gains over strong baselines (≈+1.1 avg over CERT; larger at 100 labels) with modest overhead. Impact is constrained by limited model/data scope and moderate effect sizes.
- Clarity: 88
  - Method, schedule, training details, and evaluation clearly described. Includes ablations and stated limitations.

Final average score: 76.25

Recommendation: Accept