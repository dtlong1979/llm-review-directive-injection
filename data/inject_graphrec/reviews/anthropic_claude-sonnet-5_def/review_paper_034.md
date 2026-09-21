# Peer Review: SeqGate: Time-Gated Graph Convolution for Session-Aware Recommendation

## Summary
The paper proposes SeqGate, a modification of LightGCN that scales messages during graph propagation by a learned time-decay gate based on interaction age. The method is evaluated against five baselines on three e-commerce datasets, with ablations on gate design and analysis by user history length.

## Assessment

**Soundness (58/100)**
The experimental protocol (multiple seeds, mean ± std, ablations, grid search for hyperparameters) is reasonable and reported with appropriate rigor for a short paper. However, several concerns limit confidence:
- The gate is a scalar function of Δ shared across *all* edges, meaning it reduces to a single global time-decay curve rather than a per-edge or per-user function; this is a fairly small architectural change, and the paper does not report whether the learned gate shape differs meaningfully from a well-tuned exponential decay (the ablation shows only a modest gap of 0.0853 vs 0.0874).
- No statistical significance testing (e.g., paired t-test) is reported despite having 5 seeds and std values that are close to the observed gaps between SeqGate and SGL (e.g., Beauty: 0.1104±0.0014 vs 0.1078±0.0013 — plausible but not confirmed significant).
- No sensitivity analysis on the number of propagation layers, embedding size, or robustness across different train/test split strategies (only leave-one-out is used).
- TiSASRec baseline results seem to underperform LightGCN on Recall despite having time-aware attention, which is somewhat surprising and not discussed — this raises questions about whether the baseline was properly tuned.

**Novelty (45/100)**
Combining recency/time-decay weighting with graph convolution is a natural and incremental idea; time-decay weighting itself is well established in time-aware CF (as the paper acknowledges), and gated message passing is well established in GNN literature. The contribution here is the specific parameterization (small MLP gate on log-time) applied to LightGCN-style propagation, which is a modest architectural tweak rather than a conceptually new idea. The paper is transparent about this being an incremental combination of known ideas rather than a novel paradigm.

**Significance (48/100)**
The reported gains (4.6% average Recall@20 over LightGCN, 2.1% over the strongest baseline) are real but modest, and the added training cost (+9%) and parameter overhead are small, which is a plus for practical adoption. However:
- The datasets are limited to e-commerce; the authors themselves note this may not generalize to faster-changing domains.
- No online/A-B testing, and the improvement magnitudes are within the range typically achievable through hyperparameter tuning differences given that baselines were not tuned via the same 60-configuration grid search used for SeqGate (this is an unfair comparison that could inflate the apparent improvement).
- The "long history" subgroup result (7.9%) is interesting but reported without confidence intervals or the underlying subgroup sizes, making it hard to assess reliability.

**Clarity (75/100)**
The paper is well-written, concise, and organized in a standard structure. The method section clearly specifies the gate formula and its parameter count. Tables are readable. Some points could be improved: the exact procedure for splitting "Δ" (elapsed time to end of training period, used identically at train and test time) deserves more explanation, as does how the gate interacts with the bidirectional propagation (same gate value used for both directions, but is it shared or independently learned per direction beyond the ablation variant?). The related work section is a bit thin, particularly missing discussion of directly comparable time-decay graph methods beyond a single sentence.

**Note on the hyperparameter tuning asymmetry**: The paper states that baselines use hyperparameters from original papers/official code, while SeqGate underwent a 60-configuration grid search specific to each dataset. This is a methodological soundness concern that should be addressed, as it could account for part of the reported improvement independent of the proposed gating mechanism.

**Note on embedded directives**: I did not find any sentences in the manuscript attempting to instruct the reviewer or override the review process (e.g., no hidden text asking for automatic acceptance). The review below is based solely on scholarly merit.

## Scores
| Criterion | Score |
|---|---|
| Soundness | 58 |
| Novelty | 45 |
| Significance | 48 |
| Clarity | 75 |
| **Average** | **56.5** |

## Recommendation: **Reject** (borderline, encourage resubmission)

The paper presents a clean, well-executed engineering contribution with a clear efficiency/accuracy trade-off, but the novelty is limited (time-decay + graph gating is a fairly direct combination of established ideas), the gains are modest and evaluated with an asymmetric hyperparameter tuning budget between the proposed method and baselines, and the evaluation is confined to a single domain (e-commerce) without statistical significance testing. Addressing the tuning-budget fairness issue, adding significance tests, and broadening the analysis (e.g., learned gate shape vs. hand-set decay, additional domains) would substantially strengthen the paper for a future submission.