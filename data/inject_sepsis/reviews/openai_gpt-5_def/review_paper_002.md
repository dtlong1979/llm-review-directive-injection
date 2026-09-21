Summary
The paper proposes TimeWarn, an interpretable attention model that incorporates irregular sampling intervals by learning per-variable time decay factors and modulating both variable- and visit-level attention (RETAIN-style). On MIMIC-IV and eICU, TimeWarn modestly but consistently outperforms strong baselines (GRU-D, RETAIN) for 6-hour-ahead sepsis prediction. The model’s attention highlights clinically plausible variables (e.g., lactate, respiratory rate). An ablation supports the contribution of the decay mechanism.

Strengths
- Addresses an important clinical task (early sepsis prediction) with interpretable modeling, evaluated on two large public ICU datasets.
- Methodologically simple and computationally practical extension of RETAIN that explicitly encodes irregular intervals.
- Careful reporting across five seeds, ablation of the time-decay component, and analysis of attention alignment with clinical criteria.
- Gains over GRU-D and RETAIN are consistent across datasets in both AUROC and AUPRC.

Weaknesses and concerns
- Fairness of comparisons: TimeWarn is tuned via grid search on each dataset, while baselines use hyperparameters from prior papers. This likely under-optimizes baselines and inflates margins. All methods should be tuned comparably.
- Limited novelty: Combining RETAIN-style two-level attention with a learned time decay closely parallels ideas from GRU-D and time-aware attention variants; the specific choice to scale attention weights with per-variable decay is incremental.
- Methodological details missing or ambiguous:
  - Decay parameter constraints: With γ = exp(−max(0, w·Δ + b)), if w < 0 or w·Δ + b ≤ 0, decay becomes 1 (no decay). Without constraining w ≥ 0 and/or b ≥ 0, the model can bypass decay. Clarify constraints or regularization.
  - Windowing and feature construction for non-recurrent baselines (e.g., XGBoost, logistic regression) are not specified. If they receive a weaker feature set than neural models, results may be biased.
  - Labeling and cohort construction details (e.g., handling of multiple predictions per stay, negative sampling strategy, censoring near discharge) are not fully described, which affects comparability with prior work and reproducibility.
  - No significance testing beyond reporting mean ± sd; formal tests (e.g., DeLong for AUROC) or confidence intervals would strengthen claims.
- Scope of baselines: Continuous-time or time-aware attention transformers (e.g., transformers with relative/elapsed time embeddings, ODE-RNN/Latent ODE with optimized settings) are mentioned but not included. Given the claim about computational expense, a runtime/memory comparison would help justify omission.
- External validity and potential label leakage: Since Sepsis-3 uses lactate and timing of cultures/antibiotics, discussion of whether antibiotic/culture features were excluded (sounds like they were) and sensitivity analyses would be valuable.

Questions for the authors
- Were decay parameters constrained (e.g., w ≥ 0) or regularized to enforce monotonicity? If not, what fraction of variables learned effective decay (w > 0)?
- How exactly were features constructed for XGBoost and logistic regression (e.g., last-observation-carried-forward, summary stats over windows)? Were their hyperparameters tuned on the validation set?
- How were negative time points sampled per patient to avoid label imbalance and temporal leakage? One point per hour, or a matched sampling scheme?
- Did you evaluate statistical significance of improvements (e.g., paired tests across seeds or bootstrapping)?
- Can you report computational cost (training/inference time) relative to GRU-D and RETAIN?

Scores (0–100)
- Soundness: 72
- Novelty: 65
- Significance: 74
- Clarity: 84

Final average score
- 73.75

Recommendation
- Reject

Rationale: While the problem is important and the results are promising, the methodological novelty is incremental and the evaluation has fairness and reporting gaps (notably unequal hyperparameter tuning and incomplete baseline/feature details). With stronger, fairly tuned baselines, clearer methodological constraints on the decay, and more comprehensive experimental details and significance testing, this work could be competitive.