Here is my review.

Strengths
- Simple, model-agnostic idea: progressively increasing augmentation strength during contrastive intermediate training.
- Consistent improvements over strong baselines (CERT, SimCSE, UDA) across four datasets, with gains largest in the lowest-label regime.
- Clear ablations isolating the effect of the curriculum and augmentation types.
- No inference-time cost and minimal implementation overhead.

Weaknesses
- Modest absolute gains (≈1.1 avg points over CERT) and limited to four classic, relatively short-text English datasets with BERT-base only.
- Potential fairness concern: CurCon is tuned via grid search per dataset, while baselines are run with hyperparameters from their papers rather than re-tuned on the same validation splits.
- Missing statistical significance tests for per-dataset gains.
- Limited comparison to more recent semi-/self-supervised or augmentation strategies beyond UDA, CERT, and SimCSE.
- Some implementation specifics could be clearer (e.g., exact augmentation sampling probabilities once multiple operators are available, and full hyperparameter grids).

Scores (0–100)
- Soundness: 82
- Novelty: 74
- Significance: 76
- Clarity: 88

Final average score: 80.0

Recommendation: Accept

Rationale: Despite incremental novelty and modest gains, the method is clean, reproducible in spirit, consistently improves over strong baselines, and is practically useful for low-resource settings with no inference overhead.