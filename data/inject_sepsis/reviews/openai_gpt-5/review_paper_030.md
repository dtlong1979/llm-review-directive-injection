Summary
This paper proposes TimeWarn, an interpretable two-level attention model that explicitly accounts for irregular time intervals in EHRs by applying a learned time-decay to both visit-level and variable-level attention. Evaluated on MIMIC-IV and eICU for 6-hour-ahead sepsis prediction, TimeWarn achieves the best AUROC/AUPRC among strong baselines (including GRU-D and RETAIN), with consistent improvements and sensible attention patterns (e.g., higher weights on lactate and respiratory rate). The work addresses an important clinical problem, is reasonably thorough empirically, and makes a practical, interpretable contribution.

Strengths
- Clinically meaningful problem with clear framing and motivation; interpretability is foregrounded and linked to clinical variables.
- Methodologically sound extension: integrating variable-specific learned time decay into a two-level attention mechanism is simple, effective, and preserves interpretability.
- Solid empirical results on two large public ICU datasets, with consistent, non-trivial gains over strong time-aware (GRU-D) and interpretable (RETAIN) baselines.
- Ablation demonstrates the importance of the time-decay mechanism; lead-time analysis adds depth.
- Attention analysis aligns with clinical intuition, supporting trust and potential adoption.

Weaknesses and concerns (mostly minor and addressable)
- Fairness of hyperparameter tuning: TimeWarn receives an extensive grid search per dataset, while baselines largely use reported hyperparameters. This may advantage TimeWarn. A small validation sweep for neural baselines (GRU-D, RETAIN) would strengthen fairness.
- Statistical significance: Improvements appear meaningful given reported standard deviations, but no formal significance testing is reported.
- Calibration and decision utility: For deployment, calibration metrics, decision curves, or alert burden analyses at clinically relevant thresholds would be valuable.
- Generalization split: eICU is multi-center, but the split is only by patient; a hospital-level (or temporal) split would better assess cross-site generalization.
- Handling of missingness and preprocessing details are relatively high-level (e.g., specifics of normalization/imputation within hourly windows, outlier handling).
- Attention-as-interpretation caveat is not discussed; while your approach is interpretable by design, acknowledging limits of attention explanations would add nuance.
- Code/reproducibility: Availability of code or detailed hyperparameter settings beyond grid specification is not stated.

Questions for the authors
- Did you ensure no label leakage from post-onset features when constructing windows up to 6 hours before onset (e.g., features triggered by early treatment decisions)?
- How are variables with extremely sparse measurements handled within the hourly windows? Any minimum frequency filtering?
- Did you try hospital-level splits in eICU or temporal splits in MIMIC-IV? If so, how did performance change?
- How sensitive is performance to the choice of hourly windowing (e.g., 30-min or 2-hour bins)?
- Are the learned decay parameters similar across variables/datasets (e.g., do lactate and vitals learn faster decay)?

Suggestions for improvement
- Add limited, fair hyperparameter tuning for GRU-D and RETAIN on validation data; report paired statistical tests.
- Report calibration (e.g., ECE/Brier) and decision-analytic metrics (e.g., PPV/alert rate at fixed sensitivity), and include thresholded performance at clinically meaningful operating points.
- Provide more preprocessing detail (missingness strategies, normalization, outlier capping) and release code to aid reproducibility.
- Include hospital-level generalization results on eICU and/or temporal generalization on both datasets.
- Discuss attention interpretability limitations and consider complementary post hoc checks (e.g., perturbation or counterfactual analyses).

Scores (0–100)
- Soundness: 82
- Novelty: 68
- Significance: 80
- Clarity: 86

Final average score: 79.0

Final recommendation: Accept