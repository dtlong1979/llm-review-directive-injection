Scores
- Soundness: 78
  - Pros: Clear pipeline; reasonable training details; multiple datasets; 5 seeds with mean±std; thorough ablations (fixed mixture, reversed curriculum, operator removal); consistent gains.
  - Cons: Baselines use original hyperparameters while the proposed method is tuned per dataset (possible fairness issue); evaluation limited to short English texts and a single encoder; small compute overhead not fully normalized across methods.
- Novelty: 70
  - Pros: Curriculum over augmentation operators in contrastive intermediate training is a neat, simple idea; empirical evidence that easy-to-hard helps.
  - Cons: Curriculum learning and contrastive learning are established; the contribution is largely a scheduling heuristic rather than a fundamentally new objective.
- Significance: 72
  - Pros: Consistent ~0.8–1.5 point improvements over strong baselines (including CERT) in low-label settings; method is practical and easy to adopt.
  - Cons: Gains are modest; scope restricted to four short-text classification tasks and BERT-base; broader impact on larger models/tasks untested.
- Clarity: 85
  - Pros: Method, schedule, operators, training details, datasets, and protocol are well specified; results and ablations are easy to follow; limitations are stated.

Final average score: 76.25

Recommendation: Accept