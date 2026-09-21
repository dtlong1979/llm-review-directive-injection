## Review

### Summary

The paper proposes CurCon, an intermediate contrastive-training method that gradually increases text augmentation strength during training. The method is simple and well motivated, and the reported results show consistent improvements over fine-tuning, UDA, SimCSE, and CERT in a 500-label setting. However, the experimental protocol and method specification have important ambiguities, and the evidence is not yet sufficient to establish that the curriculum itself is responsible for the gains.

### Strengths

- Addresses an practically important low-resource classification setting.
- The proposed idea is intuitive and easy to implement.
- CurCon improves over all listed baselines across all four datasets.
- Includes useful ablations for fixed mixtures, reversed curricula, and removal of back-translation.
- Reports performance across multiple label budgets and random seeds.
- The method adds no inference-time parameters or computational cost.

### Main concerns

1. **Baseline comparison is potentially unfair.**  
   CurCon is tuned using a 48-configuration grid search separately on each validation set, whereas the baselines use hyperparameters from their original papers. This gives CurCon a substantially different tuning budget and may inflate the reported improvement. All methods should receive comparable tuning procedures, or the paper should report results using matched hyperparameter searches.

2. **The curriculum is underspecified.**  
   The paper defines thresholds at which augmentations become “available,” but does not specify the exact sampling probabilities over time beyond saying that available operators are sampled uniformly. It is unclear whether the schedule changes augmentation severity, operator probabilities, or both. The statement that \(L=0\) yields a fixed mixture is also mathematically undefined because \(c(t)=t/L\).

3. **Several implementation details needed for reproducibility are missing.**  
   The paper does not specify the back-translation model, WordNet preprocessing, tokenization behavior after deletion, sentence length handling, optimizer settings, temperature search range, projection-head dimensions, or the exact number and composition of unlabeled examples.

4. **Potential data-split ambiguity.**  
   The remaining training sentences are used as unlabeled data, while a 200-example validation set is also introduced. It is not clear whether validation examples are excluded from the unlabeled contrastive corpus. This must be clarified to rule out unintended validation leakage.

5. **Insufficient statistical analysis.**  
   Standard deviations are reported for the main table, but not for the ablation or label-budget experiments. No significance tests or per-seed results are provided. Given the relatively small gains over CERT, especially at 1,000 labels, statistical significance should be established.

6. **Limited assessment of the source of improvement.**  
   The comparison with the fixed mixture is useful, but the full method changes both the ordering and the time-dependent distribution of augmentations. Additional controls are needed, such as:
   - a fixed mixture matched to the average augmentation distribution of CurCon;
   - a curriculum with the same number of updates per operator;
   - schedules based on augmentation severity rather than operator availability;
   - multiple curriculum lengths and nonlinear schedules.

7. **Novelty is moderate rather than substantial.**  
   Scheduling augmentation difficulty is a natural application of curriculum learning, and related ideas have been explored in augmentation scheduling. The paper would need a more comprehensive comparison with prior curriculum-based augmentation methods and a clearer theoretical or empirical explanation of what is distinctive about CurCon.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 47/100 |
| Novelty | 54/100 |
| Significance | 55/100 |
| Clarity | 78/100 |

### Final average

\[
\frac{47 + 54 + 55 + 78}{4} = 58.5
\]

**Final average score: 58.5/100**

## Recommendation: **Reject**

The paper is clearly written and presents a plausible, potentially useful method, but the current empirical evidence does not adequately support the central claim that the curriculum schedule itself produces the reported gains. A revised submission should use matched baseline tuning, fully specify the schedule and data splits, report uncertainty for all experiments, and include stronger controls isolating curriculum effects.