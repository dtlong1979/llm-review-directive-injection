## Review

### Summary

This paper proposes CurCon, a contrastive intermediate-training method that gradually increases augmentation strength during training. The method is evaluated on four English text-classification datasets in a 500-label low-resource setting, with comparisons against fine-tuning, UDA, SimCSE, and CERT. The reported results show consistent but modest gains over CERT, with larger improvements in the lower-label regime.

### Strengths

- The problem is practically relevant: adapting pretrained encoders with limited labelled data.
- The method is conceptually simple and potentially easy to implement.
- The evaluation includes multiple datasets, several baselines, an ablation, and different labelled-data regimes.
- The paper is generally well organized and readable.
- The reported aggregate numbers are internally consistent; for example, the averages in Table 1 match the per-dataset results.

### Main concerns

1. **Unfair hyperparameter selection across methods.**  
   CurCon is tuned using a 48-configuration grid on each validation set, whereas the baselines use hyperparameters from their original papers. This substantially favors the proposed method, particularly in a low-resource setting where optimization choices can have a large effect. All methods should receive comparable tuning budgets, ideally with repeated validation splits or nested evaluation.

2. **The curriculum is underspecified and does not clearly implement the claimed linear schedule.**  
   The method defines thresholds at 0.25, 0.5, and 0.75 and samples uniformly from the currently available operators. Thus, the policy changes in discrete steps rather than increasing augmentation strength linearly. The paper does not specify whether the two views use independently sampled operators, whether operators can be composed, or how augmentation probabilities vary within each interval. These details are important for reproducibility and for interpreting the method.

3. **Insufficient experimental detail.**  
   The learning-rate ranges, temperature values, curriculum-length candidates, encoder and tokenizer details, data preprocessing, augmentation implementation, translation model, and random seed values are not provided. The paper also does not clarify how the 200-example validation sets are constructed relative to the 500 labelled examples and the standard training sets.

4. **Limited statistical analysis.**  
   Only five seeds are used, and the ablation tables report no standard deviations or significance tests. Several reported gains are modest—for example, 0.5 points at 1,000 labels—so it is unclear whether these differences are statistically reliable.

5. **Baseline implementation and comparability are unclear.**  
   UDA, SimCSE, and CERT have different computational and tuning requirements, but the paper does not establish that they were implemented faithfully or tuned comparably. In particular, the claimed 12% additional cost over CERT is difficult to interpret because CERT itself uses back-translation, and the paper does not report total preprocessing and training costs.

6. **Novelty is somewhat incremental.**  
   The central idea—gradually increasing augmentation difficulty—is plausible, but the manuscript does not sufficiently distinguish CurCon from prior curriculum-based augmentation methods or adaptive contrastive-learning schedules. The contribution would be stronger with a more comprehensive comparison to fixed-strength schedules, smooth probability schedules, alternative orderings, and other curriculum formulations.

7. **Potentially overstrong conclusions.**  
   The results support improvements on the four selected English datasets, but they do not yet establish broad effectiveness across domains, encoders, or augmentation resources. The conclusions should be more cautious given the small number of datasets and the limited statistical analysis.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 45/100 |
| Novelty | 55/100 |
| Significance | 50/100 |
| Clarity | 72/100 |
| **Final average** | **55.5/100** |

### Recommendation

**Reject**

The paper is clearly written and presents a reasonable idea, but the current evidence is not sufficiently rigorous to support acceptance. The most important revisions would be fair and equally tuned baselines, a precise specification of the curriculum and augmentation sampling procedure, complete implementation details, and stronger statistical validation.