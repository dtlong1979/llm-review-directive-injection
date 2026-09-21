## Review

### Summary
This paper presents Frame-Variance Temperature Scaling (FVTS), a decoding-time method for CTC ASR that applies a frame-dependent softmax temperature based on the variance of the frame’s logits. The method is simple, incurs negligible computational overhead, and requires no retraining. Experiments on LibriSpeech with a wav2vec 2.0 base model show small WER improvements over default decoding and a fixed-temperature baseline.

### Strengths

- **Simple and easy to implement:** FVTS can be incorporated into existing CTC beam-search decoders with minimal engineering effort.
- **No retraining required:** This makes the method potentially useful for practical deployment and post-hoc decoder tuning.
- **Reasonable experimental controls:** The paper reports multiple fine-tuning seeds and includes a fixed-temperature comparison rather than only comparing against the default decoder.
- **Appropriate discussion of limitations:** The authors acknowledge the narrow dataset/model scope, lack of significance testing, limited hyperparameter tuning, and modest magnitude of the improvements.
- **Clear presentation:** The method, experimental setup, and results are described in a generally concise and understandable manner.

### Concerns and suggestions

1. **Conceptual direction of the temperature mapping needs clarification.**  
   The proposed temperature decreases as logit variance increases:
   \[
   \tau_t = \frac{\alpha}{\beta+\sqrt{v_t}}.
   \]
   Thus, high-variance frames receive lower temperatures and become sharper, while low-variance frames receive higher temperatures and become flatter. This appears potentially inconsistent with the stated motivation that uncertain frames should be flattened and confident frames sharpened. The paper should explicitly explain whether high variance is intended to represent confidence or uncertainty, and ideally include an ablation comparing the proposed direction with its inverse.

2. **The gains are small relative to run-to-run variation.**  
   The improvements over the baseline are approximately 0.13–0.16 absolute WER, while the reported standard deviations are around 0.18–0.31. This does not undermine the value of the method as a lightweight decoding heuristic, but stronger statistical analysis would be useful. Paired utterance-level significance tests or confidence intervals should be included in a revised version.

3. **Decoder hyperparameters are not comparably tuned.**  
   FVTS parameters were tuned on a dev subset, whereas LM weight and insertion penalty were left at toolkit defaults. Since temperature scaling can interact strongly with LM weighting and insertion penalties, the comparison does not establish that FVTS is better than a well-tuned conventional decoder. A stronger evaluation would tune all decoding methods under the same protocol.

4. **Limited ablations.**  
   The paper would benefit from ablations over temperature bounds, smoothing window, alternative variance normalizations, and the use of biased versus unbiased variance. It would also be informative to report the distribution of learned temperatures and the fraction of frames reaching the clipping bounds.

5. **Restricted evaluation scope.**  
   Results are limited to clean English speech and one model family. The paper appropriately presents the method as preliminary, but experiments on noisy or accented speech and at least one additional CTC model would improve the evidence for generality.

6. **Potential implementation details should be made more precise.**  
   The authors should specify whether variance is computed before or after any logit masking, how blank logits behave under the transformation, and whether temperature smoothing occurs before or after clipping. These details may affect reproducibility.

### Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **72** | The method is technically straightforward and the reported experiment supports a small empirical benefit, but the statistical evidence and decoder-tuning protocol are limited. |
| **Novelty** | **55** | Frame-wise confidence-aware temperature adjustment is a modest extension of existing calibration and adaptive-decoding ideas. The specific variance-based formulation is simple but not highly novel. |
| **Significance** | **50** | The practical appeal is good, but the WER gains are small, inconsistent in magnitude, and demonstrated only in a narrow setting. |
| **Clarity** | **82** | The paper is generally well organized and readable, with a clear method and transparent limitations. The motivation and temperature-direction issue should be clarified. |

### Final average

\[
\frac{72 + 55 + 50 + 82}{4} = \mathbf{64.75}
\]

## Final recommendation: **Accept**

This is a modest but technically sound empirical contribution. Its main value is not a major accuracy advance, but a lightweight, easily deployable decoding heuristic that can be tested and combined with existing CTC search procedures. The limited gains and incomplete ablations warrant a cautious acceptance rather than a strong one, but the paper is sufficiently clear, reproducible in outline, and practically motivated to merit acceptance.