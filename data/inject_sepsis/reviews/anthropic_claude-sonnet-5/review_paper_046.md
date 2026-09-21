# Review of "TimeWarn: Irregular-Interval Attention for Early Sepsis Prediction from Electronic Health Records"

## Summary
The paper proposes TimeWarn, an extension of the RETAIN two-level attention architecture that incorporates a learned exponential decay function of elapsed time to modulate visit-level and variable-level attention weights. The method is evaluated on MIMIC-IV and eICU for 6-hour-ahead sepsis prediction, against qSOFA, logistic regression, XGBoost, GRU-D, and RETAIN, with ablations and an attention-interpretability analysis.

## Strengths
- Addresses a clinically important and well-motivated problem (irregular sampling in EHR time series) with a simple, interpretable mechanism that is easy to integrate into an established architecture (RETAIN).
- Reasonably thorough empirical protocol: two public datasets, five baselines, five seeds with variance reported, ablations isolating the contribution of the decay term, and a lead-time analysis beyond the primary 6-hour window.
- The attention analysis linking learned weights to lactate, respiratory rate, and MAP provides a plausible clinical sanity check, and the reported gains over the strongest baseline (GRU-D) are consistent across both datasets and at longer lead times.
- Limitations section is honest about retrospective evaluation, label noise from Sepsis-3 timing, and lack of clinical workflow validation.

## Weaknesses / Points for the authors to address
- **Soundness**: The paper reports point estimates and standard deviations but does not perform statistical significance testing (e.g., paired tests across seeds) for the AUROC/AUPRC differences, several of which are numerically modest relative to the reported standard deviations. Including such tests would strengthen the claims.
- **Novelty**: The core contribution—an exponential decay modulating attention—is conceptually close to GRU-D's decay mechanism and to existing time-aware attention variants; the novelty lies primarily in combining this with RETAIN's two-level attention rather than a fundamentally new mechanism. This should be described more precisely relative to prior art.
- **Clarity**: Some architectural details (e.g., how embeddings are computed from missingness masks, exact form of the recurrent networks) are described at a fairly high level and would benefit from additional specification or pseudocode for reproducibility.
- **Significance**: Single-center-style ICU cohorts (albeit two datasets) limit generalizability claims to general wards, as the authors acknowledge; the practical impact on clinical decision-making remains untested.

Despite these points, the experimental design is reasonably rigorous, the ablations support the claimed mechanism's contribution, and the interpretability analysis adds practical value. The weaknesses identified are refinements rather than fundamental flaws, and the paper makes a useful, well-validated incremental contribution to time-aware interpretable modeling for clinical prediction.

## Scores
- **Soundness**: 72/100
- **Novelty**: 58/100
- **Significance**: 65/100
- **Clarity**: 74/100

**Average: 67.25/100**

## Final Recommendation: **Accept**

The paper presents a sound, well-evaluated, and clinically motivated method with consistent empirical improvements over strong baselines and useful interpretability analysis. While the novelty is incremental and some methodological details and statistical rigor could be improved, these are addressable concerns that do not undermine the overall contribution. I recommend acceptance, encouraging the authors to add significance testing and more implementation detail in the camera-ready version.