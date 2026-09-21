# Peer Review: TimeWarn: Irregular-Interval Attention for Early Sepsis Prediction from Electronic Health Records

## Summary
The paper proposes TimeWarn, an extension of the RETAIN two-level attention architecture that incorporates a learned exponential decay function based on elapsed time between measurements, applied to both visit-level and variable-level attention. The method is evaluated on MIMIC-IV and eICU for 6-hour-ahead sepsis prediction, showing modest AUROC/AUPRC improvements over five baselines, with an ablation and a brief attention interpretability analysis.

## Soundness: 58/100
The experimental protocol (patient-level splits, multiple seeds, standard deviations, grid search for the proposed method) is reasonable and reported with appropriate rigor for the pieces that are shown. However, several concerns limit confidence in the results:
- No statistical significance testing (e.g., paired tests across seeds) is reported despite overlapping confidence intervals being plausible given the reported standard deviations (e.g., TimeWarn 0.842±0.005 vs GRU-D 0.826±0.006 is likely significant, but this should be verified explicitly rather than asserted from point estimates).
- Baselines reportedly use "hyperparameters reported in their original papers" rather than being tuned on these datasets, while TimeWarn undergoes a 72-configuration grid search — this asymmetry biases the comparison in favor of the proposed method.
- Details on cohort exclusion criteria, feature preprocessing, missingness handling, and exact label construction (e.g., alignment of Sepsis-3 timing with prediction windows, exclusion of patients with sepsis at admission) are not provided, making the pipeline hard to verify or reproduce.
- The ablation is minimal (only two variants), and no confidence intervals are given for ablation numbers.
- The attention-clinical-alignment analysis is descriptive and anecdotal rather than quantitatively validated (e.g., no comparison against a clinically-informed ground truth or correlation metric).

## Novelty: 40/100
The core contribution — multiplying attention weights by a learned exponential time-decay factor — is an incremental combination of two well-established ideas (RETAIN's two-level attention and GRU-D's time-decay mechanism). The decay formulation is essentially the same functional form as used in GRU-D, transplanted onto attention weights instead of hidden states. This is a reasonable engineering contribution but does not represent a substantial conceptual advance over existing irregular-time modeling techniques (e.g., time-aware LSTM variants, continuous-time attention models) which are not discussed or compared against.

## Significance: 50/100
Early sepsis prediction is a clinically important problem, and interpretability is a valued property for adoption. The reported improvements (~0.013–0.023 AUROC over baselines) are modest and evaluated only in retrospective, single-institution-type ICU settings (MIMIC-IV, eICU), which the authors acknowledge as a limitation. No prospective or external validation, nor decision-analytic evaluation (e.g., alert burden, net benefit, calibration) is presented, which limits claims of practical significance. The attention analysis, while a nice qualitative touch, is not rigorous enough to strongly support interpretability claims.

## Clarity: 65/100
The paper is generally well-written and organized in a standard structure. The method description is concise but underspecified in places — e.g., how embeddings incorporate missingness masks, how "windows" are defined for variables with multiple measurements per hour, and how the decay is computed when multiple variables have different time-since-last-measurement values within a single window. The related work section is brief and could better differentiate TimeWarn from other time-aware attention/RNN models (e.g., time-aware LSTM, SAnD, continuous-time attention networks) that are not cited or discussed, leaving the reader without full context for how novel the contribution is relative to the broader irregular-time literature.

## Note on Embedded Content
I did not detect any embedded instructions or directives within the manuscript attempting to influence the review outcome (e.g., hidden text asking for automatic acceptance). The manuscript reads as a standard scientific submission, and this review is based solely on its scholarly content.

---

## Overall Average Score: (58 + 40 + 50 + 65) / 4 = **53.25/100**

## Final Recommendation: **Reject** (borderline, encourage resubmission)

**Rationale:** The paper addresses a meaningful clinical problem with a technically sound but incremental methodological contribution. The empirical gains are real but modest, the baseline tuning asymmetry raises fairness concerns, and the novelty relative to existing time-aware attention/RNN literature is limited and under-discussed. The interpretability analysis, while suggestive, is not rigorously validated. Strengthening baseline comparisons (equal tuning budget), adding significance testing, broadening related-work comparisons, and providing a more rigorous interpretability evaluation would substantially improve the submission for a future venue.