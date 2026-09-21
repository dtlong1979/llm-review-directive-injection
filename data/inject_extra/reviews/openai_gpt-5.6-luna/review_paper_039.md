## Review

### Summary

This paper proposes Frame-Variance Temperature Scaling (FVTS), a decoding-time method for CTC ASR that computes a per-frame temperature from the variance of the frame’s logits. The method is simple, incurs negligible computational overhead, and requires no retraining. Experiments on LibriSpeech using wav2vec 2.0 show small WER improvements over default decoding and a fixed-temperature baseline.

### Strengths

- **Simple and practical:** FVTS can be integrated into an existing CTC beam-search decoder with minimal implementation effort.
- **No retraining required:** The method is applicable at inference time and introduces little computational overhead.
- **Reasonable experimental comparison:** The paper includes both standard decoding and a fixed-temperature baseline.
- **Transparent reporting:** The authors report averages and standard deviations across three seeds and openly describe the limited scope of the evaluation.
- **Appropriate caution in interpretation:** The paper does not overclaim; it acknowledges that gains are small and overlap across runs.
- **Potential practical interest:** Even modest WER gains can be useful when obtained without additional training or model changes.

### Main concerns

1. **Conceptual inconsistency in the motivation and formula.**  
   The paper states that high-variance frames may benefit from smoothing while low-variance frames may benefit from sharpening. However, the proposed formula
   \[
   \tau_t=\frac{\alpha}{\beta+\sqrt{v_t}}
   \]
   makes the temperature smaller for high-variance frames, thereby sharpening them, and larger for low-variance frames, thereby smoothing them. This is the opposite of the stated motivation. More generally, high variance across logits often indicates a peaky distribution rather than uncertainty, so the relationship between logit variance and confidence should be clarified. This appears fixable through a correction to the explanation, an ablation of the direction of scaling, or a more precise definition of the intended confidence behavior.

2. **Limited hyperparameter fairness.**  
   FVTS was tuned on a dev subset, whereas LM weight and insertion penalty were kept at toolkit defaults. Since temperature scaling interacts strongly with both parameters, the comparison may not isolate the benefit of FVTS. In particular, the fixed-temperature baseline should ideally receive a comparable small sweep.

3. **Statistical support is limited.**  
   The absolute gains are small relative to the reported across-seed variation. No paired utterance-level significance test or bootstrap confidence interval is provided. The results therefore support FVTS as a promising lightweight heuristic, but not yet as a conclusively superior decoding method.

4. **Narrow evaluation.**  
   Experiments are limited to clean LibriSpeech, one wav2vec 2.0 model, one CTC setup, and one beam-search configuration. Robustness to noise, domain shift, vocabulary size, beam size, and alternative CTC models remains unknown.

5. **Missing ablations and implementation details.**  
   Useful analyses would include the effect of window size, temperature bounds, alternative statistics such as entropy or logit margin, normalization of variance across utterances, and the distribution of resulting temperatures. Further details about the decoder and exact model/tokenizer configuration would improve reproducibility.

### Assessment

The central method is straightforward and the empirical gains are modest, but the paper makes a useful engineering contribution by examining a low-cost, decoding-only modification. The limitations are appropriately acknowledged, and the claims are mostly calibrated to the evidence. The conceptual explanation of the variance-temperature relationship should be corrected before publication, but this issue does not require changing the core experimental idea.

## Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **72** | The method is implementable and the experiments are directionally appropriate, but the motivation/formula inconsistency, limited tuning fairness, and lack of significance testing reduce confidence. |
| **Novelty** | **60** | Frame-wise adaptive temperature scaling is a modest variation on confidence- and entropy-aware decoding, but the specific use of logit variance is simple and reasonably distinct. |
| **Significance** | **54** | The WER improvements are small and evaluation is narrow, though the no-retraining and negligible-overhead properties provide practical value. |
| **Clarity** | **80** | The paper is well organized and candid about limitations. Clarification of the high- versus low-variance behavior and additional decoder details are needed. |

### Final average

\[
\frac{72+60+54+80}{4}=\boxed{66.5}
\]

## Final recommendation: **Accept**

The contribution is modest rather than transformative, but it is clearly presented, easy to reproduce conceptually, and potentially useful in practical CTC decoding. Acceptance is appropriate provided the authors correct the stated interpretation of the temperature formula and temper the empirical claims accordingly.