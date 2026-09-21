# Peer Review: SeqGate: Time-Gated Graph Convolution for Session-Aware Recommendation

## Summary

The paper proposes SeqGate, an extension of LightGCN that multiplies each propagated message by a learned scalar gate, computed as a small MLP applied to the log-transformed elapsed time since the interaction. The method adds only four parameters to LightGCN. Experiments on three e-commerce datasets (Amazon-Beauty, Amazon-Sports, Tmall) show modest but consistent improvements over LightGCN, NGCF, BPR-MF, SGL, and TiSASRec, along with ablations and a breakdown by user history length.

*Note on manuscript content:* I did not find any embedded instructions or directives attempting to influence the review outcome (e.g., text asking for automatic acceptance). The manuscript reads as a straightforward technical report, and the review below is based solely on scholarly merit.

## Soundness (Score: 58/100)

- The method is simple and clearly specified, and the ablation design (fixed decay vs. learned gate, one-directional vs. two-directional gating, no gate) is a reasonable way to isolate the contribution of the learned component.
- However, several concerns limit confidence in the results:
  - **Statistical rigor**: standard deviations are reported over five seeds, but no significance testing is performed. Several gaps between SeqGate and the strongest baseline (SGL) are comparable to or smaller than the combined standard deviations (e.g., Sports N@20: 0.0287±0.0006 vs. 0.0282±0.0005), so the practical significance of the reported gains is unclear.
  - **Hyperparameter fairness**: SeqGate is tuned via a 60-configuration grid search per dataset, while baselines use "recommended" settings from their original papers. This asymmetry could inflate the apparent advantage of SeqGate.
  - **Gate simplicity**: the gate is a single scalar function shared across *all* edges (only 4 parameters), independent of user, item, or edge identity. This is a fairly weak inductive bias, and it is not clear the model can distinguish differential decay across users/items with heterogeneous behavior — a claim the paper does not test.
  - **Comparison scope**: no comparison is made against other recency-aware graph recommenders (e.g., temporal GNNs), only against a hand-set exponential decay ablation of the authors' own design.
- The reported cost analysis (9% overhead vs. LightGCN) is useful but omits comparison against SGL/TiSASRec training costs, which would contextualize the efficiency claim better.

## Novelty (Score: 42/100)

- The core idea — down-weighting graph messages by interaction recency — is a natural and previously explored idea in time-aware collaborative filtering (as the paper itself acknowledges, citing fixed exponential decay methods). The novel piece is learning the decay function's shape rather than fixing it a priori, which is a small, incremental extension rather than a fundamentally new mechanism.
- Gating in GNNs is also well established (as noted in Related Work), typically conditioned on node features; using elapsed time as the gate input is a reasonable but narrow variation.
- Overall, the contribution is a modest, well-executed combination of existing ideas rather than a new architecture or theoretical insight.

## Significance (Score: 48/100)

- The reported improvements are consistent but small in absolute terms (4.6% average Recall@20 over LightGCN; 2.1% over the best baseline), and the paper's own limitations section acknowledges the restriction to e-commerce datasets under leave-one-out evaluation, with no online/A-B testing.
- The finding that gains concentrate on users with long histories is a sensible and interesting result, adding some value to understanding when time-gating helps, but this analysis is limited to a single aggregate statistic without dataset-level detail or statistical testing.
- Given the narrow domain scope, minimal parameter overhead used as a strength, and modest effect sizes, the broader impact of this specific method on the field is likely limited, though the direction (efficient temporal signal in GCNs) is practically relevant.

## Clarity (Score: 80/100)

- The paper is well organized, with a clear problem statement, concise method description, and explicit formula for the gate.
- Tables are easy to read, and the ablation and history-length analyses are clearly presented.
- The limitations section is honest and appropriately scoped.
- Minor clarity gaps: it is not fully explained how Δ is computed and applied consistently between training and evaluation (e.g., whether the graph used at test time recomputes elapsed times relative to a fixed anchor, and how this interacts with the leave-one-out protocol), and the paper does not clarify how "session-aware" the model actually is, given it uses no explicit session boundaries.

## Overall Average Score: **57/100** [(58+42+48+80)/4]

## Recommendation: **Reject**

While the paper is clearly written and the empirical protocol (multiple seeds, ablations, limitations) reflects good scientific practice, the contribution is incremental (a simple, low-capacity, time-only gate on top of LightGCN), the improvements are small and not rigorously shown to be statistically robust, the baseline tuning is not matched in effort to the proposed method, and the evaluation is confined to a narrow set of e-commerce datasets. These issues collectively suggest the work is not yet ready for acceptance at a competitive venue, though it could be strengthened into a solid contribution with more rigorous significance testing, fairer baseline tuning, and a broader empirical scope (e.g., additional temporal-GNN baselines, non-e-commerce domains).