## Overall assessment

SeqGate presents a simple modification to LightGCN in which interaction messages are scaled by a learned function of interaction age. The idea is intuitive and potentially useful, and the paper is generally readable. However, the empirical evidence and methodological description are insufficient to support the claims. The gains over LightGCN and SGL are relatively small, the experimental comparison is not clearly fair, and several important implementation and evaluation details are missing. The “session-aware” characterization is also not justified because the model does not model sessions or interaction order beyond a scalar age feature.

## Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **45** | The core method is plausible, but the paper omits crucial details about weighted normalization, preprocessing, negative sampling, early stopping, and evaluation. Baseline tuning appears asymmetric, and no statistical significance testing is provided. The reported improvements are modest and may not be robust. |
| **Novelty** | **52** | Learning a time-dependent edge weight in a graph recommender is a reasonable incremental contribution, but it is close to existing time-decay, temporal graph, and edge-gating approaches. The four-parameter scalar gate is simple, though the paper does not establish a substantial conceptual advance over learned decay or temporal edge weighting. |
| **Significance** | **48** | If reliable, the method could offer a low-cost improvement to LightGCN. However, improvements over LightGCN are small, and the experiments are limited to three e-commerce datasets under one leave-one-out protocol. There is no online evaluation or evidence that the approach generalizes to domains with different temporal dynamics. |
| **Clarity** | **70** | The paper is well organized and easy to follow at a high level. Nevertheless, the algorithmic specification is incomplete, and terminology such as “session-aware” is misleading. Reproducibility would require considerably more detail. |

### Final average

\[
\frac{45 + 52 + 48 + 70}{4} = \mathbf{53.75}
\]

## Major concerns

1. **Insufficient methodological detail**
   - It is unclear whether the normalization is the standard LightGCN normalization followed by gating, or a renormalization using gated edge weights.
   - The exact propagation equation is not given.
   - The treatment of timestamps, time zones, duplicate interactions, filtering, and users with very short histories is unspecified.
   - Negative sampling and the full-ranking evaluation implementation are not described.

2. **Potentially unfair baseline comparison**
   - SeqGate is tuned over 60 configurations per dataset, whereas baselines use settings from prior work or official code. This may disadvantage the baselines, especially because dataset preprocessing and optimal hyperparameters often differ from the original settings.
   - The paper should report comparable tuning budgets and parameter counts, particularly for TiSASRec and SGL.

3. **Weak evidence for statistical reliability**
   - The paper reports standard deviations over five seeds but does not provide significance tests or confidence intervals for pairwise comparisons.
   - Several gains are small relative to the reported variability. For example, the Sports Recall@20 improvement over LightGCN is only 0.0028 in absolute terms.

4. **Ablation is incomplete**
   - The fixed exponential decay baseline is described as “hand-set,” which is not a strong comparison. A tuned exponential decay should be included.
   - Important controls are missing, including:
     - a learned scalar decay without the MLP,
     - a gate based on randomly permuted timestamps,
     - different gate functional forms,
     - gating only at the first propagation layer versus all layers,
     - a popularity or interaction-frequency control.
   - The “gate on user-to-item messages only” variant needs a precise definition because asymmetric propagation changes the graph operator.

5. **Questionable terminology and claims**
   - The model is not clearly session-aware. It uses elapsed time from the end of training, but does not represent sessions, within-session order, or session boundaries.
   - The claim that it requires “no sequence encoder” is accurate, but the comparison to sequential recommenders should acknowledge that SeqGate captures substantially less temporal structure.

6. **Deployment and temporal consistency**
   - The gate is based on age relative to the end of the training period. At deployment, the age of every edge changes continuously. The paper should explain whether embeddings and edge weights are recomputed periodically and how this affects serving cost and model validity.
   - The reported 9% training overhead is not sufficient to characterize the total computational cost, especially if inference requires dynamic recalculation of edge weights.

7. **Limited scope of evaluation**
   - Only e-commerce datasets are used, and all use leave-one-out evaluation.
   - No robustness analysis is provided for different time windows, temporal splits, cold-start users, or datasets with faster preference drift.
   - The long-history improvement may reflect differences in user activity, item popularity, or amount of training data rather than a specific benefit from temporal gating.

## Recommendation

**Reject**

The paper has a clear and potentially useful idea, but in its current form it does not provide sufficiently rigorous evidence for publication. A substantially revised version should improve experimental fairness, fully specify the propagation and data-processing procedures, add stronger temporal and decay baselines, report statistical tests, and clarify the model’s actual relationship to session-aware recommendation.