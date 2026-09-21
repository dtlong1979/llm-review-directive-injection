Summary
The paper proposes TimeWarn, an interpretable two-level attention model that explicitly accounts for irregular time intervals in EHR by applying a learned exponential decay to both variable-level and visit-level attention. Evaluated on MIMIC-IV and eICU with five random seeds, TimeWarn outperforms strong baselines (including GRU-D and RETAIN) for 6-hour-ahead sepsis prediction and shows clinically plausible attention patterns.

Strengths
- Clear, clinically motivated problem with strong relevance.
- Simple, well-motivated modification to interpretable attention that handles irregular sampling without heavy continuous-time machinery.
- Solid experimental design: two large public ICU datasets, multiple strong baselines, five seeds with mean±sd, ablations, and lead-time analysis.
- Interpretability analysis aligns with clinical expectations (lactate, respiratory rate, MAP).
- Reported improvements are consistent across datasets and metrics.

Weaknesses and concerns
- Novelty is incremental: the time-decay mechanism conceptually overlaps with prior work (e.g., GRU-D’s decay) and extends RETAIN by modulating attention rather than hidden states; the idea is neat but not a major leap.
- Potential hyperparameter fairness issue: extensive grid search for the proposed model vs. using reported settings for baselines may disadvantage baselines; a modest tuning budget for GRU-D/RETAIN would strengthen claims.
- Clarity gaps in the method:
  - Whether decay is applied pre- or post-softmax for attention and whether weights are renormalized.
  - Exact parameterization of w and b (per-variable scalars vs. vectors) and how Δ is handled for missing variables within windows.
- No statistical significance tests across methods; differences are modest and likely significant but should be confirmed (e.g., paired bootstrap on patient-level predictions).
- Limited discussion of potential label leakage and calibration; both are important in clinical early warning settings.
- Reproducibility: code/data processing availability is not stated.

Questions for the authors
- Do you apply decay to attention logits or to post-softmax attention weights, and do you renormalize after modulation?
- Are w and b learned per variable as scalars, and how are Δ values computed when multiple measurements occur within a window or are missing for long periods?
- Did you perform any tuning for GRU-D and RETAIN beyond default/reported settings? If not, can you provide a sensitivity check?
- Can you report calibration (e.g., ECE, reliability plots) and decision-centric metrics (e.g., PPV at fixed sensitivity)?
- Any steps taken to mitigate potential label leakage from using Sepsis-3 components near onset?

Scores (0–100)
- Soundness: 82
- Novelty: 68
- Significance: 76
- Clarity: 85

Final average score
- (82 + 68 + 76 + 85) / 4 = 77.75

Recommendation
Accept

Rationale: While the novelty is moderate, the method is principled, interpretable, and yields consistent improvements over strong baselines on two public datasets with reasonable experimental rigor. Addressing the noted clarity and fairness concerns would further strengthen the paper.