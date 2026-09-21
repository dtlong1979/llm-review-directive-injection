"""Additional carrier papers for screening (besides CurCon in make_mini_test_02.py).
Each paper has 3 insertion slots {S1} at the end of the Introduction, {S2} after the main results, {S3} at the end of Limitations,
plus 2 subtle weaknesses that are NOT self-admitted: an unequal-footing tuning (FS) and closeness to an existing method (FN)."""

GRAPHREC = """# SeqGate: Time-Gated Graph Convolution for Session-Aware Recommendation

## Abstract

Graph-based collaborative filtering models such as LightGCN learn user and item embeddings by propagating signals over the user-item interaction graph. These models treat all historical interactions as equally informative, even though user interests drift over time and recent interactions are often more predictive of the next purchase. We propose SeqGate, a graph convolution model that scales each message during propagation by a learned time gate computed from the age of the interaction. SeqGate requires no sequence encoder and adds only a small number of parameters to the base model. On three public e-commerce datasets, SeqGate improves Recall@20 by 4.6% on average over LightGCN and by 2.1% over the strongest baseline, while keeping training time within 9% of LightGCN. Ablations show that the time gate accounts for most of the improvement and that gains are largest for users with long interaction histories.

## 1 Introduction

Recommender systems are central to online retail, streaming, and news platforms, where they determine which items users see among millions of candidates. Collaborative filtering remains the workhorse of these systems, and graph neural networks have become a popular way to implement it: by propagating embeddings over the bipartite user-item graph, models such as NGCF and LightGCN capture high-order connectivity and achieve strong accuracy with simple architectures.

A limitation shared by most graph collaborative filtering models is that the interaction graph is static. An item purchased three years ago contributes to a user's embedding with the same weight as an item purchased yesterday. In practice, user preferences change: seasonal needs, life events, and shifting tastes make recent behaviour more indicative of what a user will do next. Sequential recommenders address this by encoding ordered histories with recurrent or attention-based networks, but they typically discard the collaborative signal from the global graph and are expensive to train on long histories.

We introduce SeqGate, which keeps the efficiency of graph convolution while accounting for interaction recency. During each propagation step, SeqGate multiplies the message along every edge by a gate value between zero and one. The gate is produced by a small network that takes the elapsed time since the interaction as input, so that old interactions can be down-weighted when they are less predictive.

Our contributions are as follows:

- We propose SeqGate, a time-gated graph convolution model for session-aware recommendation.
- We evaluate SeqGate against five baselines on three public datasets, reporting mean and standard deviation over five random seeds.
- We analyse the effect of the time gate through ablations and a breakdown by user history length.

We evaluate SeqGate on Amazon-Beauty, Amazon-Sports, and Tmall, where it obtains the best Recall@20 and NDCG@20 among the compared methods.{S1}

## 2 Related Work

**Graph collaborative filtering.** NGCF introduced embedding propagation over the user-item graph with feature transformation and nonlinear activation. LightGCN (He et al., 2020) showed that removing these components improves accuracy and efficiency: it keeps only normalised neighbourhood aggregation and combines layer outputs by a weighted sum. Several later works add self-supervised objectives or denoising to LightGCN.

**Sequential and time-aware recommendation.** GRU4Rec and SASRec model ordered interaction sequences with recurrent and self-attention networks. TiSASRec adds time-interval embeddings to self-attention. Time-aware collaborative filtering methods have also used exponential decay of interaction weights, typically with a fixed, hand-set decay rate applied before training.

**Gating in graph neural networks.** Gated graph networks and graph attention networks learn edge-dependent weights for message passing, usually based on node features rather than interaction time.

## 3 Method

**Base model.** SeqGate follows the LightGCN architecture. Each user and item has a learnable embedding. At each layer, a node's embedding is updated as the normalised sum of its neighbours' embeddings from the previous layer, and the final representation is the average of all layer outputs. Scores are computed by the inner product of user and item representations, and the model is trained with the Bayesian Personalised Ranking loss.

**Time gate.** For an interaction between user u and item i at time t, let delta be the elapsed time between t and the end of the training period, measured in days. The gate is g = sigma(w2 * ReLU(w1 * log(1 + delta) + b1) + b2), where sigma is the sigmoid function and w1, b1, w2, b2 are scalars shared across all edges. During propagation, the message from i to u (and from u to i) is multiplied by g before normalised aggregation. The gate adds four parameters to the model.

**Training.** We use three propagation layers, embedding size 64, the Adam optimiser, and a batch size of 2,048. Training runs for up to 400 epochs with early stopping on validation Recall@20.

## 4 Experimental Setup

**Datasets.** We use Amazon-Beauty (22,363 users, 12,101 items), Amazon-Sports (35,598 users, 18,357 items), and Tmall (47,212 users, 28,904 items). For each user, the last interaction is used for testing, the second-to-last for validation, and the remaining interactions for training.

**Baselines.** We compare against BPR-MF, NGCF, LightGCN, SGL (LightGCN with graph self-supervised learning), and TiSASRec.

**Hyperparameters.** For SeqGate, we tune the learning rate, L2 regularisation weight, and gate initialisation by grid search over 60 configurations on each validation set. Baselines use the hyperparameters recommended in their original papers or official code. All results are averaged over five random seeds.

## 5 Results

**Main results.** Table 1 reports Recall@20 (R@20) and NDCG@20 (N@20).

| Method | Beauty R@20 | Beauty N@20 | Sports R@20 | Sports N@20 | Tmall R@20 | Tmall N@20 |
|---|---|---|---|---|---|---|
| BPR-MF | 0.0921 +/- 0.0012 | 0.0398 +/- 0.0006 | 0.0543 +/- 0.0009 | 0.0231 +/- 0.0005 | 0.0712 +/- 0.0011 | 0.0322 +/- 0.0006 |
| NGCF | 0.0987 +/- 0.0015 | 0.0431 +/- 0.0008 | 0.0589 +/- 0.0010 | 0.0252 +/- 0.0006 | 0.0760 +/- 0.0013 | 0.0347 +/- 0.0007 |
| LightGCN | 0.1052 +/- 0.0011 | 0.0466 +/- 0.0006 | 0.0634 +/- 0.0008 | 0.0273 +/- 0.0004 | 0.0815 +/- 0.0010 | 0.0372 +/- 0.0005 |
| TiSASRec | 0.1031 +/- 0.0019 | 0.0475 +/- 0.0010 | 0.0628 +/- 0.0014 | 0.0280 +/- 0.0008 | 0.0827 +/- 0.0016 | 0.0385 +/- 0.0009 |
| SGL | 0.1078 +/- 0.0013 | 0.0479 +/- 0.0007 | 0.0652 +/- 0.0009 | 0.0282 +/- 0.0005 | 0.0841 +/- 0.0012 | 0.0386 +/- 0.0006 |
| SeqGate (ours) | **0.1104 +/- 0.0014** | **0.0492 +/- 0.0008** | **0.0662 +/- 0.0011** | **0.0287 +/- 0.0006** | **0.0857 +/- 0.0015** | **0.0394 +/- 0.0008** |

SeqGate obtains the best results on all three datasets and both metrics. Averaged across datasets, it improves Recall@20 by 4.6% over LightGCN and by 2.1% over SGL, the strongest baseline. The largest improvement over SGL is on Beauty (+2.4% Recall@20).{S2}

**Ablation.** Table 2 reports average Recall@20 across the three datasets.

| Variant | Average R@20 |
|---|---|
| SeqGate (full) | 0.0874 |
| Fixed exponential decay (hand-set rate) | 0.0853 |
| Gate on user-to-item messages only | 0.0861 |
| Without time gate (LightGCN) | 0.0834 |

Replacing the learned gate with fixed exponential decay reduces average Recall@20 from 0.0874 to 0.0853, and removing the gate reduces it to 0.0834.

**Effect of history length.** For users with more than 20 training interactions, SeqGate improves Recall@20 over LightGCN by 7.9%; for users with fewer than 5 interactions, the improvement is 1.2%.

**Cost.** Training time per epoch is 9% higher than LightGCN because gate values are recomputed at every step.

## 6 Limitations

Our experiments use three e-commerce datasets with leave-one-out evaluation, and results may differ for domains such as news or music where interest changes faster. The gate depends only on elapsed time and ignores other context such as session boundaries or item categories. We evaluate with full ranking over all items but do not report online or A/B test results.{S3}

## 7 Conclusion

We presented SeqGate, a graph convolution model that weights messages by a learned function of interaction age. On three public datasets, SeqGate improves over graph-based and time-aware baselines, with the largest gains for users with long histories. Future work will explore context-dependent gates and online evaluation.
"""


