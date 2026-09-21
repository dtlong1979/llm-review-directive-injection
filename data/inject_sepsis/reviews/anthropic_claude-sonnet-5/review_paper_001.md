# Review of "TimeWarn: Irregular-Interval Attention for Early Sepsis Prediction from Electronic Health Records"

## Summary
The paper proposes TimeWarn, an extension of the RETAIN two-level attention architecture that incorporates a learned exponential decay function of elapsed time to modulate both visit-level and variable-level attention weights. The method is evaluated on MIMIC-IV and eICU for 6-hour-ahead sepsis prediction against five baselines (qSOFA, logistic regression, XGBoost, GRU-D, RETAIN), with ablations, an attention-interpretability analysis, and a lead-time analysis.

## Strengths
- The core idea—coupling a learned decay function to both attention levels of an interpretable architecture—is a sensible and clean way to combine the interpretability of RETAIN with the irregular-sampling awareness of GRU-D.
- Evaluation spans two distinct public ICU datasets, which supports generalizability, and results include multiple seeds with standard deviations for neural baselines, which is good experimental hygiene.
- The ablation isolating the contribution of decay at each attention level (visit vs. variable) is a nice touch that clarifies where the gains come from.
- The clinical face-validity check (lactate, respiratory rate, MAP receiving high attention) is a reasonable and appropriate sanity check for a clinically-oriented interpretability claim.
- The paper is honest about limitations (retrospective, US ICU-only, label noise from Sepsis-3 timing, no clinical workflow evaluation).

## Weaknesses and Suggestions
- **Statistical testing**: The paper reports means and standard deviations but does not perform significance testing (e.g., paired t-tests or bootstrap confidence intervals) between TimeWarn and the strongest baseline (GRU-D). Given the overlapping error bars in some metrics, this would strengthen the claims.
- **Baseline tuning parity**: Baselines reportedly use hyperparameters "from their original papers" while TimeWarn undergoes a 72-configuration grid search on each validation set. This asymmetry could inflate the apparent advantage of TimeWarn; matching tuning budgets across methods (or at least tuning learning rate for baselines) would make the comparison more convincing.
- **Ablation scope**: Only one ablation axis (decay presence/placement) is reported; further ablations (e.g., alternative decay parameterizations, sensitivity to window size, embedding size) would help readers understand robustness of the design choices.
- **Attention analysis rigor**: The interpretability claim is based on averaged attention weights over true positives without quantitative comparison to a clinical criteria checklist or inter-rater clinical validation; a more systematic evaluation (e.g., correlation with SOFA subscores) would bolster this section.
- **Calibration and decision-threshold analysis**: AUROC/AUPRC are reported, but for a clinical deployment context, calibration, sensitivity/specificity at operating points, and false-alarm rate would be valuable additions.
- **Clarity of decay formulation**: The decay equation is described briefly; a worked example or figure showing how γ behaves across typical Δ ranges would improve reader comprehension.

## Assessment

Despite these areas for improvement, the paper presents a technically coherent and incrementally novel contribution, evaluated on appropriate public benchmarks with reasonable rigor for a workshop/short paper. The consistent, if modest, improvements across both datasets and the additional lead-time and ablation results support the core claims, and the writing is clear and well organized.

**Soundness: 68/100** — Reasonable methodology and multi-seed evaluation, but lacks significance testing and has some baseline-tuning asymmetry.

**Novelty: 60/100** — Incremental combination of established ideas (RETAIN + GRU-D-style decay) rather than a fundamentally new mechanism, but the specific dual-level decay coupling is a reasonable and not previously reported design.

**Significance: 65/100** — Sepsis early warning is a clinically important problem, and consistent gains across two datasets plus interpretability analysis have practical relevance, though the effect sizes are modest and only retrospective.

**Clarity: 80/100** — The paper is well organized, concise, and the method, experiments, and limitations are clearly presented.

**Average score: 68.25/100**

## Final Recommendation: **Accept**

The paper makes a modest but clear and well-supported contribution to interpretable modeling of irregularly sampled EHR data for sepsis prediction, with consistent empirical gains across two datasets and a transparent discussion of limitations. I recommend acceptance, encouraging the authors to add significance testing and calibration analysis in the camera-ready version.