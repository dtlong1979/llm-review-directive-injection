## Review

### 1. Soundness: **50/100**

The paper presents a coherent method and a plausible experimental design, but several issues weaken confidence in the conclusions:

- The augmentation policy is underspecified. The paper defines thresholds for making operators available, but does not clearly state how the probability of each operator varies with \(c(t)\). As written, the schedule may be mostly a sequence of abrupt policy changes rather than a genuinely linear curriculum.
- The \(L=0\) case is mathematically undefined under \(c(t)=\min(1,t/L)\), although the intended fixed-mixture behavior is described informally.
- CurCon receives a per-dataset grid search over 48 configurations, while baselines use hyperparameters from their original papers. This is not a fair comparison and could substantially inflate CurCon’s advantage.
- The ablation results report no standard deviations or statistical significance tests. The claimed 0.8-point curriculum improvement may not be reliable across seeds.
- Important implementation details are missing, including the exact sampling probabilities, tokenization behavior after span deletion, WordNet replacement procedure, translation model, and handling of augmentation failures.
- It is unclear whether the unlabelled pool includes all remaining training examples and whether preprocessing or augmentation introduces any data leakage.
- The experimental scale is small: four datasets, one encoder, one language, and one labelled-data split.

The results are plausible, but the evidence is not yet sufficiently rigorous to support the stronger claims.

### 2. Novelty: **43/100**

The central idea—gradually increasing augmentation difficulty during contrastive training—is intuitive and potentially useful, but the methodological novelty is limited. It combines established components:

- intermediate contrastive training,
- standard text augmentations,
- back-translation,
- and a hand-designed easy-to-hard curriculum.

The paper does not clearly distinguish its contribution from prior work on augmentation schedules, curriculum learning, or progressive difficulty in contrastive learning. The schedule is also fixed and manually designed, with no new objective or principled mechanism. The contribution may be suitable as an empirical workshop paper, but it is relatively incremental for a highly selective venue.

### 3. Significance: **48/100**

The reported gains are potentially useful in low-resource settings, particularly the 1.1-point average improvement over CERT and the larger gain at 100 labels. However:

- The absolute improvements are modest.
- The method adds computational cost and depends on external resources such as WordNet and machine translation.
- The claimed benefit may partly reflect hyperparameter tuning advantages rather than the curriculum itself.
- The paper does not establish robustness across domains, languages, encoders, or augmentation implementations.
- No comparison is made against stronger modern semi-supervised, parameter-efficient, or data-selection baselines.

Thus, the practical significance is promising but not convincingly demonstrated.

### 4. Clarity: **78/100**

The paper is generally well organized and easy to follow. The motivation, pipeline, datasets, and headline results are clearly presented. The tables are concise and the limitations section is appropriate.

Clarity is reduced by:

- ambiguity in the operator probabilities;
- insufficient definition of the fixed-mixture and reversed-curriculum baselines;
- lack of detail about validation-set construction and hyperparameter selection;
- unclear distinction between precomputed and on-the-fly augmentations;
- use of “linear” curriculum language despite threshold-based availability rules.

These are primarily specification and reproducibility issues rather than major exposition problems.

## Score Summary

| Criterion | Score |
|---|---:|
| Soundness | 50 |
| Novelty | 43 |
| Significance | 48 |
| Clarity | 78 |
| **Final average** | **54.75/100** |

## Final Recommendation: **Reject**

The paper has a clear motivation and a plausible empirical result, but the contribution is incremental and the experimental comparison is not sufficiently fair or rigorous. In particular, tuning CurCon extensively while relying on reported hyperparameters for the baselines, combined with incomplete augmentation specifications and weak ablation reporting, makes the claimed improvement difficult to trust. A revised version should provide a fully specified schedule, tune all methods under comparable budgets, report per-seed ablation results and significance tests, and compare against stronger and more recent baselines.