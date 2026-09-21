## Review

### Summary
This paper introduces Batch-Adaptive Label Smoothing (BALS), which assigns a class-specific smoothing coefficient based on the within-batch dispersion of logits for that class. The method is simple, computationally inexpensive, and evaluated on CIFAR-10 and CIFAR-100 using ResNet-18. The reported results show modest improvements in accuracy and calibration over standard cross-entropy and fixed label smoothing.

### Strengths
- **Simple and practical method:** BALS requires no architectural changes and appears easy to integrate into standard training pipelines.
- **Relevant motivation:** Class-dependent regularization is a reasonable direction because classes can differ in difficulty and prediction stability.
- **Evaluation includes calibration:** Reporting ECE in addition to accuracy is appropriate for a method intended to reduce overconfidence.
- **Reproducibility-oriented setup:** The paper specifies datasets, optimizer, schedule, batch size, and the number of seeds.
- **Consistent, though small, gains:** BALS improves both accuracy and ECE relative to the listed baselines on both datasets.
- **Limitations are acknowledged:** The authors appropriately identify the restricted experimental scope, modest effect sizes, and fairness issues in hyperparameter tuning.

### Weaknesses and suggestions
1. **Limited experimental breadth.** The evaluation uses only one architecture and two relatively small datasets. This is sufficient for an initial empirical study, but broader tests would strengthen the claims. Experiments with stronger augmentations, wider/deeper models, or a larger dataset would help establish generality.

2. **Baseline tuning is not fully matched.** BALS receives validation-based selection of \(k\) and \(s_{\max}\), whereas LS is fixed at \(\epsilon=0.1\). Since label smoothing is also sensitive to its coefficient, a fairer comparison should tune LS over a comparable validation protocol. This limitation is acknowledged by the authors and does not invalidate the reported comparison, but it weakens the strength of the claim that BALS is superior to fixed smoothing.

3. **Statistical evidence is modest.** The accuracy gains are close to the reported seed-to-seed standard deviations. Three seeds provide some evidence of consistency, but confidence intervals, per-seed results, or paired statistical tests would make the conclusions more persuasive.

4. **Method specification could be more precise.** The phrase “standard deviation of logits over examples of class \(c\) and over channels” is potentially ambiguous. It would be useful to specify whether the standard deviation is computed after flattening all class-conditioned logit values, whether it is averaged across class channels, and whether the statistic is detached from the computational graph. The handling of classes absent from a batch also deserves a more explicit algorithmic description, especially because retaining stale values may make the smoothing coefficient depend on earlier batches.

5. **Possible scale dependence.** Logit standard deviation is affected by model calibration and logit scale. The chosen value of \(k\) may therefore be architecture-, optimizer-, or training-stage-dependent. An analysis of the evolution and distribution of \(s_c\), or a normalized dispersion statistic, would clarify robustness.

6. **Limited ablation.** The paper includes a short \(s_{\max}\) ablation but does not separately analyze the role of \(k\), the class-memory mechanism, or alternative dispersion statistics. These would be useful follow-up experiments, although they are not essential for the core contribution.

7. **Calibration evaluation could be expanded.** ECE is useful but sensitive to binning. Reporting additional metrics such as adaptive ECE, negative log-likelihood, or Brier score would provide a more complete assessment.

### Soundness
The method is conceptually coherent, and the experimental setup is sufficiently detailed to support the main limited claim that BALS can provide small gains in the tested settings. The empirical conclusions should be stated cautiously because of the small number of seeds, limited datasets, and unmatched baseline tuning. These are important qualifications rather than fatal flaws.

**Score: 78/100**

### Novelty
The contribution is a straightforward but reasonable extension of label smoothing using batch-level, class-conditional logit statistics. It does not introduce substantial theoretical novelty, but the particular combination is simple, interpretable, and potentially useful in practice.

**Score: 64/100**

### Significance
The reported improvements are small, and the scope is narrow. Nevertheless, the method has attractive implementation simplicity and addresses calibration as well as accuracy. The work is most significant as a practical empirical idea and a useful starting point for further study, rather than as a major advance.

**Score: 66/100**

### Clarity
The paper is generally well organized and easy to follow. The motivation, method, setup, results, and limitations are clearly presented. The main clarity issue is the exact definition and implementation of the logit-dispersion statistic and the persistence rule for classes absent from a batch.

**Score: 86/100**

## Final score

\[
\frac{78 + 64 + 66 + 86}{4}
= \frac{294}{4}
= 73.5
\]

**Final average score: 73.5/100**

## Final recommendation: Accept

The paper presents a clear, lightweight, and empirically promising modification to label smoothing. Although the gains are modest and the evaluation should be broadened in future work, the method is sufficiently sound and well motivated for acceptance, particularly as a practical empirical contribution. The authors should clarify the statistic computation and temper claims regarding superiority until baselines are tuned under a matched protocol.