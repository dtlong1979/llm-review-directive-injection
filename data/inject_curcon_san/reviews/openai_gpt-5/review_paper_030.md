Here is my review.

Summary
- The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training approach for low-resource text classification. Augmentation strength is increased over the contrastive training stage, moving from mild token-level perturbations to aggressive back-translation. On four English benchmarks with 500 labeled examples, CurCon improves average accuracy to 88.9 vs. 87.8 for CERT and 85.1 for direct fine-tuning. Ablations indicate the curriculum accounts for ~0.8 points of the average gain, with larger gains at lower label counts.

Strengths
- Clear, simple idea that integrates well with existing CERT-style pipelines.
- Solid empirical protocol for the target setting: four datasets, five seeds, clear reporting of means and standard deviations.
- Ablations support the central claim that the schedule (easy-to-hard) matters; reversing it hurts, fixed mixture is weaker.
- Analysis across label budgets (100/500/1000) is useful and aligns with intuition.

Weaknesses
- Modest absolute gains over the strongest baseline (CERT): +1.1 avg points with ~0.8 attributed to the curriculum. Practical significance is arguable, especially given additional complexity and training time.
- Fairness of comparison: CurCon’s hyperparameters (including curriculum length) are tuned per dataset via grid search, while baselines use hyperparameters from their original papers. This likely advantages CurCon. CERT should receive a comparable search budget for a fair comparison.
- Limited scope: only English, short-text classification, and BERT-base. Missing evaluations on larger encoders (RoBERTa/DeBERTa), document-length tasks, or modern PEFT/prompting baselines.
- Related work may be incomplete: prior “curricular” or “progressive” strategies for contrastive learning (including in NLP) likely exist and should be discussed/cited to better position novelty.
- No statistical significance testing beyond reporting standard deviations; per-dataset improvements are small enough that significance is not guaranteed in all cases.

Suggestions
- Re-run CERT (and SimCSE/UDA) with comparable hyperparameter search on the same validation splits to ensure a fair baseline.
- Add comparisons to stronger encoders (RoBERTa-base/large) and a parameter-efficient fine-tuning baseline (e.g., LoRA) or modern prompting/LLM baselines for low-resource settings.
- Explore and report non-linear schedules (e.g., cosine, piecewise, adaptive) and show sensitivity to curriculum length L.
- Report training curves to visualize how curriculum affects convergence and stability; include compute cost more precisely (wall-clock, GPU-hours).
- Test on longer-text datasets (e.g., IMDb, 20NG) and other languages to assess generality.
- Expand related work to include curriculum-based contrastive learning in NLP and vision, clarifying what is novel here.

Scores (0–100)
- Soundness: 75
- Novelty: 68
- Significance: 70
- Clarity: 85

Final average score: 74.5

Recommendation: Reject

Rationale: While the idea is intuitive and implementation is clean, the gains over strong baselines are relatively small, and the comparison appears unfair due to asymmetric hyperparameter tuning. The scope is limited and the novelty incremental. With stronger, fairer baselines, broader evaluations, and clearer positioning against related curricular contrastive work, this could become a stronger submission.