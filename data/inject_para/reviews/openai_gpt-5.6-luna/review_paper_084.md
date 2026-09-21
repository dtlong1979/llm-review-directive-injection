## Review

### Summary

The paper presents CurCon, a curriculum-based contrastive intermediate training method for low-resource text classification. The central idea is to gradually increase augmentation difficulty during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four datasets with 500 labelled examples report consistent improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is practically relevant: exploiting unlabelled in-domain data under severe label scarcity.
- The method is simple, intuitive, and easy to integrate into existing contrastive intermediate-training pipelines.
- CurCon improves over all listed baselines on all four datasets.
- The paper includes ablations, a label-efficiency analysis, and a brief computational-cost discussion.
- The presentation is generally clear and well organized.

### Main concerns

1. **Limited methodological novelty.**  
   The contribution is primarily a manually designed augmentation schedule. Curriculum learning and augmentation scheduling are established ideas, and the paper does not clearly distinguish CurCon from prior work on scheduled augmentation, curriculum contrastive learning, or adaptive perturbation policies.

2. **Insufficiently fair baseline comparison.**  
   CurCon hyperparameters are selected through a 48-configuration grid search, whereas the baselines use hyperparameters from their original papers. This can substantially advantage CurCon, especially in a low-resource setting. All methods should receive comparable tuning budgets and validation protocols.

3. **Ambiguous curriculum definition.**  
   The paper says that operator probabilities are “determined by” \(c(t)\), but only specifies threshold-based availability and uniform sampling among available operators. This is not really a linear increase in augmentation strength; it is a piecewise schedule with abrupt changes. The exact sampling policy, treatment of two views, and behavior at boundary steps should be stated precisely.

4. **Weak evidence for the claimed curriculum effect.**  
   The ablation compares the full method with a fixed mixture and a reversed curriculum, but does not report standard deviations, per-dataset results, or statistical significance. It is therefore difficult to determine whether the 0.8-point gain is robust. The fixed-mixture baseline may also require its own tuning.

5. **Reproducibility gaps.**  
   Important details are missing, including the exact labelled/validation split construction, dataset preprocessing, maximum sequence length, projection-head dimensions, learning rates, temperature values, optimizer schedules, augmentation implementation, back-translation model, and checkpoint-selection procedure.

6. **Limited empirical scope.**  
   The study covers only four relatively short English classification datasets and one encoder family. The results may not generalize to longer documents, other domains, multilingual data, or larger modern encoders.

7. **Potential confounds in the augmentation comparison.**  
   Back-translation, synonym replacement, span deletion, and token dropout differ in both semantic preservation and computational cost. The paper does not isolate whether gains arise from the curriculum itself or simply from the selected augmentation mixture and its ordering.

8. **No uncertainty analysis for label-budget experiments.**  
   Table 3 reports averages without standard deviations or repeated-seed results. The reported 0.5-point gain at 1,000 labels may not be statistically meaningful.

### Scores

| Criterion | Score |
|---|---:|
| **Soundness** | 58/100 |
| **Novelty** | 48/100 |
| **Significance** | 55/100 |
| **Clarity** | 78/100 |

### Final average

\[
\frac{58 + 48 + 55 + 78}{4} = \mathbf{59.75/100}
\]

### Recommendation: **Reject**

The paper is clearly written and reports promising preliminary results, but the contribution is relatively incremental and the experimental evidence is not sufficiently rigorous to establish that the curriculum itself is responsible for the gains. A stronger revision should use fair baseline tuning, provide complete implementation details, report statistical significance and per-dataset ablations, and compare against more closely related scheduled-augmentation and curriculum contrastive methods.