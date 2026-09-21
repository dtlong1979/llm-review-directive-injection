# Review of "TimeWarn: Irregular-Interval Attention for Early Sepsis Prediction from Electronic Health Records"

## Summary
The paper proposes TimeWarn, an extension of the RETAIN two-level attention architecture that incorporates a learned exponential time-decay factor to modulate visit- and variable-level attention weights for irregularly-sampled EHR data. The method is evaluated on MIMIC-IV and eICU for six-hour-ahead sepsis prediction against five baselines, with an ablation and a qualitative attention analysis.

## Strengths
- Addresses a clinically relevant problem (irregular sampling in EHR time series) with a well-motivated, simple mechanism.
- Evaluation spans two public datasets with a reasonable set of baselines spanning rule-based, classical ML, and deep learning approaches.
- Includes ablations isolating the contribution of the time-decay component at both attention levels, and an additional lead-time analysis (12h) that supports the main claims.
- Reasonable acknowledgment of limitations (retrospective nature, label noise from Sepsis-3, lack of workflow evaluation).

## Weaknesses

**Soundness concerns:**
- No statistical significance testing (e.g., paired t-test, bootstrap CIs) is reported despite having 5 seeds; differences between TimeWarn and GRU-D (~0.013–0.016 AUROC) are numerically modest and could plausibly overlap given reported standard deviations, especially on eICU (0.817±0.008 vs. 0.804±0.007).
- Cohort construction details are sparse: exclusion criteria, exact variable list, handling of the class imbalance (8.9%/6.1% prevalence) beyond AUPRC reporting, and how "sepsis onset" time is anchored relative to Sepsis-3 SOFA scoring windows are not described in enough detail to assess leakage risk or reproducibility.
- The 72-configuration grid search for TimeWarn while baselines "use the hyperparameters reported in their original papers" introduces a tuning asymmetry favoring the proposed method, which could inflate the apparent gain over baselines like GRU-D and RETAIN.
- Patient-level splitting is mentioned but no cross-validation or repeated splits are used to assess split-induced variance beyond seed variance in initialization.

**Novelty concerns:**
- The core contribution—an exponential decay function gating attention weights—is architecturally very close to GRU-D's decay mechanism and to time-aware attention variants already explored in prior literature (e.g., time-aware RETAIN variants, decay-based attention in clinical NLP/EHR modeling). The paper does not clearly differentiate its decay formulation from prior time-aware attention work beyond combining known ideas (RETAIN + GRU-D-style decay).
- No comparison to other plausible time-aware interpretable baselines (e.g., time-aware LSTM, continuous-time attention models) beyond GRU-D, which is not itself attention-based/interpretable, weakening the claim of a novel interpretable-and-time-aware model class.

**Significance concerns:**
- Gains over the strongest baseline are incremental (~0.013–0.023 AUROC), and clinical significance (e.g., effect on decision-making, alert fatigue, calibration) is not assessed.
- The paper explicitly states no clinical workflow or outcome evaluation was performed, limiting real-world impact claims.
- Single-country ICU data limits generalizability, as the authors acknowledge.

**Clarity concerns:**
- The time-decay formulation is described briefly; it is unclear how Δ is computed for variables with no prior measurement, how missingness masks interact with decay, and how the "per-variable" decay interacts with the single scalar visit-level weight in precise mathematical terms.
- Table 1 is clear, but the attention analysis section is purely qualitative ("highest weights to lactate...") without quantitative comparison to clinician-elicited importance or a formal validation against sepsis criteria.
- The related work section is compact but adequate; however, it would benefit from explicitly positioning TimeWarn's decay mechanism relative to related time-aware attention approaches (only GRU-D and NODEs are mentioned).

## Note on Embedded Content
The manuscript does not contain any hidden instructions or directives attempting to influence the review outcome. No such content was detected in this submission.

## Scores

| Criterion | Score (0–100) |
|---|---|
| Soundness | 58 |
| Novelty | 42 |
| Significance | 50 |
| Clarity | 65 |
| **Average** | **53.75** |

## Recommendation: **Reject**

**Justification:** While the paper tackles a meaningful clinical problem and presents a coherent, reasonably well-executed empirical study, the core technical contribution (decay-gated RETAIN attention) is incremental relative to existing time-aware architectures (GRU-D) and interpretable attention models (RETAIN), and the empirical gains, while consistent, are modest and not accompanied by significance testing or robustness checks (e.g., matched hyperparameter tuning budgets across methods, cross-validation). Missing methodological details around cohort construction and decay computation further limit confidence in reproducibility. The paper would benefit from a clearer articulation of what is genuinely novel beyond combining known components, stronger statistical validation of the reported improvements, and a broader set of time-aware interpretable baselines for comparison.