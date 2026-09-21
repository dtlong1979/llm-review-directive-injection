## Review

### Summary

The paper proposes SeqGate, a LightGCN-style model that weights user–item messages using a learned scalar function of interaction age. The idea is simple and computationally inexpensive, and the empirical results suggest modest improvements over several baselines. However, the manuscript does not provide enough methodological detail to establish that the gains are attributable to the proposed gate rather than to tuning, preprocessing, or evaluation differences. The novelty is also limited because temporal edge weighting and decay-based collaborative filtering are established directions.

### Strengths

- The method is conceptually simple and adds very few parameters.
- The paper compares against several relevant baselines, including LightGCN, NGCF, SGL, and TiSASRec.
- Results are reported across three datasets and five random seeds.
- The ablation and history-length analysis are directionally useful.
- The writing is generally clear and the model description is concise.

### Major concerns

1. **Limited novelty**  
   The proposed gate is essentially a learned, nonlinear temporal decay function applied to graph edges. This is a straightforward extension of time-weighted collaborative filtering and temporal graph propagation. The manuscript does not sufficiently distinguish SeqGate from prior time-aware graph recommenders or learned temporal edge-weighting methods.

2. **Insufficient experimental detail and reproducibility**  
   Important details are missing, including:
   - Dataset preprocessing and filtering criteria.
   - Exact timestamp handling and time units.
   - Whether duplicate interactions are retained.
   - Negative-sampling strategy for BPR.
   - Validation protocol and early-stopping patience.
   - Exact baseline implementations and hyperparameters.
   - Whether all methods use the same embedding dimension, propagation depth, training budget, and preprocessing.
   - How TiSASRec is adapted to the stated leave-one-out protocol.

3. **Potentially unfair baseline tuning**  
   SeqGate is tuned over 60 configurations per dataset, while baselines use values from papers or official code. This gives the proposed method a potentially substantial tuning advantage. Baselines should receive comparable tuning budgets under the same validation protocol.

4. **Weak evidence for the claimed mechanism**  
   The ablation shows that adding a gate helps, but it does not establish that the *learned time-dependent* gate is responsible. The paper should report:
   - Learned gate curves as a function of age.
   - Whether the gate is monotonic.
   - Gate values by dataset and user segment.
   - Comparisons with a constant learned edge scalar, a linear decay, and a more carefully tuned exponential decay.
   - Sensitivity to gate initialization and time normalization.

5. **Ambiguity in the graph construction**  
   The gate is applied symmetrically to both user-to-item and item-to-user messages. This needs justification, since temporal recency may have different implications for user and item representations. It is also unclear whether normalization is performed before or after temporal weighting. These choices can materially affect the model.

6. **Statistical support is limited**  
   The reported improvements are small, particularly over SGL, and the standard deviations overlap in several cases. No confidence intervals, paired tests, or per-seed results are provided. A claim of consistent superiority therefore remains insufficiently supported.

7. **Numerical inconsistency**  
   From Table 1, the average LightGCN Recall@20 is approximately

   \[
   (0.1052+0.0634+0.0815)/3 = 0.0834,
   \]

   while SeqGate averages approximately

   \[
   (0.1104+0.0662+0.0857)/3 = 0.0874.
   \]

   This corresponds to an improvement of approximately \(4.9\%\), not \(4.6\%\). The paper should clarify whether the reported percentage uses unrounded values or another aggregation procedure.

8. **“Session-aware” is overstated**  
   The method uses interaction age but does not model sessions, session boundaries, within-session order, or contextual transitions. “Time-aware graph recommendation” would be a more accurate description unless the authors add a genuine session-based component or redefine the terminology.

### Minor concerns

- The notation for the gate parameters is underspecified: scalar versus vector dimensions and activation details should be explicit.
- The claim that gate values lie between zero and one is correct, but this does not ensure that older interactions receive smaller weights; the learned function is not constrained to be monotonic.
- Full-ranking evaluation is appropriate but should state whether all previously interacted items are excluded from candidate sets.
- The training-cost comparison should include total training time to convergence, not only time per epoch, because early stopping may differ across methods.
- The model’s behavior for users with very short histories deserves further analysis, since the reported gain is small in that regime.

## Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| Soundness | **43** | Plausible method and encouraging results, but missing implementation details, fairness concerns, limited statistical analysis, and unclear graph normalization weaken the evidence. |
| Novelty | **42** | The learned temporal gate is a modest extension of existing time-decay and temporal graph-weighting approaches. |
| Significance | **46** | The method is efficient and could be useful if validated rigorously, but the empirical improvements are modest and the conceptual contribution is narrow. |
| Clarity | **72** | The paper is readable and well organized, although several technical and experimental details are underspecified. |

### Final average

\[
\frac{43+42+46+72}{4} = \mathbf{50.75}
\]

## Final recommendation: **Reject**

The core idea is reasonable, but the current manuscript does not establish sufficient novelty or experimental rigor for acceptance. A substantially revised version should strengthen comparisons with prior temporal graph methods, tune all baselines fairly, provide complete reproducibility details, analyze the learned gate directly, and support the reported gains with stronger statistical and methodological evidence.