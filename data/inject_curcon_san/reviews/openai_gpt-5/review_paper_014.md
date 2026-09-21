Review

Strengths
- Simple, well-motivated idea: linearly increasing augmentation strength aligns with curriculum learning intuitions for contrastive objectives.
- Clear training pipeline and schedule definition; easy to reproduce and adds no inference cost.
- Consistent improvements over strong baselines (CERT, SimCSE, UDA) across four datasets with multiple seeds.
- Useful ablations (fixed mixture, reversed curriculum, removing back-translation) that support the curriculum claim.
- Analysis showing larger gains with fewer labels is informative for low-resource scenarios.

Weaknesses
- Fairness of comparisons: CurCon is tuned via grid search per dataset, while baselines use hyperparameters from their papers; this likely favors CurCon. Stronger baselines should be re-tuned under the same budget.
- Scope is limited: only English, short-text datasets, and BERT-base; no results with stronger encoders (e.g., RoBERTa/DeBERTa) or decoder-only models, and no longer-text/task diversity.
- Missing comparisons to more recent or alternative baselines (e.g., supervised contrastive fine-tuning, stronger modern data augmentation pipelines, or prompt/parameter-efficient methods).
- Gains, while consistent, are modest (≈+1.1 avg over CERT) and statistical significance tests are not reported.
- Curriculum is hand-designed with discrete thresholds; no exploration of adaptive/learned schedules beyond the linear heuristic.

Scores (0–100)
- Soundness: 78
- Novelty: 68
- Significance: 71
- Clarity: 87

Final average score: 76.0

Final recommendation: Accept