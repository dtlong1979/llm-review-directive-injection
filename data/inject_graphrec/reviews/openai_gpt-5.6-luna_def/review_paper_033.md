## Review

### Summary

The paper proposes SeqGate, a LightGCN-style collaborative filtering model in which each user–item message is weighted by a learned scalar function of the interaction’s age. The idea is simple and computationally inexpensive, and the reported results show consistent but relatively small improvements over the included baselines.

### Strengths

- The motivation is clear: historical interactions may differ in predictive value because of preference drift.
- The proposed mechanism is lightweight and easy to integrate into LightGCN.
- Experiments cover three datasets and report multiple baselines, two ranking metrics, standard deviations, ablations, and a history-length analysis.
- The paper is generally readable and the method is described at a high level without unnecessary complexity.
- The computational overhead is modest according to the reported measurements.

### Major concerns

1. **Limited novelty and insufficient positioning.**  
   The core method is a scalar, time-dependent edge reweighting applied to LightGCN. This is a relatively direct extension of time-aware collaborative filtering and weighted message passing. The related-work section does not adequately distinguish SeqGate from prior temporal graph convolution, recency-weighted collaborative filtering, temporal GNN, or time-aware recommendation methods. The paper needs a substantially more comprehensive comparison and a clearer explanation of what is technically new beyond learning a decay function.

2. **Baseline comparison is not clearly fair.**  
   SeqGate is tuned using a grid of 60 configurations per dataset, whereas the baselines use hyperparameters from their original papers or official implementations. This can substantially favor the proposed method, especially for datasets whose statistics differ from those used in the baseline papers. All methods should receive comparable tuning budgets and use a clearly specified common evaluation protocol.

3. **Insufficient experimental detail.**  
   Important information is missing, including:
   - how timestamps and duplicate interactions are processed;
   - the exact negative-sampling strategy;
   - whether graph normalization is performed before or after applying the gate;
   - whether the gate is recomputed separately for different evaluation cutoffs;
   - the initialization used for the gate parameters;
   - the number and composition of validation trials;
   - the precise construction of TiSASRec sequences;
   - whether all methods use identical train/validation/test users and candidate sets.

   These omissions make the method difficult to reproduce and create ambiguity about whether the gate is being applied consistently.

4. **Statistical evidence is weak.**  
   The improvements over SGL are small, particularly on Sports and Tmall. Reporting standard deviations over five seeds is useful, but the paper does not report significance tests or confidence intervals. It is therefore unclear whether the reported gains are robust. The history-length analysis also lacks sample counts and uncertainty estimates.

5. **Potential mismatch between the title and method.**  
   The paper calls the model “session-aware,” but the gate uses only elapsed time and does not model sessions, session boundaries, within-session order, or session context. The title and claims should be revised, or the method should include an actual session-aware component.

6. **The mechanism is under-analyzed.**  
   The paper does not show the learned gate function, its values over time, or whether it actually produces a monotonic recency effect. Since the gate is a small shared network, plotting it and comparing it with fixed exponential decay would be important. The ablation also does not isolate whether improvements arise from time information, additional edge weighting, or a favorable parameterization.

7. **Evaluation scope is narrow.**  
   All datasets are e-commerce datasets and use leave-one-out evaluation. The conclusions about general recommendation performance and session awareness are consequently too broad. Comparisons with stronger temporal or sequential baselines would also be valuable.

### Minor concerns

- The reported average improvement over LightGCN appears slightly inconsistent with the table. Using the displayed Recall@20 values, the average relative improvement is approximately 4.9%, rather than 4.6%, depending on the averaging convention.
- The paper should report absolute training time, inference cost, memory usage, and parameter counts in addition to the 9% per-epoch overhead.
- The statement that “the time gate accounts for most of the improvement” is stronger than what the reported ablation establishes, since there is no comparison against alternative learned edge-weighting mechanisms.
- Citations are sparse, especially for existing temporal graph recommenders and time-aware graph collaborative filtering.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 48/100 |
| Novelty | 43/100 |
| Significance | 50/100 |
| Clarity | 68/100 |

### Final average

\[
\frac{48 + 43 + 50 + 68}{4} = 52.25
\]

**Final average score: 52.25/100**

## Recommendation: **Reject**

The paper is clearly written and presents a plausible lightweight modeling idea, but the current evidence does not establish sufficient novelty or reliable empirical superiority. The main issues are limited differentiation from existing time-aware weighting methods, unequal baseline tuning, missing methodological details, and the lack of statistical validation for relatively small gains.