## Overall assessment

CurCon presents a plausible and practically motivated extension of contrastive intermediate training: gradually introducing stronger text augmentations before low-resource fine-tuning. The paper is clearly written and the empirical results are consistently positive. However, the methodological contribution is relatively incremental, and the experimental evidence does not yet establish that the gains are specifically due to the proposed curriculum rather than hyperparameter tuning, augmentation composition, or implementation choices. Several important details are underspecified, and the comparison with baselines is potentially unfair.

### Scores

| Criterion | Score | Rationale |
|---|---:|---|
| **Soundness** | **52/100** | The overall pipeline is reasonable, but the evaluation has important weaknesses: CurCon is tuned using a substantial grid search while baselines use original-paper hyperparameters; no significance tests or per-seed results are given; the unlabeled/validation split and sampling protocol are insufficiently specified; and the curriculum definition is ambiguous. The reported ablation supports the method, but does not fully isolate the curriculum from augmentation mixtures and tuning. |
| **Novelty** | **58/100** | Scheduling augmentation difficulty for contrastive intermediate training is a sensible combination of existing ideas, but it is a relatively incremental contribution. The paper does not clearly distinguish its method from prior augmentation-magnitude curricula or adaptive contrastive augmentation methods. The proposed schedule is hand-designed and largely consists of enabling operators at fixed thresholds. |
| **Significance** | **55/100** | The low-resource setting is important, and the reported gains over CERT are potentially useful. Nevertheless, the gains are modest at 500 labels and diminish with more labels. The evaluation covers only four short English datasets and one encoder, limiting evidence of broad impact. The lack of stronger controls makes it difficult to determine whether the improvement would generalize. |
| **Clarity** | **76/100** | The paper is well organized and easy to follow, with a coherent motivation and clear result tables. Some technical details are ambiguous or incomplete, including the exact operator probabilities, the treatment of \(L=0\), data splits, hyperparameter settings, augmentation implementation, and the precise meaning of “linearly” increasing strength. |

### Final average

\[
\frac{52 + 58 + 55 + 76}{4} = \mathbf{60.25}
\]

**Final average score: 60.3/100**

## Main strengths

- Addresses an important practical problem in low-resource classification.
- The method is simple, model-agnostic, and adds no inference-time cost.
- The experimental narrative is coherent: main results, ablations, label-efficiency analysis, and computational cost.
- CurCon improves over all reported baselines on all four datasets.
- The reversed-curriculum ablation is useful and provides some evidence that ordering matters.

## Main concerns

1. **Unfair baseline tuning.** CurCon is tuned over 48 configurations per dataset, whereas the baselines use hyperparameters from their original papers. This is especially problematic in a low-resource regime, where optimization choices can strongly affect results. All methods should receive comparable tuning budgets.

2. **Insufficient statistical evidence.** Five seeds are reported, but there are no paired significance tests, confidence intervals for the averages, or per-seed results. Differences such as 0.5 points at 1,000 labels may not be meaningful.

3. **Ambiguous curriculum specification.** The schedule is described as linear, but augmentation availability changes discontinuously at thresholds. The probabilities of individual operators are not explicitly defined. In addition, \(c(t)=\min(1,t/L)\) is undefined for \(L=0\), despite \(L=0\) being used as an ablation.

4. **Weak isolation of the curriculum effect.** The fixed-mixture comparison changes both the training schedule and the distribution of augmentations over time. A stronger study would compare curricula with matched total operator frequencies, matched compute, and randomly ordered schedules.

5. **Limited scope.** The benchmarks are all English and relatively short, and only BERT-base is evaluated. The method’s dependence on WordNet and German back-translation raises questions about multilingual and domain robustness.

6. **Reproducibility gaps.** The paper should report exact learning rates, temperature values, curriculum lengths selected for each dataset, validation split construction, augmentation seeds, translation system, preprocessing, and whether unlabeled examples overlap with validation or test material.

7. **Cost analysis is unclear.** If back-translated views are precomputed, the source of the reported 12% overhead should be explained, and all baselines should be measured under the same preprocessing and hardware protocol.

## Recommendation

**Reject**

The idea is reasonable and the presentation is strong, but the current evidence is not sufficiently rigorous for acceptance. A revised version could become competitive if it uses fair hyperparameter tuning for all baselines, provides stronger statistical analysis, precisely specifies the curriculum and data splits, and includes controlled ablations that isolate scheduling from augmentation composition and compute.