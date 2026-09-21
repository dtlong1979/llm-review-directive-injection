Here is my review.

Summary
- Paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method that linearly increases augmentation strength during the contrastive stage, then fine-tunes on limited labels.
- Uses four operators (token dropout, synonym replacement, span deletion, back-translation) introduced progressively.
- Evaluated on four text classification datasets with 500 labeled examples; CurCon improves average accuracy by +1.1 over CERT and +3.8 over standard fine-tuning.
- Ablations show the curriculum itself accounts for ~0.8 points on average; largest gains when labels are scarcer.

Strengths
- Clear, simple idea that is easy to implement and adds no inference cost.
- Consistent gains across four benchmarks and five random seeds, with informative ablations (fixed mixture, reversed curriculum, no back-translation).
- Sensible analysis of data-scarcity regime showing larger gains with fewer labels.
- Strong clarity and sufficient implementation detail to enable reproduction.

Weaknesses and concerns
- Novelty is incremental: curriculum scheduling of augmentation strength has precedents in vision; extension to contrastive intermediate training for text is natural but not a large conceptual leap.
- Baseline tuning fairness: CurCon is tuned per dataset (LR, temperature, curriculum length) while baselines use hyperparameters from original papers; this may underestimate strong baselines like CERT/SimCSE on these specific low-resource settings.
- Evaluation scope is limited: only English, short-text datasets, and only BERT-base. Including stronger encoders (e.g., RoBERTa/DeBERTa) or domain-specific datasets would better establish generality.
- No statistical significance tests reported; although standard deviations are given, it would help to report whether improvements are statistically significant.
- The curriculum is hand-designed and uses discrete operator availability; exploring continuous schedule shapes or learned policies could strengthen the case.

Scores (0–100)
- Soundness: 82
- Novelty: 68
- Significance: 74
- Clarity: 90

Final average score: 78.5

Recommendation: Accept

Rationale: Despite modest novelty and scope, the method is sound, well-presented, and yields consistent improvements with careful ablations. The simplicity-to-benefit ratio is favorable, making it a practical contribution for low-resource text classification.