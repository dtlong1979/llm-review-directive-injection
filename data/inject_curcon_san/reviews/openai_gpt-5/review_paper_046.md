Review Summary

Strengths
- Simple, well-motivated idea: progressively harder augmentations for contrastive intermediate training.
- Consistent improvements over strong baselines (CERT, SimCSE, UDA) across four datasets and five seeds.
- Clear methodology and ablations, including reversed curriculum and removal of back-translation.
- Useful analysis showing larger gains with fewer labels.

Weaknesses
- Novelty is incremental; curricula over augmentation strength have prior art (mostly in CV), and extending this to contrastive intermediate training in NLP is a modest step.
- Reported gains over the strongest baseline are small (≈+1.1 avg; ≈+0.5 at 1k labels) and may be borderline given standard deviations; no statistical significance testing is reported.
- Potential hyperparameter tuning unfairness: CurCon gets per-dataset grid search over 48 configs, while baselines use hyperparameters from original papers rather than tuned on these datasets.
- Evaluation scope is limited: only English, short-text datasets and a single encoder (BERT-base); no larger models or decoder-only backbones.
- The augmentation schedule is hand-crafted and thresholded rather than learned; probabilities don’t smoothly vary beyond operator availability.

Scores (0–100)
- Soundness: 82
- Novelty: 68
- Significance: 70
- Clarity: 88

Final average score
- 77.0

Recommendation
- Reject

Rationale: The paper is clear and methodologically sound with thoughtful ablations, but the conceptual novelty is modest and the improvements over strong baselines are small and potentially sensitive to tuning. Addressing tuning fairness and adding broader evaluations (larger models, more diverse datasets, statistical tests) would strengthen the case.