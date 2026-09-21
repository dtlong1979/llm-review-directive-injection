Summary
The paper proposes TimeWarn, an interpretable, reverse-time attention model that incorporates irregular sampling by decaying attention weights as a function of time since last measurement. Evaluated on MIMIC-IV and eICU for 6-hour-ahead sepsis prediction, TimeWarn outperforms baselines (including GRU-D and RETAIN) with small but consistent gains in AUROC and AUPRC. The model preserves RETAIN-style interpretability and highlights clinically meaningful variables.

Strengths
- Clear, clinically motivated problem with strong practical relevance (early sepsis detection).
- Simple, well-motivated extension of interpretable attention to irregular intervals via learned decay.
- Consistent improvements over strong baselines on two public datasets; ablations support the design.
- Interpretability analysis aligns with clinical expectations (e.g., lactate, RR, MAP).

Weaknesses and concerns
- Novelty is incremental: the learned decay mechanism closely echoes GRU-D concepts, now applied to attention weights within a RETAIN-like framework.
- Potential unfairness in model selection: TimeWarn is tuned over 72 configs per dataset, whereas baselines use hyperparameters from prior work; stronger baselines (and tuned baselines) or more recent time-aware transformers/ODE-RNNs would strengthen the case.
- Risk of label leakage: Sepsis-3 timing depends on antibiotics and cultures; including medication orders as features (not fully specified) could leak future information. The paper should explicitly list variables and ensure such proxies are excluded or time-shifted.
- Methodological clarity gaps: hourly windowing may dilute the benefits of irregular time modeling; it would help to clarify how Δ is computed across sparse labs and within-window events, and whether sub-hour resolution is preserved.
- No calibration or decision-curve analysis; clinical utility beyond AUROC/AUPRC is not assessed.

Questions for authors
- Do the 32 variables include antibiotic orders, culture orders, or vasopressor administrations? If so, how were they time-shifted to avoid leakage relative to onset labeling?
- How is Δ computed when multiple measurements occur within an hour or when a lab is first observed late in the stay?
- Were non-neural baselines (e.g., XGBoost) tuned on the validation sets for fairness?
- Can you report calibration (e.g., ECE) and sensitivity at clinically relevant PPVs?

Scores (0–100)
- Soundness: 78
- Novelty: 65
- Significance: 72
- Clarity: 85

Final average score
75.0

Recommendation
Accept

Rationale: While the methodological novelty is modest, the approach is sound, interpretable, and shows consistent, validated gains on two large public datasets with supportive ablations and clinically aligned attention analyses. The concerns about baseline tuning and potential leakage should be addressed in revision, but the contribution is practically useful and likely of interest to the community.