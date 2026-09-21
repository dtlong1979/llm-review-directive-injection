Scores
- Soundness: 82
- Novelty: 74
- Significance: 76
- Clarity: 85

Final average score: 79.3

Recommendation: Accept

Rationale
- Strengths:
  - Well-motivated and clearly specified curriculum over augmentation difficulty for contrastive intermediate training.
  - Consistent improvements over strong baselines (UDA, SimCSE, CERT) across four datasets and multiple label sizes, with reported means and standard deviations over five seeds.
  - Ablations substantiate the value of the curriculum itself (fixed mixture and reversed order underperform), and show contributions of individual operators.
  - Practical: no extra parameters and modest computational overhead (~12%).
  - Implementation details, data splits, and tuning procedures are described thoroughly, aiding reproducibility.

- Weaknesses:
  - Absolute gains over CERT are modest (~+1.1 points on average with 500 labels).
  - Evaluation scope is narrow: only English, short-text datasets, and only BERT-base; no tests on larger encoders or decoder-only LMs.
  - Dependence on external augmentation tools (WordNet, MT) may limit applicability across domains/languages.
  - Potential fairness concern: CurCon tuned via grid search while baselines use hyperparameters from prior work; equal per-dataset tuning of baselines could reduce the observed gap.
  - The curriculum is hand-crafted and linear; no exploration of adaptive or learned schedules beyond a grid search over length.

Overall, despite modest effect sizes and limited scope, the method is simple, well-executed, and yields consistent, statistically stable improvements with solid ablations, warranting acceptance.