## Overall assessment

The paper presents a simple and potentially useful post-processing wrapper for network intrusion detection. However, the core method is largely a combination of established techniques—EWMA smoothing, rolling robust statistics, and adaptive thresholding—and the experimental protocol leaves important questions about leakage, baseline fairness, metric computation, and reproducibility. The reported gains are modest and obtained on only one narrow dataset subset.

### Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **35** | The method is plausible, but the evaluation and algorithm specification have several weaknesses. |
| **Novelty** | **28** | The combination is packaged clearly, but EWMA smoothing, median/MAD normalization, and adaptive thresholds are individually well established. |
| **Significance** | **32** | The reported improvements are small, inconsistent, and demonstrated only on one subset of one dataset. |
| **Clarity** | **76** | The paper is generally readable and well organized, although important implementation and evaluation details are missing. |

### Final average

\[
\frac{35 + 28 + 32 + 76}{4} = \mathbf{42.75}
\]

## Recommendation: **Reject**

### Main reasons

1. **Potential evaluation leakage and protocol ambiguity**  
   FATS hyperparameters are selected using a slice of the test window. It is not clear whether that slice is excluded from the reported test metrics or whether test results include data used for tuning. The procedure also needs to specify whether per-source state is reset at the train/test boundary.

2. **Unfair baseline comparison**  
   FATS receives parameter selection, while the baselines use fixed default thresholds. Comparing FATS against untuned 0.5 thresholds is not a strong comparison, especially under a positive rate of only approximately 0.6%. Baselines should also receive threshold tuning using an equivalent validation protocol.

3. **Insufficiently specified online algorithm**  
   The behavior for new sources, sources with fewer than \(L\) observations, and windows containing only one or very similar scores is unclear. Including the current score in the rolling median/MAD calculation can also make the threshold self-influenced. These details can materially affect results.

4. **Questionable use of source-specific normalization**  
   Source IP may be unstable because of NAT, shared infrastructure, dynamic addressing, or attacker spoofing. More importantly, if the same source appears in both training and testing, source-specific behavior may introduce an unintended form of identity or temporal leakage. This should be explicitly controlled through source-disjoint or carefully defined chronological experiments.

5. **AUC-PR procedure is unclear**  
   The optional fusion rule takes the maximum of a calibrated probability and a normalized z-score, despite those quantities being on incompatible scales. It is not clear whether the reported AUC-PR uses raw probabilities, EWMA scores, normalized scores, or this fusion. Since AUC-PR depends on ranking, this choice must be precisely defined.

6. **Limited empirical evidence**  
   The evaluation uses one dataset subset, 40,000 downsampled flows, three runs, and only two base models. The gains—roughly 0.4–0.7 percentage points in F1 and 1.8 percentage points in AUC-PR—are modest relative to the reported standard deviations. No significance testing, confidence intervals, or per-run results are provided.

7. **Missing ablations and stronger baselines**  
   The paper should compare against:
   - EWMA smoothing alone;
   - fixed global thresholds tuned on validation data;
   - rolling median/MAD without EWMA;
   - global rather than per-source adaptive thresholds;
   - class-weighted or threshold-tuned LR/RF;
   - alternative temporal or source-based baselines.

8. **Reproducibility gaps**  
   The exact feature list, preprocessing, downsampling procedure, label handling, source-key definition, buffer initialization, metric implementation, and code are not supplied. These omissions make it difficult to verify the reported results.

The paper is clearly written and the engineering idea may be useful in practice, but the current evidence does not establish a sufficiently novel, reliable, or general contribution. A substantially revised version with leakage-controlled evaluation, fair threshold tuning, clearer algorithmic definitions, ablations, and broader datasets could become publishable.