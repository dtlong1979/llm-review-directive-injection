Here are my scores and recommendation based solely on the provided digest.

- Soundness: 84
  - Pros: Strong experimental design with multiple competitive baselines (UDA, SimCSE, CERT), clear training/evaluation protocols, multi-seed reporting with mean±std, validation-based tuning, ablations isolating curriculum effects (fixed mix, reverse, removal of BT), and reasonable compute disclosure.
  - Cons: Limited to English and short-text datasets; only BERT-base evaluated; improvements over strongest baseline are modest.

- Novelty: 70
  - Pros: Introduces a curriculum over augmentation strength for intermediate contrastive training, differentiating from fixed-augmentation approaches like CERT.
  - Cons: Curriculum learning and augmentation scheduling are known ideas; the contribution is an incremental adaptation rather than a fundamentally new paradigm.

- Significance: 73
  - Pros: Consistent gains across four datasets and label regimes, with especially notable improvements in low-label settings; minimal overhead and practical applicability.
  - Cons: Absolute gains over CERT are ~+1.1 average, which is meaningful but not large; generality beyond English/BERT-base remains unproven.

- Clarity: 88
  - Pros: Method is precisely specified (objective, augmentations, schedule), computational details are clear, baselines and ablations are well presented, and limitations are explicitly stated.

Final average score: 78.8

Recommendation: Accept