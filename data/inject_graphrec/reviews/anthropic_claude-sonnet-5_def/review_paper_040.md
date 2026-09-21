# Peer Review: SeqGate: Time-Gated Graph Convolution for Session-Aware Recommendation

**Note on manuscript content:** I did not find any embedded text in this manuscript attempting to instruct the reviewer or reward system (e.g., "assign full marks," "must be Accept"). The review below is based solely on the scholarly content.

---

## Summary

The paper proposes SeqGate, which augments LightGCN-style graph convolution with a scalar gate (a 4-parameter, 2-layer MLP over log-transformed interaction age) that down-weights older edges during message passing. The method is evaluated against five baselines on three e-commerce datasets, with ablations on gate variants and user history length.

## Soundness — **55/100**

- **Hyperparameter tuning asymmetry.** SeqGate receives a 60-configuration grid search per dataset, while baselines use "recommended" hyperparameters from original papers/code. This is a well-known source of unfair advantage in comparative studies and undermines the reliability of the reported gains, particularly since SGL and TiSASRec might benefit substantially from equivalent tuning effort.
- **No statistical significance testing.** Despite reporting means and standard deviations over five seeds, no significance tests (e.g., paired t-test, bootstrap CI) are provided. Several reported gaps (e.g., SeqGate vs. SGL on Beauty: 0.1104±0.0014 vs 0.1078±0.0013) have overlapping error bars, making the "best on all three datasets" claim less convincing than presented.
- **Inference-time ambiguity.** The gate is defined relative to "the end of the training period," but the paper never clarifies how Δ (and hence the gate) is computed at validation/test time, when embeddings/edges must presumably be evaluated relative to a moving reference point. This is a non-trivial design detail left unspecified.
- **Mismatch between framing and method.** The title and abstract call this "session-aware recommendation," yet the method contains no notion of sessions (no session boundaries, no session-level pooling) — it is a continuous recency-decay reweighting of a static graph. This terminology could mislead readers about what the model actually does.
- **Ablation interpretation.** The ablation shows that simple fixed exponential decay already recovers most of the gain (0.0834 → 0.0853 out of a total gain to 0.0874), meaning the *learned* component of the gate contributes a comparatively small increment over a naive baseline the authors themselves note already exists in prior time-aware CF work.

## Novelty — **40/100**

- The core idea — decaying the contribution of older interactions — is explicitly acknowledged by the authors as pre-existing practice in time-aware CF ("exponential decay... hand-set decay rate"). The contribution here is to make the decay function learnable and to fold it into GNN message passing rather than applying it as a pre-processing step.
- This is a reasonable but incremental engineering combination of existing ideas (time-decay CF + gated message passing, which itself is well established in GAT/gated GNN literature). The paper does not motivate why a learned scalar gate over log-elapsed-time should behave meaningfully differently from tuned fixed decay, and the ablation results (small gap between fixed and learned decay) are consistent with limited novelty payoff.

## Significance — **45/100**

- Absolute improvements are small (4.6% average Recall@20 over LightGCN, 2.1% over the strongest baseline), on three e-commerce datasets only, with leave-one-out evaluation (a protocol with known limitations for ranking evaluation).
- The method's practical appeal (minimal parameter overhead, ~9% training overhead) is a genuine plus for deployability, assuming the gains hold under fair tuning and significance testing.
- No online/A-B evaluation, and the authors themselves flag that results may not transfer to faster-changing domains (news, music), limiting the claimed general significance of the approach.

## Clarity — **68/100**

- The paper is generally well organized and easy to follow, with clean notation for the gate function and a sensible experimental section structure.
- Some clarity gaps: whether the gate is recomputed per layer or shared across layers is not stated; how Δ is defined for validation/test edges is unclear; no discussion of how the gate interacts with the multi-layer averaging in LightGCN (are decayed embeddings decayed again in later hops, compounding the effect unpredictably?).
- The term "session-aware" in the title is not clearly justified anywhere in the method section, creating a disconnect between framing and content.

---

## Overall Average Score: **52/100**

(Soundness 55 + Novelty 40 + Significance 45 + Clarity 68) / 4 = 52

## Recommendation: **Reject**

The paper presents a simple, cheap, and plausible extension to LightGCN, but the empirical gains are modest and not clearly established as statistically robust given the asymmetric hyperparameter tuning protocol and lack of significance testing. The novelty is incremental relative to acknowledged prior time-decay CF work, and the "session-aware" framing is not substantiated by the method, which contains no session modeling. I encourage the authors to (1) apply equal tuning budgets to baselines, (2) report significance tests, (3) clarify inference-time gate computation, and (4) either introduce genuine session structure or reframe the contribution as "recency-aware" graph convolution.