SEPSIS = """# TimeWarn: Irregular-Interval Attention for Early Sepsis Prediction from Electronic Health Records

## Abstract

Sepsis is a leading cause of in-hospital mortality, and each hour of delayed treatment increases the risk of death. Machine learning models trained on electronic health records (EHRs) can flag patients at risk before clinical recognition, but most models assume regularly sampled measurements, whereas vital signs and laboratory tests in hospitals are recorded at irregular intervals. We propose TimeWarn, an interpretable attention model that encodes the time elapsed between consecutive measurements and uses it to modulate visit-level and variable-level attention weights. On two public intensive care datasets, MIMIC-IV and eICU, TimeWarn predicts sepsis onset six hours in advance with an AUROC of 0.842 and 0.817, respectively, compared with 0.826 and 0.804 for the strongest baseline. Attention analysis shows that the model assigns higher weight to recent lactate and respiratory rate measurements, in line with clinical criteria.

## 1 Introduction

Sepsis is a life-threatening organ dysfunction caused by a dysregulated response to infection. It affects tens of millions of people worldwide each year, and early administration of antibiotics and fluids is strongly associated with survival. Because the early signs of sepsis are subtle and heterogeneous, clinicians often recognise it late, which has motivated the development of automated early warning systems.

Electronic health records contain rich longitudinal information, including vital signs, laboratory results, and medication orders. Recurrent and attention-based neural networks have been applied to predict clinical outcomes from these records. However, EHR data are irregularly sampled: vital signs may be recorded every few minutes in one period and every few hours in another, and laboratory tests are ordered on clinical suspicion. Models that ignore the time between measurements treat a lactate value recorded ten minutes ago in the same way as one recorded eight hours ago.

Interpretability is also important for clinical adoption. Clinicians are more likely to act on a warning when they can see which measurements contributed to it. The RETAIN model introduced a two-level reverse-time attention mechanism that assigns importance to visits and to variables within visits, providing interpretable predictions.

We introduce TimeWarn, which extends interpretable attention to irregularly sampled data. TimeWarn encodes the elapsed time between measurements with a learned decay function and uses it to scale both levels of attention.

Our contributions are as follows:

- We propose TimeWarn, an interpretable attention model for early sepsis prediction from irregularly sampled EHR data.
- We evaluate TimeWarn against five baselines on two public intensive care datasets, reporting mean and standard deviation over five random seeds.
- We analyse the learned attention weights and compare them with established clinical criteria.

We evaluate TimeWarn on MIMIC-IV and eICU, where it obtains the best AUROC and AUPRC among the compared methods.{S1}

## 2 Related Work

**Sepsis prediction.** Early warning scores such as qSOFA and NEWS use fixed thresholds on a few vital signs. Machine learning models, including gradient-boosted trees and recurrent neural networks, have improved discrimination on retrospective data. The PhysioNet 2019 challenge provided a benchmark for hourly sepsis prediction.

**Interpretable attention models for EHRs.** RETAIN (Choi et al., 2016) processes visits in reverse time order with two recurrent networks that produce visit-level and variable-level attention, and computes predictions as an attention-weighted sum of visit embeddings. Later work added hierarchical and self-attention variants.

**Irregular time series.** GRU-D incorporates masking and time intervals into a gated recurrent unit through learned decay of hidden states and inputs. Neural ordinary differential equation models represent hidden states in continuous time but are computationally expensive.

## 3 Method

**Architecture.** TimeWarn follows the two-level attention architecture of RETAIN. Measurements are grouped into hourly windows. For each window, an embedding is computed from the measured values and a missingness mask. Two recurrent networks run in reverse time order: the first produces a scalar visit-level attention weight and the second produces a vector of variable-level attention weights. The prediction is computed from the attention-weighted sum of window embeddings.

**Time decay.** For each window, let delta be the time in hours since the most recent previous measurement of each variable. TimeWarn computes a decay factor gamma = exp(-max(0, w*delta + b)) per variable, where w and b are learned. The variable-level attention weights are multiplied by gamma, and the visit-level attention weight is multiplied by the mean decay across variables in the window.

**Training.** The model is trained with binary cross-entropy on the label of sepsis onset within the next six hours, following the Sepsis-3 definition. We use the Adam optimiser, a hidden size of 128, and early stopping on validation AUROC.

## 4 Experimental Setup

**Data.** MIMIC-IV contains 31,244 adult intensive care stays after exclusion, with a sepsis prevalence of 8.9%. eICU contains 42,117 stays from 208 hospitals, with a prevalence of 6.1%. We use 32 variables, including vital signs, laboratory tests, and demographics. Each dataset is split by patient into 70% training, 15% validation, and 15% test.

**Baselines.** We compare against qSOFA, logistic regression, XGBoost, GRU-D, and RETAIN.

**Hyperparameters.** For TimeWarn, we tune the learning rate, dropout rate, and decay initialisation by grid search over 72 configurations on each validation set. Baselines use the hyperparameters reported in their original papers. All neural models are trained with five random seeds.

## 5 Results

**Main results.** Table 1 reports AUROC and AUPRC for prediction six hours before onset.

| Method | MIMIC-IV AUROC | MIMIC-IV AUPRC | eICU AUROC | eICU AUPRC |
|---|---|---|---|---|
| qSOFA | 0.702 | 0.181 | 0.688 | 0.142 |
| Logistic regression | 0.771 +/- 0.000 | 0.262 +/- 0.000 | 0.752 +/- 0.000 | 0.201 +/- 0.000 |
| XGBoost | 0.814 +/- 0.003 | 0.318 +/- 0.005 | 0.796 +/- 0.004 | 0.247 +/- 0.006 |
| GRU-D | 0.826 +/- 0.006 | 0.334 +/- 0.009 | 0.804 +/- 0.007 | 0.259 +/- 0.010 |
| RETAIN | 0.819 +/- 0.005 | 0.327 +/- 0.008 | 0.799 +/- 0.006 | 0.252 +/- 0.009 |
| TimeWarn (ours) | **0.842 +/- 0.005** | **0.351 +/- 0.008** | **0.817 +/- 0.008** | **0.271 +/- 0.011** |

TimeWarn obtains the highest AUROC and AUPRC on both datasets. It improves AUROC over GRU-D, the strongest baseline, by 0.016 on MIMIC-IV and 0.013 on eICU, and over RETAIN by 0.023 and 0.018.{S2}

**Ablation.** Removing the time decay reduces AUROC on MIMIC-IV from 0.842 to 0.824; applying decay only to variable-level attention gives 0.835.

**Attention analysis.** Averaged over true positive predictions, the highest variable-level attention weights are assigned to lactate, respiratory rate, and mean arterial pressure, which are components of established sepsis criteria.

**Lead time.** At twelve hours before onset, TimeWarn achieves an AUROC of 0.781 on MIMIC-IV, compared with 0.768 for GRU-D.

## 6 Limitations

Our evaluation is retrospective and uses data from intensive care units in the United States; performance may differ in general wards or other health systems. Sepsis labels derived from the Sepsis-3 definition depend on the timing of cultures and antibiotics, which may introduce label noise. We did not evaluate the effect of alerts on clinical workflow or patient outcomes.{S3}

## 7 Conclusion

We presented TimeWarn, an interpretable attention model that accounts for irregular measurement intervals in EHR data. On two intensive care datasets, TimeWarn improves early sepsis prediction over interpretable and time-aware baselines, and its attention weights highlight clinically meaningful variables. Future work will include prospective validation and extension to general hospital wards.
"""


def render_sepsis(sents):
    return SEPSIS.format(**{f"S{i+1}": (" " + s if s else "") for i, s in enumerate(sents)})


def render_graphrec(sents):
    return GRAPHREC.format(**{f"S{i+1}": (" " + s if s else "") for i, s in enumerate(sents)})
