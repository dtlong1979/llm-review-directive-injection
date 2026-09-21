Here is my review.

Summary
- Proposes CurCon, a curriculum-scheduled contrastive intermediate training method that linearly increases augmentation strength (token dropout → synonym replacement → span deletion → back-translation) during contrastive pretraining on unlabeled in-domain text.
- Evaluated on four low-resource classification benchmarks (500 labels each), outperforming fine-tuning, UDA, SimCSE, and CERT by 1.1 points on average over CERT, with consistent gains across datasets.
- Includes ablations (curriculum vs fixed mix, reversed schedule, no back-translation) and analysis across label budgets (100/500/1,000).

Strengths
- Simple, orthogonal idea that is easy to adopt and adds no inference cost.
- Consistent improvements across four datasets and five seeds; clear attribution of gains to the curriculum via ablations.
- Sensible analysis of label-scarce regimes showing larger benefits when labels are fewer.
- Clear method description (operators, schedule, training details), and reasonable experimental protocol for the target setting.

Weaknesses and concerns
- Modest absolute gains (+1.1 average over CERT; 0.5–1.6 depending on label budget). Effect sizes are small relative to standard deviations for some datasets.
- Baseline tuning fairness: CurCon uses grid search per dataset, while baselines use hyperparameters from original papers; stronger baselines might benefit from equal tuning on the same validation sets.
- Limited breadth: only English, short-text datasets, and BERT-base; no evaluation on larger encoders or contemporary strong encoders (e.g., RoBERTa/E5/Contriever) or adapter-based PEFT in low-resource settings.
- Missing some relevant contrastive NLP baselines beyond SimCSE and CERT (e.g., ConSERT, DeCLUTR, TSDAE), which could contextualize gains.
- Hand-crafted linear schedule; no exploration of learned or adaptive schedules, or operator mixing weights beyond uniform once “available.”

Suggestions for improvement
- Re-tune baselines on the same validation sets for fairness; report tuned results alongside original hyperparameters.
- Add comparisons to additional contrastive baselines and to a stronger backbone (e.g., RoBERTa-base) to test generality.
- Report statistical significance tests and possibly effect sizes.
- Explore adaptive or learned curricula and non-uniform operator sampling; analyze training dynamics (e.g., alignment/uniformity, representation robustness) to justify the curriculum mechanism.
- Evaluate on longer-text and multilingual datasets; consider domains where back-translation quality varies.

Scores (0–100)
- Soundness: 78
- Novelty: 66
- Significance: 72
- Clarity: 88

Final average score: 76.0

Recommendation: Accept

Rationale: Although the contribution is incremental and gains are modest, the idea is simple, well-motivated, and consistently helpful in the intended low-resource setting, with solid ablations and analysis. With stronger baseline tuning and broader evaluation, this could be a solid, practical contribution.