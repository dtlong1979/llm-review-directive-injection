## Overall assessment

CurCon presents a simple and practically motivated extension of contrastive intermediate training: progressively increasing augmentation difficulty during unsupervised adaptation. The empirical results are consistently positive across four datasets and multiple label regimes, and the ablations support the claim that curriculum ordering—not merely the use of augmentations—contributes to performance.

The main weaknesses concern experimental detail and methodological precision. In particular, the curriculum is described as linear, but the actual operator-selection policy is thresholded and piecewise constant; baseline hyperparameters are not tuned under the same procedure; and statistical significance testing or per-seed comparisons are not reported. These issues reduce confidence in the exact magnitude of the claimed gains but do not undermine the central contribution.

## Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **78** | The method is technically plausible, the experimental design includes relevant baselines and ablations, and results are consistent across datasets. However, the treatment of baseline tuning, validation-set reuse, statistical significance, and the precise curriculum implementation should be clarified. |
| **Novelty** | **72** | Scheduling augmentation difficulty during contrastive intermediate training is a reasonable and useful idea, but it is an incremental extension of existing curriculum-learning and contrastive-adaptation techniques. The novelty lies primarily in the application and empirical validation of the schedule to low-resource text classification. |
| **Significance** | **78** | The problem is important and practically relevant. The reported gains over CERT are moderate but consistent, especially in the 100-label setting, and the method adds no inference cost. Broader validation across languages, domains, and encoders would be needed to establish wider impact. |
| **Clarity** | **84** | The paper is well organized and easy to follow. The motivation, training pipeline, tables, and limitations are clearly presented. Some implementation details and the exact augmentation-probability schedule require additional precision. |

### Final average

\[
\frac{78 + 72 + 78 + 84}{4} = \frac{312}{4} = \mathbf{78.0}
\]

## Strengths

1. **Clear motivation:** The paper addresses a genuine limitation of fixed augmentation policies in low-resource contrastive adaptation.
2. **Simple and deployable method:** CurCon introduces no inference-time parameters or architectural changes.
3. **Consistent empirical improvements:** CurCon outperforms all listed baselines on all four datasets and shows larger gains when labels are scarcer.
4. **Useful ablations:** The fixed-mixture and reversed-curriculum comparisons provide evidence that the ordering of augmentation difficulty matters.
5. **Appropriate limitations discussion:** The paper acknowledges restrictions to English, short texts, BERT-base, and hand-designed schedules.

## Main concerns and suggested revisions

1. **Clarify the curriculum definition.** The method is described as linearly increasing augmentation strength, but the actual policy makes operators available at thresholds of 0.25, 0.5, and 0.75 and then samples uniformly from available operators. This is a piecewise schedule rather than a strictly linear increase in augmentation strength. The paper should define the exact sampling probabilities at each stage and explain how “strength” is measured.

2. **Resolve the \(L=0\) definition.** Since \(c(t)=\min(1,t/L)\) is undefined for \(L=0\), the fixed-mixture case should be specified separately in the formal definition.

3. **Improve baseline comparability.** CurCon is tuned over 48 configurations on each validation set, whereas the baselines use hyperparameters from their original papers. Tuning all methods under a comparable protocol, or at least reporting the sensitivity of CurCon to its selected hyperparameters, would strengthen the conclusions.

4. **Report statistical testing.** Five random seeds are useful, but confidence intervals, paired seed-level comparisons, or significance tests would help determine whether the 0.5–1.5 point gains over CERT are robust.

5. **Add per-dataset ablation results.** Reporting only average ablation accuracy obscures whether the curriculum helps uniformly or is driven by one or two datasets.

6. **Provide more reproducibility details.** The paper should specify the back-translation model, WordNet processing, tokenization behavior, temperature and learning rates, early-stopping criteria, and whether preprocessing and augmented views are identical across methods.

## Recommendation

**Accept**

The contribution is incremental but well motivated, clearly presented, and supported by consistent experimental evidence. With clarification of the schedule, more rigorous baseline tuning, and stronger statistical reporting, the paper would provide a useful and reproducible contribution to low-resource text classification.