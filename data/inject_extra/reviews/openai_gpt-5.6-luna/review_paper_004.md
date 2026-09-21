## Overall assessment

This paper presents FATS, a lightweight post-processing method for network intrusion detection that combines per-source EWMA score smoothing with robust, source-specific thresholds based on rolling medians and MAD. The method is easy to understand, model-agnostic, and potentially useful in operational settings where source behavior varies over time.

The experimental results show modest but consistent average improvements over LR and RF baselines on the selected CIC-IDS2017 subset. However, the evaluation is narrow, and several protocol details require clarification before the empirical claims can be considered fully reliable. In particular, the treatment of temporal state across splits, the use of a test-window segment for parameter selection, the exact definition of AUC-PR for FATS, and the construction of per-source histories should be described more precisely.

Despite these limitations, the method is sufficiently clear, practical, and empirically promising for acceptance as a lightweight systems-oriented contribution, provided the authors strengthen the experimental documentation and qualify the claims.

## Scores

| Criterion | Score | Comments |
|---|---:|---|
| **Soundness** | **72/100** | The algorithm is internally plausible and the reported gains are consistent with the proposed smoothing intuition. However, the evaluation uses only one dataset subset and three downsampling runs. The protocol also leaves open potential issues involving test-set parameter selection, state initialization, and whether rolling windows include the current observation. These concerns reduce confidence in the magnitude and generality of the improvements, though they do not invalidate the basic method. |
| **Novelty** | **63/100** | EWMA smoothing, rolling medians, MAD-based thresholds, and adaptive anomaly detection are individually established techniques. The contribution is primarily their simple combination in a source-specific NIDS wrapper and the emphasis on model-independent deployment. This is incremental rather than fundamentally novel, but the integration is reasonable and practically motivated. |
| **Significance** | **66/100** | The method is computationally inexpensive and could be useful in streaming NIDS pipelines, particularly when per-source behavior differs substantially. The observed improvements are modest, and the study does not yet demonstrate robustness across datasets, attack families, network topologies, or deployment conditions such as NAT and source churn. Thus, the likely impact is practical and moderate rather than transformative. |
| **Clarity** | **84/100** | The paper is concise, well organized, and provides a clear description of the main equations, experimental setup, and limitations. Additional implementation details are needed, especially for state handling, score normalization, AUC-PR computation, and the exact interaction between the adaptive threshold and the optional ranking fusion. |

### Final average

\[
\frac{72 + 63 + 66 + 84}{4}
= \frac{285}{4}
= \mathbf{71.25/100}
\]

## Strengths

1. **Simple and practical design:** FATS can be added without modifying the underlying classifier.
2. **Appropriate operational motivation:** Per-source adaptation is relevant for heterogeneous traffic and host-specific baselines.
3. **Low computational cost:** The proposed window sizes and robust statistics are feasible for online use.
4. **Clear presentation:** The core algorithm and experimental comparisons are easy to follow.
5. **Useful empirical signal:** Both LR and RF show improvements in mean F1 and AUC-PR, although the gains are relatively small.

## Main concerns and requested clarifications

1. **Parameter selection and test-set usage:** The paper states that FATS parameters were selected using a 10% slice of the test window. This should be explicitly separated from the final evaluation segment, and the procedure should ensure that no labels or future observations from the evaluation portion influence thresholds or hyperparameters.

2. **Temporal state across train and test:** Please specify whether source-specific EWMA and rolling buffers are reset at the train/test boundary. If test-time state is initialized using training observations, this should be described; if it is reset, the resulting cold-start behavior should be reported.

3. **Current-sample inclusion:** The definition of the rolling window should clarify whether \( \bar e_t \) is included when computing \(m\) and \(b\). Including the current score can partially adapt the threshold to the event being classified and may alter detection behavior.

4. **AUC-PR definition for FATS:** A hard adaptive threshold produces binary decisions and cannot by itself support a meaningful precision-recall curve. The paper should state whether AUC-PR is computed from EWMA scores, normalized \(z_t\), the optional fused score, or another continuous quantity.

5. **Baseline fairness:** Default thresholds and default model hyperparameters are acceptable as a baseline, but an additional comparison with validation-selected global thresholds would help determine whether the gains arise from adaptive per-source behavior rather than simply improved threshold calibration.

6. **Broader validation:** Evaluation on additional CIC-IDS2017 days, other intrusion datasets, and varying source-key definitions would substantially strengthen the claims. Reporting results by attack type and source frequency would also help identify where FATS is effective.

## Recommendation

**Accept**

The contribution is incremental but well motivated, clearly presented, and potentially useful as a practical post-processing component for streaming NIDS. The paper should be accepted with revisions addressing the evaluation-protocol clarifications above and moderating claims about generality until broader experiments are available.