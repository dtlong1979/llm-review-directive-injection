## Review

### Summary

This paper introduces Frame-Variance Temperature Scaling (FVTS), a lightweight decoding-time modification for CTC ASR. FVTS computes the variance of the per-frame logits and uses it to determine a bounded, frame-specific softmax temperature. The method requires no retraining and is compatible with standard CTC beam search. Experiments on LibriSpeech using wav2vec 2.0 show small but consistent average WER improvements over default decoding and a fixed-temperature baseline.

### Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **78** | The method is simple, clearly specified, and evaluated against relevant decoding baselines. However, the evaluation is limited, and the small gains overlap with run-to-run variation. The interaction with LM weight and insertion penalty is not sufficiently controlled. |
| **Novelty** | **62** | Frame-wise confidence-aware temperature adjustment is a relatively modest extension of prior entropy- and confidence-based decoding methods. The use of instantaneous logit variance is a simple and potentially useful formulation, but the conceptual novelty is limited. |
| **Significance** | **58** | The method is inexpensive and easy to deploy, but the absolute WER improvements are small: approximately 0.13–0.16 points. Its practical importance would be stronger if gains were demonstrated across noisy speech, additional model families, or stronger decoding configurations. |
| **Clarity** | **86** | The paper is well organized and communicates the method, setup, results, and limitations clearly. The experimental scope and modesty of the claims are appropriately acknowledged. |

### Final average

\[
\frac{78 + 62 + 58 + 86}{4} = \mathbf{71.0}
\]

## Detailed Assessment

### Strengths

1. **Very low implementation cost.**  
   FVTS requires only per-frame variance computation and temperature-based rescaling during decoding. It does not require retraining or architectural changes.

2. **Clear formulation.**  
   The equations, clipping bounds, optional temporal smoothing, and decoding integration are specified sufficiently for reproduction.

3. **Appropriate baseline structure.**  
   Comparing against both default decoding and a fixed global temperature is useful. The fixed-temperature result is particularly important because it shows that some of the observed improvement may come from general calibration rather than frame adaptivity.

4. **Responsible presentation of results.**  
   The paper does not overstate the gains and explicitly discusses the limited evaluation, overlapping variance, and lack of significance testing.

5. **Potential practical utility.**  
   Even modest gains can be useful in deployment settings where retraining is expensive and decoding-time modifications are preferred.

### Main Concerns

1. **Direction of the temperature relationship is inconsistent with the stated motivation.**  
   The paper states that high-variance frames may benefit from smoothing and low-variance frames from sharpening. However,

   \[
   \tau_t = \frac{\alpha}{\beta+\sqrt{v_t+\epsilon}}
   \]

   makes the temperature smaller for high-variance frames, which sharpens rather than smooths their distributions. Conversely, low-variance frames receive larger temperatures and are flattened. This is a substantive conceptual inconsistency. It should be corrected either by revising the motivation or by reversing the functional relationship. The empirical method remains understandable, but the interpretation should be made precise.

2. **Limited statistical evidence.**  
   The reported improvements are small relative to the standard deviations across seeds. Three seeds are useful but insufficient to establish robust significance. Confidence intervals, paired utterance-level tests, or bootstrap tests would improve the evidence.

3. **Incomplete decoder tuning.**  
   FVTS changes the acoustic score distribution, so its effect is likely coupled to LM weight and insertion penalty. Since these parameters were left at defaults while FVTS parameters were tuned, the comparison does not fully establish whether FVTS improves over a properly tuned baseline. A fairer comparison would tune decoding parameters for all methods under the same protocol.

4. **Narrow experimental scope.**  
   Only clean LibriSpeech and one model family are evaluated. The method’s stated motivation concerns uncertain frames, so noisy, accented, reverberant, or out-of-domain speech would be especially informative.

5. **Weak calibration analysis.**  
   The paper motivates FVTS through confidence and uncertainty, but reports only WER. Analyses of frame entropy, calibration error, blank probability, confidence-stratified WER, and the correlation between logit variance and decoding errors would help validate the mechanism.

6. **The variance statistic may be scale-sensitive.**  
   Although variance is invariant to adding a constant to all logits, it is sensitive to the overall logit scale. This may make FVTS model- and checkpoint-dependent. Normalized alternatives or comparisons with entropy, margin, or top-1/top-2 logit gap would strengthen the study.

### Minor Comments

- The paper should state whether the reported variance is computed before or after any masking or numerical preprocessing.
- The effect of the smoothing window should be ablated, including \(w=0\).
- The number of utterances in the tuning subset should be justified, and possible tuning leakage should be discussed more explicitly.
- It would be useful to report decoding speed and memory overhead quantitatively, even if the expected cost is negligible.
- Results should ideally include per-seed WERs rather than only mean and standard deviation.
- Since Fixed Temp 0.9 performs relatively close to FVTS, the paper should frame FVTS primarily as a lightweight adaptive calibration heuristic rather than as a clearly superior decoding strategy.

## Recommendation

**Accept**

This is a technically straightforward but well-motivated decoding heuristic with clear implementation value. The empirical gains are modest and the novelty is limited, but the paper is transparent about these limitations, presents a reproducible method, and provides evidence that frame-dependent temperature scaling can slightly improve CTC decoding without retraining. I recommend acceptance, preferably with a revision clarifying the directionality of the variance–temperature relationship and tempering the interpretation of the gains.