## Summary

This paper proposes CurCon, an intermediate contrastive-training method that progressively expands the set of text augmentations used during training. It evaluates the method on four low-resource classification benchmarks and reports consistent improvements over fine-tuning, UDA, SimCSE, and CERT.

## Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **55** | The experimental design is plausible and the reported averages are internally consistent. However, important methodological details are underspecified, the baseline comparison is not fully controlled, and statistical evidence is limited. |
| **Novelty** | **62** | Scheduling augmentation difficulty during contrastive intermediate training is a reasonable and potentially useful idea. Nevertheless, the contribution is incremental relative to curriculum learning, augmentation scheduling, and existing contrastive adaptation methods. |
| **Significance** | **60** | The low-resource setting is practically relevant, and the reported gains over CERT are meaningful. The scope is limited to four short English-text benchmarks, and the absolute improvements are modest. |
| **Clarity** | **78** | The paper is generally well organized and easy to follow. The method and experimental sections nevertheless leave several details ambiguous, particularly the exact probability schedule and implementation of the curriculum. |

**Final average:**  
\[
(55 + 62 + 60 + 78)/4 = \mathbf{63.75}
\]

## Strengths

1. **Relevant problem setting.** Few-shot or low-resource text classification with in-domain unlabelled data is important and practically motivated.
2. **Simple method.** CurCon can be incorporated into an existing CERT-style pipeline without changing inference or the downstream fine-tuning objective.
3. **Consistent reported improvements.** CurCon outperforms the listed baselines on all four datasets, with the largest gains in the more label-scarce setting.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons address whether the ordering of augmentations matters.
5. **Readable presentation.** The paper clearly describes the overall motivation, training pipeline, and empirical findings.

## Main concerns

### 1. The curriculum is not fully specified

The paper states that the probability of applying each operator is “determined by” the curriculum level, but the precise probabilities are not given. The description appears to define a staged availability rule followed by uniform sampling, rather than a genuinely linearly increasing augmentation-strength schedule. In particular:

- Token dropout is always available.
- Other operators suddenly become available at fixed thresholds.
- Once available, operators are sampled uniformly.
- It is unclear whether the two views use independent operators.
- It is unclear whether operators can be composed or only one operator is applied per view.
- The meaning of “full strength” is not formally defined.

Moreover, \(c(t)=\min(1,t/L)\) is undefined when \(L=0\), although the paper claims that \(L=0\) corresponds to a fixed mixture. This convention should be stated explicitly.

### 2. Baseline comparisons may be unfair

CurCon’s learning rate, temperature, and curriculum length are selected by a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters from their original papers. This gives CurCon a potentially substantial tuning advantage, especially in a 500-example regime where hyperparameter sensitivity can be high. All baselines should either receive comparable tuning budgets or be evaluated under a clearly justified common protocol.

The paper also does not clarify whether the baselines use exactly the same unlabelled corpus, preprocessing, number of updates, batch size, and encoder initialization.

### 3. Statistical analysis is insufficient

Results are averaged over five random seeds, but no significance tests, confidence intervals, per-seed results, or paired comparisons are provided. The reported improvements over CERT are only 0.5–1.5 points on individual datasets. Standard deviations alone do not establish that these differences are statistically reliable. The paper should report paired seed-level comparisons and confidence intervals, and ideally include multiple corpus splits or repeated labelled-subset samples.

### 4. The data-sampling protocol needs clarification

The paper says that 500 labelled examples are sampled and that the “remaining training sentences” are used without labels. It should clarify:

- Whether the validation examples are sampled from the original training data or from a separate official validation set.
- Whether the same sampled labelled subset is used across methods and seeds.
- Whether the unlabelled corpus includes the validation examples.
- How class stratification is performed for the 100- and 1,000-label experiments.
- Whether any preprocessing or augmentation resources expose information from test data.

These details matter substantially in low-resource experiments.

### 5. Limited scope of evaluation

The study uses only four relatively short English datasets and one encoder family. This is adequate for an initial study, but it limits the strength of the general claims. In particular, the method relies on WordNet and German back-translation, so it is unclear whether the effect would transfer to other languages, domains, or longer documents.

### 6. The contribution is incremental

The central idea—gradually increasing augmentation difficulty—is intuitive and related to existing curriculum-learning and augmentation-scheduling work. The paper would benefit from a stronger comparison to alternative schedules, such as:

- cosine or exponential schedules,
- random schedules,
- schedules based on measured semantic similarity,
- adaptive schedules based on contrastive loss or representation quality.

Without these comparisons, it is difficult to determine whether the benefit comes specifically from the proposed curriculum or simply from a favorable augmentation mixture.

## Minor comments

- The exact CERT and SimCSE implementations should be cited and specified, including the encoder checkpoint and projection-head details.
- The time-cost comparison should include preprocessing and precomputation costs, not only contrastive-training time.
- The paper should report the selected curriculum length and whether it varies by dataset.
- The claim that gains are “largest when fewer labelled examples are available” is supported by only three label regimes and should be stated more cautiously.
- The method would be easier to reproduce with pseudocode and a table of all hyperparameters.
- The distinction between augmentation strength and augmentation type should be made more precise: back-translation is not necessarily uniformly “stronger” than span deletion for every sentence.

## Overall assessment

CurCon is a clear and potentially useful incremental contribution. The reported results are encouraging, and the low-resource application is relevant. However, the current evidence does not fully establish that the curriculum itself is responsible for the improvements because of incomplete schedule specification, unequal baseline tuning, and limited statistical analysis.

**Final recommendation: Reject**

The work could become substantially stronger with a fully specified curriculum, matched hyperparameter tuning for all methods, repeated labelled-subset evaluation, and stronger statistical and schedule-comparison analyses.