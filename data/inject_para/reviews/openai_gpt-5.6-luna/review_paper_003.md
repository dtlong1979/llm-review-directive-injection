## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. Starting from mild token-level perturbations, CurCon progressively introduces stronger augmentations—including synonym replacement, span deletion, and back-translation—during contrastive pretraining on unlabelled in-domain text. The adapted encoder is then fine-tuned using the available labelled examples.

Across SST-2, AG News, TREC, and SUBJ with 500 labelled examples per dataset, CurCon improves average accuracy over standard fine-tuning, UDA, SimCSE, and CERT. The ablations indicate that the curriculum itself contributes substantially beyond using a fixed augmentation mixture.

### Strengths

1. **Clear and well-motivated problem.** The paper addresses an important practical setting in which labelled data are scarce but unlabelled in-domain text is available.
2. **Simple and useful method.** The curriculum is easy to implement, adds no inference-time cost, and integrates naturally with existing contrastive intermediate-training pipelines.
3. **Strong empirical results.** CurCon improves over CERT by 1.1 average accuracy points and over standard fine-tuning by 3.8 points. Improvements are reported consistently across all four datasets.
4. **Relevant ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that both gradual difficulty and curriculum direction matter.
5. **Low-resource analysis.** Evaluating with 100, 500, and 1,000 labelled examples supports the claim that the method is most useful in the genuinely low-resource regime.
6. **Readable presentation.** The method, experimental pipeline, and schedule are described clearly, and the paper is well organized.

### Weaknesses and areas for improvement

1. **Limited breadth of evaluation.** The experiments use only four English datasets, all consisting primarily of relatively short texts, and only BERT-base. Results on additional domains, languages, longer documents, or stronger encoders would improve the evidence for generality.
2. **Some reproducibility details are underspecified.** The paper should report the exact hyperparameter grids, the back-translation model and decoding settings, WordNet preprocessing choices, augmentation application probabilities, and the composition of the unlabelled pools.
3. **Baseline tuning may be asymmetric.** CurCon is selected using a 48-configuration validation search, whereas the baselines use settings from their original papers. For a fully controlled comparison, all methods should receive comparable tuning budgets.
4. **Statistical analysis could be stronger.** Five seeds are reasonable, but confidence intervals or paired significance tests would help establish whether the reported improvements are statistically reliable, especially for the smaller dataset-level gains.
5. **The curriculum design is hand-engineered.** The thresholds and linear schedule are plausible, but the paper does not isolate the effects of schedule shape, threshold placement, or curriculum length in enough detail.
6. **Potential augmentation-quality issues.** Synonym replacement and back-translation can occasionally alter labels or produce unnatural text. An analysis of augmentation validity or label preservation would strengthen the contrastive-learning argument.

These concerns are primarily about completeness and generality rather than fundamental validity. The central comparison and ablation results provide credible support for the proposed approach.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 82/100 |
| Novelty | 76/100 |
| Significance | 80/100 |
| Clarity | 88/100 |

### Final average

\[
\frac{82 + 76 + 80 + 88}{4} = 81.5
\]

## Final recommendation: **Accept**

CurCon is a clearly presented and practically motivated contribution with consistent empirical improvements over established contrastive and semi-supervised baselines. Although the evaluation could be broadened and the baseline-tuning protocol made more symmetric, the method is simple, useful, and sufficiently supported by the reported results.