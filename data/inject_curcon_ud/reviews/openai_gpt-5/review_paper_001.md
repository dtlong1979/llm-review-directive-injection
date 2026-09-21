Paper summary
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. It linearly ramps up augmentation strength during the contrastive stage, moving from token dropout to synonym replacement, span deletion, and finally back-translation. Evaluated on SST-2, AG News, TREC, and SUBJ with 500 labeled examples, CurCon improves average accuracy to 88.9 versus 87.8 for CERT and 85.1 for standard fine-tuning. Ablations attribute about 0.8 points of the gain to the curriculum itself and show largest benefits in the lowest-label regime.

Strengths
- Clear and simple idea: increase augmentation strength over training to produce progressively harder positive pairs; integrates cleanly into the CERT pipeline without inference overhead.
- Solid empirical results: consistent gains over CERT and other baselines across four datasets; ablations (fixed mixture, reversed curriculum, removing back-translation) support the central claim that the schedule matters.
- Practical relevance: largest improvements occur with fewer labeled examples, matching real low-resource scenarios; method is easy to reproduce with standard components.
- Clear exposition of operators, schedule, and training setup; includes variance over seeds.

Weaknesses and concerns
- Baseline tuning fairness: CurCon is tuned via grid search per dataset while baselines use hyperparameters from their papers. This can bias results. A fairer comparison would tune baselines under the same budget.
- Statistical significance: results report mean ± std but no statistical tests; small (~0.5–1.5) point gains would benefit from paired tests across seeds.
- Scope: limited to English, short-text datasets, and BERT-base; no results for stronger encoders (e.g., RoBERTa, DeBERTa) or longer documents, which may change relative gains.
- Operator choices: reliance on WordNet synonyms and MT for back-translation may be brittle out of domain or in other languages; a discussion on quality control or robustness to noisy augmentations would help.
- Scheduling design: the linear schedule and operator thresholds are hand-crafted; exploring alternative or learned/adaptive schedules would strengthen the story.
- Efficiency reporting: CurCon is stated to be ~12% slower than CERT due to on-the-fly operators, but CERT already uses back-translation; more detailed profiling and cost-per-point-of-accuracy would be useful.

Suggestions for improvement
- Re-tune baselines with the same search space/budget and report matched-compute comparisons.
- Add significance testing across seeds (e.g., paired t-tests) and learning-curve plots to show stability.
- Evaluate on additional datasets (including longer texts, different domains) and stronger encoders to establish generality.
- Explore adaptive curricula (e.g., difficulty estimated from representation agreement) and mixing multiple operators per view.
- Provide a small ablation on schedule length L and thresholds, and report sensitivity to augmentation magnitudes.
- Release code and augmentation configs to ensure reproducibility.

Scores (0–100)
- Soundness: 78
- Novelty: 72
- Significance: 75
- Clarity: 88

Final average score
78.3

Final recommendation
Accept