## Review

### Summary

The paper presents SeqGate, a LightGCN-style model that weights user–item messages using a learned scalar function of interaction age. The approach is simple and computationally inexpensive, and the reported results show consistent but relatively modest improvements over LightGCN and SGL on three datasets.

### Soundness: **62/100**

The core method is technically plausible, and the experimental design includes reasonable components: temporal leave-one-out splitting, multiple baselines, ablations, and reporting over five seeds. However, several details prevent full confidence in the conclusions:

- The aggregation procedure is underspecified. It is unclear whether the time-weighted edges are normalized using the original LightGCN degree normalization or whether degrees are recomputed from the gated weights. These choices can produce substantially different models.
- The comparison is not clearly controlled. SeqGate receives a 60-configuration grid search, whereas baselines use settings from their papers or official implementations. This may disadvantage the baselines.
- Dataset preprocessing, filtering criteria, timestamp handling, negative sampling, and exact validation protocol are not provided in sufficient detail for reproduction.
- The reported improvements are small relative to the standard deviations, and no paired statistical significance tests are presented.
- The claim of a 4.6% average Recall@20 improvement over LightGCN does not exactly match the table. The average Recall values are approximately 0.08337 for LightGCN and 0.08743 for SeqGate, corresponding to roughly a 4.9% relative improvement.
- The analysis does not establish whether the method benefits from genuine temporal modeling or simply from a dataset-specific recency prior.

### Novelty: **45/100**

The model is a straightforward extension of LightGCN with an edge weight based on interaction age. Learned temporal weighting has been explored extensively in time-aware collaborative filtering, temporal graph models, and sequential recommendation. The specific use of a four-parameter shared MLP gate is a compact implementation, but the conceptual novelty is limited.

The paper would need a stronger distinction from prior temporal graph convolution and adaptive decay methods. In particular, the related-work discussion should compare against learned temporal decay, temporal graph neural networks, and graph recommenders with time-aware edge weights—not only fixed exponential decay.

### Significance: **54/100**

The method is attractive from an engineering perspective: it adds very few parameters, does not require a sequence encoder, and reports consistent gains across the tested datasets. The stronger gains for users with long histories are also practically relevant.

Nevertheless, the absolute improvements are modest, and the evaluation is limited to three offline e-commerce datasets using leave-one-out evaluation. The model is called “session-aware,” but it does not model sessions, session boundaries, item transitions, or within-session order; it only uses the age of an interaction. The absence of online evaluation or stronger temporal baselines limits the evidence for broad practical impact.

### Clarity: **76/100**

The paper is generally well organized and easy to follow. The method, experimental setup, and main conclusions are presented clearly. The tables are concise and useful.

Important details are missing, however:

- exact graph normalization with gates;
- gate initialization and the meaning of the initialization grid;
- preprocessing and filtering rules;
- sequence/history construction for TiSASRec;
- baseline tuning procedures;
- hardware and training-time measurement protocol;
- whether the temporal cutoff is shared globally or determined per user;
- the precise definition of the history-length subsets.

The terminology “session-aware” is also potentially misleading because the proposed model is temporal or recency-aware rather than session-aware in the usual recommendation sense.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 62 |
| Novelty | 45 |
| Significance | 54 |
| Clarity | 76 |
| **Average** | **59.25** |

## Final recommendation: **Reject**

The paper is clearly written and reports a plausible, lightweight modification with encouraging empirical results. However, the limited novelty, incomplete methodological details, potentially unfair baseline tuning, lack of significance testing, and imprecise “session-aware” framing make the evidence insufficient for acceptance in its current form. A revised version should provide a more comprehensive comparison to temporal graph methods, clarify the normalization and evaluation protocol, ensure matched hyperparameter tuning, and substantiate the gains with significance tests and stronger analysis.