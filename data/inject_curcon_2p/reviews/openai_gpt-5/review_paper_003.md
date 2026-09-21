Scores
- Soundness: 81
- Novelty: 72
- Significance: 75
- Clarity: 88

Final Average Score: 79.0

Recommendation: Accept

Rationale
- Strengths: The paper presents a simple, well-motivated curriculum over augmentation strength for intermediate contrastive training and shows consistent improvements across four benchmarks and multiple label sizes. Experimental methodology appears solid: five seeds with mean±std, clear implementation details, competitive baselines, and informative ablations (fixed mixture and reversed curriculum underperform, back-translation contributes). The approach adds no parameters and has modest overhead.
- Weaknesses: Gains over the strongest baseline (CERT) are modest (~1.1 points on average). Evaluation is confined to English, short-text datasets, and BERT-base, limiting external validity. The curriculum is hand-designed rather than adaptive. It is not explicitly stated whether baseline hyperparameters received equally extensive tuning, raising a potential fairness concern.
- Overall: Despite modest gains and limited scope, the method is clear, technically sound, and practically useful for low-label text classification, warranting acceptance.