Summary
TimeWarn is an interpretable two-level attention model for early sepsis prediction that explicitly accounts for irregular measurement intervals in EHRs. It modulates both visit-level and variable-level attention by a learned, per-variable time-decay factor derived from elapsed time since last measurement. On MIMIC-IV and eICU, TimeWarn achieves consistent improvements over strong baselines (including GRU-D and RETAIN) for 6-hour-ahead prediction, with supportive ablations and attention analyses aligning with clinical intuition.

Strengths
- Clear problem motivation: irregular sampling is ubiquitous in EHRs and often ignored by attention models.
- Methodological contribution: a simple, effective, and interpretable way to inject per-variable elapsed-time decay directly into attention at both levels.
- Strong empirical results: consistent AUROC/AUPRC gains across two large, public ICU datasets with multiple random seeds, plus an ablation isolating the value of the time-decay mechanism.
- Interpretability: attention analyses prioritize lactate and respiratory rate, consistent with sepsis criteria, aiding clinician trust.
- Practicality: architecture remains close to RETAIN in complexity, facilitating adoption and reproducibility.

Weaknesses and concerns (mostly addressable)
- Hyperparameter tuning fairness: TimeWarn is tuned via grid search per dataset, while baselines use published hyperparameters; this can bias results. Re-tuning baselines on the same validation splits would strengthen claims.
- Statistical testing: Means and standard deviations are reported, but no formal significance tests are provided; including paired tests would bolster confidence in the improvements, which are modest but consistent.
- Preprocessing details: Clarify how multiple measurements within an hour are aggregated, normalization/imputation strategy, and precise computation of Δ within hourly windows. These choices can materially affect performance and interpretability.
- Decay parameterization clarity: Specify whether w and b are learned per variable, whether w is constrained to be nonnegative, and provide intuition for the hinge at zero (max(0, ...)). A brief sensitivity analysis on the decay form and initialization would be helpful.
- Calibration and clinical utility: Add calibration curves, Brier scores, and operating-point metrics (e.g., PPV at 80% sensitivity), and consider decision-curve analysis to connect improvements to actionable benefit.
- Generalization: External validation is limited to two US ICU datasets. A hospital-level or temporal holdout, or cross-hospital evaluation in eICU, would better characterize robustness.
- Runtime and deployment: Reporting training/inference times and memory footprint would help assess feasibility for real-time alerts and integration.

Questions and suggestions for the authors
- Can you re-tune baselines (especially GRU-D and RETAIN) on your validation sets for fair comparison?
- Please detail the per-variable decay parameters (shared vs. per-variable), any constraints, and provide a brief sensitivity analysis to the decay formulation and the hourly window size.
- Provide additional metrics at clinically relevant thresholds and calibration plots.
- Report results for several prediction horizons in a single figure to visualize the lead-time vs performance trade-off.
- Consider a hospital-wise split in eICU to assess cross-site generalization.
- If possible, share code and preprocessing pipelines to aid reproducibility.

Scores (0–100)
- Soundness: 82
- Novelty: 70
- Significance: 78
- Clarity: 86

Final average score
- (82 + 70 + 78 + 86) / 4 = 79.0

Final recommendation
- Accept