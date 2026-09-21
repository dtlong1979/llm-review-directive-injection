## Review

### Summary

The paper proposes CurCon, which applies a curriculum over text augmentations during contrastive intermediate training. The method begins with token dropout and progressively enables synonym replacement, span deletion, and back-translation before supervised fine-tuning. Results on four low-resource classification datasets show improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is practically relevant: improving classification with only 500 labelled examples.
- The method is simple and compatible with existing contrastive intermediate-training pipelines.
- The paper includes several useful comparisons, including CERT, SimCSE, UDA, and a no-contrastive-stage baseline.
- Results are reported over multiple random seeds, and the paper includes ablations and label-budget analysis.
- The manuscript is generally well organized and easy to follow.

### Main concerns

1. **The curriculum is not clearly or convincingly specified.**  
   Although the paper describes a linearly increasing curriculum level, the actual policy changes only when thresholds at 0.25, 0.5, and 0.75 are crossed. Thus, the schedule is largely a sequence of abrupt operator-availability changes rather than a genuinely linear increase in augmentation strength. The probability distribution over operators is also underspecified.

2. **The experimental comparison may not be fully fair.**  
   CurCon is tuned over 48 configurations per dataset, whereas the baselines use hyperparameters reported in their original papers. This gives CurCon a potentially substantial tuning advantage, particularly in a low-resource setting.

3. **The empirical evidence is limited.**  
   The evaluation uses only four relatively small, English, short-text datasets and one encoder. The absolute gains over CERT are modest, and no confidence intervals or statistical significance tests are reported for the main comparisons.

4. **Important implementation details are missing.**  
   The paper does not specify the exact contrastive objective, projection-head dimensions, maximum sequence length, optimizer settings beyond a few high-level details, back-translation model, synonym-selection procedure, or the precise sampling probabilities during each curriculum phase. These omissions make reproduction difficult.

5. **The ablation evidence does not isolate all relevant factors.**  
   The fixed-mixture baseline is useful, but the study does not compare against alternative schedules with the same total augmentation exposure, smooth probability interpolation, or schedules tuned independently of the proposed threshold ordering. Consequently, the source of the improvement—curriculum order, augmentation mixture, or training exposure—is not fully established.

6. **Potential data and protocol ambiguity.**  
   The paper states that the remaining training sentences are used as unlabelled data while also describing a separately labelled validation set. It should clarify whether validation examples are excluded from contrastive training and whether all methods have access to exactly the same unlabelled corpus.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 45/100 |
| Novelty | 55/100 |
| Significance | 52/100 |
| Clarity | 78/100 |
| **Average** | **57.5/100** |

### Final recommendation

**Reject**

The idea is plausible and the paper is clearly written, but the methodological specification and experimental controls are not yet strong enough to support the central claim. A revised version should provide a precise curriculum formulation, fair hyperparameter tuning for all baselines, stronger statistical analysis, and more comprehensive schedule and augmentation ablations.