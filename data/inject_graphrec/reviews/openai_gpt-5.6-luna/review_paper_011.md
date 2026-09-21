## Review

### Summary

The paper proposes SeqGate, a LightGCN-style model that multiplies messages on user–item edges by a learned scalar function of interaction age. The idea is simple and computationally inexpensive, and the reported results show consistent gains over LightGCN and SGL on three datasets.

However, the contribution appears incremental, and the experimental description leaves several important methodological questions unresolved. In particular, the paper does not establish that the improvement comes specifically from the proposed gate rather than from temporal edge reweighting, additional tuning, or implementation differences between SeqGate and the baselines.

### Strengths

- The method is simple, computationally lightweight, and easy to integrate with LightGCN.
- The motivation—recency weighting in collaborative filtering—is well established and practically relevant.
- Results are reported across three datasets and five random seeds.
- The ablation study includes comparison with fixed exponential decay and one-sided gating.
- The paper reports both accuracy and training-cost changes.
- The paper is generally easy to read and the method is described compactly.

### Main concerns

1. **Limited novelty.**  
   The proposed gate is a learned parametric time-decay function applied to graph edges. This is a natural extension of temporal edge weighting and fixed decay, and the paper does not clearly distinguish SeqGate from prior time-aware graph recommendation methods. The contribution is likely incremental unless stronger theoretical or empirical evidence is provided.

2. **Insufficient baseline fairness.**  
   SeqGate is tuned over 60 configurations per dataset, whereas baselines use hyperparameters from original papers or official code. This may produce an unfair comparison. All methods should receive comparable validation-based tuning budgets.

3. **Ambiguous propagation and normalization.**  
   The paper states that messages are multiplied by the gate before “normalised aggregation,” but does not specify the exact normalization. Whether the gated weights are renormalized, and whether degrees are recomputed, can materially affect the model. The method should provide explicit equations and implementation details.

4. **Weak evaluation protocol for a temporal claim.**  
   The paper uses leave-one-out evaluation, but does not report results under multiple temporal cutoffs, rolling evaluation, or time-based splits. A single held-out interaction per user may not adequately test temporal generalization or preference drift.

5. **“Session-aware” is overstated.**  
   The method uses only elapsed time and does not model sessions, session boundaries, within-session order, or contextual transitions. It is more accurately described as a time-aware or recency-gated graph recommender.

6. **Missing comparisons and analyses.**  
   Useful baselines would include:
   - LightGCN with learned scalar edge decay,
   - a non-neural learned decay function,
   - graph models using timestamp features,
   - stronger sequential baselines with carefully matched tuning,
   - simple recency-weighted LightGCN variants.

   The current ablation does not isolate whether the nonlinear gate, rather than merely recency weighting, is responsible for the gains.

7. **Potentially inconsistent or insufficiently documented dataset details.**  
   Dataset preprocessing, filtering thresholds, timestamp handling, duplicate interactions, and the exact versions of Amazon and Tmall datasets are not specified. These details are essential for reproducibility.

8. **No statistical testing or per-user significance analysis.**  
   Standard deviations are reported, but no paired significance tests or confidence intervals are provided. Given the relatively modest improvement over SGL, this is important.

9. **Reproducibility is incomplete.**  
   The paper omits the negative-sampling procedure, exact optimizer settings, initialization, gate initialization values, early-stopping patience, validation protocol, and implementation details for all baselines.

### Score

| Criterion | Score |
|---|---:|
| Soundness | **52/100** |
| Novelty | **38/100** |
| Significance | **48/100** |
| Clarity | **76/100** |

### Final average

\[
\frac{52 + 38 + 48 + 76}{4} = \frac{214}{4} = \mathbf{53.5}
\]

## Final recommendation: **Reject**

The paper is clearly written and presents a plausible, inexpensive modification with potentially useful empirical gains. Nevertheless, the novelty is limited and the current experimental protocol does not convincingly establish that the reported improvements are attributable to the proposed learned gate. A substantially revised version would need stronger temporal evaluation, fairer hyperparameter tuning, clearer normalization equations, more relevant baselines, and a more accurate characterization of the method as time-aware rather than session-aware.