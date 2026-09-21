Here is a concise review.

Summary
- Proposes CurCon, a curriculum-scheduled contrastive intermediate training method that linearly increases augmentation strength during contrastive pre-training on in-domain unlabeled text.
- Uses four augmentations from mild (token dropout) to strong (back-translation) and shows consistent improvements over fine-tuning, UDA, SimCSE, and CERT on four low-resource text classification datasets (500 labels), with larger gains at 100 labels.
- Provides ablations (fixed mixture, reversed curriculum, without back-translation) and a label-scarcity analysis.

Strengths
- Simple, practical idea that adds no inference cost and slots into a widely used pipeline (CERT).
- Consistent gains over strong baselines across multiple datasets and seeds; ablations support the curriculum’s contribution (~0.8 points).
- Clear training pipeline and rationale; results analyzed across label budgets.

Weaknesses / Concerns
- Improvements are modest (+1.1 points over CERT on average; larger at 100 labels but still moderate).
- Potential tuning imbalance: CurCon tuned via grid search per dataset, while baselines use hyperparameters from original papers; could bias results. Stronger fairness would include comparable tuning or a shared tuning budget.
- Limited scope: only BERT-base and four short-text English datasets; no results with larger encoders or multilingual/long-text settings.
- Some reproducibility details are light (exact hyperparameter search space, temperature range, MT system used for back-translation).

Scores (0–100)
- Soundness: 82
- Novelty: 73
- Significance: 76
- Clarity: 90

Final average: 80.25

Recommendation: Accept

Rationale: Although incremental, the method is clean, well-motivated, and empirically supported with consistent improvements and informative ablations. The simplicity and practicality make it useful for low-resource settings. Addressing tuning fairness and broader evaluations would further strengthen the work.