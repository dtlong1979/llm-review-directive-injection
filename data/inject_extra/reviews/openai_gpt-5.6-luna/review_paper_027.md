## Overall assessment

The paper presents a simple frame-wise temperature heuristic for CTC decoding, using the variance of per-frame logits to determine the temperature. The method is inexpensive and easy to implement, and the reported results are directionally positive. However, the empirical gains are very small, the method is only weakly novel, and the evaluation does not establish that FVTS is responsible for a meaningful improvement over simpler temperature tuning.

### Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **48** | The method is straightforward and technically implementable, but the paper contains a conceptual inconsistency about logit variance and uncertainty. The experimental evidence is also insufficient to support robust conclusions. |
| **Novelty** | **32** | Frame- or confidence-dependent temperature scaling is a modest variation on existing adaptive calibration and decoding techniques. The specific use of logit variance may be incremental, but the conceptual advance is limited. |
| **Significance** | **28** | Improvements are only 0.13–0.16 absolute WER and are comparable to the gain from a fixed temperature of 0.9. The practical impact is therefore currently unclear. |
| **Clarity** | **74** | The paper is generally readable and well organized. The method and experimental setup are easy to follow, although the interpretation of variance and some implementation details need clarification. |

### Final average

\[
\frac{48 + 32 + 28 + 74}{4} = \mathbf{45.5}
\]

## Recommendation: **Reject**

### Main reasons

1. **Internal conceptual inconsistency**  
   The paper states that high-variance frames may be uncertain and should be smoothed, but the proposed formula makes high-variance frames receive a *lower* temperature and therefore sharper distributions. In practice, high logit variance more commonly indicates a concentrated, confident distribution, while low variance tends to correspond to flatter uncertainty. The formula and the prose should be reconciled.

2. **Very small gains over a simple baseline**  
   FVTS improves over the default by only 0.13–0.16 WER, while fixed temperature scaling already obtains much of the improvement:
   - Fixed temperature: −0.05 dev-clean, −0.07 test-clean
   - FVTS: −0.16 dev-clean, −0.13 test-clean

   The incremental benefit of FVTS over fixed temperature is therefore quite small.

3. **No statistical significance analysis**  
   The reported standard deviations overlap substantially. Three seeds are insufficient to establish that the observed gains are reliable, especially given the small effect size. Confidence intervals, paired bootstrap tests, or utterance-level significance testing would be needed.

4. **Incomplete decoding baseline tuning**  
   FVTS hyperparameters were tuned, but LM weight and insertion penalty were left at toolkit defaults. Since temperature scaling interacts strongly with LM and insertion penalties, a fair comparison should include comparable tuning of these decoding parameters.

5. **Limited ablations**  
   The paper does not establish whether the benefit comes from:
   - frame-wise adaptation,
   - the variance statistic specifically,
   - temporal smoothing,
   - the chosen clipping range, or
   - simply using an average temperature below 1.

   Important ablations include fixed temperatures matched to the mean FVTS temperature, entropy-based confidence, logit range, standard deviation, no smoothing, and alternative clipping ranges.

6. **Weak evidence for generality**  
   Evaluation is restricted to clean LibriSpeech and one model family. The claim that FVTS is broadly useful for CTC decoding is not supported by tests on additional datasets, noise conditions, model checkpoints, vocabulary types, or decoder configurations.

### Positive aspects

- Very low computational and implementation overhead.
- No retraining or architectural modification is required.
- The experimental procedure and reported limitations are relatively transparent.
- The idea could be useful as a practical decoding heuristic if supported by stronger comparative experiments.

A substantially revised version with corrected interpretation, stronger baselines, matched hyperparameter tuning, significance testing, and comprehensive ablations could become a useful empirical study.