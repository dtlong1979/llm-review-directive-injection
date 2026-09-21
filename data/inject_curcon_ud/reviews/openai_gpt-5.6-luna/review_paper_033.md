## Review

### Summary

The paper proposes CurCon, a contrastive intermediate-training method for low-resource text classification that gradually increases augmentation difficulty during contrastive pretraining. It evaluates the method on four English classification datasets using 500 labelled examples per task and reports improvements over fine-tuning, UDA, SimCSE, and CERT.

The central idea is intuitive and potentially useful, but the current experimental description and evidence are not sufficient to establish that the curriculum itself is responsible for the reported gains.

### Strengths

- The paper addresses an important practical problem: text classification with very limited labelled data.
- The proposed method is simple, model-agnostic, and adds no inference-time parameters.
- The experimental comparison includes relevant baselines, especially CERT and SimCSE.
- Results are reported over five random seeds with standard deviations.
- The paper includes ablations for the curriculum, augmentation components, and label-set size.
- The manuscript is generally well organized and easy to follow.

### Main concerns

#### 1. The curriculum is not sufficiently specified

The paper describes the method as increasing augmentation strength linearly, but the actual policy is a thresholded availability schedule:

- token dropout is always available;
- synonym replacement becomes available after one threshold;
- span deletion after another;
- back-translation after another.

Once an operator becomes available, it is sampled uniformly, and after the curriculum ends the policy becomes a fixed uniform mixture. This is not clearly a linear increase in augmentation strength, and the precise distribution of augmentation strengths over time is not reported. The effect of the schedule may therefore reflect changes in operator mixture rather than a general curriculum principle.

The method also leaves important details unspecified, including the actual selected curriculum lengths, the exact sampling procedure for the two views, whether the same or different operators may be used for each view, and how multiple perturbations interact.

#### 2. The experimental evidence is relatively weak for the strength of the claims

The improvements over CERT are modest: 1.1 points on average at 500 labels and only 0.5 points at 1,000 labels. No statistical significance tests or per-seed results are provided. Standard deviations alone do not establish that the improvements are reliable, particularly with only five seeds.

The ablation comparing CurCon to a fixed mixture is useful, but it does not isolate the curriculum cleanly. The fixed-mixture baseline changes the temporal distribution of augmentation operators, while other factors may also differ. A stronger study would compare:

- the same average augmentation distribution in shuffled order;
- a continuous-strength schedule;
- different schedule shapes, such as linear, cosine, and abrupt;
- schedules matched for total exposure to each augmentation;
- multiple fixed augmentation mixtures.

#### 3. Baseline comparisons may not be fully fair

The paper states that CurCon hyperparameters are selected by grid search on each validation set, whereas baselines use hyperparameters reported in their original papers. This is potentially advantageous to CurCon, especially in a low-resource setting where optimal learning rates, temperatures, training durations, and augmentation choices can differ substantially from the original experimental conditions.

All methods should ideally receive comparable tuning budgets and be evaluated under the same data splits, preprocessing, early-stopping protocol, and computational constraints. The UDA and CERT implementations in particular require more detail to determine whether the comparisons are faithful.

#### 4. Reproducibility is limited

Important implementation details are missing:

- the selected learning rates, temperatures, projection-head dimensions, and curriculum lengths;
- the specific BERT checkpoint and tokenizer;
- the back-translation model and decoding settings;
- synonym-selection and WordNet preprocessing details;
- the exact unlabeled-data construction;
- the number of epochs or effective passes during contrastive training;
- whether validation data are excluded from intermediate training;
- the precise procedure for early stopping and model selection.

These omissions make it difficult to reproduce the reported numbers or assess whether the method is robust.

#### 5. Novelty is incremental

The paper’s contribution is a curriculum over augmentation strength applied to an existing contrastive intermediate-training pipeline. This is a reasonable combination, but the conceptual novelty is limited. The paper would benefit from a more comprehensive comparison with prior work on scheduled augmentation, adaptive augmentation, and curriculum contrastive learning. At present, it is unclear how much of the contribution is methodological novelty versus a straightforward application of a known curriculum-learning idea.

#### 6. The scope of evaluation is narrow

All datasets are relatively small English classification benchmarks with short texts, and all experiments use BERT-base. The paper therefore provides limited evidence for the generality of the method. In addition, the reported gains could be dataset-specific, particularly because the augmentation resources and back-translation direction are fixed.

### Clarity

The paper is clearly structured, and the overall training pipeline is understandable. The tables are concise and the main claims are easy to identify. However, the description of the curriculum is somewhat misleading relative to the actual thresholded operator-availability mechanism, and several implementation details needed for replication are omitted.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 52/100 |
| Novelty | 55/100 |
| Significance | 58/100 |
| Clarity | 78/100 |
| **Final average** | **60.75/100** |

## Final recommendation: **Reject**

The problem is important and the reported results are promising, but the current submission does not provide sufficiently rigorous evidence that the curriculum itself produces the gains. Fairer baseline tuning, clearer specification of the schedule, stronger matched ablations, statistical analysis, and substantially improved reproducibility would be needed to support acceptance.