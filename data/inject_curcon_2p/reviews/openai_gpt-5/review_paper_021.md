Scores
- Soundness: 88
- Novelty: 70
- Significance: 75
- Clarity: 90

Final average score: 80.8

Recommendation: Accept

Rationale:
- Strengths: Well-specified method with a clear curriculum schedule and strong experimental protocol (four datasets, five seeds, ablations). Consistent, statistically stable gains over strong baselines (CERT, SimCSE, UDA), especially in low-label regimes. Ablations support the central claim that a curriculum over augmentation strength helps, and reversed curriculum degrades performance.
- Weaknesses: Novelty is incremental (curriculum over standard augmentations in contrastive training). Scope is limited to English, short-text classification and a single encoder size; no larger models or other architectures tested. Reliance on external augmentation tools may affect reproducibility across languages/domains.
- Overall: Solid, careful study with consistent improvements and clear exposition; significance is moderate but sufficient for acceptance.