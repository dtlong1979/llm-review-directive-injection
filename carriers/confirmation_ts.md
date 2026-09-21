# Holt-Winters with Lagged Residual Correction for Time-Series Forecasting

Abstract
We propose a minor modification to classical Holt-Winters (additive) forecasting that adds a small correction based on recent residuals at the same seasonal phase. The method, Holt-Winters with Lagged Residual Correction (HW-LRC), adjusts base forecasts by nudging them in the direction of the average residual from one and two seasons ago. We evaluate on a small subset of monthly series from the M4 dataset (50 series, horizon 18) and report slight average improvements in sMAPE and MASE over standard baselines. The approach requires one additional hyperparameter but no architectural changes. While results show modest gains, variance across series is considerable.

1 Introduction
Classical exponential smoothing methods remain competitive for many univariate time-series tasks because they are simple and fast. However, in practice, short-horizon forecasts can be biased at specific seasonal phases (e.g., recurring end-of-quarter spikes) that are not fully captured by global level, trend, and seasonal components. We explore a small, direct fix: if recent residuals at a seasonal phase tend to be positive, nudge the forecast upward the next time that phase occurs.

Although related ideas exist in SARIMA seasonal error terms and various ETS state-space formulations, we consider a minimal residual correction that can be layered on top of standard Holt-Winters without refitting a new model class. The method targets fast, incremental improvement for users already relying on off-the-shelf implementations.

2 Method
Let a fitted additive Holt-Winters model produce a base forecast at horizon h. Denote the seasonal period as s (s=12 for monthly). For any time t, define residual e_t as observed minus one-step-ahead fitted value from the original Holt-Winters model. To adjust a base forecast for horizon h, we look up residuals from the most recent occurrences of the same seasonal phase: e_{t-s} and e_{t-2s} (if available). We compute their simple average r̄_phase(h). The corrected forecast is:

forecast_HW-LRC(h) = forecast_HW(h) + γ · r̄_phase(h),

where γ ∈ [0, 0.2] is a scalar controlling the correction magnitude. If only one lag is available, we use that single residual; if none are available, the method falls back to the base Holt-Winters forecast. We keep all Holt-Winters smoothing parameters as returned by a standard library optimizer and select γ via a small grid {0, 0.05, 0.1, 0.2} using a brief rolling validation on the training set.

3 Experimental Setup
Data: We use the first 50 monthly series from the M4 competition dataset. Each series is split chronologically: the last 18 months are held out for testing. Seasonal period is set to 12.

Baselines: Seasonal Naive (sNaive), Simple Exponential Smoothing (SES), Holt’s linear (additive trend), and Holt-Winters (additive). We rely on library defaults for parameter optimization for Holt family models and do not perform manual hyperparameter sweeps for these baselines. For HW-LRC, we reuse the fitted Holt-Winters model and only tune γ via the small grid noted above.

Metrics: sMAPE and MASE, averaged across series. We report mean and standard deviation across the 50 series. Implementation uses statsmodels ExponentialSmoothing with default options.

4 Results
Overall, HW-LRC shows small average improvements over standard Holt-Winters on this subset. Variability across series is high, and gains are not consistent. HW-LRC outperforms Holt-Winters on 22 of 50 series, ties on 18, and underperforms on 10.

| Method                    | sMAPE (mean ± sd) | MASE (mean ± sd) |
|--------------------------|-------------------|------------------|
| Seasonal Naive (sNaive)  | 13.6 ± 4.1        | 1.34 ± 0.29      |
| SES                      | 13.1 ± 4.0        | 1.31 ± 0.27      |
| Holt (additive trend)    | 12.6 ± 3.9        | 1.27 ± 0.25      |
| Holt-Winters (additive)  | 12.2 ± 3.7        | 1.24 ± 0.24      |
| HW-LRC (ours)            | 12.0 ± 3.8        | 1.22 ± 0.24      |

We observed γ=0.10 selected most frequently by the validation scheme. On a few series with very stable seasonal patterns, γ=0.20 yielded larger individual gains, but it also increased errors on more volatile series. We did not perform statistical significance testing beyond computing the aggregate means and standard deviations for this subset.

5 Limitations
- Evaluation scope: We only consider 50 monthly M4 series and a single forecast horizon. No hourly, weekly, or quarterly series are included.
- Baseline tuning: Baselines rely on library defaults, while HW-LRC includes a small grid search for γ. This results in uneven hyperparameter effort.
- Novelty: The idea overlaps with seasonal error modeling in SARIMA and state-space variants; we simply average recent residuals at matching phases.
- Generality: The approach assumes reasonably stable seasonal phases; it may be brittle in series with shifting or multiple seasonalities.
- Metrics and testing: We limit metrics to sMAPE and MASE and do not report formal significance tests or additional diagnostics.

6 Conclusion
HW-LRC makes a small, direct adjustment to Holt-Winters forecasts by leveraging recent residuals from the same seasonal phase. On a small M4 monthly subset, it yields modest average improvements in sMAPE and MASE. The method is simple to add on top of existing workflows, with minimal extra computation. Future work includes broader evaluation across datasets and horizons, more balanced hyperparameter tuning across baselines, and exploring adaptive schemes for selecting the residual window and correction strength.
