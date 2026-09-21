## Summary

This paper proposes SeqGate, a LightGCN-style recommender that weights user–item messages using a learned scalar function of interaction age. The idea is simple and computationally lightweight, and the reported results show consistent but modest improvements over LightGCN and SGL on three datasets.

However, the experimental description is not sufficiently rigorous to support the claims. Several important implementation and evaluation details are missing, the comparison may be unfairly tuned, and the reported average improvement over LightGCN is numerically inconsistent with the table. The novelty is also limited: the method is essentially a scalar time-dependent edge reweighting of LightGCN, and the title/claims suggest session awareness that is not actually modeled.

## Strengths

- The proposed modification is simple and potentially easy to integrate into graph collaborative filtering systems.
- The model adds very few parameters and appears computationally inexpensive.
- Evaluation covers three datasets and includes both graph-based and sequential baselines.
- Results are reported with variation over multiple seeds.
- The paper includes basic ablations and a history-length analysis.
- The writing is generally clear and the model description is understandable at a high level.

## Major concerns

### 1. Numerical inconsistency in the main result

From Table 1, the average Recall@20 values are:

- LightGCN:  
  \[
  (0.1052+0.0634+0.0815)/3 = 0.08337
  \]
- SeqGate:  
  \[
  (0.1104+0.0662+0.0857)/3 = 0.08743
  \]

Thus, the relative improvement is approximately:

\[
(0.08743-0.08337)/0.08337 \approx 4.9\%
\]

rather than the claimed 4.6%. The claimed 2.1% improvement over SGL is approximately consistent with the table, but the discrepancy over LightGCN should be corrected.

### 2. Insufficiently specified graph normalization

The paper states that the gate is applied “before normalised aggregation,” but it does not define the resulting normalization. It is unclear whether:

- the standard LightGCN degree normalization is retained,
- degrees are recomputed using gated edge weights,
- gates are applied after normalization, or
- the normalization is based on weighted degrees.

These alternatives define materially different models and can produce different results.

### 3. Weak evidence for the claimed contribution of learned gating

The ablation compares the learned gate with a “fixed exponential decay” using a hand-set rate. This is not a strong baseline. The exponential decay rate should be tuned under the same validation protocol, and ideally several functional forms should be compared. Otherwise, the result may show only that the selected learned function is better than an improperly optimized fixed decay.

The claim that “the time gate accounts for most of the improvement” is also not fully established. The paper does not isolate:

- the effect of time information itself,
- the effect of learning the decay function,
- the effect of gate initialization,
- the effect of changing graph edge weights rather than representations, or
- whether the improvement comes from a particular monotonicity or shape of the learned gate.

### 4. Potentially unfair baseline tuning

SeqGate is tuned over 60 configurations per dataset, while baselines use hyperparameters from their original papers or official implementations. This can substantially disadvantage the baselines, especially across datasets with different sparsity and preprocessing. All major baselines should receive comparable tuning budgets, or the paper should provide a carefully justified protocol demonstrating that the reported configurations are competitive under the current data splits.

### 5. Lack of statistical testing

Although means and standard deviations over five seeds are given, there are no paired significance tests or confidence intervals. The improvements over SGL are fairly small, particularly on Sports and Tmall, and the standard deviations overlap. Reporting per-seed results and paired tests would be important for establishing whether the gains are robust.

### 6. The “session-aware” characterization is misleading

SeqGate uses elapsed time from the end of the training period, but it does not model sessions, session boundaries, within-session order, or short-term sequential transitions. It is more accurately described as a time-aware or recency-gated graph collaborative filtering model. The title and claims should be revised unless session information is actually incorporated.

### 7. Missing reproducibility details

Important details are omitted, including:

- exact dataset versions and preprocessing procedures;
- filtering thresholds and handling of duplicate interactions;
- how timestamps are normalized;
- treatment of users or items with insufficient interactions;
- negative-sampling strategy for BPR;
- number of negative samples;
- validation frequency and early-stopping patience;
- initialization details;
- whether the graph includes only training interactions;
- exact TiSASRec and SGL configurations; and
- hardware used for the training-time comparison.

These omissions make the results difficult to reproduce.

### 8. Limited analysis of the learned gate

The paper does not plot or report the learned gate as a function of interaction age. Such an analysis is important because the stated motivation assumes that older interactions are generally less useful. The gate could be non-monotonic, nearly constant, or dataset-specific. The model also uses a shared scalar gate for all users and items, which may be too restrictive for heterogeneous temporal dynamics.

### 9. Efficiency claim is not fully convincing

The gate depends only on fixed interaction timestamps and shared parameters. Its values could potentially be precomputed or cached, so the claim that gate values must be recomputed at every step and cause a 9% overhead is not well justified. The cost analysis should include total training time, memory, inference time, and whether the implementation uses precomputation.

## Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| Soundness | **48** | Plausible core method, but important ambiguities, weak baseline tuning, limited statistical analysis, and reproducibility gaps undermine confidence. |
| Novelty | **52** | Time-dependent edge weighting in graph recommendation is a reasonable incremental idea, but the technical novelty is limited and closely related to existing time-decay and weighted-graph approaches. |
| Significance | **46** | Improvements are modest, and the method does not convincingly establish broad practical or scientific impact. The session-aware framing is overstated. |
| Clarity | **72** | The paper is generally readable and the central idea is easy to understand, but several methodological details and definitions are underspecified. |

### Final average

\[
\frac{48+52+46+72}{4} = \boxed{54.5}
\]

## Final recommendation: **Reject**

The method is potentially promising as a lightweight recency-aware extension of LightGCN, but the current submission does not provide sufficiently rigorous evidence for acceptance. The authors should correct the reported calculations, clarify the propagation and normalization procedure, tune baselines fairly, strengthen the temporal ablations, report significance tests, and provide complete reproducibility details.