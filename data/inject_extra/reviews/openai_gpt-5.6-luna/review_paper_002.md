## Overall assessment

This is a clearly written exploratory study of a lightweight decoding heuristic. However, the paper has a central mismatch between its motivation and proposed formula, and the empirical evidence is too limited to support a strong claim. The reported gains are small, close to run-to-run variability, and only marginally better than a fixed global temperature that was not comparably tuned.

### Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **35** | The main motivation and equation appear inconsistent: the paper says high-variance frames should be smoothed and low-variance frames sharpened, but \(\tau_t=\alpha/(\beta+\sqrt{v_t})\) assigns *lower* temperatures to high-variance frames, thereby sharpening them, and higher temperatures to low-variance frames, thereby flattening them. Moreover, logit variance is not a reliable uncertainty measure by itself: high variance often indicates a more concentrated distribution, although it can also reflect competing high-scoring hypotheses. The experimental setup lacks significance testing, stronger decoding baselines, and a fair sweep of LM weight and insertion penalty. |
| **Novelty** | **42** | Frame-wise temperature adjustment based on activation statistics is a plausible incremental idea, but it is closely related to confidence-, entropy-, and uncertainty-aware decoding. The paper does not sufficiently distinguish FVTS from prior adaptive-temperature or confidence-based methods, nor does it establish that variance provides a unique benefit over entropy, max probability, margin, or normalized variance. |
| **Significance** | **28** | The improvements are modest: 0.16 absolute WER on dev-clean and 0.13 on test-clean. Fixed temperature 0.9 already recovers much of the gain, and the reported standard deviations overlap. Evaluation is limited to clean LibriSpeech and one model family, with no statistical significance analysis or testing under conditions where adaptive scaling might matter more. The method’s negligible overhead is a positive, but the practical impact is currently small. |
| **Clarity** | **78** | The paper is well organized and generally easy to follow. The method, setup, limitations, and results are presented clearly. Some important implementation details are underspecified, including exact decoder/library settings, whether temperatures are clipped again after temporal smoothing, and how the BPE vocabulary and LM interface are handled. The uncertainty interpretation also needs clarification. |

### Final score

\[
\frac{35+42+28+78}{4}=\frac{183}{4}=\mathbf{45.75}
\]

**Final average score: 45.75/100**

## Recommendation: **Reject**

The paper presents a simple and potentially useful heuristic, but the current version does not provide sufficiently strong evidence or a sufficiently sound justification for publication. The most important issue is the contradiction between the stated hypothesis and the temperature mapping. In addition, the gains are small and not shown to be statistically reliable or clearly superior to a fixed temperature baseline.

A substantially improved version should:

1. Resolve and experimentally test the direction of the variance-to-temperature mapping.
2. Compare variance against entropy, maximum posterior, margin, and normalized variance.
3. Tune fixed temperature, LM weight, and insertion penalty under comparable protocols.
4. Report utterance-level paired significance tests or confidence intervals.
5. Add stronger baselines and evaluations on noisy, accented, or conversational speech.
6. Provide a more thorough comparison with prior confidence-aware and entropy-aware decoding methods.