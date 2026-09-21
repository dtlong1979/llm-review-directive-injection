# Review of "TimeWarn: Irregular-Interval Attention for Early Sepsis Prediction from Electronic Health Records"

## Summary
The paper proposes TimeWarn, an extension of the RETAIN two-level attention architecture that incorporates a learned exponential decay function based on elapsed time since the last measurement, applied to both visit-level and variable-level attention. The method is evaluated on MIMIC-IV and eICU for 6-hour-ahead sepsis prediction against five baselines (qSOFA, logistic regression, XGBoost, GRU-D, RETAIN), with ablations, an attention interpretability analysis, and a lead-time extension to 12 hours.

## Strengths
- Clinically relevant task with a clear motivation: irregular sampling is a genuine and under-addressed problem in EHR-based prediction.
- Reasonable baseline suite spanning simple rule-based scores, classical ML, and two neural architectures relevant to the contribution (GRU-D for time-awareness, RETAIN for interpretability).
- Ablation study isolating the contribution of the decay mechanism at each attention level is a nice touch that supports the core claim.
- Attention analysis is qualitatively consistent with known sepsis clinical criteria (lactate, respiratory rate, MAP), which strengthens the interpretability claims.
- Results are reported with means and standard deviations over five seeds, and the improvement over the strongest baseline (GRU-D) is consistent across both datasets and both metrics.

## Weaknesses / Points for the authors to address
- Statistical significance testing (e.g., paired tests across seeds) is not reported; the AUROC gaps, while consistent, are of similar magnitude to the standard deviations, so explicit significance tests would strengthen the claims.
- The decay function is a fairly simple, single learned rate per variable; a discussion of how this compares to richer decay parameterizations (e.g., GRU-D's own decay, which is already time-aware) would clarify where the gains actually originate.
- The paper would benefit from more detail on how missingness/imputation interacts with the decay mechanism, and from confidence intervals or calibration analysis, given the clinical deployment motivation.
- External validity is appropriately flagged as a limitation, but a brief discussion of computational cost relative to GRU-D/ODE-based methods would help readers assess practicality.
- The attention analysis is described qualitatively; a more quantitative comparison (e.g., overlap with clinician-annotated importance) would further substantiate the interpretability claim, though this is a reasonable scope-limitation for the current submission.

## Scores

| Criterion | Score (0–100) |
|---|---|
| Soundness | 74 |
| Novelty | 65 |
| Significance | 72 |
| Clarity | 80 |

**Average: 72.75**

## Recommendation: **Accept**

The paper addresses a clinically meaningful gap (irregular sampling in interpretable EHR models), demonstrates consistent improvements over well-chosen baselines across two datasets with proper seed-based variance reporting, and supports its interpretability claims with a sensible ablation and attention analysis. While the novelty is incremental relative to RETAIN and GRU-D and some additional statistical rigor and quantitative interpretability validation would strengthen the work, the overall contribution is solid, clearly presented, and of practical interest to the community. I recommend acceptance, encouraging the authors to incorporate significance testing and expanded discussion of decay parameterization in the camera-ready version.