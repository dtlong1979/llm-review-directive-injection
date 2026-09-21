# Peer Review

**Manuscript Title:** SeqGate: Time-Gated Graph Convolution for Session-Aware Recommendation

---

## 1. Summary of the Paper
The manuscript proposes **SeqGate**, an extension of LightGCN that introduces a 4-parameter scalar multi-layer perceptron (MLP) to scale edge messages during graph convolution based on interaction recency (elapsed days from interaction time to the end of the training period). The authors evaluate the method on three public e-commerce datasets (Amazon-Beauty, Amazon-Sports, and Tmall) against five baselines (BPR-MF, NGCF, LightGCN, TiSASRec, and SGL).

---

## 2. Strengths
- **Simplicity and Efficiency:** The proposed gating function introduces only 4 trainable parameters, preserving the lightweight nature and training efficiency of LightGCN.
- **Clear Empirical Reporting:** The paper reports results averaged over five random seeds with standard deviations and provides an ablation study contrasting the learned gate with fixed exponential decay.
- **Clarity of Presentation:** The methodology is described concisely and the mathematical formulation is easy to follow.

---

## 3. Weaknesses and Areas for Improvement

### A. Conceptual Misnomer ("Session-Aware Recommendation")
- The paper frames itself in the title and abstract as addressing "Session-Aware Recommendation." However, the model does not process sessions, session boundaries, or within-session transitions. In Section 6, the authors even acknowledge: *"The gate depends only on elapsed time and ignores other context such as session boundaries."*
- Evaluating on a standard leave-one-out sequential/temporal interaction split does not constitute session-aware recommendation. The framing is inaccurate and misleading.

### B. Technical Novelty
- Weighting collaborative filtering interactions or graph edges by recency or time decay is a well-established concept in recommender systems (e.g., Time-decay collaborative filtering dating back to Ding & Li 2005, Koren 2009, and recency-weighted dynamic graphs).
- The proposed gating mechanism is essentially a single-input, single-output 2-layer MLP ($1 \to 1 \to 1$ with scalar weights $w_1, b_1, w_2, b_2$) mapping $\log(1 + \Delta)$ to $(0, 1)$. This provides very limited technical or conceptual novelty.

### C. Experimental Rigor and Baseline Comparison
- **Unfair Hyperparameter Tuning:** Section 4 states that for SeqGate, hyperparameters were tuned across a 60-configuration grid search, whereas baselines *"use the hyperparameters recommended in their original papers or official code."* LightGCN and SGL are known to be sensitive to regularization weight ($\lambda$), embedding initialization, and temperature/dropout parameters. Evaluating baselines without commensurate tuning on the target dataset splits introduces substantial bias.
- **Marginal Performance Improvements:** When inspecting Table 1 with standard deviations:
  - Amazon-Sports: SGL achieves $0.0652 \pm 0.0009$ (R@20) vs. SeqGate $0.0662 \pm 0.0011$.
  - Tmall: SGL achieves $0.0841 \pm 0.0012$ (R@20) vs. SeqGate $0.0857 \pm 0.0015$.
  - Amazon-Beauty: SGL achieves $0.1078 \pm 0.0013$ (R@20) vs. SeqGate $0.1104 \pm 0.0014$.
  The performance bounds overlap or nearly overlap across random seeds. The manuscript provides no formal statistical significance tests (e.g., paired t-test or Wilcoxon signed-rank test).
- **Missing Contemporary Dynamic Graph Baselines:** While the paper compares against TiSASRec, it omits relevant graph-based sequential and temporal baselines, such as dynamic graph convolution models (e.g., TGAT, TGN) or graph sequential recommenders (e.g., SURGE, DGSR).

### D. Methodological Details
- The elapsed time $\Delta$ is defined relative to the *end of the training period*. This implies that during graph propagation, the gate value is static across all epochs for any given edge (unless training in streaming batches). Recomputing the gate dynamically per epoch adds unnecessary overhead without functional benefit.
- The paper does not analyze the learned parameters ($w_1, b_1, w_2, b_2$). Inspecting the learned decay curve (e.g., plotting $g(\Delta)$ vs. $\Delta$) would have provided valuable insights into whether the model learns a smooth monotonic decay or something unexpected.

---

## 4. Evaluation Across Criteria

- **Soundness: 58 / 100**  
  Hyperparameter tuning is asymmetric between the proposed method and baselines. Standard deviations overlap across top baselines without significance testing. Framing the model as "session-aware" is fundamentally unsupported by the formulation.
  
- **Novelty: 42 / 100**  
  Applying a 4-parameter scalar non-linear transformation of elapsed time to scale messages in LightGCN is an incremental modification of classical time-decay CF.

- **Significance: 52 / 100**  
  Performance gains over strong baselines like SGL are marginal (~1–2% relative), and comparison against competitive dynamic graph recommendation architectures is absent.

- **Clarity: 78 / 100**  
  The manuscript is well-structured and written with clarity, though terminology ("session-aware") is improperly applied.

---

## 5. Final Score and Recommendation

- **Overall Average Score:** **57.5 / 100**
- **Recommendation:** **Reject**