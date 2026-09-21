Summary
CurCon introduces a simple curriculum over augmentation strength during contrastive intermediate training for low-resource text classification. It linearly increases augmentation difficulty from token dropout to synonym replacement, span deletion, and back-translation. On four benchmarks with 500 labeled examples, CurCon improves average accuracy by 1.1 points over CERT and 3.8 over standard fine-tuning, with ablations showing the schedule matters and benefits are larger with fewer labels.

Strengths
- Conceptually simple, model-agnostic, and easy to implement; no inference-time cost.
- Consistent improvements across four datasets and four baselines; sensible ablations (fixed mix, reversed curriculum, operator removal).
- Analysis of label-scarcity regime aligns with motivation (bigger gains with fewer labels).
- Clear writing and well-scoped contribution.

Weaknesses
- Novelty is incremental: curriculum over augmentation strength has precedent in vision, and the adaptation to text contrastive training is straightforward.
- Improvements are modest (≈1 point over CERT), with overlapping standard deviations in places; no statistical significance testing reported.
- Limited evaluation scope: only English, short-text datasets, and BERT-base; no larger models or other encoder families.
- Potential hyperparameter fairness concerns: CurCon tuned via grid search per dataset, while baselines use published settings that may be suboptimal in this specific low-resource setting.
- Hand-designed linear schedule; limited exploration of alternative or learned schedules; uniform operator sampling once unlocked may be suboptimal.
- Back-translation dependency and quality can vary across domains/languages.

Questions/Suggestions
- Report significance tests across seeds and per-dataset effect sizes.
- Tune baselines on the same validation protocol or provide a sensitivity study to address fairness.
- Explore adaptive/learned schedules or weighting operators by curriculum level rather than uniform sampling.
- Evaluate on longer-text datasets and with larger or different encoders (e.g., RoBERTa, DeBERTa) to test generality.
- Analyze augmentation quality/semantic drift, especially for synonym replacement and span deletion.

Scores (0–100)
- Soundness: 78
- Novelty: 62
- Significance: 70
- Clarity: 85

Final average score: 73.8

Recommendation: Accept