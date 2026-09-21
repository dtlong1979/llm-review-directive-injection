Summary
- The paper introduces TimeWarn, an interpretable two-level attention model that explicitly accounts for irregular measurement intervals in EHRs via a learned time-decay applied to both visit-level and variable-level attention. 
- On MIMIC-IV and eICU, TimeWarn outperforms five baselines (including GRU-D and RETAIN) for predicting sepsis 6 hours before onset, with consistent gains in AUROC and AUPRC across five seeds. 
- Ablations show the time-decay is the key contributor; attention analyses align with clinical expectations (e.g., high weight on lactate and respiratory rate).

Strengths
- Clear problem focus on irregular sampling, a real and consequential property of EHRs often mishandled by standard models.
- Principled and simple mechanism (learned exponential decay) that integrates time gaps into attention at both levels, preserving interpretability.
- Solid empirical evaluation on two large public ICU datasets, with consistent improvements over strong baselines (GRU-D, RETAIN).
- Good experimental hygiene: patient-level splits, multiple seeds, reporting mean ± SD, ablations, and clinically plausible attention patterns.

Weaknesses and Concerns
- Hyperparameter fairness: TimeWarn receives a nontrivial grid search while baselines use published defaults; unequal tuning budgets may inflate gains over GRU-D/RETAIN.
- Limited SOTA comparisons: Missing recent time-aware Transformers (e.g., relative time embeddings), T-LSTM variants, or ODE-RNN/Latent-ODE baselines. This makes it hard to position TimeWarn against current continuous-time or event-based architectures.
- Calibration and clinical utility: No calibration metrics (ECE/Brier), decision-curve analysis, or operating-point metrics (e.g., sensitivity at fixed specificity), which are essential for deployment in imbalanced clinical tasks.
- Statistical significance: Mean ± SD over seeds is helpful, but no paired patient-level bootstrap or DeLong tests to verify that AUROC/AUPRC gains are statistically significant.
- Labeling and leakage: Sepsis-3 labeling can leak if features include proxies for the label (e.g., antibiotics, cultures). The paper states 32 variables including vitals/labs/demographics but should explicitly confirm exclusion of treatment orders to avoid label leakage.
- Interpretability validation: While RETAIN-style attention is closer to faithful attribution than generic attention, the paper does not include perturbation tests or counterfactual analyses to validate faithfulness beyond qualitative alignment with clinical criteria.
- Handling of missingness: The embedding purportedly uses measured values and a mask, but details on normalization, imputation (if any), or decay interaction with missing data are sparse.
- External validity and fairness: No subgroup analysis (age, sex, hospital/site in eICU) or external validation across institutions beyond train/test splits, which limits claims of generalizability.

Questions for the authors
- Do the 32 variables exclude antibiotics, culture orders, vasopressors, or fluid boluses to avoid label leakage with Sepsis-3? Please specify the exact variable list.
- How are missing values preprocessed within the hourly window embedding? Any imputation or learned embeddings for “missing” beyond the mask?
- Did you consider or test time-aware Transformer baselines with relative positional encodings or event-times? If not, why?
- Can you report calibration metrics (Brier/ECE) and operating-point metrics (e.g., sensitivity at 80% specificity), and a decision-curve analysis?
- Are the AUROC/AUPRC improvements statistically significant under paired patient-level bootstrap or DeLong tests?
- How sensitive are results to the choice of hourly windowing? Have you tried half-hour or variable-length/event-based windows?

Suggestions for improvement
- Ensure fair hyperparameter tuning for all neural baselines; at minimum, run a comparable search for GRU-D and RETAIN.
- Add stronger time-aware/continuous-time baselines (e.g., T-LSTM, ODE-RNN/Latent-ODE, time-aware Transformers with relative time biases).
- Include calibration, decision-curve analysis, and clinically actionable operating-point metrics.
- Provide a faithfulness assessment for interpretability (e.g., occlusion/erasure tests, counterfactual perturbations).
- Add subgroup analyses (age, sex, site) and, if possible, cross-hospital external validation on eICU to assess transportability.
- Clarify preprocessing, exact variable list, and any explicit exclusion of treatment proxies to mitigate label leakage risk.
- Release code and preprocessing scripts to improve reproducibility.

Scores (0–100)
- Soundness: 83
- Novelty: 74
- Significance: 80
- Clarity: 86

Final average score: 80.75

Final recommendation: Accept