Summary
The paper proposes TimeWarn, an interpretable two-level attention model that explicitly incorporates irregular time intervals between EHR measurements by learning a decay term that modulates both visit-level and variable-level attention. Evaluated on MIMIC-IV and eICU for predicting sepsis 6 hours before onset, TimeWarn shows consistent, modest gains over strong baselines (including GRU-D and RETAIN), along with an ablation supporting the contribution of time-aware modulation. Attention analyses align with clinical expectations.

Strengths
- Clear, clinically motivated problem with strong practical relevance.
- Method is simple, interpretable, and leverages irregular intervals in a principled way via learned decays applied to attention at two levels.
- Solid empirical evaluation on two large public ICU datasets, with multiple baselines and ablation.
- Gains are consistent in AUROC and AUPRC; attention weights highlight clinically meaningful variables.
- Reasonable discussion of limitations.

Weaknesses
- Novelty is incremental relative to RETAIN and GRU-D; modulating attention by time decay is a straightforward extension.
- Potential fairness issues in model selection: TimeWarn is tuned via grid search, while several baselines appear to use default or literature hyperparameters; logistic regression and XGBoost lack comparable tuning and report no variability.
- Limited detail on cohort construction, label derivation specifics, and preprocessing (e.g., exact Sepsis-3 operationalization, exclusion criteria, handling of multiple stays), which affects reproducibility.
- No formal statistical significance testing of performance differences; improvements are modest.
- Missing stronger contemporary baselines for irregular time series (e.g., Transformer variants with time encodings, ODE-RNN/Latent ODE) to position contributions more clearly.
- Interpretability evaluation is qualitative and aggregate-only; case studies or clinician validation would strengthen claims.

Questions for the authors
- How exactly were Sepsis-3 labels operationalized (e.g., alignment of suspected infection with SOFA increase, handling of timing uncertainty)? Any sensitivity analyses?
- Were baselines (especially XGBoost and RETAIN/GRU-D) tuned on the validation set to a comparable extent? Can you report their results under similar hyperparameter sweeps?
- Do results hold when including medication orders or interventions as features (and if excluded, how were proxy treatment signals handled)?
- Any runtime and memory comparisons versus baselines, especially GRU-D and RETAIN?

Suggestions
- Provide fuller preprocessing and labeling details, and release code to enhance reproducibility.
- Add statistical tests or confidence intervals for differences.
- Include at least one strong contemporary time-aware baseline (e.g., time-aware Transformers or ODE-RNN).
- Expand interpretability evaluation with case studies and clinician feedback.

Scores (0–100)
- Soundness: 80
- Novelty: 65
- Significance: 74
- Clarity: 88

Final average score: 76.8

Recommendation: Accept

Rationale: Although the methodological novelty is modest, the paper addresses an important problem with a clean, interpretable approach and demonstrates consistent improvements across two major datasets with supportive ablations. With stronger baseline tuning and expanded methodological comparisons, the contribution would be even more compelling, but the current evidence justifies acceptance.