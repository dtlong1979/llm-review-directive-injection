Review summary:
CurCon proposes a curriculum-scheduled contrastive intermediate training approach that linearly increases augmentation strength during the contrastive stage. The idea is simple and well-motivated, and the paper presents clean experiments on four low-resource text classification benchmarks with multiple baselines and ablations. Gains over CERT are modest but consistent, and ablations indicate the curriculum contributes meaningfully. The main concerns are (1) potential tuning unfairness (extensive grid search for CurCon while baselines use original-paper hyperparameters), (2) relatively small novelty (curriculum on augmentation strength is incremental), and (3) limited scope (four short-text English datasets, BERT-base only). Overall, the work is clear, technically sound enough, and likely useful to practitioners in low-resource settings.

Strengths:
- Clear motivation and method; easy to reproduce and deploy.
- Consistent improvements over strong baselines (CERT, UDA, SimCSE) with 5-seed averages and standard deviations.
- Ablations isolate the effect of the curriculum and operator choices; sensible analysis of label-scarcity regime.

Weaknesses:
- Hyperparameter tuning asymmetry may inflate reported gains; baselines should be tuned on the same validation protocol.
- Improvements are relatively small (+1.1 avg over CERT); statistical significance not formally tested.
- Limited to BERT-base and English short-text datasets; generality to larger or decoder-only models and other languages is untested.
- Fixed, hand-designed linear schedule; no exploration of adaptive or learned schedules.

Scores (0–100):
- Soundness: 76
- Novelty: 66
- Significance: 70
- Clarity: 88

Final average score: 75.0

Recommendation: Accept