# Peer Review: SeqGate: Time-Gated Graph Convolution for Session-Aware Recommendation

## Summary

This paper proposes SeqGate, a modification to LightGCN that incorporates temporal information into graph-based collaborative filtering. The key idea is to scale messages during propagation by a learned time gate that depends on the elapsed time since each interaction. The method is evaluated on three e-commerce datasets and shows improvements over LightGCN and other baselines.

---

## Detailed Assessment

### Soundness: 72/100

**Strengths:**
- The core methodological approach is sound: using a learned gate function to weight edges by interaction recency is a reasonable design choice
- Experimental methodology is generally solid: five random seeds with mean/std reported, proper train/validation/test splits
- The time gate formulation (log-transformed elapsed days with two-layer MLP) is simple and interpretable
- Ablation studies appropriately validate the contribution of the time gate component

**Weaknesses:**
- **Limited theoretical motivation**: Why is this specific gate formulation (log(1+Δ) through two-layer MLP) better than alternatives? No justification provided
- **Incomplete experimental controls**: 
  - SeqGate hyperparameters tuned via grid search (60 configurations) while baselines use "recommended" settings—this could bias results in SeqGate's favor
  - No mention of tuning effort/computational cost for baselines
- **Missing analysis of learned gates**: What do the learned w1, w2, b1, b2 values look like? Do they encode monotonic decay? This would strengthen understanding
- **Temporal data leakage concerns**: The gate uses "elapsed time... measured from the end of the training period." This is clear, but the interaction of this with the validation/test split deserves more careful discussion
- **Statistical significance**: While standard deviations are reported, no significance tests (t-tests) are provided to verify that improvements are statistically meaningful. Some improvements are small relative to std devs

### Novelty: 58/100

**Strengths:**
- Combining time-aware weighting with graph convolution is a straightforward contribution
- The approach is simpler than sequential methods (GRU4Rec, SASRec) while addressing similar limitations of static graphs
- The specific instantiation (learned gate vs. fixed decay) is somewhat novel

**Weaknesses:**
- **Limited conceptual novelty**: The idea of weighting edges by interaction recency is not new (acknowledged with "exponential decay" baselines). The contribution is primarily engineering: replacing hand-set decay with learned parameters
- **Narrow scope**: Adding a learned scalar gate to LightGCN is an incremental modification, not a fundamental algorithmic advance
- **Limited exploration of design space**: Why only sigmoid-gated messages? Why not edge-wise gates (requiring more parameters)? Why not attention-based approaches? No justification for design choices
- **Prior work on gating underexplored**: The paper mentions gated graph networks and graph attention but doesn't clearly position the difference from prior gating mechanisms

### Significance: 68/100

**Strengths:**
- The improvement is consistent across three datasets and both metrics (R@20 and NDCG@20)
- The method is practical: only ~9% training time overhead and 4 additional parameters
- Results on long-history users (7.9% improvement) suggest the method addresses a real pattern in user behavior
- E-commerce recommendation is a high-impact application

**Weaknesses:**
- **Modest absolute improvements**: 4.6% over LightGCN and 2.1% over the strongest baseline (SGL) are respectable but not transformative
- **Narrow evaluation scope**: 
  - Only three datasets, all from e-commerce domain
  - Authors acknowledge "results may differ for domains such as news or music where interest changes faster"
  - No online A/B test results, which is critical for practical impact claims
- **Comparison fairness**: TiSASRec, which also incorporates time information, is underperformed here. It's unclear why a temporal attention model underperforms. More analysis needed
- **Limited real-world validation**: Leave-one-out evaluation is standard but doesn't capture real deployment scenarios (e.g., repeated exposure, diversity, fairness)

### Clarity: 82/100

**Strengths:**
- Paper is well-written and easy to follow
- Experimental setup is clearly described
- Main results table is informative
- Method section is concise
- Limitations are explicitly acknowledged

**Weaknesses:**
- **Missing implementation details**:
  - How is the "weighted sum" of layer outputs computed in the final representation? Are weights learned or fixed?
  - What is the initial value for w1, w2 in the "gate initialisation" that is tuned?
  - Code availability not mentioned (reproducibility concern)
