Summary
- Paper proposes CurCon: a curriculum-scheduled contrastive intermediate training method that linearly increases augmentation strength during the contrastive stage (token dropout → synonym replacement → span deletion → back-translation).
- Evaluated on four text-classification datasets with 500 labeled examples; shows +1.1 avg accuracy over CERT and +3.8 over standard fine-tuning. Ablations attribute ~0.8 points to the curriculum. Gains decrease as labeled data increase.

Strengths
- Clear, simple idea that aligns with curriculum learning intuition; easy to implement and adds no inference cost.
- Consistent improvements over multiple baselines across four datasets; includes ablations (fixed mix, reversed curriculum, no BT).
- Solid experimental hygiene: five seeds, mean±std, curriculum hyperparameter study, analysis vs. label count.
- Paper is well-written and organized; method details are mostly sufficient for reproduction.

Weaknesses/Concerns
- Baseline fairness: CurCon’s hyperparameters are tuned via grid search on validation sets, while baselines use settings from their papers. Equal tuning budgets for all methods would be more fair and could narrow the margins.
- Missing strong and common baselines for low-resource adaptation: task/domain-adaptive pretraining (TAPT/DAPT with MLM), and more recent contrastive or sentence-embedding methods (e.g., DeCLUTR/ConSERT) and supervised contrastive finetuning. Also absent are parameter-efficient methods and prompt-based finetuning which are relevant in low-resource regimes.
- Scope limited to BERT-base and short English texts; no results with stronger encoders (e.g., RoBERTa, DeBERTa) or decoder-only LMs, which could change relative gains.
- Reported gains over CERT are modest (avg +1.1) and the curriculum-specific gain is ~0.8 on average; with standard deviations ~0.6–1.0, the practical significance is moderate.
- Risk of validation overfitting given 200-example dev sets and 48-config grid searches per dataset.

Questions/Suggestions
- Provide results with equal hyperparameter tuning budgets for all baselines or a subset of key ones (CERT, UDA).
- Add DAPT/TAPT baselines and at least one stronger encoder (e.g., RoBERTa-base) to test robustness of conclusions.
- Report per-dataset results for the 100/1,000 label regimes and significance tests.
- Explore mixing multiple augmentations per view or adaptive/learned curricula to test if stronger gains are possible.

Scores (0–100)
- Soundness: 80
- Novelty: 68
- Significance: 72
- Clarity: 90

Final average score: 77.5

Recommendation: Reject
Rationale: The idea is clean and the results are promising, but the contribution is incremental and the experimental evidence is not yet strong enough due to baseline omissions and tuning fairness concerns. With stronger baselines, equal tuning, and broader evaluations, this could become a solid contribution.