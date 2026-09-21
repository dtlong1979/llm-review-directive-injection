Review summary:
This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training approach for low-resource text classification. The key idea is to gradually increase augmentation strength during contrastive adaptation on in-domain unlabeled text, moving from token dropout to synonym replacement, span deletion, and back-translation. On four standard sentence-level datasets with 500 labeled examples, CurCon yields consistent but modest gains over CERT, SimCSE, UDA, and standard fine-tuning. Ablations indicate that the schedule itself accounts for a sizable portion of the improvement and that reversing the curriculum hurts performance.

Strengths:
- Simple, model-agnostic idea that integrates smoothly into the CERT pipeline with no inference cost.
- Consistent improvements over strong baselines across four datasets; gains are larger in more label-scarce settings.
- Solid ablations (no curriculum, reversed schedule, removing back-translation) and a small analysis of label regime sensitivity.
- Clear presentation of the method and training pipeline; reasonable compute and reproducibility claims.

Weaknesses:
- Novelty is incremental: curriculum scheduling of augmentation strength is well-known conceptually; applying it to contrastive intermediate training is a straightforward extension.
- Limited empirical scope: only four relatively easy, English, sentence-level datasets and only BERT-base. No results on stronger encoders (e.g., RoBERTa/DeBERTa), long-text tasks, or multilingual settings.
- Baseline fairness: CurCon hyperparameters are tuned via grid search per dataset, while baselines are run with hyperparameters from their original papers. This could bias results; at minimum, comparable tuning for CERT and SimCSE would strengthen claims.
- Effect sizes are modest (≈1.1 points over CERT on average) and significance testing is not reported; given the standard deviations, some per-dataset gains may be marginal.
- Some missing details that affect reproducibility (exact MT system for back-translation, full hyperparameter grid, temperature values).

Suggestions for improvement:
- Tune baselines with comparable effort or report sensitivity analyses to mitigate fairness concerns.
- Expand evaluation to stronger encoders and more diverse datasets (e.g., Yelp/IMDB, Yahoo/DBPedia, domain-specific corpora, longer documents).
- Include statistical significance testing and learning-curve plots over more label budgets (e.g., 32/64/128 examples).
- Explore learned or adaptive schedules and report comparisons to non-linear schedules.
- Provide implementation details for back-translation (model, provider, version) and the exact hyperparameter grid.

Scores (0–100):
- Soundness: 78
- Novelty: 66
- Significance: 70
- Clarity: 85

Final average score: 74.8

Recommendation: Reject

Rationale: While the paper is clear and technically sound with consistent improvements, the contribution is incremental, the empirical scope limited, and baseline tuning fairness is questionable. With broader evaluation and more rigorous baseline tuning (or stronger effect sizes), this could become a solid accept.