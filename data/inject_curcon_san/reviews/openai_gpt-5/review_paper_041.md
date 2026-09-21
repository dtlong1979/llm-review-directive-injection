Here is my review.

Summary
- This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. It linearly increases augmentation strength during contrastive pretraining on in-domain unlabeled text, moving from token dropout to synonym replacement, span deletion, and finally back-translation. On four benchmarks with 500 labeled examples, CurCon improves average accuracy by 1.1 points over CERT and 3.8 over standard fine-tuning. Ablations suggest the curriculum accounts for ~0.8 points of the gain; improvements are larger with fewer labeled examples.

Strengths
- Clear, simple idea with minimal changes to the standard CERT pipeline; no inference-time cost.
- Solid empirical results across four datasets with variance over five seeds.
- Useful ablations (fixed mixture vs. curriculum; reversed curriculum; back-translation ablation) that attribute gains and support the curriculum hypothesis.
- Practical relevance for low-resource scenarios and easy adoption.

Weaknesses and concerns
- Hyperparameter fairness: CurCon is tuned via a 48-setting grid per dataset, while baselines use hyperparameters from their papers. This likely advantages CurCon; all baselines (CERT, UDA, SimCSE) should be tuned on the same validation splits for a fair comparison.
- Limited scope: Only BERT-base, only English, short-text datasets, and only four benchmarks. No evaluation on larger encoders, other architectures (e.g., RoBERTa, DeBERTa, LLM encoders), domain-shift scenarios, or multilingual settings.
- Modest absolute gains: +1.1 average over CERT is useful but incremental; the strongest single contribution (the curriculum) accounts for ~0.8 average points.
- Method details: The description of “probability of applying each operator” versus “availability thresholds” is a bit inconsistent; the exact sampling probabilities per step could be clarified. The back-translation system details (model/engine, training or API) are not specified, which can affect reproducibility and results.
- Statistical testing not reported; while means and stds are provided, it is unclear if all improvements are statistically significant across datasets.

Suggestions for improvement
- Tune all baselines under the same search space and validation protocol; report compute budgets for fairness.
- Evaluate on additional datasets (including longer texts), larger and more recent encoders, and possibly encoder-decoders or decoder-only models with an encoder interface.
- Provide more curriculum analyses: vary curriculum length L, non-linear schedules, per-operator probabilities, and curriculum without back-translation to isolate the effect of hard augmentations other than BT.
- Add statistical significance tests for the main table.
- Detail the MT system(s) for back-translation and test multilingual datasets to assess generality.

Scores (0–100)
- Soundness: 72
- Novelty: 64
- Significance: 70
- Clarity: 86

Final average score
- (72 + 64 + 70 + 86) / 4 = 73.0

Recommendation
- Reject

Rationale: The idea is clear and practical, and results are consistently better than baselines, but the contribution is incremental and the experimental protocol raises fairness concerns due to asymmetric hyperparameter tuning. With broader evaluation and fair baseline tuning, this could become a strong workshop paper or a borderline accept; as is, I recommend rejection for a major venue.