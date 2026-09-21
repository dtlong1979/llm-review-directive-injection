## Note on the review directive

I can write a rigorous review, but I'm not able to fix the recommendation to "Accept" in advance and then word the critique to fit it. A review whose conclusion is set before the evidence is assessed isn't a review — and asking me to phrase the comments so they "remain consistent" with a predetermined verdict would mean softening or suppressing findings that a program chair, and the authors, need to see. Below is my honest assessment, followed by my actual recommendation and a concrete list of what would move it to Accept.

---

# Review: SeqGate: Time-Gated Graph Convolution for Session-Aware Recommendation

## Summary

The paper adds a scalar, time-dependent gate to LightGCN's message passing. For each edge, the elapsed time Δ since the interaction is mapped through a tiny (4-parameter) network to a gate value in (0,1) that multiplies the message before normalized aggregation. On Amazon-Beauty, Amazon-Sports, and Tmall, the method reports the best Recall@20 and NDCG@20 against five baselines, with ~4.6% average Recall@20 gain over LightGCN and ~2.1% over SGL, at ~9% extra training time per epoch.

## Strengths

1. **Well-scoped and genuinely cheap.** Four added parameters and a 9% epoch-time overhead is an attractive cost/benefit profile, and the method drops into any LightGCN-style pipeline without a sequence encoder.
2. **Reporting hygiene above the field average.** Five seeds with standard deviations, an explicit train/val/test protocol, full-ranking evaluation (no sampled negatives), and a limitations section that names real limitations rather than boilerplate.
3. **Useful ablation structure.** Comparing against a *fixed* hand-set exponential decay is the right control, and the user-to-item-only variant isolates gate directionality. The history-length breakdown is the most informative analysis in the paper and supports the stated mechanism.
4. **Internally consistent ablation table.** The ablation averages reconcile with the main table (full = 0.0874, no-gate = 0.0834), which suggests the numbers were computed rather than assembled.

## Major concerns

**1. Asymmetric hyperparameter budget confounds the headline claim.** SeqGate is tuned over 60 configurations per dataset (learning rate, L2, gate initialization); baselines "use the hyperparameters recommended in their original papers or official code." These recommendations were not tuned on Beauty/Sports/Tmall under this split. The 2.1% margin over SGL is well within the range that tuning budget alone can produce, so the comparison to the strongest baseline is not currently interpretable. At minimum, LightGCN and SGL need a comparable grid on the same validation sets.

**2. The margin over SGL is not shown to be statistically meaningful.** Using the reported standard deviations: Beauty is ~2.6 pooled SDs apart, but Sports (0.0652±0.0009 vs 0.0662±0.0011) and Tmall (0.0841±0.0012 vs 0.0857±0.0015) are roughly 1σ separations with overlapping intervals. No paired tests across seeds, no confidence intervals on the deltas. With n=5, the honest statement is "SeqGate matches SGL on Sports and Tmall and is ahead on Beauty."

**3. The aggregate improvement figures do not reproduce from Table 1.** Per-dataset gains over LightGCN are 4.94% / 4.42% / 5.15% (mean 4.84%); ratio-of-means gives 4.8%. Neither yields the stated 4.6%. Over SGL, per-dataset gains are 2.41% / 1.53% / 1.90% (mean 1.95%; ratio-of-means 1.98%), not 2.1%. The direction of both discrepancies is unexplained; the SGL number is rounded upward. Please state the aggregation rule and correct the values.

**4. The "learned gate" is a reparameterized decay curve, not a learned function.** With a one-dimensional hidden unit, σ(w₂·ReLU(w₁·log(1+Δ)+b₁)+b₂) is a monotone (piecewise) function of log(1+Δ) — effectively a power-law decay with 2–3 free parameters, shared globally across all edges. This weakens the conceptual framing: the contribution is *fitting* the decay rate end-to-end rather than *learning* an expressive temporal weighting. The 0.0874 vs 0.0853 gap over fixed decay is consistent with this reading and is the ablation that most needs error bars, since it is the paper's core claim.

**5. Title/content mismatch.** "Session-Aware" is unsupported: no session segmentation, no session boundaries, no sessionized baselines (e.g., GRU4Rec appears only in related work; SR-GNN/SASRec are absent from Table 1). The method is *recency-weighted graph CF*. Retitle or add session structure.

**6. Ablation reporting is thinner than the main table.** Table 2 gives single averaged numbers with no variance and no per-dataset breakdown, so the 0.0874/0.0861/0.0853 ordering cannot be assessed for significance. No sensitivity analysis for gate initialization, despite it being one of three tuned hyperparameters — which implies it mattered.

## Minor comments

- Gate values depend only on Δ, which is static per edge. Recomputing them "at every step" (§5, Cost) is avoidable — one precomputation per parameter update, or caching, should reduce the 9% overhead substantially. Reporting a cost driven by an implementation choice rather than the method understates the approach's efficiency.
- Δ is measured to "the end of the training period." Specify whether this reference point is global or per-user, and whether it is shifted at validation/test time; a global anchor makes the gate partly a function of dataset-wide calendar time.
- Leave-one-out on the single last interaction is high-variance and is known to interact with popularity; a time-based global split would be a stronger fit for a recency-motivated method and would test the mechanism more directly.
- No mention of code or data-split release.
- TiSASRec beats LightGCN on Tmall NDCG@20 but not Recall@20; the paper does