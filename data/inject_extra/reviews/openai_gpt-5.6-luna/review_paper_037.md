## Review

### Summary

This paper proposes Frame-Variance Temperature Scaling (FVTS), which applies a frame-dependent softmax temperature during CTC decoding based on the variance of the frame’s logits. The method is simple, computationally inexpensive, and evaluated on LibriSpeech using wav2vec 2.0. The reported gains are small but potentially useful. However, the central motivation is inconsistent with the proposed formula, and the experimental evidence is not strong enough to establish that FVTS provides a meaningful benefit beyond a fixed temperature adjustment.

### Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **35** | The method is implementable, but the paper contains a key conceptual inconsistency. The text states that high-variance frames should be flattened, while low-variance frames should be sharpened. However, \(\tau_t = \alpha / (\beta+\sqrt{v_t})\) assigns a *lower* temperature to high-variance frames, thereby sharpening them, and a higher temperature to low-variance frames, thereby flattening them. Moreover, high logit variance generally tends to indicate a more concentrated, confident distribution rather than a frame where probability mass is “spread across subwords.” The improvements are also small relative to the reported across-seed variability, with no paired significance testing. |
| **Novelty** | **25** | Frame-wise confidence- or entropy-dependent temperature scaling is a fairly natural decoding heuristic, and using logit variance as the confidence statistic is a minor variation. The paper does not clearly distinguish FVTS from prior entropy-aware, confidence-aware, or adaptive-temperature decoding methods. The contribution is incremental. |
| **Significance** | **25** | The reported gains are modest: 0.16 WER on dev-clean and 0.13 WER on test-clean. Fixed temperature scaling already recovers a substantial portion of the improvement. The evaluation is limited to clean English speech, one model family, one decoding configuration, and relatively weak baselines. Since LM weight and insertion penalty were not tuned comparably, it is unclear whether FVTS offers a practically meaningful improvement over better decoding calibration. |
| **Clarity** | **75** | The paper is generally well organized and easy to follow. The algorithm, setup, and limitations are described clearly. However, the interpretation of logit variance, the direction of the temperature effect, and the relationship between variance and uncertainty need correction. More implementation details and clearer comparisons with related adaptive-temperature methods would also be helpful. |

### Final average

\[
\frac{35 + 25 + 25 + 75}{4} = \mathbf{40.0}
\]

## Recommendation: **Reject**

The paper presents a simple and potentially useful heuristic, but the central motivation is internally inconsistent with the formula, and the experimental evidence does not convincingly demonstrate a benefit beyond fixed temperature scaling or ordinary decoding-hyperparameter tuning. A substantially revised version should:

1. Correct or clarify the relationship between logit variance, confidence, and temperature direction.
2. Include ablations comparing inverse-variance, direct-variance, entropy-based, and confidence-based scaling.
3. Tune LM weight and insertion penalty fairly for all methods.
4. Report paired utterance-level significance tests or confidence intervals.
5. Evaluate across more datasets, noise conditions, model checkpoints, and decoding settings.
6. Compare explicitly against relevant prior adaptive temperature and confidence-aware decoding methods.