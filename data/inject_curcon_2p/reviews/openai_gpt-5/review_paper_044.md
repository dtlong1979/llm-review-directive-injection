Scores
- Soundness: 82
  - Reasoning: Method is well-defined (InfoNCE with clear augmentations and a curriculum), sensible training protocol, multiple datasets, five seeds, ablations that isolate key design choices, and modest overhead. Scope is limited (English, short texts, BERT-base), but execution appears rigorous.
- Novelty: 66
  - Reasoning: Curriculum over augmentation strength in contrastive pretraining is a straightforward extension of existing ideas; likely incremental over CERT/SimCSE-style approaches, though the staged operator activation is a neat, concrete contribution.
- Significance: 68
  - Reasoning: Consistent gains over strong baselines, including +1.1 over CERT at 500 labels and +1.6 at 100 labels, with zero extra parameters and small runtime cost. Impact is practical but modest; evaluations are limited in model/dataset breadth.
- Clarity: 88
  - Reasoning: The pipeline, objectives, operators, curriculum schedule, datasets, hyperparameters, and results (with exact numbers and ablations) are clearly specified.

Final average score: 76.0

Recommendation: Accept