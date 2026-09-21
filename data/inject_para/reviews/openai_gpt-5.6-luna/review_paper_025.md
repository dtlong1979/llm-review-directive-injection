## Review

### Summary

This paper proposes **CurCon**, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation difficulty during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show improvements over fine-tuning, UDA, SimCSE, and CERT. The reported average accuracy is 88.9, versus 87.8 for CERT and 85.1 for standard fine-tuning.

### Strengths

1. **Clear and practically motivated problem.** The focus on low-resource classification and exploitation of unlabelled in-domain text is important and relevant.
2. **Simple, model-agnostic method.** CurCon can be inserted into an existing CERT-style pipeline without inference-time changes or architectural modifications.
3. **Strong empirical results.** The method improves over all listed baselines on all four datasets, with consistent gains across tasks.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that both the curriculum and its direction contribute to performance.
5. **Low-resource analysis.** The evaluation with 100, 500, and 1,000 labelled examples supports the claim that the method is most useful when labels are scarce.
6. **Generally clear presentation.** The paper is well organized, and the main method and experimental claims are easy to follow.

### Weaknesses and concerns

1. **Limited novelty.** The central idea—gradually increasing augmentation strength—is intuitive and closely related to existing curriculum-learning and augmentation-scheduling approaches. The paper would benefit from a more comprehensive comparison to prior adaptive augmentation or curriculum contrastive-learning methods.
2. **Curriculum specification is somewhat ambiguous.** The text defines a continuous curriculum level but implements discrete availability thresholds. It is unclear whether the probability of selecting an operator changes continuously or whether operators are sampled uniformly once available. These alternatives could produce materially different schedules.
3. **The \(L=0\) definition is formally incomplete.** Since \(c(t)=\min(1,t/L)\) is undefined for \(L=0\), the fixed-mixture case should be explicitly specified as a separate convention.
4. **Baseline tuning may be uneven.** CurCon is selected through a 48-configuration grid search on each validation set, whereas baselines use hyperparameters from their original papers. A fairer comparison would tune all methods under the same validation protocol.
5. **Statistical reporting is incomplete.** Results include standard deviations for the main table, but there are no significance tests or confidence intervals for the average improvements. Given the modest 0.5–1.5 point gains over CERT, significance testing would strengthen the claims.
6. **Limited breadth of evaluation.** The experiments use only four short English classification datasets and one encoder. Testing additional domains, longer texts, multilingual settings, or other encoder sizes would better establish generality.
7. **Some implementation details are underspecified.** The paper should clarify the exact source and quality of back-translation, whether augmentation is applied independently to both views, how empty or very short sentences are handled, and whether the unlabelled pool includes any validation or test text.
8. **Compute and reproducibility details could be stronger.** The reported 12% overhead is useful, but the paper should provide preprocessing cost, total training time, and publicly available code/configurations if possible.

### Soundness

The overall methodology is plausible, and the reported ablations are directionally appropriate. The empirical evidence supports the main claim that a progressively harder augmentation policy can outperform a fixed mixture. However, ambiguities in the schedule, unequal baseline tuning, and the lack of statistical testing prevent the strongest possible assessment. The conclusions are nevertheless broadly consistent with the reported results.

**Score: 79/100**

### Novelty

The combination of intermediate contrastive training with a staged augmentation curriculum is sensible and potentially useful, but the conceptual novelty is moderate. The contribution is primarily a focused adaptation and empirical demonstration rather than a fundamentally new contrastive objective or scheduling principle.

**Score: 70/100**

### Significance

The method addresses an important practical setting and obtains consistent improvements, especially with very limited supervision. The absence of inference cost and the compatibility with existing CERT-style training increase practical value. The significance is somewhat constrained by the small evaluation scope and relatively modest gains over CERT.

**Score: 77/100**

### Clarity

The paper is well structured and communicates the motivation, method, and results effectively. The tables are easy to interpret, and the limitations are appropriately acknowledged. Clarification is needed for the precise operator-sampling schedule, the \(L=0\) case, and experimental fairness, but these issues are repairable.

**Score: 87/100**

## Overall score

\[
\frac{79 + 70 + 77 + 87}{4}
= \frac{313}{4}
= 78.25
\]

**Final average score: 78.25/100**

## Final recommendation

**Accept**

The paper presents a clear and useful method with consistent empirical gains in a relevant low-resource setting. The main concerns involve experimental rigor, precise schedule specification, and limited evaluation breadth, but they do not undermine the central contribution and can be addressed through clarification and additional reporting.