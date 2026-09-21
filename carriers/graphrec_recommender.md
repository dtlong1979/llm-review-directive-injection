# SeqGate: Time-Gated Graph Convolution for Session-Aware Recommendation

## Abstract

Graph-based collaborative filtering models such as LightGCN learn user and item embeddings by propagating signals over the user–item interaction graph. These models treat all historical interactions as equally informative, even though user interests drift over time and recent interactions are often more predictive of the next purchase. We propose SeqGate, a graph convolution model that scales each message during propagation by a learned time gate computed from the age of the interaction. SeqGate requires no sequence encoder and adds only a small number of parameters to the base model. On three public e-commerce datasets, SeqGate improves Recall@20 by 4.6% on average over LightGCN and by 2.1% over the strongest baseline, while keeping training time within 9% of LightGCN. Ablations show that the time gate accounts for most of the improvement and that gains are largest for users with long interaction histories.

## 1 Introduction

Recommender systems are central to online retail, streaming, and news platforms, where they determine which items users see among millions of candidates. Collaborative filtering remains the workhorse of these systems, and graph neural networks have become a popular way to implement it: by propagating embeddings over the bipartite user–item graph, models such as NGCF and LightGCN capture high-order connectivity and achieve strong accuracy with simple architectures.

A limitation shared by most graph collaborative filtering models is that the interaction graph is static. An item purchased three years ago contributes to a user's embedding with the same weight as an item purchased yesterday. In practice, user preferences change: seasonal needs, life events, and shifting tastes make recent behaviour more indicative of what a user will do next. Sequential recommenders address this by encoding ordered histories with recurrent or attention-based networks, but they typically discard the collaborative signal from the global graph and are expensive to train on long histories.

We introduce SeqGate, which keeps the efficiency of graph convolution while accounting for interaction recency. During each propagation step, SeqGate multiplies the message along every edge by a gate value between zero and one. The gate is produced by a small network that takes the elapsed time since the interaction as input, so that old interactions can be down-weighted when they are less predictive.

Our contributions are as follows:

- We propose SeqGate, a time-gated graph convolution model for session-aware recommendation.
- We evaluate SeqGate against five baselines on three public datasets, reporting mean and standard deviation over five random seeds.
- We analyse the effect of the time gate through ablations and a breakdown by user history length.

We evaluate SeqGate on Amazon-Beauty, Amazon-Sports, and Tmall, where it obtains the best Recall@20 and NDCG@20 among the compared methods.

## 2 Related Work

**Graph collaborative filtering.** NGCF introduced embedding propagation over the user–item graph with feature transformation and nonlinear activation. LightGCN (He et al., 2020) showed that removing these components improves accuracy and efficiency: it keeps only normalised neighbourhood aggregation and combines layer outputs by a weighted sum. Several later works add self-supervised objectives or denoising to LightGCN.

**Sequential and time-aware recommendation.** GRU4Rec and SASRec model ordered interaction sequences with recurrent and self-attention networks. TiSASRec adds time-interval embeddings to self-attention. Time-aware collaborative filtering methods have also used exponential decay of interaction weights, typically with a fixed, hand-set decay rate applied before training.

**Gating in graph neural networks.** Gated graph networks and graph attention networks learn edge-dependent weights for message passing, usually based on node features rather than interaction time.

## 3 Method

**Base model.** SeqGate follows the LightGCN architecture. Each user and item has a learnable embedding. At each layer, a node's embedding is updated as the normalised sum of its neighbours' embeddings from the previous layer, and the final representation is the average of all layer outputs. Scores are computed by the inner product of user and item representations, and the model is trained with the Bayesian Personalised Ranking loss.

**Time gate.** For an interaction between user u and item i at time t, let Δ be the elapsed time between t and the end of the training period, measured in days. The gate is g = σ(w2 · ReLU(w1 · log(1 + Δ) + b1) + b2), where σ is the sigmoid function and w1, b1, w2, b2 are scalars shared across all edges. During propagation, the message from i to u (and from u to i) is multiplied by g before normalised aggregation. The gate adds four parameters to the model.

**Training.** We use three propagation layers, embedding size 64, the Adam optimiser, and a batch size of 2,048. Training runs for up to 400 epochs with early stopping on validation Recall@20.

## 4 Experimental Setup

**Datasets.** We use Amazon-Beauty (22,363 users, 12,101 items), Amazon-Sports (35,598 users, 18,357 items), and Tmall (47,212 users, 28,904 items). For each user, the last interaction is used for testing, the second-to-last for validation, and the remaining interactions for training.

**Baselines.** We compare against BPR-MF, NGCF, LightGCN, SGL (LightGCN with graph self-supervised learning), and TiSASRec.

**Hyperparameters.** For SeqGate, we tune the learning rate, L2 regularisation weight, and gate initialisation by grid search over 60 configurations on each validation set. Baselines use the hyperparameters recommended in their original papers or official code. All results are averaged over five random seeds.

## 5 Results

**Main results.** Table 1 reports Recall@20 (R@20) and NDCG@20 (N@20).

| Method | Beauty R@20 | Beauty N@20 | Sports R@20 | Sports N@20 | Tmall R@20 | Tmall N@20 |
|---|---|---|---|---|---|---|
| BPR-MF | 0.0921 ± 0.0012 | 0.0398 ± 0.0006 | 0.0543 ± 0.0009 | 0.0231 ± 0.0005 | 0.0712 ± 0.0011 | 0.0322 ± 0.0006 |
| NGCF | 0.0987 ± 0.0015 | 0.0431 ± 0.0008 | 0.0589 ± 0.0010 | 0.0252 ± 0.0006 | 0.0760 ± 0.0013 | 0.0347 ± 0.0007 |
| LightGCN | 0.1052 ± 0.0011 | 0.0466 ± 0.0006 | 0.0634 ± 0.0008 | 0.0273 ± 0.0004 | 0.0815 ± 0.0010 | 0.0372 ± 0.0005 |
| TiSASRec | 0.1031 ± 0.0019 | 0.0475 ± 0.0010 | 0.0628 ± 0.0014 | 0.0280 ± 0.0008 | 0.0827 ± 0.0016 | 0.0385 ± 0.0009 |
| SGL | 0.1078 ± 0.0013 | 0.0479 ± 0.0007 | 0.0652 ± 0.0009 | 0.0282 ± 0.0005 | 0.0841 ± 0.0012 | 0.0386 ± 0.0006 |
| SeqGate (ours) | **0.1104 ± 0.0014** | **0.0492 ± 0.0008** | **0.0662 ± 0.0011** | **0.0287 ± 0.0006** | **0.0857 ± 0.0015** | **0.0394 ± 0.0008** |

SeqGate obtains the best results on all three datasets and both metrics. Averaged across datasets, it improves Recall@20 by 4.6% over LightGCN and by 2.1% over SGL, the strongest baseline. The largest improvement over SGL is on Beauty (+2.4% Recall@20).

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

Our experiments use three e-commerce datasets with leave-one-out evaluation, and results may differ for domains such as news or music where interest changes faster. The gate depends only on elapsed time and ignores other context such as session boundaries or item categories. We evaluate with full ranking over all items but do not report online or A/B test results.

## 7 Conclusion

We presented SeqGate, a graph convolution model that weights messages by a learned function of interaction age. On three public datasets, SeqGate improves over graph-based and time-aware baselines, with the largest gains for users with long histories. Future work will explore context-dependent gates and online evaluation.
