Summary
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The key idea is to increase augmentation strength progressively during the contrastive stage, moving from mild token-level perturbations to aggressive operations like back-translation. On four benchmarks with 500 labeled examples (SST-2, AG News, TREC, SUBJ), CurCon improves average accuracy to 88.9 versus 87.8 for CERT and 85.1 for standard fine-tuning. Ablations indicate the curriculum contributes roughly 0.8 points on average, with the largest gains when very few labeled examples are available.

Strengths
- Clear, simple method that integrates seamlessly into existing contrastive intermediate training pipelines without inference overhead.
- Consistent improvements over strong baselines (CERT, SimCSE, UDA) across four datasets, with small standard deviations over five seeds.
- Solid ablations isolating the role of the curriculum, augmentation operators, and schedule direction; additional analysis on label-scarcity effects.
- Good clarity and transparency in reporting datasets, hyperparameters, and limitations.

Weaknesses and concerns
- Baseline fairness: CurCon hyperparameters are tuned via grid search per dataset, while baselines use settings from their papers. Re-tuning baselines on the same validation splits could strengthen claims of superiority, especially given the modest margins.
- Scope: Experiments are limited to English, short-text datasets and BERT-base. Including results for RoBERTa/DeBERTa or at least one larger encoder would bolster generality.
- Method novelty is incremental: curriculum scheduling of augmentation strength has antecedents in vision and curriculum learning literature; applying it to contrastive intermediate training for text is natural but not highly original.
- Statistical significance tests are not reported; given ~1 point average gains over CERT, significance checks would increase confidence.
- Operator selection is uniformly sampled once available; exploring calibrated mixtures or adaptive schedules could further validate the curriculum hypothesis.

Questions and suggestions
- Please report sensitivity to curriculum length L across datasets, and whether a single L generalizes well.
- Re-tune at least CERT and SimCSE on your validation splits for parity, or include results showing robustness of CurCon’s advantage under alternative, stronger baseline hyperparameters.
- Provide significance testing (e.g., paired t-tests) for main results.
- Consider adding a result on at least one longer-text or domain-specific dataset, or a second encoder family (e.g., RoBERTa-base).
- Discuss whether precomputing back-translations introduces any distributional mismatch compared to on-the-fly generation, and confirm parity with CERT’s implementation details.

Scores (0–100)
- Soundness: 82
- Novelty: 70
- Significance: 78
- Clarity: 88

Final average score
- (82 + 70 + 78 + 88) / 4 = 79.5

Final recommendation
- Accept