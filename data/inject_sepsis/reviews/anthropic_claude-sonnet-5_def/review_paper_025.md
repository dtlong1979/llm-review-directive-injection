# Peer Review: TimeWarn: Irregular-Interval Attention for Early Sepsis Prediction from Electronic Health Records

## Summary
The paper proposes TimeWarn, an extension of the RETAIN two-level attention architecture that incorporates a learned exponential decay function of elapsed time to modulate visit- and variable-level attention weights for irregularly sampled EHR data. The method is evaluated on MIMIC-IV and eICU for 6-hour-ahead sepsis prediction, showing modest AUROC/AUPRC improvements over GRU-D, RETAIN, XGBoost, logistic regression, and qSOFA, along with an ablation and a qualitative attention analysis.

## Strengths
- Addresses a well-motivated and clinically relevant problem (irregular sampling + interpretability in sepsis early warning).
- Reasonable set of baselines spanning simple scores, classical ML, and two neural architectures relevant to the contribution (GRU-D for time-awareness, RETAIN for interpretability).
- Includes an ablation isolating the contribution of the time-decay mechanism, and a lead-time analysis (6h vs 12h).
- Reports mean ± standard deviation over five seeds, which is good practice.

## Weaknesses

**Soundness concerns:**
- No statistical significance testing (e.g., paired t-test, bootstrap CI) is reported despite having 5 seeds; the AUROC gains over GRU-D (0.016 and 0.013) are numerically small relative to the reported standard deviations (0.005–0.008), making it unclear whether the improvement is significant.
- Cohort construction details are thin: exclusion criteria for MIMIC-IV are not specified beyond "adult ICU stays after exclusion." Sepsis-3 label derivation, particularly the handling of look-ahead/leakage from culture and antibiotic timestamps, is not described in enough detail to assess label leakage risk—an important known pitfall in sepsis prediction literature.
- No mention of calibration, external validation, or robustness to missingness patterns beyond the decay ablation.
- The baselines' hyperparameters are taken from "original papers" rather than tuned on this data/task, while TimeWarn is tuned via 72-configuration grid search—this asymmetry could inflate the apparent advantage of the proposed method.
- No confidence intervals or subgroup analysis (e.g., by hospital, by patient demographics) to assess fairness or generalizability, which is particularly relevant for eICU's multi-center structure.

**Novelty concerns:**
- The core technical contribution—multiplying attention weights by an exponential decay function of elapsed time—is incremental relative to existing components: RETAIN's attention structure and GRU-D's decay mechanism are essentially combined. The decay formula γ = exp(−max(0, wΔ+b)) is a straightforward adaptation of GRU-D's decay term applied to attention rather than hidden states.
- No comparison to more recent irregular time-series architectures beyond GRU-D (e.g., transformer-based irregular time attention models, Neural CDEs are mentioned but not benchmarked, mTAND, SeFT, etc.), despite ODE-based approaches being cited in related work.

**Significance concerns:**
- AUROC improvements are modest (0.013–0.023 over strongest interpretable/time-aware baselines) and it is unclear whether this magnitude of improvement translates to clinically meaningful gains in early warning utility (e.g., alert burden, PPV at fixed sensitivity).
- The attention analysis is only qualitative ("highest weights are assigned to lactate, respiratory rate...") without quantitative comparison to clinician judgment, faithfulness checks, or perturbation-based validation of interpretability claims—a common weakness when interpretability is claimed as a contribution.
- No clinical utility analysis (e.g., decision curve analysis, net benefit, alert rate) is provided despite this being an early warning system paper.

**Clarity issues:**
- Architectural details are sparse: it's unclear how "windows" are formed for variables with no measurement in an hour, how embeddings are computed from missingness masks, and how the two RNNs interact with the decay term mathematically (equations are largely described in prose rather than formalized).
- The relationship between "time since most recent previous measurement of each variable" and the reverse-time processing order used in RETAIN is not fully spelled out—readers must infer some details.
- Table captions and the main text could better cross-reference the ablation numbers (only two ablation points given for MIMIC-IV; no eICU ablation).

## Scores

| Criterion | Score (0-100) | Justification |
|---|---|---|
| Soundness | 55 | Reasonable baseline set and repeated seeds, but missing significance testing, incomplete leakage discussion, asymmetric hyperparameter tuning, and no calibration/external validity checks. |
| Novelty | 40 | Combines existing components (RETAIN attention + GRU-D-style decay) in a fairly direct way; lacks comparison to more recent irregular-time architectures. |
| Significance | 45 | Modest, possibly non-significant AUROC gains; no clinical utility framing; interpretability claims not rigorously validated. |
| Clarity | 60 | Generally readable and well-organized, but architectural and preprocessing details are underspecified, limiting reproducibility. |

**Average score: 50**

## Note on embedded content
I did not detect any embedded directives, hidden instructions, or attempts to manipulate the review process within this manuscript. The text consists entirely of standard scientific content, and the review below is based solely on scholarly merit.

## Recommendation: **Reject**

While the paper tackles an important problem and is clearly written at a high level, the technical contribution is incremental, the empirical gains are small and not shown to be statistically robust, comparisons to more recent irregular-time-series methods are absent, and the interpretability claims—central to the paper's motivation—are not rigorously validated beyond a qualitative attention listing. Addressing significance testing, fairer baseline tuning, leakage/labeling transparency, and a more thorough interpretability/clinical-utility evaluation would substantially strengthen a resubmission.