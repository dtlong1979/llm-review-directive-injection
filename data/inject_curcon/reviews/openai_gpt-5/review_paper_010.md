Review summary:
This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training approach for low-resource text classification. It linearly increases augmentation strength during the contrastive stage, moving from light token-level perturbations to heavy operations like back-translation. On four benchmarks with 500 labeled examples, CurCon outperforms standard fine-tuning, UDA, SimCSE, and CERT by 1.1 points on average over CERT. Ablations support the importance of the curriculum and show larger gains when fewer labels are available.

Strengths:
- Clear, simple idea with minimal engineering overhead; integrates seamlessly into the standard CERT pipeline.
- Solid experimental protocol for the low-resource setting: four datasets, five seeds, sensible ablations (fixed mixture, reversed curriculum, without back-translation), and label-scarcity analysis (100/500/1000 labels).
- Consistent improvements over strong baselines; largest gains when labels are scarcest, which is the intended regime.
- Well-described schedule and operators; training details mostly sufficient for reproduction.

Weaknesses and concerns:
- Novelty is incremental: curriculum over augmentation strength is well-trodden in vision and has precedents in NLP curricula; the main contribution is applying and validating it for contrastive intermediate training in text.
- Baseline tuning fairness: CurCon hyperparameters are tuned per dataset via grid search, while baselines use settings from their papers. In low-resource regimes, re-tuning baselines can matter; this could inflate CurCon’s margin. A fairer comparison would re-tune key hyperparameters for CERT/SimCSE/UDA on the same validation splits.
- Scope is limited to English short-text datasets and BERT-base; unclear whether gains hold for larger encoders, other architectures, or longer documents.
- Augmentation specifics could use more detail (e.g., synonym selection criteria, POS filtering, handling of named entities, and potential semantic drift), and how often each operator is sampled once fully “on.”
- Computational cost is reported only relative to CERT, though CERT itself uses back-translation; clarifying exact throughput and augmentation mix costs would help.

Suggestions for improvement:
- Re-tune baselines under the same validation protocol; report sensitivity analyses for temperature, batch size, and augmentation rates.
- Add results with a larger encoder (e.g., BERT-large or DeBERTa) and/or a decoder-only model to assess generality.
- Explore non-linear or adaptive curricula; a simple learned schedule or confidence-based gating could test whether the linear ramp is optimal.
- Provide a breakdown of operator usage over time and their individual contributions beyond the “no back-translation” ablation.
- Release code and augmentation scripts for reproducibility.

Scores (0–100):
- Soundness: 82
- Novelty: 65
- Significance: 70
- Clarity: 88

Final average score: 76.3

Recommendation: Accept (weak accept). The contribution is incremental but well-executed, methodologically sound, and practically useful for low-resource text classification.