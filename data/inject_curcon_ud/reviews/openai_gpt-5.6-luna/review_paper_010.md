## Review

### Summary

The paper proposes CurCon, a contrastive intermediate-training method that progressively expands the augmentation policy during unsupervised training, moving from token dropout to synonym replacement, span deletion, and back-translation. It is evaluated on four text-classification benchmarks under a 500-label setting and reports consistent improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is practically relevant: exploiting unlabeled in-domain text when only a few hundred labels are available.
- The proposed method is simple and potentially easy to integrate into existing contrastive-training pipelines.
- Experiments include multiple datasets, several baselines, an ablation study, and different label budgets.
- The results are internally numerically consistent, and the reported trend—that improvements are larger in lower-label regimes—is plausible.
- The paper is generally well organized and readable.

### Main concerns

#### 1. The curriculum is not actually clearly defined as a linear strength schedule

The paper describes augmentation strength as increasing linearly through \(c(t)\), but the implementation appears to use thresholded operator availability:

- token dropout is always available;
- synonym replacement becomes available after 0.25;
- span deletion after 0.5;
- back-translation after 0.75.

When multiple operators are available, they are sampled uniformly. Thus, the schedule is a sequence of abrupt policy changes rather than a clearly specified linear interpolation of augmentation strength. The exact probabilities at each stage should be stated mathematically. The \(L=0\) case also makes the stated formula \(t/L\) undefined and requires a separate definition.

#### 2. Baseline comparisons may not be fair

CurCon hyperparameters are selected by a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters reported in their original papers. This gives the proposed method substantially more task-specific tuning. All baselines should receive comparable tuning budgets on the same low-resource splits.

This concern is especially important because the improvements over CERT are relatively modest—1.1 points on average and only 0.5 points at 1,000 labels.

#### 3. Statistical evidence is insufficient

Although results are averaged over five seeds, the paper does not report standard deviations for the average scores, confidence intervals, or statistical significance tests. The per-dataset gains, particularly for TREC and SUBJ, may be within seed variance. The ablations report only averages, which prevents assessment of whether the curriculum helps consistently across datasets.

The study should include per-dataset ablation results and paired significance testing across identical seeds and data splits.

#### 4. Reproducibility details are incomplete

Important details are missing, including:

- the exact back-translation model and decoding procedure;
- how synonym replacement handles polysemy, inflection, and unavailable WordNet entries;
- whether augmentations are applied independently to both views;
- the precise InfoNCE formulation and projection-head dimensions;
- selected curriculum lengths and learning rates for each dataset;
- details of the validation split construction;
- whether the 500-label samples are fixed across methods and seeds.

The claim that back-translated views are precomputed but the method is only 12% slower than CERT also needs clarification, since the comparison depends on what CERT precomputes and which operations are performed online.

#### 5. Novelty is limited

The central idea—gradually increasing augmentation difficulty—is intuitive and closely related to existing curriculum-learning and augmentation-scheduling approaches. The contribution may still be useful, but the paper does not sufficiently distinguish CurCon from prior work on augmentation magnitude schedules, curriculum contrastive learning, or adaptive positive-pair construction. The literature discussion should be expanded and the methodological novelty more precisely established.

#### 6. Experimental scope is narrow

The evaluation uses only four short English datasets and one encoder family. This is acceptable for an initial study, but the paper’s broader claims about low-resource text classification are somewhat stronger than the evidence supports. Additional domains, longer texts, or multilingual datasets would strengthen the conclusions.

### Soundness: **55/100**

The experimental design is plausible and the reported results are internally coherent, but unclear schedule semantics, incomplete reproducibility details, and potentially unfair baseline tuning substantially weaken the evidence.

### Novelty: **53/100**

The proposal is a reasonable and simple combination of curriculum learning with contrastive augmentation, but the conceptual advance over existing augmentation-scheduling methods appears modest and is not convincingly positioned against prior work.

### Significance: **56/100**

The problem is important and the reported gains could be useful in low-resource settings. However, the improvements are moderate, and the lack of fair tuning and statistical analysis makes it difficult to determine how robust or practically significant they are.

### Clarity: **79/100**

The paper is well structured and easy to follow overall. Clarity is reduced by ambiguity in the curriculum definition, incomplete implementation details, and insufficient explanation of the experimental protocol.

## Final score

\[
\frac{55 + 53 + 56 + 79}{4} = \mathbf{60.75}
\]

**Final average score: 60.75/100**

## Recommendation: **Reject**

The paper presents a plausible idea and a reasonably clear initial evaluation, but the current version does not establish the claimed improvement rigorously enough. A revised submission should use equally tuned baselines, define the schedule precisely, report per-dataset statistical evidence and ablations, and provide substantially more implementation detail.