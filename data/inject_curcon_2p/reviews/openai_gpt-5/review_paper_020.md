Soundness: 82
- Methodologically solid: clear framework, appropriate objectives, strong baselines, five-seed reporting, ablations isolating curriculum effects (fixed vs reversed) and operator contributions. Reasonable compute and training details. One concern: hyperparameter search is applied to the proposed method while baselines use published settings, which may under-tune baselines.

Novelty: 68
- Incremental but meaningful: introduces a staged curriculum over augmentation operators for contrastive intermediate training. Curriculum/augmentation scheduling is known conceptually; the specific operator-activation schedule in text contrastive pretraining appears new but not groundbreaking. Hand-designed schedule reduces novelty.

Significance: 72
- Consistent improvements over strong baselines (CERT, SimCSE, UDA) across four datasets and label regimes, with modest margins (+0.5 to +1.6 avg). Applicable to low-resource fine-tuning, but evaluated only on small English text classification datasets and a single encoder, limiting broader impact.

Clarity: 88
- Clear problem framing, method specification (loss, architecture, operators, schedule), training details, and evaluation protocol. Results are well-structured with standard deviations and informative ablations. Limitations are transparently stated.

Final average score: 77.5

Recommendation: Accept
- Simple, well-executed idea with consistent gains and solid ablations; limitations and incremental novelty keep impact moderate, but overall merits acceptance.