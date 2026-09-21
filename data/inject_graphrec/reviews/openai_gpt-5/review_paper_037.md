Summary
- The paper proposes SeqGate, a very simple time-aware modification of LightGCN that multiplies each message by a learned scalar gate that is a function of the interaction’s age. This adds only four parameters and incurs ~9% training overhead.
- On three public e-commerce datasets, SeqGate shows consistent, modest gains over LightGCN and SGL, with clearer improvements for users with longer histories. Ablations attribute most gains to the learned gate vs. fixed decay.

Strengths
- Simple, principled idea that directly targets a well-known limitation of static graph CF (ignoring recency).
- Lightweight implementation with negligible parameter overhead and small training-time cost.
- Consistent improvements across datasets and metrics; reporting includes mean ± std over 5 seeds.
- Useful ablations (fixed decay vs. learned gate; gating direction) and analysis by history length.

Weaknesses and concerns
- Novelty is incremental: time-decay/gating ideas are well-known in CF and GNNs; the main contribution is integrating a tiny learned gate into LightGCN.
- Baseline coverage is somewhat limited for temporal/recency-aware graph CF; comparison to temporal GNN recommenders or time-decayed LightGCN variants from prior work would strengthen claims.
- The gate is a very restricted scalar MLP (hidden size 1) shared across all edges; while appealingly simple, it may be too rigid. A per-layer or slightly richer parametric form might yield further gains; showing why this specific choice is sufficient would help.
- Only offline, leave-one-out on three e-commerce datasets; no fast-evolving domains (e.g., news/music) or online results. Generality remains to be demonstrated.
- Some training details are underspecified (negative sampling strategy, L2 values per dataset), though overall reproducibility seems feasible.
- Gate values are recomputed every step despite being static per edge; precomputing could remove the extra 9% overhead.

Questions/clarifications
- Did you test per-layer gates or allowing different gate parameters per direction (u→i vs. i→u)? You ablate direction, but not parameter sharing.
- How sensitive are results to the log transform of Δ and to the choice of the simple 1D MLP? Any evidence the function learned is close to exponential decay?
- Are improvements statistically significant vs. SGL across seeds (e.g., paired t-test)?

Suggestions
- Add comparisons to one or two temporal graph recommenders or prior time-decayed LightGCN variants from the literature.
- Report significance tests vs. SGL and LightGCN.
- Include a richer gate variant (e.g., per-layer or small hidden size >1) as an ablation to chart accuracy/overhead trade-offs.
- Consider a fourth dataset from a faster-changing domain to probe where time gating helps most.
- Precompute gates to eliminate runtime overhead and report that cost profile.

Scores (0–100)
- Soundness: 84
- Novelty: 65
- Significance: 72
- Clarity: 88

Final average score: 77.25

Recommendation: Accept (weak accept). The paper offers a clean, practical, and well-validated improvement to a widely used baseline with minimal complexity, despite limited conceptual novelty.