## Review

### Summary

The paper proposes CurCon, a curriculum for contrastive intermediate training in which text augmentations become progressively stronger during training. It evaluates the method on four low-resource classification datasets using 500 labelled examples per task and reports improvements over fine-tuning, UDA, SimCSE, and CERT. The idea is intuitive and the empirical results are promising, but the paper has important methodological and reporting weaknesses that make the conclusions difficult to validate.

### Strengths

- Addresses a practically relevant low-resource classification setting.
- The proposed method is simple, model-agnostic, and introduces no inference-time parameters.
- Evaluates across four datasets and includes multiple baselines.
- Reports results over multiple random seeds and includes ablations for curriculum direction, back-translation, and labelled-data scale.
- The paper is generally well organized and easy to follow.

### Main concerns

#### 1. The curriculum is underspecified and internally inconsistent

The schedule defines a scalar curriculum level and threshold-based operator availability, but it does not clearly define the probability of selecting each augmentation. Once several operators are available, the paper says they are sampled uniformly, which means the augmentation distribution changes discontinuously rather than increasing linearly in strength.

Moreover, the statement that \(L=0\) yields a fixed mixture conflicts with the formula \(c(t)=\min(1,t/L)\), which is undefined for \(L=0\). The exact behavior at the thresholds and whether the two views receive independently sampled operators are also unclear. These details materially affect the method and need to be specified precisely.

#### 2. The experimental comparison may be unfair

CurCon is tuned using a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters from their original papers. This gives CurCon substantially more task-specific tuning and makes the reported gains difficult to attribute solely to the curriculum. Baselines should receive comparable tuning budgets, or the paper should report both standard and fairly tuned comparisons.

The paper also does not state whether the validation examples are excluded from the unlabelled corpus used for contrastive training. If validation sentences are included without labels during intermediate training, this should be explicitly disclosed and applied consistently.

#### 3. Evidence for the curriculum effect is limited

The fixed-mixture ablation shows a 0.8-point average difference, but only aggregate results are reported. There are no per-dataset ablations, standard deviations, confidence intervals, or statistical tests for this comparison. Given the small number of seeds and relatively modest improvements, it is not clear whether the curriculum effect is statistically reliable.

The reversed-curriculum result is suggestive, but it is also not clear whether it is matched for augmentation frequency, compute, or the exact distribution of views.

#### 4. Reproducibility is insufficient

Important implementation details are missing, including:

- the exact definition of operator probabilities;
- how synonym replacement handles unavailable or ambiguous WordNet entries;
- the back-translation model and decoding settings;
- tokenizer and sequence-length details;
- projection-head dimensions;
- learning-rate and temperature values selected by grid search;
- the precise construction of labelled, validation, and unlabelled splits;
- whether results use identical splits across methods.

The reported 12% computational overhead also needs more detail, including whether preprocessing and translation costs are included.

#### 5. Claims are somewhat stronger than the evidence supports

The paper claims that CurCon obtains the best average accuracy and that gains are largest with fewer labels, which is supported descriptively. However, the conclusions should be more cautious because the evaluation covers only four small English datasets, uses one encoder, and does not establish statistical significance. The broad claim that the curriculum itself is responsible for the improvements is not yet fully demonstrated.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 45/100 |
| Novelty | 55/100 |
| Significance | 54/100 |
| Clarity | 74/100 |
| **Final average** | **57.0/100** |

### Recommendation: **Reject**

The core idea is plausible and the presentation is clear, but the current paper does not provide sufficiently rigorous or reproducible evidence for publication. The inconsistent curriculum specification, unequal hyperparameter tuning, limited statistical analysis, and missing experimental details are substantial issues. A revised version should precisely define the schedule, tune all baselines comparably, report per-dataset ablations with uncertainty or significance testing, clarify data usage, and provide enough implementation detail for replication.