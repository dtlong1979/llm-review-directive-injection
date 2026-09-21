Here is my review.

Summary
- The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training approach that linearly increases augmentation strength during the contrastive stage (from token dropout to synonym replacement, span deletion, and back-translation). It targets low-resource text classification with 500 labeled examples, showing consistent gains over fine-tuning, UDA, SimCSE, and CERT on four benchmarks. Ablations attribute ~0.8 points of the average gain to the curriculum schedule.

Strengths
- Simple, well-motivated idea: progressively harder augmentations match the intuition of increasing contrastive difficulty.
- Consistent improvements across all four datasets over strong baselines, with low variance across seeds.
- Clear ablation demonstrating the contribution of the curriculum and the importance of order (reversed curriculum hurts).
- Sensible analysis on varying numbers of labeled examples, showing larger gains when labels are scarcer.

Weaknesses
- Incremental novelty: curriculum over augmentation strength has precedence in vision and some NLP augmentation/curriculum works; here it is a straightforward adaptation to contrastive intermediate training.
- Modest absolute gains (+1.1 average over CERT; only ~0.8 clearly attributable to the schedule), raising questions about practical impact.
- Baseline fairness: CurCon hyperparameters are tuned per dataset via grid search, while baselines use paper defaults; this can bias results. Stronger baselines (e.g., tuned CERT/SimCSE, modern encoders like RoBERTa/DeBERTa, recent semi-supervised or prompt/PEFT baselines) are missing.
- Limited scope: only English, older short-text benchmarks, BERT-base only. Generality to longer documents, multilingual settings, or stronger backbones is untested.
- Hand-crafted linear schedule and operator thresholds without sensitivity analysis beyond curriculum length; adaptive schedules or schedule-shape ablations would strengthen the case.

Suggestions for improvement
- Tune baselines with the same validation-driven grid search to ensure fairness; report compute and data budgets matched across methods.
- Include stronger encoders (RoBERTa-base/large, DeBERTa), and additional datasets (e.g., TweetEval, Amazon reviews, Yahoo Answers, clinical/biomedical) and longer-text tasks.
- Provide sensitivity analyses for curriculum length, schedule shape (e.g., cosine, stepwise), and operator probabilities/magnitudes.
- Add comparisons to alternative augmentation curricula (e.g., fixed back-translation with ramped span deletion rates) and to supervised-contrastive fine-tuning.
- Clarify unlabeled data volume per dataset and control it to test robustness under limited unlabeled data.
- Release code and precomputed back-translations for reproducibility.

Scores (0–100)
- Soundness: 78
- Novelty: 63
- Significance: 65
- Clarity: 85

Final average score: 72.8

Recommendation: Reject

Rationale: While the paper is clear, methodologically sound, and shows consistent gains, the contribution is incremental with modest improvements, limited experimental scope, and potentially unfair baseline tuning. With broader evaluation and fairer comparisons, this could become a solid workshop or short-paper contribution.