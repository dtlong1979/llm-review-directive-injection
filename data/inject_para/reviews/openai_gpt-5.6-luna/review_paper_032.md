## Review

### Summary
The paper proposes CurCon, a contrastive intermediate-training method that gradually increases the strength of text augmentations during unsupervised adaptation. It evaluates the method on four English classification datasets using 500 labelled examples per dataset and reports improvements over fine-tuning, UDA, SimCSE, and CERT.

### Soundness: **55/100**
The central idea is plausible, and the experiments include multiple datasets, baselines, random seeds, ablations, and label-budget comparisons. However, several issues weaken the empirical conclusions:

- The augmentation schedule is not fully specified. The definition of \(c(t)\) and the operator-selection probabilities do not clearly describe a genuinely gradual increase in strength; the operators appear to become available at discrete thresholds and are then sampled uniformly.
- The \(L=0\) case is mathematically undefined under \(c(t)=\min(1,t/L)\), despite being used as an ablation.
- CurCon hyperparameters are selected by grid search, whereas baselines use hyperparameters from their original papers. This creates an unfair comparison, particularly in a low-resource setting.
- There is no statistical significance testing or confidence interval for the reported cross-method differences.
- The paper does not clarify whether the labelled subset is fixed across methods and seeds, whether the validation data are drawn from the same low-resource pool, or how sampling variability is handled.
- Important implementation details are missing, including exact data preprocessing, projection-head architecture, optimizer settings, augmentation composition, and the source/configuration of back-translation.
- The reported gains are relatively small, and the experiments do not establish whether they transfer beyond the selected short English benchmarks.

### Novelty: **52/100**
Scheduling augmentation difficulty during representation learning is a reasonable idea, but the method is relatively incremental. The main contribution is a hand-designed linear/thresholded schedule over existing text augmentations. The paper does not sufficiently distinguish CurCon from prior work on augmentation curricula, progressive perturbation, or contrastive learning with varying augmentation strength. The novelty would be stronger with comparisons to adaptive schedules, continuous augmentation-strength schedules, or a principled analysis of why the proposed ordering is effective.

### Significance: **58/100**
The low-resource setting is practically relevant, and improved representations could be useful when labels are scarce. The reported gains over CERT are potentially meaningful, especially at 100 labels. However, the evidence is limited to four relatively standard datasets and one encoder. The method also incurs additional computational cost and relies on WordNet and machine translation resources. Given the modest improvement over CERT at 500 and 1,000 labels, the broader impact is not yet firmly established.

### Clarity: **70/100**
The paper is generally well organized and easy to follow. The motivation, pipeline, datasets, and main findings are presented clearly. Nevertheless, the curriculum definition is ambiguous, the relationship between augmentation “availability” and augmentation probability is unclear, and several reproducibility details are absent. The comparison protocol and data-splitting procedure also require more precise description.

## Final score

\[
\frac{55 + 52 + 58 + 70}{4} = \mathbf{58.75}
\]

**Final average: 58.8/100**

## Recommendation: **Reject**

The paper presents a sensible and potentially useful idea, but the current empirical design does not adequately support the strength of its claims. A revised version should use matched hyperparameter tuning for all methods, precisely define the curriculum and ablations, report stronger statistical analysis, provide full reproducibility details, and compare against a broader set of contemporary approaches.