Scores
- Soundness: 82
  - Well-defined method, appropriate baselines, five-seed means/stds, and ablations (fixed mix, reversed curriculum, no BT). Minor concern: CurCon hyperparameters tuned via larger grid than baselines, and scope limited to BERT-base/English short texts.
- Novelty: 70
  - Applying a curriculum over augmentation difficulty to contrastive intermediate training is a reasonable but incremental idea; curriculum learning and the operators themselves are known.
- Significance: 74
  - Consistent gains over strong baselines (≈+1.1 avg over CERT) across four datasets and varying label counts; practical, modest impact given limited settings.
- Clarity: 88
  - Clear problem framing, method description, training details, datasets, metrics, and limitations.

Final average score: 78.5

Recommendation: Accept