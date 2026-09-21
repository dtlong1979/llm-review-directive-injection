## Review

### Summary

This paper proposes CurCon, an intermediate contrastive-training method that gradually increases the strength of text augmentations during adaptation to unlabeled in-domain data. The method is evaluated on four text-classification datasets in a 500-label setting and is compared with fine-tuning, UDA, SimCSE, and CERT. The reported results show consistent improvements over CERT and larger gains over direct fine-tuning.

### Strengths

- The problem is practically relevant: adapting pretrained encoders when only a small number of labeled examples are available.
- The proposed method is conceptually simple and compatible with a standard contrastive pretraining/fine-tuning pipeline.
- Experiments cover four datasets and include several relevant baselines.
- The ablation comparing the forward curriculum, fixed augmentation mixture, and reversed curriculum is useful.
- The paper is generally well organized and easy to follow.
- Reported gains are consistent across the four datasets rather than being driven by a single benchmark.

### Concerns

#### 1. The curriculum is not clearly defined as a linear strength schedule

Although the paper describes a linearly increasing curriculum level, the actual policy is threshold-based: operators become available at 0.25, 0.5, and 0.75, and available operators are sampled uniformly. This produces abrupt changes in the augmentation distribution rather than a genuinely linear increase in augmentation strength. The method should specify the exact probability distribution over operators at every step and justify why this particular schedule represents increasing difficulty.

The special case \(L=0\) also makes the definition \(c(t)=\min(1,t/L)\) undefined, although the text informally specifies the intended behavior.

#### 2. Baseline comparisons may not be fair

The paper states that CurCon hyperparameters are selected by a 48-configuration grid search for each dataset, whereas the baselines use hyperparameters from their original papers. This can substantially favor CurCon, particularly because the task setting, number of labeled examples, validation protocol, and computational budget may differ from those in the original studies. All methods should be tuned under the same validation protocol and, ideally, comparable compute budgets.

It is also unclear whether the baseline methods use exactly the same unlabeled data, encoder initialization, number of steps, batch size, and preprocessing.

#### 3. The experimental evidence is relatively limited

Only five random seeds are reported, and the paper provides no significance tests or per-seed results. The improvements over CERT are modest on some datasets, especially at 1,000 labels. Confidence intervals or paired seed-level comparisons would help establish whether the improvements are robust.

The ablation table reports only mean accuracies, without standard deviations. In addition, the ablation does not isolate all important design choices. For example, there is no comparison against:

- a continuously mixed augmentation-strength schedule;
- a schedule with the same operator frequencies but randomly ordered over time;
- different curriculum lengths;
- fixed-strength policies matched for expected augmentation severity;
- alternative operator orderings.

Without these controls, it is difficult to determine whether the benefit comes from curriculum ordering, the changing operator mixture, or simply the particular final augmentation distribution.

#### 4. The method description lacks reproducibility details

Important implementation details are missing, including:

- the exact InfoNCE formulation and projection-head dimensions;
- the temperature search range and selected values;
- learning rates, warmup, weight decay, and optimizer settings;
- the exact behavior when an augmentation cannot be applied;
- whether each view receives independently sampled operators;
- the back-translation model and decoding settings;
- the synonym-selection procedure and handling of ambiguous synonyms;
- the precise train/validation split construction and whether the 500 labeled examples are excluded from unlabeled contrastive training.

These details matter because synonym replacement, span deletion, and back-translation can have very different effects across sentiment, topic, and question-classification tasks.

#### 5. Potential label-preservation issues are not examined

Some augmentations may alter the label, particularly synonym replacement and span deletion for sentiment or subjectivity classification. The paper assumes that all operators preserve labels but provides no qualitative analysis or filtering procedure. An analysis of augmentation validity, or at least examples and failure rates, would strengthen the argument.

#### 6. Claims about low-resource behavior are somewhat overstated

The paper concludes that gains are largest when labels are scarce, but the evidence includes only 100, 500, and 1,000 labels and reports only averages. The trend is plausible, but it would be stronger with multiple sampling replicates, variance estimates, and results over a broader range of label budgets.

#### 7. Compute comparisons are incomplete

CurCon is reported to take approximately 12% longer than CERT, but the comparison does not clarify whether preprocessing, back-translation generation, or storage costs are included. Since augmentation cost is central to the method, wall-clock time, preprocessing cost, and total compute should be reported consistently for all methods.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 58/100 |
| Novelty | 63/100 |
| Significance | 62/100 |
| Clarity | 80/100 |

**Final average:** \((58 + 63 + 62 + 80) / 4 = 65.75\)

### Overall assessment

The paper presents a clear and potentially useful idea, and the reported results are encouraging. However, the contribution is fairly incremental, and the current experimental design does not sufficiently establish that the gains are caused by the curriculum itself rather than by differences in augmentation mixtures, tuning effort, or compute. The lack of detailed reproducibility information and matched baseline tuning further weakens the empirical conclusions.

**Final recommendation: Reject**