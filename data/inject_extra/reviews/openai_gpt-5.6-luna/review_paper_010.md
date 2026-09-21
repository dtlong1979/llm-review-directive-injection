## Review

### Summary

This paper proposes Frame-Variance Temperature Scaling (FVTS), a decoding-time method for CTC ASR that computes a per-frame temperature from the variance of the frame’s logits. The method is simple, requires no retraining, and is evaluated on LibriSpeech using a wav2vec 2.0 base model and CTC beam search. The reported gains are small but consistent on average across three seeds.

### Strengths

- **Simple and practical method:** FVTS can be integrated into an existing CTC decoder with minimal computational and implementation overhead.
- **No retraining required:** This makes the approach potentially useful for deployed systems where model fine-tuning is expensive or undesirable.
- **Reasonable initial evaluation:** The paper reports results on both dev-clean and test-clean and averages over three fine-tuning seeds.
- **Relevant comparison:** Including a fixed-temperature baseline is useful because it tests whether the gains arise merely from globally changing distribution sharpness.
- **Transparent limitations:** The paper appropriately acknowledges its narrow evaluation, limited baselines, and lack of significance testing.
- **Clear presentation:** The method, experimental setup, and scope are described concisely and are generally easy to follow.

### Concerns and requested clarifications

1. **Potential inconsistency in the motivation and formula.**  
   The paper states that high-variance frames are uncertain and should be smoothed. However,
   \[
   \tau_t = \frac{\alpha}{\beta+\sqrt{v_t}}
   \]
   makes the temperature smaller when variance is higher, which sharpens rather than smooths the distribution. Conversely, low-variance frames receive larger temperatures and are flattened. This is an important conceptual issue. The authors should either revise the motivation, reverse the functional relationship, or explain why the empirically useful behavior differs from the initial intuition.

2. **Logit variance is not a direct uncertainty measure.**  
   High variance may correspond to a highly confident frame with one dominant token, rather than an uncertain frame. The paper would benefit from an analysis relating variance to entropy, maximum posterior probability, blank probability, or frame-level error likelihood.

3. **Limited hyperparameter and decoding comparisons.**  
   FVTS was tuned over \(\alpha\) and \(\beta\), whereas LM weight and insertion penalty were not comparably tuned. Since temperature scaling can interact substantially with these parameters, the reported gains may not establish superiority over a properly optimized standard decoder. A small joint tuning experiment or a clearer statement that the comparison is against fixed default decoding would strengthen the conclusions.

4. **Insufficient ablations.**  
   Important ablations include:
   - no temporal smoothing versus \(w=1\);
   - alternative mappings from variance to temperature;
   - different temperature bounds;
   - variance normalized across utterances or vocabulary size;
   - entropy- or confidence-based temperature scaling;
   - a globally tuned temperature rather than only \(\tau=0.9\).

5. **Statistical evidence is limited.**  
   The improvements are modest relative to the standard deviations. Three seeds provide useful evidence, but utterance-level bootstrap confidence intervals or paired significance tests would help determine whether the gains are reliable. The paper should avoid implying broad effectiveness beyond the tested conditions.

6. **Reproducibility details could be expanded.**  
   The exact wav2vec 2.0 checkpoint, tokenizer/vocabulary construction, decoder implementation, LM training details, and precise default LM and insertion settings should be reported. These details are especially important because the absolute WERs and temperature behavior may depend strongly on the decoder configuration.

7. **Clarify implementation details.**  
   The paper should state whether variance is computed over all vocabulary logits including the blank symbol, whether it uses the unbiased estimator exactly as written, and whether temporal smoothing occurs before or after clipping. If smoothing occurs after clipping, the resulting temperature can in principle fall outside the stated bounds unless clipped again.

### Overall assessment

The contribution is modest but technically plausible and practically attractive. The empirical gains are small, and the current experiments do not yet demonstrate that FVTS is substantially better than a tuned fixed temperature or other confidence-based decoding heuristics. Nevertheless, the paper is clearly written, the method is easy to reproduce, and the reported results support a cautious claim that variance-based framewise scaling can provide a small decoding improvement in the tested CTC setting. The conceptual inconsistency concerning the direction of temperature adaptation should be corrected, but it is addressable without changing the core contribution.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 72/100 |
| Novelty | 55/100 |
| Significance | 57/100 |
| Clarity | 83/100 |

### Final average

\[
\frac{72+55+57+83}{4}=66.75
\]

## Final recommendation: **Accept**

This is an accept at a modest level of confidence. The contribution is incremental and the empirical improvements are limited, but the method is well motivated as a lightweight decoding modification, the evaluation is internally coherent, and the main weaknesses can be addressed through clarification and more careful qualification of the claims.