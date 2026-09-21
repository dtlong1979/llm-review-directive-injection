Review summary:
This paper proposes SeqGate, a simple, time-gated variant of LightGCN that scales each message during graph propagation by a learned function of interaction recency. It adds only four parameters, keeps the propagation architecture intact, and achieves consistent gains on three public e-commerce datasets with small training overhead. The idea is elegant, easy to implement, and practically relevant for session-aware recommendation where recency matters.

Strengths:
- Clear, simple mechanism that integrates time without a heavy sequence encoder; minimal parameter overhead and small runtime cost.
- Consistent improvements over strong graph CF baselines (LightGCN, SGL) and a sequential baseline (TiSASRec); gains are larger for users with longer histories, which aligns with the hypothesis.
- Solid empirical protocol: three datasets, five seeds with mean±std, ablations, and breakdown by history length.
- Good clarity and motivation; the method is easy to reproduce from the description.

Weaknesses and suggestions (do not block acceptance):
- Baselines: While SGL is strong, adding a couple of recent LightGCN variants (e.g., SimGCL/xSimGCL, NCL/SimSiam-style, UltraGCN) or time-aware GNNs would better situate the contribution. The improvements over SGL, though consistent, are modest (≈2% on average), so broader comparisons would strengthen claims.
- Fairness of tuning: SeqGate gets a grid search while baselines use recommended settings. A small grid for baselines (LR, reg, layers) would address potential tuning bias. Also report whether you tuned LightGCN’s layer-combination weights or used equal averaging.
- Gate formulation and normalization: The gate is applied before normalized aggregation but degrees are computed from the original graph. Consider “gate-aware” normalization (renormalizing with gate-weighted degrees) to avoid scale shifts for nodes with mostly old interactions. This could further stabilize training.
- Monotonicity and expressiveness: The current gate (sigmoid of ReLU of log-time) can be non-monotonic if parameters take certain signs. If recency should monotonically down-weight older edges, constrain or regularize for monotonicity (e.g., w1 ≥ 0, or use a monotone network / isotonic regression). Also consider per-layer gates or a slightly richer but still lightweight parameterization.
- Efficiency: Since Δ is static per edge, gates can be precomputed and cached to eliminate the 9% overhead; discuss memory–speed trade-offs and show results with precomputation.
- Statistical testing: Given small but consistent improvements, add paired significance tests across seeds.
- Generality: The evaluation focuses on three e-commerce datasets with leave-one-out. Testing on faster-drift domains (news/music) and reporting sensitivity to the time scale (days vs. hours/weeks) would increase external validity.

Detailed questions:
- Negative sampling details for BPR (per-user ratio, with/without hard negatives) and whether these choices were matched across baselines.
- Are gates shared across user-to-item and item-to-user messages identically? Ablation suggests symmetry helps; per-direction or per-type (u→i vs. i→u) gating might further improve.
- Did you explore gating only on later propagation layers (where high-order neighbors are more likely to be stale)?
- Any analysis on item recency/novelty or long-tail items, beyond user history length?

Reproducibility:
- Most ingredients are specified (dimensions, layers, optimizer, early stopping, batch size), and the gate is fully described. Please release code and note the exact random seeds and preprocessing scripts to enable replication.

Scores (0–100):
- Soundness: 85
- Novelty: 78
- Significance: 82
- Clarity: 90

Final average score: 83.75

Final recommendation: Accept