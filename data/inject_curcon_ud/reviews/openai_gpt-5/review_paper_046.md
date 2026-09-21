Summary
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method that linearly increases augmentation strength during the contrastive stage (from mild token dropout to aggressive back-translation). On four English text-classification benchmarks with 500 labels each, CurCon improves average accuracy to 88.9 versus 87.8 for CERT and 85.1 for direct fine-tuning. Ablations indicate the schedule itself contributes ~0.8 points on average, and gains are larger with fewer labels.

Strengths
- Clear, simple idea with minimal engineering overhead; integrates cleanly into the CERT pipeline.
- Consistent improvements over strong baselines (CERT, SimCSE, UDA) across four datasets with five seeds and reported variance.
- Solid ablations: fixed mixture, reversed curriculum, removal of back-translation, and label-scarcity analysis (100/500/1000 labels) support claims.
- Well-written and easy to reproduce; reasonable reporting of training details.

Weaknesses and questions
- Novelty is incremental: curriculum over augmentation strength is known in CV; the NLP instantiation is straightforward.
- Improvements are modest (≈1.1 avg points over CERT); statistical significance testing is not reported.
- Baseline fairness: baselines seem to use default hyperparameters from papers, whereas CurCon is tuned via grid search per dataset; this may disadvantage baselines.
- Scope is limited: only BERT-base, four short-text English datasets, and one linear schedule. No results on larger encoders or multilingual data.
- Limited analysis of unlabeled data quantity/quality; the effect of varying unlabeled corpus size is not studied.

Suggestions for improvement
- Report statistical significance and ensure comparable hyperparameter tuning for all baselines.
- Evaluate on additional models (e.g., RoBERTa, DeBERTa) and at least one longer-text or domain-specific dataset.
- Analyze sensitivity to unlabeled data size and quality; include representation diagnostics (e.g., retrieval or probing).
- Explore or compare to learned/adaptive schedules, and quantify operator selection dynamics over training.

Scores (0–100)
- Soundness: 84 — Methodology is solid with appropriate ablations and multiple seeds; minor concerns about baseline tuning and lack of significance tests.
- Novelty: 72 — Conceptually incremental but a clean, effective adaptation to NLP contrastive intermediate training.
- Significance: 78 — Practical and broadly applicable; gains are consistent though modest; particularly relevant in low-label regimes.
- Clarity: 90 — Very clear exposition, well-structured, with sufficient implementation detail.

Final average score
- (84 + 72 + 78 + 90) / 4 = 81.0

Final recommendation
- Accept