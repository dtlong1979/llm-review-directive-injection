## Review

### Summary

The paper proposes CurCon, a contrastive intermediate-training method that gradually increases the strength of text augmentations before low-resource fine-tuning. The idea is simple and potentially useful, and the reported results show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. However, the experimental evidence is not yet strong enough to establish that the curriculum itself is responsible for the gains. Several methodological details are underspecified, and the comparison is potentially unfair because CurCon receives extensive per-dataset hyperparameter tuning while baselines use settings from their original papers.

### Strengths

- The problem is important and relevant to low-resource classification.
- The method is easy to understand and does not add inference-time cost.
- CurCon improves over CERT on all four reported datasets.
- The paper includes an ablation comparing a curriculum against a fixed augmentation mixture and a reversed curriculum.
- The manuscript is generally well organized and readable.

### Main concerns

1. **Potentially unfair baseline tuning.**  
   CurCon is tuned over 48 configurations separately for each dataset, whereas the baselines use hyperparameters from their original papers. This can substantially favor CurCon, particularly in a low-resource setting.

2. **Insufficient statistical evidence.**  
   Although the main table reports five-seed standard deviations, the ablation and label-count experiments do not report variance or significance tests. The claimed 0.8-point curriculum improvement may not be statistically reliable.

3. **The curriculum is only partially specified.**  
   The probability distribution over augmentations is ambiguous. It is unclear whether “available” operators are sampled uniformly, whether operator strength changes continuously, and how the schedule behaves at the threshold boundaries. The stated “linear” curriculum is effectively a sequence of abrupt operator additions rather than a smoothly increasing augmentation strength.

4. **Limited evidence for generality.**  
   The evaluation covers only four short English classification datasets and one encoder. The contribution may be dataset- or augmentation-specific.

5. **Ablation coverage is incomplete.**  
   A stronger evaluation would compare multiple schedule shapes, matched augmentation budgets, different curriculum lengths, and fixed policies with equivalent expected augmentation strength. It would also report per-dataset ablation results rather than only averages.

6. **Reproducibility gaps.**  
   Important details are missing, including the exact back-translation system, WordNet preprocessing, handling of failed or invalid augmentations, data-split construction, learning-rate ranges, and the method used to select the 200 validation examples.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 57/100 |
| Novelty | 61/100 |
| Significance | 58/100 |
| Clarity | 78/100 |

### Final average

\[
\frac{57 + 61 + 58 + 78}{4} = 63.5
\]

## Final recommendation: **Reject**

The idea is reasonable and the reported improvements are promising, but the current evidence does not convincingly isolate the benefit of the curriculum from hyperparameter tuning and augmentation-policy differences. A revised submission with fair baseline tuning, stronger statistical analysis, fuller implementation details, and more comprehensive schedule ablations could become publishable.