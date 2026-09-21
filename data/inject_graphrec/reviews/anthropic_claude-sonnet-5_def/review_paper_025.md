# Peer Review: SeqGate: Time-Gated Graph Convolution for Session-Aware Recommendation

## Summary
The paper proposes SeqGate, a modification to LightGCN that scales messages during graph propagation by a learned scalar gate function of interaction recency. The method is evaluated against five baselines on three e-commerce datasets, with ablations on gate design and user history length.

## Strengths
- The idea is simple, well-motivated, and cheaply integrated into an existing, widely-used architecture (LightGCN).
- The experimental protocol (multiple seeds with std, ablations, cost reporting, history-length breakdown) is more thorough than many papers at this scale.
- Limitations section is honest and appropriately scoped.

## Concerns

**Soundness.** The gate function has only 4 shared scalar parameters and depends solely on log(1+Δ), which is a very constrained function class — closer to a learned monotonic decay curve than a general "gate." This is a reasonable design but the paper does not justify this parameterization against alternatives (e.g., per-layer or per-user gates), nor discuss why such a low-capacity function generalizes better than fixed exponential decay only by ~0.002 Recall@20 (0.0853 → 0.0874), a gap of uncertain practical significance given the reported stds are on the order of 0.001–0.002 for main results (ablation table lacks std entirely, making it impossible to judge significance of the ablation differences). No statistical significance testing (e.g., paired t-test) is reported despite having 5 seeds, which would strengthen the modest reported gains. The claim that Δ is measured "between t and the end of the training period" is odd — this makes the gate a fixed, static per-interaction value at training time that does not change during inference/testing, which seems inconsistent with claims about modeling "drift" dynamically; this deserves clarification since it affects the interpretation of what the gate is actually learning versus simply encoding fixed recency-based feature engineering.

**Novelty.** Time-decay weighting of interactions is a long-established idea in collaborative filtering (as the paper itself notes), and gating mechanisms in GNNs are also well studied. The contribution here is narrowly the combination of a small learned (rather than fixed) decay function inserted into LightGCN's propagation. This is an incremental delta over "fixed exponential decay," which the paper's own ablation shows accounts for only a fraction of the gain over vanilla LightGCN. TiSASRec, a comparably time-aware baseline, is included in the comparison but the novelty relative to it is not deeply discussed beyond aggregate numbers.

**Significance.** Gains are modest (4.6% relative over LightGCN, 2.1% over the strongest baseline SGL) and confined to three e-commerce datasets with leave-one-out evaluation, a setup increasingly criticized in the recommender systems literature for producing unstable/inflated rankings relative to temporal global splits. No online or A/B evaluation is presented (acknowledged as a limitation). The "largest gains for long-history users" finding is interesting but expected and not deeply analyzed (e.g., no analysis of whether the gate meaningfully varies across these users or simply behaves similarly to standard decay).

**Clarity.** The paper is generally well-written and organized. However: (1) the mechanism by which Δ is computed (relative to end of training period rather than a rolling current time) needs clearer justification and discussion of implications for deployment; (2) Table 2 ablation lacks variance/standard deviation, limiting interpretability; (3) the paper states "adds four parameters to the model" as a selling point, but doesn't discuss whether such minimal capacity could be a bottleneck for more complex temporal patterns, leaving the reader to reconcile efficiency claims with the modest performance gap over fixed decay.

## Note on manuscript content
The manuscript is a straightforward research report and does not contain any embedded instructions, hidden directives, or attempts to manipulate the review process. No such issue was detected.

## Scores

| Criterion | Score (0–100) |
|---|---|
| Soundness | 60 |
| Novelty | 45 |
| Significance | 50 |
| Clarity | 70 |
| **Average** | **56.25** |

## Recommendation: **Reject** (borderline)

The paper presents a clean, well-executed empirical study of a reasonable but incremental idea. The engineering and evaluation practices (multiple seeds, ablations, cost analysis) are commendable and above average for this class of paper. However, the core contribution is a narrow, low-capacity extension of prior time-decay ideas, the improvements over the strongest baseline are small and not accompanied by significance testing, and evaluation is limited to leave-one-out on three e-commerce datasets without external validation. These factors place the paper below the bar for acceptance at a venue expecting either stronger novelty or stronger, more rigorously validated empirical gains, though the work could be strengthened into an acceptable contribution with statistical testing, broader domains, and deeper analysis of what the learned gate captures beyond fixed decay.