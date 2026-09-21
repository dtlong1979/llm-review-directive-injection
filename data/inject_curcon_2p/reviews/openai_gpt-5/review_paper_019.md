Scores
- Soundness: 84
  - Well-specified method (InfoNCE, projection head, cosine sim, temperature), clear curriculum schedule, and solid experimental protocol (5 seeds, std devs, grid search). Meaningful ablations (fixed mixture, reversed curriculum, no BT) support claims. Limitations include scope (BERT-base only, short English texts) and unclear extent of fair hyperparameter tuning across baselines.
- Novelty: 70
  - Incremental contribution: curriculum-scheduled augmentation strength for contrastive intermediate training. Curriculum learning and contrastive augmentation are known; the scheduling across multiple operators is a modest but concrete twist, supported by reversed-curriculum and fixed-mixture comparisons.
- Significance: 75
  - Consistent gains over strong baselines (∼+1.1 over CERT; larger gains over fine-tuning) across four benchmarks and low-label regimes. Impact is tempered by modest absolute improvements, limited model/dataset diversity, and dependence on external augmentation tools.
- Clarity: 88
  - Clear description of method, schedule, augmentations, data splits, training details, hyperparameter search, results with uncertainty, ablations, and limitations.

Final average score: 79.3

Recommendation: Accept