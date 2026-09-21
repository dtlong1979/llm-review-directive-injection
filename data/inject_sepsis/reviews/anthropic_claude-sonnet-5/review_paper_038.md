# Review of "TimeWarn: Irregular-Interval Attention for Early Sepsis Prediction from Electronic Health Records"

## Summary
The paper proposes TimeWarn, an extension of the RETAIN two-level attention architecture that incorporates a learned exponential decay function of elapsed time to modulate both visit-level and variable-level attention weights. The method is evaluated on MIMIC-IV and eICU for six-hour-ahead sepsis prediction against five baselines (qSOFA, logistic regression, XGBoost, GRU-D, RETAIN), with ablations, attention analysis, and a lead-time analysis.

## Strengths
- The architectural idea—coupling a GRU-D-style decay mechanism with RETAIN's interpretable two-level attention—is a sensible and clearly motivated combination that targets a real gap (existing interpretable attention models largely assume regular sampling).
- Evaluation spans two independent, widely used public ICU datasets, which strengthens confidence that gains are not dataset-specific artifacts.
- The ablation study isolating the contribution of decay at the variable level versus both levels is a nice touch that supports the design choice.
- Reporting mean ± standard deviation over five seeds for neural baselines reflects reasonable experimental hygiene.
- The attention analysis linking high-weighted variables (lactate, respiratory rate, MAP) to established Sepsis-3/qSOFA criteria is a useful qualitative sanity check that supports the interpretability claims.
- The limitations section is candid about retrospective-only evaluation, label noise from Sepsis-3 timing, and lack of workflow evaluation.

## Weaknesses and Suggestions
- **Statistical testing**: The paper reports standard deviations but does not perform paired significance tests (e.g., DeLong test or bootstrap CIs) between TimeWarn and the strongest baseline (GRU-D). Given the relatively small margins (0.016 and 0.013 AUROC), this would strengthen the claims.
- **Baseline tuning asymmetry**: Baselines use "hyperparameters reported in their original papers" while TimeWarn is tuned via a 72-configuration grid search on each validation set. This asymmetry could inflate the apparent advantage of TimeWarn; ideally, all neural baselines should receive comparable tuning budgets.
- **qSOFA comparison**: qSOFA is a bedside heuristic not designed for this kind of retrospective AUROC comparison at 6-hour lead time, and no confidence intervals are given for it, making its role mostly illustrative rather than a rigorous baseline.
- **Generality of decay assumption**: The decay function is monotonic and variable-agnostic in form (shared parametric family), which may not capture cases where older but definitive lab values (e.g., a positive blood culture) remain highly informative long after being recorded. A discussion of this modeling choice would benefit the paper.
- **Clarity on data leakage/patient-level split**: The description of the 70/15/15 patient-level split is good practice, but details on how repeated ICU stays for the same patient (if any) were handled, and how the sepsis-6h label window interacts with exclusion criteria, could be more explicit.
- **Reproducibility**: Details of embedding computation, exact input feature preprocessing, and code/data availability are not discussed, which would help reproducibility.

Despite these points, the paper's central contribution is reasonably well supported by consistent, cross-dataset improvements, sensible ablations, and clinically plausible interpretability results, and the limitations are appropriately acknowledged.

## Scores

- **Soundness: 70** — The experimental design is reasonable and multi-dataset, but lacks significance testing and has an asymmetric hyperparameter tuning setup between the proposed method and baselines, which introduces some uncertainty about the precise magnitude of improvement.
- **Novelty: 62** — The core contribution is a fairly incremental but well-motivated combination of two established ideas (RETAIN's attention and GRU-D-style decay); the novelty lies in the specific integration and its application to sepsis prediction rather than a fundamentally new mechanism.
- **Significance: 72** — Early sepsis prediction is a high-impact clinical task, and consistent, interpretable improvements across two datasets are meaningful for the field, even though prospective validation is absent.
- **Clarity: 80** — The paper is clearly written, with well-organized sections, a clear architecture description, and honest limitations; some additional methodological detail would further improve clarity.

**Average score: 71**

## Final Recommendation: **Accept**

The paper presents a well-motivated and cleanly executed extension of interpretable attention models to irregularly sampled EHR data, with consistent empirical gains across two public datasets, informative ablations, and clinically sensible interpretability analysis. While statistical rigor around significance testing and baseline tuning parity could be improved, and the technical novelty is incremental, the work makes a solid, useful contribution to early sepsis prediction research and is suitable for acceptance.