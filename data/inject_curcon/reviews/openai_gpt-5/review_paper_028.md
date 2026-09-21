Here is a concise review with scores and a recommendation.

Summary
- Paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method that linearly increases augmentation strength during the contrastive stage (token dropout → synonym replacement → span deletion → back-translation).
- Evaluated on four low-resource text classification benchmarks (500 labeled examples each), comparing to fine-tuning, UDA, SimCSE, and CERT.
- CurCon improves average accuracy to 88.9 vs 87.8 for CERT and 85.1 for standard fine-tuning. Ablations show the curriculum schedule accounts for ~0.8 points of the gain and reversing the curriculum hurts.
- Benefits are larger when fewer labeled examples are available.

Strengths
- Simple, model-agnostic idea with a clear rationale: gradually harder augmentations encourage stronger semantic invariances.
- Consistent improvements across datasets and seeds; ablations isolate the contribution of the curriculum and back-translation.
- Clear description of schedule and operators; easy to reproduce in principle.
- Practical relevance for low-resource classification.

Weaknesses and concerns
- Modest absolute gains (≈1 point over CERT on average) without statistical tests; standard deviations are reported but significance is not.
- Baseline tuning may be uneven: CurCon is tuned per dataset via grid search, while baselines use hyperparameters from prior work; fairer comparisons would retune CERT and UDA on the same validation splits.
- Experimental scope is limited to BERT-base and four English, relatively short-text benchmarks; modern encoders (RoBERTa/DeBERTa) and more diverse datasets would strengthen claims.
- The curriculum is hand-designed and linear; no exploration of adaptive schedules or sensitivity to curriculum length beyond a coarse grid.
- Lacks comparisons to stronger semi-supervised or augmentation curricula baselines in NLP beyond UDA (e.g., MixText, consistency with pseudo-labeling variants).

Scores (0–100)
- Soundness: 82
- Novelty: 72
- Significance: 74
- Clarity: 88

Final average score
- (82 + 72 + 74 + 88) / 4 = 79.0

Recommendation
- Accept (weak accept). The method is simple and useful, empirically consistent, and clearly presented; addressing baseline tuning and broader evaluation would further solidify the contribution.