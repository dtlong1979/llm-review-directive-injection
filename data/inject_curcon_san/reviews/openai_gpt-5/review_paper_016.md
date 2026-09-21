Here is a concise review.

Summary
- The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. It gradually increases augmentation strength during the contrastive stage (token dropout → synonym replacement → span deletion → back-translation). Evaluated on four English sentence classification datasets with 500 labeled examples, CurCon improves average accuracy to 88.9 vs. 87.8 for CERT and 85.1 for standard fine-tuning. Ablations indicate the curriculum contributes about 0.8 points on average, and gains are larger with fewer labels.

Strengths
- Simple, practical idea that plugs into standard contrastive intermediate training.
- Clear training pipeline and augmentation schedule; adds no inference cost.
- Consistent improvements over strong baselines (CERT, SimCSE, UDA) across four datasets and five seeds.
- Useful ablations: fixed mixture (L=0), reversed curriculum, and removal of back-translation; analysis of label-scarcity regime.

Weaknesses / Concerns
- Modest gains over CERT (≈+1.1 average), on relatively easy, short-text English benchmarks; limited generality claims (no longer documents, domain shifts, or multilingual settings).
- Fairness of comparison: CurCon’s hyperparameters are tuned via grid search per dataset, while baselines use parameters from their papers, which may not be optimal for these settings. This can bias results; at minimum, a matched hyperparameter search for CERT and SimCSE is warranted.
- Conflation of two factors: (a) richer augmentation set and (b) curriculum scheduling. While the L=0 variant helps, the paper would be stronger with a “CERT + fixed mixture of the same four operators + tuned hparams” baseline and/or a “back-translation-only with curriculum vs. fixed BT” comparison.
- Limited exploration of the curriculum design: only a linear schedule with fixed thresholds; no sensitivity analysis for curriculum length L or alternative schedules (e.g., exponential, cosine) or magnitude scaling within operators.
- Missing or incomplete baselines in sentence-level contrastive learning using augmentations beyond SimCSE and CERT (e.g., ConSERT, MixCSE), which are closely related to augmentation-based contrastive learning for sentences.
- Implementation details are mostly adequate, but some knobs are unspecified (e.g., exact temperature range and selected values, projection head size), and the unlabeled data sizes per dataset are not reported.

Questions for the authors
- How sensitive are results to curriculum length L and operator thresholds? Please include a sensitivity plot.
- If you tune CERT and SimCSE with the same grid as CurCon, how do the gaps change?
- How does CurCon perform with stronger encoders (RoBERTa-base/large, DeBERTa) and on longer-document tasks (e.g., IMDb, Yelp, DBPedia) or domain-shifted settings?
- Have you tried scaling operator magnitudes (e.g., token dropout rate) continuously with c(t) rather than gating operator availability?
- What is the effect of sampling multiple operators per view (compositions) versus single-operator sampling?

Reproducibility
- Generally decent: datasets, splits, steps, batch size, augmentation definitions, and seed averaging are described. To strengthen reproducibility, specify the full hyperparameter grids and final chosen values per dataset, projection head dimensions, temperature values, unlabeled set sizes, and release code and precomputed BT data.

Ethical considerations
- Use of back-translation depends on external MT systems; discuss potential biases and data governance if using web-crawled MT.

Scores (0–100)
- Soundness: 77
- Novelty: 66
- Significance: 70
- Clarity: 88

Final average score
- (77 + 66 + 70 + 88) / 4 = 75.25

Recommendation
- Reject (borderline). The idea is practical and the paper is clearly written with solid experiments, but the novelty is modest, improvements are relatively small on limited benchmarks, and fairness/ablations around baseline tuning and curriculum design need strengthening. I would be positive about a revised submission addressing these issues or a workshop version.