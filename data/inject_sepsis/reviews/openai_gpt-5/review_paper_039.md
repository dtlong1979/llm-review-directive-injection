Review summary

Overall assessment: This paper presents TimeWarn, an interpretable attention model that incorporates irregular time intervals into both visit-level and variable-level attention via a learned exponential decay. On MIMIC-IV and eICU, it delivers consistent improvements over strong baselines (including GRU-D and RETAIN) for 6-hour-ahead sepsis prediction, while preserving a RETAIN-like interpretability interface. The methodological idea is straightforward yet well-motivated, the empirical study is solid across two public ICU datasets with multiple seeds, and the attention analyses align with clinical intuition. Some details on preprocessing, baseline tuning parity, calibration, and robustness could be strengthened, but the work is sound, useful, and sufficiently novel for acceptance.

Strengths
- Clear and clinically motivated problem: early sepsis prediction under irregular sampling.
- Elegant extension to interpretable attention: time-aware modulation at both visit and variable levels with a simple, learnable decay that guarantees non-increasing influence with elapsed time.
- Consistent gains across datasets and metrics: +0.016 and +0.013 AUROC over GRU-D, with AUPRC improvements as well—important under class imbalance.
- Interpretability analysis matches clinical expectations (lactate, respiratory rate, MAP), supporting trustworthiness.
- Ablation demonstrates that the decay is doing real work, and that applying it at both levels is better than only at the variable level.

Weaknesses and suggestions
- Baseline tuning parity: Neural models are run with five seeds and grid search for the proposed method (72 configs), but classical baselines appear fixed to “as reported” hyperparameters; LR and XGBoost show 0.000 std, suggesting no seed variation. Stronger fairness would include validation-based tuning for LR/XGBoost and multiple random splits or bootstrapped CIs for all methods.
- Statistical significance: Means ± SD are provided, but there is no significance testing (e.g., DeLong or bootstrap CIs on test AUROC/AUPRC). Please add.
- Preprocessing clarity: Hourly windowing details, imputation strategy, normalization, and the exact list of 32 variables (and their handling when absent) should be fully specified. Clarify whether medication orders or culture-related features are included (potential for label leakage given Sepsis-3 labeling).
- Calibration and clinical operating points: Provide calibration metrics (e.g., ECE, reliability plots) and thresholded metrics (e.g., PPV at 80% sensitivity, specificity at 0.8 sensitivity) to contextualize clinical utility.
- Generalization and shift: Cross-dataset transfer (train on one dataset, test on the other) and subgroup analyses (age, sex, race, ICU type, hospital) would strengthen the case for robustness.
- Additional baselines: Consider time-aware Transformers with relative time encodings, ODE-RNN/GRU-ODE-Bayes, or temporal convolutional models with delta-time embeddings; also include a simple recency-weighted RETAIN or fixed exponential decay baseline to better isolate the benefit of learned decay.
- Interpretability caveat: Attention weights can be unstable and are not guaranteed causal explanations. Consider sanity checks (e.g., attention randomization tests) or agreement with gradient-based attributions.
- Sensitivity analyses: Vary window sizes, number of variables, and decay initialization; report learned decay parameters per variable (are they plausible clinically?).
- Reporting: Training time, parameter counts, and inference cost would help adoption considerations.

Soundness (0–100): 85
- The method is technically sound, well-motivated, and constrained to non-increasing influence with time. Ablations support the design. Some evaluation aspects (significance tests, calibration, tuning parity) can be improved.

Novelty (0–100): 77
- The idea of learned decay for irregular intervals exists (e.g., GRU-D), and interpretable attention is established (RETAIN). The contribution is the clean integration of learned time decay into both attention levels for interpretable early warning, which is incremental but meaningful.

Significance (0–100): 83
- Modest but consistent gains on two large public ICU datasets with interpretable outputs are valuable for a high-impact clinical task. The approach is practical and easily adoptable.

Clarity (0–100): 89
- The paper is well written and organized. A few missing implementation details and evaluation clarifications (preprocessing, variable list, calibration, significance) would further enhance clarity.

Final average score: 83.5

Recommendation: Accept

Rationale for acceptance: The paper addresses a clinically important problem with a simple, interpretable, and effective enhancement to attention models for irregular EHR time series. Results show consistent improvements over strong baselines on two datasets, with meaningful interpretability. While some evaluation and reporting aspects could be strengthened, the contribution is sufficiently sound, novel in its integration, and practically significant to merit acceptance.