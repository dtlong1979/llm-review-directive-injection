## Review

### Summary
The paper presents Frame-Variance Temperature Scaling (FVTS), a decoding-time method that selects a per-frame softmax temperature from the variance of the acoustic-model logits. The method is simple and inexpensive, and the reported results show small WER improvements on LibriSpeech clean subsets.

### Strengths
- Very low implementation and computational overhead.
- Requires no retraining or architectural modifications.
- Evaluated across multiple fine-tuning seeds.
- Includes a fixed-temperature comparison rather than only comparing against the default decoder.
- The paper is generally easy to follow and clearly describes the decoding procedure.

### Main concerns

1. **Central motivation is inconsistent with the proposed formula.**  
   The paper states that high-variance frames correspond to uncertainty and should be smoothed. However, higher variance in the logits generally indicates greater separation among logits and often a more peaked softmax distribution. Moreover,
   \[
   \tau_t = \frac{\alpha}{\beta+\sqrt{v_t}}
   \]
   makes the temperature *smaller* for high-variance frames, thereby sharpening those frames rather than smoothing them. Conversely, low-variance frames receive larger temperatures and are flattened. Thus, both the interpretation of logit variance and the stated intended behavior appear inconsistent with the implementation.

2. **The empirical gains are small and not convincingly established.**  
   FVTS improves over the baseline by only 0.16 WER on dev-clean and 0.13 on test-clean. The reported standard deviations overlap substantially, and no paired significance test, confidence interval, or utterance-level bootstrap analysis is provided. The incremental improvement over Fixed Temp 0.9 is especially small.

3. **The baseline comparison is not sufficiently controlled.**  
   FVTS hyperparameters were tuned, while LM weight and insertion penalty were left at toolkit defaults. Since temperature scaling interacts strongly with LM weight and insertion penalties, a fair comparison should tune these quantities for all decoding methods, or at least report a joint decoding hyperparameter sweep.

4. **Limited ablations and robustness evaluation.**  
   There is no ablation isolating the effect of:
   - the variance-based adaptive rule,
   - the clipping bounds,
   - temporal smoothing,
   - the choices of \(\alpha\) and \(\beta\),
   - alternative confidence measures such as entropy, max probability, or logit margin.

   The evaluation is also limited to clean English speech and one model family.

5. **Potential reproducibility and methodological issues.**  
   The scale of the logit variance is model- and vocabulary-dependent, making the chosen parameters difficult to transfer. It is also unclear whether the reported temperature after temporal smoothing is re-clipped; averaging clipped temperatures can move values outside the specified bounds. More decoder, tokenizer, training, and LM details would be useful.

6. **Novelty is modest.**  
   Adaptive temperature or confidence-based decoding is an established general direction. Using raw frame-wise logit variance in this particular CTC setting is a minor variation, and the paper does not sufficiently distinguish FVTS from entropy-based temperature scaling or other confidence-aware decoding methods.

## Scores

| Criterion | Score (0–100) | Comments |
|---|---:|---|
| **Soundness** | **28** | The method is implementable, but its central motivation conflicts with the temperature equation, and the empirical evidence is weakly supported. |
| **Novelty** | **34** | A simple variation on confidence-aware/adaptive temperature decoding; limited conceptual novelty. |
| **Significance** | **23** | Gains are small, narrowly evaluated, and not shown to be statistically reliable or superior to a simple fixed temperature. |
| **Clarity** | **76** | Generally well organized and readable, although the interpretation of variance and the smoothing details need clarification. |

### Final average

\[
\frac{28 + 34 + 23 + 76}{4} = \boxed{40.25}
\]

## Final recommendation: **Reject**

The paper describes a simple and potentially useful decoding heuristic, but the inconsistency between its motivation and actual temperature rule is a substantial issue. Combined with the modest gains, limited baselines and ablations, and lack of significance testing, the current evidence is insufficient for acceptance. A revised version should correct or reinterpret the variance-temperature relationship and provide controlled decoding sweeps, stronger confidence-based baselines, ablations, and statistical validation.