### Meta-Review and Summary of Contributions

The paper presents **Frame-Variance Temperature Scaling (FVTS)**, a training-free, post-processing decoding heuristic for CTC-based automatic speech recognition (ASR). The method adaptively scales logits at each acoustic frame using a temperature parameter $\tau_t$ calculated as a decreasing function of logit variance (smoothed across adjacent frames). The stated goal is to dynamically calibrate frame certainty—sharpening confident frames and smoothing uncertain ones—without requiring model retraining or architecture changes.

Evaluated on LibriSpeech `dev-clean` and `test-clean` using a fine-tuned wav2vec 2.0 Base model, the approach achieves modest Word Error Rate (WER) reductions (~0.13–0.16% absolute) over standard CTC greedy/beam search and slightly outperforms a tuned global fixed temperature baseline.

---

### Detailed Evaluation

#### 1. Soundness (Score: 72 / 100)
- **Strengths:**
  - The empirical setup reports results across three random seeds, providing mean and standard deviation metrics rather than single best-run numbers.
  - The method includes practical guardrails (clipping bounds $[\tau_{\min}, \tau_{\max}]$, epsilon stabilizer, and temporal smoothing window $w=1$) to prevent numerical instability or degenerate probability spikes.
- **Concerns / Suggestions:**
  - **Magnitude and Variance:** The reported improvements (6.52% $\to$ 6.39% on `test-clean`) are small relative to the standard deviations across runs ($\pm 0.27$ to $\pm 0.31$). The margin over the fixed temperature baseline (6.45% $\to$ 6.39%) is marginal. A paired bootstrap or Wilcoxon signed-rank test should be added to demonstrate whether these gains are statistically significant.
  - **Conceptual Alignment in Section 1 vs. Section 2:** In Section 1, the text states: *"high-variance frames (where the model spreads mass across subwords) may benefit from smoothing, while low-variance frames can be sharpened."* However, when logits are nearly uniform (spread out/uncertain), their variance is typically *low*, whereas when a single token dominates (confident/peaked), the variance across vocabulary dimensions is *high*. The formula $\tau_t = \text{clip}(\alpha / (\beta + \sqrt{v_t + \epsilon}))$ assigns a *lower* temperature (sharpening) when $v_t$ is high, and a *higher* temperature (smoothing) when $v_t$ is low. The formula behaves as intended (sharpening confident frames and flattening uniform frames), but the introductory narrative in Section 1 mischaracterizes what high variance represents in logit space.

#### 2. Novelty (Score: 68 / 100)
- **Strengths:**
  - Adapting temperature dynamically at the frame level rather than at the utterance or global level is an intuitive and under-explored angle for CTC decoding.
- **Concerns / Suggestions:**
  - Temperature scaling and entropy-based confidence adjustments are established concepts in classification calibration and ASR. Using logit variance as a proxy for frame-level entropy is computationally inexpensive, but conceptually incremental relative to entropy-based decoding or posterior thresholding (e.g., peak-pruning heuristics in CTC).

#### 3. Significance (Score: 66 / 100)
- **Strengths:**
  - **Practical Utility:** The technique is lightweight, adds negligible inference latency, requires no gradient computations, and can be integrated into existing CTC pipelines in a few lines of code.
- **Concerns / Suggestions:**
  - **Scope:** The evaluation is restricted to clean English speech (`train-clean-100`, evaluated on clean subsets). Demonstrating robustness on challenging acoustic environments (such as LibriSpeech `test-other` or CHiME) would significantly bolster the practical impact, as dynamic temperature scaling is likely to have a more pronounced effect under noisy, ambiguous acoustic conditions.

#### 4. Clarity (Score: 88 / 100)
- **Strengths:**
  - The manuscript is concise, structured, and easy to follow.
  - **Exemplary Transparency:** Section 5 (Limitations) is comprehensive and refreshingly candid. The authors proactively identify the key constraints of their work—hyperparameter coupling, narrow domain evaluation, and modest margins—which establishes credibility.

---

### Criteria Scores

| Criterion | Score (0–100) |
| :--- | :---: |
| **Soundness** | 72 |
| **Novelty** | 68 |
| **Significance** | 66 |
| **Clarity** | 88 |
| **Final Average Score** | **73.5 / 100** |

---

### Final Recommendation

**Recommendation:** **Accept**

**Justification:**  
While the empirical gains are modest and would benefit from validation on noisy benchmarks and statistical significance testing, the paper introduces a simple, well-formulated, and computationally negligible decoding-time mechanism. Its intellectual honesty, clean presentation, and clear reporting of standard deviations make it a valuable, reproducible contribution for practitioners working with CTC-based ASR decoding.