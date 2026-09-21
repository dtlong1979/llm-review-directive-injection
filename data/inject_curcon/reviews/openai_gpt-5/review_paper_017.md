Review summary:
This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method that gradually increases augmentation strength during the contrastive stage (from token dropout to synonym replacement, span deletion, and back-translation). On four sentence-level English classification benchmarks with 500 labeled examples, CurCon improves average accuracy to 88.9 vs. 87.8 for CERT and 85.1 for standard fine-tuning. Ablations suggest the curriculum contributes ~0.8 points.

Strengths:
- Clear, simple idea that integrates smoothly with CERT-style pipelines; no inference overhead.
- Consistent improvements across four datasets and five seeds; helpful ablations (fixed mixture, reversed curriculum, removal of back-translation).
- Sensible analysis of label-budget sensitivity (100/500/1,000 labels), showing larger gains when labels are scarce.
- Well-written and easy to follow; implementation details and limitations are stated.

Weaknesses:
- Novelty is incremental: curriculum on augmentation strength for contrastive learning is established in vision; the extension to NLP is straightforward.
- Limited experimental scope: only sentence-level English datasets, only BERT-base; no evaluation on longer texts or other domains/languages; no larger or decoder-only encoders.
- Baseline fairness concerns: CurCon uses per-dataset grid search (48 configs) while baselines appear to use hyperparameters from original papers without comparable tuning on the same validation sets; this can inflate CurCon’s relative gains.
- Modest absolute gains over CERT (≈1.1 avg), which may fall within expected variance for small datasets; no statistical significance testing beyond mean±std.
- Limited schedule analysis: only linear schedule is tested; no sensitivity curves for curriculum length, operator probabilities, or alternative schedules (e.g., cosine, stepwise, adaptive).
- Missing comparisons to stronger/semi-recent low-resource baselines (e.g., PET/ADAPET, consistency-based variants beyond UDA, supervised contrastive fine-tuning, or adapter-based approaches), and to more modern sentence encoders.

Questions/suggestions:
- Tune baselines on the same validation protocol as CurCon to ensure fairness; report validation-tuned performance and compute budgets.
- Provide sensitivity analyses for curriculum length and schedule shapes; consider adaptive schedules.
- Include larger/backbone variants (RoBERTa-large, DeBERTa, modern encoder-only models) and at least one non-English dataset.
- Add statistical significance testing across seeds.
- Report how many back-translated views are precomputed per example and any filtering; analyze the effect of each operator’s strength (not just presence/absence).

Scores (0–100):
- Soundness: 78
- Novelty: 66
- Significance: 70
- Clarity: 88

Final average score: 75.5

Recommendation: Reject

Rationale: While the paper is clearly written and demonstrates consistent albeit modest gains with a sensible curriculum, the contribution is incremental and the empirical scope is narrow. Baseline tuning fairness is a notable concern. Strengthening the evaluation breadth, ensuring fair hyperparameter tuning, and providing deeper schedule analyses would make the case for acceptance stronger.