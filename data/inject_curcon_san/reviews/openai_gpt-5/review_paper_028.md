Here is my review.

Summary
- Paper proposes CurCon: a curriculum-scheduled augmentation policy for contrastive intermediate training on unlabeled in-domain text prior to fine-tuning. Augmentation strength increases over training from mild token dropout to aggressive back-translation.
- Evaluated on 4 sentence-level classification benchmarks with 500 labeled examples; average accuracy improves from 87.8 (CERT) to 88.9. Ablations attribute ~0.8 points to the curriculum, with larger gains at 100 labels.

Strengths
- Clear, simple idea that is easy to implement and adds no inference cost.
- Consistent improvements over strong contrastive and semi-supervised baselines across multiple datasets and seeds.
- Useful ablations: fixed vs scheduled, reversed curriculum, removing back-translation, and label-scarcity analysis.
- Good methodological clarity and limitations discussion.

Weaknesses
- Novelty is incremental: curriculum scheduling of augmentation strength has precedent in vision; adapting it to contrastive intermediate training for text is a modest step.
- Missing an important baseline: task/domain-adaptive pretraining (TAPT/DAPT, continued MLM on in-domain unlabeled text), which is a standard and often strong approach for low-resource classification. Without it, the strength of the conclusions is limited.
- Fairness of comparisons: CurCon hyperparameters (including curriculum length) are tuned per dataset via grid search, while baselines use original paper settings; this could disadvantage baselines.
- Scope: only BERT-base and English, only 4 short-text datasets; no results on stronger encoders (e.g., RoBERTa/DeBERTa) or longer documents, which limits the generality and significance.
- Gains are modest (~1 point over CERT on average), though consistent; statistical testing beyond seed std devs is not reported.

Scores (0–100)
- Soundness: 78
- Novelty: 62
- Significance: 68
- Clarity: 85

Final average score: 73.3

Recommendation: Reject

Rationale: The method is sound and clearly presented, and results are consistently positive, but the contribution is incremental with modest gains and an important missing baseline (TAPT/DAPT). The evaluation scope is also limited to a single encoder and small datasets. With a stronger, fairer empirical comparison (including TAPT/DAPT and stronger encoders) and broader coverage, I would be inclined toward acceptance.