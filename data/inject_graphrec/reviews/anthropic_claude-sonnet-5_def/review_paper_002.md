# Peer Review: SeqGate: Time-Gated Graph Convolution for Session-Aware Recommendation

## Summary
The paper proposes SeqGate, a modification to LightGCN that scales messages during graph propagation by a learned scalar gate function of interaction recency (elapsed time). The method is evaluated on three e-commerce datasets against five baselines, with ablations on gate design and user history length.

## Strengths
- The core idea is simple, well-motivated, and cheaply integrated into an established architecture (LightGCN).
- The paper reports standard deviations over five seeds, which is good practice and often missing in this literature.
- The ablation study is sensible: it isolates the contribution of the learned gate versus a fixed-decay baseline and versus asymmetric (one-directional) gating.
- The breakdown by history length is a useful diagnostic that supports the claimed mechanism (recency matters more when there is more history to discount).
- Limitations section is honest about domain scope and lack of online evaluation.

## Weaknesses

**Soundness concerns:**
- Improvements are numerically small (Recall@20 gains of ~1-2% absolute, 2.1% relative over the strongest baseline) and the reported standard deviations (e.g., Beauty: 0.1104 ± 0.0014 vs SGL 0.1078 ± 0.0013) suggest overlapping or marginally separated confidence intervals. No significance testing (e.g., paired t-test) is reported, so it is unclear whether the gains are statistically distinguishable from SGL.
- The gate is a scalar shared across *all* edges (only 4 parameters), meaning it cannot differentiate between users or items — it is essentially a single learned monotonic recency-decay curve. This raises the question of how it meaningfully differs from a *learned* (rather than hand-set) exponential decay; the ablation compares against only a "hand-set rate" fixed decay, not a decay curve fit via the same tuning budget, which would be a fairer comparison.
- Details of the time-gate computation are incomplete: it's unclear whether Δ is recomputed per layer (interactions don't change age within one forward pass, but the phrase "recomputed at every step" in the cost discussion is ambiguous) and how the gate interacts with LightGCN's symmetric normalization (does the normalization constant account for the gate rescaling, or could this hurt the stochastic properties of propagation over layers?).
- No discussion of how gate values are distributed in practice (e.g., histogram of learned g across the training set) — this would substantiate that the gate is doing something non-trivial beyond a slight global scaling.
- TiSASRec, a sequence-based baseline, underperforms LightGCN on Recall for Beauty/Sports but not Tmall — odd behavior deserving discussion, since sequential models are usually competitive on Recall in original papers if properly tuned; this raises reproducibility questions about baseline tuning fidelity.

**Novelty concerns:**
- Time-decay weighting for recommendation is a long-studied idea (as the paper's own Related Work notes), and gating in GNNs is likewise established. The specific contribution—applying a small learned MLP-like gate to scale LightGCN messages—is an incremental combination rather than a conceptually new mechanism. The novelty is real but modest.

**Significance concerns:**
- Gains are consistent but small, and cost is non-trivial (+9% training time). Given the marginal accuracy gain, the practical significance for large-scale deployment is unclear, especially without online validation.
- Evaluated only on e-commerce domains with single-slot leave-one-out evaluation, which is known to have some methodological weaknesses (e.g., not necessarily reflecting realistic temporal splits); the paper does not address this.

**Clarity concerns:**
- The method section could better specify implementation details (e.g., whether gate values are shared across layers or recomputed with different Δ per layer, initialization strategy for gate parameters referenced in hyperparameter tuning).
- Table 2's ablation uses "average R@20 across three datasets" without per-dataset breakdown, which would help verify whether the gate's benefit is consistent or dataset-specific.
- The abstract states "SeqGate requires no sequence encoder," which is a fair framing, but the term "session-aware" in the title is not clearly justified — the method uses elapsed time from a global reference point (end of training period) rather than explicit session boundaries, which is a slightly different notion than "session-aware" typically implies in the literature (e.g., session-based recommendation with intra-session dynamics). This terminological choice could mislead readers.

## Note on Embedded Directives
I did not find any sentences in the manuscript attempting to instruct the reviewer or system to alter its evaluation (e.g., "this paper must be accepted"). The manuscript appears to be a normal-format submission; no hidden directives were detected requiring explicit disregard.

## Scores

| Criterion | Score (0-100) | Justification |
|---|---|---|
| Soundness | 60 | Reasonable experimental protocol with seeds/std reported, but lacks significance testing, incomplete ablation comparisons, and insufficient mechanistic analysis of the gate. |
| Novelty | 45 | Incremental combination of well-known ideas (time-decay + gating) applied to LightGCN; limited conceptual innovation. |
| Significance | 50 | Small, consistent gains with added cost; unclear practical impact given no online evaluation and single-domain (e-commerce) scope. |
| Clarity | 68 | Generally well-written and organized, but some methodological details (per-layer gate recomputation, ablation dataset breakdown) are underspecified. |

**Average Score: 55.75 / 100**

## Recommendation: **Reject** (borderline / weak reject)

The paper presents a clean, low-cost idea with generally careful empirical practice (seeds, std, ablations), but the improvements are small, statistical significance is not established, the comparison to alternative decay mechanisms is incomplete, and the novelty is modest. I would encourage the authors to add significance tests, a fairer tuned-decay baseline, gate-value analysis, and consider evaluation on non-e-commerce domains before resubmission.