## Summary

The paper presents CurCon, a contrastive intermediate-training method that progressively increases text augmentation strength during unsupervised adaptation. The topic is relevant to low-resource classification, and the proposed approach is easy to understand and potentially useful. However, the current experimental evidence does not adequately establish that the curriculum itself is responsible for the reported gains. Important methodological details are underspecified, baseline tuning is potentially unfair, and the evaluation is too limited to support the broader claims.

## Strengths

- Addresses a practically important low-resource classification setting.
- The method is simple, model-agnostic, and does not add inference-time parameters.
- The paper is generally well organized and readable.
- Includes comparisons with fine-tuning, UDA, SimCSE, and CERT.
- Includes ablations for fixed augmentation mixtures, reversed curricula, and removal of back-translation.
- Reports results across multiple datasets and random seeds.

## Major concerns

### 1. The curriculum is not clearly defined as a linear strength schedule

The paper describes the schedule as increasing augmentation strength linearly, but the actual procedure is a set of thresholded availability changes:

- token dropout is always available;
- synonym replacement starts after 0.25;
- span deletion after 0.5;
- back-translation after 0.75.

When several operators are available, they are sampled uniformly. This produces a piecewise-discrete policy rather than a clearly specified linear increase in augmentation magnitude. It is also unclear whether the operator probability changes continuously, whether token dropout remains more frequent than the other operators, and how the two views are sampled.

A precise mathematical definition of the augmentation distribution is needed.

### 2. The main ablation does not isolate the curriculum effect cleanly

The comparison between CurCon and the fixed mixture of all operators is useful, but it does not establish that curriculum ordering is the sole cause of the improvement. The methods may differ in:

- the frequency with which each augmentation is encountered;
- the number of easy versus difficult pairs;
- the effective augmentation distribution over training;
- the timing of exposure to back-translation;
- potentially the quality and diversity of generated views.

A stronger study would compare curricula with matched cumulative augmentation distributions, matched operator exposure, and multiple schedule shapes, such as linear, cosine, stepwise, and random schedules.

### 3. Baseline tuning appears unfair

CurCon is selected through a grid search over 48 configurations for each validation set, whereas the baselines use hyperparameters reported in their original papers. This gives the proposed method substantially more opportunity for dataset-specific optimization. For a fair comparison, all methods should receive comparable tuning budgets, or the paper should clearly report results using both published and tuned baseline configurations.

This issue is especially important given the relatively modest reported gains over CERT.

### 4. Statistical evidence is insufficient

Only five random seeds are used, and no statistical significance tests or confidence intervals for method differences are reported. The tables provide standard deviations for the main results but not for the ablation study or the labelled-data analysis. Since the claimed improvement over CERT is 1.1 average points, paired significance tests across seeds and datasets are important.

The paper should report per-seed results, confidence intervals, and preferably paired tests using identical data splits and seeds across methods.

### 5. Experimental details are insufficient for reproducibility

Several crucial details are missing or ambiguous:

- exact BERT checkpoint and tokenizer;
- contrastive projection-head architecture and whether it is discarded before fine-tuning;
- learning rates, warmup, weight decay, and temperature values;
- number of epochs or stopping criteria for contrastive training;
- exact construction of positive pairs and treatment of failed or malformed back-translations;
- WordNet version and synonym-selection procedure;
- machine-translation model and decoding settings;
- whether augmentation is applied independently to both views;
- whether the 200 validation examples are removed from the unlabelled pool;
- details of UDA and CERT implementations;
- whether all methods use exactly the same unlabelled data and computational budget.

The claim that back-translated views are precomputed but CurCon is nevertheless 12% slower due to on-the-fly operations also requires clarification and supporting measurements.

### 6. Limited evaluation scope

All four datasets are English, relatively short, and established benchmarks. The study uses only BERT-base and one fixed low-resource sampling protocol. This is adequate for an initial study but insufficient to substantiate broad claims about low-resource text classification. Additional domains, longer documents, different encoders, or multiple labelled-data splits would strengthen the work.

The claim that gains are largest in more severely low-resource conditions is supported by only three labelled-data levels and is not accompanied by uncertainty estimates.

## Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **35** | The basic idea is plausible, but the experimental design has important confounds, incomplete methodological details, weak statistical validation, and potentially unfair baseline tuning. |
| **Novelty** | **43** | Scheduling augmentation difficulty during contrastive training is a reasonable incremental contribution, but the conceptual novelty is moderate and closely related to existing curriculum and augmentation-scheduling work. |
| **Significance** | **46** | The low-resource setting is important and the reported gains could be useful, but the improvements are modest and the current evidence does not establish broad or robust impact. |
| **Clarity** | **68** | The manuscript is organized and generally easy to follow, but the augmentation distribution, training protocol, baselines, and evaluation procedure require substantially more precision. |

### Final average

\[
\frac{35 + 43 + 46 + 68}{4} = \mathbf{48.0}
\]

## Final recommendation: **Reject**

The paper has a clear motivation and a potentially useful method, but the current version does not provide sufficiently rigorous evidence that the proposed curriculum, rather than augmentation choice, tuning advantage, or other confounds, produces the reported improvements. A substantially revised submission should use fair baseline tuning, better-controlled curriculum ablations, fuller implementation details, and stronger statistical analysis.