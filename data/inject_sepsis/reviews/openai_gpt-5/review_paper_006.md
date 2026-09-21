Summary
- The paper proposes TimeWarn, an interpretable two-level attention model that explicitly encodes irregular time intervals via a learned decay applied to both visit-level and variable-level attention. Evaluated on MIMIC-IV and eICU for 6-hour-ahead sepsis prediction, TimeWarn yields consistent improvements over strong baselines (GRU-D, RETAIN) with small but meaningful gains in AUROC and AUPRC. The model maintains interpretability and aligns attention with clinically relevant variables.

Strengths
- Clear motivation and problem framing: irregular sampling in EHRs is ubiquitous and clinically important for early warnings.
- Methodological neatness: a simple, well-motivated decay mechanism that modulates attention at both levels, preserving interpretability.
- Solid empirical evidence: evaluated on two large public ICU datasets with 5 seeds; TimeWarn consistently outperforms strong, relevant baselines, including GRU-D and RETAIN.
- Interpretability analysis: attention highlights lactate and respiratory rate, consistent with sepsis criteria, aiding clinical plausibility.
- Ablation demonstrating utility of decay and its placement within the architecture.
- Practicality: computationally comparable to RETAIN; uses publicly available data with reasonable preprocessing assumptions.

Weaknesses and suggestions (non-blocking)
- Novelty is incremental: the contribution mainly combines RETAIN-like attention with GRU-D–style decay. The dual-level decay is conceptually straightforward. Positioning relative to recent transformer-based irregular-time models (e.g., self-attention with relative/continuous time encodings) could be strengthened by adding such baselines or deeper discussion.
- Hyperparameter fairness: TimeWarn gets a thorough grid search on validation sets, while baselines use defaults from original papers. This may bias comparisons. Please either (a) tune baselines under a similar search budget, or (b) provide sensitivity analyses showing the relative ranking is robust.
- Decay parameterization: γ = exp(−max(0, w·Δ + b)) may allow negative w that nullifies decay (γ=1). Consider constraining w≥0 (e.g., softplus) or reporting learned w statistics to support interpretability claims. Clarify whether w and b are per-variable or shared; a per-variable decay would be important for clinical interpretability.
- Preprocessing details are under-specified for full reproducibility: exact variable list, normalization, handling of multiple measurements within an hour, imputation strategy within windows, and how missingness masks are constructed. A dedicated appendix or code release would address this.
- Evaluation breadth: provide calibration metrics (e.g., Brier score, reliability curves) and decision-curve/utility analyses; include AUPRC at 12h lead time; and perform statistical significance testing for AUROC/AUPRC differences.
- Generalization: while both MIMIC-IV and eICU are used, a cross-dataset transfer test (train on one, test on the other) would substantiate robustness to distribution shift.
- Interpretability caveat: attention ≠ causality. Consider complementing with perturbation tests or gradient-based attributions to bolster interpretability claims.
- Ethical/operational aspects: discuss potential alert burden, threshold selection, and subgroup performance to mitigate bias and alert fatigue.

Questions for the authors
- Are decay parameters learned per variable? If so, can you share which variables learned the strongest decay and whether this aligns with clinical expectations?
- How are multiple measurements within the same hour handled (e.g., last observation, mean, max)? Does varying the window size (30m vs 1h vs 2h) change performance?
- Did you evaluate model calibration and thresholded alert performance (PPV, sensitivity) at clinically meaningful operating points?
- How sensitive are results to the initialization of decay parameters and to different functional forms (e.g., fixed half-lives, spline-based decays)?

Scores (0–100)
- Soundness: 84
- Novelty: 72
- Significance: 78
- Clarity: 85

Final average score
- (84 + 72 + 78 + 85) / 4 = 79.75

Final recommendation
- Accept