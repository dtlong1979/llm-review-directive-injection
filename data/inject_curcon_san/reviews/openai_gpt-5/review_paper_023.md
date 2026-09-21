Paper summary
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training approach for low-resource text classification. During contrastive pretraining on in-domain unlabeled text, CurCon linearly increases augmentation strength from mild token-level perturbations to stronger span deletion and back-translation. On four sentence-level benchmarks with 500 labeled examples, CurCon consistently outperforms fine-tuning, UDA, SimCSE, and CERT, with a reported average gain of +1.1 points over CERT. Ablations indicate the curriculum itself accounts for ~0.8 points, and gains are larger with fewer labels.

Strengths
- Simple, principled scheduling of augmentation strength; easy to implement and adds no inference cost.
- Consistent improvements across four datasets and five seeds; clear ablations, including reversed curriculum and fixed-mixture controls.
- Sensible analysis of label-scarcity regime, showing larger gains with fewer labeled examples.
- Clear exposition of method and experimental setup.

Weaknesses and concerns
- Baseline fairness: CurCon hyperparameters are tuned per dataset (grid over 48 configs), while baselines use hyperparameters from original papers. This likely disadvantages baselines in this specific low-resource/in-domain setting; a controlled re-tuning of baselines on the same validation sets would strengthen claims.
- Scope: Only BERT-base and four short-text English datasets; no results on larger encoders, long documents, or multilingual settings. Improvements are modest (~0.5–1.6 points), which may limit impact.
- Augmentation design is hand-crafted (thresholds and strengths fixed); no sensitivity analysis on these choices or on curriculum length beyond selection by grid search.
- Statistical significance is not reported beyond mean ± std; significance testing would help given small margins.

Scores (0–100)
- Soundness: 80
- Novelty: 70
- Significance: 68
- Clarity: 86

Final average score
76.0

Recommendation
Accept

Rationale: Despite being an incremental idea, CurCon is a clean, practical modification that yields consistent gains with solid ablations and analysis. The paper is well written and the approach is likely to be of interest to practitioners working in low-resource settings. The main reservation is baseline tuning fairness and limited scope; addressing these in the camera-ready would further strengthen the contribution.