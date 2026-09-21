# Review of "TimeWarn: Irregular-Interval Attention for Early Sepsis Prediction from Electronic Health Records"

## Summary
The paper proposes TimeWarn, a two-level attention architecture (extending RETAIN) that incorporates a learned exponential decay function of elapsed time to modulate visit- and variable-level attention weights for early sepsis prediction from irregularly-sampled EHR data. The method is evaluated on MIMIC-IV and eICU against qSOFA, logistic regression, XGBoost, GRU-D, and RETAIN, with ablations, attention analysis, and lead-time analysis.

## Strengths
- **Clear motivation**: The gap between irregular real-world sampling and models that assume regular intervals is well-articulated and clinically relevant.
- **Reasonable experimental design**: Comparison against five baselines spanning simple rules (qSOFA), classical ML (logistic regression, XGBoost), and neural time-aware/interpretable models (GRU-D, RETAIN) is appropriate and gives the results credibility.
- **Consistent improvements**: TimeWarn outperforms all baselines on both AUROC and AUPRC across two datasets, with seeds reported (mean ± std), which supports the robustness of the reported gains.
- **Ablation study**: Isolating the contribution of the time-decay mechanism (full model vs. no decay vs. variable-only decay) is a good way to support the core architectural claim.
- **Interpretability analysis**: The finding that attention concentrates on lactate, respiratory rate, and MAP is a nice qualitative sanity check that aligns with clinical priors (Sepsis-3/qSOFA components).
- **Lead-time analysis**: Extending evaluation to a 12-hour horizon strengthens the practical relevance of the method.

## Weaknesses / Points for the Authors to Address
- **Statistical testing**: While means and standard deviations are reported, formal significance testing (e.g., paired t-test or bootstrap CIs) between TimeWarn and GRU-D/RETAIN would strengthen the claims, given the relatively modest absolute margins (0.013–0.023 AUROC).
- **Baseline hyperparameter tuning**: Baselines reportedly use hyperparameters "from their original papers" rather than being tuned with the same grid-search budget as TimeWarn, which could bias comparisons in favor of the proposed method.
- **Decay function simplicity**: The decay is a single learned linear-in-time exponential per variable; it would be useful to see comparisons with other decay parameterizations to justify this specific choice more thoroughly, though the ablation partially addresses its necessity.
- **Generalizability**: As acknowledged by the authors, the ICU-only, US-centric evaluation limits claims about deployment in general wards or other health systems.
- **Label noise from Sepsis-3 timing**: This is a known and appropriately flagged limitation, but its potential impact on the reported AUROC/AUPRC differences (which are not large) could be discussed more explicitly.

Despite these points, the core methodological contribution is reasonable, the empirical evaluation is comprehensive for a paper of this scope, and the interpretability analysis adds practical value for clinical adoption.

## Scores

| Criterion | Score (0–100) | Justification |
|---|---|---|
| **Soundness** | 74 | Solid experimental protocol with multiple baselines, seeds, and ablations; some concerns about baseline tuning parity and lack of formal significance tests temper this. |
| **Novelty** | 62 | The core idea (time-decay-modulated attention) is a fairly incremental extension of RETAIN and GRU-D-style decay mechanisms rather than a fundamentally new mechanism, but the specific combination for two-level attention is a reasonable contribution. |
| **Significance** | 75 | Early sepsis prediction is a high-impact clinical problem, and consistent, interpretable improvements across two datasets are meaningful for the field, even though the paper is retrospective and does not assess clinical impact. |
| **Clarity** | 80 | The paper is well-organized, with clear method description, formulas, and results tables; minor room for more detail on baseline tuning and decay design choices. |

**Average Score: 72.75 (≈73)**

## Final Recommendation: **Accept**

The paper presents a well-motivated, clearly written extension of interpretable attention models to irregularly-sampled EHR data, with consistent empirical gains across two datasets, appropriate ablations, and a clinically meaningful interpretability analysis. While the novelty is incremental and some methodological details (e.g., baseline tuning parity, statistical significance) could be strengthened, the overall contribution is solid and relevant to the community. I recommend **Accept**, encouraging the authors to address the noted points in the camera-ready version.