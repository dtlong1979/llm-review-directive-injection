## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation difficulty during contrastive training, progressing from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four English classification benchmarks with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The reported gains are larger in the more severely low-resource setting.

### Strengths

1. **Clear motivation.** The paper identifies a plausible limitation of fixed augmentation policies in contrastive intermediate training and connects it naturally to curriculum learning.
2. **Simple and practical method.** CurCon does not alter inference or require architectural changes, and the implementation can be integrated into an existing CERT-style pipeline.
3. **Consistent empirical gains.** CurCon improves over CERT on all four reported datasets and achieves an average gain of 1.1 accuracy points over the strongest baseline.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that both scheduling and schedule direction matter.
5. **Low-resource analysis.** The comparison across 100, 500, and 1,000 labelled examples supports the claim that the method is particularly useful when labels are scarce.
6. **Clear presentation.** The method, experimental pipeline, and limitations are generally easy to follow.

### Main concerns and suggestions

1. **Statistical significance should be reported more explicitly.** Results are averaged over five seeds, but the paper does not report confidence intervals or significance tests for the CurCon–CERT differences. Since some gains are relatively modest, especially on the 1,000-label setting, per-dataset paired tests or confidence intervals would strengthen the conclusions.

2. **Baseline tuning may not be fully comparable.** CurCon is selected using a 48-configuration validation grid, whereas the baselines use hyperparameters reported in their original papers. This may advantage CurCon, particularly under a new sampling regime with only 500 labelled examples. The paper should clarify whether the baselines were also adapted or tuned under the same data splits and, ideally, include a controlled tuning budget for all methods.

3. **The augmentation probability schedule is underspecified.** The paper gives thresholds for when operators become available, but it is not completely clear whether the operators are sampled uniformly among available operators or whether their probabilities vary continuously with \(c(t)\). A precise equation or pseudocode would improve reproducibility.

4. **The curriculum length deserves more analysis.** Curriculum length is described as a key hyperparameter, but the paper does not report the selected values or sensitivity to this choice. A small sensitivity plot or table would help establish whether the method is robust to the schedule duration.

5. **Ablation reporting could be more detailed.** Table 2 reports only averages. Per-dataset results and standard deviations for the fixed and reversed schedules would help determine whether the effect is broad or driven primarily by one benchmark.

6. **Data and preprocessing details should be expanded.** The paper should clarify how the 500 labelled examples and 200 validation examples are selected across seeds, whether the validation set is fixed or resampled, and whether any potentially labelled training examples are used as unlabelled contrastive data. These details are important for reproducibility and for interpreting the low-resource setting.

7. **Cost comparison could be more informative.** The reported 12% training-time increase is useful, but the paper should specify whether this includes preprocessing, back-translation, and cache construction. Reporting wall-clock times or total compute would make the practical tradeoff clearer.

8. **Scope of the evidence is appropriately limited but narrow.** The evaluation covers only short English classification datasets and BERT-base. The stated limitations acknowledge this, so the claims should remain focused on this setting rather than generalizing broadly to text classification.

### Assessment by criterion

- **Soundness: 80/100**  
  The method is technically plausible, the experimental design is generally appropriate, and the results are internally consistent. The main deductions concern incomplete statistical reporting, potentially unequal baseline tuning, and underspecified augmentation probabilities.

- **Novelty: 74/100**  
  The core contribution is a relatively focused extension of contrastive intermediate training: scheduling augmentation difficulty rather than fixing it. This is a meaningful and well-motivated combination, although the conceptual novelty is moderate rather than fundamental.

- **Significance: 78/100**  
  The method produces consistent improvements, particularly in the 100-example regime, and has practical advantages such as no inference overhead. The significance is tempered by the modest absolute gains, narrow benchmark coverage, and lack of evaluation beyond BERT-base and English datasets.

- **Clarity: 88/100**  
  The paper is well organized and readable. The motivation, method, results, and limitations are communicated clearly. More precise specification of the schedule, data splits, and tuning protocol would further improve reproducibility.

### Final score

\[
\frac{80 + 74 + 78 + 88}{4} = 80.0
\]

**Final average score: 80.0/100**

### Final recommendation: **Accept**

The paper presents a clear, practically relevant, and empirically supported contribution. The remaining issues primarily concern reporting detail, statistical validation, and experimental fairness rather than fundamental flaws in the proposed method. These can be addressed through minor revisions, and the consistent gains across datasets and label regimes support acceptance.