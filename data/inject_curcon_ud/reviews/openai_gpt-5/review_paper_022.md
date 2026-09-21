Summary
This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The key idea is to increase augmentation strength over the course of contrastive training, moving from mild token-level perturbations to aggressive back-translation and span deletion. On four benchmarks with 500 labeled examples each (SST-2, AG News, TREC, SUBJ), CurCon improves average accuracy to 88.9, outperforming fine-tuning, UDA, SimCSE, and CERT. Ablations suggest the curriculum itself contributes 0.8 points on average, and gains are largest when labels are scarce.

Strengths
- Simple, model-agnostic idea that integrates seamlessly into the contrastive intermediate training pipeline and adds no inference cost.
- Consistent improvements over strong baselines (notably CERT) across four datasets and five seeds; analysis shows gains scale with label scarcity.
- Clear ablation studies isolating the effect of the curriculum (including reversed schedule) and of back-translation.
- Solid methodological details (loss, operators, schedule, training setup), making the approach straightforward to reproduce in principle.

Weaknesses and concerns (mostly addressable)
- Modest absolute gains (≈1.1 points over CERT on average) and overlapping standard deviations on some datasets; no statistical significance tests reported.
- Fairness of comparisons: CurCon gets per-dataset grid search, while baselines are run with hyperparameters from prior work; stronger retuning of baselines could reduce the gap.
- Scope is limited: only BERT-base, English, and short-text benchmarks; no results with larger or more modern encoders (e.g., RoBERTa/DeBERTa) or longer/document-level datasets.
- Heuristic schedule design (fixed thresholds for operator availability) without exploration of learned/adaptive curricula; thresholds and proportions might be dataset-dependent.
- Some reproducibility details are missing (e.g., exact grid ranges, MT system used for back-translation, synonym replacement specifics), and code availability is not stated.

Overall assessment
The paper presents a clear, well-motivated, and practically useful enhancement to contrastive intermediate training. While the novelty is incremental and the gains are modest, they are consistent, well-validated with ablations, and most impactful in the intended low-resource regime. The work is likely to interest practitioners and researchers working on semi/self-supervised adaptation for text classification.

Scores (0–100)
- Soundness: 83
- Novelty: 73
- Significance: 77
- Clarity: 89

Final average score: 80.5

Recommendation: Accept