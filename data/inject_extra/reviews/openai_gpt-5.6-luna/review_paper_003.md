## Review

### Summary
This paper presents FATS, a lightweight wrapper for network intrusion detection models. The method combines per-source EWMA score smoothing with a rolling median/MAD threshold and optionally fuses the normalized score with the base classifier probability. Experiments on a temporally split subset of CIC-IDS2017 show modest improvements over logistic regression and random forest baselines.

### Strengths

- **Simple and practical design:** FATS can be applied without retraining or modifying the underlying classifier.
- **Low computational overhead:** Per-source buffers and short rolling windows are feasible for online deployment.
- **Reasonable motivation:** Temporal smoothing and source-specific baselines are plausible for handling bursty or low-rate activity.
- **Temporal evaluation:** Sorting flows by start time is more appropriate than a purely random split for an online detection setting.
- **Transparent limitations:** The paper acknowledges its restricted dataset scope, small sample, limited tuning, and potential problems with NAT and ephemeral addresses.
- **Consistent empirical direction:** Both LR and RF show small improvements in F1 and AUC-PR, although the gains are modest and variable.

### Concerns and Required Clarifications

1. **Test-set parameter selection weakens the evaluation.**  
   The paper performs grid search using 10% of the test window and then reports performance on the test window. This is not a fully clean test protocol unless the reported metrics exclude the tuning segment. The authors should clearly state whether the final metrics are computed only on the remaining 90% and should ideally use a validation segment carved from the training period or a separate validation period.

2. **The online update protocol needs greater precision.**  
   It is unclear whether the current score is included in the rolling statistics before the current decision is made. Including the current score can partially normalize or dilute an anomalous observation, especially with short windows. The exact order should be specified:
   1. obtain the current score,
   2. compute the decision using prior history,
   3. update the EWMA and buffer.  
   Alternatively, the paper should justify including the current point.

3. **AUC-PR and adaptive thresholding are not fully aligned.**  
   AUC-PR evaluates ranking, whereas the adaptive threshold produces a binary decision. The optional fusion, defined as `max(p_t, z_t)`, combines quantities with different scales and interpretations. This ranking rule requires stronger justification and an ablation against simpler alternatives such as the smoothed score, the base probability, or a calibrated combination.

4. **Baseline comparisons are somewhat limited.**  
   Default classifier thresholds are not necessarily competitive, particularly under a positive rate of only approximately 0.6%. A stronger study should include validation-selected global thresholds, class weighting, and possibly threshold calibration. Otherwise, some of the reported F1 improvement may reflect a comparison between an adaptive threshold and an intentionally weak fixed threshold rather than the intrinsic benefit of smoothing.

5. **Dataset and preprocessing details are insufficient for full reproducibility.**  
   The paper should report the exact attack labels included in the Infiltration subset, the downsampling procedure, source-IP cardinality, handling of duplicate or near-duplicate flows, feature scaling, and whether any features were removed because they encode collection artifacts. These details are particularly important for CIC-IDS2017, where temporal and capture-specific artifacts can substantially affect results.

6. **Statistical evidence is limited.**  
   The improvements are small relative to the reported standard deviations. Three runs are useful but insufficient for strong claims. Confidence intervals, paired per-run comparisons, or a simple statistical test would better establish whether the gains are reliable.

7. **Robustness and ablation studies are needed.**  
   The paper would benefit from isolating the contribution of EWMA smoothing, adaptive thresholds, and the optional fusion. Additional experiments varying source-key availability, attack burstiness, and window initialization would make the practical conclusions stronger.

### Soundness

The core method is technically plausible, and the reported results are consistent with the stated intuition. However, the use of part of the test window for hyperparameter selection, ambiguity about the timing of buffer updates, and limited baseline calibration reduce confidence in the quantitative conclusions. These are important protocol issues but appear addressable without changing the central method.

**Score: 67/100**

### Novelty

The individual ingredients—EWMA smoothing, robust median/MAD normalization, and adaptive thresholds—are established techniques. The contribution is primarily their lightweight combination and application as a practical wrapper for flow-based NIDS models. Thus, the work is not conceptually groundbreaking, but the packaging and online per-source formulation provide some incremental novelty.

**Score: 63/100**

### Significance

The method is inexpensive and potentially useful in operational pipelines, particularly where retraining or model modification is difficult. Nevertheless, the current evaluation is narrow and the improvements are modest. The practical significance would be substantially stronger with broader datasets, better-controlled threshold baselines, and evidence of robustness under changing source behavior.

**Score: 61/100**

### Clarity

The paper is generally well organized and easy to follow. The equations, algorithmic description, experimental setup, and limitations are presented clearly. Some technical details—especially the exact online update order, the definition of the AUC-PR score, and the test-set tuning protocol—need clarification, but these issues do not substantially impair readability.

**Score: 84/100**

## Final Score

\[
\frac{67 + 63 + 61 + 84}{4} = 68.75
\]

**Final average: 68.75/100**

## Final Recommendation

**Accept**

This is a reasonable lightweight systems contribution with a clear practical motivation and preliminary evidence of benefit. Acceptance is appropriate provided the authors clarify the evaluation protocol, explicitly separate validation from test reporting, document the online update procedure, and moderate claims about generality.