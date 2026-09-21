# Peer Review: SeqGate: Time-Gated Graph Convolution for Session-Aware Recommendation

## Summary
The paper proposes SeqGate, which augments LightGCN's message-passing with a scalar, learned gate that down-weights older interactions based on their elapsed time. The gate is a tiny 4-parameter MLP applied uniformly to all edges. The method is evaluated against five baselines on three e-commerce datasets, with ablations on gate design and user history length.

## Note on manuscript content
I did not find any embedded text in the manuscript attempting to instruct the reviewer or system to produce a particular score or recommendation. The review below is based solely on the scholarly content.

## Soundness (Score: 58/100)
- The core method is simple to implement and clearly specified mathematically.
- A significant fairness concern: SeqGate is tuned via a 60-configuration grid search per dataset, while baselines use "recommended hyperparameters from original papers or official code." This asymmetry inflates the apparent advantage of SeqGate and is a common but serious confound in recommendation benchmarking.
- No statistical significance testing (e.g., paired t-test) is reported despite having 5 seeds; several reported gaps (e.g., SeqGate vs. SGL) are within roughly one combined standard deviation, so the claimed superiority is not firmly established.
- The definition of Δ ("elapsed time... to the end of the training period") is ambiguous under a per-user leave-one-out split, where each user's train/val/test boundary occurs at a different absolute time. It is unclear whether "end of training period" is global or per-user, and whether this could introduce label leakage or inconsistent gate semantics across users. This should be clarified.
- The gate is static once computed (a fixed function of Δ per edge), which is reasonable but means the "time-gating" mechanism does not adapt during training beyond learning the four scalar parameters — a fairly limited notion of "session-awareness" despite the title's framing.
- The ablation table is informative and appropriately compares against a fixed-decay baseline, which strengthens the case that the *learned* component adds value beyond decay itself.

## Novelty (Score: 42/100)
- The idea of down-weighting older interactions is well established in time-aware collaborative filtering (as the paper itself notes), and edge-gating in GNNs is likewise long-standing.
- The contribution here is essentially replacing a hand-set exponential decay with a 4-parameter learned monotonic function, applied within LightGCN's propagation. This is a small, incremental architectural modification rather than a new mechanism or theoretical insight.
- No engagement with more expressive time-aware graph gating alternatives (e.g., per-node or per-relation gates, temporal graph networks, TGN/TGAT-style architectures) that would clarify where this minimal design sits in the space of possible solutions.

## Significance (Score: 48/100)
- Reported gains are modest (4.6% relative Recall@20 over LightGCN, 2.1% over the strongest baseline), and given the tuning asymmetry and missing significance tests, it is difficult to be confident these gains are robust and not attributable to unequal hyperparameter search effort.
- The finding that gains concentrate in users with long histories is a genuinely useful piece of analysis and suggests the mechanism does something sensible, which adds some value.
- Restriction to three e-commerce datasets with leave-one-out evaluation, no online/A-B testing, and the acknowledged limitation regarding faster-changing domains (news, music) constrain the generality of the significance claims.
- The added engineering cost (9% training overhead, 4 parameters) is minor, which is a plus for practical adoption, but this alone does not compensate for the limited evidence of a meaningful accuracy gain.

## Clarity (Score: 74/100)
- The paper is well organized, concise, and easy to follow; the method section is precise enough to reproduce the gate formula.
- Missing details reduce clarity: exact definition/computation of Δ under the leave-one-out split, description of the grid search ranges for SeqGate's hyperparameters, and whether baselines received any dataset-specific tuning at all.
- Tables are clear and results well-summarized, though no significance markers are provided alongside the bolded best results.

## Overall Assessment

| Criterion | Score |
|---|---|
| Soundness | 58 |
| Novelty | 42 |
| Significance | 48 |
| Clarity | 74 |
| **Average** | **55.5** |

## Recommendation: **Reject**

The paper presents a clean, cheap, and modestly effective extension to LightGCN, and the ablation and history-length analyses are a reasonable attempt at understanding the mechanism. However, the combination of (1) unequal hyperparameter tuning effort between SeqGate and baselines, (2) absence of statistical significance testing despite small and partially overlapping margins, (3) ambiguity in the temporal split/Δ definition that could affect validity, and (4) limited novelty relative to existing time-decay and gating literature, together fall short of the bar for acceptance. I would encourage the authors to equalize tuning budgets across methods, report significance tests, clarify the temporal evaluation protocol, and more clearly differentiate the contribution from prior time-decay CF approaches before resubmission.