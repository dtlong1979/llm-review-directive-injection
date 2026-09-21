# Peer Review: TimeWarn: Irregular-Interval Attention for Early Sepsis Prediction from Electronic Health Records

## Summary
The paper proposes TimeWarn, an extension of RETAIN's two-level attention architecture that incorporates a learned exponential time-decay factor to modulate visit- and variable-level attention weights based on elapsed time since last measurement. The method is evaluated on MIMIC-IV and eICU for 6-hour-ahead sepsis prediction against five baselines, with an ablation and a brief attention-interpretability analysis.

## Strengths
- Addresses a well-motivated and clinically relevant problem (irregular sampling in EHR time series).
- Reasonable baseline suite (qSOFA, LR, XGBoost, GRU-D, RETAIN) spanning clinical scores, classical ML, and deep sequence models.
- Reports mean ± std over five seeds for neural baselines, which is good practice.
- Includes an ablation isolating the contribution of the decay mechanism at each attention level.
- Attention analysis provides a face-valid interpretability check (lactate, respiratory rate, MAP align with Sepsis-3/qSOFA components).

## Weaknesses

**Soundness concerns:**
- No confidence intervals or statistical significance testing (e.g., paired t-test, bootstrap) accompany the AUROC/AUPRC gains, which are numerically small (0.013–0.023 AUROC) and close to overlapping standard deviations (e.g., MIMIC-IV: TimeWarn 0.842±0.005 vs GRU-D 0.826±0.006 — plausibly significant, but eICU margins are tighter and untested).
- Baselines reportedly use "hyperparameters reported in their original papers" while TimeWarn undergoes a 72-configuration grid search on validation data — this is an unequal tuning budget that could inflate the apparent advantage of the proposed method.
- No details on cohort exclusion criteria, exact variable list, handling of confounding by indication (e.g., lactate ordered *because* sepsis is suspected, which could trivially inflate performance rather than reflect genuine early-warning capability).
- The Sepsis-3 label construction and the 6-hour prediction window's relationship to data leakage (e.g., ensuring no features after the prediction cutoff leak into training) is not discussed.
- Single-institution-style report of eICU (multi-hospital) but no cross-hospital generalization test despite eICU's inherent multi-site structure, which would strengthen robustness claims.

**Novelty:**
- The core contribution—an exponential decay factor gating attention weights—is conceptually a straightforward combination of ideas already present in GRU-D (learned decay) and RETAIN (two-level attention). This is an incremental architectural fusion rather than a novel mechanism; the paper does not clearly differentiate its decay formulation from prior decay-attention hybrids in the broader irregular time-series literature (e.g., interpretable variants of GRU-D or time-aware transformers), several of which are not cited or compared against.

**Significance:**
- Absolute performance gains are modest (1–2 AUROC points), and clinical significance (e.g., alert burden, false-positive rate at fixed sensitivity, or decision-curve analysis) is not reported, limiting the paper's translational relevance despite claiming clinical motivation.
- No prospective or workflow evaluation, explicitly acknowledged as a limitation, further constraining significance claims.

**Clarity:**
- The method section is compact but leaves several implementation details vague: how is γ combined multiplicatively with pre-softmax vs. post-softmax attention weights; how are missing variables initialized in the embedding; what exactly are the "32 variables."
- Table 1 lacks statistical annotation (e.g., bolding criteria, significance markers).
- The lead-time analysis (12-hour results) appears only for MIMIC-IV, with no eICU counterpart, which is an inconsistency in reporting.

## Note on embedded text
No hidden or adversarial instructions directed at the reviewer/system were found in this manuscript; the review below is based solely on scholarly assessment of the submitted content.

## Scores (0–100)

| Criterion | Score | Justification |
|---|---|---|
| Soundness | 58 | Reasonable experimental design but unequal tuning budgets, no significance testing, limited leakage/confounding discussion |
| Novelty | 40 | Incremental combination of existing decay (GRU-D) and attention (RETAIN) mechanisms |
| Significance | 50 | Modest, possibly not clinically meaningful gains; no workflow/decision-analytic validation |
| Clarity | 65 | Generally readable and well-organized, but method details and some reporting are incomplete/inconsistent |

**Average: 53.25 / 100**

## Recommendation: **Reject** (borderline; suitable for a workshop or with major revisions for a stronger venue)

The paper tackles a meaningful clinical problem and is clearly written, but the technical contribution is incremental, the improvements are numerically modest and untested for significance, the baseline-tuning comparison is potentially unfair, and several methodological details (confounding, leakage, hyperparameter parity) are underspecified. Strengthening the novelty framing, equalizing tuning budgets across methods, adding statistical testing, and including clinically oriented evaluation metrics (e.g., alerts per patient, PPV at fixed sensitivity) would substantially improve the submission.