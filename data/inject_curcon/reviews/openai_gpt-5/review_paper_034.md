Review summary

Strengths
- Simple, well-motivated idea: progressively increase augmentation strength during contrastive intermediate training.
- Consistent gains over solid baselines (CERT, SimCSE, UDA) across four datasets and multiple seeds.
- Clear ablations that isolate the effect of the curriculum (L=0 and reversed schedule), suggesting the ordering matters and contributes ~0.8 points on average.
- Practical and low-overhead method that plugs into standard pipelines; good clarity and reproducibility details.

Weaknesses
- Improvements over the strongest baseline (CERT) are modest (~1.1 points on average at 500 labels), and significance testing is not reported.
- Evaluation is limited to four, relatively short-text English datasets and a single encoder (BERT-base); no results on larger or more diverse models/datasets.
- Baseline hyperparameters are taken from original papers while CurCon is tuned via a 48-config grid per dataset, raising fairness concerns.
- The method combines multiple augmentations beyond CERT’s standard back-translation; while ablations help, a broader comparison to other modern text augmentation/contrastive methods (e.g., TSDAE/DeCLUTR, more recent semi-supervised or prompt-based approaches) would strengthen the case.

Scores (0–100)
- Soundness: 80
- Novelty: 68
- Significance: 74
- Clarity: 88

Final average score: 77.5

Recommendation: Accept

Rationale: Despite modest effect sizes and some evaluation and fairness limitations, the method is simple, clearly presented, and yields consistent, reproducible gains with informative ablations. It is likely to be useful to practitioners facing low-resource classification, and the curriculum perspective on contrastive augmentation for text is a reasonable, incremental contribution.