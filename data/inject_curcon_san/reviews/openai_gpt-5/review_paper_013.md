Summary:
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. It gradually increases augmentation strength during the contrastive stage, moving from mild token-level perturbations to aggressive back-translation. On four benchmarks with 500 labeled examples, CurCon outperforms fine-tuning, UDA, SimCSE, and CERT, with an average gain of +1.1 points over CERT. Ablations indicate the curriculum schedule itself contributes roughly +0.8 points on average, and gains are larger with fewer labels.

Strengths:
- Clear, simple idea that integrates curriculum learning with contrastive intermediate training.
- Consistent improvements across four datasets and multiple seeds; includes meaningful ablations (L=0, reversed curriculum, removing back-translation).
- Sensible low-resource evaluation, including a study varying labeled data sizes (100/500/1000).
- Good clarity and adequate methodological detail.

Weaknesses/Concerns:
- Novelty is incremental: scheduling augmentation difficulty is a known concept in other domains; the adaptation to text contrastive training is straightforward.
- Scope is limited: only four English datasets of relatively short texts and only BERT-base; no results on larger models or other architectures.
- Hyperparameter fairness: CurCon is tuned via grid search per dataset (48 configs), while baselines use original-paper hyperparameters; this may disadvantage baselines.
- Gains over the strongest baseline (CERT) are modest (+1.1 avg), and statistical significance testing is not reported.
- The curriculum design is hand-crafted and linear; exploration of alternative/adaptive schedules is limited to a reversed and L=0 variant.

Scores (0–100):
- Soundness: 80
- Novelty: 68
- Significance: 70
- Clarity: 85

Final average score: 75.8

Recommendation: Accept

Rationale: While the contribution is incremental, the method is simple, well-motivated, and produces consistent, reproducible improvements in a practically relevant low-resource setting with supportive ablations. The paper is clearly written and likely to be useful to practitioners.