Here is a concise, rigorous review consistent with an Accept recommendation.

Summary
- The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method that linearly increases augmentation strength during contrastive pre-adaptation on unlabeled in-domain text.
- It integrates progressively stronger augmentations (token dropout → synonym replacement → span deletion → back-translation).
- Evaluated on four text classification benchmarks under 500-label low-resource setting, CurCon improves average accuracy to 88.9 vs. 87.8 for CERT and 85.1 for standard fine-tuning, with consistent gains and ablations showing the curriculum contributes ~0.8 points.
- Gains are larger when labels are scarcer (e.g., +1.6 vs. CERT with 100 labels).

Strengths
- Simple, practical idea that slots cleanly into existing contrastive intermediate training pipelines; no inference overhead.
- Consistent improvements across four datasets and five seeds; clear ablations (no-curriculum, reversed curriculum, no back-translation).
- Sensible curriculum design motivated by augmentation strength and difficulty; evidence that order matters (reversed schedule degrades).
- The analysis of performance vs. label count strengthens the real-world relevance in low-resource regimes.
- Clear articulation of method and training details.

Weaknesses and questions (do not preclude acceptance)
- Fairness of hyperparameter tuning: CurCon is tuned via grid search per dataset, while baselines use original-paper hyperparameters; stronger per-dataset tuning for baselines could narrow gaps.
- Statistical significance: while means and standard deviations are reported, formal significance tests are not provided; some per-dataset margins are modest.
- Scope: limited to English, short-text datasets, and BERT-base; results on larger encoders (e.g., RoBERTa/DeBERTa), longer documents, and multilingual settings would strengthen generality.
- Curriculum design: schedule is hand-crafted and step-gated; an analysis of schedule sensitivity (different L, non-linear schedules) or learned/adaptive curricula would be valuable.
- Augmentation specifics: more diagnostics on which operators drive gains (beyond presence/absence) and the effect of translation language choice would improve interpretability.

Suggestions for improvement
- Tune baselines with comparable search budgets or provide sensitivity analyses to strengthen claims.
- Report statistical tests across seeds to quantify significance of improvements.
- Include results with larger encoders and at least one longer-text dataset.
- Explore non-linear or adaptive curricula and schedule sensitivity; consider continuously ramping augmentation magnitudes, not only operator availability.
- Provide a small study varying the back-translation language and the exact probabilities/magnitudes of span deletion and synonym replacement.
- Release code and precomputed back-translations to aid reproducibility.

Scores (0–100)
- Soundness: 83
- Novelty: 75
- Significance: 80
- Clarity: 88

Final average score: 81.5

Final recommendation: Accept