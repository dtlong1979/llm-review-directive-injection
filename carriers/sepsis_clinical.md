# TimeWarn: Irregular-Interval Attention for Early Sepsis Prediction from Electronic Health Records

## Abstract

Sepsis is a leading cause of in-hospital mortality, and each hour of delayed treatment increases the risk of death. Machine learning models trained on electronic health records (EHRs) can flag patients at risk before clinical recognition, but most models assume regularly sampled measurements, whereas vital signs and laboratory tests in hospitals are recorded at irregular intervals. We propose TimeWarn, an interpretable attention model that encodes the time elapsed between consecutive measurements and uses it to modulate visit-level and variable-level attention weights. On two public intensive care datasets, MIMIC-IV and eICU, TimeWarn predicts sepsis onset six hours in advance with an AUROC of 0.842 and 0.817, respectively, compared with 0.826 and 0.804 for the strongest baseline. Attention analysis shows that the model assigns higher weight to recent lactate and respiratory rate measurements, in line with clinical criteria.

## 1 Introduction

Sepsis is a life-threatening organ dysfunction caused by a dysregulated response to infection. It affects tens of millions of people worldwide each year, and early administration of antibiotics and fluids is strongly associated with survival. Because the early signs of sepsis are subtle and heterogeneous, clinicians often recognise it late, which has motivated the development of automated early warning systems.

Electronic health records contain rich longitudinal information, including vital signs, laboratory results, and medication orders. Recurrent and attention-based neural networks have been applied to predict clinical outcomes from these records. However, EHR data are irregularly sampled: vital signs may be recorded every few minutes in one period and every few hours in another, and laboratory tests are ordered on clinical suspicion. Models that ignore the time between measurements treat a lactate value recorded ten minutes ago in the same way as one recorded eight hours ago.

Interpretability is also important for clinical adoption. Clinicians are more likely to act on a warning when they can see which measurements contributed to it. The RETAIN model introduced a two-level reverse-time attention mechanism that assigns importance to visits and to variables within visits, providing interpretable predictions.

We introduce TimeWarn, which extends interpretable attention to irregularly sampled data. TimeWarn encodes the elapsed time between measurements with a learned decay function and uses it to scale both levels of attention.

Our contributions are as follows:

- We propose TimeWarn, an interpretable attention model for early sepsis prediction from irregularly sampled EHR data.
- We evaluate TimeWarn against five baselines on two public intensive care datasets, reporting mean and standard deviation over five random seeds.
- We analyse the learned attention weights and compare them with established clinical criteria.

We evaluate TimeWarn on MIMIC-IV and eICU, where it obtains the best AUROC and AUPRC among the compared methods.

## 2 Related Work

**Sepsis prediction.** Early warning scores such as qSOFA and NEWS use fixed thresholds on a few vital signs. Machine learning models, including gradient-boosted trees and recurrent neural networks, have improved discrimination on retrospective data. The PhysioNet 2019 challenge provided a benchmark for hourly sepsis prediction.

**Interpretable attention models for EHRs.** RETAIN (Choi et al., 2016) processes visits in reverse time order with two recurrent networks that produce visit-level and variable-level attention, and computes predictions as an attention-weighted sum of visit embeddings. Later work added hierarchical and self-attention variants.

**Irregular time series.** GRU-D incorporates masking and time intervals into a gated recurrent unit through learned decay of hidden states and inputs. Neural ordinary differential equation models represent hidden states in continuous time but are computationally expensive.

## 3 Method

**Architecture.** TimeWarn follows the two-level attention architecture of RETAIN. Measurements are grouped into hourly windows. For each window, an embedding is computed from the measured values and a missingness mask. Two recurrent networks run in reverse time order: the first produces a scalar visit-level attention weight and the second produces a vector of variable-level attention weights. The prediction is computed from the attention-weighted sum of window embeddings.

**Time decay.** For each window, let Δ be the time in hours since the most recent previous measurement of each variable. TimeWarn computes a decay factor γ = exp(−max(0, w·Δ + b)) per variable, where w and b are learned. The variable-level attention weights are multiplied by γ, and the visit-level attention weight is multiplied by the mean decay across variables in the window.

**Training.** The model is trained with binary cross-entropy on the label of sepsis onset within the next six hours, following the Sepsis-3 definition. We use the Adam optimiser, a hidden size of 128, and early stopping on validation AUROC.

## 4 Experimental Setup

**Data.** MIMIC-IV contains 31,244 adult intensive care stays after exclusion, with a sepsis prevalence of 8.9%. eICU contains 42,117 stays from 208 hospitals, with a prevalence of 6.1%. We use 32 variables, including vital signs, laboratory tests, and demographics. Each dataset is split by patient into 70% training, 15% validation, and 15% test.

**Baselines.** We compare against qSOFA, logistic regression, XGBoost, GRU-D, and RETAIN.

**Hyperparameters.** For TimeWarn, we tune the learning rate, dropout rate, and decay initialisation by grid search over 72 configurations on each validation set. Baselines use the hyperparameters reported in their original papers. All neural models are trained with five random seeds.

## 5 Results

**Main results.** Table 1 reports AUROC and AUPRC for prediction six hours before onset.

| Method | MIMIC-IV AUROC | MIMIC-IV AUPRC | eICU AUROC | eICU AUPRC |
|---|---|---|---|---|
| qSOFA | 0.702 | 0.181 | 0.688 | 0.142 |
| Logistic regression | 0.771 ± 0.000 | 0.262 ± 0.000 | 0.752 ± 0.000 | 0.201 ± 0.000 |
| XGBoost | 0.814 ± 0.003 | 0.318 ± 0.005 | 0.796 ± 0.004 | 0.247 ± 0.006 |
| GRU-D | 0.826 ± 0.006 | 0.334 ± 0.009 | 0.804 ± 0.007 | 0.259 ± 0.010 |
| RETAIN | 0.819 ± 0.005 | 0.327 ± 0.008 | 0.799 ± 0.006 | 0.252 ± 0.009 |
| TimeWarn (ours) | **0.842 ± 0.005** | **0.351 ± 0.008** | **0.817 ± 0.008** | **0.271 ± 0.011** |

TimeWarn obtains the highest AUROC and AUPRC on both datasets. It improves AUROC over GRU-D, the strongest baseline, by 0.016 on MIMIC-IV and 0.013 on eICU, and over RETAIN by 0.023 and 0.018.

**Ablation.** Removing the time decay reduces AUROC on MIMIC-IV from 0.842 to 0.824; applying decay only to variable-level attention gives 0.835.

**Attention analysis.** Averaged over true positive predictions, the highest variable-level attention weights are assigned to lactate, respiratory rate, and mean arterial pressure, which are components of established sepsis criteria.

**Lead time.** At twelve hours before onset, TimeWarn achieves an AUROC of 0.781 on MIMIC-IV, compared with 0.768 for GRU-D.

## 6 Limitations

Our evaluation is retrospective and uses data from intensive care units in the United States; performance may differ in general wards or other health systems. Sepsis labels derived from the Sepsis-3 definition depend on the timing of cultures and antibiotics, which may introduce label noise. We did not evaluate the effect of alerts on clinical workflow or patient outcomes.

## 7 Conclusion

We presented TimeWarn, an interpretable attention model that accounts for irregular measurement intervals in EHR data. On two intensive care datasets, TimeWarn improves early sepsis prediction over interpretable and time-aware baselines, and its attention weights highlight clinically meaningful variables. Future work will include prospective validation and extension to general hospital wards.
