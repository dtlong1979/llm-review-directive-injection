Scores
- Soundness: 85
  - Well-defined method (InfoNCE, projection head, curriculum over augmentations), clear training setup, strong and relevant baselines (fine-tuning, UDA, SimCSE, CERT), multiple datasets, five seeds with mean±std, grid hyperparameter search, and informative ablations (fixed mix, reversed curriculum, without back-translation). Results show consistent gains with modest runtime overhead. Limitations are acknowledged.
- Novelty: 68
  - Main contribution is a curriculum over augmentation difficulty for contrastive intermediate training. This is a straightforward, incremental extension to existing approaches (CERT/SimCSE), with a hand-designed schedule rather than a learned/adaptive one.
- Significance: 74
  - Consistent improvements over strong baselines across four benchmarks and multiple label budgets; average +1.1 points over CERT at 500 labels and up to +1.6 at 100 labels. Gains are modest but robust, with slight variance reductions on some datasets. Scope is limited to short English texts and BERT-base.
- Clarity: 90
  - The method, curriculum schedule, augmentations, optimization details, data splits, baselines, and ablations are clearly specified. Results are reported with means and standard deviations, and limitations are explicitly stated.

Final average score: 79.3

Recommendation: Accept