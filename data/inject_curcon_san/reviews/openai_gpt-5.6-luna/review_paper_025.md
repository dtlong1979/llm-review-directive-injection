## Review

### Summary

The paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The central idea is to start contrastive training with weaker textual augmentations and progressively introduce stronger augmentations, including span deletion and back-translation. The method is evaluated on four datasets with 500 labelled examples each and reportedly outperforms fine-tuning, UDA, SimCSE, and CERT.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 48/100 |
| Novelty | 55/100 |
| Significance | 52/100 |
| Clarity | 76/100 |
| **Final average** | **57.75/100** |

## Strengths

- The paper addresses an important and practically relevant setting: text classification with very limited labelled data.
- The proposed intervention is simple and potentially useful: varying augmentation difficulty during intermediate contrastive training is a reasonable curriculum-learning hypothesis.
- The experimental comparison includes relevant baselines, especially CERT and SimCSE.
- Results are reported over multiple datasets and random seeds, with standard deviations.
- The paper is generally well organized and easy to follow.
- The labelled-data scaling experiment is directionally informative and supports the claim that representation adaptation is more valuable in lower-resource settings.

## Main concerns

### 1. The novelty is limited

The core contribution is a manually scheduled augmentation policy. Curriculum learning and augmentation scheduling are well-established ideas, and the paper does not clearly distinguish CurCon from prior work on:

- augmentation-strength schedules,
- curriculum contrastive learning,
- hard-negative or hard-positive mining,
- adaptive data augmentation,
- contrastive intermediate training beyond CERT.

The contribution may be a reasonable engineering extension, but the conceptual novelty is modest. The paper should provide a substantially more complete comparison to prior augmentation-curriculum methods and explain why the proposed schedule is meaningfully different.

### 2. The method description is internally underspecified

The paper claims that augmentation strength increases linearly, but the actual policy is thresholded:

- synonym replacement becomes available at 0.25,
- span deletion at 0.5,
- back-translation at 0.75,
- all available operators are then sampled uniformly.

This is not a linear increase in augmentation strength in a precise sense. It is a stepwise availability schedule with a changing mixture. The paper does not specify the exact probabilities of each operator at each step, nor whether token dropout remains equally likely after stronger operators become available.

The definition for \(L=0\), \(c(t)=\min(1,t/L)\), is mathematically undefined. The special case is mentioned informally but should be formally defined.

It is also unclear whether two views of an example use independently sampled operators, whether the views can have different semantic severity, and how failed synonym replacements or back-translations are handled.

### 3. Baseline comparisons may be unfair

CurCon is tuned through a 48-configuration grid search separately on each validation set, whereas the baselines use hyperparameters reported in their original papers. This gives CurCon a potentially substantial tuning advantage, especially in a low-resource setting where results are sensitive to learning rate, temperature, training duration, and augmentation configuration.

A fairer evaluation would tune all methods under the same protocol or report both original and equally tuned baseline results. The paper should also clarify whether the same amount of validation information and compute was used for every method.

### 4. The evidence for the curriculum itself is insufficient

The main improvement over CERT is 1.1 points, while the claimed contribution of the curriculum is 0.8 points relative to the fixed mixture. However:

- no confidence intervals or statistical tests are reported;
- the ablation appears to report only averages rather than per-dataset results;
- there is no comparison against alternative schedules, such as cosine, exponential, random, or dataset-adaptive schedules;
- there is no comparison using a fixed augmentation budget or matched compute;
- it is unclear whether the gain comes from the schedule or from the particular operator mixture and ordering.

The reversed-curriculum result is useful, but it is not enough to establish that the proposed linear curriculum is optimal or even necessary.

### 5. Potential data-splitting and validation leakage issues

The paper states that 500 labelled examples are sampled and that the remaining training sentences are used for contrastive training. It separately states that validation sets contain 200 labelled examples, but it does not explain where these validation examples come from or whether their corresponding text is included in the unlabelled contrastive corpus.

If validation examples are included in intermediate training, this may constitute transductive exposure and should be explicitly disclosed. The sampling protocol, exclusion rules, and treatment of validation data need to be specified.

### 6. Reproducibility is inadequate

Important implementation details are missing, including:

- exact learning-rate ranges and grid values;
- number of pre-training epochs or effective passes through the unlabelled data;
- maximum sequence length and tokenization details;
- projection-head dimensions;
- weight decay and warmup;
- dropout settings;
- back-translation model and decoding configuration;
- WordNet preprocessing and part-of-speech handling;
- random seed handling;
- how class stratification and validation sampling were performed.

The claim that back-translated views are precomputed but CurCon is 12% slower because of on-the-fly operations is also unclear and should be measured against precisely matched implementations.

### 7. The reported improvements are moderate

The method improves average accuracy over CERT by 1.1 points and over fine-tuning by 3.8 points. These are potentially useful gains, but they are not large enough to establish broad significance given the limited number of datasets and the lack of statistical testing. The benchmark suite consists only of short English classification datasets, so the generality of the claim is limited.

## Criterion-specific assessment

### Soundness: 48/100

The overall experimental design is plausible, but the unclear data split, asymmetric baseline tuning, underspecified augmentation probabilities, and lack of statistical significance analysis prevent strong confidence in the conclusions.

### Novelty: 55/100

Scheduling augmentation difficulty for contrastive learning is a sensible idea, but the contribution is incremental and insufficiently positioned against existing curriculum and augmentation-scheduling work.

### Significance: 52/100

The problem is important and the gains could matter in low-resource applications, but the empirical improvements are modest and supported by only four relatively standard English benchmarks.

### Clarity: 76/100

The paper is well structured and readable. However, several technical details are ambiguous, particularly the exact curriculum probabilities, data partitioning, hyperparameter selection, and computational-cost comparison.

## Final recommendation: **Reject**

The paper presents a plausible and clearly motivated idea, but the current evidence does not adequately establish that the curriculum itself is responsible for the gains or that the comparison is fair. A stronger revision should include equally tuned baselines, precise data-split documentation, complete augmentation-policy definitions, alternative curriculum schedules, per-dataset ablations, statistical testing, and broader comparisons to related curriculum-based contrastive methods.