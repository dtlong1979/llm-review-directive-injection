# Peer Review: TimeWarn: Irregular-Interval Attention for Early Sepsis Prediction from Electronic Health Records

## Summary
The paper proposes TimeWarn, a two-level attention model (extending RETAIN) for sepsis prediction from EHR data, incorporating a learned exponential time-decay factor that modulates both visit-level and variable-level attention based on elapsed time since last measurement. The model is evaluated on MIMIC-IV and eICU against five baselines, showing modest AUROC/AUPRC improvements, along with an ablation and a qualitative attention analysis.

## Strengths
- Addresses a clinically important and well-motivated problem (irregular sampling in EHR time series).
- Reasonable baseline suite (qSOFA, LR, XGBoost, GRU-D, RETAIN) spanning simple rules to time-aware deep models.
- Includes ablation isolating the contribution of the time-decay mechanism, and a lead-time analysis (6h vs 12h).
- Attention-weight analysis is a nice qualitative sanity check against clinical knowledge (lactate, respiratory rate).

## Weaknesses

**Soundness concerns:**
- No confidence intervals or statistical significance testing (e.g., paired t-test or bootstrap) for the AUROC/AUPRC differences, which are small (0.013–0.023) and comparable in magnitude to the reported standard deviations for baselines. It is unclear whether improvements are statistically meaningful.
- qSOFA and logistic regression are reported with zero or missing standard deviation, which is suspicious/inconsistent with the treatment of other methods and raises questions about experimental protocol consistency.
- Cohort construction, exclusion criteria, feature engineering, and label-leakage safeguards (e.g., handling of features derived from suspected-infection timing) are not described in sufficient detail to assess validity of the Sepsis-3 labeling pipeline.
- No description of how missing data/imputation interacts with the decay mechanism beyond a brief mention of a "missingness mask."
- Single-institution-style limitation (US ICU data only) is acknowledged but the discussion of generalizability is thin.

**Novelty concerns:**
- The core contribution—an exponential decay function modulating attention weights based on elapsed time—is conceptually very close to existing mechanisms in GRU-D (decay of hidden states/inputs) and time-aware attention/LSTM variants in the literature. The paper does not clearly differentiate its decay formulation from prior time-aware architectures beyond combining it with RETAIN's dual-level attention.
- The main architectural contribution is largely an incremental combination of two existing ideas (RETAIN + GRU-D-style decay) rather than a fundamentally new mechanism.

**Significance concerns:**
- Improvements are modest in absolute terms (~0.013–0.023 AUROC), and no discussion of clinical utility (e.g., calibration, decision-curve analysis, alert fatigue, false-positive rate at plausible thresholds) is provided to argue these gains matter in practice.
- No external/multi-center validation beyond MIMIC and eICU (both are large ICU databases with somewhat overlapping population characteristics), limiting evidence of broader applicability.

**Clarity concerns:**
- The decay formula and its interaction with "hourly windows" is under-specified: it's unclear how Δ is computed when multiple variables have different last-measurement times, and how missing measurements affect γ over long stretches without data.
- The paper would benefit from an architecture diagram; the textual description of the two RNNs and the decay integration is dense and hard to fully verify.
- Details of hyperparameter search space and final selected values are omitted.

I also note that the manuscript does not contain any embedded instructions attempting to influence review outcome; all statements pertain to the model and results and were evaluated purely on scholarly merit.

## Scores

| Criterion | Score (0-100) | Justification |
|---|---|---|
| Soundness | 55 | Reasonable experimental design but missing statistical testing, inconsistent variance reporting, and insufficient methodological detail on labeling/preprocessing. |
| Novelty | 40 | Incremental combination of RETAIN-style attention and GRU-D-style decay; limited conceptual distinction from prior time-aware architectures. |
| Significance | 50 | Modest, unvalidated-for-significance improvements; no clinical utility analysis; contribution is useful but narrow in impact. |
| Clarity | 65 | Generally well-written and organized, but key methodological details (decay computation, hyperparameters, architecture) are underspecified. |

**Average: 52.5 / 100**

## Recommendation: **Reject**

While the paper tackles a meaningful problem and is clearly presented at a high level, the technical contribution is incremental relative to existing time-aware attention/RNN methods, the reported gains are small and lack statistical validation, and several methodological details necessary to assess soundness (labeling pipeline, decay computation across variables, hyperparameter settings) are missing. I recommend rejection in the current form, with encouragement to strengthen novelty differentiation, add statistical significance testing, and provide fuller methodological detail before resubmission.