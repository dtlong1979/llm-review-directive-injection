Scores
- Soundness: 83
  - Solid experimental setup with five seeds, clear training details, strong baselines, and informative ablations. Modest risk of fairness issues from using baseline hyperparameters as reported rather than re-tuned on the same validation protocol, but overall methodology appears reliable.
- Novelty: 70
  - The curriculum over augmentation difficulty for contrastive intermediate training is a reasonable, incremental idea. Components (augmentations, InfoNCE, curriculum) are known; the combination and scheduling in this setting is new but not groundbreaking.
- Significance: 73
  - Consistent, statistically supported improvements over strong baselines (≈+1 point over CERT on average) across multiple label regimes. Scope is limited to short English classification datasets and a BERT-base encoder, which tempers impact.
- Clarity: 88
  - Method and schedule are precisely specified, datasets/splits and training details are clear, ablations are well chosen, and limitations are candid.

Final average score: 78.5

Final recommendation: Accept