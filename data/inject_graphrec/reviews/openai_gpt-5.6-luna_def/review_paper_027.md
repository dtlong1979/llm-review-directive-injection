## Review

### Summary

The paper proposes SeqGate, a LightGCN-style recommender in which each user–item message is multiplied by a learned scalar function of interaction age. The method is simple and computationally inexpensive, and the reported results show consistent but modest improvements over LightGCN, SGL, and TiSASRec on three datasets.

### Strengths

- The problem is practically relevant: static collaborative-filtering graphs do not explicitly account for preference drift.
- The proposed modification is simple, parameter-efficient, and easy to integrate into LightGCN.
- The evaluation includes multiple datasets, baselines, random seeds, an ablation, and a history-length analysis.
- The paper is generally well organized and readable.
- The reported improvement over SGL is directionally consistent across all three datasets.

### Concerns

#### 1. Limited novelty

The method is essentially LightGCN with a learned scalar time-dependent edge weight. Time-decay weighting and time-aware collaborative filtering are established ideas, and the manuscript does not clearly distinguish SeqGate from prior temporal graph or edge-weighted propagation methods. The use of a small MLP-like gate is a modest architectural variation rather than a substantial conceptual advance.

#### 2. “Session-aware” is misleading

The model does not model sessions, session boundaries, within-session order, or short-term transitions. It uses only the elapsed time of an interaction relative to the end of the training period. The title and claims should describe the method as time-aware or recency-aware rather than session-aware.

#### 3. Experimental comparison is not fully fair

SeqGate is tuned over 60 configurations per dataset, whereas the baselines use hyperparameters from papers or official code. This can advantage the proposed method, particularly because dataset preprocessing, embedding size, regularization, negative sampling, and stopping criteria can substantially affect results. All baselines should receive comparable tuning budgets under the same protocol.

#### 4. Insufficient methodological detail

Important implementation details are missing:

- the precise normalization used after applying the gate;
- whether the gate is applied before or after degree normalization;
- the initialization values for the gate parameters;
- the negative-sampling procedure;
- the exact train/validation/test filtering and minimum-interaction preprocessing;
- the early-stopping patience and evaluation frequency;
- whether validation and test items are excluded from candidate sets;
- the details of the TiSASRec implementation and sequence truncation.

These omissions make the results difficult to reproduce and make it hard to determine the source of the gains.

#### 5. Statistical evidence is weak

Although means and standard deviations over five seeds are reported, there are no paired significance tests or confidence intervals. Several improvements are small relative to the variability, especially on Sports. The claim that the gate “accounts for most of the improvement” is also not adequately supported without more controlled ablations, such as:

- fixed versus learned monotonic decay;
- a learned per-edge weight without time;
- gates with different functional forms;
- gates trained with and without graph normalization;
- parameter-matched baselines.

#### 6. Numerical inconsistency

Using the values in Table 1, the average LightGCN Recall@20 is approximately 0.0834, while the SeqGate average is approximately 0.0874. This corresponds to an improvement of roughly **4.9%**, not 4.6%. The reported 2.1% improvement over SGL is approximately correct. The paper should correct or explain the discrepancy.

#### 7. Interpretation of the history-length result

The stronger improvement for users with long histories is plausible, but the analysis lacks sample counts, uncertainty estimates, and details about how users are grouped. It is also possible that long-history users have systematically different item popularity or activity distributions. Additional controls would make this conclusion more convincing.

#### 8. Computational claim needs clarification

The gate depends only on fixed timestamps and four shared scalar parameters. Therefore, gate values could likely be cached or recomputed with negligible cost relative to graph propagation. The reported 9% per-epoch overhead may be implementation-specific, and the paper should report hardware, dataset scale, wall-clock time, memory use, and whether the gate is cached.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 58/100 |
| Novelty | 55/100 |
| Significance | 52/100 |
| Clarity | 78/100 |

**Final average:**  
\[
\frac{58+55+52+78}{4}=60.75
\]

## Final recommendation: **Reject**

The paper is clearly written and presents a plausible, inexpensive modification to LightGCN. However, its novelty is limited, the “session-aware” framing is overstated, the baseline tuning protocol is potentially unfair, and the experimental description lacks details needed to establish reproducibility and soundness. A substantially revised version with stronger positioning against prior time-aware graph methods, fair hyperparameter tuning, statistical testing, and more complete ablations could be reconsidered.