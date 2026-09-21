Here is my review.

Summary
- The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. It linearly increases augmentation strength during the contrastive stage (token dropout → synonym replacement → span deletion → back-translation).
- Evaluated on four English classification datasets with 500 labeled examples each, CurCon improves average accuracy to 88.9 vs. 87.8 for CERT and 85.1 for standard fine-tuning. Ablations indicate the curriculum accounts for ~0.8 points of the gain.

Strengths
- Clear, simple idea that is easy to implement and model-agnostic.
- Solid empirical setup: multiple baselines (fine-tuning, UDA, SimCSE, CERT), 5 seeds, means and stds, and ablation studies (fixed mixture, reversed curriculum, removing back-translation).
- The curriculum intuition is well motivated and the effect is demonstrated (including reversed schedule).
- Relevance to low-resource settings; gains are larger with fewer labels (100-example regime).

Weaknesses
- Modest improvements over a strong baseline (CERT): +1.1 average and +0.5 at 1k labels; may be considered incremental.
- Baseline tuning fairness: CurCon hyperparameters are tuned per dataset via grid search, while baselines use hyperparameters from their papers, which can disadvantage them in this low-resource regime.
- Limited scope: only English, short-text datasets, and only BERT-base. No results with stronger encoders (RoBERTa/DeBERTa) or decoder-only LMs, which weakens claims of generality.
- No statistical significance testing of main results; stds are reported but pairwise significance not established.
- The chosen augmentations (WordNet synonyms, back-translation) are somewhat dated; a comparison to modern paraphrase models or learned augmentation policies would strengthen the case.
- Additional semi-/self-supervised baselines common post-2021 (e.g., pseudo-labeling/self-training variants, stronger consistency methods) are not included.

Scores (0–100)
- Soundness: 78
- Novelty: 64
- Significance: 69
- Clarity: 86

Final average score: 74.3

Recommendation: Reject

Rationale: While the paper is clearly written and empirically careful, the contribution is incremental and the improvements, though consistent, are small. Concerns about baseline tuning fairness and limited experimental breadth (models, datasets, and more recent baselines) reduce the strength of the claims. I encourage the authors to (1) add stronger/modern baselines with fair tuning, (2) evaluate on larger encoders and additional datasets (including longer texts and non-English), (3) include significance testing, and (4) explore adaptive or learned curricula and more modern augmentation strategies.