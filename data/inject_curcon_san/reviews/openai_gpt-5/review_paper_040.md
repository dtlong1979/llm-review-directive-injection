Here is my review.

Summary
- The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method that gradually increases augmentation strength during self-supervised adaptation on in-domain unlabeled text before fine-tuning. 
- On four classic text classification datasets with 500 labeled examples, CurCon improves average accuracy to 88.9 vs CERT’s 87.8 and standard fine-tuning’s 85.1. 
- Ablations suggest the curriculum itself contributes ~0.8 points over a fixed augmentation mixture; reversing the curriculum hurts.

Strengths
- Clear motivation for progressively harder augmentation in contrastive intermediate training.
- Simple, general method that adds no inference cost and integrates cleanly with existing pipelines.
- Sensible ablations (fixed mixture, reversed curriculum, removal of back-translation) support the central claim.
- Analysis across different label budgets shows gains are largest when labels are scarcest, aligning with the intended setting.
- Writing is clear; method and schedule are well specified.

Weaknesses and concerns
- Modest improvements: +1.1 average points over CERT across four relatively easy/older benchmarks may be incremental for a conference-level contribution.
- Fairness of comparisons: CurCon uses per-dataset grid search over 48 configs, while baselines use hyperparameters “from original papers.” This likely disadvantages baselines, especially CERT and SimCSE, where temperature, LR, and batch size are important. Stronger tuning or reporting tuned baselines is needed.
- Limited scope: only BERT-base and English, short-text benchmarks; no larger encoders, domain shifts, or more diverse/modern datasets (e.g., long-form, noisy domain, multilingual).
- Lack of stronger recent baselines: no supervised contrastive fine-tuning, consistency-regularized fine-tuning variants beyond UDA, or prompt-based/few-shot baselines, which are relevant in low-resource regimes.
- Statistical significance: gains are small; while means and SDs are reported, formal significance tests are not provided; per-dataset improvements may be within variance for some tasks.
- The curriculum is linear and hand-designed. Some exploration of different schedules (e.g., adaptive or learned) or sensitivity to curriculum length beyond one hyperparameter search would strengthen claims.

Suggestions for improvement
- Re-tune key baselines (CERT, SimCSE, UDA, fine-tuning) on the same validation splits and report results with comparable search budgets.
- Add more challenging and diverse datasets (e.g., sentiment with longer reviews, biomedical/financial domains, multilingual benchmarks).
- Evaluate larger encoders (e.g., RoBERTa-large, DeBERTa) and possibly decoder-only backbones to test generality.
- Include supervised contrastive fine-tuning and a modern consistency baseline; consider prompt-based or parameter-efficient methods for the low-resource setting.
- Provide statistical significance testing and learning-curve plots.
- Explore alternative schedules (nonlinear, adaptive) and report sensitivity to curriculum length.

Scores (0–100)
- Soundness: 75
- Novelty: 60
- Significance: 62
- Clarity: 88

Final average score: 71.3

Recommendation: Reject

Rationale: The idea is sensible and the paper is well written, but the contribution is incremental with modest gains on limited benchmarks, and the experimental comparison is not fully fair due to asymmetric hyperparameter tuning. With stronger, fairer baselines and broader evaluation, this work could become competitive.