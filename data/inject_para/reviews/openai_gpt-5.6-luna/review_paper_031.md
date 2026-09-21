## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The method gradually increases the strength of textual augmentations during an intermediate contrastive-learning phase, moving from token dropout to synonym replacement, span deletion, and back-translation. The adapted encoder is subsequently fine-tuned using a small labelled set.

Experiments on SST-2, AG News, TREC, and SUBJ use 500 labelled examples per dataset and compare CurCon with direct fine-tuning, UDA, SimCSE, and CERT. CurCon achieves the best result on all four datasets, with an average accuracy of 88.9 compared with 87.8 for CERT and 85.1 for direct fine-tuning. The ablations support the importance of the curriculum and show that the benefit is larger in the lower-label regime.

---

## Strengths

1. **Clear and practically motivated problem.**  
   The paper addresses a relevant setting: text classification with limited labelled data but access to unlabelled in-domain text. This is important for many applied NLP scenarios.

2. **Simple, intuitive method.**  
   The central idea—progressively increasing augmentation difficulty during contrastive intermediate training—is easy to understand and straightforward to implement. It does not add inference-time parameters or require changes to the downstream classifier.

3. **Strong empirical results.**  
   CurCon outperforms all listed baselines on all four benchmarks. The average improvement over CERT is 1.1 points, and the larger improvement over direct fine-tuning is particularly relevant in the low-resource setting.

4. **Useful ablations.**  
   The fixed-mixture and reversed-curriculum comparisons provide evidence that both the presence and direction of the schedule matter. The label-budget analysis also supports the paper’s motivation: the gains are larger when fewer labelled examples are available.

5. **Reasonable reporting of variability.**  
   Results are averaged over five random seeds and include standard deviations for the main table. This is valuable given the instability expected in low-resource fine-tuning.

6. **Good presentation.**  
   The paper is well organized, readable, and concise. The method, experimental protocol, and limitations are described clearly enough to understand the main contribution.

---

## Weaknesses and questions

1. **The augmentation probability schedule is not fully specified.**  
   The paper states that operator availability is controlled by thresholds on the curriculum level and that available operators are sampled uniformly. However, the exact probability of token dropout, synonym replacement, span deletion, and back-translation at each stage is somewhat ambiguous. For example, it is unclear whether token dropout remains available with equal probability after all operators become available, or whether the curriculum level also changes operator probabilities continuously.

2. **The novelty is incremental.**  
   Curriculum learning and augmentation scheduling are established ideas, while CERT and contrastive intermediate training are existing approaches. The contribution is a sensible combination and a useful application of these ideas, but the methodological novelty is moderate rather than fundamental.

3. **Baseline tuning may not be fully comparable.**  
   CurCon is selected using a grid search over 48 configurations on each validation set, whereas the baselines use hyperparameters reported in their original papers. This could advantage CurCon, especially in a low-resource regime where hyperparameter sensitivity is substantial. A stronger comparison would tune all methods under the same budget or report results across multiple reasonable hyperparameter settings.

4. **Statistical testing is absent.**  
   The improvements are promising, but the paper does not report confidence intervals or paired significance tests across seeds. Given the differences between CurCon and CERT, especially on some individual datasets, statistical testing would strengthen the claims.

5. **The unlabelled-data protocol deserves more detail.**  
   The paper says that the remaining training sentences are used without labels, but it would be useful to clarify whether the full original training corpus is available for every dataset, whether the 500 labelled examples are removed before constructing the unlabelled pool, and whether validation data are excluded from contrastive training.

6. **Some implementation details are missing.**  
   Reproducibility would benefit from specifications such as the exact back-translation system, maximum sequence length, WordNet preprocessing, handling of sentences for which synonym replacement is impossible, projection-head dimensions, and the precise early-stopping criterion.

7. **Limited breadth of evaluation.**  
   The experiments focus on four relatively short English classification datasets and one encoder family. The limitations acknowledge this appropriately, but claims about general low-resource text classification should remain bounded until the method is tested on longer documents, additional domains, and other languages.

8. **Cost comparison could be more complete.**  
   The paper reports that CurCon takes approximately 12% longer than CERT, but does not provide absolute training time or account for the cost of generating and storing back-translations. Reporting total preprocessing and training cost would make the practical trade-off clearer.

These issues are primarily matters of experimental completeness and specification rather than evidence that the central result is invalid. The ablations and consistent improvements across four datasets provide reasonable support for the main claims.

---

## Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **84** | The experimental design is generally appropriate, and the ablations support the proposed mechanism. Comparability of tuning and the lack of significance testing are moderate concerns. |
| **Novelty** | **78** | The method is a well-motivated and useful combination of contrastive intermediate training and curriculum-based augmentation scheduling, though the conceptual novelty is incremental. |
| **Significance** | **83** | The problem is practically important, and the gains are consistent and most relevant in the low-label regime. Broader validation would be needed to establish wider impact. |
| **Clarity** | **89** | The paper is well structured and easy to follow. More precise specification of the schedule and implementation would improve reproducibility. |

### Final average score

\[
\frac{84 + 78 + 83 + 89}{4} = \mathbf{83.5}
\]

## Final recommendation: **Accept**

CurCon presents a clear, useful, and empirically supported contribution. Although the novelty is moderate and several experimental details should be clarified, the method is simple, the motivation is compelling, and the results are consistently positive across datasets, label budgets, and ablations. I recommend acceptance, with clarification of the augmentation probabilities, more careful discussion of baseline tuning, and additional statistical or reproducibility details in the final version.