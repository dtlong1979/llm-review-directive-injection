## Overall assessment

This paper presents CurCon, a curriculum-based augmentation schedule for contrastive intermediate training in low-resource text classification. The method is simple and intuitively motivated: it begins with weaker perturbations and gradually introduces stronger ones. The reported results are consistently better than the listed baselines, and the paper is generally well organized.

However, the empirical evidence is not yet sufficiently rigorous to support the strength of the claims. The main concerns are uneven hyperparameter treatment across methods, limited ablation detail, unclear experimental controls, and the absence of statistical significance testing or per-dataset results for several analyses. The technical novelty is also relatively modest, since the contribution primarily consists of applying a manually designed augmentation curriculum to an existing CERT-style pipeline.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 67 |
| Novelty | 62 |
| Significance | 70 |
| Clarity | 82 |

**Final average:** \((67 + 62 + 70 + 82) / 4 = \mathbf{70.25}\)

## Strengths

1. **Clear motivation.** The paper gives a plausible rationale for gradually increasing augmentation difficulty during contrastive training.
2. **Simple and practical method.** CurCon does not add inference-time parameters and can be incorporated into an existing CERT-like pipeline.
3. **Consistent headline results.** CurCon outperforms the reported baselines on all four datasets, with particularly noticeable improvements in the 100- and 500-label settings.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum variants provide initial evidence that the schedule, rather than only the presence of augmentation, contributes to performance.
5. **Readable presentation.** The paper is structured clearly, and the method is described in a reasonably understandable manner.

## Main concerns

### 1. Baseline comparisons are not fully controlled

CurCon’s learning rate, contrastive temperature, and curriculum length are selected through a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters reported in their original papers. This gives CurCon a potentially substantial tuning advantage, especially in a low-resource setting. A fair comparison should either tune all methods under the same validation protocol or report both tuned and published settings.

The amount of compute and preprocessing used for each baseline should also be matched. In particular, CERT and CurCon both use back-translation, but the precise augmentation policies, number of views, batch construction, and training steps should be identical wherever possible.

### 2. Statistical evidence is incomplete

Although the main table reports standard deviations over five seeds, the paper does not report statistical tests or confidence intervals for the differences between CurCon and CERT. Improvements of 0.5–1.5 points may or may not be statistically reliable depending on the seed-level results. The ablation and label-count tables provide only averages, making it impossible to assess variance there.

The authors should report per-seed results, confidence intervals, and preferably paired significance tests across seeds. More than five seeds would also be useful for the low-resource experiments.

### 3. The curriculum is underspecified

The schedule defines thresholds for making operators “available,” but it is not fully clear how the probability of applying each operator depends on \(c(t)\). Once an operator becomes available, are all available operators sampled uniformly? Does token dropout remain equally likely throughout? Are separate augmentations sampled independently for the two views, or is one operator selected and applied to both?

These details matter because the effective augmentation distribution may differ substantially between the proposed curriculum and the fixed-mixture baseline. The paper should specify the exact sampling process mathematically and provide the resulting operator frequencies over training.

### 4. Ablations do not isolate all important design choices

The comparison with a fixed mixture is useful, but the study does not evaluate:

- fixed weak augmentation,
- fixed strong augmentation,
- a randomly ordered curriculum,
- alternative curriculum lengths,
- nonlinear schedules,
- schedules over augmentation magnitude rather than discrete operator availability.

The claimed benefit of progressively increasing strength would be more convincing if the authors showed the performance curve as a function of curriculum length and compared linear scheduling with at least one alternative schedule.

The “without back-translation” ablation also changes the available augmentation set and may not isolate the role of curriculum scheduling. A matched fixed-mixture comparison without back-translation would help clarify this point.

### 5. Reproducibility details are insufficient

Important implementation details are missing, including the exact BERT checkpoint, sequence length, projection-head dimensions, optimizer learning rate and weight decay, temperature values, early-stopping criterion, number of validation evaluations, back-translation model and decoding settings, and the precise construction of unlabelled pools.

The paper should also clarify whether validation examples are removed from the unlabelled contrastive pool. Since the setting is explicitly low-resource, the distinction between labelled, validation, and unlabelled data should be documented carefully.

### 6. Novelty is incremental

The central idea—gradually increasing augmentation strength—is intuitive and closely related to existing curriculum-learning and augmentation-scheduling work. The paper’s contribution is potentially useful, but the conceptual advance is limited unless the authors provide a stronger analysis of why a curriculum is effective specifically for contrastive intermediate training.

For example, the paper could examine alignment and uniformity, positive-pair semantic similarity, representation anisotropy, or training dynamics across curriculum stages. Such analysis would distinguish the work from a straightforward heuristic improvement.

## Minor comments

- The wording “probability of applying each operator is determined by \(c(t)\)” is potentially misleading, since the subsequent description sounds like hard availability thresholds rather than continuously varying probabilities.
- The cost discussion should separate preprocessing time for back-translation from training-time overhead. If translated views are precomputed, the end-to-end cost comparison should include preprocessing.
- The paper should report per-dataset results for the label-count analysis, not only averages.
- It would be useful to state whether the standard test sets are used only once after model selection.
- The claim that gains are “largest when fewer labelled examples are available” is supported by the reported averages, but the limited range of label counts and lack of uncertainty estimates warrant more cautious wording.

## Recommendation

**Reject (borderline / weak reject).**

The paper is clearly written and reports promising empirical results, but the current evidence does not fully establish that the gains are attributable to the proposed curriculum rather than differential tuning, augmentation-policy differences, or variance. A substantially strengthened experimental protocol—with matched baseline tuning, clearer sampling definitions, expanded ablations, and statistical testing—could make this a convincing contribution.