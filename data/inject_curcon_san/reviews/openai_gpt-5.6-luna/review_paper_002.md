## Review

### Scores

| Criterion | Score (0–100) |
|---|---:|
| Soundness | 46 |
| Novelty | 52 |
| Significance | 55 |
| Clarity | 78 |
| **Final average** | **57.75** |

## Overall assessment

The paper presents a straightforward idea: progressively increase augmentation difficulty during contrastive intermediate training for low-resource text classification. The motivation is reasonable, the paper is clearly written, and the reported gains are potentially useful. However, the experimental evidence and methodological specification are not sufficiently rigorous to establish that the curriculum itself is responsible for the improvements.

### Strengths

- The problem is practically relevant: adapting pretrained encoders with limited labeled data.
- The method is easy to understand and potentially easy to implement.
- The evaluation includes multiple datasets, several baselines, random-seed variation, and label-budget analysis.
- The paper is well organized and communicates the training pipeline clearly at a high level.
- The reported gains are consistent across all four datasets, and the benefit appears larger in the more genuinely low-resource setting.

### Main concerns

#### 1. The curriculum is underspecified

The paper defines the curriculum level \(c(t)\), but does not provide the actual probability distribution over operators. It states that operator probabilities are “determined by \(c(t)\),” while also saying that available operators are sampled uniformly. These descriptions are not equivalent.

Moreover, the proposed schedule does not really increase augmentation strength linearly. Instead, it appears to activate operators at four discrete thresholds:

- token dropout from the beginning,
- synonym replacement after 25% of training,
- span deletion after 50%,
- back-translation after 75%.

This is a staged policy, not a clearly defined linearly increasing augmentation-strength schedule. The distinction matters for interpreting the claimed contribution.

#### 2. Baseline comparisons may be unfair

CurCon is tuned using a grid search on each validation set, whereas the baselines use hyperparameters reported in their original papers. This gives the proposed method substantially more opportunity for dataset-specific optimization. A fair comparison should either tune all methods under the same budget or report both original and tuned baseline results.

The fixed-mixture ablation also needs careful matching for training budget, augmentation frequency, and hyperparameter tuning. Without this, the claimed 0.8-point curriculum benefit may partly reflect optimization differences.

#### 3. Insufficient statistical analysis

Although five random seeds are reported, the paper provides no statistical significance tests or confidence intervals for the comparisons. Several gains are relatively small, especially at 1,000 labeled examples. Per-dataset ablation results are also absent, making it difficult to determine whether the effect is robust or driven by one or two datasets.

#### 4. Reproducibility gaps

Important implementation details are missing, including:

- exact BERT checkpoint and preprocessing;
- the back-translation system and translation direction;
- how synonym replacements are selected and disambiguated;
- whether augmentations are applied independently to both views;
- how invalid or excessively short augmented examples are handled;
- the exact projection-head architecture;
- learning rates, schedules, warmup, weight decay, and temperature values;
- the procedure for selecting the 500 labeled examples and validation examples across seeds.

These omissions are especially problematic because augmentation behavior can strongly affect contrastive-learning results.

#### 5. Limited evaluation scope

All datasets are short English classification benchmarks. The paper does not test domain shift, longer documents, multilingual data, different encoder sizes, or transfer to tasks unlike the intermediate-training corpus. Thus, the broader significance of the method remains uncertain.

#### 6. Computational and practical claims need clarification

The paper says back-translated views are precomputed, but CurCon is still approximately 12% slower because of on-the-fly operations. A more detailed accounting of preprocessing, storage, training time, and total wall-clock cost would be useful. It is also unclear whether the computational cost of generating the back-translations is included.

## Criterion-specific evaluation

### Soundness: 46/100

The overall experimental design is plausible, but the unclear curriculum definition, potentially unfair baseline tuning, limited statistical analysis, and missing implementation details substantially weaken the evidence. The central claim—that the schedule itself produces the gains—is not yet convincingly isolated.

### Novelty: 52/100

Scheduling augmentation difficulty for contrastive learning is a reasonable incremental contribution, but the conceptual novelty is modest. The method combines established components—contrastive intermediate training, standard text augmentations, and curriculum scheduling—without a particularly new objective or adaptive mechanism.

### Significance: 55/100

The low-resource setting is important, and the reported improvements could be practically meaningful. However, the gains over CERT are moderate, and the experiments are too narrow to establish broad impact. Stronger controls and wider evaluation could raise the significance considerably.

### Clarity: 78/100

The paper is well structured and readable. The motivation, pipeline, and results are easy to follow. The main clarity issue is technical ambiguity in the augmentation probability schedule and several missing implementation details.

## Final recommendation: **Reject**

The paper has a clear presentation and a potentially useful idea, but the current evidence is not sufficiently rigorous for acceptance. A revised version should precisely define the curriculum policy, tune all baselines comparably, include stronger ablations and statistical tests, and provide enough implementation detail for reliable reproduction.