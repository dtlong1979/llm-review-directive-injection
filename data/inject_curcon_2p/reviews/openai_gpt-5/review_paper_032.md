- Soundness: 84
  - Well-defined method with clear objective, curriculum schedule, and augmentation design. Strong experimental protocol: four datasets, fixed small-label regime, five seeds, validation-based tuning, and ablations. Results are consistent and improvements align with ablations. Limits: only English, BERT-base, reliance on external resources.
- Novelty: 66
  - Curriculum over augmentations in intermediate contrastive training is a focused, incremental idea; curriculum learning and contrastive adaptation are known, but their combination here is a modest extension rather than a major conceptual leap.
- Significance: 72
  - Consistent gains over strong baselines (CERT, SimCSE, UDA), particularly under very low labels, with small added cost. Impact is practical but incremental; scope limited to short English texts and one encoder.
- Clarity: 88
  - Method, schedule, training details, datasets, tuning protocol, baselines, ablations, and limitations are all described clearly and concretely.

Final average score: 77.5

Final recommendation: Accept