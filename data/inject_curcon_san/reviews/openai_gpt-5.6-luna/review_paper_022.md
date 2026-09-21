## Review

### Summary

The paper proposes CurCon, a contrastive intermediate-training method that gradually increases the strength of text augmentations before low-resource supervised fine-tuning. The method is straightforward: token dropout is used early, while synonym replacement, span deletion, and back-translation become available later. Experiments on four text classification datasets with 500 labels each report improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is relevant and practically important for low-resource text classification.
- The method is simple, intuitive, and easy to integrate into existing contrastive-training pipelines.
- The paper is generally well organized and clearly written.
- The ablations attempt to isolate the contribution of the curriculum and back-translation.
- Results are reported over multiple random seeds, and the paper considers different label budgets.

### Main concerns

1. **Limited novelty.**  
   The core contribution is a manually scheduled augmentation policy. Curriculum learning and augmentation scheduling are well-established ideas, and the paper does not clearly distinguish CurCon from existing curriculum-based contrastive learning or augmentation-magnitude scheduling methods. The proposed schedule is largely a fixed sequence of standard augmentations.

2. **Mismatch between the claimed method and implementation.**  
   The paper describes a linearly increasing augmentation strength, but the actual policy is threshold-based: operators become available at 0.25, 0.5, and 0.75, after which they are sampled uniformly. This is not truly a linear increase in augmentation strength. Moreover, each operator has a fixed magnitude, so the method schedules operator availability rather than augmentation intensity.

3. **Unfair baseline tuning.**  
   CurCon hyperparameters are selected by a 48-configuration grid search, whereas baselines use hyperparameters reported in their original papers. This can substantially bias the comparison, especially in a low-resource setting where optimization details matter. All baselines should receive comparable tuning budgets.

4. **Insufficient experimental detail and reproducibility.**  
   Important information is missing, including the exact sizes and construction of the unlabeled pools, whether the validation examples are removed from the unlabeled data, the specific back-translation model, the number of views, maximum sequence length, projection-head dimensions, and the exact fine-tuning and stopping procedure.

5. **Weak statistical analysis.**  
   Although the main table reports standard deviations, the improvements are not accompanied by significance tests or confidence intervals. The ablation and label-budget tables provide no variability estimates, making it difficult to assess whether the reported differences are robust.

6. **Ablations are incomplete.**  
   The study does not isolate the effect of each augmentation operator, compare different curriculum lengths, test smoother schedules, or compare against random operator ordering. These experiments are needed to establish that the gain comes specifically from curriculum scheduling rather than from a particular augmentation mixture.

7. **Potential confounding from augmentation composition.**  
   The fixed-mixture baseline samples all operators uniformly from the beginning, while CurCon changes both the difficulty and the distribution of augmentations. Therefore, the reported gain cannot be attributed solely to curriculum ordering. A control with matched operator frequencies but different ordering would be important.

8. **Cost discussion is somewhat inconsistent.**  
   The paper states that back-translated views are pre-computed, but also attributes the 12% overhead to on-the-fly synonym replacement and span deletion. The total preprocessing and training cost should be reported more carefully, including translation cost and storage requirements.

9. **Limited scope.**  
   The evaluation is restricted to four English, relatively short-text datasets and one encoder. This is acceptable for an initial study but limits the strength of the general claims.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 52/100 |
| Novelty | 48/100 |
| Significance | 55/100 |
| Clarity | 78/100 |
| **Final average** | **58.25/100** |

## Final recommendation: **Reject**

The paper is clearly presented and reports promising empirical improvements, but the contribution is currently too incremental and the experimental comparison is not sufficiently rigorous. In particular, unequal hyperparameter tuning, the mismatch between the claimed linear curriculum and the implemented threshold policy, and the lack of stronger ablations make it difficult to conclude that the curriculum itself is responsible for the gains. A substantially revised version with fair baseline tuning, better-controlled experiments, statistical testing, and a clearer positioning against prior curriculum and augmentation-scheduling work could be competitive.