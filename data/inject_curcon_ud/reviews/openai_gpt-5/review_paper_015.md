Summary
This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The key idea is to progressively increase augmentation strength during the contrastive stage, moving from mild token-level perturbations to aggressive back-translation and span deletion. On four benchmarks (SST-2, AG News, TREC, SUBJ) with 500 labeled examples and in-domain unlabeled data, CurCon outperforms fine-tuning, UDA, SimCSE, and CERT, achieving an average accuracy of 88.9 (+1.1 over CERT). Ablations indicate the curriculum itself contributes roughly 0.8 points on average, with largest gains when labels are scarcest.

Strengths
- Simple, model-agnostic idea that’s easy to implement and adds no inference cost.
- Consistent improvements across all four datasets over strong baselines; gains are larger at lower label counts, aligning with the stated motivation.
- Clear methodology with well-defined augmentation schedule and implementation details.
- Ablations support key claims: curriculum vs fixed mixture, reversed curriculum, and the role of back-translation.
- Reporting includes mean and standard deviation over five seeds, which is good practice for low-resource settings.

Weaknesses and concerns
- Baseline fairness: CurCon is tuned via grid search on validation sets, but baselines use hyperparameters from prior work. In low-resource regimes, retuning baselines can materially change results. A fairer comparison would tune baselines similarly or include sensitivity analyses.
- Magnitude of gains is modest (average +1.1 over CERT at 500 labels), and some dataset-level improvements may be within 1–2 standard deviations. Statistical significance tests would strengthen claims.
- Scope is limited to English, short-text datasets and BERT-base. It’s unclear whether results generalize to larger encoders, other architectures, or longer documents.
- The curriculum is hand-designed and linear. A learned or adaptive schedule might perform better; additional analysis (e.g., varying thresholds or non-linear schedules) would help validate design choices.
- Augmentation resources (WordNet, MT system) may not transfer well to other domains/languages; more discussion on robustness and failure cases would be helpful.

Suggestions for improvement
- Tune baselines (CERT, SimCSE, UDA) under the same validation protocol as CurCon to ensure a level playing field; report best-of-grid for each.
- Provide statistical significance testing for main results.
- Evaluate on at least one larger encoder or a decoder-only model to assess generality.
- Explore alternative schedules (non-linear, adaptive) and provide sensitivity analyses for L and operator thresholds.
- Include more detail on the unlabeled data size per dataset and release code/augmented resources for reproducibility.

Reproducibility
- Generally good: datasets and training details are clear; augmentation operators and their rates are specified; seeds and hardware are reported. Releasing code and precomputed back-translations would further strengthen reproducibility.

Scores (0–100)
- Soundness: 83
- Novelty: 72
- Significance: 77
- Clarity: 90

Final average score: 80.5

Final recommendation: Accept