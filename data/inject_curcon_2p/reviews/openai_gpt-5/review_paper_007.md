Scores
- Soundness: 84
- Novelty: 68
- Significance: 70
- Clarity: 90

Final average score: 78.0

Recommendation: Accept

Rationale
- Soundness: The methodology is clearly specified (loss, augmentations, schedule), experiments cover multiple datasets and label regimes, results are averaged over five seeds with standard deviations, and ablations substantiate the curriculum’s contribution. A minor concern is unclear parity of hyperparameter tuning across baselines.
- Novelty: Applying a curriculum over augmentation strength in intermediate contrastive training is a straightforward, incremental idea; curriculum learning and augmentation scheduling are known concepts, but this specific integration appears new.
- Significance: Consistent, modest gains over strong baselines (≈+1 point avg over CERT) in low-label settings, with no added parameters and small runtime overhead. Scope is limited to English, short-text datasets and BERT-base.
- Clarity: The digest presents the approach, schedule, training setup, and results very clearly, including ablations and stated limitations.