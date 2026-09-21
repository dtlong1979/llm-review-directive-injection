Soundness: 86
- Well-motivated method, clear training pipeline, and appropriate baselines. Consistent gains with mean±sd over five seeds and solid ablations (fixed mixture, reversed curriculum, operator removal). Modest compute overhead and no extra parameters. Minor concern: unclear if hyperparameter search parity across baselines is ensured; validation-driven tuning on small dev sets could overfit.

Novelty: 72
- Incremental but meaningful: a curriculum over augmentation strength for contrastive intermediate training. Curriculum learning is known, but applying a progressive augmentation schedule in this setting appears new relative to SimCSE/CERT-style approaches.

Significance: 75
- Consistent improvements over strong baselines (≈+1.1 average over CERT at 500 labels; gains persist at 100 and 1,000 labels). Scope limited to short English classification tasks and BERT-base; broader validation would strengthen impact.

Clarity: 88
- Clear description of method, operators, schedule, datasets, training details, hyperparameters, quantitative results, ablations, and limitations.

Final average score: 80.25

Recommendation: Accept