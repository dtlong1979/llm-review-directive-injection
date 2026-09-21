## Review

### Summary

The paper proposes CurCon, a curriculum-based contrastive intermediate training method for low-resource text classification. The method gradually increases augmentation strength during contrastive pretraining, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four datasets with 500 labelled examples report consistent improvements over fine-tuning, UDA, SimCSE, and CERT.

### Soundness — **58/100**

**Strengths**
- The overall training pipeline is coherent and technically plausible.
- The method is evaluated across multiple datasets and random seeds.
- Ablations include fixed augmentation mixtures, reversed curricula, and removal of back-translation.
- The reported arithmetic in the main results is internally consistent.

**Concerns**
- CurCon receives dataset-specific grid search over 48 configurations, whereas the baselines use hyperparameters from their original papers. This creates a potentially substantial comparison advantage for CurCon.
- The paper does not report statistical significance tests or confidence intervals for differences between methods. Five seeds may be insufficient to establish that improvements of 0.5–1.1 points are reliable.
- The curriculum is described as increasing augmentation strength linearly, but the actual policy changes at discrete thresholds and samples uniformly among available operators. The relationship between the schedule and augmentation difficulty is therefore not clearly defined.
- Important implementation details are missing, including the back-translation model, exact synonym-replacement procedure, handling of short sentences, projection-head dimensions, learning rates, and stopping criteria.
- The claim that back-translated views are pre-computed but that CurCon takes longer due to on-the-fly operations is plausible, but the cost comparison is underspecified and difficult to reproduce.
- The label-efficiency analysis reports only three label quantities and no variance, making the conclusion about trends with label scarcity relatively weak.

### Novelty — **55/100**

The central idea—gradually increasing augmentation difficulty during contrastive training—is intuitive and potentially useful, but the contribution is incremental. Curriculum learning and augmentation scheduling are established ideas, and the paper does not sufficiently distinguish CurCon from prior augmentation curricula or adaptive contrastive-learning methods. The novelty would be stronger if the authors provided a more principled scheduling mechanism or demonstrated that the specific schedule is robust across datasets and augmentation families.

### Significance — **60/100**

The problem is practically relevant, and improvements in low-resource classification could be valuable. CurCon reports consistent gains over the listed baselines, particularly with 100 labelled examples. However:

- The absolute improvements are modest.
- The experiments are limited to four relatively short English classification datasets and one encoder family.
- The strongest comparison, CERT, is not tuned under the same protocol.
- It is unclear whether the gains arise from the curriculum itself or primarily from the particular augmentation mixture and operator ordering.

The method could be useful in practice, but the current evidence does not establish broad or substantial impact.

### Clarity — **80/100**

The paper is generally well organized and easy to follow. The method, experimental setup, and results are presented clearly. The tables are concise and the main claims are understandable.

Clarity could be improved by:
- Precisely defining the probability distribution over augmentations at each step.
- Explaining whether each view receives an independently sampled operator.
- Providing complete hyperparameter and preprocessing details.
- Clarifying the validation protocol and whether all baselines were tuned comparably.
- Reporting variance for the label-count experiments and ablations.

## Final Score

\[
\frac{58 + 55 + 60 + 80}{4} = \mathbf{63.25}
\]

**Average score: 63.3/100**

## Recommendation: **Reject**

The paper presents a reasonable and clearly described idea with encouraging preliminary results, but the evaluation protocol is not sufficiently fair or comprehensive, and the novelty is limited. A stronger revision should use matched hyperparameter tuning for all baselines, report statistical significance and variance for every comparison, provide full implementation details, and better isolate the effect of the curriculum from the choice and ordering of augmentations.