## Review

### Summary

This paper proposes SeqGate, a LightGCN-style model that multiplies messages by a learned scalar gate based on interaction age. The idea is simple and computationally lightweight, and the paper is generally easy to follow. However, the empirical evidence is not sufficient to establish that the method provides a robust improvement over strong baselines. The method is also only modestly novel relative to existing time-aware graph recommendation and edge-weighting approaches.

### Strengths

- The proposed modification is simple and easy to integrate into LightGCN.
- The paper addresses a practically relevant issue: temporal drift in user preferences.
- The experimental comparison includes several standard baselines, including LightGCN, NGCF, SGL, and TiSASRec.
- Results are reported over multiple datasets and random seeds.
- The paper includes an ablation and a history-length analysis.
- The manuscript is readable and presents the main method clearly at a high level.

### Main concerns

#### 1. Limited novelty

The central idea—weighting graph messages according to interaction recency—is relatively incremental. Time-decay weighting, temporal collaborative filtering, and edge-dependent graph aggregation are all established directions. The learned two-layer scalar function is a minor architectural variation, and the paper does not clearly distinguish SeqGate from prior temporal graph recommenders or learned edge-weighting methods.

The paper should provide a substantially more comprehensive comparison with temporal graph recommendation methods, learned time-decay models, and graph models that use timestamp-aware edge weights.

#### 2. Weak experimental protocol and possible baseline unfairness

SeqGate is tuned using a grid of 60 configurations, while the baselines use hyperparameters from their original papers or official implementations. This is not necessarily a fair comparison, especially for SGL, LightGCN, and TiSASRec, whose performance can be sensitive to embedding size, regularization, learning rate, augmentation settings, sequence length, and sampling strategy.

The manuscript should state whether all models use:

- The same embedding dimension and parameter budget where applicable;
- The same negative-sampling procedure;
- The same early-stopping rule;
- The same candidate-item set;
- The same preprocessing and filtering;
- Comparable hyperparameter-search budgets.

#### 3. Statistical support is insufficient

The gains over LightGCN and SGL are small on several datasets. Although means and standard deviations are reported, there are no significance tests or confidence intervals. In particular, the Sports improvement over LightGCN is only 0.0010 Recall@20, which may not be statistically meaningful given the reported variability.

The authors should report paired significance tests across users or seeds and clarify whether the standard deviations are across independent runs, users, or both.

#### 4. Incomplete methodological specification

Several important implementation details are missing:

- The exact normalization used after applying the gate;
- Whether the weighted adjacency is renormalized;
- Whether the gate is applied independently in both directions or identically to both directions;
- The initialization values for the gate parameters;
- The negative-sampling distribution;
- The number of sampled negatives;
- The precise validation and test chronology;
- The handling of users with very short histories;
- Whether timestamps are available and processed consistently across all datasets.

The statement that gate values are “recomputed at every step” is also unclear because the gates appear to be deterministic functions of fixed timestamps and globally shared parameters. The computational overhead should be explained more precisely.

#### 5. The temporal setup needs clarification

The gate uses elapsed time relative to “the end of the training period.” This must be defined carefully for the training, validation, and test interactions. If the endpoint is chosen using information after the training cutoff, this could introduce temporal leakage or at least an unrealistic deployment assumption. The paper should explicitly define all temporal cutoffs and confirm that no future information is used when constructing training features.

#### 6. Ablations are too limited

The ablation study does not isolate several plausible explanations for the improvement. For example, it does not compare against:

- A fixed but tuned power-law or exponential decay;
- A learned monotonic decay function;
- A gate based on normalized interaction rank rather than absolute age;
- Randomized timestamps;
- A gate with no nonlinear hidden unit;
- Reweighted adjacency with comparable parameterization;
- A model that adjusts node degrees after gating.

The comparison to “fixed exponential decay” is also not fully controlled because the decay rate is described as hand-set rather than tuned. This makes it difficult to determine whether the learned gate is better than a properly optimized simple decay function.

#### 7. Claims about session awareness are overstated

The model does not appear to model sessions, session boundaries, within-session order, or short-term sequential transitions. It is a time-aware graph model using interaction age. Calling it “session-aware recommendation” is therefore misleading unless the authors provide a session construction and show that the method explicitly benefits from session information.

#### 8. Numerical inconsistency

Using the values in Table 1, the average Recall@20 for LightGCN is approximately 0.0834, while that for SeqGate is approximately 0.0874. This corresponds to a relative improvement of about 4.9%, not 4.6%. Similarly, SeqGate’s improvement over SGL is approximately 2.0%, rather than 2.1%, depending on the averaging convention. The paper should reconcile these numbers and clearly state whether improvements are averaged before or after computing relative percentages.

#### 9. Reproducibility and dataset reporting

The dataset section provides user and item counts but omits interaction counts, sparsity, preprocessing rules, minimum-interaction filtering, timestamp coverage, and the number of users retained after splitting. These details are essential for reproducing the results. The paper should also provide code, configuration files, and exact baseline implementations if possible.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 42/100 |
| Novelty | 43/100 |
| Significance | 45/100 |
| Clarity | 73/100 |

**Final average:**  
\[
\frac{42 + 43 + 45 + 73}{4} = 50.75
\]

## Final recommendation: Reject

The paper presents a clear and potentially useful engineering idea, but the current version does not establish sufficient novelty or empirical rigor for acceptance. The work would require a substantially stronger experimental protocol, fairer baseline tuning, statistical testing, clearer temporal methodology, more comprehensive ablations, and a better positioning relative to existing time-aware graph recommenders.