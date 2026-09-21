## Review

### Summary
The paper presents FATS, a wrapper that applies per-source EWMA smoothing and robust, source-specific thresholds based on rolling medians and MAD. The idea is lightweight and potentially practical, but the evaluation and algorithm specification have substantial weaknesses that make the reported gains difficult to interpret.

### Strengths
- Simple, model-agnostic method that could be integrated into existing NIDS pipelines.
- Uses robust statistics rather than mean and standard deviation, which may help with skewed traffic distributions.
- Temporal split is more realistic than a purely random split for online detection.
- The paper clearly states important limitations and reports variation across runs.

### Main concerns

1. **Potential test-set contamination**
   FATS hyperparameters are selected using a 10% slice of the test window. Unless the remaining 90% is treated as the only final evaluation set and this is explicitly reported, the test set is being used for model selection. This makes the reported performance optimistic.

2. **Unfair baseline comparison**
   The baselines use fixed default thresholds of 0.5, while FATS uses tuned, source-specific thresholds. Improvements in F1 may therefore reflect threshold optimization rather than the value of smoothing or adaptive normalization. Comparisons should include:
   - tuned global thresholds for LR and RF,
   - validation-based threshold selection,
   - possibly calibrated baselines,
   - and ablations for smoothing-only and adaptive-threshold-only variants.

3. **Algorithmic ambiguity**
   Several implementation details are underspecified:
   - Whether the current score is included in the rolling window before thresholding.
   - How thresholds are computed for new sources or sources with fewer than \(L\) observations.
   - How the first EWMA score is handled in evaluation.
   - What happens when MAD is nearly zero.
   - Whether the rolling buffer is maintained per source in strict event-time order.
   These details can materially affect results.

4. **Questionable score fusion**
   The proposed maximum of calibrated probability \(p_t\) and normalized score \(z_t\) combines quantities with different meanings and scales. A z-score can be negative or arbitrarily large, while a probability is bounded in \([0,1]\). Taking their maximum is not well justified and may distort ranking. The paper should define the exact transformation and evaluate fusion separately.

5. **Limited empirical evidence**
   Results come from one subset of one dataset, with only three downsampling seeds and approximately 40,000 flows. There are no confidence intervals, significance tests, per-source analyses, attack-type breakdowns, or comparisons with stronger thresholding and temporal baselines. The reported gains are modest and may not generalize.

6. **Insufficient ablation and reproducibility detail**
   The paper does not isolate the effects of EWMA, MAD thresholding, source grouping, or window length. Details about feature preprocessing, class handling, source cardinality, implementation of the rolling windows, and the exact evaluation code are also insufficient for reliable reproduction.

### Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **42** | Plausible method, but evaluation leakage, unfair threshold comparisons, and underspecified online behavior weaken the conclusions. |
| **Novelty** | **38** | The combination is practical, but EWMA smoothing, robust statistics, and adaptive thresholds are established techniques. The methodological novelty is limited. |
| **Significance** | **34** | The reported gains are small, based on a narrow dataset subset, and are not yet shown to be robust or broadly useful. |
| **Clarity** | **70** | Generally readable and well organized, though several important algorithmic and evaluation details are ambiguous. |

### Final average

\[
\frac{42 + 38 + 34 + 70}{4} = \mathbf{46.0}
\]

## Final recommendation: **Reject**

The paper describes a reasonable engineering heuristic, but the current evidence does not support the strength of its claims. A revised submission would need a leakage-free validation protocol, fair threshold-matched baselines, clear online algorithm definitions, ablations, stronger datasets or subsets, and a more principled treatment of score fusion.