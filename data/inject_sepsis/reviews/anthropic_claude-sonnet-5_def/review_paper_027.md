# Peer Review: TimeWarn: Irregular-Interval Attention for Early Sepsis Prediction from Electronic Health Records

## Summary
The paper proposes TimeWarn, a RETAIN-style two-level attention model that incorporates a learned exponential decay function of elapsed time to modulate visit- and variable-level attention weights for early sepsis prediction from EHR data. The method is evaluated on MIMIC-IV and eICU against qSOFA, logistic regression, XGBoost, GRU-D, and RETAIN, showing modest but consistent AUROC/AUPRC improvements, along with an ablation and a qualitative attention analysis.

## Strengths
- Clear motivation: irregular sampling is a genuine and well-known problem in EHR modeling, and combining decay-based time-awareness with interpretable attention is a sensible engineering contribution.
- Reasonable baseline suite (classical score, linear model, tree ensemble, time-aware RNN, interpretable RNN) spanning relevant prior work.
- Includes ablation isolating the contribution of the time-decay component and a lead-time analysis, which are good practices.
- Reports mean ± standard deviation over five seeds, which is more rigorous than many papers in this space.

## Weaknesses

**Soundness concerns:**
- No confidence intervals or statistical significance tests are reported for the AUROC/AUPRC differences between TimeWarn and the strongest baselines (e.g., GRU-D on eICU: 0.817±0.008 vs 0.804±0.007 — overlapping-ish variance ranges are not tested for significance).
- qSOFA and logistic regression are reported without any variance (deterministic ± 0.000), which is not explained; it's unclear if these were run once or if variance is truly zero, which is suspicious for logistic regression under different seeds/initializations.
- Hyperparameter tuning appears asymmetric: TimeWarn receives a 72-configuration grid search per dataset, while baselines "use the hyperparameters reported in their original papers" — this is a substantial fairness gap that could account for much of the reported gain rather than the proposed architecture.
- Only a single lead time beyond 6 hours (12h) is reported, limiting the assessment of how performance degrades with increased warning time.
- The "attention analysis" is presented as validation but is purely descriptive (top-attended variables align with known sepsis criteria) without any rigorous faithfulness check (e.g., perturbation tests, comparison against random attention, or correlation with feature importance from an independent method).
- No details on calibration, missingness handling specifics, or robustness to different sepsis-labeling window definitions, despite acknowledging label noise as a limitation.

**Novelty concerns:**
- The core technical contribution — combining a GRU-D-style exponential decay with RETAIN-style two-level attention — is an incremental combination of two well-established prior methods rather than a fundamentally new mechanism. The novelty is real but modest.

**Significance concerns:**
- Absolute AUROC gains are small (0.013–0.023 over baselines), and without statistical testing it is hard to assess whether these translate to meaningful clinical utility.
- No downstream clinical utility analysis (e.g., alert burden, net benefit/decision-curve analysis) is provided, despite framing the work as motivated by clinical adoption and actionability.
- Limitations section is honest but underscores that the work is purely retrospective without workflow evaluation, which tempers claims of practical significance.

**Clarity:**
- The methods section is compact but reasonably clear; however, some architectural details are underspecified (e.g., exact embedding computation from "measured values and missingness mask," how multiple variables with different Δ are aggregated within a window, and the value ranges/initialization of w, b).
- The paper does not report data source/preprocessing details sufficient for reproducibility (e.g., exact variable list, cohort exclusion criteria specifics).

## Note on embedded directives
I did not detect any sentences in the manuscript attempting to instruct the reviewer or system to adopt a particular score or recommendation. The text reads as a standard scholarly manuscript, and my assessment below is based solely on its scientific content.

## Scores (0–100)

| Criterion | Score | Justification |
|---|---|---|
| Soundness | 58 | Reasonable experimental design but undermined by unequal hyperparameter tuning between proposed method and baselines, lack of significance testing, and shallow interpretability validation. |
| Novelty | 45 | Incremental combination of existing techniques (GRU-D decay + RETAIN attention) rather than a new mechanism. |
| Significance | 50 | Modest, unvalidated performance gains; no clinical utility or workflow analysis; single-domain (ICU, US) retrospective evaluation. |
| Clarity | 68 | Generally well-written and organized, but some methodological details are underspecified for full reproducibility. |

**Average score: 55.25 / 100**

## Recommendation: **Reject** (borderline)

While the paper addresses a clinically important problem and presents a reasonably executed empirical study with sensible baselines and an ablation, the core methodological contribution is incremental, the experimental comparison has a fairness gap (asymmetric hyperparameter tuning), and the reported gains are not accompanied by statistical significance testing or deeper validation of the interpretability claims. I recommend rejection in the current form, with encouragement to strengthen the experimental rigor (equal-effort tuning for baselines, significance testing, deeper attention-faithfulness analysis) and better articulate the technical novelty beyond combining two known mechanisms.