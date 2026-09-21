## Review

### Summary

This paper proposes CurCon, a contrastive intermediate-training method that gradually increases the strength of text augmentations before low-resource supervised fine-tuning. The method is evaluated on four English classification datasets with 500 labeled examples per dataset and compared against fine-tuning, UDA, SimCSE, and CERT. The reported results show consistent improvements over all baselines, with an average gain of 1.1 accuracy points over CERT.

### Strengths

- The problem is important and practically relevant: adapting pretrained encoders with limited labeled data.
- The proposed method is simple and compatible with existing contrastive pretraining pipelines.
- The experiments include multiple datasets, several relevant baselines, multiple random seeds, and label-budget analysis.
- The ablation results support the claim that a curriculum can be beneficial.
- The paper is generally well organized and easy to follow.

### Concerns

#### Soundness

The main experimental conclusions are plausible, but several details limit confidence in the results:

1. **The curriculum is not actually linearly scheduled in the described implementation.**  
   Although \(c(t)\) increases linearly, augmentations become available only at thresholds 0.25, 0.5, and 0.75. The resulting policy is piecewise constant rather than linearly increasing in strength. Moreover, the exact probability distribution over available operators is not fully specified.

2. **The \(L=0\) definition is mathematically undefined.**  
   The formula \(c(t)=\min(1,t/L)\) cannot be evaluated for \(L=0\), despite the claim that this setting corresponds to the fixed-mixture baseline. A special-case definition is needed.

3. **Baseline tuning appears potentially unfair.**  
   CurCon is selected using a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters reported in their original papers. This can inflate the relative advantage of CurCon, particularly in a low-resource setting.

4. **Statistical testing is absent.**  
   Results are averaged over five seeds, but there are no confidence intervals, paired significance tests, or per-seed results. Several improvements, especially on some datasets, may be comparable to run-to-run variation.

5. **Reproducibility details are insufficient.**  
   Important details such as the exact back-translation system, preprocessing, maximum sequence length, augmentation application to the two views, sampling strategy, and data deduplication are omitted.

6. **The experimental scope is limited.**  
   All datasets are English and relatively short, and only BERT-base is evaluated. This makes the broad claims about low-resource text classification somewhat stronger than the evidence supports.

The ablations are useful, but the fixed-mixture comparison and the “reversed curriculum” comparison should ideally be matched more carefully for augmentation frequency and computational cost.

#### Novelty

The central idea—progressively increasing augmentation difficulty during contrastive learning—is reasonable and potentially useful, but it is an incremental combination of existing components: CERT-style intermediate contrastive training, standard text augmentations, and curriculum learning. The paper would benefit from a stronger comparison to prior work on augmentation scheduling and curriculum-based contrastive learning. The novelty is therefore moderate rather than substantial.

#### Significance

The reported gains are consistent across four datasets, and the larger improvement under smaller label budgets is practically relevant. However, the absolute improvement over CERT is modest—1.1 average accuracy points—and the experimental limitations make it difficult to determine whether the gains arise from the curriculum itself or from additional tuning and augmentation-policy choices. The method has potential value, but the current evidence does not establish a major advance.

#### Clarity

The paper is clearly structured, and the motivation, pipeline, and main results are easy to understand. However, the augmentation probabilities and curriculum mechanics need a more precise mathematical specification. The handling of \(L=0\), the relationship between “augmentation strength” and operator availability, and the exact experimental protocol should be clarified.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 59/100 |
| Novelty | 57/100 |
| Significance | 62/100 |
| Clarity | 78/100 |
| **Final average** | **64.0/100** |

## Final recommendation

**Reject**

The idea is promising and the presentation is clear, but the current submission has insufficient experimental rigor for acceptance. In particular, unequal baseline tuning, underspecified curriculum probabilities, lack of statistical testing, and limited reproducibility details weaken the central claim that the curriculum itself produces the reported gains.