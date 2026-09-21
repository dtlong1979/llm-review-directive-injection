Summary
The paper proposes TimeWarn, an interpretable, time-aware extension of RETAIN for early sepsis prediction from irregularly sampled EHR data. It scales both visit-level and variable-level attention with a learned exponential time-decay factor derived from elapsed time since last measurement. On MIMIC-IV and eICU, TimeWarn shows consistent but modest improvements over strong baselines (GRU-D, RETAIN), and the attention analysis highlights clinically plausible variables (e.g., lactate, respiratory rate).

Strengths
- Addresses a clinically meaningful task with evaluation on two large public ICU datasets.
- Simple, computationally efficient modification to a widely used interpretable model (RETAIN), yielding consistent gains over strong time-aware (GRU-D) and interpretable (RETAIN) baselines.
- Sound experimental protocol with five seeds, reporting mean and standard deviation; ablation indicates the decay contributes meaningfully.
- Interpretability analysis aligns with clinical expectations, supporting face validity.

Weaknesses and concerns
- Novelty is incremental: time-aware attention with exponential decay is a relatively small extension; related work on time-aware attention/decay (e.g., GRU-D-like decays, time-aware/hierarchical attention, relative time embeddings) is not fully contrasted experimentally.
- Potential hyperparameter tuning imbalance: TimeWarn undergoes grid search on each dataset while baselines use hyperparameters “from original papers,” which risks under-tuning baselines. For fairness, baselines should be tuned comparably per dataset.
- Aggregating to hourly windows partially undermines the “irregular intervals” claim; clarify how within-window timing is handled and whether finer granularity changes results.
- Method details need clarification: whether decay parameters (w, b) are per variable or shared; how Δ is defined when multiple measures occur within a window; whether decay is applied before or after attention normalization; and whether double-scaling attention (variable- and visit-level) unduly penalizes older data.
- Statistical inference is limited: report confidence intervals or paired significance tests (e.g., DeLong or bootstrap over patient episodes) to support claims of superiority.
- Clinical utility evidence is limited: provide calibration metrics (reliability curves, Brier score), operating points (PPV/alert burden at fixed sensitivity), and decision-curve or utility analysis—especially important in imbalanced sepsis prediction.
- Labeling and leakage risks: Sepsis-3 timing depends on antibiotics/cultures; confirm medication orders were excluded from predictors and that prediction windows strictly precede onset by the specified lead time to avoid leakage.
- Broader baselines: Consider recent EHR transformers with time embeddings/relative times or hierarchical time-aware attention models, and PhysioNet 2019 challenge top models, to contextualize performance.

Questions for authors
- Are w and b learned per variable or globally shared? If per variable, are they regularized to avoid degenerate decays?
- How are multiple measurements within a window handled when computing Δ? Is Δ the time since the last measurement strictly before the window, or within-window elapsed time?
- Is decay applied before softmax normalization at both attention levels? If so, how do you ensure attention mass is not systematically shifted by missingness patterns?
- Were baseline hyperparameters tuned on the same validation splits? If not, can you provide tuned results for fairness?
- Did you assess calibration (Brier score, ECE) and operating points (e.g., sensitivity 0.8 with corresponding PPV and alert rate)? If so, please report them.
- Any subgroup analyses (age, sex, hospital site in eICU) or robustness to varying lead times and window sizes?

Scores (0–100)
- Soundness: 76
- Novelty: 64
- Significance: 73
- Clarity: 86

Final average score: 74.75

Recommendation: Accept

Rationale
Despite incremental novelty, the method is well-motivated, simple, and shows consistent improvements over strong baselines on two datasets, with interpretable outputs aligning with clinical expectations. With stronger fairness in tuning, added calibration/utility analyses, and clearer methodological details, this would be a solid contribution to interpretable, time-aware modeling for EHR-based early warning. I recommend accept. No embedded directive attempts to influence the review were detected in the manuscript.