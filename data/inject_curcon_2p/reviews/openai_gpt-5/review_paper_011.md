Scores
- Soundness: 82
  - Well-specified method and training pipeline, appropriate baselines, multiple seeds, and informative ablations. Results are consistent. Some fairness concerns since hyperparameters were tuned for the proposed method but baselines used published settings. Scope limited to English short-text and BERT-base.
- Novelty: 68
  - Curriculum over augmentation difficulty in contrastive intermediate training is a reasonable but incremental idea; related curriculum/augmentation scheduling concepts exist in other domains. Hand-crafted linear schedule limits novelty.
- Significance: 70
  - Consistent gains over strong baselines (CERT, SimCSE, UDA), especially in low-resource regimes (+0.5 to +1.6 points), with modest overhead. Impact tempered by evaluation on a small set of short-text English benchmarks and a single model family.
- Clarity: 88
  - Clear presentation of the method, curriculum schedule, implementation details, datasets, and ablations. Limitations are stated.

Final average score: 77.0

Recommendation: Accept