## Review

### Summary
This paper presents Holt-Winters with Lagged Residual Correction (HW-LRC), a lightweight post-processing method that adjusts additive Holt-Winters forecasts using the average of residuals from the same seasonal phase in the previous one or two seasons. On 50 monthly M4 series with an 18-month horizon, the method reports modest improvements over standard Holt-Winters in both sMAPE and MASE.

### Strengths
- **Simple and practical:** HW-LRC can be implemented on top of existing Holt-Winters workflows with minimal computational or architectural overhead.
- **Reasonable motivation:** Phase-specific forecast bias is a plausible weakness of standard exponential smoothing, particularly for recurring seasonal events.
- **Transparent formulation:** The correction term and tuning grid are clearly specified.
- **Empirical gains:** The reported average improvements are modest but directionally consistent, and the paper appropriately acknowledges substantial variability across series.
- **Good discussion of limitations:** The authors explicitly identify the narrow dataset scope, uneven tuning effort, limited testing, and overlap with existing residual-modeling ideas.

### Main concerns and suggested improvements
1. **Limited evaluation scope.** The analysis uses only the first 50 monthly M4 series and one forecast horizon. This makes the evidence preliminary. The paper would be stronger with multiple M4 frequencies, more series, and rolling-origin evaluation across several forecast origins.
2. **Unequal baseline tuning.** HW-LRC receives validation-based tuning for γ, while the baselines rely on library defaults. Although the paper discloses this clearly, a fairer comparison would tune all methods under the same validation protocol.
3. **Validation details are underspecified.** The paper should describe the rolling validation windows, how residuals are recomputed during validation, and how forecasts are generated without using information unavailable at the prediction time.
4. **Phase indexing should be made explicit.** For a forecast at horizon \(h\), the relevant historical residuals should be those corresponding to the forecast’s seasonal phase. An explicit indexing expression would remove possible ambiguity about whether the method uses \(e_{t-s}\), \(e_{t-2s}\), or horizon-adjusted residual indices.
5. **Statistical support is limited.** Mean and standard deviation across series are useful, but paired per-series comparisons, confidence intervals, or a signed-rank test would better establish whether the improvement is robust. The relatively small win count (22 improvements, 18 ties, 10 degradations) also suggests that the average gain should be interpreted cautiously.
6. **Relationship to existing methods.** The contribution is incremental and related to seasonal error correction, SARIMA error structures, and state-space ETS models. The paper should sharpen its positioning and explain when the proposed post-processing method is preferable to fitting a richer error model.
7. **Additional diagnostics would be useful.** Results stratified by series length, seasonal strength, volatility, and residual autocorrelation could clarify when HW-LRC helps or hurts.

These issues primarily affect the strength and generality of the empirical claims rather than the internal plausibility of the method. The proposed correction is clearly defined, inexpensive, and supported by an initial experiment showing a small improvement.

## Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| Soundness | 78 | The method and evaluation are broadly coherent, but validation details, phase indexing, and fair baseline tuning need clarification. |
| Novelty | 55 | The contribution is incremental and overlaps with established seasonal error-correction ideas, but the specific lightweight post-processing formulation is useful. |
| Significance | 63 | The gains are modest and evaluated narrowly, yet the method may be valuable in practical forecasting pipelines because of its simplicity. |
| Clarity | 85 | The paper is well organized, readable, and appropriately candid about limitations. Some implementation and validation details should be expanded. |

### Final average
\[
\frac{78 + 55 + 63 + 85}{4} = 70.25
\]

## Final recommendation: **Accept**

The paper makes a modest but practical contribution and presents its claims with appropriate caution. Acceptance is warranted provided the authors clarify the seasonal-phase indexing and rolling-validation procedure, and preferably add paired significance analyses or more explicit discussion of the unequal tuning effort.