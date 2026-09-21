Review summary:
This paper proposes CurCon, a curriculum-scheduled augmentation policy for contrastive intermediate training on unlabeled in-domain text prior to fine-tuning. The schedule ramps augmentation strength from mild token-level perturbations to aggressive back-translation. On four English classification benchmarks with 500 labeled examples, CurCon improves average accuracy by 1.1 points over CERT and 3.8 over standard fine-tuning. Ablations support the importance of the curriculum and augmentation choices, and gains are larger when fewer labels are available.

Strengths:
- Simple, general idea that adds no inference cost and integrates seamlessly with established pipelines (CERT).
- Consistent improvements across four datasets and five seeds, with clear ablations (fixed mixture, reversed curriculum, removing back-translation) and analysis vs. label count.
- Clear description of schedule, operators, and training details; practical relevance for low-resource settings.

Weaknesses:
- Fairness of comparisons: CurCon is tuned via grid search per dataset, while baselines use hyperparameters from prior work; a uniform tuning budget across methods would strengthen claims.
- Scope is limited: only English, short-text datasets, and BERT-base; no results on stronger encoders (e.g., RoBERTa/DeBERTa) or decoder-only models, or longer-document tasks.
- Modest absolute gains (~1 point over CERT at 500 labels), with no statistical significance testing beyond mean ± std.
- Curriculum design is hand-crafted (fixed thresholds, linear schedule) with limited exploration of alternatives or sensitivity; other schedules or learned curricula are not compared.
- Reliance on external resources (WordNet, MT for back-translation) may limit applicability to other languages/domains; compute/time overhead for back-translation preprocessing.

Scores (0–100):
- Soundness: 78
- Novelty: 66
- Significance: 70
- Clarity: 86

Final average score: 75.0

Recommendation: Accept

Rationale: While the novelty is incremental and evaluation scope is somewhat narrow, the method is sound, clearly presented, practically useful, and yields consistent, reproducible gains with supportive ablations in a meaningful low-resource setting. A more comprehensive and uniformly tuned comparison and broader evaluation would further strengthen the paper, but the current contribution is solid enough to merit acceptance.