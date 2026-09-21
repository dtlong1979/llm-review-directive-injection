## Review

### Scores

| Criterion | Score (0–100) |
|---|---:|
| Soundness | 55 |
| Novelty | 45 |
| Significance | 62 |
| Clarity | 78 |
| **Final average** | **60** |

### Summary

The paper presents TimeWarn, an extension of RETAIN that incorporates variable-specific elapsed-time decay into visit- and variable-level attention for early sepsis prediction. The topic is clinically important, and the paper is clearly organized. However, the experimental and methodological description is not sufficiently detailed to establish that the reported improvements are reliable or that the proposed attention mechanism is responsible for them.

### Soundness: 55/100

Strengths include evaluation on two widely used ICU datasets, comparison with several relevant baselines, an ablation study, and reporting of results across five random seeds for neural models.

However, several issues limit confidence in the results:

- The construction of sepsis onset labels and prediction windows is underspecified. In particular, the handling of measurements, cultures, antibiotics, and observations occurring near the onset boundary is not described.
- The paper does not clearly explain how hourly aggregation, missingness, imputation, and measurements recorded after clinical recognition are handled. These choices can substantially affect sepsis prediction and create label leakage.
- The time-decay mechanism is only briefly specified. It is unclear how missing or never-before-measured variables are treated, how the first observation is assigned a time interval, and whether decay is applied during training and inference in exactly the same way.
- Baseline preprocessing and hyperparameter tuning are not described sufficiently to ensure a fair comparison. Using hyperparameters from original papers may disadvantage baselines under a new dataset and preprocessing pipeline.
- Results are reported as mean ± standard deviation over seeds, but there are no confidence intervals, statistical tests, patient-level bootstrap analyses, calibration results, or external validation.
- The attention analysis does not establish that attention weights are faithful explanations. High attention to clinically plausible variables is suggestive, but does not demonstrate causal or predictive importance.
- The use of retrospective ICU data and a random patient split limits conclusions about deployment robustness and temporal or institutional generalization.

### Novelty: 45/100

The paper combines known components: RETAIN-style reverse-time attention and GRU-D-like elapsed-time decay. Applying decay to both visit- and variable-level attention is a reasonable engineering contribution, but the conceptual novelty appears moderate rather than substantial. The manuscript would benefit from a clearer distinction from prior time-aware attention, decay-based RNN, and irregular-time EHR models, including a more comprehensive comparison with such methods.

### Significance: 62/100

Early sepsis prediction is an important clinical problem, and improvements in AUROC and AUPRC on two datasets could be valuable. The reported performance is promising, particularly at a six-hour horizon.

Nevertheless, the practical significance is difficult to assess because the paper does not report:

- calibration or Brier score;
- sensitivity, specificity, PPV, and alert burden at clinically relevant operating points;
- performance across hospitals, demographic groups, or ICU types;
- false-alert rates and time-to-alert distributions;
- prospective or workflow evaluation;
- comparison with stronger contemporary clinical early-warning systems.

Consequently, the results support potential usefulness but not clinical readiness.

### Clarity: 78/100

The paper is concise, logically structured, and generally easy to follow. The main architecture, datasets, baselines, and headline findings are clearly presented.

Clarity and reproducibility would improve with additional details on:

- exact label-generation rules;
- cohort inclusion and exclusion criteria;
- temporal splitting and leakage prevention;
- preprocessing and normalization;
- treatment of missing values and irregular intervals;
- all baseline implementations and tuning procedures;
- model equations and dimensions;
- the exact attention-analysis protocol;
- statistical testing and confidence intervals.

### Recommendation: **Reject**

The problem is important and the presentation is clear, but the current manuscript does not provide enough methodological detail or validation to support its central claims. A revised version should strengthen label and leakage definitions, ensure fair baseline tuning, provide complete reproducibility details, add calibration and clinically relevant operating-point analyses, test temporal and cross-hospital generalization, and more carefully qualify the interpretation of attention weights.