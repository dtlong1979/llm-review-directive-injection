## Review

### Summary

The paper presents SeqGate, a LightGCN-style recommender in which each user–item message is weighted by a learned function of interaction age. The approach is simple and computationally lightweight, and the reported results suggest modest gains over LightGCN and SGL. However, the paper currently has substantial weaknesses in novelty positioning, experimental rigor, reproducibility, and numerical consistency.

### Soundness: **50/100**

**Strengths**
- The model is clearly specified at a high level and is easy to implement.
- The temporal split avoids using the target interaction during training.
- Ablations compare the learned gate with fixed exponential decay and with no gate.
- Results are reported over multiple random seeds with standard deviations.

**Concerns**
1. **Numerical inconsistencies in the reported improvements.**  
   From Table 1, the average Recall@20 values are approximately:
   - LightGCN: \((0.1052+0.0634+0.0815)/3=0.08337\)
   - SGL: \((0.1078+0.0652+0.0841)/3=0.08570\)
   - SeqGate: \((0.1104+0.0662+0.0857)/3=0.08743\)

   Thus, SeqGate improves over LightGCN by approximately **4.9%**, not 4.6%, and over SGL by approximately **2.0–2.5%** depending on rounding, rather than 2.1% exactly. These are not large discrepancies, but they undermine confidence in the analysis.

2. **Potentially unfair baseline tuning.**  
   SeqGate is tuned over 60 configurations per dataset, whereas baselines use hyperparameters from original papers or official code. This does not establish a fair comparison, particularly for SGL and TiSASRec, whose performance can be sensitive to tuning and data preprocessing.

3. **Insufficient statistical testing.**  
   Five seeds and standard deviations are useful, but no paired significance tests or confidence intervals are provided. Given the relatively small absolute gains, it is unclear whether the improvements are statistically reliable.

4. **Incomplete experimental details.**  
   The paper does not specify negative sampling, exact early-stopping patience, initialization, graph normalization after gating, hardware, or the precise evaluation protocol for users with insufficient interactions. These omissions reduce reproducibility.

5. **The claimed cost analysis is not well justified.**  
   Interaction ages are fixed, and gate computation is a simple scalar function. The paper states that gate values are recomputed at every step but does not report hardware, wall-clock measurements, or whether the overhead includes all training components. The 9% figure is therefore difficult to assess.

6. **The “session-aware” characterization is overstated.**  
   SeqGate uses elapsed time but does not model sessions, session boundaries, within-session order, or contextual transitions. It is better described as a time-aware or recency-aware graph model.

7. **Limited ablation scope.**  
   The experiments do not isolate whether gains arise from the learned functional form, the use of edge weights, or simply a global recency prior. Additional comparisons are needed, such as:
   - fixed scalar or linear decay,
   - learned monotonic decay,
   - user-specific or dataset-specific decay,
   - gates based on item-side versus user-side age,
   - gates without the extra nonlinear parameterization.

### Novelty: **35/100**

The core idea—using interaction age to weight messages in graph collaborative filtering—is intuitive and closely related to existing temporal graph convolution, time-decay collaborative filtering, temporal attention, and edge-weighted message-passing methods. The proposed gate is a small neural parameterization of a scalar decay function, with only four shared parameters. That makes the method simple, but the conceptual novelty is limited.

The related-work discussion is also too narrow. It mentions fixed exponential decay and generic gated graph networks but does not adequately distinguish SeqGate from prior temporal GNNs, dynamic graph recommenders, time-aware LightGCN variants, or learned edge-decay methods. The paper would need a substantially stronger literature review and more direct comparisons to establish novelty.

### Significance: **45/100**

The method is attractive because it is simple, efficient, and potentially easy to integrate into graph-based recommendation systems. The reported gains are consistent across datasets, and the larger improvement for users with long histories is plausible and practically relevant.

However, the gains are modest, and the evaluation is limited:
- only three datasets,
- all from e-commerce,
- only leave-one-out offline evaluation,
- no online or industrial-scale evidence,
- no robustness analysis across different temporal horizons,
- no comparison with strong modern temporal or sequential baselines beyond TiSASRec.

The method may be useful as an incremental improvement, but the current evidence does not establish broad or substantial significance.

### Clarity: **76/100**

The paper is generally well organized and readable. The model description, tables, and claimed contributions are easy to follow. The paper is concise without major stylistic problems.

Clarity is reduced by:
- the use of “session-aware” for a model without explicit session modeling,
- insufficient details about graph normalization and training,
- unclear baseline tuning procedures,
- unsupported or inconsistent percentage calculations,
- limited explanation of how the gate interacts with LightGCN normalization.

## Score Summary

| Criterion | Score |
|---|---:|
| Soundness | 50 |
| Novelty | 35 |
| Significance | 45 |
| Clarity | 76 |
| **Final average** | **51.5/100** |

## Final Recommendation: **Reject**

The paper presents a plausible and clean baseline-level idea, but the current version does not sufficiently establish novelty or experimental reliability. The recommendation could improve with fair retuning of all baselines, corrected aggregate statistics, stronger temporal comparisons, significance testing, a fuller ablation study, detailed reproducibility information, and more accurate positioning as a time-aware rather than session-aware model.