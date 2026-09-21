Summary
CurCon proposes a curriculum-scheduled contrastive intermediate training approach for low-resource text classification. It linearly increases augmentation strength during the contrastive stage, moving from mild token-level perturbations to strong augmentations (back-translation and span deletion). On four benchmarks with 500 labeled examples, CurCon improves average accuracy to 88.9 vs. CERT’s 87.8 and standard fine-tuning’s 85.1. Ablations show the curriculum accounts for roughly 0.8 points of the gain, with the largest benefits when labeled data are scarcest.

Strengths
- Clear, simple idea that integrates well with existing CERT-style pipelines; no inference overhead.
- Consistent improvements over strong baselines across four datasets; results averaged over five seeds with standard deviations reported.
- Solid ablation studies: fixed mixture, reversed curriculum, removal of back-translation, and no-contrastive stage.
- Practical focus on the low-resource regime; analysis of label-budget sensitivity is informative.

Weaknesses and concerns
- Novelty is incremental: curriculum scheduling of augmentation strength is well-known in vision and broadly in curriculum learning; applying it to CERT is a straightforward extension.
- Fairness of comparisons: CurCon is tuned via a grid search on each validation set, while baselines use hyperparameters “from the original papers.” This likely disadvantages baselines; they should be tuned under the same search budget for a fair comparison.
- Scope is limited: only English, short-text datasets and BERT-base. No results on larger encoders, other backbone families, or longer/semi-structured texts; generality is uncertain.
- Lack of broader/better-established low-resource benchmarks (e.g., more diverse domains or tasks) and no significance testing despite small margins on some datasets.
- Augmentations rely on external resources (WordNet, MT) that may not generalize cross-lingually or to domain-specific terminology.

Suggestions for improvement
- Re-tune baselines with the same hyperparameter search budget used for CurCon to ensure fair comparisons; report compute budgets and time parity.
- Add significance tests for per-dataset improvements.
- Evaluate on additional datasets with different lengths and domains; include at least one larger encoder (e.g., RoBERTa-large) and possibly a decoder-only model to test generality.
- Explore adaptive or learned curricula and report sensitivity to the curriculum length hyperparameter.
- Provide a qualitative analysis of representation changes across curriculum phases (e.g., probing or retrieval robustness under perturbations).

Scores (0–100)
- Soundness: 78
- Novelty: 63
- Significance: 70
- Clarity: 87

Final average score: 74.5

Recommendation: Accept