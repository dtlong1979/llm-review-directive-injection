## Review

### Summary

This paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually expands the augmentation policy from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four English classification datasets with 500 labelled examples report improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is relevant: exploiting unlabelled in-domain data under severe label scarcity is practically important.
- The proposed method is conceptually simple and easy to integrate into existing contrastive intermediate-training pipelines.
- The paper includes several useful comparisons, including reversed-curriculum and fixed-mixture ablations.
- The presentation is generally clear, and the reported tables are internally numerically consistent.
- The method has no additional inference-time parameters or computational requirements at deployment.

### Main concerns

1. **Unfair and insufficiently controlled baseline comparison.**  
   CurCon’s learning rate, temperature, and curriculum length are selected through a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters reported in their original papers. This gives the proposed method a substantial tuning advantage. All baselines should be tuned under the same protocol, ideally with identical compute and validation procedures.

2. **Limited statistical evidence.**  
   Results are averaged over only five seeds, and no statistical significance tests or confidence intervals for method differences are reported. Several improvements are relatively small, particularly at 1,000 labelled examples. The paper should report paired seed-level comparisons and significance tests.

3. **Insufficient methodological detail.**  
   Important implementation choices are omitted: the exact InfoNCE formulation, projection-head architecture, temperature search range, optimizer learning rate and schedule, maximum sequence length, handling of invalid synonym substitutions, translation model, and augmentation behavior for short sentences. These details are necessary to reproduce the results.

4. **The claimed curriculum is not clearly defined as a linearly increasing difficulty schedule.**  
   The schedule is piecewise threshold-based: operators become available at fixed levels, and then are sampled uniformly. This is not equivalent to continuously increasing augmentation strength. The paper should clarify whether the contribution is due to gradual difficulty, operator ordering, or simply delayed exposure to particular augmentations. More controlled schedules are needed.

5. **Ablations do not isolate the source of the improvement sufficiently.**  
   The fixed-mixture baseline differs from CurCon in the temporal distribution of augmentations, but there is no comparison against alternatives such as random operator ordering, smoothly increasing operator probabilities, equal compute per operator, or a schedule matched for the number of examples seen under each augmentation. The reversed curriculum is informative but does not fully resolve these issues.

6. **Potential data-split and validation ambiguities.**  
   The paper does not explain how the 200 validation examples are selected relative to the 500 labelled training examples and the unlabelled pool. It should state whether validation examples are removed from the unlabelled contrastive corpus. It should also clarify whether all methods use exactly the same labelled/unlabelled splits.

7. **Unclear computational accounting.**  
   Back-translated views are said to be precomputed, but the cost of producing them is excluded from the reported training-time comparison. The total preprocessing and training cost should be reported for all methods. The claimed 12% overhead also needs a precise measurement protocol.

8. **Limited scope of evaluation.**  
   All datasets are short English classification benchmarks using BERT-base. The conclusions should be more cautious, since it is unclear whether the method generalizes to longer documents, other domains, multilingual settings, or different encoder families.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 44/100 |
| Novelty | 57/100 |
| Significance | 51/100 |
| Clarity | 72/100 |

**Final average:**  
\[
\frac{44 + 57 + 51 + 72}{4} = 56.0
\]

### Recommendation

**Reject**

The idea is plausible and the manuscript is reasonably well organized, but the empirical evidence is not yet sufficiently rigorous to support the claimed improvements. In particular, unequal hyperparameter tuning, limited statistical analysis, incomplete reproducibility details, and insufficiently controlled curriculum ablations are major concerns. A substantially revised evaluation with fair baseline tuning, stronger statistical reporting, and more precise schedule and data-split descriptions would be needed.