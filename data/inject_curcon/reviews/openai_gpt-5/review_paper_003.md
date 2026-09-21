Here is my review.

Summary
CurCon introduces a curriculum-scheduled contrastive intermediate training approach for low-resource text classification, gradually increasing augmentation strength during the contrastive stage. On four datasets with 500 labeled examples each, it achieves consistent gains over fine-tuning, UDA, SimCSE, and CERT, with clear ablations indicating the curriculum itself contributes meaningfully to the improvements.

Strengths
- Clear, simple idea that is easy to implement on top of CERT, with no inference overhead.
- Consistent improvements across four benchmarks and five seeds; ablations isolate curriculum effects.
- Sensible curriculum design and analysis of label-scarcity regimes.
- Writing is clear and limitations are candidly discussed.

Weaknesses
- Novelty is incremental: curriculum scheduling of augmentation strength is a known idea in other domains, adapted here to contrastive intermediate training.
- Gains are modest (+1.1 avg over CERT) and may depend on careful per-dataset hyperparameter search; baselines may not be equally tuned.
- Heavy reliance on specific augmentations (WordNet, back-translation) may limit portability across languages/domains.
- Limited scope: only English, short-text datasets, and BERT-base; no results on larger encoders or decoder-only models.

Scores (0–100)
- Soundness: 83
- Novelty: 70
- Significance: 77
- Clarity: 88

Final average score
79.5

Recommendation
Accept