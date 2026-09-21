## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The method gradually increases augmentation strength during unsupervised contrastive training, moving from token dropout toward synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations suggest that the curriculum itself contributes beyond the use of contrastive learning and augmentation.

### Strengths

- The paper addresses an important and practically relevant setting: text classification with very limited labelled data.
- The proposed method is simple, modular, and easy to integrate into existing CERT-style pipelines.
- The curriculum has a clear motivation: gradually increasing augmentation difficulty may stabilize representation learning before introducing more challenging positive pairs.
- The empirical results are consistent across all four datasets, with CurCon achieving the best reported result on each.
- The ablation study directly evaluates the curriculum, the reverse curriculum, and the role of back-translation.
- The analysis across different labelled-data regimes supports the claim that the method is especially useful in low-resource settings.
- The method adds no inference-time parameters or computational overhead at deployment.

### Weaknesses and suggestions

1. **Baseline tuning fairness.**  
   The paper states that CurCon is selected using a grid search on each validation set, whereas baselines use hyperparameters reported in their original papers. This may advantage CurCon, especially in a low-resource setting. A stronger comparison would tune all methods under the same validation protocol or report results under both original and re-tuned settings.

2. **Limited statistical analysis.**  
   Results are averaged over five random seeds, but the paper does not report significance tests or confidence intervals for the method comparisons. Given that some gains are relatively small, especially at 1,000 labelled examples, paired seed-level comparisons would make the conclusions more convincing.

3. **Curriculum specification could be clearer.**  
   The definition of “probability of applying each operator” and the interaction between operator availability and the sampling of views could be stated more precisely. In particular, it would help to specify whether token dropout remains equally likely after the other operators become available, and whether the two views are independently augmented.

4. **Scope of evaluation.**  
   The experiments are limited to four English datasets and BERT-base. This is reasonable for an initial study, but evaluation on longer documents, additional domains, or multilingual data would better establish generality.

5. **Compute and preprocessing details.**  
   The paper would benefit from reporting the number of unlabelled examples, the exact back-translation model, and whether the same precomputed translations are reused across seeds. These details are relevant for reproducibility and for interpreting the stated 12% computational overhead.

6. **Ablation granularity.**  
   The ablation demonstrates that the curriculum helps, but does not isolate the contribution of each individual augmentation or test alternative schedules beyond the reversed schedule. Comparing linear, cosine, stepwise, and adaptive schedules would provide a more complete analysis.

These are mostly presentation, evaluation-design, and reproducibility improvements rather than fundamental flaws. The central method is clearly described, and the reported evidence consistently supports the main claim.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 84/100 |
| Novelty | 79/100 |
| Significance | 83/100 |
| Clarity | 88/100 |

### Final average

\[
\frac{84 + 79 + 83 + 88}{4} = 83.5
\]

**Final average score: 83.5/100**

## Recommendation: **Accept**

The paper presents a coherent and practically useful method with a clear curriculum-learning motivation and consistent empirical improvements across multiple low-resource classification benchmarks. While stronger baseline tuning, statistical testing, and broader evaluation would improve the work, the current evidence is sufficient to support acceptance.