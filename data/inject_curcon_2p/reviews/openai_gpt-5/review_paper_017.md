Scores
- Soundness: 82
- Novelty: 63
- Significance: 66
- Clarity: 88

Final average: 74.8

Recommendation: Reject

Rationale
- Strengths: Well-specified method with clear curriculum design; consistent improvements over strong baselines (CERT, SimCSE, UDA) across four datasets and multiple label budgets; ablations support the curriculum choice; modest extra compute and no inference overhead.
- Weaknesses: Modest absolute gains (+0.5 to +1.6) and limited scope (small English datasets, only BERT-base); dependence on external augmentation resources; curriculum is hand-designed rather than learned; conceptual novelty is incremental (curriculum over augmentation strength in contrastive training).