- **Insufficient analysis of learned behavior**: The paper would benefit from visualizing how gate values vary with interaction age, or showing example learned parameters
- **Ablation presentation**: Table 2 lacks error bars, making it hard to assess significance of differences (e.g., 0.0874 vs. 0.0853)
- **Related work presentation**: The "Gating in graph neural networks" paragraph is quite short and could more clearly distinguish SeqGate from prior work

---

## Detailed Comments

1. **Method design**: Why log(1+Δ) specifically? Have you tried sqrt(Δ) or other transformations? Ablation on this would strengthen the paper.

2. **Baseline comparison**: The grid search over 60 configurations for SeqGate vs. "recommended hyperparameters" for others is a potential source of bias. Did you tune baseline hyperparameters to the same extent?

3. **TiSASRec underperformance**: TiSASRec incorporates explicit time information but underperforms LightGCN on some metrics. Why? This deserves investigation—it challenges the narrative that the problem is important.

4. **Gate analysis**: Table 2 shows fixed exponential decay achieves 0.0853 vs. learned 0.0874. Is the learned decay substantially better, or is the difference within noise? Significance testing would clarify.

5. **Generalization**: The largest gains are for long-history users (7.9%). What is the user distribution? Are most users short-history? This affects practical impact.

6. **Scalability**: What is the memory overhead? How does SeqGate scale to billion-scale graphs?

---

## Minor Issues

- Abstract: "keeps training time within 9% of LightGCN" is a bit awkward; suggest "increases training time by 9%"
- Section 3: "session-aware" in the title, but sessions aren't explicitly modeled—only elapsed time
- Table 1: Would benefit from bold formatting or star notation for statistical significance
- Figure/visualization missing: A plot of gate values vs. interaction age would greatly aid interpretation

---

## Missing Experiments

1. Hyperparameter tuning parity: Tune baselines equally, report results
2. Significance tests: t-tests or bootstrap CIs for main results
3. Gate behavior visualization: Show learned decay curves
4. Domain generalization: Evaluate on non-e-commerce data (news, music, movie) to test claims about generalizability
5. Online evaluation: A/B test in production system
6. Analysis of learned parameters: What values do w1, w2 actually take?

---

## Questions for Authors

1. How sensitive is SeqGate to the choice of time encoding (log vs. alternatives)?
2. Why does the fixed exponential decay baseline perform quite well (0.0853), suggesting the learned component is only marginally better?
3. Have you tested on datasets without temporal information to see if SeqGate hurt performance?

---

## Overall Assessment

This is a competent incremental contribution that shows consistent empirical improvements on a practical problem. The method is simple, efficient, and addresses a real limitation of static graph models. However, the novelty is limited (learned gate to replace fixed decay), the improvements are modest relative to the strongest baseline, and the evaluation is narrow in scope (e-commerce only, no online validation).

The paper makes a solid engineering contribution but falls short of being a significant research advance. It would be suitable for a workshop or applications track but is borderline for a top-tier venue.

**Strengths summary:** Clear writing, sound methodology, consistent improvements, practical efficiency
**Weaknesses summary:** Limited novelty, modest gains, narrow domain, incomplete controls, missing analysis

---

## Scoring

| Category | Score | Justification |
|----------|-------|---------------|
| **Soundness** | 72 | Generally sound, but hyperparameter tuning imbalance and missing significance tests are concerns |
| **Novelty** | 58 | Incremental: learned gate for edge weighting is straightforward, narrow design space exploration |
| **Significance** | 68 | Consistent improvements but modest (2–4%), limited to e-commerce, no online validation |
| **Clarity** | 82 | Well-written but missing implementation details and gate behavior analysis |
| **Average** | **70** | |

---

## Final Recommendation

**BORDERLINE REJECT** (leaning toward reject for a top conference, suitable for workshop/applications venue)

The paper presents competent work with solid experimental results, but the contribution is incremental and the evaluation is narrow. Key concerns are: (1) modest improvements over strong baselines, (2) unclear if gains are due to hyperparameter tuning advantage, (3) evaluation limited to e-commerce domain despite claims of addressing a general temporal pattern, and (4) lack of online validation for a high-impact application area. The work would be strengthened by parity in hyperparameter tuning, significance testing, analysis of learned gate behavior, and evaluation on diverse domains and in production settings.

For acceptance at a selective venue, I would recommend: addressing hyperparameter tuning parity, adding statistical significance tests, visualizing learned gate behavior, and evaluating on at least one non-e-commerce dataset before resubmission.