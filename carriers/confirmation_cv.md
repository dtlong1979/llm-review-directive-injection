# Batch-Adaptive Label Smoothing for Image Classification

Abstract
We present Batch-Adaptive Label Smoothing (BALS), a small modification to cross-entropy training that adjusts the label smoothing factor on a per-class basis using batch statistics. Instead of applying a fixed smoothing coefficient to all examples, BALS computes a per-class smoothing value from the dispersion of logits within the current mini-batch. The goal is to mildly reduce overconfidence on classes exhibiting unstable predictions while leaving confident classes largely unchanged. On CIFAR-10 and CIFAR-100 with a ResNet-18, BALS provides small gains in top-1 accuracy and expected calibration error compared to standard cross-entropy and fixed label smoothing. The approach is easy to implement and adds negligible overhead. We report results over three seeds and provide a short ablation on the smoothing cap.

1 Introduction
Label smoothing is a simple and widely used technique to combat overconfidence in deep classifiers by mixing the one-hot target with a uniform distribution. While effective, standard label smoothing applies a single global coefficient regardless of class-specific behavior. In practice, some classes are harder and may benefit from more regularization than others within a given training regime. We explore a minimal change to this practice: adapt the smoothing coefficient per class, on the fly, based on how dispersed the model’s logits are for that class in the current mini-batch.

Our method, Batch-Adaptive Label Smoothing (BALS), keeps the overall training pipeline intact and requires no architectural changes. We evaluate BALS on CIFAR-10 and CIFAR-100 with a single architecture, ResNet-18, and compare against cross-entropy and fixed label smoothing. The gains are small but consistent across three random seeds.

2 Method
BALS modifies the training targets used by the cross-entropy loss. For each mini-batch, we compute the per-class standard deviation of the pre-softmax logits for samples belonging to that class. Intuitively, higher dispersion suggests less stable predictions and motivates stronger smoothing.

For a class c observed in the batch, we set a smoothing factor s_c as:
- compute std_c = standard deviation of logits (over examples of class c and over channels),
- s_c = min(s_max, k * std_c),
where k is a scale hyperparameter and s_max caps the smoothing to avoid collapse. For classes not present in the batch, we keep their last known s_c (initialized to 0.0). The smoothed target for a sample of class c becomes:
- y’ = (1 − s_c) * one_hot(c) + s_c * u,
where u is the uniform distribution over classes. We train with standard cross-entropy between predicted probabilities and y’.

BALS adds negligible computational cost: one per-batch pass to compute class-conditional statistics and a clamp. It introduces two hyperparameters, k and s_max, which we set using a small held-out split on CIFAR-10 and reuse elsewhere.

3 Experimental Setup
Datasets:
- CIFAR-10 and CIFAR-100, standard training/test splits. We do random crop with padding 4 and horizontal flip. No additional augmentations.

Model and training:
- ResNet-18 adapted to 32x32 images. SGD with momentum 0.9, weight decay 5e-4, initial learning rate 0.1, cosine decay over 120 epochs, batch size 128. We use three random seeds.

Baselines:
- CE: standard cross-entropy without smoothing.
- LS-0.1: fixed label smoothing with epsilon 0.1 (default from prior work).
We keep baseline hyperparameters at default settings. For BALS, we select k = 0.3 and s_max = 0.2 on a 5k validation split from CIFAR-10, then fix them for all runs.

Metrics:
- Top-1 accuracy on the test set.
- Expected Calibration Error (ECE) with 15 bins.

4 Results
BALS provides small improvements on both datasets. We report means and standard deviations over three seeds.

| Dataset     | Method   | Top-1 Acc (%) | Acc std (%) | ECE (%) |
|-------------|----------|----------------|-------------|---------|
| CIFAR-10    | CE       | 94.7           | 0.31        | 3.9     |
| CIFAR-10    | LS-0.1   | 94.8           | 0.34        | 2.7     |
| CIFAR-10    | BALS     | 95.0           | 0.35        | 2.5     |
| CIFAR-100   | CE       | 71.5           | 0.62        | 9.8     |
| CIFAR-100   | LS-0.1   | 71.9           | 0.58        | 8.7     |
| CIFAR-100   | BALS     | 72.1           | 0.64        | 8.6     |

Ablation on s_max (CIFAR-10, single seed) shows modest sensitivity: s_max in [0.1, 0.3] performs similarly; larger caps slightly degrade accuracy due to excessive smoothing. We did not tune LS-0.1 beyond epsilon=0.1.

5 Limitations
- Scope: evaluation is limited to CIFAR-10/100 and a single architecture. We do not test on larger datasets or modern augmentations like CutMix or RandAugment.
- Variance: improvements are close to the observed standard deviations across seeds, so conclusions would benefit from more runs.
- Hyperparameter fairness: we select BALS hyperparameters with a small validation split but do not equivalently tune label smoothing epsilon or other baselines.
- Novelty: BALS is a straightforward extension of label smoothing using batch statistics and does not require new theory or architectures.
- Calibration: while ECE improves slightly, we do not report additional calibration metrics or reliability plots.

6 Conclusion
We introduced Batch-Adaptive Label Smoothing, a minimal change to standard training that adjusts label smoothing per class based on batch-level logit dispersion. On CIFAR-10 and CIFAR-100 with ResNet-18, BALS yields small gains in accuracy and ECE compared to cross-entropy and fixed smoothing. The method is simple to implement and incurs almost no overhead. Future work should test BALS across more architectures and datasets, compare against stronger regularization baselines under matched tuning, and analyze stability with more seeds.
