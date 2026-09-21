Review

Summary
The paper proposes TimeWarn, an interpretable attention model for early sepsis prediction that explicitly accounts for irregular measurement intervals by learning a per-variable time-decay that modulates both visit-level and variable-level attention. Evaluations on two public ICU datasets (MIMIC-IV and eICU) show consistent, modest gains over strong baselines (GRU-D, RETAIN), with ablations indicating the benefit of the time-decay mechanism. The method maintains interpretability in the RETAIN style and highlights clinically meaningful variables (e.g., lactate, respiratory rate).

Strengths
- Addresses a central practical issue in EHR modeling: irregular sampling, with a simple, computationally light mechanism.
- Solid experimental design: two large public datasets, reasonable baselines, five seeds, and ablations.
- Consistent performance improvements in AUROC/AUPRC across datasets and horizons; interpretable attention analysis aligns with clinical expectations.
- Clear writing and positioning within related work.

Weaknesses and Concerns
- Novelty is incremental: combining a learned time-decay with hierarchical attention is a natural extension of RETAIN and conceptually overlaps with ideas from GRU-D and time-aware attention models; related prior art could be discussed more thoroughly.
- Fairness of baseline tuning: TimeWarn benefits from grid search per dataset, whereas baselines use original-paper hyperparameters, which may underrepresent their best achievable performance on these datasets.
- Methodological details missing or under-specified:
  - Preprocessing and imputation strategy, handling of multiple measurements within an hour, normalization, and how missingness is encoded into embeddings.
  - Clear safeguards against label leakage when defining “within the next six hours” (e.g., exclusion of post-onset features or proxies like immediate orders tied to sepsis treatment).
- Evaluation breadth:
  - No calibration metrics or decision-curve analyses; thresholded performance (PPV/NPV at clinically relevant sensitivities) would make clinical utility clearer.
  - Statistical significance vs. baselines beyond seed variance (e.g., patient-level bootstrapped CIs) is not reported; improvements, while consistent, are modest (e.g., +0.013–0.016 AUROC).
- Interpretability claims rely on attention weights, which are known not to be definitive explanations; robustness across seeds, patients, and correlation with perturbation-based importance would strengthen claims.
- The visit-level decay uses mean decay across variables, which may unduly penalize windows with many sparsely measured labs despite recent critical measurements; alternatives (e.g., learned aggregation, coverage-weighted schemes) could be explored.

Suggestions for Improvement
- Tune baselines (at least GRU-D and RETAIN) with comparable search on validation sets to ensure fairness; report bootstrapped CIs and statistical tests.
- Add calibration (ECE/Brier), decision-curve or utility analysis, and thresholded operating points relevant to clinical practice.
- Provide more preprocessing details and code to ensure reproducibility; analyze robustness across hospital sites in eICU.
- Strengthen interpretability via perturbation tests, consistency across seeds, and comparison of attention at different lead times.
- Consider additional baselines such as time-aware/self-attention Transformers with continuous-time encodings.

Scores (0–100)
- Soundness: 78
- Novelty: 65
- Significance: 72
- Clarity: 82

Final average score: 74.25

Recommendation: Accept