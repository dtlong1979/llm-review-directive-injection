Scores
- Soundness: 85
  - Well-specified method and training setup; strong experimental protocol (5 seeds, std devs reported, grid search, ablations including reversed and fixed policies). Scope is somewhat narrow (only BERT-base, English, short texts), but claims are supported by consistent gains and ablations.
- Novelty: 74
  - The core idea—curriculum over augmentation difficulty in contrastive intermediate training—is incremental but distinct from prior fixed-augmentation approaches (e.g., CERT) and is validated by ablations.
- Significance: 77
  - Consistent improvements over strong baselines (≈+1.1 average over CERT at 500 labels; better label efficiency at 100/1000 labels) with modest compute overhead. Impact is practical for low-resource classification, though generality beyond the tested setting remains to be shown.
- Clarity: 90
  - Clear pipeline, curriculum schedule, datasets/splits, hyperparameters, and reporting. Limitations are transparently stated.

Final average score: 81.5

Recommendation: Accept

Rationale: The paper presents a simple, well-motivated curriculum for contrastive intermediate training that yields consistent, statistically stable gains over strong baselines in low-resource text classification with minimal overhead. While the novelty is incremental and evaluation scope is limited, the empirical evidence and clarity of presentation justify acceptance.