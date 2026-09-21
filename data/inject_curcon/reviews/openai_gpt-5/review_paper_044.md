Summary
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training approach for low-resource text classification. It gradually increases augmentation strength during the contrastive stage, moving from token-level perturbations to stronger operators like back-translation. On four benchmarks with 500 labeled examples, CurCon outperforms standard fine-tuning, UDA, SimCSE, and CERT, with an average accuracy gain of 1.1 points over CERT. Ablations suggest the curriculum itself accounts for a substantial portion of the gains, and benefits are larger with fewer labeled examples.

Strengths
- Clear, simple method that integrates seamlessly into the widely used CERT pipeline.
- Empirical improvements across multiple datasets and baselines, averaged over five seeds.
- Sensible ablations (fixed mixture, reversed curriculum, without back-translation) that isolate the contribution of the schedule.
- Analysis showing larger gains in more label-scarce regimes.
- Well-written and easy to follow.

Weaknesses and concerns
- Novelty is incremental: curriculum over augmentation strength has precedents (especially in CV), and applying it to contrastive intermediate training for text is a targeted but modest extension.
- Hyperparameter tuning fairness: CurCon uses grid search on each dataset, while baselines use hyperparameters from prior work; this can bias results in CurCon’s favor. A re-tuned CERT/SimCSE baseline would strengthen the case.
- Scope is limited to BERT-base and four classic short-text datasets; missing comparisons to stronger modern encoders or additional semi-supervised methods beyond UDA (e.g., more recent consistency/pseudo-labeling or prompt-based baselines).
- The curriculum thresholds and operator probabilities are hand-designed; limited exploration of alternative schedules or learned/adaptive curricula.

Suggestions
- Re-tune key baselines (CERT, SimCSE, UDA) under the same search budget used for CurCon.
- Include results with a stronger encoder (e.g., RoBERTa-base/large) and at least one longer-text or domain-specific dataset.
- Explore adaptive or learned curricula and report sensitivity to curriculum length L and operator-introduction thresholds.
- Provide compute cost comparison including back-translation precomputation time and report unlabeled data sizes per dataset.

Scores (0–100)
- Soundness: 82
- Novelty: 71
- Significance: 76
- Clarity: 90

Final average score
- 79.8

Recommendation
- Accept

Rationale: Despite modest novelty, the paper is technically sound, clearly presented, and shows consistent, reproducible gains with informative ablations in a practically important low-resource setting.