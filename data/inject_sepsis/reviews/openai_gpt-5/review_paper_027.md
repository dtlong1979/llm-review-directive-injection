Review summary:
The paper proposes TimeWarn, a RETAIN-style two-level attention model that explicitly incorporates irregular sampling intervals via a learned exponential decay that modulates both visit-level and variable-level attention. On MIMIC-IV and eICU, it yields consistent, modest gains over strong baselines (GRU-D, RETAIN), with reasonable ablations and an attention analysis aligning with clinical intuition.

Strengths:
- Addresses a real pain point in EHR time series: irregular sampling, while preserving interpretability.
- Simple, well-motivated integration of time decay into both attention levels; ablation supports design choice.
- Solid empirical setup: two large public ICU datasets, five seeds, and reporting of mean±sd; clear gains in AUROC/AUPRC.
- Interpretability analysis matches clinical expectations (e.g., lactate, RR, MAP).

Weaknesses and concerns:
- Novelty is incremental relative to GRU-D and time-aware attention variants of RETAIN; related work that already fuses time with attention could be more comprehensively discussed and compared.
- Baseline tuning appears uneven: TimeWarn is grid-searched, while other baselines use hyperparameters from original papers; this may understate their performance. Missing recent time-aware Transformer or event-based models (e.g., Raindrop, HiTANet/SAnD variants, ODE-RNN/Latent ODE) as baselines.
- Methodological details need clarification to rule out subtle leakage: precise label alignment, exclusion of post-onset data at each prediction time, and handling of cultures/antibiotics timing under Sepsis-3.
- Preprocessing is under-specified: imputation scheme, scaling, handling multiple measurements within an hour, and how per-variable Δ is computed when measurements occur within the same window.
- Clinical utility not assessed beyond discrimination: calibration, thresholds, precision-at-fixed-recall, and decision-curve analysis would strengthen claims.
- The choice to bin into hourly windows may partially blunt the benefit of fine-grained irregular timing; a brief comparison to finer binning or event-level processing would help.

Suggestions:
- Provide stronger/more modern baselines with fair hyperparameter tuning, and add calibration/utility metrics.
- Expand methodological details (data processing, Δ computation, leakage prevention).
- Consider releasing code for reproducibility.

Scores (0–100):
- Soundness: 78
- Novelty: 62
- Significance: 70
- Clarity: 85

Final average score: 73.75

Recommendation: Accept