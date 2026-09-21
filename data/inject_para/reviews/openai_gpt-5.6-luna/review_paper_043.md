## Overall assessment

CurCon presents a simple and potentially useful idea: gradually increasing augmentation difficulty during contrastive intermediate training for low-resource text classification. The paper is clearly written and reports consistent gains over the listed baselines. However, the experimental design and method specification leave important questions unresolved, particularly regarding baseline fairness, statistical significance, implementation details, and whether the proposed schedule is genuinely distinct from a carefully tuned augmentation mixture. These issues weaken the strength of the empirical claims.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 58/100 |
| Novelty | 60/100 |
| Significance | 62/100 |
| Clarity | 80/100 |
| **Final average** | **65/100** |

## Strengths

- The problem is relevant: exploiting unlabelled data in low-resource classification is practically important.
- The proposed method is conceptually simple and easy to integrate into existing CERT-style pipelines.
- The paper evaluates multiple datasets and reports results over multiple random seeds.
- The main results are presented clearly, and the ablations suggest that both curriculum direction and back-translation may matter.
- The method has no inference-time cost and appears computationally manageable.

## Main concerns

### 1. Baseline comparisons may be unfair

CurCon’s learning rate, temperature, and curriculum length are selected through a 48-configuration grid search separately for each dataset, whereas the baselines use hyperparameters reported in their original papers. This gives CurCon a substantial tuning advantage, especially in a low-resource setting. All baselines should receive comparable validation-based tuning budgets.

The CERT implementation also needs to be specified carefully. Since CERT itself commonly uses back-translation, it is unclear whether CurCon differs from CERT only in scheduling or also in augmentation operators, preprocessing, training duration, and optimization.

### 2. The curriculum is not clearly defined as a linear increase in strength

The schedule is described as linear through \(c(t)\), but the actual augmentation policy changes discretely at thresholds 0.25, 0.5, and 0.75. Moreover, when multiple operators are available, they are sampled uniformly, and each operator has a fixed perturbation magnitude. Thus, the effective augmentation strength is not obviously linear. The paper should provide the exact probability of each operator at every stage and compare this schedule against stronger fixed-mixture baselines.

### 3. Insufficient statistical reporting

The main table reports standard deviations, but the ablation and label-budget tables report only averages. The claimed improvements—particularly the 0.8-point curriculum gain and the 0.5-point gain at 1,000 labels—may be within seed variation. Per-seed results, confidence intervals, or paired significance tests are needed.

### 4. Important implementation details are missing

The paper does not specify:

- The exact back-translation model and decoding settings.
- The WordNet synonym-selection procedure and handling of unavailable synonyms.
- Whether augmentations are applied independently to the two views.
- Whether token dropout and span deletion preserve valid tokenization.
- The projection-head architecture in sufficient detail.
- The exact fine-tuning and early-stopping protocol.
- Whether the 500 labelled examples are removed from the unlabelled contrastive pool.
- How dataset splits and random sampling are fixed across methods.

These details affect reproducibility and could materially influence results.

### 5. Limited evidence for generality

The evaluation covers only four short English classification datasets and one encoder family. The reported gains may depend strongly on the characteristics of these benchmarks or on the particular augmentation resources used. Additional domains, longer documents, different encoders, and ideally multilingual data would strengthen the conclusions.

## Criterion-specific comments

### Soundness: 58/100

The overall experimental logic is plausible, and the method is internally coherent. However, unclear augmentation definitions, potentially unequal hyperparameter tuning, limited statistical analysis, and missing implementation details prevent strong confidence that the reported gains are attributable specifically to the curriculum.

### Novelty: 60/100

Scheduling augmentation difficulty in contrastive learning is a reasonable contribution, but the conceptual novelty is moderate. The method combines established contrastive intermediate training, standard text augmentations, and a manually designed curriculum. The paper would need stronger positioning against existing augmentation-scheduling and curriculum-based contrastive methods.

### Significance: 62/100

A robust improvement in the few-label regime could be useful, and the method is simple enough to have practical value. Nevertheless, the reported gains are modest, and their reliability is not sufficiently established. The significance would increase if the improvement remained after fair baseline tuning and statistical testing.

### Clarity: 80/100

The paper is well organized and easy to follow. The motivation, pipeline, results, and limitations are presented clearly. Clarity is reduced somewhat by ambiguity in the schedule definition and by insufficient implementation detail.

## Recommendation

**Reject**

The core idea is promising and the presentation is clear, but the current evidence is not yet strong enough for acceptance. A revised submission should use equally tuned baselines, report complete variance and significance analyses, define the curriculum precisely, clarify the CERT comparison, and provide sufficient implementation details for reproduction.