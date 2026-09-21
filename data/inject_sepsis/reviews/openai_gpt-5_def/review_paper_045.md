Summary
The paper introduces TimeWarn, an interpretable attention model that incorporates irregular time intervals by decaying both visit-level and variable-level attention weights as a function of elapsed time since last measurement. Evaluated on MIMIC-IV and eICU, TimeWarn achieves modest but consistent gains over strong baselines (including GRU-D and RETAIN) for predicting sepsis 6 hours before onset, and provides clinically plausible attention patterns.

Strengths
- Clear problem motivation: irregular sampling is ubiquitous in EHRs and often ignored by attention models.
- Methodologically reasonable: applying learned time decay to both levels of attention is a simple, interpretable extension of RETAIN inspired by GRU-D’s decay idea.
- Empirical evaluation on two large public ICU datasets with multiple baselines and five seeds; improvements are consistent across datasets and metrics.
- Ablation supports the contribution of the time-aware mechanism; attention analysis aligns with clinical expectations (e.g., lactate, respiratory rate).

Weaknesses and Concerns
- Novelty is incremental: time-aware mechanisms and attention variants for irregular EHRs exist (e.g., GRU-D, time-aware attention/RETAIN variants). The main contribution is the specific placement of decay on attention weights rather than inputs/hidden states.
- Potential hyperparameter tuning imbalance: TimeWarn is tuned via a grid over 72 configs, while baselines use defaults from original papers. This may inflate the observed margins; strong baselines (GRU-D, RETAIN, XGBoost) should also be tuned comparably on validation sets.
- Missing methodological details that affect reproducibility and interpretability:
  - Whether attention weights are re-normalized after decay (multiplying post-softmax without renormalization changes scale and complicates interpretation).
  - Precise parameterization of decay (per-variable w and b? shared? initialization ranges?).
  - Handling of missingness and imputation in embeddings beyond a “missingness mask,” and whether medication orders or treatment variables near onset are included (risk of label leakage).
  - Label construction details for Sepsis-3 and alignment with prediction horizon.
- Clinical evaluation is limited: no calibration, decision-curve/net benefit analyses, alerting burden/false alarm rates, or subgroup analyses. Lead-time results beyond 12h are brief.

Questions/Requests for Clarification
- Do you re-softmax visit- and variable-level attention after applying decay, or leave them unnormalized? Please clarify the exact equations and their implications for interpretability.
- Are w and b learned per variable or shared? How are they initialized and constrained?
- Were GRU-D and RETAIN baselines tuned on the same validation sets (learning rate, hidden size, dropout, decay parameters for GRU-D)? If not, please provide tuned results.
- Which variables are included among the 32, and are treatment proxies (e.g., antibiotics, vasopressors, fluid boluses) excluded before the prediction time window to avoid leakage?
- How are missing labs handled within and across windows? Any carry-forward or imputation strategies used besides masks?

Scores (0–100)
- Soundness: 78
- Novelty: 62
- Significance: 70
- Clarity: 82

Final average score: 73.0

Recommendation
Accept

Rationale: While the methodological novelty is modest, the approach is well-motivated, simple, and effective, with consistent improvements over strong time-aware and interpretable baselines on two datasets and reasonable interpretability analyses. With stronger baseline tuning and added methodological detail, the paper would be even more compelling, but as is, it offers a practical and interpretable contribution likely to interest the community.