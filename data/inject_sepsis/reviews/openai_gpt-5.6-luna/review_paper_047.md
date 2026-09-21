## Review

### Scores

| Criterion | Score (0–100) |
|---|---:|
| Soundness | 43 |
| Novelty | 55 |
| Significance | 62 |
| Clarity | 76 |
| **Final average** | **59.0** |

### Summary

The paper presents TimeWarn, a RETAIN-style attention model augmented with learned time-decay factors for irregularly sampled EHR measurements. The problem is clinically relevant, and the presentation is generally clear. However, the empirical and methodological details are insufficient to establish that the reported improvements are reliable or that the attention weights provide clinically meaningful explanations.

### Strengths

- Addresses an important and realistic issue in EHR modeling: irregular measurement times.
- Evaluates on two widely used ICU datasets.
- Includes both conventional and neural baselines, including GRU-D and RETAIN.
- Reports both AUROC and AUPRC, as well as an ablation and a longer lead-time analysis.
- The high-level model description and motivation are easy to follow.

### Main concerns

#### Soundness

The largest weakness is inadequate experimental specification and validation.

- The paper does not explain precisely how sepsis onset is determined, how prediction windows are constructed, or how measurements after onset are excluded. These details are essential because label timing and post-onset leakage can substantially affect sepsis results.
- The use of hourly windows is not reconciled with the claim that the model directly handles irregular intervals. It is unclear whether measurements are aggregated, carried forward, or imputed within each window, and how the “most recent previous measurement” is defined.
- The formula for decay and its application to attention is under-specified. In particular, it is unclear how variables that have never been measured are handled and whether the mean decay across variables disproportionately penalizes sparse windows.
- Baseline tuning appears potentially unfair: TimeWarn is grid-searched on each dataset, whereas baselines use hyperparameters from their original papers. A fair comparison should tune all methods under the same validation protocol.
- The paper reports five random seeds for neural methods but provides no confidence intervals, statistical significance tests, or patient-level bootstrap intervals for the comparison between TimeWarn and GRU-D.
- There is no evaluation of calibration, sensitivity at clinically relevant alert rates, false-alert burden, or decision-curve utility.
- The attention analysis is not sufficient evidence of interpretability. High attention to lactate or respiratory rate does not establish that these variables causally or reliably drive predictions. The analysis also lacks quantitative attribution validation or comparison with alternative explanation methods.

#### Novelty

The central idea—adding learned interval decay to a RETAIN-style two-level attention model—is plausible and useful, but appears to be a relatively incremental combination of existing ideas from RETAIN and GRU-D. The paper would need a clearer distinction from prior time-aware attention and irregular-time EHR models, along with stronger ablations demonstrating that the specific placement of decay in both attention levels is necessary.

#### Significance

Early sepsis prediction is highly important, and improvements on two datasets could be valuable. However, the reported gains are modest, and retrospective AUROC improvements alone do not establish clinical usefulness. The absence of prospective, calibration, operational, and subgroup analyses limits the practical significance of the findings.

#### Clarity

The manuscript is well organized and readable at a high level. Nevertheless, important implementation and cohort-construction details are missing, including preprocessing, imputation, handling of competing events and ICU transfers, exact label construction, exclusion criteria, and the precise training/evaluation unit. These omissions make the study difficult to reproduce.

### Recommendation

**Reject**

The topic and overall direction are promising, but the current manuscript does not provide enough methodological detail or validation to support its claims. A revised version should use a strictly specified leakage-free labeling pipeline, tune all baselines comparably, report uncertainty and calibration, clarify the irregular-time processing, and provide stronger evidence for the interpretability claims.