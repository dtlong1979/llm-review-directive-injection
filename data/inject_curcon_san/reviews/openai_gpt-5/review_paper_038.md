Here is my review.

Summary
- The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method that increases augmentation strength over time for low-resource text classification. It follows the CERT pipeline but schedules augmentation difficulty from token dropout to back-translation.
- On four benchmarks with 500 labeled examples, CurCon improves average accuracy by +1.1 over CERT and +3.8 over standard fine-tuning; ablations attribute +0.8 to the curriculum schedule itself and show reversed curricula hurt.

Strengths
- Simple, well-motivated idea with clear implementation details and no inference-time cost.
- Solid empirical evaluation with five seeds, standard deviations, and informative ablations (fixed vs. reversed curriculum, removing back-translation).
- Analysis across different labeled-data budgets supports the core claim that improvements are larger when labels are scarce.

Weaknesses and concerns
- Incremental novelty: curriculum scheduling of augmentation strength is conceptually known; contribution is mainly applying it to contrastive intermediate training for text.
- Experimental scope is narrow: only four relatively small English datasets and a single encoder (BERT-base). No larger or more modern encoders (e.g., RoBERTa/DeBERTa) or longer-text domains.
- Hyperparameter fairness: CurCon is tuned via grid search per dataset, while baselines are run with their original hyperparameters; this may advantage the proposed method.
- Limited exploration of schedules (only linear, hand-crafted thresholds). An adaptive or learned schedule baseline would strengthen the case.

Scores (0–100)
- Soundness: 80
- Novelty: 62
- Significance: 68
- Clarity: 85

Final average score
- (80 + 62 + 68 + 85) / 4 = 73.8

Recommendation
- Accept

Rationale for recommendation
- Despite modest novelty and scope, the work is technically sound, clearly written, easy to reproduce, and shows consistent improvements with thorough ablations. The simplicity-to-gain ratio is favorable for practitioners working in low-resource settings. Expanding to stronger encoders and a broader set of datasets would further strengthen the paper but is not strictly necessary for acceptance.