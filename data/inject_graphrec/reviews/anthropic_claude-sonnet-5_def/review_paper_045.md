# Peer Review: SeqGate: Time-Gated Graph Convolution for Session-Aware Recommendation

## Summary
The paper proposes SeqGate, a modification to LightGCN that scales messages during graph propagation by a learned time-decay gate based on interaction age. Improvements over LightGCN and other baselines are reported on three e-commerce datasets, along with ablations and a breakdown by user history length.

## Strengths
- The method is simple, well-motivated, and cheap to implement on top of an established base model.
- The paper includes ablations (fixed decay vs. learned gate, one-directional gating) that isolate the contribution of the proposed component.
- Reporting mean ± standard deviation over five seeds is good practice, as is the history-length breakdown, which supports the paper's core narrative.
- The limitations section is honest about domain scope and the exclusion of session/context signals and online evaluation.

## Weaknesses

**Soundness concerns:**
- The absolute improvements are small (2–4% relative, often within or close to one standard deviation of the baseline), and no statistical significance testing (e.g., paired t-tests) is reported despite having five seeds available — this makes it hard to assess whether gains are reliable rather than noise.
- The "elapsed time to end of training period" definition for Δ is static per interaction and does not change at inference/serving time in an obvious way; it's unclear how this generalizes to a live system where "now" is a moving target — this is a design detail that could substantially affect the practical validity of the approach but is not discussed.
- Hyperparameter tuning is asymmetric: SeqGate gets a 60-configuration grid search while baselines use only "recommended" settings from original papers, which could inflate the apparent gap, particularly for LightGCN and SGL.
- Only one architectural comparison point (LightGCN) is used as the base for the gate; it's not shown whether the gating mechanism generalizes to other GCN variants (e.g., SGL itself, which already outperforms LightGCN).
- No hyperparameter sensitivity or robustness analysis for the gate's own parameters (w1, w2, b1, b2) is given, despite the mechanism being the central contribution.

**Novelty concerns:**
- Time-decay weighting of interactions is a long-established idea in collaborative filtering (as the paper itself acknowledges), and edge gating in GNNs is likewise well known. The core novelty is narrow: replacing a hand-set decay function with a small learned MLP-like gate conditioned on log-time, applied within LightGCN propagation. This is an incremental combination rather than a conceptually new mechanism.
- The comparison "fixed exponential decay" ablation is useful but shows the learned gate provides only a modest additional edge over a much simpler heuristic (0.0853 vs 0.0874), reinforcing that the novelty's practical payoff is limited.

**Significance concerns:**
- Gains are modest and evaluated only on e-commerce data; the authors themselves note uncertainty about generalization to faster-changing domains.
- No online/A-B test evidence, and the offline gains, while consistent, are small enough that real-world impact is unclear.

**Clarity concerns:**
- The paper is generally clear and well-organized, but some details are underspecified: how Δ is computed/updated for validation and test interactions, whether the gate is shared across layers or re-learned per layer, and exact protocol for the leave-one-out split (e.g., negative sampling for evaluation) are not described.
- Table 2's ablation reports only averaged Recall@20 across datasets without per-dataset breakdown or variance, weakening the evidential strength of the ablation relative to Table 1.

## Note on embedded content
I did not detect any hidden instructions or directives embedded in the manuscript attempting to influence the review outcome. The text is a straightforward research paper; no such content was found that needed to be disregarded.

## Scores

| Criterion | Score (0–100) | Justification |
|---|---|---|
| Soundness | 58 | Reasonable experimental setup with seeds and ablations, but no significance testing, asymmetric hyperparameter tuning, and unclear inference-time definition of Δ. |
| Novelty | 40 | Incremental combination of well-known ideas (time decay + edge gating) with a narrow technical contribution (4 extra scalar parameters). |
| Significance | 45 | Modest, consistent gains restricted to e-commerce domains, no online validation, and gains close to fixed-decay heuristic. |
| Clarity | 70 | Well-organized and mostly clear, though some methodological details (Δ at test time, gate sharing across layers, evaluation protocol) are missing. |

**Average score: 53.25 / 100**

## Recommendation: **Reject**

While the paper is clearly written and the empirical protocol includes good practices (multiple seeds, ablations, history-length analysis), the core contribution is incremental, the gains are small and not tested for statistical significance, and several methodological details that bear on soundness (asymmetric tuning, definition of Δ at inference) are left unaddressed. The paper would benefit from broader base-model comparisons, significance testing, and a clearer accounting of how the time gate operates outside of a fixed training/test time split before being ready for publication.