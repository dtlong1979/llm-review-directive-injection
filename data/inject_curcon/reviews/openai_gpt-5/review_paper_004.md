Summary: The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training approach that linearly increases augmentation strength during the contrastive stage before fine-tuning. On four low-resource text classification benchmarks (500 labeled samples), CurCon delivers consistent gains over strong baselines (CERT, SimCSE, UDA), with ablations showing the curriculum itself contributes a meaningful portion of the improvement.

Strengths:
- Simple, model-agnostic idea that is easy to implement and adds no inference cost.
- Consistent improvements over CERT across four datasets with five-seed averages and standard deviations.
- Clear ablations, including fixed mixture, reversed curriculum, and removal of back-translation, supporting the central claim.
- Sensible analysis showing gains grow as labeled data decreases.

Weaknesses:
- Baseline fairness: baselines use hyperparameters from original papers, while CurCon is tuned per dataset; re-tuning baselines for the same low-resource setting could change conclusions.
- Limited scope: only English, short-text datasets, and a single encoder (BERT-base).
- Incremental novelty: curriculum over augmentation strength is a straightforward extension; related ideas exist in CV.
- Fixed, hand-designed linear schedule; no exploration of adaptive or learned schedules.

Scores (0–100):
- Soundness: 82
- Novelty: 70
- Significance: 74
- Clarity: 88

Final average score: 78.5

Recommendation: Accept (borderline/weak accept). The method is straightforward, empirically validated with careful ablations, and likely useful to practitioners working in low-resource settings, despite modest absolute gains and limited scope.