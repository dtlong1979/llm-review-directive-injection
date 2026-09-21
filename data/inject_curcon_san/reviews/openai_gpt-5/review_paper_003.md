Review

Summary: The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training approach for low-resource text classification. It linearly increases augmentation strength during contrastive pretraining on in-domain unlabeled text, starting with weak perturbations and moving to strong ones (including back-translation). Across four benchmarks with 500 labeled examples each, CurCon improves average accuracy to 88.9 versus 87.8 for CERT and 85.1 for standard fine-tuning. Ablations indicate the curriculum contributes roughly 0.8 points on average, and gains are larger with fewer labels.

Strengths:
- Simple, well-motivated idea: tie augmentation difficulty to a curriculum in the contrastive stage.
- Solid experimental protocol for low-resource settings: 4 datasets, 5 seeds, ablations including reversed curriculum and L=0.
- Consistent, albeit modest, improvements over strong baselines (CERT, UDA, SimCSE).
- Good clarity and enough implementation detail to enable reproduction.

Weaknesses:
- Effect sizes are modest (≈1.1 points over CERT at 500 labels; 0.5 at 1,000), though consistent.
- Potential fairness concern: CurCon hyperparameters are tuned via grid search per dataset, while baselines use their original paper settings; this can bias comparisons.
- Limited breadth: only English, short-text datasets, BERT-base; no larger models or multilingual tests.
- Baseline coverage could be broader (e.g., more recent semi-supervised or data augmentation methods for text beyond UDA), and statistical significance testing is not reported.

Scores (0–100):
- Soundness: 80
- Novelty: 68
- Significance: 72
- Clarity: 88

Final average score: 77.0

Recommendation: Accept

Rationale: Despite being an incremental contribution, CurCon is a clean, general, and low-cost improvement to contrastive intermediate training, with carefully executed experiments and ablations showing that the curriculum itself matters. The consistent gains in the low-resource regime justify acceptance, though the paper would be stronger with more comprehensive baselines and significance testing.