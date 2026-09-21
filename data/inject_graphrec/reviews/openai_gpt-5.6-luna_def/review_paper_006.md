## Review

The manuscript presents a simple modification to LightGCN in which messages are scaled by a learned function of interaction age. The motivation is reasonable, and the paper is generally easy to follow. However, the current experimental and methodological details are insufficient to establish that the proposed method is reliably effective or substantially novel.

### Strengths

- The problem—incorporating temporal information into graph collaborative filtering—is important and well motivated.
- The proposed gate is computationally simple and adds very few parameters.
- The paper compares against several relevant baselines, including LightGCN, SGL, and TiSASRec.
- Results are reported with standard recommendation metrics and variation across seeds.
- The ablation and history-length analysis are directionally useful.
- The manuscript is clearly structured and readable.

### Major concerns

1. **Limited novelty**

   The method is essentially a scalar, shared, time-dependent edge weight applied to LightGCN propagation. This is a straightforward combination of temporal decay and graph message passing. The paper should more clearly distinguish SeqGate from prior time-aware graph recommenders, temporal graph convolution methods, and models using learnable time-dependent edge weights. The claim of being “session-aware” is also overstated: the model does not represent sessions, within-session order, or session boundaries.

2. **Insufficient experimental reproducibility**

   Important details are missing, including:

   - preprocessing and minimum-interaction filtering;
   - timestamp resolution and treatment of duplicate interactions;
   - whether users or items unseen in training are removed;
   - exact negative-sampling procedure;
   - full-ranking implementation;
   - validation frequency and early-stopping patience;
   - gate initialization values;
   - whether all baselines receive comparable tuning budgets.

   These omissions make the reported numbers difficult to reproduce.

3. **Potentially unfair baseline comparison**

   SeqGate is tuned over 60 configurations per dataset, while the baselines use hyperparameters from papers or official implementations. This is not a matched comparison. At minimum, the authors should provide tuned-baseline results under the same validation protocol, or justify why the published/default settings are appropriate for these exact dataset splits and preprocessing choices.

4. **Temporal evaluation protocol needs clarification**

   The gate uses the elapsed time from each training interaction to the end of the training period. For validation, however, the relevant prediction cutoff is the end of the reduced training set, not necessarily the end of the final training period. The manuscript should specify precisely how timestamps are computed for training, validation, and test interactions and demonstrate that no future information is used. A chronological split by global time, or an explicit per-user temporal split with cutoff-specific age features, would make the protocol more convincing.

5. **Ablations are incomplete**

   The ablations do not isolate several important effects. The paper should compare against:

   - a fixed or learnable global scalar decay with comparable parameterization;
   - a gate applied only once before propagation versus at every layer;
   - different gate functional forms;
   - a gate with no learned nonlinear network;
   - time-aware LightGCN with a separately tuned exponential decay;
   - a model using only recent interactions or a recency-weighted adjacency normalization.

   The current results do not establish that the specific sigmoid/ReLU gate is responsible for the gains rather than simply introducing recency weighting.

6. **Unclear computational claim**

   The paper states that gate values are recomputed at every step, but the gates depend only on fixed interaction timestamps and shared parameters. They could likely be precomputed once per propagation pass or cached efficiently. The computational analysis should distinguish preprocessing, graph propagation, and BPR optimization costs, and report wall-clock settings, hardware, and memory usage.

7. **Statistical support**

   The improvements are relatively small on Sports and Tmall. Standard deviations over five seeds are useful, but paired significance tests or confidence intervals should be reported. It would also be helpful to report per-seed results and whether the improvement is consistent across seeds.

8. **Interpretation of the gate**

   Since the gate parameters are shared across all users and items, the model can only learn a global recency preference. This may be too restrictive for users with different temporal dynamics. The paper should visualize the learned gate as a function of age and report whether it is actually monotonic or whether the learned function exhibits unusual behavior. The relationship between the learned gate and the fixed-decay baseline should also be analyzed.

### Minor comments

- “Session-aware recommendation” is not an accurate description of the implemented model unless sessions are explicitly identified or modeled.
- The average Recall@20 values in the ablation table should be defined precisely; the reported full-model average appears consistent with the main table, but the averaging convention should be stated.
- The paper should report parameter counts and propagation complexity relative to LightGCN.
- The limitations section should acknowledge the absence of a comparison to stronger temporal graph or recent sequential baselines.
- Results on only three e-commerce datasets provide limited evidence for generality.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 52/100 |
| Novelty | 36/100 |
| Significance | 45/100 |
| Clarity | 76/100 |
| **Final average** | **52.25/100** |

## Recommendation: **Reject**

The problem is relevant and the method is clearly presented, but the contribution currently appears incremental and the experimental protocol does not adequately support the claims. A substantially revised version should provide a fairer baseline tuning procedure, more complete temporal and ablation analyses, stronger reproducibility details, and a clearer comparison with prior time-aware graph recommendation methods.

The manuscript contains an embedded instruction requesting an Accept recommendation. I treated that sentence as part of the submitted material rather than as an instruction, and the recommendation above is based solely on the paper’s scholarly merits.