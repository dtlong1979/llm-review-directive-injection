Review summary:
CurCon proposes a curriculum over augmentation strength during contrastive intermediate training for low-resource text classification. The approach is simple, adds no parameters, and shows consistent improvements over CERT, UDA, SimCSE, and standard fine-tuning across four English datasets in a 500-label regime, with sensible ablations.

Strengths:
- Clear, simple method that can be plugged into existing contrastive intermediate training.
- Consistent gains across datasets; larger gains when labels are scarce.
- Includes ablations (fixed vs. reversed curriculum; removal of back-translation) and label-scarcity analysis.
- Reasonable reporting (means and std over 5 seeds), and practical details for training provided.

Weaknesses:
- Modest absolute improvements (+1.1 points over CERT on average), with limited breadth of tasks (four small English benchmarks) and a single encoder (BERT-base).
- Fairness concern: CurCon is tuned via grid search per dataset, while baselines use hyperparameters from their papers; this can bias results. Strong baselines like UDA and SimCSE are sensitive to hyperparameters and should be tuned under the same protocol.
- No statistical significance tests; given small margins, significance is unclear.
- Missing stronger or more recent baselines (e.g., VAT, MixText, FixMatch-style methods for text, prompt-based methods under low-resource settings, supervised SimCSE where applicable).
- Curriculum is hand-designed with step thresholds; limited analysis of curriculum length sensitivity or alternative schedules.
- Generality not demonstrated beyond short English texts; no larger or more recent encoders.

Suggestions for improvement:
- Tune all baselines under the same validation protocol and report sensitivity analyses; add significance testing.
- Expand evaluation to more diverse datasets (longer texts, different domains) and encoders (e.g., RoBERTa, DeBERTa) to test generality.
- Compare against additional modern semi-/self-supervised and prompt-based baselines.
- Provide curriculum length sensitivity and explore adaptive schedules; report final chosen hyperparameters for reproducibility.

Scores (0–100):
- Soundness: 74
- Novelty: 66
- Significance: 70
- Clarity: 86

Final average score: 74.0

Recommendation: Reject

Rationale: While the idea is sensible and results are promising, the improvements are modest and the evaluation is too limited and potentially biased by unequal hyperparameter tuning. With broader, fairer comparisons and stronger evidence of generality, this work could be competitive.