Review summary

Strengths
- Clear, well-motivated idea: progressively increasing augmentation strength aligns with curriculum learning intuitions for contrastive adaptation.
- Simple to implement, model-agnostic, no inference overhead.
- Consistent improvements over strong baselines (CERT, SimCSE, UDA) on four benchmarks; results averaged over five seeds with ablations.
- Solid ablations isolate the contribution of the curriculum (L=0, reversed curriculum, remove back-translation).

Weaknesses
- Novelty is incremental: scheduling augmentation strength is a straightforward extension of existing contrastive/intermediate training, and similar ideas exist in CV.
- Limited empirical scope: only BERT-base, only short-text English datasets (SST-2, AGNews, TREC, SUBJ), modest scale. Lacks evaluation on larger encoders, modern or long-text datasets, or multilingual settings.
- Fairness of comparisons: CurCon hyperparameters are tuned via grid search per dataset, while baselines appear to use hyperparameters from prior work without re-tuning on the same validation splits, potentially inflating CurCon’s margin.
- Gains, while consistent, are modest (+1.1 average over CERT at 500 labels). Statistical significance beyond standard deviations is not established (no significance tests reported).
- Augmentation design is hand-crafted with discrete phase transitions; no exploration of smoother or learned schedules, or sensitivity to thresholds; limited analysis of failure modes or domain shifts.

Scores (0–100)
- Soundness: 77
- Novelty: 62
- Significance: 66
- Clarity: 88

Final average score
- (77 + 62 + 66 + 88) / 4 = 73.3

Recommendation
- Reject

Rationale: The paper is clear and technically sound with sensible experiments and ablations, but the contribution is incremental and evaluated on a narrow, somewhat dated benchmark suite with modest gains and potentially unfair hyperparameter tuning asymmetry. Strengthening by re-tuning baselines, adding larger/backbone models and modern datasets, providing significance tests, and exploring learned/continuous curricula would make the work more compelling.