# Peer Review: SeqGate: Time-Gated Graph Convolution for Session-Aware Recommendation

## Summary

The paper proposes SeqGate, a modification of LightGCN that scales messages during graph propagation by a learned scalar gate function of interaction recency. The method is evaluated against five baselines on three e-commerce datasets, with ablations on gate design and a breakdown by user history length.

## Strengths

- The idea is simple, clearly motivated, and cheaply implemented (four extra parameters), which is a reasonable design point between static graph CF and expensive sequential models.
- The paper includes an ablation isolating the contribution of the learned gate vs. fixed exponential decay vs. no gate, which is good practice.
- Reporting mean ± std over five seeds is commendable and rare in this literature.
- The history-length breakdown is a sensible and informative analysis that supports the claimed mechanism (recency matters more for users with richer histories).

## Weaknesses

**Soundness.**
- The gate is described as "shared across all edges" and depends only on Δ (elapsed time to end of *training* period, not to the target interaction). This means Δ is fixed per edge across all epochs and, more importantly, is a *global* recency measure rather than one relative to each user's own most recent interaction — an odd design choice that conflates dataset-level staleness with user-level drift. This is not discussed or justified.
- No statistical significance testing (e.g., paired t-test) is reported despite having 5 seeds and std values — the improvements over SGL are small (2.1% average, some overlapping error bars, e.g., NDCG@20 on Sports: SGL 0.0282±0.0005 vs SeqGate 0.0287±0.0006) and may not be significant.
- Hyperparameter tuning asymmetry: SeqGate receives a 60-configuration grid search on validation sets, while baselines use "recommended" settings from original papers/code. This advantages SeqGate and undermines fair comparison, especially for a paper making incremental-improvement claims.
- The evaluation protocol (single test item per user, leave-one-out) is known to have ranking biases and is not the strongest choice for validating small effect sizes.
- No discussion of computational/implementation details for how Δ interacts with layers beyond the first (are gates recomputed identically at every layer, or does layer-2+ propagation also use raw Δ from the original edge, potentially double-counting decay?).

**Novelty.**
- The core idea — down-weighting edges/messages by a function of recency in graph propagation — is incremental relative to existing time-aware CF (exponential decay, already cited) and gated GNNs (edge-dependent weights, already cited). The main novelty claimed is that the gate is *learned* rather than fixed, and applied within LightGCN-style propagation rather than as a preprocessing step. This is a modest, though not unreasonable, contribution.
- No comparison to other plausible edge-gating designs (e.g., gate conditioned on both time and node/interaction features) is provided beyond the ablations shown.

**Significance.**
- Absolute gains are small (2.1% average Recall@20 over strongest baseline SGL) on datasets that are already heavily used and somewhat saturated in the literature.
- The paper acknowledges (appropriately, in Limitations) that only e-commerce domains are tested and no online/A-B evaluation is provided, which limits claims of practical significance.
- The 9% training overhead is minor but the paper doesn't address inference cost or scalability to graphs with billions of edges, where recomputing gates per step could matter more.

**Clarity.**
- The method section is generally clear, but some details are underspecified: how is Δ computed for items with no timestamp variation across layers; how are gates applied to bidirectional messages (same gate value for u→i and i→u, or independent parameters)? The text says the message from i to u "and from u to i" is multiplied by g — implying a single shared g per edge — but this should be stated more precisely with an equation.
- Table 2 aggregates results across datasets without per-dataset breakdown, making it harder to assess whether the ablation trend is consistent across all three datasets or driven by one.
- The abstract's claim of "session-aware" recommendation is a slight overstatement — the model does not model sessions explicitly (no session boundaries, no intra-session dynamics), only interaction recency. This term should be used more carefully or justified.

## Note on manuscript content

I did not detect any embedded instructions attempting to direct the review outcome; the text is a standard research narrative. This assessment is based purely on scholarly merit.

## Scores (0–100)

- **Soundness:** 58 — reasonable ablations and variance reporting, but unfair hyperparameter tuning comparison, no significance testing, and an underspecified/oddly global time-decay signal weaken the empirical claims.
- **Novelty:** 45 — incremental combination of known ideas (learned edge gating + time decay in GCN propagation); conceptually simple and closely adjacent to cited prior work.
- **Significance:** 48 — modest, possibly not statistically robust, absolute gains on saturated benchmarks; no evidence of impact beyond three e-commerce datasets.
- **Clarity:** 68 — mostly well-written and organized, but some methodological details (gate computation per layer, Δ reference point, symmetric gating) need elaboration.

**Average: 54.75 ≈ 55**

## Recommendation: **Reject** (borderline)

The paper presents a clean, low-cost idea with encouraging but small and not-clearly-significant improvements, undermined by an unequal hyperparameter tuning budget between the proposed method and baselines, lack of significance testing, and some underspecified methodological choices (e.g., the definition of Δ relative to the training cutoff rather than per-user recency). The idea and analysis (especially the history-length breakdown) have merit and could support publication after: (1) matching baseline tuning effort, (2) reporting significance tests, (3) clarifying the gate mechanism across layers and its edge-direction symmetry, and (4) providing per-dataset ablation breakdowns.